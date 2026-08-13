#!/usr/bin/env python3
"""
merge_score.py — k-way merge the per-shard counts, score with logDice, write SQLite.

MEMORY IS THE WHOLE DESIGN HERE. This runs at the END of a 9-hour unsupervised job, so
an OOM at this stage costs the entire night. Two decisions follow from that:

  * The merge is a STREAMING k-way merge (heapq.merge over pre-sorted per-shard files),
    so peak memory is one line per open shard rather than the whole table.
  * The join against the marginals happens IN SQLITE, not in Python dicts. The obvious
    implementation holds both marginal tables in memory; at this corpus size that is
    tens of millions of string keys, several GB per table, on an 11 GB box that is also
    running grafana, prometheus and a ZFS ARC. SQLite does the same join on disk with a
    bounded page cache. It is slower and it finishes.

WHAT IS AND ISN'T FILTERED
--------------------------
The database is written essentially UNFILTERED (pair count >= MIN_PAIR, default 3).
The recipe says to apply freq >= 20 and logDice >= 3.0 here. Don't: those floors were
tuned against DWDS's multi-billion-token corpus, and at this corpus size they are wrong
by an unknown factor in an unknown direction. Baking them in means re-running the night
to change them. tools/wortprofil_db.py applies them at query time instead, with the same
B1-intersection logic as tools/wortprofil.py, where retuning costs a second.

    logDice(a,b) = 14 + log2( 2*f(a,b) / (f(a) + f(b)) )

Case is aggregated OUT of the score and reported in its own column: 'in die Wohnung' and
'in der Wohnung' are one collocation with two meanings, so they share a frequency and
are distinguished by a column rather than split into two half-strength rows.
"""

import glob
import gzip
import heapq
import json
import math
import os
import sqlite3
import sys
import time

SEP = "\t"
MIN_PAIR = int(os.environ.get("MIN_PAIR", "3"))


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def rows_of(path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            key, _, cnt = line.rstrip("\n").rpartition(SEP)
            yield key, int(cnt)


def merged(paths):
    """Stream (key, summed_count) over sorted per-shard files. Bounded memory."""
    cur_key, total = None, 0
    for key, cnt in heapq.merge(*(rows_of(p) for p in paths), key=lambda kv: kv[0]):
        if key != cur_key:
            if cur_key is not None:
                yield cur_key, total
            cur_key, total = key, 0
        total += cnt
    if cur_key is not None:
        yield cur_key, total


def load_marginal(db, table, paths, label):
    """Marginals are logDice's denominator, so they are never pruned. Straight to disk."""
    t0, n = time.time(), 0

    def gen():
        nonlocal n
        for key, cnt in merged(paths):
            rel, _, lemma = key.partition(SEP)
            n += 1
            yield rel, lemma, cnt

    db.executemany(f"INSERT INTO {table} VALUES (?,?,?)", gen())
    db.commit()
    log(f"  {label}: {n:,} keys in {time.time()-t0:.0f}s")
    return n


def load_pairs(db, paths):
    """Stream pairs, collapsing the case column into a frequency + a dominant case.
    MIN_PAIR is applied here, which is what keeps the staging table to a size SQLite
    can index comfortably."""
    t0, seen, kept = time.time(), 0, 0

    def gen():
        nonlocal seen, kept
        cur, by_case = None, {}

        def emit(cur, by_case):
            f_ab = sum(by_case.values())
            if f_ab < MIN_PAIR:
                return None
            case = max(by_case, key=lambda c: (by_case[c], c))
            return cur[0], cur[1], cur[2], f_ab, case

        for key, cnt in merged(paths):
            seen += 1
            rel, head, colloc, case = key.split(SEP)
            gk = (rel, head, colloc)
            if gk != cur:
                if cur is not None:
                    row = emit(cur, by_case)
                    if row:
                        kept += 1
                        yield row
                cur, by_case = gk, {}
            by_case[case] = by_case.get(case, 0) + cnt
            if seen % 20_000_000 == 0:
                log(f"  ...{seen:,} pair-rows read, {kept:,} kept, {time.time()-t0:.0f}s")
        if cur is not None:
            row = emit(cur, by_case)
            if row:
                kept += 1
                yield row

    db.executemany("INSERT INTO pair_stage VALUES (?,?,?,?,?)", gen())
    db.commit()
    log(f"  pairs: {seen:,} distinct read, {kept:,} kept (>= {MIN_PAIR}) "
        f"in {time.time()-t0:.0f}s")
    return seen, kept


def main():
    counts = sys.argv[1] if len(sys.argv) > 1 else "/work/counts"
    outdb = sys.argv[2] if len(sys.argv) > 2 else "/work/merged/wp.db"
    os.makedirs(os.path.dirname(outdb), exist_ok=True)

    # Drive the file list off the .done markers, NOT off globbing each family
    # separately. parse_shard.py writes pairs -> hm -> cm -> .done, so a worker killed
    # mid-write leaves a complete pairs file with no marginals. Globbing independently
    # would then either drop those rows silently (inner join finds no marginal) or,
    # worse, keep marginals whose pairs are missing — which inflates f(a)/f(b) against
    # f(a,b) and pushes every logDice for that shard's headwords silently DOWN.
    # .done is the only atomic completion signal, so it decides.
    names = [os.path.basename(d)[:-len(".done")]
             for d in sorted(glob.glob(os.path.join(counts, "*.done")))]
    if not names:
        print("no completed shards found — did the parse phase run?", file=sys.stderr)
        return 1
    pair_files = [os.path.join(counts, n + ".pairs.tsv.gz") for n in names]
    hm_files = [os.path.join(counts, n + ".hm.tsv.gz") for n in names]
    cm_files = [os.path.join(counts, n + ".cm.tsv.gz") for n in names]
    missing = [p for p in pair_files + hm_files + cm_files if not os.path.exists(p)]
    if missing:
        print(f"shard marked done but output missing ({len(missing)} files, e.g. "
              f"{missing[:3]}). Delete those shards' .done markers and re-run the "
              f"parse to regenerate them.", file=sys.stderr)
        return 1
    log(f"merging {len(names)} completed shards, MIN_PAIR={MIN_PAIR}")

    tmpdb = outdb + ".tmp"
    for stale in (tmpdb, tmpdb + "-journal"):
        if os.path.exists(stale):
            os.remove(stale)
    db = sqlite3.connect(tmpdb)
    db.executescript("""
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;
        PRAGMA cache_size = -262144;         -- 256 MB, deliberately modest
        PRAGMA temp_store = FILE;
        CREATE TABLE pair_stage (rel TEXT, head TEXT, colloc TEXT,
                                 freq INTEGER, case_ TEXT);
        CREATE TABLE hm (rel TEXT, lemma TEXT, f INTEGER);
        CREATE TABLE cm (rel TEXT, lemma TEXT, f INTEGER);
    """)

    t0 = time.time()
    seen, kept = load_pairs(db, pair_files)
    load_marginal(db, "hm", hm_files, "headword marginals")
    load_marginal(db, "cm", cm_files, "collocate marginals")

    log("indexing marginals...")
    db.executescript("CREATE UNIQUE INDEX ix_hm ON hm(rel, lemma);"
                     "CREATE UNIQUE INDEX ix_cm ON cm(rel, lemma);")

    # SQLite's log2() needs SQLITE_ENABLE_MATH_FUNCTIONS, which the stdlib build may
    # not have. Registering it from Python is portable and fast enough.
    db.create_function("logdice", 3,
                       lambda f_ab, f_a, f_b: round(14 + math.log2(2 * f_ab / (f_a + f_b)), 4),
                       deterministic=True)

    log("joining + scoring...")
    db.executescript("""
        CREATE TABLE colloc AS
        SELECT p.head                        AS headword,
               p.rel                         AS relation,
               p.colloc                      AS collocate,
               logdice(p.freq, h.f, c.f)     AS logdice,
               p.freq                        AS freq,
               p.case_                       AS case_
        FROM pair_stage p
        JOIN hm h ON h.rel = p.rel AND h.lemma = p.head
        JOIN cm c ON c.rel = p.rel AND c.lemma = p.colloc;
    """)
    written = db.execute("SELECT count(*) FROM colloc").fetchone()[0]

    log(f"indexing {written:,} scored rows...")
    db.executescript("""
        CREATE INDEX idx_head ON colloc(headword);
        CREATE INDEX idx_head_rel ON colloc(headword, relation);
        DROP TABLE pair_stage;
        CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT);
    """)

    shard_meta = []
    for p in sorted(glob.glob(os.path.join(counts, "*.done"))):
        try:
            with open(p) as f:
                shard_meta.append(json.load(f))
        except Exception:
            pass
    info = {
        "shards_parsed": len(shard_meta),
        "sentences": sum(m["sentences"] for m in shard_meta),
        "tokens": sum(m["tokens"] for m in shard_meta),
        "triples_extracted": sum(m["rows"] for m in shard_meta),
        "distinct_pairs_before_prune": seen,
        "rows_written": written,
        "min_pair_count": MIN_PAIR,
        "corpus": "OPUS OpenSubtitles de v2024",
        "model": "de_core_news_sm 3.8.0 / spaCy 3.8.15",
        "built": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    db.executemany("INSERT OR REPLACE INTO meta VALUES (?,?)",
                   [(k, str(v)) for k, v in info.items()])
    db.commit()
    # VACUUM is cosmetic (it reclaims the dropped staging table). Letting it raise
    # would skip the rename below and strand a finished database in wp.db.tmp while
    # the driver reports MERGE FAILED — a whole morning lost to a space optimisation.
    try:
        log("VACUUM...")
        db.execute("VACUUM")
    except Exception as e:
        log(f"VACUUM failed ({e}) — keeping the unvacuumed database, it is fully usable")
    db.close()
    os.replace(tmpdb, outdb)
    print(json.dumps(info, indent=2))
    log(f"wrote {outdb} in {(time.time()-t0)/60:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())

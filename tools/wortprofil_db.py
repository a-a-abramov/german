#!/usr/bin/env python3
"""
wortprofil_db.py — query the OpenSubtitles-derived Wortprofil built by tools/opus/.

Same output as wortprofil.py, same relation names, same B1 intersection, same two
floors — but from a local SQLite database instead of a hand-saved DWDS page, so the
text-writer's Step 2b stops needing a browser.

    python3 tools/wortprofil_db.py Wohnung
    python3 tools/wortprofil_db.py Wohnung Tasse Schrank --tsv
    python3 tools/wortprofil_db.py Wohnung --min-freq 40 --min-dice 4 --top 15
    python3 tools/wortprofil_db.py Wohnung --all          # skip the B1 filter

THE FLOORS ARE NOT THE DWDS FLOORS. freq >= 20 / logDice >= 3.0 were tuned against a
multi-billion-token corpus. This database is built from ~10^8 tokens of film dialogue,
so retune: --min-freq scales roughly with corpus size, --min-dice does not. The database
is stored unfiltered (down to freq 3) precisely so you can move these without a rebuild.
Start by running with --all --min-freq 5 on a word you know and see where the junk
begins.

CASE is a column this database has and DWDS does not (guide §1.4). For prepositional
groups it shows the dominant case of the noun in the group, which is what separates
'in die Wohnung' (Akk., direction) from 'in der Wohnung' (Dat., location).
"""

import argparse
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import WORTPROFIL_DB as DEFAULT_DB              # noqa: E402
from wortprofil import RELATION_PATTERNS, in_b1, load_b1   # noqa: E402

CASE_DE = {"Nom": "Nom.", "Acc": "Akk.", "Dat": "Dat.", "Gen": "Gen."}


def chunk_of(headword, rel, collocate):
    return RELATION_PATTERNS.get(rel, "{L} … {c}").format(L=headword, c=collocate)


def fetch(db, headword, args):
    """The --relations filter belongs here, not in the renderer: applied downstream it
    would silently do nothing in --tsv mode."""
    q = ["SELECT relation, collocate, logdice, freq, case_ FROM colloc "
         "WHERE headword = ? AND freq >= ? AND logdice >= ?"]
    params = [headword, args.min_freq, args.min_dice]
    if args.relations:
        q.append("AND (" + " OR ".join("relation LIKE ?" for _ in args.relations) + ")")
        params += [f"%{r}%" for r in args.relations]
    q.append("ORDER BY relation, logdice DESC")
    return db.execute(" ".join(q), params).fetchall()


def render_md(headword, rows, b1, args):
    out = [f"## {headword}", "",
           f"*Filter: Freq ≥ {args.min_freq}, logDice ≥ {args.min_dice}"
           + ("" if args.all else ", B1 lemmas only")
           + f" · source: OpenSubtitles de v2024*", ""]
    by_rel = {}
    for rel, colloc, ld, freq, case in rows:
        if not args.all and not in_b1(colloc, b1):
            continue
        by_rel.setdefault(rel, []).append((colloc, ld, freq, case))

    if not by_rel:
        out.append("*(nothing passed the filter — lower --min-freq / --min-dice, "
                   "or try --all)*")
        return "\n".join(out)

    for rel, recs in sorted(by_rel.items(), key=lambda kv: -max(r[1] for r in kv[1])):
        out.append(f"### {rel}")
        out += ["", "| chunk | collocate | Kasus | logDice | Freq | B1 |",
                "|---|---|:-:|---:|---:|:-:|"]
        for colloc, ld, freq, case in recs[:args.top]:
            out.append("| {} | {} | {} | {:.1f} | {} | {} |".format(
                chunk_of(headword, rel, colloc), colloc,
                CASE_DE.get(case, ""), ld, freq,
                "✓" if in_b1(colloc, b1) else "·"))
        out.append("")
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("words", nargs="*")
    p.add_argument("--db", default=DEFAULT_DB)
    p.add_argument("--min-freq", type=int, default=20)
    p.add_argument("--min-dice", type=float, default=3.0)
    p.add_argument("--top", type=int, default=20, help="max collocates per relation")
    p.add_argument("--all", action="store_true", help="keep non-B1 collocates too")
    p.add_argument("--tsv", action="store_true")
    p.add_argument("--relations", nargs="*", default=None,
                   help="substring filter on relation names, e.g. --relations Akkusativ")
    p.add_argument("--info", action="store_true", help="print build metadata and exit")
    args = p.parse_args()

    if not os.path.isfile(args.db):
        sys.exit(f"no database at {args.db} — build it with tools/opus/ or pass --db")
    db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)

    if args.info:
        for k, v in db.execute("SELECT k, v FROM meta ORDER BY k"):
            print(f"{k:32} {v}")
        return

    if not args.words:
        sys.exit("give at least one headword (or --info)")
    b1 = load_b1()
    if args.tsv:
        print("headword\trelation\tcollocate\tcase\tlogdice\tfreq\tin_b1\tchunk")
    chunks = []
    for w in args.words:
        rows = fetch(db, w, args)
        if not rows:
            print(f"# {w}: no rows (not in corpus, or below the floors)", file=sys.stderr)
            continue
        if args.tsv:
            for rel, colloc, ld, freq, case in rows:
                if not args.all and not in_b1(colloc, b1):
                    continue
                print("\t".join(map(str, [w, rel, colloc, case, round(ld, 3), freq,
                                          int(in_b1(colloc, b1)),
                                          chunk_of(w, rel, colloc)])))
        else:
            chunks.append(render_md(w, rows, b1, args))
    if chunks:
        print("\n\n".join(chunks))


if __name__ == "__main__":
    main()

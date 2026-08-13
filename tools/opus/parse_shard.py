#!/usr/bin/env python3
"""
parse_shard.py — parse one shard, write its three count tables, exit.

One shard per process, single-threaded spaCy. NOT nlp.pipe(n_process=N): that ships
parsed Docs back to one parent process which then does all the counting, so on 4 cores
the parent is the bottleneck and the pickling costs more than the parse. Independent
processes over independent shards scale linearly and checkpoint for free — a shard whose
.done marker exists is skipped on restart, so a crash at 3am costs one shard, not a night.

Three tables per shard, because logDice needs the marginals:

    pairs   relation, headword, collocate, case  -> count      f(a,b)
    hm      relation, headword                   -> count      f(a)
    cm      relation, collocate                  -> count      f(b)

NOTHING IS PRUNED HERE. Per-shard pruning is the obvious way to save memory and it is
wrong at this shard size: a collocation occurring 30 times across the corpus appears
once or twice per shard, so a "drop count < 2 per shard" rule deletes precisely the
frequency band the freq>=20 floor is meant to keep. Pruning happens once, after the
merge, against global counts. The marginals are never pruned at all — logDice's
denominator has to be exact.

Files are written sorted so the merge can be a streaming k-way merge with bounded
memory, and are written to .tmp then renamed, so an interrupted shard can't leave a
half-written file that looks complete.
"""

import gzip
import json
import os
import sys
import time

import spacy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import triples          # noqa: E402

SEP = "\t"


def write_sorted(path, counts):
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=4) as f:
        for key in sorted(counts):
            f.write(f"{key}{SEP}{counts[key]}\n")
    os.replace(tmp, path)


def main():
    shard = sys.argv[1]
    outdir = sys.argv[2]
    name = os.path.basename(shard).replace(".txt.gz", "")
    done = os.path.join(outdir, f"{name}.done")
    if os.path.exists(done):
        print(f"[{name}] already done, skipping")
        return 0

    t0 = time.time()
    nlp = spacy.load("de_core_news_sm", exclude=["ner"])

    pairs, hm, cm = {}, {}, {}
    sents = tokens = rows = 0

    with gzip.open(shard, "rt", encoding="utf-8", errors="replace") as f:
        # batch_size tuned for short subtitle lines; n_process left at 1 deliberately.
        for doc in nlp.pipe((ln.rstrip("\n") for ln in f), batch_size=500):
            sents += 1
            tokens += len(doc)
            for head, rel, colloc, case in triples(doc):
                # Tab is the field separator and lemmas can't contain one, so a joined
                # string key is safe — and it costs far less memory than a 4-tuple,
                # which matters at a few million distinct keys per worker.
                pk = f"{rel}{SEP}{head}{SEP}{colloc}{SEP}{case}"
                pairs[pk] = pairs.get(pk, 0) + 1
                hk = f"{rel}{SEP}{head}"
                ck = f"{rel}{SEP}{colloc}"
                hm[hk] = hm.get(hk, 0) + 1
                cm[ck] = cm.get(ck, 0) + 1
                rows += 1

    write_sorted(os.path.join(outdir, f"{name}.pairs.tsv.gz"), pairs)
    write_sorted(os.path.join(outdir, f"{name}.hm.tsv.gz"), hm)
    write_sorted(os.path.join(outdir, f"{name}.cm.tsv.gz"), cm)

    meta = {"shard": name, "sentences": sents, "tokens": tokens, "rows": rows,
            "distinct_pairs": len(pairs), "seconds": round(time.time() - t0, 1),
            "tokens_per_sec": round(tokens / max(time.time() - t0, 1e-9))}
    with open(done, "w") as f:
        json.dump(meta, f)
    print(f"[{name}] {sents:,} sents  {tokens:,} tok  {meta['seconds']}s  "
          f"{meta['tokens_per_sec']:,} tok/s  {len(pairs):,} distinct pairs", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

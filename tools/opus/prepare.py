#!/usr/bin/env python3
"""
prepare.py — turn OPUS OpenSubtitles de.txt.gz into deduplicated, uniformly sampled
parse shards.

Three things this does that the recipe in groundwork/diy-wortprofil-opensubtitles.md
does not, each of which affects the correctness of the resulting statistics:

1. NO PREFIX SAMPLING.  The recipe's `itertools.islice(f, limit)` reads the first N
   lines, i.e. the first few hundred films. Register, era and genre are all skewed by
   whatever OPUS happened to concatenate first. We stream the whole file and select by
   a hash of the sentence, which is a uniform sample over the entire corpus.

2. DEDUPLICATION.  OpenSubtitles carries several subtitle versions of the same film
   plus vast line-level repetition ("Was ist das?"). Duplicates inflate logDice for
   stock phrases specifically, which is exactly the part of the output we care about.
   Selecting by hash makes this free: identical sentences hash identically, so a
   duplicate is either always selected or never, and the `seen` set collapses it.
   Memory stays bounded by the SAMPLE size, not the corpus size — a set over all
   ~60M surviving lines would be several GB.

3. ROUND-ROBIN SHARDING.  Sentence i goes to shard i % n_shards, so every shard is
   itself a uniform sample of the whole corpus. If the overnight run only gets through
   40 of 60 shards, the result is an unbiased 2/3 sample rather than a corpus prefix.

Usage
    python3 prepare.py --count-only          # pass 1: how many sentences survive?
    python3 prepare.py --target 22000000     # pass 2: write the shards
"""

import argparse
import glob
import gzip
import hashlib
import json
import os
import re
import sys
import time

# Subtitle furniture: HTML italics, speaker dashes, music notes, [sound effects],
# (parentheticals) and ALLCAPS speaker labels at the start of a line.
BAD = re.compile(r"<[^>]+>|\{[^}]*\}|♪|♫|\[[^\]]*\]|\([^)]*\)")
LEAD = re.compile(r"^\s*[-–—]+\s*")
SPEAKER = re.compile(r"^\s*[A-ZÄÖÜ][A-ZÄÖÜ .]{1,20}:\s*")
WS = re.compile(r"\s+")
NORM = re.compile(r"[^0-9a-zäöüß ]+")


def clean(line):
    s = BAD.sub(" ", line)
    s = LEAD.sub("", s)
    s = SPEAKER.sub("", s)
    return WS.sub(" ", s).strip()


def keep(s):
    """Length and shape filters. Subtitles are full of one-word interjections; those
    add noise, not signal, and a sentence needs a few words to hold a dependency."""
    if not (20 < len(s) < 200):
        return False
    if s.count(" ") < 3:
        return False
    if not any(c.islower() for c in s):        # ALLCAPS shouting / signage
        return False
    return True


def digest(s):
    """Stable 8-byte hash of the case- and punctuation-normalised sentence.
    Normalising means 'Was ist das?' and 'Was ist das!' collapse to one."""
    n = NORM.sub("", s.casefold())
    n = WS.sub(" ", n).strip()
    return int.from_bytes(hashlib.blake2b(n.encode("utf-8"), digest_size=8).digest(), "big")


def stream(path):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            s = clean(line)
            if keep(s):
                yield s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--corpus", default="/data/de.txt.gz")
    p.add_argument("--out", default="/work/shards")
    p.add_argument("--count-only", action="store_true",
                   help="pass 1: count surviving/unique lines so --target can be exact")
    p.add_argument("--target", type=int, default=22_000_000,
                   help="how many unique sentences to sample")
    p.add_argument("--survivors", type=int, default=0,
                   help="unique survivor count from pass 1; 0 = assume 55M")
    p.add_argument("--shards", type=int, default=72)
    args = p.parse_args()

    t0 = time.time()

    if args.count_only:
        # We only need the unique COUNT, not the set — count uniques on a 1/64
        # sub-sample of hash space and multiply. Bounded memory, ~1% accurate.
        seen, kept, total, words = set(), 0, 0, 0
        for s in stream(args.corpus):
            kept += 1
            words += s.count(" ") + 1
            h = digest(s)
            if h % 64 == 0:
                seen.add(h)
            if kept % 5_000_000 == 0:
                print(f"  ...{kept:,} kept, {time.time()-t0:.0f}s", file=sys.stderr, flush=True)
        uniq = len(seen) * 64
        print(json.dumps({
            "surviving_lines": kept, "estimated_unique": uniq,
            "words_in_surviving": words,
            "mean_words_per_line": round(words / max(kept, 1), 2),
            "seconds": round(time.time() - t0),
        }, indent=2))
        return

    survivors = args.survivors or 55_000_000
    # Probability a given UNIQUE sentence is selected. Hash space is bucketed into
    # 1e6 slots; take the first `thresh` of them.
    thresh = max(1, min(1_000_000, round(1_000_000 * args.target / survivors)))
    print(f"[prepare] target={args.target:,} unique-est={survivors:,} "
          f"thresh={thresh}/1e6 shards={args.shards}", file=sys.stderr, flush=True)

    os.makedirs(args.out, exist_ok=True)
    for stale in glob.glob(os.path.join(args.out, "shard_*.txt.gz")):
        os.remove(stale)
    writers = [gzip.open(os.path.join(args.out, f"shard_{i:04d}.txt.gz"), "wt",
                         encoding="utf-8", compresslevel=4)
               for i in range(args.shards)]

    seen = set()
    n = words = scanned = dups = 0
    try:
        for s in stream(args.corpus):
            scanned += 1
            h = digest(s)
            if h % 1_000_000 >= thresh:
                continue
            if h in seen:                      # exact/near duplicate line
                dups += 1
                continue
            seen.add(h)
            writers[n % args.shards].write(s + "\n")
            n += 1
            words += s.count(" ") + 1
            if n % 2_000_000 == 0:
                print(f"  ...{n:,} written, {scanned:,} scanned, "
                      f"{time.time()-t0:.0f}s", file=sys.stderr, flush=True)
    finally:
        for w in writers:
            w.close()

    meta = {"sentences": n, "words": words, "scanned": scanned,
            "duplicates_dropped_in_sample": dups,
            "dup_rate_in_sample": round(dups / max(dups + n, 1), 3),
            "shards": args.shards, "thresh_per_million": thresh,
            "seconds": round(time.time() - t0)}
    meta["mean_words_per_sentence"] = round(words / max(n, 1), 2)
    with open(os.path.join(args.out, "prepare-meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
wordfreq.py — rank a batch's words by how common they actually are in German.

WHY: a batch's 148 words are not equally worth your memory. `die Wohnung` (band 4)
earns a whole scene; `der Abfalleimer` (band 2) earns a clause. This orders them so
the cramming texts can spend their real estate accordingly.

TWO DATA SOURCES, both fully sanctioned (unlike Wortprofil — see
docs/collocations-method.md §3.2):

  1. BULK, one request, no per-word traffic  [default]
     https://www.dwds.de/lemma/csv — the DWDS Lemmadatenbank, an offered download
     (Content-Disposition: attachment) linked from https://www.dwds.de/lemma/list.
     279,346 lemmas with a `frequenzklasse` column. `/lemma` is not robots-disallowed.
     Cached to data/dwds/dwds_lemmata.csv (~27 MB) — fetched once, reused forever.

  2. FINE-GRAINED, one request per word       [--hits]  ** SPOT-CHECKS ONLY **
     https://www.dwds.de/api/frequency/?q=WORT — the documented frequency API, which
     returns raw `hits`. Rate-limited to one request per 1.5 s and cached per word.

     Use it on a HANDFUL of words: the `n/a` homographs, and ties you actually need
     broken. Do NOT sweep a whole 148-word wordlist with it — 148 sequential automated
     requests is precisely the "automated mechanism to access dwds.de" that the DWDS
     legal notice in robots.txt names, documented endpoint or not. The bulk CSV already
     gives you a band for every word, so a sweep buys almost nothing. This script
     refuses runs over --hits-limit words unless you override it deliberately.

THE SCALE (identical in both sources): an integer 0-6, HIGHER = MORE FREQUENT.
    frequency = clamp(log10(hits / total * 1_000_000) + 2, 0, 6)
It is coarse on purpose — 7 bands over 279k lemmas, so ties are enormous
(111,672 lemmas sit in band 0). Use bands to sort words into tiers; use --hits to
order within a tier. `n/a` means DWDS has no frequency for that lemma (affixes,
multiword entries, lemmatisation problems) — it does NOT mean "rare".

USAGE
    python3 tools/wordfreq.py --words Tasse Wohnung Fauteuil
    python3 tools/wordfreq.py --words Tasse Wohnung Fauteuil --hits
    python3 tools/wordfreq.py --words Wohnung Schrank Tasse
    python3 tools/wordfreq.py --words Tasse Wohnung Fauteuil --tsv
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paths import DWDS_CACHE as CACHE                        # noqa: E402

LEMMA_CSV = os.path.join(CACHE, "dwds_lemmata.csv")
LEMMA_URL = "https://www.dwds.de/lemma/csv"
HITS_CACHE = os.path.join(CACHE, "frequency-hits.json")
FREQ_URL = "https://www.dwds.de/api/frequency/?q={}"
UA = "anki-b1-cram/personal-study"
DELAY = 1.5  # seconds between /api/frequency calls — be a good guest


def load_bands():
    """lemma -> frequenzklasse (int 0-6, or None for 'n/a'). One download, then cached."""
    if not os.path.isfile(LEMMA_CSV):
        os.makedirs(CACHE, exist_ok=True)
        sys.stderr.write("fetching the DWDS Lemmadatenbank once (~27 MB)…\n")
        req = urllib.request.Request(LEMMA_URL, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=300) as r, open(LEMMA_CSV, "wb") as f:
            f.write(r.read())
    bands = {}
    with open(LEMMA_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            fk = row.get("frequenzklasse")
            val = int(fk) if fk and fk.isdigit() else None
            # A lemma can appear more than once (homographs: Schloss#1 / Schloss#2).
            # Verified against the 2026-08-09 dump: of 1,983 lemmas with multiple rows,
            # ZERO have conflicting frequenzklasse values — DWDS attributes frequency to
            # the lemma string, not the sense. So this max() can't misattribute a
            # frequent sense's band to a rare one; it's belt-and-braces. Re-check if the
            # dump is ever refreshed.
            prev = bands.get(row["lemma"], -1)
            if val is not None and (prev is None or val > prev):
                bands[row["lemma"]] = val
            elif row["lemma"] not in bands:
                bands[row["lemma"]] = val
    return bands


def fetch_hits(word, cache):
    """Raw corpus hits for one lemma via the documented API. Cached; polite delay."""
    if word in cache:
        return cache[word]
    url = FREQ_URL.format(urllib.parse.quote(word))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8"))
        # GOTCHA: when the input is ambiguous the API lemmatises to SEVERAL lemmas,
        # returns them tab-separated in `lemma`, and reports hits: 0. e.g.
        #   /api/frequency/?q=locker -> {"lemma":"locker\tlockern","hits":0,...}
        # 0 hits there means "could not attribute", NOT "this word is absent".
        lemma = d.get("lemma") or ""
        cache[word] = {"hits": d.get("hits"), "frequency": d.get("frequency"),
                       "lemma": lemma, "ambiguous": "\t" in lemma}
    except Exception as e:                                   # noqa: BLE001
        sys.stderr.write(f"  ! {word}: {e}\n")
        cache[word] = {"hits": None, "frequency": None, "lemma": "", "ambiguous": False}
    time.sleep(DELAY)
    return cache[word]


HEADWORD_RE = re.compile(r"^\|\s*([^|]+?)\s*\|")
ARTICLES = ("der ", "die ", "das ")


def read_wordlist(path, collapsed=None):
    """
    Pull headwords out of a batch wordlist.md table; strip article and forms.

    Slash-variant headwords (`der Abwart / die Abwartin`, `Stiege/Treppe`) are collapsed
    to the FIRST variant — the second is not ranked. Names of collapsed entries are
    appended to `collapsed` so the caller can report them instead of dropping silently.
    """
    words = []
    for line in open(path, encoding="utf-8"):
        m = HEADWORD_RE.match(line)
        if not m:
            continue
        w = m.group(1).strip()
        if not w or w.startswith("-") or w.lower() in ("word (with article)", "word"):
            continue
        w = re.sub(r"\s*\(.*?\)", "", w).strip()      # drop "(D)" regional tags
        w = w.split(",")[0].strip()                   # drop trailing forms
        headword = w                                  # keep for reporting, pre-strip
        for a in ARTICLES:
            if w.startswith(a):
                w = w[len(a):]
                break
        if "/" in w:
            if collapsed is not None:
                collapsed.append(headword)
            w = w.split("/")[0].strip()
        if w:
            words.append(w)
    return words


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("wordlist", nargs="?", help="a batch's wordlist.md")
    p.add_argument("--words", nargs="+", help="rank these words instead")
    p.add_argument("--hits", action="store_true",
                   help="fetch raw hits per word — SPOT-CHECKS ONLY, 1 request/word")
    p.add_argument("--hits-limit", type=int, default=25,
                   help="refuse --hits runs larger than this many uncached words "
                        "(default 25; raise deliberately, not reflexively)")
    p.add_argument("--tsv", action="store_true")
    args = p.parse_args()

    collapsed = []
    if args.words:
        words = args.words
    elif args.wordlist:
        words = read_wordlist(args.wordlist, collapsed)
    else:
        p.error("give a wordlist.md or --words")

    seen, uniq = set(), []
    for w in words:
        if w not in seen:
            seen.add(w)
            uniq.append(w)

    bands = load_bands()
    hits_cache = {}
    if args.hits:
        if os.path.isfile(HITS_CACHE):
            hits_cache = json.load(open(HITS_CACHE, encoding="utf-8"))
        todo = [w for w in uniq if w not in hits_cache]
        if len(todo) > args.hits_limit:
            sys.exit(
                f"refusing: --hits would make {len(todo)} requests to dwds.de "
                f"(limit {args.hits_limit}).\n"
                f"The bulk CSV already gives every word a band — run without --hits, then\n"
                f"spot-check just the 'n/a' and tied words:\n"
                f"    python3 tools/wordfreq.py --words <word> <word> --hits\n"
                f"If you really need the sweep, pass --hits-limit {len(todo)}.")
        if todo:
            sys.stderr.write(f"fetching hits for {len(todo)} words "
                             f"(~{len(todo) * DELAY / 60:.1f} min)…\n")

    rows = []
    for w in uniq:
        band = bands.get(w, "—")
        rec = fetch_hits(w, hits_cache) if args.hits else {}
        rows.append({"word": w,
                     "band": band if band is not None else "n/a",
                     "hits": rec.get("hits"),
                     "ambiguous": rec.get("ambiguous", False),
                     "known": w in bands})

    if args.hits:
        json.dump(hits_cache, open(HITS_CACHE, "w", encoding="utf-8"), ensure_ascii=False)

    def sort_key(r):
        b = r["band"] if isinstance(r["band"], int) else -1
        return (-b, -(r["hits"] or 0), r["word"])

    rows.sort(key=sort_key)

    if args.tsv:
        print("word\tband\thits\tin_dwds")
        for r in rows:
            print(f'{r["word"]}\t{r["band"]}\t{r["hits"] if r["hits"] is not None else ""}'
                  f'\t{int(r["known"])}')
        return

    print(f"# {len(rows)} words by DWDS frequency band (6 = most frequent)\n")
    print("| word | band |" + (" hits |" if args.hits else ""))
    print("|---|:-:|" + ("---:|" if args.hits else ""))
    for r in rows:
        line = f'| {r["word"]} | {r["band"]} |'
        if args.hits:
            if r["ambiguous"]:
                line += " ambiguous |"
            elif r["hits"]:
                line += f' {r["hits"]:,} |'.replace(",", " ")
            else:
                line += " |"
        print(line)

    amb = [r["word"] for r in rows if r["ambiguous"]]
    if amb:
        print(f"\n*Ambiguous lemmatisation, hits unusable ({len(amb)}): "
              f"{', '.join(amb)}. The API mapped these to more than one lemma and "
              f"returned 0 — that is 'could not attribute', not 'rare'.*")

    if collapsed:
        print(f"\n*Slash-variant headwords ranked by their FIRST variant only "
              f"({len(collapsed)}): {', '.join(collapsed)}.*")

    missing = [r["word"] for r in rows if not r["known"]]
    if missing:
        print(f"\n*Not in the Lemmadatenbank ({len(missing)}): "
              f"{', '.join(missing[:20])}{' …' if len(missing) > 20 else ''}. "
              f"Usually multiword entries or spelling variants — not evidence of rarity.*")


if __name__ == "__main__":
    main()

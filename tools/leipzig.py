#!/usr/bin/env python3
"""
leipzig.py — collocations for a German word, programmatically, from a licensed API.

THE ANSWER TO "where can I actually get collocations from?"
-----------------------------------------------------------
The Leipzig Corpora Collection (Wortschatz Leipzig) publishes a real REST API:

    https://api.wortschatz-leipzig.de/ws/v3/api-docs      <- OpenAPI 3 spec
    https://api.wortschatz-leipzig.de/ws/swagger-ui/index.html

  * License declared in the spec itself: **CC BY 4.0**  (terms: wortschatz-leipzig.de/usage)
  * No robots restriction on the API host, no login, no key.
  * Built for exactly this: "direct access to the data of the LCC by using a
    software of your choice."

So unlike DWDS-Wortprofil, this one you may simply call. That is what this script does.

WHAT YOU GET, AND HOW IT DIFFERS FROM WORTPROFIL
    Wortprofil : dependency-typed  -> "Tasse IST AKKUSATIV-OBJEKT VON trinken"
    Leipzig    : window-based      -> "Tasse co-occurs with trinken (sig 587)"
Leipzig does NOT label the grammatical relation. You lose the single most useful thing
Wortprofil had (see groundwork/dwds-wortprofil-guide.md §1.4). What you keep: a real,
scriptable, licensed collocation signal. `left`/`right` position is a crude proxy for
structure — a noun's left neighbours skew determiner/adjective, its right neighbours
skew the noun it heads or the preposition that follows.

The German corpora are also much smaller than DWDS's (3M sentences vs. billions of
tokens), so counts are thinner and rarer chunks simply won't appear.

USAGE
    python3 tools/leipzig.py Tasse
    python3 tools/leipzig.py Wohnung Schrank Fenster --corpus deu_wikipedia_2010_1M
    python3 tools/leipzig.py Tasse --all --limit 40
    python3 tools/leipzig.py Wohnung --tsv

Attribution, if you ever share anything built from this:
    Leipzig Corpora Collection, https://wortschatz-leipzig.de/, CC BY 4.0
"""

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wortprofil import in_b1, load_b1                        # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "dwds-cache", "leipzig")
BASE = "https://api.wortschatz-leipzig.de/ws"
DEFAULT_CORPUS = "deu_news_2012_3M"
UA = "anki-b1-cram/personal-study"
DELAY = 1.0


GLUE_POOL = os.path.join(ROOT, "groundwork", "glue-pool.md")


def log_dice(pair_freq, f_a, f_b):
    """
    logDice = 14 + log2(2*f_AB / (f_A + f_B)).

    WHY WE COMPUTE THIS OURSELVES. The API's own `sig` is frequency-scaled: measured
    over the cached results, Pearson r(pair-freq, sig) = 0.55, and the preposition `in`
    scores 1982 purely on volume. Ranking by `sig` therefore promotes common-and-
    unremarkable over rare-and-idiomatic — the OPPOSITE failure mode from logDice, which
    rewards exclusivity (guide §1.3). Since the response carries w1.freq and w2.freq
    alongside the pair frequency, logDice is computable, so the two-floor rule from the
    guide applies here exactly as it does to Wortprofil.

    Absolute values are NOT comparable between the two tools: Wortprofil counts
    dependency-typed pairs, this counts sentence-window pairs, so the same word pair
    scores differently. Compare ranks within one tool, never numbers across them.
    """
    if not pair_freq or not f_a or not f_b:
        return None
    return 14 + math.log2(2 * pair_freq / (f_a + f_b))


def load_glue():
    """
    Closed-class function words, read straight from the repo's own glue pool.

    Window co-occurrence is dominated by these (`und`, `oder`, `eine`, `die` all rank
    high for any noun) and they carry no chunk information — the text-writer weaves them
    in from glue-pool.md anyway. Filtering them here is not a guess about German: it
    reuses the classification this project already made.
    """
    # Bare articles and their inflected forms are closed-class by definition but are NOT
    # listed in the pool (which records stems like `dies-`, `einig-`). Without these,
    # `eine` sails through as a top collocate of every noun.
    words = {
        "der", "die", "das", "den", "dem", "des",
        "ein", "eine", "einen", "einem", "einer", "eines",
        "kein", "keine", "keinen", "keinem", "keiner", "keines",
        "ich", "du", "er", "sie", "es", "wir", "ihr", "man", "sich",
        "mich", "dich", "ihn", "uns", "euch", "ihnen", "mir", "dir", "ihm",
        # `sein` is deliberately here as the possessive; it also swallows the infinitive
        # "to be". Fine for this project — both are glue — but it does mean `sein` can
        # never surface as a collocate.
        "mein", "dein", "sein", "unser", "euer",
        "ist", "sind", "war", "waren", "hat", "haben", "hatte", "wird", "werden",
    }
    if os.path.isfile(GLUE_POOL):
        text = open(GLUE_POOL, encoding="utf-8").read()
        for m in re.finditer(r"`[☐☑]\s*([^`]+)`", text):
            entry = m.group(1).strip()
            for part in re.split(r"\s*(?:\.\.\.|…|/)\s*", entry):
                part = part.strip()
                if not part or " " in part:
                    continue
                if part.endswith("-"):
                    # `dies-` stands for dies/diese/dieser/diesem/diesen/dieses
                    stem = part[:-1]
                    words.update({stem} | {stem + e for e in
                                           ("e", "er", "es", "em", "en")})
                else:
                    words.add(part)
    return {w for w in words if w} | {w.capitalize() for w in words if w}


def get(path, params=None):
    url = f"{BASE}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def collocations(word, corpus, limit):
    """Window cooccurrences + immediate left/right neighbours, cached per word+corpus."""
    os.makedirs(CACHE, exist_ok=True)
    safe = urllib.parse.quote(word, safe="") + f".{corpus}.json"
    path = os.path.join(CACHE, safe)
    if os.path.isfile(path):
        return json.load(open(path, encoding="utf-8"))

    out = {}
    for kind, ep in (("window", "cooccurrences"),
                     ("left", "leftcooccurrences"),
                     ("right", "rightcooccurrences")):
        try:
            out[kind] = get(f"/cooccurrences/{corpus}/{ep}/{urllib.parse.quote(word)}",
                            {"limit": limit})
        except Exception as e:                               # noqa: BLE001
            sys.stderr.write(f"  ! {word} [{kind}]: {e}\n")
            out[kind] = []
        time.sleep(DELAY)
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    return out


def render(word, data, b1, glue, args):
    lines = [f"## {word}", "",
             f"*Corpus: `{args.corpus}` · ranked by logDice (computed, not the API's "
             f"frequency-scaled `sig`)"
             + ("" if args.all else " · B1 lemmas only, glue words dropped") + "*", ""]
    any_row = False
    for kind, title in (("window", "co-occurs with (sentence window)"),
                        ("left", "immediate left neighbour"),
                        ("right", "immediate right neighbour")):
        recs = data.get(kind) or []
        keep = []
        for r in recs:
            w2rec = r.get("w2") or {}
            w2 = w2rec.get("word", "")
            if not w2 or w2 == word:
                continue
            if not args.all and (not in_b1(w2, b1) or w2 in glue):
                continue
            dice = log_dice(r.get("freq"), (r.get("w1") or {}).get("freq"),
                            w2rec.get("freq"))
            if args.min_dice is not None and dice is not None and dice < args.min_dice:
                continue
            keep.append((w2, r.get("freq"), r.get("sig"), dice))
        if not keep:
            continue
        keep.sort(key=lambda x: -(x[3] if x[3] is not None else -99))
        any_row = True
        lines += [f"### {title}", "",
                  "| collocate | logDice | freq | sig | B1 |",
                  "|---|---:|---:|---:|:-:|"]
        for w2, freq, sig, dice in keep:
            lines.append(f"| {w2} | {f'{dice:.1f}' if dice is not None else ''} "
                         f"| {freq} | {sig} | {'✓' if in_b1(w2, b1) else '·'} |")
        lines.append("")
    if not any_row:
        lines.append("*(nothing survived — try --all, a bigger --limit, "
                     "or another --corpus)*")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("words", nargs="+")
    p.add_argument("--corpus", default=DEFAULT_CORPUS,
                   help=f"LCC corpus name (default {DEFAULT_CORPUS}); "
                        f"list them: /ws/corpora/availableCorpora")
    p.add_argument("--limit", type=int, default=25, help="rows per endpoint (default 25)")
    # No default floor: window counts and immediate-neighbour counts live on different
    # scales (a right-neighbour pair is far rarer than a same-sentence pair), so one
    # absolute logDice floor silently empties the neighbour tables — which is where the
    # verbs are. Sort by logDice, filter by B1 + glue, and let the reader stop reading.
    p.add_argument("--min-dice", type=float, default=None,
                   help="optional logDice floor; off by default (scales differ per table)")
    p.add_argument("--all", action="store_true", help="keep non-B1 collocates too")
    p.add_argument("--tsv", action="store_true")
    args = p.parse_args()

    b1 = load_b1()
    glue = load_glue()
    if args.tsv:
        print("word\tkind\tcollocate\tlogdice\tfreq\tsig\tin_b1\tis_glue")
    blocks = []
    for w in args.words:
        data = collocations(w, args.corpus, args.limit)
        if args.tsv:
            for kind in ("window", "left", "right"):
                for r in data.get(kind) or []:
                    w2rec = r.get("w2") or {}
                    w2 = w2rec.get("word", "")
                    if not w2 or w2 == w:
                        continue
                    dice = log_dice(r.get("freq"), (r.get("w1") or {}).get("freq"),
                                    w2rec.get("freq"))
                    print(f"{w}\t{kind}\t{w2}\t{f'{dice:.2f}' if dice else ''}"
                          f"\t{r.get('freq')}\t{r.get('sig')}"
                          f"\t{int(in_b1(w2, b1))}\t{int(w2 in glue)}")
        else:
            blocks.append(render(w, data, b1, glue, args))
    if blocks:
        print("\n\n".join(blocks))
        print("\n---\n*Source: Leipzig Corpora Collection, "
              "https://wortschatz-leipzig.de/ — CC BY 4.0.*")


if __name__ == "__main__":
    main()

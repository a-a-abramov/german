#!/usr/bin/env python3
"""
wortprofil.py — turn a saved DWDS-Wortprofil page into a B1-filtered chunk table.

WHY THIS READS LOCAL FILES INSTEAD OF FETCHING
----------------------------------------------
https://www.dwds.de/robots.txt disallows /wp for every user-agent and carries an
explicit legal notice: "Unauthorized use of robots or other automated mechanisms
to access dwds.de or to gather or mine data is strictly forbidden without explicit
consent from DWDS." The TDM policy (dwds_static/tdm-policy.json) permits mining
only under an obtainConsent duty. So this script never touches the network for /wp.

You open the Wortprofil page in your browser (an ordinary human page view, which is
exactly what the site is for) and save it. This script parses what you saved.

  1. Open  https://www.dwds.de/wp/?q=<WORT>&minfreq=5&limit=20&view=table&mode=full
  2. Save the page:  Cmd-S  →  "Web Page, HTML Only"  →  dwds-cache/<Wort>.html
  3. python3 tools/wortprofil.py dwds-cache/Tasse.html

The only network calls this script makes are to
https://www.dwds.de/api/lemma/goethe/{A1,A2,B1}.json — documented, publicly published
API endpoints (see https://www.dwds.de/d/api#wb-list-goethe), not robots-disallowed.
They are cached to dwds-cache/goethe-*.json after the first run.

NOTE: those three lists are INCREMENTAL, not cumulative — B1.json holds only the
words new at B1 (1842 entries; `trinken` and `heiß` are not in it, they are A1).
A B1 candidate knows the union: 3308 lemmas. This script unions all three.

USAGE
    python3 tools/wortprofil.py dwds-cache/Tasse.html            # markdown chunk table
    python3 tools/wortprofil.py dwds-cache/*.html --tsv          # tsv for scripting
    python3 tools/wortprofil.py dwds-cache/Tasse.html --all      # don't hide non-B1
    python3 tools/wortprofil.py dwds-cache/Tasse.html --min-freq 30 --min-dice 3.0
"""

import argparse
import html
import json
import os
import re
import sys
import urllib.request

CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dwds-cache")
LEVELS = ("A1", "A2", "B1")
LEVEL_URL = "https://www.dwds.de/api/lemma/goethe/{}.json"
REPO_CSV = os.path.join(os.path.dirname(CACHE), "goethe-b1-wortliste.csv")

# Wortprofil relation -> how the chunk actually surfaces in a German sentence.
# This mapping is the whole point: a bare collocate is a word, a collocate *plus its
# relation* is a chunk you can drop into a text.
#
# These are PATTERNS, not finished German. Two things the corpus data cannot supply:
#   * case      -- 'in Schrank' is *im* Schrank (Dat.) or *in den* Schrank (Akk.)
#                  depending on whether you mean location or direction.
#   * adjective endings -- the naive 'e(r)' suffix below is right for heiss -> heisse
#                  but wrong for hoch -> *hoche (hoher) and teuer -> *teuere (teure).
# Decline and case them yourself before they go into a text.
RELATION_PATTERNS = {
    "hat Adjektivattribut":         "ein(e) {c}e(r) {L}",
    "ist Adjektivattribut von":     "ein(e) {L}e(r) {c}",
    "ist Akkusativ-Objekt von":     "{L}(Akk.) {c}",
    "hat Akkusativ-Objekt":         "{L} + {c}(Akk.)",
    "ist Dativ-/Genitiv-Objekt von": "{L}(Dat./Gen.) {c}",
    "hat Dativ-/Genitiv-Objekt":    "{L} + {c}(Dat./Gen.)",
    "ist Subjekt von":              "{L} {c}(t)",
    "hat Subjekt":                  "{c} {L}(t)",
    "ist Passivsubjekt von":        "{L} wird {c}",
    "hat Passivsubjekt":            "{c} wird {L}",
    "ist in Präpositionalgruppe":   "{c} … {L}",
    "hat Präpositionalgruppe":      "{L} + {c}",
    "hat Genitivattribut":          "{L} des/der {c}",
    "ist Genitivattribut von":      "{c} des/der {L}",
    "ist Prädikativ von":           "… ist/wird {L} {c}",
    "hat Prädikativ":               "{L} ist/wird {c}",
    "mit Prädikativ":               "{L} + {c}",
    "ist Prädikativ zu":            "{c} ist/wird {L}",
    "hat Adverbialbestimmung":      "{c} {L}",
    "ist Adverbialbestimmung von":  "{L} {c}",
    "ist in Koordination mit":      "{L} und {c}",
    "hat vergleichende Wortgruppe": "{L} wie {c}",
    "ist in vergleichender Wortgruppe": "{c} wie {L}",
    "tritt auf mit":                "{L} … {c}",
    "Überblick":                    "(see source relation)",
}


# ---------------------------------------------------------------- B1 lemma set

def load_b1():
    """Everything a B1 candidate is assumed to know = A1 ∪ A2 ∪ B1, plus the repo CSV."""
    lemmas = set()
    for lvl in LEVELS:
        path = os.path.join(CACHE, f"goethe-{lvl}.json")
        if not os.path.isfile(path):
            os.makedirs(CACHE, exist_ok=True)
            req = urllib.request.Request(
                LEVEL_URL.format(lvl),
                headers={"User-Agent": "anki-b1-cram/personal-study"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
        for e in json.load(open(path, encoding="utf-8")):
            for s in e.get("sch", []):
                if s.get("lemma"):
                    lemmas.add(s["lemma"])

    # Union with this repo's source of truth (the wejn.org extraction), whose
    # headwords carry inflection baggage: "der Teppich, -e" -> "Teppich".
    if os.path.isfile(REPO_CSV):
        import csv as _csv
        with open(REPO_CSV, encoding="utf-8") as f:
            for row in _csv.reader(f):
                if not row:
                    continue
                head = row[0].split(",")[0].strip()
                head = re.sub(r"\s*\(.*?\)", "", head).strip()
                for variant in head.split("/"):
                    variant = variant.strip()
                    parts = variant.split()
                    if parts and parts[0] in ("der", "die", "das"):
                        parts = parts[1:]
                    if len(parts) == 1 and parts[0]:
                        lemmas.add(parts[0])
    return lemmas


PREPS = {
    "an", "auf", "aus", "bei", "bis", "durch", "für", "gegen", "hinter", "in", "mit",
    "nach", "neben", "ohne", "seit", "über", "um", "unter", "von", "vor", "während",
    "wegen", "zu", "zwischen", "ab", "am", "im", "zum", "zur", "beim", "vom", "ans",
    "aufs", "ins", "gegenüber", "trotz", "statt", "innerhalb", "außerhalb",
}


def in_b1(collocate, b1):
    """
    Collocates arrive as 'nippen an', 'in Schrank', 'Teelöffel auf' — a content word
    plus a preposition, in either order. Prepositions are trivially B1, so testing
    'any token in B1' passes everything (that let 'aus Porzellan' through). Test the
    CONTENT tokens only, and require all of them.
    """
    if collocate in b1:
        return True
    content = [p for p in collocate.split() if p.lower() not in PREPS]
    return bool(content) and all(p in b1 for p in content)


# ------------------------------------------------------------------- parsing

TABLE_RE = re.compile(r'<table[^>]*class="[^"]*wpassoc[^"]*"[^>]*>(.*?)</table>', re.S)
RELDESC_RE = re.compile(r'<span class="rel-desc">([^<]*)</span>')
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
COLLOC_RE = re.compile(
    r'<span class="wp-collocation wp-rel"\s*(?P<attrs>[^>]*)>\s*'
    r'<span[^>]*>(?P<text>[^<]*)</span>', re.S)
TD_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.S)
SRCREL_RE = re.compile(r'aus der Relation »([^«»]+)«')
MWE_RE = re.compile(r'href="(/wp/[^"]*\?mwe=[-\d]+)"')


def strip(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def parse_page(path):
    """-> (headword, [ {relation, collocate, logdice, freq, source_relation, mwe} ])"""
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r'<input[^>]*name="q"[^>]*value="([^"]*)"', raw)
    headword = html.unescape(m.group(1)) if m else os.path.splitext(os.path.basename(path))[0]

    out = []
    for tbl in TABLE_RE.finditer(raw):
        body = tbl.group(1)
        rd = RELDESC_RE.search(body)
        relation = html.unescape(rd.group(1)).strip() if rd else "?"
        for row in ROW_RE.finditer(body):
            r = row.group(1)
            c = COLLOC_RE.search(r)
            if not c:
                continue
            tds = TD_RE.findall(r)
            nums = [strip(td) for td in tds[1:]]
            nums = [n for n in nums if re.fullmatch(r"-?\d+(?:[.,]\d+)?", n)]
            logdice = float(nums[0].replace(",", ".")) if len(nums) > 0 else None
            freq_attr = re.search(r'data-freq="(\d+)"', c.group("attrs"))
            freq = int(freq_attr.group(1)) if freq_attr else (
                int(nums[1]) if len(nums) > 1 else None)
            src = SRCREL_RE.search(r)
            out.append({
                "relation": relation,
                "collocate": html.unescape(c.group("text")).strip(),
                "logdice": logdice,
                "freq": freq,
                "source_relation": html.unescape(src.group(1)).strip() if src else relation,
                "mwe": bool(MWE_RE.search(r)),
            })
    return headword, out


# -------------------------------------------------------------------- output

def chunk_of(headword, rec):
    pat = RELATION_PATTERNS.get(rec["source_relation"], "{L} … {c}")
    return pat.format(L=headword, c=rec["collocate"])


def render_md(headword, rows, b1, args):
    lines = [f"## {headword}", ""]
    lines.append(f"*Filter: Freq ≥ {args.min_freq}, logDice ≥ {args.min_dice}"
                 + ("" if args.all else ", B1 lemmas only") + "*")
    lines.append("")
    by_rel = {}
    for r in rows:
        if r["relation"] == "Überblick":
            continue
        by_rel.setdefault(r["relation"], []).append(r)

    kept_total = 0
    for rel, recs in by_rel.items():
        keep = [r for r in recs
                if (r["freq"] or 0) >= args.min_freq
                and (r["logdice"] or 0) >= args.min_dice
                and (args.all or in_b1(r["collocate"], b1))]
        if not keep:
            continue
        kept_total += len(keep)
        lines.append(f"### {rel}")
        if "Präpositionalgruppe" in rel:
            lines.append("*Wortprofil does not show the case — check it before you write.*")
        lines += ["",
                  "| chunk | collocate | logDice | Freq | B1 | MWE |",
                  "|---|---|---:|---:|:-:|:-:|"]
        for r in sorted(keep, key=lambda x: -(x["logdice"] or 0)):
            lines.append("| {} | {} | {} | {} | {} | {} |".format(
                chunk_of(headword, r), r["collocate"],
                f'{r["logdice"]:.1f}' if r["logdice"] is not None else "",
                r["freq"] if r["freq"] is not None else "",
                "✓" if in_b1(r["collocate"], b1) else "·",
                "🔗" if r["mwe"] else ""))
        lines.append("")
    if not kept_total:
        lines.append("*(nothing passed the filter — loosen --min-freq / --min-dice)*")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("pages", nargs="+", help="saved Wortprofil HTML file(s)")
    p.add_argument("--min-freq", type=int, default=20, help="raw frequency floor (default 20)")
    p.add_argument("--min-dice", type=float, default=3.0, help="logDice floor (default 3.0)")
    p.add_argument("--all", action="store_true", help="keep non-B1 collocates too")
    p.add_argument("--tsv", action="store_true", help="emit TSV instead of markdown")
    args = p.parse_args()

    b1 = load_b1()
    if args.tsv:
        print("headword\trelation\tcollocate\tlogdice\tfreq\tin_b1\tmwe\tchunk")
    chunks = []
    for path in args.pages:
        headword, rows = parse_page(path)
        if not rows:
            print(f"# {path}: no collocation tables found "
                  f"(did you save the page as HTML with mode=full?)", file=sys.stderr)
            continue
        if args.tsv:
            for r in rows:
                if r["relation"] == "Überblick":
                    continue
                print("\t".join(map(str, [
                    headword, r["relation"], r["collocate"], r["logdice"], r["freq"],
                    int(in_b1(r["collocate"], b1)), int(r["mwe"]),
                    chunk_of(headword, r)])))
        else:
            chunks.append(render_md(headword, rows, b1, args))
    if chunks:
        print("\n\n".join(chunks))


if __name__ == "__main__":
    main()

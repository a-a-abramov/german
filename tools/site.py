#!/usr/bin/env python3
"""
site.py — build the static reader that lives on GitHub Pages.

WHY THIS EXISTS: `content/batches/` is the only directory a human reads, but it reads
as markdown in a text editor, which is the wrong shape for the two things actually done
with it — cramming one dialogue at a time, and asking the ledger where a word stands.
So this renders three surfaces:

    the index      curriculum/vocab.db seen from above — 23 topics, what is written,
                   what is owed, and every word in the ledger, searchable
    the reader     one dialogue per page, set to be read aloud from, with the scene's
                   owned words in the margin and a gloss on every target word
    the chunks     per batch, per load-bearing word: a link to that word's live DWDS
                   Wortprofil, and every sentence we have written with the word

It is a pure function of the repo: `curriculum/vocab.db` + `content/batches/`. Nothing
is authored here and nothing in `site/` is committed on master — `publish-site.sh`
pushes the output to the `gh-pages` branch.

WORD MATCHING IS NOT REIMPLEMENTED HERE. Which target words a dialogue realises is
exactly the question `vocab.py scan` answers, so this imports its matcher
(`variants` / `csv_forms` / `phrase_matches`) rather than growing a second one that
would drift. The one difference: `scan_file` stops at a word's first sighting, because
the ledger records first sightings; the reader wants every sighting in every text, so
the loop here does not break.

USAGE

    python3 tools/site.py                 # build into site/
    python3 tools/site.py --out /tmp/x    # build somewhere else
    python3 tools/site.py --serve         # build, then serve it on :8000
"""

import argparse
import html
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from paths import BATCHES, ROOT, VOCAB_DB                                    # noqa: E402
from vocab import (REGIONAL_SQL, bare, csv_forms, fold, phrase_matches,      # noqa: E402
                   variants)

OUT = os.path.join(ROOT, "site")

# The cram order from curriculum/topics.md: concrete first, function words last.
# Batch numbers are the database key, so the stage boundaries are just numbers.
STAGES = [
    (1,  8,  "Stufe A", "Konkret & körperlich"),
    (9,  16, "Stufe B", "Situativ & alltagsweltlich"),
    (17, 20, "Stufe C", "Emotional & kommunikativ"),
    (21, 23, "Stufe D", "Abstrakt & grammatisch"),
]

WORD_CHAR = "A-Za-zÄÖÜäöüßÉéÀàÇç"


# ---------------------------------------------------------------- reading the repo

def batch_dirs():
    """[(number, slug, path), ...] for every content/batches/NN-* directory."""
    out = []
    for name in sorted(os.listdir(BATCHES)):
        m = re.match(r"^(\d+)-(.+)$", name)
        path = os.path.join(BATCHES, name)
        if m and os.path.isdir(path):
            out.append((int(m.group(1)), name, path))
    return out


def read_scenes(path):
    """[{no, title, premise, angle, words, glue, note}, ...] from a batch scenes.md."""
    scenes, cur = [], None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^###\s+Scene\s+(\d+)\s*[—–-]\s*(.+)$", line.strip())
        if m:
            cur = {"no": int(m.group(1)), "title": m.group(2).strip(),
                   "premise": "", "angle": "", "words": [], "glue": [], "note": ""}
            scenes.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^-\s+\*\*(Premise|Angle|Note|Words|Glue)[^:]*:\*\*\s*(.*)$", line.strip())
        if not m:
            continue
        key, val = m.group(1).lower(), m.group(2).strip()
        if key in ("words", "glue"):
            cur[key] = [w.strip(" *_`") for w in val.split(",") if w.strip(" *_`")]
        else:
            cur[key] = val
    return scenes


def read_texts(path):
    """[{no, title, turns:[(speaker, line)]}, ...] from a batch texts.md.

    Same two shapes vocab.parse_texts keys off — `## Text N — Title` and `A: …` — but
    the speaker letter is kept here, because the reader lays it out in the margin.
    """
    texts, cur = [], None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        m = re.match(r"^##\s+Text\s+(\d+)\s*[—–-]\s*(.+)$", line)
        if m:
            cur = {"no": int(m.group(1)), "title": m.group(2).strip(), "turns": []}
            texts.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^([A-Z]):\s+(.*)$", line)
        if m:
            cur["turns"].append((m.group(1), m.group(2)))
    return texts


def read_chunk_words(path):
    """The batch's load-bearing words, in chunks.md order.

    chunks.md is still the spine of the chunks page — it is the list of words the batch
    was actually built around — but only its headings are read. The collocation tables
    under them are not re-rendered: DWDS keeps a better, live copy of exactly that at
    /wp, so the page links there instead. A heading with no table under it was a word
    the corpus had nothing to say about, and is dropped the way it always was.
    """
    words, word, rows = [], None, 0
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^##\s+(?!#)(.+)$", line)
        if m:
            word, rows = m.group(1).strip(), 0
            continue
        if word is None or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("chunk", "") or set(cells[0]) <= set("-: "):
            continue
        rows += 1
        if rows == 1:
            words.append(word)
    return words


# ---------------------------------------------------------------- the ledger

def ledger(con):
    """Every word, plus where the ledger says it was first seen."""
    rows = list(con.execute("SELECT * FROM words WHERE 1=1" + REGIONAL_SQL))
    # alphabetical by the word itself, not by the article or the "(sich)" it carries
    rows.sort(key=lambda r: (fold(bare(r["lemma"])), r["lemma"]))
    seen = {}
    for r in con.execute("SELECT word_id, batch, text_no, title FROM uses"):
        seen[r["word_id"]] = (r["batch"], r["text_no"], r["title"])
    return rows, seen


def attest(pool, texts):
    """{text_no: {word_id: surface}} — every target and glue word each dialogue realises.

    vocab.scan_file answers this for the file as a whole and stops at a word's first
    hit. The reader needs it per text and without the break.

    This finds surfaces, which is what the reader highlights. It is NOT the coverage
    number: the ledger also carries hand-recorded uses (`vocab.py use`) for words no
    matcher can reach — three in batch 2 — so counting from here alone would under-report.
    `covered_in` below is the union, and every count on the site comes from that.
    """
    forms = {r["id"]: list(dict.fromkeys(variants(r["lemma"]) + csv_forms(r["forms"])))
             for r in pool}
    out = {}
    for t in texts:
        toks = [re.findall(r"[%s-]+" % WORD_CHAR, line) for _, line in t["turns"]]
        hits = {}
        for r in pool:
            for tokens in toks:
                hit = next((h for f in forms[r["id"]] if (h := phrase_matches(tokens, f))), None)
                if hit:
                    hits[r["id"]] = hit
                    break
        out[t["no"]] = hits
    return out


def covered_in(hits, seen, batch, text_no):
    """Word ids this text covers: matched surfaces plus the ledger's hand-recorded uses."""
    ids = set(hits.get(text_no, {}))
    ids |= {wid for wid, (b, no, _) in seen.items() if b == batch and no == text_no}
    return ids


# ---------------------------------------------------------------- html plumbing

def e(s):
    return html.escape(str(s), quote=True)


def page(title, depth, body, cls=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{up}assets/site.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='13' font-size='14'>📖</text></svg>">
</head>
<body class="{cls}">
{body}
</body>
</html>
"""


def write(out, relpath, text):
    dest = os.path.join(out, relpath)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(text)


def highlight(line, marks):
    """Wrap every attested target surface in the line with its gloss popover.

    Case-insensitive so a word that opens a sentence still gets marked — German
    capitalises its nouns anyway, and only this text's own target surfaces are in
    the pattern, so there is nothing else for a loose match to hit.
    """
    if not marks:
        return e(line)
    pat = "|".join(re.escape(s) for s in sorted(marks, key=len, reverse=True))
    rx = re.compile(r"(?<![%s])(%s)(?![%s])" % (WORD_CHAR, pat, WORD_CHAR), re.IGNORECASE)
    lookup = {s.lower(): v for s, v in marks.items()}
    out, last = [], 0
    for m in rx.finditer(line):
        lemma, gloss = lookup[m.group(1).lower()]
        out.append(e(line[last:m.start()]))
        tip = f"<b>{e(lemma)}</b>" + (f" — {e(gloss)}" if gloss else "")
        out.append(f'<span class="tw" tabindex="0"><mark>{e(m.group(1))}</mark>'
                   f'<span class="tip">{tip}</span></span>')
        last = m.end()
    out.append(e(line[last:]))
    return "".join(out)


def anchor(word):
    return "w-" + re.sub(r"[^a-z0-9]+", "-", fold(word)).strip("-")


# ---------------------------------------------------------------- the reader (Lesesaal)

def render_text(batch, topic, text, hits, scene, words_by_id, prev_t, next_t):
    """One dialogue and nothing else — the page is for reading aloud from.

    No word list, no coverage rail: that bookkeeping belongs on the batch page, and a
    margin full of vocabulary is exactly what pulls the eye off the German. The only
    thing the ledger contributes here is the gloss behind each target word.
    """
    marks = {s: (words_by_id[w]["lemma"], words_by_id[w]["gloss"])
             for w, s in hits.items() if words_by_id[w]["kind"] == "target"}

    turns = []
    for who, line in text["turns"]:
        turns.append(f'<div class="turn"><div class="who">{e(who)}</div>'
                     f'<p class="line">{highlight(line, marks)}</p></div>')

    prev_link = (f'<a href="text-{prev_t["no"]}.html">← <b>Text {prev_t["no"]}</b> — {e(prev_t["title"])}</a>'
                 if prev_t else '<a href="index.html">← Szenenplan</a>')
    next_link = (f'<a href="text-{next_t["no"]}.html"><b>Text {next_t["no"]}</b> — {e(next_t["title"])} →</a>'
                 if next_t else '<a href="index.html">Szenenplan →</a>')

    # The premise is English planning prose. It belongs on this page — it is the picture
    # the text is supposed to build — but not above the German, which is what gets read
    # first and memorised. So it opens only when asked for.
    premise = ""
    if scene and scene["premise"]:
        angle = f'<p class="angle">{e(scene["angle"])}</p>' if scene["angle"] else ""
        premise = (f'<details class="scenenote"><summary>Was passiert hier?</summary>'
                   f'<p>{e(scene["premise"])}</p>{angle}</details>')
    body = f"""<div class="lese">
  <div class="band">
    <a href="index.html">Batch {batch} · {e(topic)}</a>
    <span>Text {text["no"]}</span>
  </div>
  <article class="read">
    <p class="kicker">Szene {text["no"]}</p>
    <h1>{e(text["title"])}</h1>
    {premise}
    {"".join(turns)}
  </article>
  <nav class="pager">{prev_link}{next_link}</nav>
</div>
<script src="../../assets/site.js"></script>"""
    return page(f'{text["title"]} — Batch {batch}', 2, body, cls="lesesaal")


# ---------------------------------------------------------------- batch page

def render_batch(batch, topic, scenes, texts, covered, words_by_id, batch_words, has_chunks):
    by_no = {t["no"]: t for t in texts}
    everywhere = set().union(*covered.values()) if covered else set()
    used = {w["id"] for w in batch_words if w["id"] in everywhere}
    cards = []
    for sc in scenes:
        t = by_no.get(sc["no"])
        seen = {words_by_id[i]["lemma"] for i in covered.get(sc["no"], set())}
        n_hit = sum(1 for w in sc["words"] if w in seen)
        head = (f'<a class="scene" href="text-{t["no"]}.html">' if t else '<div class="scene idle">')
        tail = "</a>" if t else "</div>"
        status = (f'<span class="meta">{n_hit}/{len(sc["words"])} Wörter im Text</span>'
                  if t else '<span class="meta">noch nicht geschrieben</span>')
        cards.append(f"""{head}
      <div class="n">Szene {sc["no"]}</div>
      <h3>{e(sc["title"])}</h3>
      <p class="premise">{e(sc["premise"])}</p>
      {status}{tail}""")

    chunks_link = ('<a class="side" href="chunks.html">Wortprofil &amp; Belege →<span>'
                   'zu jedem tragenden Wort das DWDS-Wortprofil und jeder Satz, '
                   'in dem wir es benutzt haben</span></a>'
                   if has_chunks else "")
    body = f"""<header class="topbar">
  <a class="home" href="../../index.html">← Alle Themen</a>
  <span class="crumb">Batch {batch:02d}</span>
</header>
<main class="wrap">
  <h1 class="pagetitle">{e(topic)}</h1>
  <div class="statrow">
    <div class="stat"><b>{len(texts)}</b><span>Dialoge</span></div>
    <div class="stat"><b>{len(batch_words)}</b><span>Zielwörter</span></div>
    <div class="stat"><b>{len(used)}</b><span>davon im Text belegt</span></div>
    <div class="stat"><b>{100 * len(used) // max(len(batch_words), 1)}%</b><span>Abdeckung</span></div>
  </div>
  {chunks_link}
  <div class="scenes">{"".join(cards)}</div>
</main>"""
    return page(f"Batch {batch:02d} — {topic}", 2, body, cls="kartei")


# ------------------------------------------------------- chunks page: the two sources

# The Wortprofil as the user reads it, their filter settings baked in; only `q` and
# `pos` change per word. Nothing here fetches it. https://www.dwds.de/robots.txt
# disallows /wp for robots outright — tools/wortprofil.py carries the full notice — so
# the page hands over a link and the reader opens it, which is an ordinary page view.
DWDS_WP = ("https://www.dwds.de/wp/?q={q}&comp-method=diff&comp=&display=lemma&pos={pos}"
           "&minstat=3&minfreq=100&by=logDice&limit=15&view=table&table=&mode=")


def dwds_link(word, row):
    """The DWDS Wortprofil URL for one chunk word.

    `q` is the chunks.md heading itself: those headings came from the Wortprofil in the
    first place, so they are already the lemma DWDS knows. `pos` only narrows it when
    the ledger's headword makes the part of speech plain — an article means a noun, a
    `hat`/`ist` principal part means a verb. Empty otherwise: /wp resolves a bare lemma
    by itself, and a wrong pos would return an empty table.
    """
    pos = ""
    if row is not None:
        if row["lemma"].strip().split(" ")[0].lower() in ("der", "die", "das"):
            pos = "Substantiv"
        elif re.search(r",\s*(hat|ist)\s+\w", row["forms"] or ""):
            pos = "Verb"
    return DWDS_WP.format(q=quote(word), pos=pos)


SENT_SPLIT = re.compile(r'(?<=[.!?…])\s+(?=[A-ZÄÖÜ„»"(])')
ABBREV = ("dr.", "fr.", "hr.", "nr.", "st.", "ca.", "bzw.", "usw.", "z.", "b.")


def sentences(line):
    """One dialogue turn cut into the sentences this page quotes.

    A turn runs to four sentences and usually only one of them carries the word, so
    quoting whole turns would bury what the reader came for. A stop only splits before
    a capital — German capitalises its nouns, so that costs nothing — and never after a
    title: `Dr. Sänger` is the one abbreviation the corpus actually contains.
    """
    out = []
    for part in SENT_SPLIT.split(line):
        part = part.strip()
        if not part:
            continue
        if out and out[-1].rsplit(" ", 1)[-1].lower() in ABBREV:
            out[-1] += " " + part
        else:
            out.append(part)
    return out


def exact_owners(pool):
    """{surface: word_id} for every single-word form the ledger spells out.

    vocab's matcher folds umlauts and strips inflection, which is right for its own
    question ("does this text realise this word?") but too loose for this one ("which
    word is this sentence a sighting of?"): it lets `die Küche` claim the token
    *Kuchen*. A form the ledger spells out exactly belongs to the word that spells it,
    and no fuzzy claim survives against it.

    Spelling is taken literally — umlauts and capital both. That is the whole point of
    the map: `Küchen` and `Arm` must not be answered by `der Kuchen` and `arm`. It only
    ever rejects, so the one thing it gets wrong — a verb capitalised at the start of a
    sentence, where `Trinken` is not the noun the map knows — is the harmless direction:
    the surface is simply not in it, and the matcher's claim stands.
    """
    out = {}
    for r in pool:
        for f in variants(r["lemma"]) + csv_forms(r["forms"]):
            if " " not in f:
                out.setdefault(f, r["id"])
    return out


def belege(word, row, corpus, owner):
    """[(batch, slug, text, sentence, surface), ...] — every sighting in every dialogue.

    The corpus is one house across all batches, so a word keeps turning up after its
    own batch is done; those later sightings are the interesting ones and the page
    would be poorer for cutting them.
    """
    wid = row["id"] if row is not None else None
    forms = ((variants(row["lemma"]) + csv_forms(row["forms"])) if row is not None
             else [word])
    forms = list(dict.fromkeys(forms))
    out = []
    for batch, slug, text in corpus:
        for _, line in text["turns"]:
            for s in sentences(line):
                toks = re.findall(r"[%s-]+" % WORD_CHAR, s)
                hit = next((h for f in forms if (h := phrase_matches(toks, f))), None)
                if hit and owner.get(hit, wid) == wid:
                    out.append((batch, slug, text, s, hit))
    return out


def mark(sentence, surface):
    """The word itself, marked in its sentence — and nothing more.

    Deliberately not `highlight`: that hangs a gloss popover off every marked word,
    which earns its place in a dialogue you are reading and would be pure noise on a
    list of a hundred sightings of words you already have the gloss for above.
    """
    rx = re.compile(r"(?<![%s])(%s)(?![%s])" % (WORD_CHAR, re.escape(surface), WORD_CHAR),
                    re.IGNORECASE)
    out, last = [], 0
    for m in rx.finditer(sentence):
        out.append(e(sentence[last:m.start()]))
        out.append(f"<mark>{e(m.group(1))}</mark>")
        last = m.end()
    out.append(e(sentence[last:]))
    return "".join(out)


# ---------------------------------------------------------------- chunks page

def render_chunks(batch, topic, words, index, corpus, owner, seen, text_at):
    """Per load-bearing word: the live Wortprofil, and every line we have written with it.

    This used to reprint a filtered snapshot of the collocation tables. DWDS serves the
    same tables live, better, and with every knob exposed, so the profile is now one
    link — and the space goes to the half no one else can render, which is the word
    standing in our own sentences, each one a click from the dialogue it comes from.
    """
    def link(b, no):
        """The dialogue at (batch, text no), as href and label from where we stand."""
        bslug, title = text_at[(b, no)]
        href = f'text-{no}.html' if b == batch else f'../{bslug}/text-{no}.html'
        label = f'Text {no} · {e(title)}' if b == batch \
            else f'Batch {b:02d} · Text {no} · {e(title)}'
        return href, label

    blocks, total = [], 0
    for w in words:
        row = index.get(w) or index.get(fold(w))
        hits = belege(w, row, corpus, owner)
        hits.sort(key=lambda h: (h[0] != batch, h[0], h[2]["no"]))
        total += len(hits)

        lis = []
        for b, _, t, sentence, surface in hits:
            href, label = link(b, t["no"])
            lis.append(f'<li><p class="de">{mark(sentence, surface)}</p>'
                       f'<a class="src" href="{href}">{label}</a></li>')

        # A word the matcher cannot reach — `das Ei` in *Eier*, `erschrecken` in
        # *erschrocken* — may still be recorded in the ledger by hand. The sentence
        # cannot be cut out automatically, but the dialogue it is in is known, and
        # saying nothing here would contradict every coverage number on the site.
        recorded = seen.get(row["id"]) if row is not None else None
        if lis:
            found = f'<ol class="belege">{"".join(lis)}</ol>'
        elif recorded and (recorded[0], recorded[1]) in text_at:
            href, label = link(recorded[0], recorded[1])
            found = (f'<p class="nobeleg">im Ledger belegt, aber nicht automatisch '
                     f'aus dem Satz zu schneiden — <a class="src" href="{href}">'
                     f'{label}</a></p>')
        else:
            found = '<p class="nobeleg">noch in keinem Dialog</p>'

        head = e(row["lemma"]) if row is not None else e(w)
        gloss = (f'<span class="g">{e(row["gloss"])}</span>'
                 if row is not None and row["gloss"] else "")
        blocks.append(f"""<section class="wp" id="{anchor(w)}">
  <h2><span class="w">{head}</span>{gloss}
    <a class="dwds" href="{e(dwds_link(w, row))}" target="_blank"
       rel="noopener">DWDS-Wortprofil ↗</a></h2>
  {found}
</section>""")

    body = f"""<header class="topbar">
  <a class="home" href="index.html">← Batch {batch:02d}</a>
  <span class="crumb">Wortprofil &amp; Belege</span>
</header>
<main class="wrap">
  <h1 class="pagetitle">Wortprofil &amp; Belege</h1>
  <p class="lede">Die tragenden Wörter aus {e(topic)}. Zu jedem Wort das
  DWDS-Wortprofil — was ein Muttersprachler mit dem Wort tatsächlich sagt, live und
  vollständig, statt einer Kopie davon — und darunter jeder Satz, den wir selbst damit
  geschrieben haben, mit dem Weg zurück in seinen Dialog.</p>
  <p class="wpcount">{len(words)} Wörter · {total} Belege aus allen Batches</p>
  <div class="wplist">{"".join(blocks)}</div>
</main>
<script src="../../assets/site.js"></script>"""
    return page(f"Wortprofil & Belege — Batch {batch:02d}", 2, body, cls="kartei")


# ---------------------------------------------------------------- the index (Kartei)

def render_index(rows, seen, written, topics, dirslug):
    targets = [r for r in rows if r["kind"] == "target"]
    glue = [r for r in rows if r["kind"] == "glue"]
    covered = sum(1 for r in targets if r["id"] in seen)
    dialogues = sum(len(v) for v in written.values())

    # A plain numbered list, not 23 cards: only two of them are anywhere to go, and the
    # cram order is the point — a card grid buries a sequence under decoration.
    cards = []
    for lo, hi, stage, stage_name in STAGES:
        cards.append(f'<div class="stagehead"><b>{stage}</b><span>{e(stage_name)}</span></div>')
        cards.append('<ol class="topics">')
        for b in range(lo, hi + 1):
            if b not in topics:
                continue
            n = sum(1 for r in targets if r["batch"] == b)
            if b in written:
                cards.append(
                    f'<li><a href="batch/{dirslug[b]}/index.html">'
                    f'<span class="n">{b:02d}</span><span class="t">{e(topics[b])}</span>'
                    f'<span class="m">{n} Wörter · {len(written[b])} Dialoge</span></a></li>')
            else:
                cards.append(
                    f'<li class="idle"><div>'
                    f'<span class="n">{b:02d}</span><span class="t">{e(topics[b])}</span>'
                    f'<span class="m">{n} Wörter</span></div></li>')
        cards.append("</ol>")

    trs = []
    for r in rows:
        where, wcls = "—", "none"
        if r["id"] in seen:
            b, no, title = seen[r["id"]]
            if b in written and no:
                where = (f'<a href="batch/{dirslug[b]}/text-{no}.html">{no} · {e(title or "")}</a>')
            else:
                where = f"Batch {b}"
            wcls = "used"
        band = r["band"]
        topic = topics.get(r["batch"], r["topic"]) if r["kind"] == "target" else r["topic"]
        key = fold(r["lemma"] + " " + (r["gloss"] or ""))
        trs.append(
            f'<tr data-k="{e(key)}" data-kind="{r["kind"]}" data-used="{1 if r["id"] in seen else 0}"'
            f' data-w="{1 if r["batch"] in written else 0}">'
            f'<td class="lemma">{e(r["lemma"])}</td>'
            f'<td class="gloss">{e(r["gloss"] or "")}</td>'
            f'<td><span class="freq" style="--n:{band or 0}"'
            f' title="DWDS-Band {band if band is not None else "?"}"></span></td>'
            f'<td class="topic">{e(topic)}</td>'
            f'<td class="{wcls}">{where}</td></tr>')

    body = f"""<header class="topbar">
  <span class="crumb">Goethe B1 · Wortliste → Dialoge → Anki</span>
  <a class="home" href="https://github.com/a-a-abramov/german">Repo ↗</a>
</header>
<main class="wrap">
  <h1 class="pagetitle">Goethe B1 — 23 Themen, ein Hausflur</h1>
  <p class="lede">Die Wortliste ist nach Situationen geschnitten, nicht alphabetisch.
  Jedes Thema wird zu Szenen, jede Szene zu einem Dialog, der auswendig gelernt wird —
  die Anki-Karten kommen danach aus genau diesen Texten.</p>

  <div class="statrow big">
    <div class="stat"><b>{len(written)} <span class="of">/ {len(topics)}</span></b><span>Themen geschrieben</span></div>
    <div class="stat"><b>{covered} <span class="of">/ {len(targets)}</span></b><span>Zielwörter belegt</span></div>
    <div class="stat"><b>{dialogues}</b><span>Dialoge</span></div>
    <div class="stat"><b>{len(glue)}</b><span>Glue-Wörter im Pool</span></div>
  </div>

  {"".join(cards)}

  <section class="wordsec">
    <div class="wordhead">
      <h2>Die Wortliste</h2>
      <input id="q" type="search" placeholder="Wort oder Bedeutung suchen …" autocomplete="off">
    </div>
    <div class="filters">
      <button class="f" data-f="target" type="button">nur Zielwörter</button>
      <button class="f" data-f="glue" type="button">nur Glue</button>
      <button class="f" data-f="used" type="button">schon im Text</button>
      <button class="f" data-f="open" type="button">noch offen</button>
      <button class="f" data-f="written" type="button">geschriebene Themen</button>
      <span class="count" id="count">{len(rows)} Wörter</span>
    </div>
    <div class="tablewrap">
      <table id="words">
        <thead><tr><th>Lemma</th><th>Bedeutung</th><th>Band</th><th>Thema</th><th>Belegt in</th></tr></thead>
        <tbody>{"".join(trs)}</tbody>
      </table>
    </div>
  </section>
</main>
<script src="assets/site.js"></script>"""
    return page("Goethe B1 — Wortliste & Dialoge", 0, body, cls="kartei")


# ---------------------------------------------------------------- build

def build(out):
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out, exist_ok=True)

    con = sqlite3.connect(VOCAB_DB)
    con.row_factory = sqlite3.Row
    rows, seen = ledger(con)

    topics = {}
    for r in con.execute("SELECT batch, topic FROM words WHERE kind='target' AND batch IS NOT NULL"
                         " GROUP BY batch ORDER BY batch"):
        topics[r["batch"]] = r["topic"]

    by_id = {r["id"]: r for r in rows}

    # The chunks page quotes the whole corpus, not just its own batch, so every
    # dialogue has to be in hand before the first one is rendered. Two flat lookups
    # over the ledger go with it: the headword a chunks.md heading names, and who owns
    # a surface outright (see exact_owners).
    corpus = []
    for b, s, p in batch_dirs():
        tpath = os.path.join(p, "texts.md")
        if os.path.exists(tpath):
            corpus += [(b, s, t) for t in read_texts(tpath)]
    # Spelling first, folded second: `Arm` and `arm` fold together, and the heading
    # `## Arm` means the noun. Only a heading no spelling matches falls through.
    index = {}
    for r in rows:
        for v in variants(r["lemma"]):
            index.setdefault(v, r)
    for r in rows:
        for v in variants(r["lemma"]):
            index.setdefault(fold(v), r)
    owner = exact_owners(rows)

    # Where a dialogue lives, by (batch, text number) — the chunks page links across
    # batches, and the ledger's own record of a use carries no slug.
    text_at = {(b, t["no"]): (s, t["title"]) for b, s, t in corpus}

    written, dirslug = {}, {}
    for batch, slug, path in batch_dirs():
        dirslug[batch] = slug
        tpath = os.path.join(path, "texts.md")
        if not os.path.exists(tpath):
            continue
        topic = topics.get(batch, slug)
        texts = read_texts(tpath)
        scenes = read_scenes(os.path.join(path, "scenes.md")) \
            if os.path.exists(os.path.join(path, "scenes.md")) else []
        chunks = read_chunk_words(os.path.join(path, "chunks.md")) \
            if os.path.exists(os.path.join(path, "chunks.md")) else []
        pool = list(con.execute(
            "SELECT * FROM words WHERE (kind='glue' OR (kind='target' AND batch=?))"
            + REGIONAL_SQL, (batch,)))
        batch_words = [r for r in pool if r["kind"] == "target"]
        hits = attest(pool, texts)
        covered = {t["no"]: covered_in(hits, seen, batch, t["no"]) for t in texts}
        written[batch] = texts

        # one coverage answer for the whole site: the ledger's record where it has one
        # (it carries hand-recorded uses no matcher can reach), the matched text otherwise
        titles = {t["no"]: t["title"] for t in texts}
        for wid, (b, no, title) in list(seen.items()):
            if b == batch and not title:
                seen[wid] = (b, no, titles.get(no))
        for t in texts:
            for wid in hits[t["no"]]:
                seen.setdefault(wid, (batch, t["no"], t["title"]))

        by_no = {s["no"]: s for s in scenes}
        for i, t in enumerate(texts):
            write(out, f"batch/{slug}/text-{t['no']}.html", render_text(
                batch, topic, t, hits[t["no"]], by_no.get(t["no"]), by_id,
                texts[i - 1] if i else None,
                texts[i + 1] if i + 1 < len(texts) else None))
        write(out, f"batch/{slug}/index.html", render_batch(
            batch, topic, scenes, texts, covered, by_id, batch_words, bool(chunks)))
        if chunks:
            write(out, f"batch/{slug}/chunks.html",
                  render_chunks(batch, topic, chunks, index, corpus, owner, seen, text_at))
        print(f"  batch {batch:02d} {slug}: {len(texts)} texts, "
              f"{len(scenes)} scenes, {len(chunks)} chunk words")

    write(out, "index.html", render_index(rows, seen, written, topics, dirslug))

    assets = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site-assets")
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    for name in ("site.css", "site.js"):
        shutil.copyfile(os.path.join(assets, name), os.path.join(out, "assets", name))
    open(os.path.join(out, ".nojekyll"), "w").close()

    n = sum(len(f) for _, _, f in os.walk(out))
    print(f"  wrote {n} files to {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=OUT, help="output directory (default: site/)")
    ap.add_argument("--serve", action="store_true", help="serve the result on :8000")
    args = ap.parse_args()

    build(args.out)

    if args.serve:
        import http.server
        import socketserver
        os.chdir(args.out)
        print("  http://localhost:8000/  (ctrl-c to stop)")
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as s:
            s.serve_forever()


if __name__ == "__main__":
    main()

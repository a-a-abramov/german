#!/usr/bin/env python3
"""
site.py — build the static reader that lives on GitHub Pages.

WHY THIS EXISTS: `content/batches/` is the only directory a human reads, but it reads
as markdown in a text editor, which is the wrong shape for the two things actually done
with it — cramming one dialogue at a time, and asking the ledger where a word stands.
So this renders both:

    the index      curriculum/vocab.db seen from above — 23 topics, what is written,
                   what is owed, and every word in the ledger, searchable
    the reader     one dialogue per page, set to be read aloud from, with the scene's
                   owned words in the margin and a gloss on every target word

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


def read_chunks(path):
    """[{word, groups:[{relation, rows:[(chunk, logdice, freq)]}]}, ...] from chunks.md."""
    words, word, group = [], None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^##\s+(?!#)(.+)$", line)
        if m:
            word = {"word": m.group(1).strip(), "groups": [], "n": 0}
            words.append(word)
            group = None
            continue
        if word is None:
            continue
        m = re.match(r"^###\s+(.+)$", line)
        if m:
            group = {"relation": m.group(1).strip(), "rows": []}
            word["groups"].append(group)
            continue
        if group is None or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5 or cells[0] in ("chunk", "") or set(cells[0]) <= set("-: "):
            continue
        group["rows"].append((cells[0], cells[3], cells[4]))
        word["n"] += 1
    return [w for w in words if w["n"]]


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

    chunks_link = ('<a class="side" href="chunks.html">Belegte Chunks →<span>'
                   'attestierte Kollokationen zu jedem tragenden Wort</span></a>'
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


# ---------------------------------------------------------------- chunks page

def render_chunks(batch, topic, chunks):
    blocks = []
    for w in chunks:
        groups = []
        for g in w["groups"]:
            if not g["rows"]:
                continue
            rows = "".join(
                f'<tr><td class="de">{e(c)}</td><td class="num">{e(ld)}</td>'
                f'<td class="num">{e(fr)}</td></tr>' for c, ld, fr in g["rows"])
            groups.append(f'<p class="rel">{e(g["relation"])}</p>'
                          f'<table class="chunks"><thead><tr><th>Chunk</th>'
                          f'<th class="num">logDice</th><th class="num">Freq</th></tr></thead>'
                          f'<tbody>{rows}</tbody></table>')
        blocks.append(f"""<details id="{anchor(w["word"])}">
  <summary><span class="w">{e(w["word"])}</span><span class="c">{w["n"]} Chunks</span></summary>
  <div class="cg">{"".join(groups)}</div>
</details>""")
    body = f"""<header class="topbar">
  <a class="home" href="index.html">← Batch {batch:02d}</a>
  <span class="crumb">Chunks</span>
</header>
<main class="wrap">
  <h1 class="pagetitle">Belegte Chunks</h1>
  <p class="lede">Kollokationen aus dem OpenSubtitles-Korpus, gefiltert auf B1-Lemmata
  (Freq ≥ 20, logDice ≥ 4,0). Sie sind der Rohstoff der Dialoge in {e(topic)} — was ein
  Muttersprachler mit diesem Wort tatsächlich sagt, nicht was grammatisch ginge.</p>
  <div class="chunklist">{"".join(blocks)}</div>
</main>
<script src="../../assets/site.js"></script>"""
    return page(f"Chunks — Batch {batch:02d}", 2, body, cls="kartei")


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
        chunks = read_chunks(os.path.join(path, "chunks.md")) \
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
            write(out, f"batch/{slug}/chunks.html", render_chunks(batch, topic, chunks))
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

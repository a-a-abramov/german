# Building your own Wortprofil from OpenSubtitles

**Why this exists.** DWDS-Wortprofil has the best data but can't be accessed
programmatically (robots.txt `Disallow: /wp`, see `dwds-wortprofil-guide.md` §3.2).
Leipzig's API is open but gives no grammatical relations and is news-skewed. Both are
*journalistic* — and batches 1–8 (Wohnung, Körper, Essen, Kleidung, Familie) are
domestic and spoken. Film dialogue is the closest freely available register.

Building it yourself gets you **all three things at once**: relation-typed collocations,
a spoken register, and no access restrictions.

**Status: designed and costed, NOT yet run.** Every URL, size, and version below was
verified live on 2026-08-09. The dependency-label mapping in Step 3 is from memory of
the TIGER scheme and **must be checked empirically** — Step 3a is that check. Don't
trust the table until you've run it.

---

## What you're building

The same data model as Wortprofil: for each headword, a list of
`(relation, collocate, logDice, frequency)`. Then feed it into the existing
`tools/wortprofil.py` output format so the text-writer's workflow doesn't change.

```
Wohnung  ist Akkusativ-Objekt von  mieten    9.2   1843
Wohnung  hat Adjektivattribut      klein     8.1    920
```

---

## Step 0 — The corpus (verified 2026-08-09)

```bash
# OPUS OpenSubtitles v2024, German monolingual
curl -O https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2024/mono/de.txt.gz
```

| | |
|---|---|
| Size | **1.57 GB** gzipped (`content-length: 1572111961`, `application/gzip`) |
| Tokens | **950,557,327** |
| Documents | 173,728 |
| Version | v2024 (`latest: True`) |
| Format | one sentence per line, plain text |

Discovered via the OPUS API (follow redirects — without `-L` it echoes the path back):

```bash
curl -sL "https://opus.nlpl.eu/opusapi/?corpus=OpenSubtitles&source=de&preprocessing=mono&version=latest"
```

> **Licensing — read before you redistribute anything.** OPUS aggregates these from
> opensubtitles.org, where subtitles are user-contributed. OPUS distributes for research
> use; the underlying material's status is murkier than the CC BY 4.0 you get from
> Leipzig. For **personal study, kept on your own disk, not redistributed** this is
> fine — which is the entire scope of this project. Do not publish the derived
> collocation database. I did not find an explicit licence statement on the OPUS
> corpus page (it 404'd); if you ever want to share output, check first.

**Don't parse all 950M tokens.** Dependency parsing is ~1–3k tokens/sec/core. The full
corpus is days of CPU. **30–50M tokens is plenty** for B1 collocations — that's still
~2M sentences, and every word on the Goethe list will occur thousands of times. Start
with 5M to validate the pipeline end to end, then scale.

---

## Step 1 — Environment

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install spacy
python -m spacy download de_core_news_sm     # verified available for spaCy 3.8
```

Model choice (all confirmed present in spaCy 3.8's compatibility index):

| model | use |
|---|---|
| `de_core_news_sm` | **start here** — fastest, has the parser, good enough for counting |
| `de_core_news_lg` | better lemmas/vectors, ~3× slower |
| `de_dep_news_trf` | best accuracy, transformer, needs a GPU to be practical |

Accuracy matters less than you'd think here: you're aggregating over millions of
sentences, so parser noise averages out. Start `sm`, only move up if results look wrong.

---

## Step 2 — Sample and clean

Subtitle text needs light cleaning — speaker dashes, HTML italics, music notes.

```python
import gzip, re, itertools

BAD = re.compile(r"<[^>]+>|^[-–—]\s*|♪|\[[^\]]*\]")

def sentences(path, limit=2_000_000):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for line in itertools.islice(f, limit):
            s = BAD.sub("", line).strip()
            # subtitles are full of one-word interjections; they add noise, not signal
            if 20 < len(s) < 200 and s.count(" ") >= 3:
                yield s
```

---

## Step 3 — Parse and extract relation triples

spaCy's German models use **TIGER-scheme dependency labels**, not Universal Dependencies.

### Step 3a — VERIFY THE LABELS FIRST (do not skip)

```python
import spacy
nlp = spacy.load("de_core_news_sm")
doc = nlp("Der Mieter hat die kleine Wohnung im Zentrum schnell gemietet.")
for t in doc:
    print(f"{t.text:12} {t.lemma_:12} {t.pos_:6} {t.dep_:6} -> {t.head.text}")
```

Print this before writing any counting code. Confirm with your own eyes which label
lands on *Wohnung* (expect `oa`), on *Mieter* (expect `sb`), on *kleine* (expect `nk`).
**If the labels differ from the table below, trust the output, not the table.**

### The mapping (unverified — check against 3a)

| TIGER dep | Wortprofil relation | surfaces as |
|---|---|---|
| `sb` | ist Subjekt von | *die Wohnung kostet* |
| `oa` | ist Akkusativ-Objekt von | *eine Wohnung mieten* |
| `da` | ist Dativ-/Genitiv-Objekt von | |
| `ag` | hat Genitivattribut | *der Preis der Wohnung* |
| `nk` (ADJ child of NOUN) | hat Adjektivattribut | *eine kleine Wohnung* |
| `mo` / `op` (via ADP) | hat / ist in Präpositionalgruppe | *in der Wohnung* |
| `pd` | hat Prädikativ | *die Wohnung ist teuer* |
| `cj` | ist in Koordination mit | *Wohnung und Haus* |

For prepositional relations, take **two** hops: the preposition's head is the content
word, so record `(Wohnung, "in", wohnen)` as a single relation `in+wohnen` — that's what
makes `in die Wohnung` distinguishable from `in der Wohnung` downstream, which is the
one thing DWDS's own display *doesn't* give you (guide §1.4). You get case for free from
the determiner's morphology (`t.morph.get("Case")`) — **your version can be better than
theirs here.**

### The extraction loop

```python
from collections import Counter

pair = Counter()      # (head_lemma, relation, child_lemma) -> count
head = Counter()      # (head_lemma, relation) -> count
child = Counter()     # (relation, child_lemma) -> count

DEP2REL = {"sb": "ist Subjekt von", "oa": "ist Akkusativ-Objekt von",
           "da": "ist Dativ-/Genitiv-Objekt von", "ag": "hat Genitivattribut",
           "pd": "hat Prädikativ", "cj": "ist in Koordination mit"}

for doc in nlp.pipe(sentences("de.txt.gz"), batch_size=200, n_process=6):
    for t in doc:
        rel = DEP2REL.get(t.dep_)
        if t.dep_ == "nk" and t.pos_ == "ADJ" and t.head.pos_ == "NOUN":
            rel = "hat Adjektivattribut"
        if not rel or t.pos_ not in ("NOUN", "VERB", "ADJ", "PROPN"):
            continue
        h, c = t.head.lemma_, t.lemma_
        pair[(h, rel, c)] += 1
        head[(h, rel)] += 1
        child[(rel, c)] += 1
```

Disable what you don't need — it roughly doubles throughput:
`spacy.load("de_core_news_sm", exclude=["ner"])`.

---

## Step 4 — Score with logDice

Identical to the statistic DWDS uses, so the guide's §1.3 two-floor rule transfers:

```python
import math

def log_dice(f_ab, f_a, f_b):
    return 14 + math.log2(2 * f_ab / (f_a + f_b))

rows = []
for (h, rel, c), f_ab in pair.items():
    if f_ab < 5:                       # noise floor; raise as the corpus grows
        continue
    rows.append((h, rel, c, log_dice(f_ab, head[(h, rel)], child[(rel, c)]), f_ab))
```

Then apply exactly what `tools/wortprofil.py` already does: the **two floors**
(`freq ≥ 20 AND logDice ≥ 3.0`, retuned for your corpus size) and the **Goethe
A1∪A2∪B1 intersection** — import `in_b1` and `load_b1` straight from that module.

---

## Step 5 — Emit in the existing format

Write `(headword, relation, collocate, logDice, freq)` to a SQLite table or TSV, then
render with the same `RELATION_PATTERNS` map in `tools/wortprofil.py`. The text-writer's
Step 2b doesn't change — it just stops needing manually saved pages.

---

## Costing

| stage | cost |
|---|---|
| Download | 1.57 GB, once |
| Parse 5M tokens (validation run) | ~30–60 min on 6 cores |
| Parse 50M tokens (real run) | ~5–10 h on 6 cores, run it overnight |
| Score + filter | seconds |

**Do the 5M validation run first and eyeball `Wohnung`, `Tasse`, `Schrank`.** If
`mieten`, `trinken`, `Schrank` don't surface near the top, something's wrong with the
label mapping — go back to Step 3a. Don't spend 10 hours before that check passes.

---

## Why this beats both existing options

| | DWDS | Leipzig | this |
|---|:-:|:-:|:-:|
| Relation-typed | ✓ | ✗ | ✓ |
| Case information | ✗ | ✗ | **✓** (from morphology) |
| Spoken/domestic register | ✗ | ✗ | **✓** |
| Programmatic | ✗ | ✓ | ✓ |
| Corpus size | billions | 3M sentences | 950M tokens |

The one thing you give up is DWDS's editorial quality — their parser and corpus are
better than `de_core_news_sm` on 50M tokens of film dialogue. For *this* project, on
*these* batches, register beats polish.

**Prior art worth reading before you start:** DWDS's own Wortprofil implementation is
GPL-3.0 at github.com/zentrum-lexikographie/wordprofile. It's this exact pipeline,
production-grade — only their *database* is unpublished, not their code. If the
hand-rolled version stalls, point theirs at your corpus instead.

# German B1 — cram texts → Anki spaced repetition

This repo produces **two distinct types of content**, and every agent working here
must keep them clearly separated:

| # | Content type | Purpose | Lives in |
|---|---|---|---|
| **1** | **Cramming texts** — short, vivid German scenes | **Initial encoding.** The user reads them slowly, visualizes, handwrites them several times, and memorizes them by heart. Mnemonic, one-time deep learning. | `content/batches/NN-*/texts.md` |
| **2** | **Anki cards** — cloze + word→meaning | **Long-term maintenance.** Spaced-repetition review *after* a text is already memorized. | `content/batches/NN-*/anki-*.txt` |

**These are two stages of one memory, not two separate study systems.** The texts come
first (encoding by hand); the cards are cut *from those same texts* afterwards
(maintenance). The Anki cloze cards deliberately replay the exact scene the user built
while cramming — so the two never compete. Never generate Anki cards for a batch whose
texts don't exist yet: the cards are derived content.

---

## Repo map (orientation for agents)

Four top-level directories, one question each: **what am I learning** (`curriculum/`),
**what have I written** (`content/`), **what do I run** (`tools/`), **how does it work**
(`docs/`). Plus `data/`, which is git-ignored and rebuildable — nothing in it is authored.

```
README.md            ← this file: the method + the two content types

content/             ← THE STUDY MATERIAL. The only directory whose contents are read by
└── batches/            a human (and, later, by the reader front-end). Everything else
    └── NN-<topic>/     here exists to produce this.
        (bracketed steps are the text-writer skill's procedure steps)
        ├── scenes.md      ← [step 1] the batch's scenes: premise · angle · words
        ├── chunks.md      ← [step 2] attested collocations per load-bearing word
        ├── texts.md       ← [step 3] CONTENT TYPE 1: the cramming dialogues
        ├── anki-cloze.txt ← [step 5] CONTENT TYPE 2: cloze cards (Anki Cloze note type)
        └── anki-basic.txt ← [step 5] CONTENT TYPE 2: word→meaning cards (Anki Basic)
        Files appear in pipeline order, so a batch mid-flight has only the early ones.
        The NN prefix is a database key (`words.batch`) — a batch dir is never renumbered.

curriculum/          ← THE PLAN AND THE BOOKKEEPING: what is to be learned, and how far
├── goethe-b1-wortliste.csv ← SOURCE OF TRUTH: official Goethe B1 Wortliste (2,886 entries)
├── vocab.db          ← THE LEDGER: every word's batch, forms, gloss, frequency band,
│                        coverage and card state. Query it with tools/vocab.py.
├── assignments.tsv   ← the ledger's plain-text seed (diffable; vocab.py init reads it)
├── topics.md         ← 23 topics in concrete→abstract cram order, plus a non-binding
│                        bank of scene premises. No word lists — those are in the ledger.
└── glue-pool.md      ← why 326 closed-class function words are pooled instead of scened,
                         and how they get woven through every batch's texts.

tools/
├── paths.py          ← every repo path in one place; the other tools import it
├── vocab.py          ← THE LEDGER CLI: words, coverage, scan, skip, cards
├── wortprofil_db.py  ← collocations from data/wortprofil.db (the normal way)
├── wortprofil.py     ← same output from a hand-saved DWDS page (fallback, needs a browser)
├── leipzig.py        ← collocations via the Leipzig API (CC BY 4.0, scriptable)
├── wordfreq.py       ← DWDS frequency bands (already imported into the ledger)
├── site.py           ← THE READER: renders the ledger + content/ into site/ (git-ignored)
├── site-assets/      ← the reader's one stylesheet and one script, copied in verbatim
├── publish-site.sh   ← builds site/ and pushes it to the gh-pages branch
└── opus/             ← the pipeline that BUILDS wortprofil.db, on a separate machine.
                         Its /home/andrey/… and /work/… paths are remote, not repo paths.

docs/                ← the method write-ups. Read in this order:
├── collocations-method.md ← WHY the texts are built from attested CHUNKS, not bare words,
│                            and how to read a Wortprofil. Start here.
├── collocations-build.md  ← the recipe for building your own relation-typed collocation
│                            DB. Built 2026-08-13; its Step 3 label table proved wrong in
│                            four ways — corrections in tools/opus/IMPLEMENTATION.md.
└── collocations-query.md  ← MANUAL: querying the finished database day to day.

data/                ← (git-ignored, rebuildable, never committed)
├── wortprofil.db     ← 1.5 GB OpenSubtitles collocation DB, built by tools/opus/
└── dwds/             ← DWDS downloads: Goethe A1/A2/B1 lemma lists (a live dependency —
                         they are the B1 filter on every chunk harvest), the 27 MB
                         Lemmadatenbank, and any Wortprofil page saved by hand.

.claude/skills/text-writer/ ← THE BRIEF for the agent that writes the texts + cards
```

There is no per-batch word list any more: a batch's words, their forms and their coverage
live in the ledger (`python3 tools/vocab.py words --batch 2`). The remaining work is, per
topic in `curriculum/topics.md`: write the texts (content type 1), then cut the cards
(content type 2) from them — **the agent doing that should invoke the `text-writer`
skill; it is the complete brief.**

### Reading the texts

`texts.md` is the authored source of truth and stays markdown — it is what the user
reviews and what `vocab.py scan` parses. The reader front-end renders it:

    python3 tools/site.py --serve     # build + http://localhost:8000
    tools/publish-site.sh             # build + push to gh-pages

live at **https://a-a-abramov.github.io/german/**. It is a pure function of
`curriculum/vocab.db` and `content/batches/` — nothing is authored in it, `site/` is
git-ignored, and only the `gh-pages` branch carries HTML. Two surfaces:

- **the index** — the 23 topics in cram order with their real state, and every word in
  the ledger, searchable, each linking to the text that taught it
- **the reader** — one dialogue per page, big serif, the scene's owned words in the
  margin, a gloss on every target word, and the batch's chunk tables one click away

Which target words a dialogue realises is not recomputed here: `site.py` imports
`vocab.py`'s matcher (`variants` / `csv_forms` / `phrase_matches`), so the site and
`vocab.py scan` can never disagree about what a text covers. The one difference is that
`scan_file` stops at a word's first sighting — the ledger records first sightings — while
the reader wants every sighting in every text.

---

## The source of truth

`curriculum/goethe-b1-wortliste.csv` — the official list extracted by wejn.org
(https://wejn.org/2023/12/extracting-data-from-goethe-zertifikat-b1-wortliste/,
repo https://github.com/wejn/goethe-b1-wortliste, © Goethe-Institut 2016, personal
use only). **2,886 entries.** Two columns:
- headword **with forms baked in** — nouns as `der Teppich, -e`, verbs as
  `abbiegen, biegt ab, bog ab, ist abgebogen` → copy straight into word tables.
- official example sentence(s) → reusable as authentic B1 context.

**Every batch is validated against this file** (a target word must appear as a headword);
that's how batch 01's invented word "Vorhang" got caught and replaced with the on-list
`das Kissen`.

**Standard German only.** The list also carries the Austrian and Swiss doublets of words it
lists for Germany (`die Stiege` for *Treppe*, `das Velo` for *Fahrrad*, `der Erdapfel` for
*Kartoffel*). The ledger records each entry's region tag and excludes the **54 A/CH-only**
entries from every batch's targets — they are out of scope, not lost (`vocab.py words
--batch N --regional` shows them). Entries tagged `(D, A)` or `(D, CH)` stay: those are
standard German that happens to be shared.

---

## Per-batch pipeline

1. **Pick a topic** from `curriculum/topics.md` — batches are ordered concrete→abstract;
   start with Stage A (Wohnung, Körper, Essen…). `vocab.py status` shows what's left.
2. **Design the scenes** — `scenes.md`: read the batch's whole word list
   (`vocab.py words --batch N`) and group it **by situation**, never by list order. This is
   the creative step; the list's sort order must never become the scenes' structure.
3. **Harvest the chunks** — `chunks.md`, from the local collocation database:
   `python3 tools/wortprofil_db.py <Wörter> --min-freq 20 --min-dice 4 --top 15`
   (see `docs/collocations-query.md`). The texts get built out of these attested combinations.
4. **Write the cramming texts (content type 1)** in three passes — initial draft → review
   and enrichment → final pass — each of which puts naturalness first: short, imaginable
   German-only **dialogues** (4–8 turns, `A:` / `B:` format), every word in its canonical
   B1 sense, glue-pool words woven in. **90–95% coverage of natural-sounding dialogue beats
   100% that reads like a word list**; leftovers are `vocab.py skip`ped with a reason.
5. **Record coverage** — `vocab.py scan content/batches/NN-*/texts.md --batch N --apply`, correcting
   the scanner's misses by hand.
6. **Cram** (the user's loop) — read slow → visualize → handwrite several times → recite.
7. **Generate the Anki cards (content type 2)** — *from the finalized texts*: one cloze
   card per target word (cut verbatim from its utterance) + one word→meaning card.

## Batch sizing

**The scene is the encoding unit; the batch is the whole topic.** Don't conflate them —
a batch is days of work, not one sitting.

- **1 scene = 1 text = 10–18 target words.** This is the unit sized to survive "know it by
  heart" in one encoding sitting + a few days of rewriting.
- **1 batch = 1 topic = one text per scene**, with the scenes designed fresh for each batch
  (8–14 of them, grouped by situation). Topics vary widely: 8–214 target words, see the
  table in `topics.md` §2. Batch 1 came to 11 texts for 148 words; the largest is Batch 16
  (Freizeit, Medien & Technik) at 214 words, the smallest Batch 4 (Tiere) at 8.
- So a batch is cranked scene by scene, over several sittings — the *batch* is the unit of
  planning and card generation, the *scene* is the unit of memorization.

## The glue pool

Pure function words (`obwohl, zwischen, derselbe, ziemlich`…) have no mental picture, so
they get **no standalone scenes**. Instead the text-writer draws from `glue-pool.md` while
writing *every* batch's texts, as connective tissue. **Rule: it's OK to repeat these words;
it's NOT OK to leave them out.** Coverage is tracked in the ledger across the whole corpus,
not per batch: `vocab.py glue --open` lists what no finished text has used yet.

## Why this shape

- **Cloze-from-your-own-text** is the bridge between the two content types: the card
  reactivates the exact scene built by hand, so cramming and spaced repetition are the
  *same* memory, not two competing ones.
- **Word→meaning** cards guarantee context-free recall so a word isn't stuck to one sentence.
- **Ledger-held forms** (gender/plural/principal parts, CSV-verified) so a nice story never
  hides a wrong article.
- **Tracking outside the prose.** Word lists inside the plan used to double as the writing
  brief, and the texts came out shaped like the lists. The plan is prose, the ledger is a
  database, and the scenes are designed from meaning.

## Anki import

- `anki-cloze.txt` → import as **Cloze** note type, fields tab-separated (Text, Back Extra).
- `anki-basic.txt` → import as **Basic** note type (Front, Back).
- Field separator = **Tab**, Allow HTML = off.

## Batches

Run `python3 tools/vocab.py status` for the live picture — it is the counter; don't mirror
its numbers here.

- **`content/batches/01-in-der-wohnung/`** — Stage A, topic 1. Rewritten with the scene-design +
  three-stage method: `scenes.md` groups the 142 words into 11 situations, `texts.md` has
  one dialogue each (142/142 covered, 154 glue words). **Awaiting the cram + review pass**;
  Anki cards are held until then, so `anki-*.txt` don't exist yet.
- **`content/batches/02-koerper-gesundheit/`** — chunks harvested, nothing written.
- **Next:** write batch 02 with the `text-writer` skill, or finish batch 01 by generating
  its cards.

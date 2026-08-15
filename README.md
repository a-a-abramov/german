# German B1 — cram texts → Anki spaced repetition

This repo produces **two distinct types of content**, and every agent working here
must keep them clearly separated:

| # | Content type | Purpose | Lives in |
|---|---|---|---|
| **1** | **Cramming texts** — short, vivid German scenes | **Initial encoding.** The user reads them slowly, visualizes, handwrites them several times, and memorizes them by heart. Mnemonic, one-time deep learning. | `batch-NN-*/texts.md` |
| **2** | **Anki cards** — cloze + word→meaning | **Long-term maintenance.** Spaced-repetition review *after* a text is already memorized. | `batch-NN-*/anki-*.txt` |

**These are two stages of one memory, not two separate study systems.** The texts come
first (encoding by hand); the cards are cut *from those same texts* afterwards
(maintenance). The Anki cloze cards deliberately replay the exact scene the user built
while cramming — so the two never compete. Never generate Anki cards for a batch whose
texts don't exist yet: the cards are derived content.

---

## Repo map (orientation for agents)

```
README.md                     ← this file: the method + the two content types
.claude/skills/text-writer/   ← THE BRIEF for the agent that writes the texts + cards
WORTPROFIL.md                 ← MANUAL: querying the OpenSubtitles collocation database
goethe-b1-wortliste.csv       ← SOURCE OF TRUTH: official Goethe B1 Wortliste (2,886 entries)
groundwork/
├── vocab.db                  ← THE LEDGER: every word's batch, forms, gloss, frequency
│                                band, coverage and card state. Query with tools/vocab.py.
├── assignments.tsv           ← the ledger's plain-text seed (diffable; vocab.py init reads it)
├── topics.md                 ← the plan: 23 topics, concrete→abstract cram order, plus a
│                                non-binding bank of scene premises. No word lists.
├── glue-pool.md              ← why 326 closed-class function words are pooled instead of
│                                scened, and how they get woven through every batch's texts.
├── dwds-wortprofil-guide.md  ← COLLOCATION METHOD: how to read DWDS-Wortprofil, and why
│                                the texts are built from attested CHUNKS, not bare words.
│                                Part Five = where to get collocations programmatically.
└── diy-wortprofil-opensubtitles.md ← the original recipe for building your own
                                 relation-typed collocation DB. BUILT 2026-08-13 — but its
                                 Step 3 label table proved wrong in four ways; corrections
                                 are in tools/opus/IMPLEMENTATION.md.
tools/
├── wortprofil.py             ← saved Wortprofil page → B1-filtered chunk table
├── wortprofil_db.py          ← SAME output, queried from opus-de/wp.db (no browser needed)
├── leipzig.py                ← collocations via the Leipzig API (CC BY 4.0, scriptable)
├── vocab.py                  ← THE LEDGER CLI: words, coverage, scan, skip, cards
├── wordfreq.py               ← DWDS frequency bands (already imported into the ledger)
└── opus/                     ← the pipeline that BUILDS wp.db (see its IMPLEMENTATION.md)
opus-de/                      ← (git-ignored) wp.db, 1.5 GB. Built, not committed.
dwds-cache/                   ← (git-ignored) Wortprofil pages you saved + Goethe A1/A2/B1
                                 lemma lists. Not committed: DWDS/Goethe content.
batch-NN-<topic>/             ← one dir per batch = one topic. Files appear in pipeline
                                 order, so a batch mid-flight has only the early ones:
        (bracketed steps are the text-writer skill's procedure steps)
├── scenes.md                 ← [step 1] the batch's scenes: premise · angle · words
├── chunks.md                 ← [step 2] attested collocations per load-bearing word
├── texts.md                  ← [step 3] CONTENT TYPE 1: the cramming dialogues
├── anki-cloze.txt            ← [step 5] CONTENT TYPE 2: cloze cards (import as Cloze note type)
└── anki-basic.txt            ← [step 5] CONTENT TYPE 2: word→meaning cards (import as Basic note type)

batch-01-in-der-wohnung/      ← the only finished batch: 11 dialogues, 142/142 words
                                 covered (scenes.md + texts.md). Cards not cut yet.
batch-02-koerper-gesundheit/  ← chunks harvested; no texts yet.
```

There is no per-batch word list any more: a batch's words, their forms and their coverage
live in the ledger (`python3 tools/vocab.py words --batch 2`). The remaining work is, per
topic in `groundwork/topics.md`: write the texts (content type 1), then cut the cards
(content type 2) from them — **the agent doing that should invoke the `text-writer`
skill; it is the complete brief.**

---

## The source of truth

`goethe-b1-wortliste.csv` — the official list extracted by wejn.org
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

1. **Pick a topic** from `groundwork/topics.md` — batches are ordered concrete→abstract;
   start with Stage A (Wohnung, Körper, Essen…). `vocab.py status` shows what's left.
2. **Design the scenes** — `scenes.md`: read the batch's whole word list
   (`vocab.py words --batch N`) and group it **by situation**, never by list order. This is
   the creative step; the list's sort order must never become the scenes' structure.
3. **Harvest the chunks** — `chunks.md`, from the local collocation database:
   `python3 tools/wortprofil_db.py <Wörter> --min-freq 20 --min-dice 4 --top 15`
   (see `WORTPROFIL.md`). The texts get built out of these attested combinations.
4. **Write the cramming texts (content type 1)** in three passes — initial draft → review
   and enrichment → final pass — each of which puts naturalness first: short, imaginable
   German-only **dialogues** (4–8 turns, `A:` / `B:` format), every word in its canonical
   B1 sense, glue-pool words woven in. **90–95% coverage of natural-sounding dialogue beats
   100% that reads like a word list**; leftovers are `vocab.py skip`ped with a reason.
5. **Record coverage** — `vocab.py scan batch-NN-*/texts.md --batch N --apply`, correcting
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

- **`batch-01-in-der-wohnung/`** — Stage A, topic 1. Rewritten with the scene-design +
  three-stage method: `scenes.md` groups the 142 words into 11 situations, `texts.md` has
  one dialogue each (142/142 covered, 154 glue words). **Awaiting the cram + review pass**;
  Anki cards are held until then, so `anki-*.txt` don't exist yet.
- **`batch-02-koerper-gesundheit/`** — chunks harvested, nothing written.
- **Next:** write batch 02 with the `text-writer` skill, or finish batch 01 by generating
  its cards.

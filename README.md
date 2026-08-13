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
TEXT-WRITER.md                ← self-contained brief for the agent that writes the texts + cards
WORTPROFIL.md                 ← MANUAL: querying the OpenSubtitles collocation database
goethe-b1-wortliste.csv       ← SOURCE OF TRUTH: official Goethe B1 Wortliste (2,886 entries)
groundwork/
├── topics.md                 ← master plan: 23 scene-topics, 204 scene OUTLINES,
│                                concrete→abstract cram order. Write texts FROM this.
├── glue-pool.md              ← 326 closed-class function words (prepositions, pronouns,
│                                particles…). NOT scened — woven through every batch's texts.
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
├── wordfreq.py               ← batch wordlist → words ranked by DWDS corpus frequency
└── opus/                     ← the pipeline that BUILDS wp.db (see its IMPLEMENTATION.md)
opus-de/                      ← (git-ignored) wp.db, 1.5 GB. Built, not committed.
dwds-cache/                   ← (git-ignored) Wortprofil pages you saved + Goethe A1/A2/B1
                                 lemma lists. Not committed: DWDS/Goethe content.
batch-NN-<topic>/             ← one dir per batch = one topic. Files appear in pipeline
                                 order, so a batch mid-flight has only the early ones:
├── wordlist.md               ← [step 2] frozen word list (article · plural/verb forms · gloss)
├── chunks.md                 ← [step 2b, optional] attested collocations per load-bearing word
├── texts.md                  ← [step 3] CONTENT TYPE 1: the cramming texts
├── anki-cloze.txt            ← [step 6] CONTENT TYPE 2: cloze cards (import as Cloze note type)
└── anki-basic.txt            ← [step 6] CONTENT TYPE 2: word→meaning cards (import as Basic note type)

batch-01-in-der-wohnung/      ← the only batch so far: wordlist.md + texts.md written
                                 (148 words, 11 texts). Cards deliberately not cut yet —
                                 they wait until the texts are reviewed (steps 5→6).
```

Groundwork is done and batch 01 is under way (texts written, cards pending). The
remaining work is, per topic in `groundwork/topics.md`: write the texts (content type 1),
then cut the cards (content type 2) from them — **the agent doing that should read
`TEXT-WRITER.md` first; it's the complete, self-contained brief.**

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

---

## Per-batch pipeline

1. **Pick a topic** from `groundwork/topics.md` — batches are ordered concrete→abstract;
   start with Stage A (Wohnung, Körper, Essen…).
2. **Freeze the word list** — `wordlist.md`: word | gender+plural or verb forms | gloss |
   text# | in-Anki? — forms copied verbatim from the CSV.
3. **Write the cramming texts (content type 1)** — turn that topic's scene outlines into
   2–3 short, imaginable German-only scenes (4–8 sentences each). Every target word in its
   canonical B1 sense; weave in glue-pool words naturally (see below). Iterate.
4. **Vet** — naturalness + correctness pass; validate every word against the CSV.
5. **Cram** (the user's loop) — read slow → visualize → handwrite several times → recite.
6. **Generate the Anki cards (content type 2)** — *from the finalized texts*: one cloze
   card per target word (cut from its sentence) + one word→meaning card.

## Batch sizing

**The scene is the encoding unit; the batch is the whole topic.** Don't conflate them —
a batch is days of work, not one sitting.

- **1 scene = 1 text = ~13 target words.** This is the unit sized to survive "know it by
  heart" in one encoding sitting + a few days of rewriting. `topics.md` pre-splits every
  topic into these scene-sized chunks (2,542 scened words / 204 scenes ≈ 12.5 each).
- **1 batch = 1 topic = one text per scene.** Topics vary widely: 1–17 scenes and 8–214
  target words (see the table in `topics.md` §2). Batch 1 is 11 scenes / 148 words;
  the largest is Batch 16 (Freizeit, Medien & Technik) at 17 scenes / 214 words, the
  smallest Batch 4 (Tiere) at a single 8-word scene.
- So a batch is cranked scene by scene, over several sittings — the *batch* is the unit of
  planning and card generation, the *scene* is the unit of memorization.

## The glue pool

Pure function words (`obwohl, zwischen, derselbe, ziemlich`…) have no mental picture, so
they get **no standalone scenes**. Instead the text-writer draws from `glue-pool.md` while
writing *every* batch's texts, as connective tissue. **Rule: it's OK to repeat these words;
it's NOT OK to leave them out.** The pool has a checkbox tracker — tick each word the first
time it lands in any finalized text, until all 326 are covered.

## Why this shape

- **Cloze-from-your-own-text** is the bridge between the two content types: the card
  reactivates the exact scene built by hand, so cramming and spaced repetition are the
  *same* memory, not two competing ones.
- **Word→meaning** cards guarantee context-free recall so a word isn't stuck to one sentence.
- **Frozen list with gender/plural/verb forms** so a nice story never hides a wrong article.

## Anki import

- `anki-cloze.txt` → import as **Cloze** note type, fields tab-separated (Text, Back Extra).
- `anki-basic.txt` → import as **Basic** note type (Front, Back).
- Field separator = **Tab**, Allow HTML = off.

## Batches

- **`batch-01-in-der-wohnung/`** — Stage A, topic 1. 148 target words across 11 scenes.
  `wordlist.md` frozen (CSV-verified forms, nothing invented) and all 11 `texts.md`
  written; glue-pool coverage ticked in `groundwork/glue-pool.md` (that file is the
  live counter — don't mirror the number here). **Awaiting the step 5 cram + review** — Anki
  cards are held until then, so `anki-*.txt` don't exist yet and `carded? = no`
  throughout the wordlist. (An earlier version of this batch predated the
  taxonomy/glue-pool structure and was removed in `2177517`; the current one was
  rewritten against it in `cd080cc`.)
- **Next:** pick another Stage A topic from `groundwork/topics.md` (Körper & Gesundheit
  is topic 2), or finish batch 01 by generating its cards.

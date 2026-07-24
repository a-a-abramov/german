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
goethe-b1-wortliste.csv       ← SOURCE OF TRUTH: official Goethe B1 Wortliste (2,886 entries)
groundwork/
├── topics.md                 ← master plan: 23 scene-topics, 204 scene OUTLINES,
│                                concrete→abstract cram order. Write texts FROM this.
└── glue-pool.md              ← 326 closed-class function words (prepositions, pronouns,
                                 particles…). NOT scened — woven through every batch's texts.
batch-NN-<topic>/             ← one dir per batch (NONE YET — first is TBD). Each holds:
├── wordlist.md               ← frozen word list (article · plural/verb forms · gloss)
├── texts.md                  ← CONTENT TYPE 1: the cramming texts
├── anki-cloze.txt            ← CONTENT TYPE 2: cloze cards (import as Cloze note type)
└── anki-basic.txt            ← CONTENT TYPE 2: word→meaning cards (import as Basic note type)
```

Groundwork is done. The next work is writing texts (content type 1) for each batch in
`groundwork/topics.md`, then generating cards (content type 2) from them.

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

- 1 batch = 1 topic = 2–3 texts = ~30–45 target words (~10–15 new words per text).
- Keeps "know it by heart" survivable in one encoding sitting + a few days of rewriting.
- Large topics in `topics.md` are pre-split into scene-sized chunks (~13 words each).

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

- None yet. (An earlier `batch-01-in-der-wohnung/` was removed — it predated this
  taxonomy/glue-pool structure; recoverable from git history if a reference is wanted.)
- Pick the first from `groundwork/topics.md` (start with a Stage A topic).

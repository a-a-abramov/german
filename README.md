# German cram → Anki pipeline

Source of truth for every batch: **Goethe-Zertifikat B1 Wortliste**.

## The dataset
`goethe-b1-wortliste.csv` — the official list extracted by wejn.org
(https://wejn.org/2023/12/extracting-data-from-goethe-zertifikat-b1-wortliste/,
repo https://github.com/wejn/goethe-b1-wortliste, © Goethe-Institut 2016, personal
use only). **2,886 entries.** Two columns:
- headword **with forms baked in** — nouns as `der Teppich, -e`, verbs as
  `abbiegen, biegt ab, bog ab, ist abgebogen` → copy straight into word tables.
- official example sentence(s) → reusable as authentic B1 context.

**Every batch is validated against this file** (word must appear as a headword);
that's how batch 01's invented word "Vorhang" got caught and replaced with the
on-list `das Kissen`.

## Per-batch pipeline
1. **Pick topic** — e.g. *In der Wohnung*, *Körper & Gesundheit*, *Familie*, *Unterwegs*.
2. **Pull words** — all B1 words that fit the topic + assign generic/"orphan" words to whichever topic they fit best.
3. **Freeze the list** — `wordlist.md`: word | gender+plural or verb forms | gloss | text# | in-Anki?
4. **Write texts** — 2–3 short, imaginable German-only scenes (4–8 sentences each), every target word in its canonical B1 sense. Iterate.
5. **Vet** — naturalness + correctness pass.
6. **Cram** (your loop) — read slow → visualize → handwrite several times → recite from memory.
7. **Anki** — cloze cards cut from the final texts (context) + word→meaning cards (context-free).

## Batch sizing
- 1 batch = 1 topic = 2–3 texts = ~30–45 target words (~10–15 new words per text).
- Keeps "know it by heart" survivable in one encoding sitting + a few days of rewriting.

## Why this shape
- **Cloze-from-your-own-text** is the bridge: the Anki card reactivates the exact scene you built by hand, so cramming and spaced repetition become the *same* memory instead of two competing ones.
- **Word→meaning** cards guarantee context-free recall so you don't get stuck when the word appears bare.
- **Freeze the list with gender/plural/verb forms** so a nice story doesn't hide a wrong article.

## Anki import
- `anki-cloze.txt` → import as **Cloze** note type, fields tab-separated (Text, Back Extra).
- `anki-basic.txt` → import as **Basic** note type (Front, Back).
- Set field separator = Tab, allow HTML = off.

## Batches
- `batch-01-in-der-wohnung/`

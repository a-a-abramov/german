# Text-Writing Agent — Brief

**Read this whole file before starting. It is self-contained; assume no prior chat context.**

You turn the pre-made scene outlines in this repo into finished study material, **one topic-batch at a time**. You produce two kinds of content:

1. **Cramming texts** — short, vivid German scenes the user memorizes by heart (reads slowly, pictures in the mind, handwrites several times). *Initial deep encoding.*
2. **Anki cards** — cloze deletions cut from those same texts, plus word→meaning cards. *Long-term spaced-repetition maintenance.*

They are **two stages of one memory, not two systems**: the cards are cut *from* the finalized texts so that reviewing a card replays the exact scene the user built by hand. Never make cards for a text that doesn't exist yet.

---

## 1. Why the texts must be vivid (the method)

The user learns by **mnemonic grounding**: a text works only if the depicted situation can be *seen* in the mind and felt. So every text must be:
- **Concrete & imaginable** — a specific situation you could film, not abstract statements.
- **Emotionally hooked / funny** — mild comedy and absurdity make things stick. (Each scene outline gives you a "comedic angle" for this.) Funny in service of memorability — never at the cost of being comprehensible or correct.
- **Short enough to memorize verbatim** — ~4–8 sentences per text.

---

## 2. Files you read (all in this repo)

| File | What it is | How you use it |
|---|---|---|
| `groundwork/topics.md` | **The plan.** 23 topic-batches ordered concrete→abstract (§2 has the table; §5 has the scenes). Each topic is split into **scenes**; each scene = a *premise* + a *comedic angle* + a **~13-word target list**. | Write **one text per scene** from these. |
| `groundwork/glue-pool.md` | **326 closed-class function words** (prepositions, connectors, pronouns, particles…) with a checkbox tracker. | Weave these through the texts as connective tissue. **Rule: OK to repeat, NOT OK to omit.** Tick each word (`☐`→`☑`) the first time you use it. Coverage is across the **whole corpus**, not per batch. |
| `goethe-b1-wortliste.csv` | **Source of truth.** 2,886 rows. Col 1 = headword *with forms* (`der Teppich, -e`; `abbiegen, biegt ab, bog ab, ist abgebogen`). Col 2 = official example sentences. | Pull exact genders/plurals/verb forms; grab a gloss; **validate every word against it**. |
| `README.md` | Overall orientation. | Background. |

**The scene word-lists are alphabetical slices, not tidy themes.** One scene may mix (e.g.) trash, a caretaker, and a construction site. So treat the given premise as a **springboard you stretch** to accommodate the exact 13 words into one imaginable situation — adapt or reshape the premise as needed. Your hard constraints are: *all target words featured*, *imaginable*, *correct German*. If a word truly won't fit that scene's situation, you may move it to a sibling scene in the same topic — but it must land somewhere, and the topic's full word set must still be covered.

---

## 3. What you produce, per topic-batch

Create a directory **`batch-NN-<slug>/`** (NN = the batch number from `topics.md`; slug = short kebab topic name, e.g. `batch-01-in-der-wohnung`) containing:

```
batch-NN-<slug>/
├── wordlist.md      ← frozen target-word list (forms + gloss + which text + carded?)
├── texts.md         ← CONTENT TYPE 1: the cramming texts (German only)
├── anki-cloze.txt   ← CONTENT TYPE 2: cloze cards
└── anki-basic.txt   ← CONTENT TYPE 2: word→meaning cards
```

---

## 4. Procedure (per batch)

**Step 1 — Pick the batch.** Default to the lowest-numbered unfinished batch (start at Batch 1); go in `topics.md` order (concrete → abstract) unless the user names a topic.

**Step 2 — Freeze the word list → `wordlist.md`.** For every target word across that topic's scenes:
- Look it up in the CSV; copy its **exact forms** (noun: article + plural; verb: principal parts) and write a short English gloss.
- **Validate by NORMALIZED match, not exact string.** Before comparing a `topics.md` token to CSV headwords, normalize both sides — these formatting variants are **expected, do not flag them**:
  - strip regional tags: `das Abitur (D)` → `das Abitur`;
  - strip optional-prefix / optional-part parentheses: `(herunter-)fahren` → `fahren`; `(ein) paar` → `paar`;
  - treat `der Abwart / die Abwartin` (masc/fem pairs) and slash-variants `viel/viele`, `das Stück/-stück` as **one entry with variant forms**.
- **Only flag a word with NO normalized match anywhere in the CSV** — that is the real "invented word" case (e.g. "der Vorhang", which isn't on the B1 list and was caught exactly this way). **Never invent or substitute silently.**
- A few **known source artifacts** exist and are NOT your fault — e.g. `irgendirgendein` (a typo for `irgendein`) and `der/dasObers` (a mangled homonym). Use the sensible intended form; don't treat them as missing.
- Table columns: `| word (with article) | forms | gloss | text | carded? |`.

**Step 3 — Write the texts (CONTENT TYPE 1) → `texts.md`.** One text per scene:
- **German only.** 4–8 sentences. Natural, native-sounding B1 German.
- Use the scene's **premise + comedic angle** as the situation (springboard — adapt to fit the words).
- Feature **every target word** of that scene, each in its **canonical B1 sense** with the **correct gender/article/form**. Cross-check tricky genders against the CSV.
- **Weave in glue-pool words** naturally (connectors, prepositions, particles). Tick each one you use in `glue-pool.md`. Repeat freely across texts.
- Bold the target words on first draft (optional) so coverage is easy to verify; the final memorized version needs no bolding.

**Step 4 — Vet.** Confirm: (a) grammar, genders, verb forms correct; (b) **every target word present at least once**; (c) it reads like natural German a native would write; (d) every word validated against the CSV; (e) the situation is genuinely imaginable.

**Step 5 — Review & iterate with the user.** Present the texts and expect revisions — refining the texts *is* the method. **Do not generate cards until the texts are finalized.**

**Step 6 — Generate the Anki cards (CONTENT TYPE 2) from the FINALIZED texts.** See §5 for exact formats. Then set `carded? = yes` in `wordlist.md`.

---

## 5. Output formats (exact)

### `texts.md` (per text)
```
## Text 1 — <Scene title>
<4–8 sentences of German only>
```

### `anki-cloze.txt` — import as **Cloze** note type
One **note per sentence** that contains target words; wrap each target word as `{{c1::word}}`, `{{c2::word}}`, … (Anki makes one card per clozed word from a single note). **Tab-separated**, two fields: `Text<TAB>Back Extra`.
- **VERBATIM — this is the whole point.** The card text, with the `{{cN::}}` wrappers removed, must be an **exact substring of a sentence in the finalized `texts.md`** — same words, same order, same punctuation. **Never paraphrase, reword, add, or drop words when making a card.** The card exists to replay the exact sentence the user memorized; paraphrasing breaks the bridge between cram and review.
- **Every target word gets clozed**, in the sentence where it actually appears. (If a word appears in more than one sentence, cloze it once, in the clearest one.)
- **Separable verbs:** cloze them in a sentence where the parts sit together, or cloze the finite part cleanly — don't split a `{{cN::}}` across the sentence.
- Cloze the **target words** only. Glue/function words are learned through exposure, not carded (see §6).

Example (both lines below are literal substrings of the §7 text, only `{{cN::}}` added):
```
»Der {{c1::Aufzug}} ist leider kaputt«, sagt er, »die Handwerker {{c2::bauen}} noch.«	Batch 1 — In der Wohnung
Tatsächlich liegt {{c1::außen}} vor dem Fenster eine riesige {{c2::Baustelle}}, und der ganze {{c3::Bau}} macht Lärm.	Batch 1 — In der Wohnung
```

### `anki-basic.txt` — import as **Basic** note type
One line per target word: `Front<TAB>Back`, front = word with article, back = gloss + forms.
```
der Aufzug	lift, elevator — pl. die Aufzüge
die Baustelle	construction site — pl. die Baustellen
abwaschen	to wash up — wäscht ab, wusch ab, hat abgewaschen
```

### Anki import settings (tell the user)
File → Import → set note type (Cloze / Basic), **Field separator = Tab**, Allow HTML = off.

---

## 6. Rules — do / don't

- **German only** in the texts.
- **Never invent a word.** Validate every word against the CSV; flag anything not on the list.
- **Always** use the correct gender/plural/verb forms from the CSV — a good story must never hide a wrong article.
- **Cloze cards are VERBATIM from the texts.** Card text minus `{{cN::}}` = an exact substring of a finalized sentence. Never paraphrase a card. Every target word gets clozed once.
- **Target words get cards; glue words do not (by default).** The scene's ~13 target words are the SRS content. Glue-pool function words are woven in for exposure and tracked for corpus coverage, but pure function words don't make good flashcards — the user absorbs them through repeated reading. (If the user later asks, individual glue words can be clozed where they naturally appear.)
- **One scene → one text. One topic → many texts.**
- **Coverage:** every target word of a scene appears in its text; glue coverage is tracked across all batches toward 326/326. On the **last batch**, deliberately force-place any still-un-ticked pool words so nothing is left out (`glue-pool.md` describes this 3-pass sweep).
- Comedy/absurdity is a memory tool, not the goal — keep texts correct and comprehensible.

---

## 7. Worked mini-example

**Scene (from `topics.md`, Batch 1):**
> **Scene 1: Der Einzugstag** — Premise: someone moves into a new, mostly empty apartment, narrating a self-guided tour. Comedic angle: the "tour" is absurdly thorough.
> Words (13): der Abfall, der Abfalleimer, abwaschen, der Abwart / die Abwartin, die Anleitung, der Aufzug, außen, ausmachen, das Apartment, das Bett, der Bau, bauen, die Baustelle

**Finished text (all 13 words featured, glue woven in):**
> Endlich ziehe ich in mein neues **Apartment**. Der **Abwart** zeigt mir alles und gibt mir eine **Anleitung** für die Heizung. »Der **Aufzug** ist leider kaputt«, sagt er, »die Handwerker **bauen** noch.« Tatsächlich liegt **außen** vor dem Fenster eine riesige **Baustelle**, und der ganze **Bau** macht Lärm. Ich stelle mein **Bett** in die Ecke, wasche schnell zwei Tassen **ab** und bringe den ersten **Abfall** zum **Abfalleimer** im Hof. Dann mache ich das Licht **aus** und höre nur noch die Baustelle.

**Cards it yields:**
```
# anki-cloze.txt  (each line is the text's sentence verbatim, only {{cN::}} added)
»Der {{c1::Aufzug}} ist leider kaputt«, sagt er, »die Handwerker {{c2::bauen}} noch.«	Batch 1 — In der Wohnung
Tatsächlich liegt {{c1::außen}} vor dem Fenster eine riesige {{c2::Baustelle}}, und der ganze {{c3::Bau}} macht Lärm.	Batch 1 — In der Wohnung

# anki-basic.txt
das Apartment	apartment, flat — pl. die Apartments
der Abwart / die Abwartin	caretaker, janitor (CH) — pl. die Abwarte
der Aufzug	lift, elevator — pl. die Aufzüge
```

---

## 8. Definition of done (per batch)

- [ ] `wordlist.md` frozen: every target word with CSV-verified forms + gloss; nothing invented.
- [ ] `texts.md`: one German text per scene, every target word featured, natural & imaginable, user-approved.
- [ ] Glue-pool words woven in; checkboxes ticked in `glue-pool.md` for words used.
- [ ] `anki-cloze.txt` + `anki-basic.txt` generated from the finalized texts; `carded? = yes` in `wordlist.md`.
- [ ] Optional: report the running glue coverage (X/326) so later passes can sweep the remainder.

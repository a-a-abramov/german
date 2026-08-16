---
name: text-writer
description: Write a batch of German B1 cramming dialogues and the Anki cards cut from them, for the Goethe-B1 → Anki repo. Use when asked to write, draft, revise or card a batch (e.g. "write batch 3", "do Essen & Restaurant", "make the cards for batch 2"). Covers scene design, the three writing stages, the collocation database, and the exact texts.md / anki-*.txt formats.
---

# Writing a batch of cramming dialogues

You turn one topic's vocabulary into finished study material. Two kinds of content:

1. **Cramming texts** — short, vivid German **dialogues** the user memorizes by heart
   (reads slowly, pictures in the mind, handwrites several times). *Initial encoding.*
2. **Anki cards** — cloze deletions cut from those same texts, plus word→meaning cards.
   *Long-term maintenance.*

They are two stages of one memory: the cards are cut **from** the finalized texts, so
reviewing a card replays the exact scene the user built by hand. Never card a text that
doesn't exist yet.

## The two failure modes to avoid

Both produce the same symptom — texts that read like vocabulary lists with quotation
marks — and both are introduced in Step 1, where no amount of careful writing can undo
them. Check for both before you write a line.

### 1. Letting the list's order become the scenes' structure

A previous pass sorted the batch's words, cut the sorted list into chunks of thirteen, and
wrote one "scene" per chunk. Words that share a first letter share nothing else, so every
dialogue was a forced march through unrelated nouns.

**Never let the word list's order become the scenes' structure.** Not alphabetical, not
frequency order (`vocab.py words` prints commonest-first — reading it top-to-bottom and
chunking is the same mistake with a different sort key), not database order. Read the
whole list, then group by **situation**: what places and moments do these words live in?
Each scene mixes frequency bands — the common words earn prominent positions, the rare
ones ride along in a subordinate clause.

### 2. Stacking synonyms into one scene

Grouping "by meaning" collapses very easily into grouping by **synonymy**, which is the
opposite of grouping by situation. Batches 1 and 2 were built that way and every one of
their eleven synonym sets landed in a single dialogue: `Flur`+`Korridor`, `Dose`+`Büchse`,
`Sofa`+`Couch`, `Klinik`+`Krankenhaus`, `putzen`+`reinigen`, `Kuli`+`Kugelschreiber`,
`Heim`+`Zuhause`, `Stock`+`Stockwerk`+`Etage`, and so on. The result is a sentence no
German has ever said: *"trag den Rest durch den Flur ins Zimmer — der Korridor ist breit
genug."*

Real speakers prime lexically: you pick a word for a thing and reuse it for the rest of
the conversation. Two synonyms in one exchange happens only when a speaker is **correcting
or being ironic**. Everywhere else it reads as a thesaurus.

> **The rule: two synonyms may both live in a batch, never in the same dialogue.**
> Distribute them across distant texts — a speaker who says *Flur* in Text 2 and
> *Korridor* in Text 7 is fine, those are different conversations. Never `skip` one of a
> pair to solve this; they are all on the Goethe list, and moving costs no coverage.

Two things this rule does **not** cover:

- **Derivational families** — `krank`/`die Krankheit`, `der Mut`/`mutig`,
  `der Hunger`/`hungrig`. A noun and its adjective in one conversation is ordinary German
  (*"Ich bin krank." / "Was für eine Krankheit?"*). Leave them together.
- **Superordinate + specific** — *"Hast du einen Stift?" / "Nimm den Kugelschreiber."*
  That is a general request answered with a specific object, not two names for one thing.

But watch for **self-glossing**, where a speaker defines their own word mid-turn: *"Ich bin
süchtig nach Süßem, das ist eine richtige Sucht."* Cut the gloss clause and move the
second word to another text.

Check it twice. **At Step 1**, against the scene plan — this is the cheap moment, before
any text exists:

```bash
python3 - <<'EOF'
import re
SETS = [("der Flur","der Korridor"), ("die Dose","die Büchse")]   # every set in the batch
owner={}; scene=None
for ln in open('content/batches/NN-<slug>/scenes.md'):
    m=re.match(r'### Scene (\d+)', ln)
    if m: scene=int(m.group(1))
    m=re.match(r'- \*\*Words \(\d+\):\*\* (.*)', ln)
    if m:
        for w in m.group(1).split(', '): owner[w.strip()]=scene
for a,b in SETS:
    sa,sb=owner.get(a),owner.get(b)
    print(("STACKED " if sa==sb is not None else "split   ")+f"{a} [S{sa}] | {b} [S{sb}]")
EOF
```

**At Stage 3**, against the ledger, which records where the words actually landed — swap
the lookup for `select u.batch,u.text_no from uses u join words w on w.id=u.word_id where
w.lemma=?` and compare text numbers instead of scene numbers.

### And: a natural dialogue beats a complete one

90–95% coverage with texts that sound like two people talking is a better outcome than
100% with texts that sound like an inventory. Words that resist a natural home get
`skip`ped with a reason and are picked up later. Note that 100% is not itself the problem
— redistributing words across texts reaches it without contortion. Chasing the last few
words *inside one scene* is.

## What makes a text work

- **A dialogue.** Two or three speakers in alternating turns — never narration, never a
  monologue with quotes in it. Spoken exchange is the register the user needs, and it is
  the only place the function words (`wieso`, `doch`, `na klar`, `eben`) sound right.
- **Concrete and imaginable** — a specific situation you could film.
- **Every speaker recoverable from the first turn or two.** The `A:`/`B:`/`C:` labels are
  scaffolding the card checker keys on — they can never become names, so the *dialogue*
  has to say who is talking, via direct address, Sie/du, or role (*"Tobi, trag den Rest
  …"*, *"Machen Sie das Hemd auf, Herr Bruckner"*). A turn that could belong to nobody in
  the cast is a bug: check each speaker against the cast list in `scenes.md`.
- **Emotionally hooked / funny** — mild comedy and absurdity stick. In service of memory,
  never at the cost of being comprehensible or correct.
- **Short enough to memorize verbatim** — 4–8 turns.
- **Built out of attested collocations** — see Step 2.

## Repo orientation

| Path | What it is |
|---|---|
| `tools/vocab.py` + `curriculum/vocab.db` | **The ledger.** Every B1 word: its batch, CSV forms, gloss, frequency band, and whether a finished text has used it. All bookkeeping lives here — never in prose files. |
| `curriculum/assignments.tsv` | Plain-text seed of the ledger (`vocab.py init` reads it). Edit here if a word must change topic, then `init --force`. |
| `curriculum/topics.md` | The plan: 23 topics ordered concrete→abstract, plus a non-binding scene-idea bank. |
| `curriculum/glue-pool.md` | Why 326 closed-class function words are pooled rather than scened, and how to weave them in. |
| `curriculum/goethe-b1-wortliste.csv` | Source of truth for forms, genders and official example sentences. |
| `docs/collocations-query.md` + `tools/wortprofil_db.py` | The collocation database: 514M tokens of film dialogue, relation-typed. Exactly the register these texts need. |
| `tools/wordfreq.py`, `tools/leipzig.py` | Frequency bands (already in the ledger) and a fallback collocation source. |

## Procedure

### Step 0 — Pick the batch and read its words

```bash
python3 tools/vocab.py status                 # which batches are done
python3 tools/vocab.py words --batch N        # the full list: forms, gloss, band, coverage
```

Default to the lowest-numbered batch that isn't done. Read the **entire** list before
writing anything — you are looking for the situations hiding in it.

**Standard German only.** The Goethe list carries the Austrian and Swiss doublets of
words it also lists for Germany — `die Stiege` for *Treppe*, `das Eck` for *Ecke*,
`der Fauteuil` for *Sessel*, `der Erdapfel` for *Kartoffel*, `das Velo` for *Fahrrad*. This
corpus teaches the D side only: the ledger tags every entry with its CSV region and hides
the 54 A/CH-only ones, so `words --batch N` already gives you a clean list (add
`--regional` if you ever need to see what was excluded). Two things follow for the texts:

- **Never write an A/CH-only word**, and never build a line, a joke or a character around
  a regional contrast ("bei uns sagt man …"). It teaches the wrong half.
- An entry tagged `(D, A)` or `(D, CH)` is *not* excluded — it is standard German that
  happens to be shared. `der Aufzug (D, A)`, `die Ecke (D, CH)`, `die Büchse (D, CH)` are
  all fair game; just write them as plain German, without the regional aside.

**The `lemma` column reproduces the source list's typos** — `derOfen`, `dieSahne`,
`irgendirgendein` and four others have a glued-on or duplicated article. Write the sensible
intended form (`der Ofen`, `irgendein`); the `forms` column has the real spelling, and
`vocab.py find <word>` prints a note on each of them. Nothing else in the ledger is
invented: every headword is CSV-matched.

Words with an empty gloss are fine to work with (the forms column tells you the gender
and principal parts); fill glosses in as you go with `vocab.py gloss "<word>" "<gloss>"`,
since `anki-basic.txt` needs them at the end.

### Step 1 — Design the scenes (this is the creative work)

Group the batch into **8–14 scenes**, each with a premise, a comedic angle, and the words
it will carry. Rules:

- Group by **situation**, not by list position. A kitchen scene pulls `der Herd`,
  `der Topf`, `abwaschen`, `das Geschirr` from wherever they sit in the list.
- 10–18 words per scene is comfortable. Some scenes carry fewer; that's fine.
- **Before you finish the plan, list the batch's synonym sets and check that no scene
  holds two members of one set.** This is much cheaper here than after the texts exist.
- A word may appear in several scenes — coverage counts the first natural use.
- Leftovers are expected. Park them in a "still homeless" list; Stage 2 finds homes for
  most, Stage 3 skips the rest.
- `curriculum/topics.md` has an inherited scene-idea bank you may raid for premises. It
  is **non-binding** — it was written against the retired alphabetical slicing, so its
  word groupings are meaningless. Take a premise if it fits your grouping; otherwise
  invent your own.

Write the scene plan to `content/batches/NN-<slug>/scenes.md` (title, premise, angle, word list) so
Stages 2 and 3 can see what each dialogue was supposed to do.

### Step 2 — Harvest chunks

Pick the **10–20 load-bearing nouns and verbs** of the batch — the ones the scenes turn
on, not all 130 words — and run:

```bash
python3 tools/wortprofil_db.py <Wort> <Wort> … --min-freq 20 --min-dice 4 --top 15 \
    > content/batches/NN-<slug>/chunks.md
```

That gives, per word and per grammatical relation, the top-15 *attested* combinations,
filtered to A1∪A2∪B1 and rendered as ready-to-use chunks (`eine heiße Tasse`,
`aus der Tasse trinken`). Pass `--min-dice 4` explicitly — the default of 3.0 was tuned
for a much larger corpus and lets light verbs through.

- **If a word comes back thin**, walk the ladder: `--min-freq 10`, then
  `--all --min-freq 5 --top 25` (the `·` rows are orientation only, never source), then
  `python3 tools/leipzig.py <Wort>`. If nothing usable comes back, write it yourself.
- **Never let a chunk drag in a non-B1 word.**
- **Skim before you pull.** The corpus is film dialogue and leans crime/drama: `Wohnung`
  returns `durchsuchen` above `mieten`. Rank order is a suggestion.
- The **Kasus** column resolves two-way prepositions (`ins Bett gehen` Akk. vs.
  `im Bett liegen` Dat.) — use it instead of guessing.
- **Vividness outranks idiomaticity.** Never let chunk-fitting flatten a scene.

### Step 3 — Three writing stages

Every batch is written in three passes over the whole set of dialogues. Each pass has one
job, and **all three share the same first priority: the dialogue must sound like two
people actually talking.**

**Stage 1 — Initial draft.** Write every scene end to end, fast, aiming for the scene's
core words. Let the conversation lead: real turns answer each other, interrupt, change
the subject, leave things implied. If a target word won't go in without bending the
sentence, leave it out — Stage 2 will look at it again. Save to `texts.md` in the format
below. Then:

```bash
python3 tools/vocab.py scan content/batches/NN-<slug>/texts.md --batch N -v
```

**Stage 2 — Review and enrichment.** Re-read every dialogue as a native speaker would.
First fix what sounds off: stilted word order, a turn nobody would ever say, comedy that
doesn't land, a speaker explaining things to someone who'd already know them.

These five tells are what a coverage-driven draft actually produces. Hunt them by name:

1. **Synonym stacking** — see the failure modes above. Run the check script.
2. **Three-item lists with a particle in the third slot** — *"Meine Nase läuft, der Kopf
   ist schwer, und müde bin ich **sowieso**."* One or two per batch is real speech; one
   per text is the batch's signature. The `außerdem`/`sowieso` is carrying the word list,
   not the speaker.
3. **Bolt-on final turns** — a closing utterance that dumps two unrelated objects
   (*"Zieh dich um, an deiner Hose ist Waschmittel. Und häng den Schirm an die Garderobe."*).
   Tie the object to what the scene is already about, or move it.
4. **Recap turns** — *"Also zwei Zimmer, vierter Stock, kein Aufzug."* Nobody summarizes
   back what they were just told. This is a drill, not a turn.
5. **Register slips** — written or bureaucratic vocabulary in casual speech: `reinigen`
   for `putzen`, `der Zugang`, `das Lager` in a private flat, *"trotz aller Regeln"*. When
   in doubt, check which verb the corpus actually uses (`Fenster putzen` has 368 hits;
   `reinigen` does not appear in *Fenster*'s top 18 at all). A target word in the wrong
   register usually just needs a different scene, not deletion.

Only then take the `missing` list from the scan and ask, word by word: *is there a line
this word would genuinely belong in?* If yes, rewrite the turn around it — don't bolt it
on. If no, leave it for Stage 3. Enrichment that damages naturalness is a regression, not
progress.

**Deliver the angle, not just the words.** Each scene in `scenes.md` has a comedic angle.
Re-read it against the finished text: if the angle isn't on the page, the text is carried
by vocabulary alone and will read flat. Restoring a designed joke costs no coverage.

**Stage 3 — Final pass.** Read every dialogue aloud, start to finish. Cut anything that
still reads like a list. Check the mechanics: genders and verb forms against the CSV,
every scene genuinely imaginable, 4–8 turns, no English. Then close out coverage:

```bash
python3 tools/vocab.py scan content/batches/NN-<slug>/texts.md --batch N --apply
python3 tools/vocab.py skip --batch N "<word>" "<word>" --reason "no natural home in this batch"
python3 tools/vocab.py status --batch N
```

Fix scanner misses by hand — it matches folded stems, not lemmas, so it misses some
compounds and split verbs:

```bash
python3 tools/vocab.py use   --batch N --text 4 "<word>"    # it IS there, scanner missed it
python3 tools/vocab.py unuse --batch N "<word>"             # false positive
```

Land at 90–95% and stop. Chasing the last few words is what produces list-shaped texts.

### Step 4 — Review with the user

Present the texts and expect revisions — refining them *is* the method. **Do not generate
cards until the user has approved the texts.** After any rewrite, re-run `scan --apply`
(it recomputes rather than increments, so coverage never drifts from what the texts say).

### Step 5 — Cards, from the finalized texts only

Cut each word's cloze from **the text its scene owns** (`scenes.md`), not from wherever
`scan` happened to see it first — the scanner records first occurrence, so a word that
turns up incidentally in an earlier dialogue is logged there. Where the two differ, note
the difference in `scenes.md` so the carding pass has one answer.

Generate `anki-cloze.txt` and `anki-basic.txt` (formats below), then record it:

```bash
python3 tools/vocab.py card --batch N --all
```

## Formats (follow literally)

### `texts.md`

```
## Text 1 — Der Einzugstag

A: Guten Tag, ich bin neu hier. Ist das mein Apartment im vierten Stock?

B: Ja, genau. Ich bin die Abwartin. Hier ist die Anleitung für die Heizung, aber der Aufzug ist leider kaputt.

A: Wieso denn? Und was ist das für ein Lärm draußen?
```

- **One turn per line**, starting with `A:`, `B:` or `C:` — a single capital, a colon, one
  space, the utterance. Nothing else on the line.
- **Blank line between turns**, or markdown collapses the exchange into a wall of text.
- **These labels and no others** — not names, not `**A:**`. Cards are verified as exact
  substrings of an utterance, and the label format is what the check keys on.
- The label is scaffolding, not German: never memorized, never clozed, never on a card.
- The `## Text N — Title` heading is what `vocab.py scan` parses. Keep the em dash.

### `anki-cloze.txt` — Anki **Cloze** note type

One note per sentence containing target words; wrap each as `{{c1::…}}`, `{{c2::…}}`.
Tab-separated, two fields: `Text<TAB>Back Extra`.

```
Ich bin die {{c1::Abwartin}}. Hier ist die {{c2::Anleitung}} für die Heizung.	Batch 1 — In der Wohnung
{{c1::Außen}} vor dem Fenster ist eine {{c2::Baustelle}}.	Batch 1 — In der Wohnung
```

- **VERBATIM.** The card text minus the `{{cN::}}` wrappers must be an **exact substring
  of a single utterance** in the finalized `texts.md` — same words, same order, same
  punctuation. Never paraphrase, reword, add or drop anything.
- **A note may not cross a turn.** Strip the speaker label; the card starts at the first
  character after `A: `. One note, one speaker's words.
- **Every covered target word gets clozed**, in the sentence where it appears (once, in
  the clearest sentence, if it appears more than once).
- **Separable verbs:** cloze them where the parts sit together, or cloze the finite part
  cleanly — never split one `{{cN::}}` across a sentence.
- Cloze target words only. Glue words are learned by exposure, not carded.

### `anki-basic.txt` — Anki **Basic** note type

`Front<TAB>Back`, front = word with article, back = gloss + forms.

```
der Aufzug	lift, elevator — pl. die Aufzüge
die Baustelle	construction site — pl. die Baustellen
abwaschen	to wash up — wäscht ab, wusch ab, hat abgewaschen
```

Tell the user: File → Import → set the note type, **Field separator = Tab**, Allow HTML
off.

## Rules

- **German only** in the texts; every text a dialogue in the `A:` / `B:` format.
- **Never invent a word.** Everything in the ledger is CSV-verified; if you need a word
  that isn't there, say so rather than substituting silently.
- **Standard German only** — no A/CH-only words, no dialect-contrast lines (see Step 0).
- **Always the correct gender, plural and verb forms** — a good story must never hide a
  wrong article. `vocab.py find <word>` prints the CSV forms.
- **Glue words: OK to repeat, not OK to omit.** They are shared across the whole corpus,
  not per batch. `vocab.py glue --open` lists what's still missing; `--group Frage`
  (or `Konjunk`, `Modal`, `Partikel`) narrows it. A dialogue mops up question words and
  particles almost for free — one speaker asks, the other hedges. Coverage of a glue word
  never retires it; keep reusing it everywhere it fits.
- **Incidental hits are a bonus.** A word from another batch that a chunk drags in still
  gets its own scene and its own card in its own batch. Nothing is struck off for having
  appeared elsewhere.
- **One scene → one text. One topic → many texts.**
- Comedy is a memory tool, not the goal. Correct and comprehensible first.

## Definition of done

- [ ] `scenes.md`: 8–14 scenes grouped by situation, each with premise + angle + words.
- [ ] No scene holds two members of one synonym set (check script in the failure modes).
- [ ] `chunks.md`: harvested at `--min-freq 20 --min-dice 4 --top 15`.
- [ ] `texts.md`: one dialogue per scene, all three stages done, natural, user-approved.
- [ ] Every speaker recoverable from the dialogue; every scene's angle actually on the page.
- [ ] No verbatim 4-word span repeated across two texts (n-gram scan over `texts.md`).
- [ ] `vocab.py scan --apply` run on the final text; leftovers `skip`ped with a reason;
      batch coverage ≥ 90%.
- [ ] `anki-cloze.txt` + `anki-basic.txt` cut verbatim from the final texts;
      `vocab.py card --batch N --all` recorded.
- [ ] Report to the user: batch coverage, glue coverage (X/326), anything skipped.

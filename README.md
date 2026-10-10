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
git-ignored, and only the `gh-pages` branch carries HTML. Three surfaces:

- **the index** — the 23 topics in cram order with their real state, and every word in
  the ledger, searchable, each linking to the text that taught it
- **the reader** — one dialogue per page, big serif, the scene's owned words in the
  margin, a gloss on every target word
- **Wortprofil & Belege** — one page per batch, one block per load-bearing word: a link
  to that word's live DWDS-Wortprofil, and under it every sentence in *our* dialogues
  that uses the word, each a click from the dialogue it comes from. The collocation
  tables themselves are no longer reprinted — DWDS serves a better, live copy at `/wp`

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

Twenty batches are written; none is carded yet. All twenty follow the scene-design +
three-stage method — `scenes.md` groups the words into situations, `texts.md` has one
dialogue per scene — and all twenty are **awaiting the cram + review pass**, so no
`anki-*.txt` exists anywhere yet.

- **`content/batches/01-in-der-wohnung/`** — Stage A, topic 1. 11 scenes, 11 dialogues.
- **`content/batches/02-koerper-gesundheit/`** — Stage A, topic 2. 12 scenes, 12 dialogues;
  3 words skipped.
- **`content/batches/03-essen-kochen-restaurant/`** — Stage A, topic 3. 12 scenes, 12
  dialogues, nothing skipped.
- **`content/batches/04-tiere/`** — Stage A, topic 4. 4 scenes, 4 dialogues, nothing skipped.
  The corpus's smallest batch by a wide margin (8 words), so it is scened at 4 rather than
  the usual 12: eight words across twelve dialogues would be the word list driving the
  structure again. Two things worth knowing before reading it — `die Schlange` is taught as
  a **queue**, which is the sense both of the Goethe list's example sentences carry, and
  `der Tierpark` is the one word in the corpus so far with **no Wortprofil at all**
  (`chunks.md` records the full ladder walk that found nothing). Its real yield is the glue
  pool, which four dialogues moved 263 → 277 of 326.
- **`content/batches/05-kleidung-aussehen/`** — Stage A, topic 5. 7 scenes, 7 dialogues,
  nothing skipped. Scened at 7 rather than the usual 12 because 43 words across twelve
  dialogues would be three target words per text. Two words are **not** the word the topic
  makes you expect, and `scenes.md` argues both from the CSV: `das Modell` is a product
  model (*"Dieses Modell gefällt mir nicht"*, of a car), never a person on a catwalk, and
  `das Kostüm` is a costume for a party, not a woman's suit. The batch's real design
  problem was its five evaluative adjectives (`schön`, `hässlich`, `elegant`, `schick`,
  `modern`), which are distributed one per scene so no garment is ever praised twice over.
  Its glue yield is the largest so far: **277 → 309 of 326 (85% → 95%)** on seven dialogues.
- **`content/batches/06-farben-formen-material/`** — Stage A, topic 6. 7 scenes, 7
  dialogues, nothing skipped. Scened at 7 for the same reason as batch 05 (41 words over
  twelve dialogues would be three targets per text), but the design problem is the
  opposite one: **24 of the 41 words are adjectives**, and five of them are one half of an
  antonym pair. Where batch 05 had to pull its five evaluative adjectives *apart*, this
  batch deliberately keeps `hart`/`weich`, `hell`/`dunkel`, `laut`/`leise`,
  `breit`/`schmal` and `senkrecht`/`waagerecht` *together*, one pair per scene — the
  contrast is what makes a speaker say either word at all. Three words are taught in the
  Goethe list's sense rather than the corpus's: `der Bogen` is a sheet of paper (not the
  one you shoot with), `der Kreis` a drawn circle (not a district or a circle of friends),
  `das Kreuz` a mark in a box (not the religious one) — and the word *Formular* is banned
  batch-wide because the scanner would read `Form` inside it. Glue yield **309 → 322 of
  326 (95% → 99%)**, leaving four words open, one of which is the CSV typo entry
  `irgendirgendein`.
- **`content/batches/07-familie-beziehungen/`** — Stage A, topic 7. 12 scenes, 12
  dialogues, nothing skipped. The whole semantic field is a family tree, so every scene
  has something at stake that happens to need the kinship words (a napkin diagram, a
  seating plan, a buffet queue, an Oma counting who visits). Its `scenes.md` is the first
  with a **continuity table** checked against Batches 1–6, and it fixed four
  contradictions in the original plan: Kevin's November party is the postponed
  celebration of the September Standesamt wedding from Batch 5; Bruckner lives alone (no
  wife); he has been caretaker 21 years; the divided flat is on the third floor. New
  standing facts for later batches: Tobi's family (the Wagners, Elke and Rolf, Kevin,
  Sandra, Oma Erna in the Altenheim), Anna Sattler on the second floor, expecting in March,
  the Lorenz couple living separated on the third, and **Bruckner retires at the end of
  December** but stays in the house. Glue yield **322 → 325 of 326**; only the CSV typo
  entry `irgendirgendein` stays open.
- **`content/batches/08-gefahr-notfall-sicherheit/`** — Stage A, topic 8. 6 scenes, 6
  dialogues, nothing skipped. Scened at 6 for the same reason as batches 05–06 (38 words).
  The topic's risk is register: the corpus uses `Katastrophe`, `Gift`, `tödlich`, `Flucht`
  and `zerstören` for thrillers. So **nothing serious happens**. Every scene is a small
  domestic emergency that one speaker inflates and another plays down: burnt rice that
  brings the Feuerwehr, a cat and a poisonous plant, a fall in front of a parked car, a
  break-in that steals nothing. Sense decisions from the CSV: `Katastrophe` is the
  everyday exaggeration, `sichern` is saving your work on a computer, `Schutz` is
  protection against cold, and `Unglück` is a serious incident, not bad luck. Two
  near-synonym pairs share a text on purpose, both argued in `scenes.md`:
  *zerstört* → *beschädigt* is a correction, and *kaputtgemacht* → *kaputtgegangen* is
  Tobi dodging the blame. The scanner cannot match `Achtung!`, `kaputtmachen` or
  `kaputtgehen`, so those are recorded by hand. New standing facts: **Herr Neumann** is
  the caretaker from January (Sie with everyone; signs everywhere; sand instead of salt).
  Bruckner is retired and still lives downstairs. Julia owns a bike, and Tobi broke its light.
  The cellar door was forced in a February break-in and **no longer sticks**. The lift is
  still broken.
- **`content/batches/09-natur-wetter-umwelt/`** — Stage B, topic 9. 14 scenes, 14
  dialogues, nothing skipped. The words are seasonal, so the scenes run from March to
  July and the weather is spread across the months. There is no forecast scene. The
  landscape words share one scene with something at stake: the view from the top is
  fog. The environment words come from people with selfish reasons: a school project,
  the Hausordnung, a paint tin. Sense decisions from the CSV: `Kanal` is a TV channel,
  `Birne` a pear, `Strom` electricity, `Energie` personal energy (*keine Energie mehr*),
  `Rind` beef *aus der Region*. Two pairs share a text on purpose, as corrections:
  `Rasen`/`Gras` and `Berg`/`Hügel`. `der See` and `die See` share the surface *See*, and
  `Öko-` can never match, so both are recorded by hand. New standing facts: Bruckner lives
  in the **Erdgeschoss**, and the Sattlers' baby was born in March. The house heats with
  oil, and the heating is off from 1 May. The stairwell light now stays on for 30 seconds.
  There is a pear tree in the garden, and Kessler is selling his field as building land.
  **Julia and Tobi plan two weeks on an Ostsee island in August**, which Batch 11 can
  pick up.
- **`content/batches/10-unterwegs-verkehr/`** — Stage B, topic 10. 12 scenes, 12
  dialogues; 2 words skipped (`der Lift`, `das Tram` — the CSV cross-references them to
  *Aufzug*/*Straßenbahn*, i.e. they are the CH words). Runs 20 July – 6 August, before the
  Ostsee trip, which is left to Batch 11. Directions are never recited: Bruckner gives them
  without glasses and with the map upside down. CSV senses: `Gang` is a gear, `Maschine`
  the aircraft, `Wagen` a railway carriage, `Schalter` a staffed counter, `Zone` a fare
  zone, `Rundfahrt` a city bus tour, `Fähre` a river ferry (recorded by hand — the scanner
  reads *Fahrer* as `Fähre`). New standing facts: Julia commutes by S-Bahn (line closed
  until end of August); Tobi has an old small blue car; Jule passed her driving test in
  July; Bruckner builds a model railway; Neumann rides a motorbike; there is a bus stop in
  front of number 19; Julia's bike light, promised in March, was in Tobi's rucksack.
- **`content/batches/11-reisen-urlaub/`** — Stage B, topic 11. 10 scenes, 10 dialogues,
  nothing skipped. August Y3: Julia and Tobi's two weeks on the Ostsee island (Sat 8 –
  Sat 22 Aug). Tobi booked a hotel on the mainland *mit Blick auf die Insel*; Frau Wolf
  rescues the trip through her old landlady Frau Claasen, whose Pension by the beach
  carries the rest of the batch — the ferry, the arrival, the guests at dinner, a rained-out
  boat trip, and Julia phoning Frau Wolf from her late husband's bench. Sense decisions:
  `die Pension` is the guesthouse and `in Pension sein` the retirement of a former civil
  servant (they share one line on purpose; `pensioniert` belongs to Frau Claasen, a retired
  teacher); `die Kabine` is a changing cubicle; `erreichen` is reaching someone by phone.
  `Viertel`/`Vorort` stay together as a contrast. New standing facts: Frau Claasen's
  Pension at the beach, twenty minutes from the harbour; the Behrens couple (twenty summers there, live in a Vorort);
  Tobi gets seasick; Bruckner took his first trip abroad, a five-day bus tour, while Frau
  Wolf fed his cat.
- **`content/batches/12-einkaufen-geld/`** — Stage B, topic 12. 15 scenes, 15 dialogues;
  2 words skipped (`einnehmen` — the CSV sense is taking medicine; `die Vermittlung` —
  both CSV senses are dated). September Y3, after the Ostsee trip: Tobi is short of money
  (rent up 80 € from December, a broken washing machine, a flea market that ends with him buying a
  stereo, a month-end spreadsheet) while the house does its own sums around him. CSV
  senses: `Gewinn` a raffle prize, `Verlust` a lost wallet, `Anlage` a stereo, `Kasten` a
  crate of water, `Karte` a cinema ticket. `einzahlen` and `der Markt` are recorded by hand
  (scanner false matches). Ledger note: the forms stored for `zählen` are those of
  `zahlen`, so every *zahlt* credits it — fix in `assignments.tsv`. New standing facts:
  Tobi's landlord Herr Fuchs; Herr Fink's coffee roastery where the old Lokal an der Ecke
  was; Jule's Girokonto with Frau Dietz; Kessler's Saturday market stall; Bruckner's first
  invoice "Nummer eins"; Leon carries Frau Wolf's bags for 50 cents a floor.
- **`content/batches/13-stadt-aemter-recht/`** — Stage B, topic 13. 14 scenes, 14
  dialogues; `der Personenstand` skipped (the CSV's D/A form is *Familienstand*, already
  taught in Batch 7). October Y3. The paperwork words are split over three settings with
  a stake each — Tobi at the Rathaus learning he never registered his own flat, the
  Sattlers' visa for Jan's parents, Bruckner's Urkunde with a coded Zeugnis — and every
  crime word belongs to someone in the house: Frau Wolf turns a fake-police phone scam
  round with the broken lift and later testifies against February's burglars; Neumann's
  new camera would film the building's only smoker: himself. Legal facts checked (not registering is
  unlawful but not *strafbar*). CSV senses: `Messe` a trade fair, `Anzeige` a police
  report, `Ursache` as in *Keine Ursache!*, `Zeugnis` an employment reference. Five
  scanner false-firsts (`streiten`, `anzeigen`, `Schulden`, `schuld`, `Recht`) are
  recorded by hand. New standing facts: **Neumann smokes** (cellar; the stairwell is now
  no-smoking); Tobi got a Strafzettel and a new Ausweis; the burglars, arrested in June, were sentenced; the
  cellar door sticks again; Bruckner got his Urkunde; there is a camera at the front door.
- **`content/batches/14-arbeit-beruf/`** — Stage B, topic 14. 14 scenes, 14 dialogues,
  nothing skipped. November Y3. **Establishes both jobs: Tobi is a Mechaniker in the
  Uni's Werkstatt** (*"eine Werkstatt für Geräte, nicht für Kraftfahrzeuge"*), Chef
  Meister Kaminski, Monday Besprechung at nine; he smokes only on breaks with Kaminski,
  which pays off Batch 3's *"Nicht privat"*. **Julia works part-time at a small Verlag**,
  two days a week at home, since the Batch 2 interview; her Chefin is Frau Lindner.
  Professions belong to people, never to a list. CSV senses: `Fach` a fridge compartment,
  `Führung` a factory tour, `Leitung` management, `Mangel` a defect, `Täter` the office
  yoghurt thief. The scanner cross-credits `Fehler`/`fehlen`, `fordern`/`fördern`,
  `Forderung`/`Förderung`, `Angestellte`/`anstellen`, `Hersteller`/`herstellen`, and
  `Arbeit` credits `arbeiten` — all six recorded by hand (`scenes.md` names each card's
  text). New standing facts: Kaminski retires next summer and offers Tobi the workshop
  (undecided); Jule waits tables at the café gegenüber; Frau Wolf was a factory
  Direktor's Sekretärin; Jan Sattler's Kraftwerk closes in two years; Frau Lorenz, once a
  Stewardess, is applying for work again; Kai imports coffee machines.
- **`content/batches/15-schule-bildung/`** — Stage B, topic 15. 10 scenes, 10 dialogues;
  1 word skipped (`eintreten` — its CSV sense is joining a club, which belongs to Batch 16).
  December Y3 – January Y4. No school-vocabulary parade: each scene has one learner with
  something at stake (Jule's Referat on sleep after two sleepless nights; Leon teaching his
  tutor patience; Amir writing a yellow door into his Lebenslauf). CSV senses: `Note` a
  school grade, `Lehre` an apprenticeship, `aufgeben` to give up, `Eintritt` an admission
  fee, `Forum` an internet forum, `Bereich` a field of work. `buchen` (the scanner reads
  *Buch*) and `Kursleiter` (headword typo) are recorded by hand. New standing facts:
  **Jule studies Biologie, Lehramt**; Prüfung in February; from January she teaches
  Tuesdays in **Herr Krämer**'s class, where she was once a pupil (the pupils call her
  *Frau Wagner*). Amir wants a Lehrstelle in a car workshop instead of the Abitur. Jule
  gives Leon paid Nachhilfe. Neumann went on a heating Fortbildung; in January the oil tank
  runs empty. Bruckner volunteers in a German Intensivkurs taught by **Frau Martens**, and
  he and Frau Wolf sign up again for March.
- **`content/batches/16-freizeit-medien-technik/`** — Stage B, topic 16. 16 scenes, 16
  dialogues; 1 word skipped (`das Billett` — Swiss-only, CSV *→ D, A: Fahrkarte*).
  Mid-January – late March Y4; Easter Y4 falls in late March, so Karneval is early
  February. `der Dialekt` is Bruckner mistaking Italian opera for a dialect — no regional
  contrast. The largest batch (213 words), so every scene turns on one
  stake rather than a hobby list: a TV remote without batteries, a piano noise complaint,
  a lost file, a bet, a video that goes viral. Print words get a speaker who justifies
  them (Gisela reads *Metropole* and *Tourismus* from a Prospekt). CSV senses: `Runde` a
  lap, `Figur` a person's figure, `Station` a U-Bahn stop, `Plan` a city map,
  `aufnehmen` recording. Two pairs share a text as corrections (*"Karneval ist ein Fest,
  keine Party"*; Maler/Künstlerin). `Bio-`, `Spiel`, `Studium` and `studieren` are
  recorded by hand.
  New standing facts: Julia has a new TV and teaches herself a digital piano; Tobi's club
  has a new trainer, Nils; Frau Wolf has a smartphone, dances at Karneval and takes
  Bruckner to the opera on the theatre subscription she never cancelled after her
  husband died; Leon's video of Bruckner's railway went viral; Frau Lorenz paints; Jule climbs on Thursdays; Werner plays golf;
  the Sattler child turned one on Easter Monday.
- **`content/batches/17-gefuehle-charakter/`** — Stage C, topic 17. 13 scenes, 13
  dialogues, nothing skipped. March – April Y4. The risk is an inventory of forty feeling
  adjectives, so nobody lists their own feelings: each one is caused by something on the
  page and usually named by someone else (a 4:0 makes Tobi a *schrecklicher Verlierer*;
  the cat bites an *ängstlich* Neumann; Frau Wolf corrects *neugierig* to
  *interessiert*). CSV senses: `arm` poor, `befreit` exempt (*vom Sport befreit*),
  `geehrt` only in a mock speech, `befriedigend` a grade for a soup, `wirken` a tablet
  working. `lieben`, `vertrauen` and `sich vergnügen` are recorded by hand (`vocab.py use
  "vertrauen"` resolves to the noun — a tool bug). New standing facts: Jule has been in
  love since January (with whom stays open); Oma Erna dances with Herr Rademacher, once a
  radio singer; Frau Wolf's birthday is at the end of April; Bruckner is *ledig* and asks
  Frau Wolf to keep phoning him every morning.
- **`content/batches/18-kommunikation-post/`** — Stage C, topic 18. 16 scenes, 16
  dialogues, nothing skipped (sixteen, because 179 words in fifteen overloaded the
  journalist and phone scenes). April – May Y4. A light arc: Frau Wolf campaigns for the
  lift by letter, radio, tenants' meeting and newspaper — and nothing is repaired.
  Written-register words (`hinweisen`, `mitteilen`, `das Schreiben`, `Aufforderung`,
  `Kommunikation`) are spoken only by the Verwaltung and Neumann. CSV senses: `Botschaft`
  an embassy, `Empfang` receipt of a letter, `Vertretung` a stand-in, `Sender`/`Hörer`
  radio, `Vorstellung` a performance, `raten` as in *Rate mal*. Contrast pairs kept
  together on purpose: Bitte/Aufforderung, Fremd-/Zweit-/Muttersprache, Artikel/
  Erzählung, duzen/siezen. Eleven owner texts are recorded by hand (`vocab.py use
  "schreiben"` resolves to the noun). New standing facts: new letterboxes (Frau Wolf's
  plate misspelt „Wolff"); post still comes for the previous tenant, Frau Seidel; postman
  Herr Simon; Jan Sattler's Muttersprache is Polnisch; Herr Lorenz is flat-hunting; Tobi's
  Muttertag parcel goes out late; Frau Wolf and Bruckner try du once her phone is repaired
  (a callback to Batch 17's birthday promise of morning calls) and go back to Sie.
- **`content/batches/20-gesellschaft-politik-wirtschaft/`** — Stage C, topic 20. 3
  scenes, 3 dialogues, nothing skipped — the smallest batch after 04 (20 words). Politics
  and economy enter the house only through everyday objects: an election poster at the
  bus stop, a ten-cent rise on rolls at Bäckerei Aydin, one of Neumann's signs. June Y4.
  Sense decisions: `die Gewalt` is force (the cellar door opens only *mit Gewalt*);
  `die Pflicht` is argued on purpose (Frau Wolf calls voting a Pflicht, Bruckner corrects
  her); `der Gott` is *Gott sei Dank*; `die Geschichte` a thing's history. New standing
  facts: a June election whose candidate Herr Vollmer once broke Bruckner's windows
  playing football in the courtyard; Aydin's rolls cost 10 cents more; the cellar door
  sticks again since the new lock (as in Batch 13). This batch also filled the English glosses for its 20
  words.
- **`content/batches/21-menge-mass-eigenschaften/`** — Stage D, topic 21. 15 scenes, 15
  dialogues, nothing skipped. July Y4. Almost all adjectives and quantities, so every
  scene needs something measured, compared or judged: Neumann's Hoffest with a cake
  contest runs through Texts 1–10 (cherries at the market, a recipe scaled up to forty,
  Bruckner's recipe card with salt and sugar swapped, a jury that has to average out
  Leon's ten-points-for-everyone), and Julia's 2.20 m sofa meets the 80 cm stairs. CSV
  senses: `die Leiter` is the ladder (the ledger row carries the manager's forms — gloss
  it "ladder — pl. die Leitern"), `echt` genuine, `knapp` narrowly, `pauschal` a flat
  delivery rate. `gewöhnen` and `Einzel-` are recorded by hand (scanner false matches).
  New standing facts: Bruckner won the cake contest with his mother's Marmorkuchen,
  baked with Tobi, by Leon's one point; Frau Wolf came second with her grandmother's
  Kirschkuchen; the sofa from Möbel Winkler went back; Bruckner wants to enlarge his
  railway; Frau Wolf is a regular at the café gegenüber.
- **Next:** write batch 19 (Zeit & Kalender, 136 words) with the `text-writer` skill, or
  close out any written batch by cramming it and generating its cards.

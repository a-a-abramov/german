# Batch 8 — Gefahr, Notfall & Sicherheit · Szenenplan

38 target words. **Six scenes**, five to eight words each, for the same reason Batches 5
and 6 used seven: 38 words over twelve dialogues would be three target words per text,
and the word list would drive the structure again.

The topic's hazard is register. Half of its words (`Katastrophe`, `Unglück`, `Flucht`,
`fliehen`, `zerstören`, `tödlich`, `Gift`) are what the film corpus uses for explosions and
murders, and a house where a disaster happens every week stops being the house of
Batches 1–7. So **nothing serious happens in this batch**. Every scene is a small domestic
emergency that one speaker inflates and another deflates: burnt rice that brings the
Feuerwehr, half a leaf the cat ate, a fall from a bike in front of a parked car, a break-in
that steals nothing. The big words are said by the person who is exaggerating, which is
how they are said in everyday speech.

## Sense decisions made against the CSV, not against the corpus

- **`die Katastrophe` is the everyday exaggeration** (*"Der Urlaub war eine Katastrophe.
  Es hat nur geregnet."*). Text 1 uses it of Tobi's dinner.
- **`sichern` is saving your work on a computer** (*"Du musst immer alle Daten im Computer
  sichern"*), not securing a door. Text 1: Julia has not saved her work when the alarm goes.
- **`der Schutz` is protection against the cold** (*"Das ist ein guter Schutz gegen
  Kälte"*). Text 5: Tobi defends his bicycle helmet on a winter walk with exactly that line.
- **`das Unglück` is a serious incident**, the CSV's *"Bei dem Unglück gab es viele
  Verletzte"*, not "bad luck". Text 2: Bruckner claims twenty-one years without one.
- **`die Gefahr` is the sign's word**, the CSV's *"Betreten der Baustelle auf eigene
  Gefahr"*. Text 5 puts the same sign at a frozen lake.
- **`die Flucht` / `fliehen` are the CSV's burglars** (*"Der Einbrecher ist sofort
  geflohen"*, *"war schon auf der Flucht"*). Text 6 is the only scene with a crime in it,
  and nothing is stolen.
- **`das Feuer`** is a fire, never *Feuer eröffnen* (the corpus's second-commonest verb).
- **`überfahren`** is a near-miss, told by the person who was nearly run over, and the
  car turns out to be parked.
- **`Achtung!`** is a printed sign (*"Achtung, Stufe!"*), and **`die Vorsicht`** is the
  spoken warning (*"Vorsicht, … sie frisst gerade das zweite Blatt"*). They sit in
  different texts (see below).

## Synonym / near-pair check

| set | kind | texts | ruling |
|---|---|:-:|---|
| `die Gefahr` / `das Risiko` | near-synonyms | 5 / 2 | **split.** `Risiko` is Neumann's office word (*"Ich gehe kein Risiko ein"*); `Gefahr` is on the sign at the lake |
| `der Unfall` / `das Unglück` / `die Katastrophe` | three ways to say *something went wrong* | 4 / 2 / 1 | **split three ways.** `Katastrophe` is the colloquial one, `Unglück` the serious one, `Unfall` the traffic one |
| `der Schutz` / `die Sicherheit` | near-synonyms | 5 / 2 | **split.** The safety word belongs to the new caretaker; the protection word belongs to the helmet |
| `die Vorsicht` / `Achtung!` | both are warning interjections | 3 / 2 | **split** |
| `beschädigen` / `zerstören` | degrees of the same thing | 6 / 6 | **left together on purpose.** It is a correction: Frau Wolf says *zerstört*, Neumann replies *"Zerstört ist da nichts … Beschädigt ist nur das Schloss."* The skill allows two near-synonyms in one exchange when a speaker is correcting another |
| `kaputtmachen` / `beschädigen` | near-synonyms | 4 / 6 | **split** |
| `kaputtgehen` / `kaputtmachen` | intransitive / transitive pair | 4 / 4 | **left together on purpose.** The contrast is the joke: *"Ich habe es nicht kaputtgemacht, es ist kaputtgegangen."* Tobi is avoiding the blame by changing the verb |

Derivational families left together, per the skill: `das Gift` / `giftig` (3),
`der Schutz` / `schützen` (5), `die Gefahr` / `gefährlich` (5), `die Flucht` / `fliehen` (6),
`kaputt` / `kaputtgehen` / `kaputtmachen` (4). `die Vorsicht` (3) and `vorsichtig` (4), and
`schaden` (3), `schädlich` (2) and `der Schaden` (4), are in different texts anyway.

## Scene order is ownership order

The scanner records a word at its **first** sighting, so a word must not appear in any
text before the one that owns it. The avoidances that cost something:

- **Texts 1–4 never say `gefährlich`, `Gefahr` or `warnen`** (Text 5). This is the
  batch's most expensive avoidance: the new caretaker in Text 2 is the natural speaker of
  *gefährlich*, and he says *Risiko* and *Sicherheit* instead.
- **Texts 1–4 never say `Schutz` or `schützen`** (Text 5). The scanner reads *Schutz* as a
  form of *schützen* and the other way round, so the two share an owner text. Text 4 has
  a helmet in it and does not mention it. Text 5 gets it instead.
- **Texts 1–5 never say `Lärm`** (Text 6). Text 1 has a smoke alarm going off, and says
  *"was piept da so"*.
- **Texts 1–3 never say `kaputt`** (Text 4), which costs Text 2 the obvious line about
  the lift. Bruckner's Text 7 complaint (*"Der Aufzug geht seit drei Jahren nicht"*) is not
  repeated.
- **Texts 1–2 never say `Vorsicht`, `Notfall` or `retten`** (Text 3), and **Texts 1–3
  never say `Unfall`, `vorsichtig` or `überfahren`** (Text 4).
- **Text 3 never says the noun `Schaden`.** The scanner credits the verb `schaden` from
  the noun (and from *schade*), so the verb's owner text, Text 3, comes first. The noun's
  owner text, Text 4, comes after it.
- **Text 1 never says `Unglück` or `Achtung`** (Text 2).
- **Every `sicher`/`sichere` comes after Text 1.** The scanner reads the adjective as a
  form of `sichern`.

Scanner artefacts to fix by hand after `scan --apply`:

- **`Achtung!`.** The headword carries its `!`, so it never matches a token. Recorded with
  `vocab.py use --batch 8 --text 2 "Achtung!"`. The card line is *"„Achtung, Stufe!" Eins
  pro Etage."*
- **`kaputtmachen` / `kaputtgehen`.** Only the infinitive is matched. The participles
  *kaputtgemacht* and *kaputtgegangen* are not, so both are recorded by hand for Text 4.

## Continuity with Batches 1–7

Checked against every dialogue in Batches 1–7. The facts this batch touches:

| fact | source |
|---|---|
| The house is **number 19**; Frau Wolf once gave the ambulance 17 | Batch 2, Text 6 |
| The lift has been broken for three years; the stairs are the only way up | Batch 1, Text 1; Batch 7, Text 12 |
| Julia lives on the **fourth floor**, next door to Frau Wolf | Batch 1, Texts 1–2 |
| Bruckner fell down *"die letzten vier Stufen"* of the stairs carrying a box; Julia was there | Batch 2, Text 6 |
| **Bruckner retired at the end of December**, 21 years as caretaker, stays in his flat downstairs (*"Ich bleibe unten in meiner Wohnung"*) with the cat; the Verwaltung's Chefin *"hat schon einen Neuen"* | Batch 7, Texts 10 and 12 |
| Bruckner lives alone, is a Nichtraucher, has a cat | Batch 3, Text 3; Batch 4, Text 2; Batch 7, Text 12 |
| **The cellar door sticks** (*"die Kellertür klemmt"*) | Batch 7, Text 12 |
| Frau Wolf's kitchen window looks onto the courtyard; the courtyard has a fence and bike stands | Batch 7, Text 4 (scenes.md); Batch 6, Text 4 |
| Tobi cooks badly (two lots of salt; the Lokal-level disaster in Batch 3) | Batch 3, Text 5 |
| Frau Wolf says **du** and *Kind* to Julia and Jule, **Sie** to Tobi; Julia says Sie to her | Batch 5, Texts 1 and 5; Batch 4, Text 1 |
| Bruckner and Julia say **Sie** to each other; Frau Wolf and Bruckner say **Sie** | Batch 4, Text 2; Batch 6, Text 4 |
| Julia, Tobi and Jule say **du** to each other | Batches 3–7 |

Decisions made as a result:

- **Herr Neumann is the new caretaker** from January, the *"Neuer"* of Batch 7, Text 10.
  He was not on stage in Batch 7, so he meets the house here.
- **Text 2 does not repair the lift.** It is still broken. Text 1's firefighters walk up
  four floors.
- **Text 1's address is right this time.** Frau Wolf says she gave *"die richtige
  Hausnummer"*. The house is 19 and the false 17 is not repeated.
- **Text 6's broken door is the sticking one from Batch 7.** The burglars forced it, and
  it no longer sticks. That is the scene's joke.
- **The farewell plant is new in this batch.** Batch 7, Text 12 names only one present
  (Tobi's cigar), so Text 3's *"eine Pflanze zum Abschied"* is a new fact, not a callback.

## New standing facts

- **Herr Neumann**, the caretaker from January. He says **Sie** to everybody and everybody
  says Sie to him. He goes by the rules, puts up signs (*"Achtung, Stufe!"* on every
  floor, *Notausgang* on the front door), and replaced Bruckner's salt with sand.
- **Bruckner, retired**, still lives downstairs (*unten*) and still salts the steps until
  Neumann takes the bucket away.
- **Frau Wolf gave Bruckner a red plant as a farewell present.** This is established
  here, in Text 3: Batch 7, Text 12 shows only Tobi's cigar, so the plant was given off
  stage. It is poisonous to cats but not deadly, and the cat eats it anyway.
- **Julia owns a bicycle.** Tobi borrowed it in January, fell on the ice in front of the
  house, broke the light and bent the front wheel (Text 4). He owes her a light.
- **Tobi wears a bike helmet** from then on, even on foot (Text 5).
- **There is a park with a lake** within walking distance, with a café on the far side
  (Text 5).
- **February break-in**: two men forced the cellar door at three in the morning, fled
  over the courtyard fence and took nothing. Frau Wolf called the police. The cellar
  door gets a new lock and **no longer sticks** (Text 6).

## Calendar

| when | text |
|---|---|
| first Saturday of January | 1. Tobi's rice sets off the alarm, and the Feuerwehr comes |
| the Monday after, Bruckner a week into retirement | 2. Neumann's first round of the stairwell |
| mid-January | 3. the cat and the plant |
| late January, ice | 4. Tobi's fall with Julia's bike |
| a Sunday in early February | 5. the frozen lake |
| a night in February | 6. the break-in |

## Cast

Same house, now January and February. **Julia** (fourth floor), **Tobi**, **Jule**,
**Frau Wolf** (next door), **Herr Bruckner** (retired, downstairs). New: **Herr
Neumann**, the caretaker.

| pair | form |
|---|---|
| Neumann ↔ everybody | Sie |
| Frau Wolf → Julia, Jule | du, *Kind* |
| Julia → Frau Wolf, Bruckner | Sie |
| Bruckner ↔ Frau Wolf | Sie |
| Julia ↔ Tobi ↔ Jule | du |

---

### Scene 1 — Samstagabend, vierter Stock

- **Premise:** Julia is working in the living room. Tobi is cooking in her kitchen and has
  burnt the rice. The smoke alarm on the ceiling goes off.
- **Angle:** Nothing is on fire, and everybody behaves as if something were. Frau Wolf has
  already dialled 112, and is proud that *this time* she gave the right house number. The
  firefighters will now climb four floors with no lift, for a pot.
- **Words (8):** der Alarm, das Feuer, brennen, (sich) verbrennen, der Notruf, die Feuerwehr, sichern, die Katastrophe
- **Chunks:** `Feuerwehr rufen` (304), `Notruf wählen` (652), `Feuer brennt` (476),
  `sich den Finger verbrennen` (270), `ein falscher Alarm` (663), *"Der Herd war noch heiß.
  Ich habe mich verbrannt"* (CSV), *"Der Urlaub war eine Katastrophe"* (CSV)
- **Deliberately absent:** `Lärm` (6), `Vorsicht`, `Notfall` (3), `kaputt`, `vorsichtig`,
  `Unfall` (4), `Unglück`, `Achtung` (2), `gefährlich`, `Gefahr` (5)

### Scene 2 — Der Neue

- **Premise:** Monday, early January. Herr Neumann, the new caretaker, is sticking signs
  to the stairwell walls. Bruckner, a week into retirement, is salting the steps as he has
  every winter. Julia is on her way down.
- **Angle:** Neumann sees risk everywhere; Bruckner sees only things he looked after for
  twenty-one years. Bruckner's claim of twenty-one years without an *Unglück* is
  contradicted by Julia, who found him at the foot of these stairs (Batch 2, Text 6).
  Neumann ends by taking his salt away.
- **Words (6):** Achtung!, die Sicherheit, der Notausgang, das Unglück, das Risiko, schädlich
- **Chunks:** *"Der Notausgang ist gleich hier bei der Treppe"* (CSV), `Risiko ist groß` (425; *kein Risiko eingehen* is
  not in the top 15 and is written from ordinary usage), *"Rauchen ist schädlich für die
  Gesundheit"* (CSV — here *schädlich für die Stufen*), *"Sicherheit ist für mich sehr
  wichtig"* (CSV)
- **Deliberately absent:** `gefährlich`, `Gefahr`, `warnen`, `Schutz` (5), `kaputt` (4)

### Scene 3 — Die rote Pflanze

- **Premise:** Mid-January. Bruckner's cat has bitten the red plant Frau Wolf gave him as
  a farewell present (new in this batch; not shown in Batch 7). He calls Julia in to look it up on her phone.
- **Angle:** The man who claimed twenty-one years without an incident declares a
  *Notfall* over half a leaf. Frau Wolf is offended on her plant's behalf, and while they
  argue the cat eats the second leaf.
- **Words (7):** der Notfall, das Gift, giftig, tödlich, retten, die Vorsicht, schaden
- **Chunks:** *"Vorsicht, das ist giftig!"* (CSV), *"Dieses Gift kann für den Menschen
  tödlich sein"* (CSV), *"Ein kleines Glas Wein kann nicht schaden"* (CSV), *"Wir haben
  einen Notfall"* (CSV)
- **Deliberately absent:** the noun `Schaden` (4), `gefährlich` (5)

### Scene 4 — Glatteis

- **Premise:** Late January. Tobi borrowed Julia's bicycle without saying so, slipped on
  the ice in front of the house and is now telling her about it.
- **Angle:** He tells it as a near-death experience; the car that almost ran him over has
  been parked there since Monday. Then he has to confess the bike, and changes the verb
  to dodge the blame.
- **Words (7):** der Unfall, überfahren, kaputt, kaputtmachen, kaputtgehen, der Schaden, vorsichtig
- **Chunks:** *"Ich hatte letzte Woche einen Unfall"* (CSV), *"Gestern hat ein Autofahrer
  einen Hund überfahren"* (CSV), *"Wer hat die Lampe kaputtgemacht?"* (CSV), *"Bitte fahr
  vorsichtig, die Straße ist glatt"* (CSV), `einen Unfall haben` (4730), `Schaden ist groß` (212 — here
  played down to *klein*)
- **Deliberately absent:** `Schutz`, `schützen` (5, so the helmet stays unmentioned),
  `gefährlich` (5), `beschädigen` (6)

### Scene 5 — Der See im Park

- **Premise:** A cold Sunday in February. Jule wants to take a shortcut across the frozen
  lake to the café. There is a sign.
- **Angle:** A role reversal. Tobi, who rode a bike on ice two weeks earlier, has become
  the cautious one and is wearing his new helmet for a walk. Jule notices, and so does the
  reader.
- **Words (5):** die Gefahr, gefährlich, warnen, der Schutz, schützen
- **Chunks:** *"Betreten der Baustelle auf eigene Gefahr"* (CSV), *"Das ist ein guter Schutz
  gegen Kälte"* (CSV), *"Ich warne Sie"* (CSV), `vor Gefahr warnen` (170)
- **Deliberately absent:** `Lärm` (6)

### Scene 6 — Die Kellertür

- **Premise:** The morning after a break-in. Frau Wolf called the police at three. Neumann
  has just been down to the cellar, and Bruckner comes up the stairs.
- **Angle:** Frau Wolf reports a disaster and Neumann reports a lock. The burglars took
  nothing and forced the cellar door, which had stuck for years and now opens easily.
  Bruckner is hurt that two strangers fixed it in one night.
- **Words (5):** der Lärm, fliehen, die Flucht, zerstören, beschädigen
- **Chunks:** *"Der Einbrecher ist sofort geflohen"* (CSV), *"Der Einbrecher war schon auf
  der Flucht"* (CSV), *"Bitte machen Sie eine Liste davon, was die Einbrecher beschädigt
  haben"* (CSV), `Lärm machen` (1523)
- **Note:** `Einbrecher` and `Polizei` are Batch 13 words. They are incidental here and get
  their own scenes there.

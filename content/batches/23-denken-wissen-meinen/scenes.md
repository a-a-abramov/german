# Batch 23 — Denken, Wissen & Meinen · Szenenplan

152 target words, **twelve scenes**, five to eighteen words each. This is the corpus finale,
September Y4, and its spine is **the lift**: broken since two years before Julia moved in,
it is finally repaired. Around the repair people do what the topic's verbs describe:
they doubt the notice (1), guess how it happened (2), argue about how the lift broke and
fetch a notebook as proof (7), decide who rides first (10), and remember the first viewing (12).
Side scenes carry the knowledge words: Tobi decides about the Werkstatt (4), a quiz
night against scientists (5), Jule admits that "Lisa" was a lie (8).

The topic's hazard is **abstract talk**: 152 mental verbs and nouns invite people
discussing opinions in general. Every word is tied to a concrete object or act: a notice on
the door, a coin, a crossword clue, a notebook from five years ago, a list on Neumann's clipboard.

## Sense decisions made against the CSV

- **`der Schein`** is a banknote (*"nur Scheine"*), Text 5: *"in kleinen Scheinen"*. Not appearance.
- **`die Praxis`** is practice vs. theory (*"In der Praxis ist vieles ganz anders"*), Text 4.
  Not the doctor's surgery.
- **`die Lage`** is location (*"zentrale Lage"*), Text 12: Bruckner at the viewing *"hat nur
  noch von der Lage geredet"*, i.e. B1 T1's *"Fünf Minuten bis ins Zentrum"*.
- **`der Bescheid`** is the Verwaltung's official decision (*"Den endgültigen Bescheid erhalten
  Sie …"*), Text 1. Different item from `Bescheid geben` (4) and `Bescheid sagen` (11).
- **`unentschieden`**: CSV sense 1, a draw (*"Es steht unentschieden"*), the quiz, Text 5.
  Tobi's indecision in Text 4 is shown, not named.
- **`die Wahl` / `wählen`**: choosing sense only, per the coordinator (Batch 20 owns the June
  election): *"Sie haben die Wahl: nach Stockwerk oder nach Alphabet"* (10), *"zwischen drei
  Antworten wählen"* (5). No election is staged or mentioned.
- **`der Faktor`**: sun-cream factor (*"Faktor fünfzig"*), Text 3, the CSV's example.
- **`fassen`**: *"einen Entschluss fassen"* (CSV 2), Text 12. Not catching a thief.
- **`festhalten`**: holding the ladder (3) and *"halten Sie sich fest"* (11). Owner Text 3.
- **`bewegen`**: physical movement (*"bewegt sich keinen Zentimeter"*, 6; *"Bewegen Sie sich
  nicht so!"*, 3). Owner Text 3 by first sighting.
- **`die Störung`**: *"Entschuldigen Sie die Störung"* (CSV), Paulsen in the stairwell, Text 9.
- **`die Nachfrage`**: demand for a product (CSV): the lift part nobody builds, Text 6.
- **`reichen`**: *"Das reicht mir nicht"* (CSV 1), Text 3.
- **`mischen`**: *"gemischte Gefühle"*, Text 12. CSV examples are *gemischtes Eis* / *gemischt,
  große und kleine Scheine*; the participle in the same "mixed" sense.
- **`die Konkurrenz`**: competitors (CSV 1/2), the scientists' team at the next table, Text 5.
- **`die Tat`**: *"gute Tat"* (CSV), Text 2.
- **`die Art`**: CSV sense 2, a person's manner (*"das ist so meine Art"*), Text 7.
- **`der Typ`**: CSV sense 1, a guy (*"der Typ von der Straße"*), Text 8.

## Synonym / near-pair check (ledger, after `scan --apply`)

| set | texts | ruling |
|---|:-:|---|
| `die Realität` / `die Wirklichkeit` | 9 / 7 | split |
| `merkwürdig` / `seltsam` | 6 / 11 | split; Paulsen says one, Neumann the other |
| `Bescheid geben` / `Bescheid sagen` | 4 / 11 | split |
| `merken` / `bemerken` / `auffallen` | 7 / 11 / 2 | split three ways |
| `achten` / `beachten` | 11 / 1 | split; both Neumann, two different days |
| `beschließen` / `entscheiden` / `sich entschließen` / `(Entschluss) fassen` | 1 / 4 / 8 / 12 | split four ways: the Verwaltung *beschließt*, Tobi *entscheidet*, Jule *entschließt sich*, Frau Wolf *fasst einen Entschluss* |
| `annehmen` (accept) / `akzeptieren` | 4 / 10 | split |
| `vermuten` / `schätzen` / `erwarten` | 2 / 3 / 6 | split |
| `erkennen` / `realisieren` | 8 / 12 | split |
| `die Situation` / `die Lage` | 11 / 12 | split (and Lage is location anyway) |
| `der Einfall` / `der Gedanke` | 10 / 12 | split |
| `das Wissen` / `die Kenntnisse` | 5 / 4 | split |
| `die Meinung` / `die Überzeugung` | 10 / 12 | split |
| `vernünftig` / `sinnvoll` | 3 / 10 | split |
| `die Wahl` / `die Alternative` | 10 / 4 | split |
| `der Respekt` / `die Rücksicht` | 2 / 10 | split |
| `der Sinn` / `sinnlos` | 11 / 4 | split; Tobi on the coin toss: *"Das ist doch sinnlos!"* |
| `die Art` / `der Typ` | 7 / 8 | split |
| derivational pairs together, per the skill | | `Zweifel` (1) / `zweifeln` (12); `Beweis`/`beweisen` (7); `Lüge`/`lügen` (8); `Wissenschaft`/`Wissenschaftler` (5); `erfinden`/`Erfindung` (5); `Einfluss`/`beeinflussen` (2); `lösen`/`Lösung` (9); `sich verhalten`/`Verhalten` (8); `Entscheidung`/`entscheiden` (4); `alternativ` (1) / `Alternative` (4); `abhängen` (4) / `abhängig` (12) |

`glauben`, `denken`, `meinen`, `finden` and `wissen` recur throughout; they are the
everyday opinion verbs and never gloss each other inside a turn.

## Ownership and scanner fixes

After `scan --apply` these were corrected with `unuse` + `use` (a rescan brings the scanner's
rows back; the owners below are the card sources):

- **`meinen`** → Text 7 (*"Was meinen Sie, Frau Wolf?"*). Scanner: *Meine* in Text 1.
- **`die Alternative`** → Text 4 (*"Und die Alternative?"*). Scanner: *alternativ* in Text 1.
- **`zweifeln`** → Text 12 (*"Zweifelst du etwa daran?"*). Scanner: the noun in Text 1.
- **`kennen`** → Text 8 (*"Dich kenne ich doch!"*). Scanner: *kann* in Text 6.
- **`scheinen`** → Text 11 (*"Es scheint, wir hängen fest."*). Scanner: *Scheinen* in Text 5.
- **`entschlossen`** → Text 10 (*"Ich bin fest entschlossen"*). Scanner: Jule's *habe mich
  entschlossen* in Text 8, which belongs to `sich entschließen`.
- **`kennenlernen`** (*kennenzulernen*, Text 8) and **`sich irren`** (*irrst*, Text 5): scanner
  misses, added with `use`.
- **Glue `irgendein`** (ledger lemma `irgendirgendein`, a CSV typo): *"irgendeine Zahl"*, Text 5,
  added with `use`. Glue pool now 326/326.
- Band-5 words land where they first fall: `wichtig`, `glauben` (1), `wissen`, `denken` (4),
  `finden` (5). `das Verhalten` is credited from *Verhalte* (Text 8), where the noun also stands
  (*"Dein Verhalten ist peinlich"*). `der Bescheid` (1) is the noun; cards for `Bescheid geben`/
  `sagen` come from Texts 4 and 11.

## Skipped (2)

- **`auflösen`**: CSV sense is dissolving a tablet. No medicine fits this September without a bolt-on line.
- **`die Herkunft`**: the only home was Tobi questioning Moritz about where he comes from,
  which turns into an identity joke. Left out.

## Continuity

Checked against continuity.md (B1–B10), slots.md, B1 T1 and B7 T7 directly, B11 in full,
and the coordinator's notes on B14 and B20.

| fact this batch touches | source |
|---|---|
| Lift "in Reparatur" for 2 years at the late-Oct Y1 viewing; Bruckner: *"Aber Treppen halten jung"*; *"zentraler können Sie nicht wohnen"* | B1 T1 (quoted in Text 12) |
| So in Sept Y4 it has been broken **fast fünf Jahre** (Texts 1, 6, 12). Julia has lived there **fast drei Jahre** (Text 12) | B1 T1, B7 T12 |
| Only this batch may repair the lift | slots.md |
| Neumann: caretaker, says Sie to everyone, signs and rules, Hausordnung | B8 T2, B9 T5, B10 T7 |
| The Verwaltung's Chefin | B7 T10 |
| Frau Wolf: 4th floor, hears everything through the wall; du + *Kind* to Julia, Sie + *junger Mann* to Tobi; *Kinder* to both | B4 T1, B9 T14 |
| Frau Wolf ↔ Bruckner Sie/Sie; Julia → Bruckner Sie | B6 T4, B7 T10 |
| Frau Wolf's mother's things in the cellar | B5 T1 |
| Bruckner: retired, EG, cat, model railway, toolbox in the cellar, his Lager in the cellar | B7 T10, B10 T5, T9, B1 T7 |
| Pear tree; pears in September; Frau Wolf bakes pear cake; Neumann allows picking then | B9 T4 |
| Jule: *"Sie heißt Lena. Nein, Lisa."*; Tobi saw her kiss "ihn" in the street, Nov Y2 | B7 T7 |
| Tobi: Mechaniker in the Uni's Werkstatt; Kaminski retires "im Sommer" Y4 after 31 years and offered him the Leiter post; it needs two years of evening Meister training; Tobi undecided | B14 (per coordinator), B14 T13–14 |
| Kneipe | B3 T10 |
| Bruckner's age is not stated (66 in Nov Y2) | B7 T10 |

Decisions:
- **No year numbers, no city name.** Dates in dialogue are only *"ab dem vierzehnten
  September"* (the notice) and *"Vierzehnter Oktober"* (Bruckner's notebook, the day the lift broke).
- **Kaminski is gone by September** (he retired in the summer), so Tobi's choice is still open
  only because he has been doing Kaminski's work since August **without signing**. The Uni
  wants an answer by Friday.
- **Lisa resolved, minimally:** Jule lied; the person Tobi saw is Moritz. In Nov Y2 it was one
  evening, then they lost touch; they have been together **since January Y4** (fits B17 T4
  *"Ich habe mich im Januar verliebt"*). Tobi asks if this was her cut-off news from the train
  (B18 T15). Nothing about engagement or living together.
- Nothing from B12–B22 events is relied on. The drafts on disk were used only to avoid name
  collisions and to check the lift arithmetic: B17's April Fool line *"nach über vier Jahren"*
  agrees with it.

## New standing facts

- **The lift is repaired.** Notice on Wed 1 Sep: the Verwaltung *hat beschlossen*, repair
  *genehmigt*, work from **14 Sep**. Done by **Sat 25 Sep**. On the first ride Neumann,
  Frau Wolf and Bruckner were **stuck for forty minutes between the 3rd and 4th floor**; it
  works after that.
- **How it broke:** on **14 October**, almost five years earlier, it stopped between the 2nd and 3rd floor carrying Frau
  Wolf, her mother's wardrobe (≈200 kg) and Bruckner with his toolbox (Bruckner's notebook).
- **The missing part** was ordered by Bruckner back then and has lain in his cellar ever
  since; the Verwaltung would not pay for the repair, and nobody asked him.
- **Why now:** in August Frau Wolf invited the Verwaltung's Chefin for coffee on the 4th floor
  (she had to sit down for ten minutes) and showed her **59 letters** about the lift.
- **Herr Paulsen**, the lift company's man. Sie with everyone; *"meine Damen"*.
- **Frau Wolf keeps taking the stairs** "aus Überzeugung", and now gets on well with Neumann.
- **Tobi takes the Werkstatt**: Leiter from **October Y4**; decided by a coin toss he tried to
  overrule (*"Zwei von drei!"*).
- **Jule's boyfriend is Moritz**, the man Tobi saw in Nov Y2 (one evening then; together since
  January Y4); "Lisa" was a lie. Moritz has a
  younger sister. du with Tobi.
- Julia, Tobi and Jule **won the Kneipe quiz** (€100) against scientists from a Konferenz at the Uni.
- Bruckner picked about **20 kg of pears**; Frau Wolf held the ladder.

## Calendar (September Y4)

| when | text |
|---|---|
| Wed 1 Sep, morning | 1. the notice |
| Thu 2 Sep | 2. Frau Wolf's coffee with the Chefin comes out |
| Sat 4 Sep | 3. pears |
| Thu 9 Sep, evening | 4. coin toss (Uni wants an answer by Fri 10) |
| Fri 10 Sep, evening | 5. quiz night |
| Tue 14 Sep | 6. Paulsen's first look; the part in the cellar |
| Wed 15 Sep | 7. the notebook |
| Sun 19 Sep | 8. Moritz |
| Wed 22 Sep | 9. crossword on the 2nd-floor landing |
| Thu 23 Sep | 10. Neumann's list |
| Sat 25 Sep, afternoon | 11. first ride, stuck |
| Sat 25 Sep, night | 12. through the wall |

Weekdays follow B10/B11's Y3 calendar (Mon 20 Jul, Sat 8 Aug Y3) moved one year on, assuming Y4
is not a leap year, so 1 Sep Y4 is a Wednesday. Dialogue names no weekday with a date.

## Cast

| speaker | address |
|---|---|
| Julia, Tobi, Jule | du |
| Frau Wolf | du + *Kind* to Julia; Sie + *junger Mann* to Tobi; Sie to Neumann, Bruckner, Paulsen |
| Herr Bruckner | Sie with Frau Wolf, Neumann, Paulsen, Julia |
| Herr Neumann | Sie to everyone |
| Herr Paulsen (new) | Sie; *meine Damen* |
| Moritz (new) | du with Jule and Tobi |

---

### Scene 1 — Wir bitten um Ihr Verständnis
- **Premise:** Wed 1 Sep, entrance hall. Neumann has pinned a notice; Frau Wolf has no glasses, Julia reads it out.
- **Angle:** Frau Wolf believes it only when she is standing inside. The notice offers the stairs *alternativ*: she has used that alternative for almost five years.
- **Words (16):** die Nachricht, wichtig, beachten, beschließen, genehmigen, feststehen, wahr, wirklich, der Bescheid, die Zustimmung, der Zweifel, ablehnen, die Begründung, glauben, alternativ, das Verständnis
- **Chunks:** `Zweifel(Akk.) haben`, *"ohne Begründung"* (CSV), *"Wir bitten um Ihr Verständnis"*, *"Bitte beachten Sie …"* (CSV)

### Scene 2 — Kaffee im vierten Stock
- **Premise:** Julia and Tobi suspect a connection between the Chefin's August visit and the repair.
- **Angle:** No scheme, says Frau Wolf: only coffee, cake, 59 letters and four floors of stairs. *"Überzeugt hat sie die Treppe ganz allein."*
- **Words (11):** auffallen, vermuten, der Zusammenhang, der Inhalt, die Absicht, geheim, (sich) überzeugen, beeinflussen, der Respekt, der Einfluss, die Tat
- **Chunks:** *"gute Tat"* (CSV), `Entscheidung(Akk.) beeinflussen`, *"Respekt!"* (CSV 3)

### Scene 3 — Zwanzig Kilo Birnen
- **Premise:** Sat 4 Sep, the pear tree; Bruckner is up the ladder as every year. Bruckner on the ladder, Frau Wolf below with sun cream.
- **Angle:** Each calls the other unreasonable; the ladder shakes because she does.
- **Words (8):** die Beschäftigung, reichen, die Nähe, festhalten, der Faktor, vernünftig, schätzen, bewegen
- **Chunks:** *"Ich schätze, um die Fünfzig"* (CSV), *"Das reicht mir"* (CSV), *"Halt dich gut fest"* (CSV)

### Scene 4 — Kopf oder Zahl
- **Premise:** Thursday night; Tobi has a pro/contra list; the Uni wants an answer by Friday.
- **Angle:** Julia's method: toss a coin (*"Das ist doch sinnlos!"*). It says no, Tobi demands "best of three" and so finds out what he wants.
- **Words (17):** die Liste, Bescheid geben, nachdenken, der Unterschied, die Praxis, abhängen, die Kenntnisse, die Alternative, die Methode, die Entscheidung, annehmen, entscheiden, sinnlos, beschäftigen, wissen, führen, denken
- **Chunks:** `ein(e) schwere(r) Entscheidung`, *"Kannst du mir bis morgen Bescheid geben?"* (CSV), *"In der Praxis ist vieles ganz anders"* (CSV)

### Scene 5 — Die Konkurrenz am Nebentisch
- **Premise:** Fri 10 Sep, Kneipe quiz, tied with scientists from a conference; last question: the first safe lift.
- **Angle:** Tobi: *"In unserem Haus ist er jedenfalls noch nicht erfunden."* Jule is right, Tobi is wrong, and the scientists lose.
- **Words (18):** unentschieden, der Wissenschaftler, die Konferenz, die Konkurrenz, finden, das Wissen, nachschlagen, die Reihe, erfinden, wählen, der Tipp, die Ahnung, sich irren, bekannt, die Erfindung, die Wissenschaft, der Schein, entdecken
- **Note:** 18 is above the brief's cap of 16; `finden` and `wählen` are incidental, so 16 were designed.
- **Chunks:** *"Es steht unentschieden"* (CSV), *"Wer ist jetzt an der Reihe?"* (CSV), *"Kannst du mir einen Tipp geben?"* (CSV), *"Ich habe keine Ahnung"*

### Scene 6 — Das Teil im Keller
- **Premise:** Tue 14 Sep. Paulsen reports to Neumann; Bruckner stands by.
- **Angle:** The part nobody makes any more has lain in Bruckner's cellar for almost five years. Nobody asked.
- **Words (11):** gründlich, der Zustand, erwarten, merkwürdig, sichtbar, feststellen, das Problem, die Nachfrage, ordentlich, die Überraschung, ausschließen
- **Chunks:** *"in sehr schlechtem Zustand"* (CSV), *"konnte aber nichts feststellen"* (CSV), *"Die Nachfrage … ist groß"* (CSV)

### Scene 7 — Das Heft von damals
- **Premise:** Julia asks how the lift broke. Frau Wolf and Bruckner each remember the other one doing it.
- **Angle:** Bruckner's notebook is the proof: both of them were in it. Frau Wolf reads it as a win.
- **Words (11):** erinnern, geschehen, die Tatsache, widersprechen, die Erinnerung, merken, die Art, der Beweis, meinen, beweisen, die Wirklichkeit
- **Chunks:** *"Ich erinnere mich noch genau an …"* (CSV), *"Ich kann mir keine Zahlen merken"* (CSV), `Tatsache ist/wird Beweis`, *"In Wirklichkeit …"* (CSV)

### Scene 8 — Lisa
- **Premise:** Sun 19 Sep. Jule introduces Moritz.
- **Angle:** Tobi recognises the man from the street almost two years ago (one evening then; together since January). "Lisa" was a lie, and Tobi's reaction shows why Jule told it.
- **Words (15):** sich verhalten, kennen, erkennen, der Typ, kennenlernen, die Lüge, lügen, das Gewissen, das Geheimnis, sich entschließen, die Wahrheit, die Reaktion, typisch, das Verhalten, der Eindruck
- **Chunks:** *"ein ganz schlechtes Gewissen"* (CSV), *"an seiner Stimme erkannt"* (CSV), *"einen guten Eindruck machen"* (CSV), *"Diese Reaktion ist typisch für ihn"* (CSV)

### Scene 9 — Sechs Buchstaben
- **Premise:** Wed 22 Sep. Frau Wolf rests on a chair on the 2nd-floor landing with her crossword.
- **Angle:** "Way up, six letters": *Aufzug* and *Treppe* both fit. From Saturday the answer is *Aufzug*.
- **Words (5):** lösen, einfallen, die Realität, die Störung, die Lösung
- **Chunks:** *"Entschuldigen Sie bitte die Störung"* (CSV), *"Mir ist wieder eingefallen …"* (CSV)

### Scene 10 — Die Reihenfolge
- **Premise:** Thu 23 Sep. Neumann's list for the first ride: floor by floor.
- **Angle:** By floor Bruckner in the Erdgeschoss comes first; by alphabet Frau Wolf comes last (*"W wie Wolf"*). Compromise: all three ride together.
- **Words (15):** die Liste (also 4), die Reihenfolge, festlegen, sinnvoll, die Meinung, entschlossen, begründen, die Wahl, aufmerksam, gelten, die Rücksicht, sich einigen, der Kompromiss, der Einfall, akzeptieren, zustimmen
- **Chunks:** *"Habt ihr den Termin schon festgelegt?"* (CSV), *"Nehmen Sie bitte Rücksicht auf …"* (CSV), *"Ich mache Sie darauf aufmerksam, dass …"* (CSV), `Kompromiss(Akk.) finden`

### Scene 11 — Halten Sie sich fest
- **Premise:** Sat 25 Sep. The three in the cabin; it stops between 3rd and 4th.
- **Angle:** Bruckner plays pilot, Neumann says it's under control, Frau Wolf wants distance in a cabin with no room, and Bruckner has brought the toolbox, as he did the day it broke.
- **Words (12):** achten, das Ziel, sich nähern, bemerken, seltsam, reagieren, scheinen, der Sinn, die Situation, Bescheid sagen, vorkommen, die Distanz
- **Chunks:** *"Halt dich gut fest"* (CSV), *"Er nähert sich … ganz langsam"* (CSV), *"Das kann vorkommen"* (CSV), *"Es hat keinen Sinn"* (CSV)

### Scene 12 — Treppen halten jung
- **Premise:** Saturday night, Julia's flat. Julia quotes Bruckner's line from the viewing.
- **Angle:** Frau Wolf, through the wall, closes the corpus: after almost five years of fighting for the lift she will keep taking the stairs, because stairs keep you young.
- **Words (11):** die Lage, die Erinnerung (also 7), realisieren, mischen, abhängig, der Gedanke, zweifeln, die Stimmung, das Verhältnis, überraschen, fassen, die Überzeugung
- **Chunks:** *"An diese Zeit habe ich viele schöne Erinnerungen"* (CSV), *"einen Entschluss gefasst"* (CSV), *"ein gutes Verhältnis zu …"* (CSV)

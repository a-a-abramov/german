# Batch 17 — Gefühle & Charakter · Szenenplan

115 target words. **Thirteen scenes**, six to twelve words each, March to April of Y4.

The topic's hazard is the inventory: forty adjectives of feeling and character that could
be recited as *"Ich bin froh, stolz und dankbar"*. So no speaker names their own feeling
from a list. Each feeling or trait comes out of something that has just happened on the
page, and usually somebody else names it:

- Tobi loses 4:0 and is called a *schrecklicher Verlierer* (Text 1).
- The cat bites Neumann, who is *ängstlich* but claims *Respekt* (Text 2).
- Frau Wolf watches the stairwell for twenty minutes and is *neugierig*, which she
  corrects to *interessiert* (Text 3).
- Tobi cooks something edible, Julia calls it a *Wunder*, and he is *beleidigt* (Text 6).
- Bruckner says he likes being *allein*, then puts the birthday into his timetable (Text 12).

Rules of thumb used throughout: at most one feeling adjective per turn where possible, no
coordination chunks (*stolz und glücklich*, *Hoffnung und Angst*), and every trait word is
a reaction to the line before it.

## Sense decisions made against the CSV, not against the corpus

- **`arm` is poor** (CSV: *"Die Regierung hilft armen Nachbarländern"*), not the pitying
  *du Arme*. Text 10: Oma Erna, *"Opa und ich waren früher arm"*.
- **`befreit` is exempt** (CSV: *"von den Rundfunk-Gebühren befreit"*), not "relieved".
  Text 8: Julia was *"in der Schule zwei Jahre vom Sport befreit"*. Relief is
  `erleichtert` (Text 5).
- **`geehrt` exists only in *Sehr geehrte …***. Letters belong to Batch 18, so it lives in
  Bruckner's mock-formal birthday speech in Frau Wolf's kitchen (Text 13).
- **`befriedigend` is a grade** (CSV: *"Das Ergebnis ist befriedigend"*). Schools belong to
  Batch 15, so Gisela grades the soup: *"Befriedigend. Eine Drei."* (Text 9).
- **`begrenzt`** (CSV: *"auf 12 begrenzt"*, a course) is the limited space in the
  stairwell: *"Im Treppenhaus ist der Platz begrenzt"* (Text 11). Courses belong to
  Batch 15.
- **`wirken` / `die Wirkung` are a tablet working** (CSV: *"Die Tabletten haben nicht
  gewirkt"*), never "to seem". Text 1.
- **`der Friede`** is *Frieden* as peace in the house (CSV: *"Endlich ist hier
  Frieden!"*). Text 11.
- **`lieb`** is CSV sense 1, a well-behaved animal: *"Die ist ganz lieb"* (Text 2).
- **`ruhig`** is keeping calm (Texts 2 and 5). **`still`** is silence (*"ganz still"*,
  Text 3).
- **`leicht`** is sense 2, easy (*"Das Rezept ist leicht"*), not light in weight. Text 6.
- **`eilen`** is CSV *"Es eilt"* (Text 2). **`die Eile`** is *in Eile sein* (Text 10).
- **`der Kellner`** is the D form the CSV gives alongside *Ober* (Batch 3 used *Ober*).
- **`aufregen`** is reflexive, *"Ich rege mich auf"* (Text 11); the CSV's *"Es regt mich
  auf"* would also do.
- **`ernst`** is *"etwas Ernstes"*, a serious relationship (Text 4). The CSV example is
  *"ein ernstes Problem"*; the adjective is the same.

## Synonym / near-pair check

| set | kind | texts | ruling |
|---|---|:-:|---|
| `froh` / `glücklich` / `fröhlich` / `vergnügt` | four shades of happy | 5 / 13 / 10 / 4 | **split four ways** |
| `die Freude` / `das Vergnügen` / `die Lust` | pleasure | 13 / 10 / 8 | **split** |
| `wütend` / `böse` / `ärgerlich` / `(sich) ärgern` / `aufregen` | anger | 1 / 7 / 9 / 9 / 11 | **split**, except `ärgerlich` + `ärgern` (one family) in Text 9 |
| `die Angst` / `(sich) fürchten` | fear | 2 / 5 | **split** |
| `ruhig` / `still` | quiet | 2 / 3 | **split.** Text 5 says *ruhig* (Tobi claims he was calm) and Julia's silence is *"du sagst ja gar nichts"*, not *still* |
| `die Ruhe` / `der Friede` | *in Ruhe / in Frieden* | 12 / 11 | **split** |
| `wunderbar` / `wunderschön` / `klasse` | praise | 6 / 13 / 10 | **split** |
| `dringend` / `eilig` / `eilen` | urgency | 11 / 9 / 2 | **split** |
| `ernst` / `ernsthaft` | serious | 4 / 7 | **split** |
| `schade` / `leider` | regret | 12 / 5 | **split** |
| `angenehm` / `gemütlich` / `entspannend` | pleasant | 9 / 12 / 8 | **split** |
| `befreit` / `erleichtern` | (false friends) | 8 / 5 | **split** |
| `traurig` / `einsam` | sad / lonely | 10 / 12 | **split** |
| `neugierig` / `interessiert` | curious | 3 / 3 | **left together on purpose.** It is a correction: Frau Wolf, *"Ich bin nicht neugierig, Kind, ich bin interessiert."* The euphemism is the joke |
| `kritisieren` / `kritisch` / `die Kritik` | one family | 9 | **together.** Gisela: *"Kritisieren? Ich bin nur kritisch."* |
| `das Glück` / `das Pech` | antonyms | 13 / 1 | **split** |
| `loben` / `kritisieren` | antonyms | 6 / 9 | **split** |
| `frech` / `höflich` | antonyms | 2 / 3 | **split** |

Derivational families left together, per the skill: `die Angst`/`ängstlich` (2),
`wirken`/`die Wirkung` (1), `verliebt`/`sich verlieben`/`die Liebe`/`lieben` (4),
`das Wunder`/`sich wundern`/`wunderbar` (6), `faul`/`faulenzen` (8), `die Kritik`/
`kritisch`/`kritisieren` (9), `ärgerlich`/`ärgern` (9), `das Vergnügen`/`sich vergnügen` (10),
`das Interesse`/`interessant` (12), `(sich) wünschen`/`der Wunsch`, `das Glück`/`glücklich` (13).

## Scanner notes (ownership)

The scanner records the first sighting. The order of the texts follows the calendar, and
these are the known mismatches between the scanner and the scene that owns a word:

- **`lieben`**: Text 2's *lieb* is read as `lieben`. The owner is Text 4 (*"Ich liebe
  private Geschichten"*), recorded with `use --text 4`. The card comes from Text 4.
- **`vertrauen` (verb)**: Text 2's *Vertrauen* is read as the verb too. The owner is
  Text 4 (*"Ich vertraue dir"*), recorded by hand in the ledger (`resolve()` picks the
  noun for `use "vertrauen"`, so the row was written with SQL). Card from Text 4.
- **`sich vergnügen`**: Text 4's *vergnügt* (the adjective) is also a form of the verb.
  The owner is Text 10 (*"Ich vergnüge mich"*), recorded with `use --text 10`. Card from
  Text 10.
- **`sich wundern`** is read from *Wunder*, but both are in Text 6. The card uses
  *"Da wundere ich mich aber"*.
- **`interessieren`** is read from *interessiert* in Text 3, which also contains
  *"Mich interessiert das überhaupt nicht"*. Both own Text 3.
- **`aufregen`** is matched on *rege* in *"Ich rege mich auf"* (Text 11).
- **`(sich) ärgern`** is matched on *ärger* in *"Mama, ärger dich nicht"* (Text 9).
- **`gefallen`** belongs to Text 10 (*"Gefällt Ihnen das Fest?"*). `sich etwas gefallen
  lassen` belongs to Text 11 (*"Das lasse ich mir nicht gefallen"*). Texts 1–9 never say
  *gefällt* or *gefallen*.
- Kept out of every text before its owner: `allein` (12), `Glück` / `wünsche` (13),
  `freue` (7), `Lust` (8), `leider` / `froh` (5), `ruhig` (2), `hoffe` (12), `dringend` (11),
  `traurig` (10).

## Continuity

Checked against `scratchpad/continuity.md` (Batches 1–10) and `slots.md`. Batches 11–16 are
being written in parallel. This batch refers to nothing that happens between August Y3
and March Y4, and it fixes no job, no subject of study and no hobby.

| fact | source |
|---|---|
| The lift has been broken since two years before the move-in (autumn Y1), so *"über vier Jahre"* in April Y4 | B1 T1; B7 T12 |
| Frau Wolf hears everything through the wall; says du + *Kind* to Julia, Sie + *junger Mann* to Tobi | B4 T1; B7 T6; B9 T14 |
| Frau Wolf phones Bruckner about the heating; the heating is on until 1 May | B7 T10; B9 T5 |
| Bruckner, retired, lives in the Erdgeschoss with his cat; electric model railway, timetable, *"Bei mir ist alles pünktlich"*; Leon visits | B7 T10; B9 T11; B10 T9 |
| Neumann: Sie with everyone, Hausordnung, signs; *"Das hätte es bei Herrn Bruckner nicht gegeben"*; Bruckner lay on the lawn | B8 T2; B9 T4–5 |
| The Lorenzes live separated in the flat under Julia, with **two doorbells**; he has a new partner | B7 T8 |
| Jule's secret date: "Lisa" (Jule), "ihn" (Tobi). **Left open**: Jule names no one and no gender | B7 T7 |
| Tobi: surname Wagner; plays football on Saturdays; can't cook (burnt rice, salted twice); tooth *hinten links* pulled by Frau Roth, while claiming to be calm | B2 T5; B3 T5; B8 T1; B9 T1 |
| Kessler sells eggs; Jule buys eggs only from him | B4 T3 |
| Gisela is Tobi's mother; Werner his father; Tobi says *Mama* | B7 T2; B10 T6, T8 |
| Oma Erna (*Frau Wagner* for Julia) in the Altenheim; *"Opa hat immer gesagt"*; Opa is dead | B7 T9 |
| Julia owns an old bicycle | B8 T4; B10 T12 |
| Bruckner says Sie to Julia and calls her *Julia*; he and Frau Wolf say Sie; Bruckner ↔ Neumann Sie | B4 T2; B6 T4; B8 T2 |

## New standing facts

- **Herr Lorenz brought his wife flowers** at the second doorbell in March Y4 (Text 3). Frau
  Wolf has not seen his new partner for weeks. Nothing is decided; the divorce thread
  stays open.
- **Jule is in love** since January Y4 and has told Julia, not Tobi (Text 4). Who it is
  stays open, and so does the gender.
- **Julia is a patient of Frau Roth** too. Tobi has not been to a check-up since his tooth
  was pulled in Y1 (Text 5).
- **Tobi can now cook one dish**: Oma Erna's vegetable soup (Text 6).
- **1 April Y4**: Tobi told Frau Wolf the lift worked (Text 7).
- **Julia was exempt from school sport for two years** (Text 8).
- **Gisela is a critical restaurant guest** who tips well (Text 9).
- **Oma Erna dances with Herr Rademacher**, a resident who was once a singer on the radio,
  at the Altenheim's spring party. She and Opa were poor when they were young (Text 10).
- **Neumann moved Frau Wolf's shoe rack** out of the stairwell; it now stands inside her
  door (Text 11).
- **Leon visits Bruckner less often now**, and the railway reaches the kitchen (Text 12).
- **Frau Wolf's birthday is a Saturday at the end of April.** Her age is not stated
  (Text 13).
- **Bruckner has never married** (*ledig*). He asks Frau Wolf to keep phoning him every
  morning, not only about the heating, which continues the phone thread of B7 T10 (Text 13).

## Calendar

| when | text |
|---|---|
| early March, a Sunday morning | 1. Tobi lost 4:0 on Saturday |
| March | 2. Neumann checks Bruckner's heating |
| March | 3. Herr Lorenz and the flowers |
| March | 4. Jule is in love |
| late March | 5. the dentist |
| late March | 6. Tobi's soup |
| 1 April | 7. April fool |
| a Sunday in April | 8. 7 a.m., Jule on the bike |
| April, a Sunday | 9. lunch with Gisela |
| April | 10. the Altenheim's spring party |
| April | 11. the shoe rack |
| late April, a weekday | 12. Bruckner's railway |
| the Saturday after, end of April | 13. Frau Wolf's birthday |

## Cast

| pair | form |
|---|---|
| Julia ↔ Tobi ↔ Jule | du |
| Frau Wolf → Julia | du, *Kind*; Julia → Frau Wolf: Sie |
| Frau Wolf → Tobi | Sie, *junger Mann*; *Kinder* / ihr to Julia and Tobi |
| Bruckner ↔ Julia | Sie; he says *Julia* |
| Bruckner ↔ Neumann, Bruckner ↔ Frau Wolf, Neumann ↔ everybody | Sie |
| Frau Roth ↔ Julia, Tobi (*Herr Wagner*) | Sie |
| Gisela ↔ Tobi | du, *Mama* |
| Gisela ↔ Kellner | Sie; she calls him *junger Mann* |
| Oma Erna ↔ Tobi | du, *Oma* |
| Julia → Oma Erna | Sie, *Frau Wagner*. Oma's form for Julia stays unstated (she only says *Julia*) |

New names: **Herr Rademacher** (Q–R, Text 10). The Kellner has no name.

---

### Scene 1 — Vier zu null

- **Premise:** Early March, a Sunday morning in Julia's flat. Tobi's team lost 4:0
  yesterday, and he came home at two, singing in the stairwell.
- **Angle:** It was not the beer, it was the disappointment, and the 4:0 was bad luck,
  four times in a row. Called a terrible loser, his only defence is that he gets plenty
  of practice.
- **Words (10):** der Verlierer / die Verliererin, betrunken, blass, wirken, die Wirkung, die Laune, das Pech, die Enttäuschung, schrecklich, wütend
- **Chunks:** `ein(e) schlechte(r) Laune` (1795), `Laune(Akk.) haben` (2120), *"Du siehst
  ganz blass aus"* (CSV), *"Wenn Sie betrunken Auto fahren"* (CSV), *"Die Tabletten haben
  nicht gewirkt"* (CSV), *"Sie ist eine gute Verliererin"* (CSV), *"Warum bist du so wütend?"* (CSV)
- **Deliberately absent:** `ärgern` (9), `traurig` (10), `Lust` (8), `Glück` (13)

### Scene 2 — Die Katze ist ganz lieb

- **Premise:** March. Neumann has to check the heating in Bruckner's flat, and the cat is
  in front of the radiator.
- **Angle:** *"Die ist ganz lieb"* is the line before every bite. The man of rules is
  afraid of a cat and calls it *Respekt*. Then the cat lies down on his list.
- **Words (9):** lieb, beißen, der Schreck, ängstlich, die Angst, ruhig, frech, das Vertrauen, eilen
- **Chunks:** *"Pass auf, dass dich der Hund nicht beißt!"* (CSV), `Schreck(Akk.)
  bekommen` (133), *"Es eilt sehr"* (CSV), *"Ich habe Vertrauen zu Ihnen"* (CSV)
- **Deliberately absent:** `fürchten` (5)

### Scene 3 — Blumen an der zweiten Klingel

- **Premise:** March, the fourth floor. Frau Wolf calls Julia over: Herr Lorenz just rang
  his own wife's doorbell, with flowers.
- **Angle:** Frau Wolf is not curious, she is *interested*. Julia is not interested at
  all, and her last line asks whether the wife took the flowers.
- **Words (7):** neugierig, interessiert, interessieren, sympathisch, höflich, still, die Hoffnung
- **Chunks:** *"Die Nachbarn sind ziemlich neugierig"* (CSV), *"Unser Nachbar ist sehr
  höflich. Er sagt immer als Erster Guten Tag"* (CSV), *"Sind Sie noch an der Wohnung
  interessiert?"* (CSV)

### Scene 4 — Jule singt

- **Premise:** March, Julia's kitchen. Jule has been singing for an hour.
- **Angle:** Jule trusts Julia with it and not her brother. Tobi walks in, and his
  questions prove her right.
- **Words (7):** vergnügt, verliebt, sich verlieben, die Liebe, lieben, vertrauen, ernst
- **Chunks:** *"Ich bin in Francesco verliebt"* (CSV), *"Ich habe mich verliebt"* (CSV),
  *"Ich vertraue dir"* (CSV), *"Er kam mit einem vergnügten Grinsen herein"* (CSV)

### Scene 5 — Bei Frau Roth

- **Premise:** Late March, the dentist's waiting room. Julia has a check-up, Tobi came
  along to show her how calm he is.
- **Angle:** Julia is afraid and fine. Tobi is calm until Frau Roth notices he has not
  been back since the tooth.
- **Words (7):** (sich) fürchten, bereit, hoffentlich, erleichtern, froh, fühlen, leider
- **Chunks:** *"Sie fürchtet sich vor Schlangen"* (CSV), *"Ich bin erleichtert, dass alles so
  gut geklappt hat"* (CSV), *"Wie fühlen Sie sich?"* (CSV)
- **Deliberately absent:** `Angst` (2)

### Scene 6 — Gemüsesuppe

- **Premise:** Late March. Tobi cooks, and nothing is burnt.
- **Angle:** Julia's praise, *"Das ist ja ein Wunder"*, is an insult. Frau Wolf smells
  the soup in her hall and is just as surprised. Tobi is proud anyway.
- **Words (9):** stolz, loben, das Wunder, sich wundern, wunderbar, kreativ, beleidigen, leicht, sich eignen
- **Chunks:** *"Ich bin stolz auf dich"* (CSV), *"Diese Schokolade schmeckt wunderbar"*
  (CSV), *"Ich wollte Sie nicht beleidigen"* (CSV), *"Dieses Hotel eignet sich besonders für
  Familien"* (CSV)

### Scene 7 — Der erste April

- **Premise:** 1 April, the stairwell. Tobi tells Frau Wolf the lift works again.
- **Angle:** She is thrilled, presses the button ten times, and then collects: Tobi
  carries her shopping up four floors.
- **Words (7):** sich freuen, begeistert, verrückt, lustig, enttäuschen, ernsthaft, böse
- **Chunks:** *"Bist du verrückt geworden?!"* (CSV), *"Hoffentlich bist du mir nicht
  böse"* (CSV), *"Leider hat mich sein Verhalten enttäuscht"* (CSV)
- **Note:** the lift stays broken. Only Batch 23 may repair it.

### Scene 8 — Sonntag, sieben Uhr

- **Premise:** A Sunday in April, 7 a.m. Jule is downstairs with her bike and wants to
  ride to Kessler for eggs.
- **Angle:** The active one against two lazy ones. Every excuse is a target word, and
  the lazy ones still get the eggs.
- **Words (12):** wach, die Bewegung, hassen, frieren, faul, befreit, geeignet, aktiv, sich lohnen, faulenzen, entspannend, die Lust
- **Chunks:** *"Bist du schon lange wach?"* (CSV), *"Sie brauchen mehr Bewegung"* (CSV),
  *"Am Wochenende können wir faulenzen"* (CSV), `Lust + auf Frühstück` (50)

### Scene 9 — Eine Drei für die Suppe

- **Premise:** April, a restaurant. Tobi has lunch with his mother.
- **Angle:** Gisela calls it being *kritisch*, and her husband loves her for it. She grades
  the soup like a school report and tips the waiter generously.
- **Words (10):** der Kellner / die Kellnerin, (sich) ärgern, eilig, ärgerlich, die Kritik, peinlich, kritisieren, kritisch, befriedigend, angenehm
- **Chunks:** `ein(e) peinliche(r) Situation` (210), *"Kritisiere mich nicht so oft"* (CSV),
  *"Hast du es eilig?"* (CSV), *"Das ist wirklich ärgerlich"* (CSV)

### Scene 10 — Frühlingsfest

- **Premise:** April, the Altenheim. Tobi and Julia visit Oma Erna, who has no time for
  them.
- **Angle:** A reversal of Batch 7, Text 9. Oma complained that nobody visits, and now she
  is dancing with Herr Rademacher and sends them away.
- **Words (9):** sich vergnügen, fröhlich, gefallen, berühmt, traurig, arm, das Vergnügen, klasse, die Eile
- **Chunks:** *"Auf der Party habe ich mich sehr vergnügt"* (CSV), *"Wie gefällt es Ihnen
  hier?"* (CSV), *"Ich finde unseren Lehrer klasse"* (CSV), *"Ich bin sehr in Eile"* (CSV)

### Scene 11 — Das Schuhregal

- **Premise:** April, the stairwell. Neumann has moved Frau Wolf's shoe rack to the cellar.
- **Angle:** Fire safety against years of habit. Julia finds the compromise (the rack
  goes inside Frau Wolf's door), and Neumann fetches it from the cellar himself.
- **Words (8):** dringend, begrenzt, dumm, sich etwas gefallen lassen, beruhigen, aufregen, der Ärger, der Friede
- **Chunks:** *"Ich muss dich dringend sprechen"* (CSV), *"Das würde ich mir nicht gefallen
  lassen"* (CSV), *"Beruhigen Sie sich bitte"* (CSV), *"Endlich ist hier Frieden!"* (CSV)
- **Deliberately absent:** `wütend` (1), `Ruhe` (12)

### Scene 12 — Bis in die Küche

- **Premise:** Late April. Julia brings Bruckner leftover cake; the railway now runs into
  his kitchen.
- **Angle:** He says he likes being alone. When she invites him to Frau Wolf's birthday,
  he writes it into his timetable straight away.
- **Words (8):** interessant, das Interesse, allein, die Ruhe, schade, einsam, hoffen, gemütlich
- **Chunks:** `in lassen … Ruhe` (10321), *"Ich habe viele Interessen"* (CSV), *"Ohne meine
  Familie fühle ich mich ein bisschen einsam"* (CSV), *"Es ist sehr gemütlich bei dir"* (CSV)

### Scene 13 — Ich habe Ohren

- **Premise:** The Saturday after, Frau Wolf's birthday. Julia, Tobi and Bruckner arrive
  for the surprise.
- **Angle:** No surprise is possible next to Frau Wolf (*"Ich habe Ohren, Kind"*): the table is already laid.
  Bruckner gives a formal speech in her kitchen, and his wish is to keep receiving the
  phone calls.
- **Words (12):** herzlich, willkommen, gespannt, wunderschön, geehrt, (sich) wünschen, das Glück, der Wunsch, ledig, dankbar, die Freude, glücklich
- **Chunks:** *"Herzlich willkommen in Köln"* (CSV), *"Sehr geehrte Damen und Herren"* (CSV),
  *"Ich wünsche Ihnen alles Gute"* (CSV), *"Ich bin Ihnen sehr dankbar für Ihre Hilfe"* (CSV)

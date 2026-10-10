# Batch 14 — Arbeit & Beruf · Szenenplan

137 target words in **fourteen scenes** of six to fifteen words each. The story slot is
November of Y3. This batch owns **Julia's job and Tobi's job**, so the first four scenes
establish them at work. Tobi is a mechanic in the university's workshop (Texts 1, 4, 13).
Julia works at a small Verlag (Texts 2, 3, 10, 12). The rest of the house appears through its
jobs: Jule's weekend job (5), Frau Wolf's old one (6), retired Bruckner (7), Jan Sattler's
power station (8), Frau Lorenz's first application in fifteen years (9) and Kai's start-up (11).
The batch ends with an open question. Tobi is offered the workshop, and he has not said yes.

The topic's hazard is the **careers fair**: a list of professions recited for their own
sake. Here each profession noun belongs to a person and comes with a reason. The other
waitress is "eigentlich Schauspielerin" (5). Frau Lorenz used to be a Stewardess (9). The
candidate is an Architektin whose Diplom is not recognised (10). Tobi wanted to be a
Profisportler at sixteen and a Sänger at eighteen, and Julia has heard him in the shower (14).
That one two-item list is the only place where professions are listed.

Julia's Verlag is working on a book of reportage about work. It runs through the batch as
a light frame: its reporter quits in Text 3, Julia interviews Frau Wolf for it in Text 6,
and the candidate is asked about it in Text 10. It is never the point of a scene.

## Sense decisions made against the CSV, not against the corpus

- **`das Fach` is a compartment** (CSV sense 1, *"im obersten Fach links"*). Text 12: the
  office fridge. It is never a school subject, because Batch 15 owns studies.
- **`die Führung` is a guided tour** (CSV sense 1, *"Die nächste Führung beginnt um 15
  Uhr"*). Text 11: Kai's tour of the manufacturer's plant. It is not management, and that
  keeps it apart from `Leitung` (Text 13).
- **`die Leitung` is the management of a department** (CSV sense 1, *"übernimmt … die
  Leitung der Abteilung"*). Text 13. It is not a phone line or a pipe.
- **`der Leiter` is the head of the workshop.** It is never the ladder (`die Leiter`). Text 7
  keeps Bruckner off any ladder for this reason.
- **`der Meister` is the master craftsman** (CSV sense 1, *"Dann frag doch den Meister"*).
  Text 1: *"fragst du den Meister. Also mich."* In Text 13, *"den Meister machen"* is the
  same title as a qualification. It is not the champion.
- **`anstellen` is *angestellt sein*** (CSV sense 2). Text 7: *"Herr Bruckner ist hier nicht
  mehr angestellt"*. It is not "switch on" or "queue".
- **`das Werk` is a factory site** (*"das Werk besichtigt"*). Text 11. `das Kraftwerk`
  (Text 8) is its own word.
- **`der Mangel` is a defect** (CSV sense 2, *"technische Mängel"*). Text 4: *"Einen Mangel
  hat ihr Gerät nämlich nicht"*.
- **`die Werkstatt`** in the CSV is a car repair shop. Tobi's is a university workshop for
  lab equipment. Text 1 says so outright: *"Wir sind eine Werkstatt für Geräte, nicht für
  Kraftfahrzeuge."* That line also covers Batch 10: Tobi's car is a wreck, and Bruckner
  fixed his brakes.
- **`das Kraftfahrzeug`** is Tobi's deliberately official word in the line above. It is the
  only place it fits.
- **`der Täter` is office comedy, not crime.** It is the yoghurt thief in Text 12, because
  Batch 13 owns the police.
- **`die Weiterbildung`** is only offered (Text 13). Nobody attends one, because Batch 15
  owns courses.
- **`zugänglich`** is wheelchair access (*"für alle zugänglich"*, CSV). Text 10.
- **`handeln` is *handeln mit*** (CSV sense 1). Text 11: *"Ich handle mit Cafés und kleinen
  Händlern."*

## Synonym / near-pair check

Checked against the ledger after `scan --apply`.

| set | texts | ruling |
|---|:-:|---|
| `Experte` / `Spezialist` / `Fachmann` / `Fachleute` / `Profi` | 3 / 4 / 11 / 8 / 7 | **split five ways** |
| `Lohn` / `Gehalt` | 5 / 2 | **split.** Jule has a wage and Julia a salary |
| `Firma` / `Betrieb` | 7 / 11 | **split.** The ledger's `Betrieb` row for Text 8 comes from a prefix match on *Betriebsrat* |
| `Werk` / `Fabrik` | 11 / 6 | **split** |
| `Arbeitsplatz` / `Arbeitsstelle` | 2 / 9 | **split** |
| `Mitarbeiter` / `Angestellte` / `Arbeiter` | 13 / 6 / 8 | **split** |
| `Leiter` / `Direktor` | 13–14 / 6 | **split.** Text 14 avoids *Direktor* |
| `Leitung` / `Führung` | 13 / 11 | **split**, and in different senses anyway |
| `Student` / `Studierende` | 5 / 4 | **split.** The professor says *Studierende*. Jule calls herself *Studentin* |
| `teilnehmen` / `sich beteiligen` | 12 / 8 | **split** |
| `Handwerker` / `Mechaniker` | 7 / 1 | **split** |
| `kündigen`+`Kündigung` / `entlassen`+`Entlassung` | 3 / 8 | **split.** The reporter quits and the power station dismisses |
| `Profi` / `Profisportler` | 7 / 14 | **split** |
| `Förderung` / `Unterstützung` | 13 / 14 | **split** |
| `Beruf` / `Tätigkeit` | 6 / 9 | **split** |

Derivational families left together, per the skill: `Reporter`/`Reportage`,
`kündigen`/`Kündigung` (3), `Hersteller` (4), `Migration`/`Migrantin` (10), `Arbeitslosigkeit`/`arbeitslos`,
`fordern`/`Forderung`, `entlassen`/`Entlassung` (8), `Unternehmer`, `Handel`/`handeln`/`Händler`,
`Erfolg`/`erfolgreich` (11), `Teilnahme`/`Teilnehmer`/`teilnehmen` (12),
`Leiter`/`Leitung`, `fördern`/`Förderung` (13), `unterstützen`/`Unterstützung` (14),
`Teilzeit`/`Vollzeit` (2, a contrast: *"Beim Gehalt ist es Teilzeit, beim Telefon
Vollzeit"*).

## Scanner artefacts: which text owns the card

The ledger records the first sighting, and its stem matching cross-credits several pairs.
The rows below were fixed with `vocab.py use`. The wrong scan rows come back on every
rescan, so ignore them. **Cut each card from the text named here:**

| word | scanner credits | real owner | why |
|---|:-:|:-:|---|
| `fehlen` | 1 (*Fehler*) | **12** | *"Mir fehlt seit Dienstag ein Stück Käse."* |
| `fördern` | 8 (*fordern*) | **13** | *"Die Uni fördert so was"*. The ledger's form column wrongly shows *fordern* |
| `die Förderung` | 8 (*Forderung*) | **13** | *"So eine Förderung bekommt nicht jeder."* Same ledger error |
| `anstellen` | 6 (*Angestellte*) | **7** | *"nicht mehr angestellt"* |
| `herstellen` | 4 (*Hersteller*) | **6** | *"Wir haben Schokolade hergestellt."* |
| `arbeiten` | 1 (*Arbeit*) | **2** | *"Du arbeitest doch Teilzeit."* |
| `gründen` | 3 (*Grund*) | 3 | *"vor zweiundzwanzig Jahren gegründet"* is in the same text |
| `leiten` | 6 | 6 | *"Offiziell hat er die Fabrik geleitet."* It is credited correctly |
| `handeln` | 11 (*Handel*) | 11 | *"Ich handle mit Cafés"* is in the same text |
| `teilnehmen` | 12 (*Teilnehmer*) | 12 | *"wollen nicht teilnehmen"* is in the same text |

The scanner does not credit female forms that the CSV lacks. That is why Text 3 says
*Experte* (Frau Wolf's *Expertin* in Text 6 is not counted) and Text 10 says *Kandidaten*.

## Continuity

Checked against continuity.md (Batches 1–10) and slots.md.

| established fact | source | how this batch uses it |
|---|---|---|
| Tobi has a **male** Chef and a Besprechung at nine | B3 T10 | Herr Kaminski, the Meister. The Monday Besprechung is at nine (T1) |
| Tobi's jacket hangs *"in der Uni"*, and he eats in the Mensa | B5 T7; B3 T11 | He works in the Uni's Werkstatt |
| Tobi's *"Nicht privat"* cigarette, said at a private Kneipe evening | B3 T10 | He smokes with his Chef on breaks, and privately only when he is talking about him: *"Privat höchstens, wenn ich über Sie rede"* (T13). The B3 evening was spent partly on *"deinen Chef"* |
| Tobi's car is a wreck, and Bruckner fixed his brakes | B10 T5 | *"Als Mechaniker für Autos bin ich sowieso der Falsche"* (T1) |
| Tobi was away all summer in Y2 | B4 T1 | No hire date and no length of service are given for Tobi |
| Julia's nervous job interview in autumn Y1 | B2 T11 | It was for this Verlag: *"Mein letztes Vorstellungsgespräch war mein eigenes, vor zwei Jahren"* (T10) |
| Julia works at home on a computer | B8 T1 | Two days a week at the kitchen table (T2) |
| Julia commutes to work by S-Bahn | B10 T1 | Her other days are in the Büro (T2). No weekdays are named |
| Frau Wolf hears everything through the wall | B4 T1, B7 T6, B9 T14 | T14 |
| Frau Wolf's chocolate habit | B2 T9, B3 T8 | She worked in a chocolate factory (T6) |
| Frau Wolf → Julia du + *Kind*, → Jule du + *Kind*, → Tobi Sie + *junger Mann* | slots.md; B5; B4 T1 | T5, T6, T14 |
| Bruckner was caretaker for 21 years, retired, and "nobody needs me" | B7 T10; B10 T5 | He fixes Frau Wolf's heating once, as a joke *selbstständiger* (T7). This answers Frau Wolf's *"wer repariert dann die Heizung"* (B7 T10) |
| The heating is off from 1 May | B9 T5 | On again in November, and dripping (T7) |
| Neumann says Sie to everyone and goes by the rules | B8 T2 | T7 |
| Jan & Anna Sattler, 2nd floor, baby born March Y3 | B7 T5, B9 T2 | T8 |
| The Lorenzes: 15-year relationship, separated since October Y2 | B7 T8 | *"einen Mann, der fünfzehn Jahre lang … seine Schlüssel gesucht hat"* (T9) |
| Kai, 36, eldest. Gisela is *Mama* | B7 T1 | T11 |
| Café gegenüber | B3 T8 | Jule waits tables there (T5) |
| Julia's birthday is a late-November Saturday | B7 T6 | Not touched. T5's Saturday falls early in the month |

**New standing facts**

- **Tobi is a Mechaniker in the Werkstatt der Uni.** The workshop repairs and builds
  equipment for the professors, not cars. His Chef is **Herr Kaminski**, the Meister and
  Leiter of the workshop. Kaminski says du to Tobi, and Tobi says *Chef* and Sie. The
  Besprechung is every Monday at nine. **Finn** is the Praktikant (Herr Kaminski / du). **Professorin
  Imhof** is the client whose equipment keeps "breaking": she presses the red button. She says
  *Herr Wagner* and Sie.
- **Kaminski retires in the summer of Y4** after 31 years. He has proposed Tobi as the next
  Leiter. That would require the Meister-Weiterbildung: evenings, two years, half paid by
  the Uni. **Tobi has not decided** (T13–14). Julia and Frau Wolf back him. Batch 15 owns
  whether he enrols.
- **Julia works Teilzeit (30 hours) at a small Verlag**: two days at home, the rest in the
  Büro. She has been there two years, since the interview in B2 T11. Her Chefin is **Frau Lindner**, who
  founded the Verlag 22 years ago with a table and a telephone. Lindner says Sie +
  *Julia*, and Julia says Sie. Her colleague **Ines** is du with Julia, and Lindner says Sie to her. Julia
  does unpaid overtime on the phone with authors.
- **Julia is now in charge of the Verlag's book project** of reportage about work (professions across three
  generations, T6; a chapter on migration, T10; the reportage was due in March, T3). The reporter quit
  by e-mail and is going to Australia (T3). There are six steps at the Verlag's entrance
  (T10).
- **Jule works as an Aushilfe in the Café gegenüber at weekends, since October.** Her
  colleague **Mira** is an actress (mentioned only).
- **Frau Wolf was a Sekretärin for almost forty years** to the Direktor of a chocolate
  factory, and by her own account she ran it.
- **Bruckner's "selbstständig" is a one-off joke, not a standing arrangement.** He fixes
  Frau Wolf's heating once, "seit heute", and is paid in cake. Batch 19 owns his retirement
  year and is free to use it or drop it.
- **Jan Sattler is an Ingenieur at the Kraftwerk and sits on the Betriebsrat.** The
  Kraftwerk closes in two years. 200 workers are at risk, and there is a strike on a Friday
  in November. **Julia and Jan say du.**
- **Frau Lorenz was a Stewardess before her marriage.** She is applying for a job at the
  airport, her first application in fifteen years. **Julia and Frau Lorenz say Sie.**
- **Kai is an Unternehmer**: he imports Italian coffee machines. His firm is a garage, a
  laptop and Gisela on the phone. His first customer is Mama. Tobi repaired the machine that went back to Italy.
- **The Verlag's yoghurt thief was Frau Lindner.** She joins Ines's Wichteln, so there are
  three participants.
- **Frau Ilić**, an Architektin from Belgrade, interviewed for an internship at the Verlag.
  She has a work permit, and her diploma is not yet recognised. The outcome is open.
- **Tobi wanted to be a Profisportler at sixteen**, and his club did not put him in the
  first team. **He wanted to be a Sänger at eighteen** (T14).

## Calendar (November, Y3)

| when | text |
|---|---|
| first Monday, 9:10 | 1. Besprechung in the Werkstatt |
| same Monday, 10:00 | 4. the Imhof appointment set in T1 (text order follows the words, not the clock) |
| first week, evening | 2. Julia's kitchen table |
| first week | 3. the reporter quits |
| first Saturday | 5. Jule at the café |
| second week | 6. Frau Wolf's interview |
| second week | 7. the dripping heating |
| second week | 8. Jan in the courtyard; strike on the Friday |
| third week | 9. Frau Lorenz's application |
| third week | 10. Frau Ilić's interview |
| third Sunday | 11. Kai at the Wagners' |
| last week | 12. the office fridge |
| last week, a weekday | 13. the cigarette with Kaminski |
| same evening | 14. through the wall |

## Cast and address forms

| pair | form |
|---|---|
| Kaminski → Tobi, Finn | du; Tobi → Kaminski: Sie, *Chef*; Finn → Kaminski: Sie, *Herr Kaminski* |
| Imhof ↔ Tobi | Sie (*Herr Wagner*, *Frau Imhof*) |
| Lindner → Julia, Ines | Sie + first name; both → Lindner: Sie |
| Julia ↔ Ines | du |
| Julia/Lindner ↔ Frau Ilić | Sie |
| Jule → Frau Wolf | Sie; Frau Wolf → Jule: du, *Kind* |
| Neumann ↔ Bruckner, Frau Wolf | Sie |
| Julia ↔ Jan Sattler | du (new) |
| Julia ↔ Frau Lorenz | Sie (new) |
| Julia ↔ Kai ↔ Tobi | du |
| Frau Wolf → Tobi | Sie, *junger Mann* |

---

### Scene 1 — Die Besprechung um neun

- **Premise:** The first Monday of November, 9:10, the Uni workshop. Tobi is late for
  Kaminski's Besprechung.
- **Angle:** Tobi is the Mechaniker whose own car is fixed by a pensioner. The professor's
  "broken" equipment is the professor herself. Finn, the over-eager intern, sorted all the
  tools by colour.
- **Words (15):** die Arbeit, die Werkstatt, der Auftrag, der Professor, der Termin, reparieren, der Fehler, das Kraftfahrzeug, der Mechaniker, das Werkzeug, der Praktikant, fleißig, erledigen, der Meister, (arbeiten, see artefacts)
- **Chunks:** `Arbeit(Akk.) erledigen` (1724), *"Dann frag doch den Meister"* (CSV),
  *"Wir hatten kein Werkzeug für die Reparatur dabei"* (CSV), *"Auf dieser Straße sind
  Kraftfahrzeuge nicht erlaubt"* (CSV, register model)

### Scene 2 — Ein Küchentisch ist kein Büro

- **Premise:** A weekday evening, Julia's kitchen. Tobi arrives with pizza. Julia is on
  the phone with her Chefin.
- **Angle:** She is part-time on her pay and full-time on the phone. The kitchen table is a
  workplace two days a week, so Tobi and his pizza get it the other days.
- **Words (14):** der Feierabend, telefonieren, das Telefon, der Verlag, arbeiten, die Teilzeit, die Vollzeit, das Gehalt, die Überstunde, der Terminkalender, anstrengend, beenden, der Arbeitsplatz, das Büro
- **Chunks:** *"Ich arbeite im Moment nur Teilzeit"* (CSV), *"Ich muss heute Überstunden
  machen"* (CSV)

### Scene 3 — Eine Gelegenheit

- **Premise:** The Verlag's office. Frau Lindner calls Julia and Ines in. The reporter
  quit at 3 a.m. by e-mail.
- **Angle:** The Chefin calls everything an opportunity. Ines congratulates Julia, meaning the
  opposite. Julia wants to read the resignation first, in case he knew something.
- **Words (10):** der Reporter, kündigen, die Reportage, der Grund, das Projekt, zuständig, der Experte, gründen, die Gelegenheit, die Kündigung
- **Chunks:** *"Aus welchem Grund?"* (CSV, after *gekündigt*), *"Das Fest ist eine gute
  Gelegenheit"* (CSV), *"Wer ist dafür zuständig?"* (CSV)

### Scene 4 — Der Spezialist kommt im März

- **Premise:** The same Monday at ten, Professorin Imhof's lab. The equipment is dead and
  the manufacturer's specialist can come in March.
- **Angle:** The plug was out. Tobi does not cancel the specialist; let him come in March and search.
- **Words (7):** die Studierenden, der Hersteller, der Spezialist, die Reparatur, der Mangel, nützen, der Zufall
- **Chunks:** *"Wir schicken es an den Hersteller zurück"* (CSV), *"Die Maschine hat
  technische Mängel"* (CSV), *"Es hat nichts genützt"* (CSV), *"Es war reiner Zufall"* (CSV)

### Scene 5 — Die Aushilfe

- **Premise:** A Saturday, the Café gegenüber. Jule is waiting tables. Frau Wolf and Julia
  come in.
- **Angle:** Frau Wolf is the hardest customer in the room. She checks the kitchen herself,
  then tips the change from ten euros.
- **Words (10):** die Kellnerin, die Aushilfe, die Studentin, verdienen, der Lohn, die Schauspielerin, das Personal, sich anstrengen, die Kundin, der Rest
- **Chunks:** *"Wir suchen eine freundliche Aushilfe"* (CSV), *"Dieser Eingang ist nur für
  das Personal"* (CSV), *"Den Rest gebe ich dir später"* (CSV)

### Scene 6 — Fast vierzig Jahre

- **Premise:** Julia interviews Frau Wolf for the book.
- **Angle:** Officially the Direktor ran the chocolate factory. Frau Wolf ran it, and that
  explains the chocolate. Her job title gets a footnote.
- **Words (12):** der Beruf, die Generation, berufstätig, die Sekretärin, die Fabrik, herstellen, der Direktor, leiten, (die Expertin), die Karriere, der Angestellte, die Industrie
- **Chunks:** *"In unserer Firma stellen wir Schokolade her"* (CSV), *"Wer leitet den
  Kurs?"* (CSV), *"Björn ist Angestellter"* (CSV)

### Scene 7 — Selbstständig

- **Premise:** Frau Wolf's flat. Her heating drips. Neumann catches Bruckner with his
  toolbox.
- **Angle:** Neumann's rule is that the Firma is responsible and a Handwerker will come in
  three weeks. Bruckner gets round it by declaring himself self-employed as of today. His
  fee is cake.
- **Words (8):** die Firma, zuständig, anstellen, der Handwerker, selbstständig, der Anspruch, der Profi, leisten
- **Chunks:** *"Wer ist dafür zuständig?"* (CSV), *"Früher war ich selbstständig"* (CSV),
  *"Er ist doch ein Profi"* (CSV), *"keinen Anspruch auf …"* (CSV)

### Scene 8 — Das Kraftwerk

- **Premise:** The courtyard. Jan Sattler looks wrecked. The baby is one reason, and the
  power station closing is the other.
- **Angle:** Jan's union speech ends at home. The toughest demands come at 3 a.m. from the
  cot.
- **Words (13):** das Kraftwerk, die Arbeitslosigkeit, der Ingenieur, die Fachleute, der Arbeiter, arbeitslos, der Betriebsrat, die Entlassung, fordern, entlassen, die Gewerkschaft, sich beteiligen, die Forderung
- **Chunks:** *"Die Arbeitnehmer fordern mehr Geld"* (CSV), *"Die Firma hat viele Mitarbeiter
  entlassen"* (CSV), *"Wer möchte sich beteiligen?"* (CSV, here *am Streik*)

### Scene 9 — Die erste Bewerbung seit fünfzehn Jahren

- **Premise:** Frau Lorenz (3rd floor) asks Julia for help with an application.
- **Angle:** Fifteen years of marriage become a CV line. Her ex-husband's lost keys become
  "Erfahrung mit schwierigen Kunden".
- **Words (8):** beruflich, die Bewerbung, die Unterlagen, die Stewardess, die Qualifikation, die Tätigkeit, sich bewerben, die Arbeitsstelle
- **Chunks:** *"Was machen Sie beruflich?"* (CSV), *"Ich schicke Ihnen alle Unterlagen"*
  (CSV), *"Welche Tätigkeit würde Ihnen Spaß machen?"* (CSV)

### Scene 10 — Auf der anderen Seite vom Tisch

- **Premise:** The Verlag. Julia conducts her first interview, for an internship. Lindner
  listens.
- **Angle:** It reverses B2 T11, with Julia's hands shaking on the other side of the table.
  The candidate is an architect. She refuses the "Migrantin" label in favour of her
  profession, then audits the building.
- **Words (10):** der Kandidat, das Vorstellungsgespräch, das Praktikum, die Architektin, die Arbeitserlaubnis, das Diplom, anerkennen, die Migration, die Migrantin, zugänglich
- **Chunks:** *"Meine Ausbildung wird hier nicht anerkannt"* (CSV), *"Der Park ist für
  alle zugänglich"* (CSV)

### Scene 11 — Import und Export

- **Premise:** Sunday at the Wagners'. Kai announces he is an Unternehmer.
- **Angle:** Kai's "Import und Export" is a garage, his mother is the first customer, and
  the first "export" was a return. Tobi did the repair for free.
- **Words (13):** der Unternehmer, der Import, der Export, der Betrieb, erfolgreich, das Werk, die Führung, handeln, der Händler, der Kunde, der Handel, der Fachmann, der Erfolg
- **Chunks:** *"Firma Schulz, Import und Export"* (CSV), *"Er handelt mit Obst und
  Gemüse"* (CSV), *"Sie ist erfolgreiche Unternehmerin"* (CSV), *"Wir haben gestern das
  Werk besichtigt"* (CSV)

### Scene 12 — Das Fach im Kühlschrank

- **Premise:** The Verlag kitchen. Ines's yoghurt is gone from her shelf. Her Wichteln
  sign has two names on it.
- **Angle:** The culprit is the Chefin, who confesses unprompted and joins the Wichteln as
  penance.
- **Words (7):** das Fach, fehlen, der Täter, die Teilnahme, der Teilnehmer, der Kollege, teilnehmen
- **Chunks:** *"Die Handtücher sind im obersten Fach"* (CSV), *"Die Teilnahme … ist
  kostenlos"* (CSV)

### Scene 13 — Eine Zigarette mit dem Chef

- **Premise:** Outside the workshop door. Kaminski takes Tobi out for a cigarette.
- **Angle:** This is the payoff of *"Nicht privat"*: Tobi smokes with his boss, and privately only when he talks about him.
  Kaminski is retiring, and he wants Tobi to take over.
- **Words (8):** der Leiter, der Mitarbeiter, die Weiterbildung, fördern, die Förderung, die Leitung, die Herausforderung, die Leistung
- **Chunks:** *"Ab 1. Juli übernimmt Herr Meier die Leitung"* (CSV), *"Für das Projekt
  bekommen wir eine Förderung"* (CSV), *"Das Spiel ist eine Herausforderung"* (CSV)

### Scene 14 — Durch die Wand

- **Premise:** The same evening, Julia's flat. Tobi doubts himself.
- **Angle:** His failed careers (football, then singing) are his case against himself.
  Julia backs him, and so does Frau Wolf through the wall, which settles it 2:0.
- **Words (7):** die Karriere, der Profisportler, der Verein, die Mannschaft, der Sänger, unterstützen, die Unterstützung
- **Chunks:** *"Mein Sohn möchte Profisportler werden"* (CSV), *"Ich nehme Ihre
  Unterstützung gern an"* (CSV)

## Still homeless

None. 137/137 are covered with no skips. Two female forms are absent from the CSV and
were avoided as card targets (*Expertin*, *Kandidatin*). A card cut from Text 6 or Text 10 for
those forms would not match the headword.

# Batch 15 — Schule & Bildung · Szenenplan

82 target words in **ten scenes** of five to twelve words each. One word is skipped
(`eintreten`, see below). The topic is learning at every age: Jule's university and her
first lessons as a teacher, Leon's primary school, a pupil's first Lebenslauf, a Lehrling
who fixes what the caretaker's Fortbildung could not, and a German course where Bruckner
helps out.

The topic's hazard is the **school-vocabulary parade**: *Lehrer, Schüler, Klasse,
Unterricht, Note, Prüfung* in one breath. Here each scene has one learner with something at
stake: Jule's Referat on sleep after two sleepless nights, Frau Wolf's hated new
Übersetzer, Leon's four lines that Frau Wolf knows eighty of, Leon teaching his tutor
patience, Amir writing a yellow door into a Lebenslauf.

## Sense decisions

- **`die Note` is a school grade** (CSV sense 1), never a musical note. Text 6.
- **`die Lehre` is an apprenticeship** (*"eine dreijährige Lehre"*, CSV). Text 5.
- **`aufgeben` is "to give up"** (CSV sense 2, *"Man darf nie aufgeben"*). The parcel sense
  belongs to post office scenes (Batch 18). Text 3.
- **`der Eintritt` is the admission fee** (*"Der Eintritt ist frei"*, CSV). Text 8.
- **`anwenden` is applying what one has learnt** (*das Gelernte anwenden*). The CSV example
  is an ointment, but the verb is the same. Neumann wants to apply his Fortbildung. Text 5.
- **`das Forum` is an Internetforum** (CSV), the online forum of Jule's seminar. Text 3.
- **`der Bereich`** is a field of work (CSV sense 1, *"In welchem Bereich möchten Sie
  arbeiten?"*). Text 9.
- **`das System`** is the new heating control Neumann learnt about (CSV sense 2, *"Ich kenne
  Ihr System nicht"*). Text 5.
- **`die Übung`** is practice, as in *mir fehlt die Übung* (CSV sense 2). Text 10.
- **`der Lerner / die Lernerin`** is the course teacher's word for her students. Text 7.

## Skipped

- **`eintreten`.** The CSV sense is joining a club (*"in einen Sportverein eingetreten"*).
  Clubs belong to Batch 16 (Freizeit), which runs in parallel and owns everyone's clubs. The
  literal "come in" sense would not be the list's sense.

## Synonym / near-pair check

| set | kind | texts | ruling |
|---|---|:-:|---|
| `das Referat` / `die Präsentation` | near-synonyms | 1 / 10 | **split** |
| `die Prüfung` / `die Klassenarbeit` | near-synonyms | 3 / 6 | **split** |
| `die Lehre` / `die Ausbildung` | near-synonyms | 5 / 9 | **split** |
| `der Unterricht` / `der Kurs` / `das Seminar` | teaching settings | 8 / 7 / 1 | **split** |
| `die Aufgabe` / `die Übung` / `die Hausaufgabe` | task words | 6 / 10 / 4 | **split** |
| `der Schüler` / `der Lerner` | learners | 8 / 7 | **split** |
| `der Lehrer` / `der Kursleiter` | teachers | 1 / 7 | **split** |
| `die Lehre` / `die Lehrstelle` | word and its compound | 5 / 9 | split anyway |
| `die Lehrstelle` / `die Ausbildung` | specific + superordinate | 9 / 9 | **left together on purpose**: Amir names the specific thing (*eine Lehrstelle*), Jule answers with the general one (*eine Ausbildung … auch mit Abitur*) |
| `das Kapitel` / `der Abschnitt` | chapter and a section inside it | 3 / 3 | **left together on purpose**: part and whole, not two names for one thing (*"im dritten Kapitel, zweiter Abschnitt"*) |
| `anwesend` / `abwesend` | antonyms | 7 / 7 | **left together on purpose**: a roll call needs both |
| `der Kurs` / `der Intensivkurs` | word and its compound | 7 / 7 | **left together on purpose**: the teacher names the course type once, then says *Kurs* |

Derivational families left together, per the skill: `erklären`/`die Erklärung` (6),
`die Aussprache`/`aussprechen` (7), `die Übersetzung`/`der Übersetzer`/`übersetzen` (2),
`die Präsentation`/`präsentieren` (10), `die Entwicklung` (1) and `entwickeln` (8) are
apart anyway. `die Forschung`/`das Institut` (1) are related but not synonyms.

## Scene order is ownership order

The scanner records a word at its first sighting, so the owner text comes first, or the
earlier texts avoid the word:

- **Text 1 owns `der Lehrer / die Lehrerin`** (Jule: *"Ich will mal Lehrerin werden"*). Later
  texts say *Lehrerin* and *Lehrer* freely.
- **Text 1 never says `Buch` or `lesen`** (Text 2), **`lernen` or `Prüfung`** (Text 3).
- **Texts 1–3 never say `Schule` or `Klasse`** (Text 4). **Texts 1–5 never say `Note`,
  `Aufgabe` or `erklären`** (Text 6). **Texts 1–6 never say `Kurs`** (Text 7). **Texts 1–7
  never say `Schüler` or `Unterricht`** (Text 8). **Texts 1–9 never say `Präsentation`**
  (Text 10).

Scanner artefacts, fixed by hand after `scan --apply`:

- **`buchen`** is credited by *Buch* in Text 2 (folded stem). The scan row for `buchen` at
  Text 2 comes back on every rescan and is removed with `vocab.py unuse --batch 15 buchen`
  followed by `vocab.py use --batch 15 --text 8 buchen`. Its card is cut from Text 8:
  *"Ich habe den Besuch schon gebucht."*
- **`der Kursleiter / die Kursleiter`**: the ledger's headword has a typo (feminine
  *Kursleiter*), so *Kursleiterin* is not matched. Recorded with `use --text 7`. Card line:
  *"Ich bin Frau Martens, Ihre Kursleiterin."*
- **`aussprechen`**, **`abschreiben`**, **`aufgeben`**, **`fortsetzen`** are matched as
  split verbs (*sprechen … aus*, *schreib … ab*, *gebe auf*, *setzen … fort*), which is
  correct.

## Continuity

### Facts this batch touches

| fact | source |
|---|---|
| Jule is Tobi's younger sister and a student; she has a *Kurs*; she eats in the Mensa | B3 T11, B7 T7, B3 hdr |
| Jule supervised a class trip with **Herr Krämer** (he says du, she says Sie) and stayed in the same hostel at 13. **Amir** (13 then) was on that trip; Jule and Amir say du; Amir left Izmir at four and remembers the sea and a yellow door | B7 T11 |
| Jule loves nature; buys eggs from Kessler's farm | B9 T8, B4 T3 |
| Tobi's elder brother is **Kai** | B7 T1 |
| Tobi's surname is **Wagner**, so Jule's is too | B2 T5, B9 T7 |
| **Leon** lives on the first floor and goes to school; says Sie to adults; Frau Wolf says du and *mein Junge* | B7 T4, B9 T6 |
| Bruckner's model railway with a timetable; Leon unplugged it; departure 15:10 | B10 T9 |
| Bruckner is retired since January Y3; Frau Wolf phones him about the heating | B7 T10 |
| **Neumann** is the caretaker; Sie to everyone; heating is **oil**, switched off in May | B8 T2, B9 T5 |
| Frau Wolf says du + *Kind* to Julia, Sie + *junger Mann* to young men; Julia says Sie | B4 T1, B10 T2 |
| Frau Wolf hears everything through the wall; Julia lives on the 4th floor, no lift | B1 T1, B9 T14 |

### New standing facts

- **Jule studies Biologie and wants to become a teacher** (Text 1). Her second subject is
  left open. She has a Seminar with a Referat in December and a **Prüfung in February**
  (Texts 1, 3).
- **Herr Krämer was Jule's own teacher** (T8 *"Er war mein Lehrer, hier in diesem Raum"*; the
  texts.md header calls him her *Biologielehrer*) at the school where he still teaches
  (Text 8). From January Jule teaches in his class **every Tuesday** as a Praktikum. The
  pupils call her **Frau Wagner** (Text 8). In February the class visits a farm whose
  farmer "knows" Jule (Kessler is implied, not named) to see chicks hatch from eggs.
- **Amir** is in Herr Krämer's class and wants to work with cars. He writes a Lebenslauf for
  a pupils' Praktikum in a car workshop and plans a Lehrstelle after the Abschluss; Krämer
  wants him to do the Abitur (Text 9).
- **Jule gives Leon paid Nachhilfe** (his mother pays) before a Klassenarbeit; Leon and
  Jule say **du** (Text 6). Leon solves a sum with Bruckner's 15:10 train. Leon's teacher is a woman (*meine Lehrerin*, Text 4), unnamed.
- **Leon says four lines of a Christmas poem at his school's Weihnachtsfeier.** Frau Wolf
  learnt the whole poem at school and accepts his half-invitation to say the rest (Text 4).
- **Frau Wolf has read crime novels for fifty years**; her translated series has a new
  translator with the latest volume. She bought Julia a copy for Christmas (Text 2).
- **Neumann attended a Fortbildung on heating systems** in December. In early January the
  heating fails because **the oil tank is empty**; the Heizungsfirma's **Lehrling** (one
  year left of his Lehre) sees it at once (Text 5). Frau Wolf's flat was at 14 °C.
- **Bruckner helps as a volunteer in a German Intensivkurs** for adults, three weeks in
  January, led by **Frau Martens** (new). Frau Wolf signed him up as a helper (Text 10:
  *"ich habe Sie hier zum Helfen angemeldet"*). The course ends with an interkulturelles Fest and continues in March; both he
  and Frau Wolf sign up for the next one (Text 10).
- New minor characters: **Frau Martens** (Kursleiterin), **Herr Moreno** (a learner in the
  course; his country is not stated), **Frau Malik** (an absent learner, named only), a
  nameless **Lehrling**.

### Address forms (new pairs marked *)

| pair | form |
|---|---|
| Jule ↔ Julia ↔ Tobi | du |
| Herr Krämer → Jule | du ("Jule") in private; in front of the class he says *Frau Wagner* |
| Jule → Herr Krämer | Sie |
| * Amir → Jule | in Text 8 he calls out *Jule* and she asks for *Frau Wagner* in class (he does not address her directly afterwards); in Text 9, after class, du + *Jule* |
| * Herr Krämer → Amir | du; Amir → Krämer: Sie |
| * Jule ↔ Leon | du / du (a student tutor; Leon still says Sie to the older adults) |
| Frau Wolf → Leon | du, *mein Junge*; Leon → Frau Wolf: Sie |
| Frau Wolf → Julia | du, *Kind*; Julia → Frau Wolf: Sie |
| * Neumann ↔ Lehrling | Sie / Sie |
| * Frau Wolf → Lehrling | Sie, *junger Mann* |
| * Frau Martens ↔ Bruckner, Frau Wolf, Herr Moreno | Sie |
| Frau Wolf ↔ Bruckner | Sie |

### Calendar (December Y3 – January Y4)

| when | text |
|---|---|
| early December, evening before the Seminar | 1. Jule rehearses her Referat at Julia's |
| first Saturday in December | 2. Buchhandlung, Christmas shopping |
| mid-December | 3. Uni-Bibliothek, before the Christmas break |
| a few days before Christmas | 4. Leon's poem for the Weihnachtsfeier |
| first Monday in January | 5. the heating and the Lehrling |
| first week of January | 6. Nachhilfe before Leon's Klassenarbeit |
| second Monday in January | 7. first morning of the Intensivkurs |
| the next day, a Tuesday | 8. Jule's first lesson in Krämer's class |
| a week later | 9. Amir's Lebenslauf |
| last Friday in January | 10. the course's last day, the Fest |

## Cast

Same house. **Julia**, **Tobi**, **Jule**, **Frau Wolf**, **Herr Bruckner** (retired),
**Herr Neumann** (caretaker), **Leon** (first floor). Back from Batch 7: **Herr Krämer** and
**Amir**. New: **Frau Martens**, **Herr Moreno**, a **Lehrling** of the heating firm.

---

### Scene 1 — Acht Stunden Schlaf

- **Premise:** Early December, evening, Julia's flat. Jule rehearses tomorrow's Referat for
  her Biologie Seminar in front of Julia and Tobi.
- **Angle:** The Referat proves that sleep makes students better, and Jule hasn't slept for
  two nights to finish it. Tobi falls asleep halfway, and he calls it science.
- **Words (12):** die Universität, das Seminar, das Referat, die Biologie, die Forschung, das Institut, das Ergebnis, die Abbildung, die Entwicklung, analysieren, beginnen, der Lehrer / die Lehrerin
- **Chunks:** `Referat(Akk.) halten` (191), *"Genug Schlaf ist wichtig für die Entwicklung"* (CSV), *"Auf der Abbildung sehen Sie …"* (CSV)
- **Deliberately absent:** `Buch`, `lesen` (2), `lernen`, `Prüfung` (3), `Schule` (4)

### Scene 2 — Fortsetzung folgt

- **Premise:** First Saturday in December, the Buchhandlung. Frau Wolf and Julia are buying
  Christmas presents.
- **Angle:** Frau Wolf has waited a year for the next volume of her crime series. A new
  Übersetzer ruins the Stil on page one. She buys it anyway, and a second copy for Julia, so
  she has someone to complain to.
- **Words (9):** die Buchhandlung, das Buch, der Leser / die Leserin, lesen, die Fortsetzung, die Übersetzung, der Übersetzer, übersetzen, der Stil
- **Chunks:** `Buch(Akk.) lesen` (5511), `Buch(Akk.) schenken` (190), *"Fortsetzung folgt"* (CSV), `ein(e) deutsche(r) Übersetzung` (36)

### Scene 3 — Pst!

- **Premise:** Mid-December, the Uni-Bibliothek. Tobi brings Jule biscuits, which are not
  allowed.
- **Angle:** Tobi whispers louder than he talks. Jule has read one Abschnitt ten times and
  wants to quit. Tobi's advice comes from copying Kai's old exercise books, and it fails.
  What works is a name: he asks about "Lisa from her course" and Jule is suddenly very busy
  studying.
- **Words (8):** die Bibliothek, das Kapitel, der Abschnitt, die Prüfung, lernen, abschreiben, das Forum, aufgeben
- **Chunks:** `für lernen … Prüfung` (246), `in Bibliothek lernen` (55), *"Lesen Sie bitte den zweiten Abschnitt"* (CSV), *"Er hat die Hausaufgaben von mir abgeschrieben"* (CSV), *"Man darf nie aufgeben"* (CSV)
- **Note:** the Lisa thread from B7 T7 is only touched, never resolved. The word *Kurs* is avoided (Text 7).

### Scene 4 — Vier Zeilen

- **Premise:** A few days before Christmas, the stairwell / Frau Wolf's door. Leon has to
  learn a Christmas poem for the Weihnachtsfeier.
- **Angle:** Leon needs four lines. Frau Wolf learnt all of it in her school days and
  recites far past the four. Leon invites her to the Feier to say the rest herself; she says
  yes before he has finished asking.
- **Words (5):** das Gedicht, die Hausaufgabe, die Schule, die Klasse, der Beginn
- **Chunks:** `Gedicht(Akk.) lernen` (62), *"Zu Beginn der Stunde …"* (CSV), *"vor der ganzen Klasse"*

### Scene 5 — Der Lehrling

- **Premise:** The first Monday in January, the cellar, the heating is dead. Neumann is
  back from a Fortbildung; the firm sends a Lehrling. Frau Wolf comes down in her coat.
- **Angle:** Neumann knows everything in theory and wants to check everything step by
  step. The Lehrling sees at once that the oil tank is empty. Frau Wolf invites the boy up
  for cake.
- **Words (8):** die Fortbildung, ausgebildet, die Lehre, der Lehrling, anwenden, theoretisch, prüfen, das System
- **Chunks:** *"Mein Cousin will eine dreijährige Lehre machen"* (CSV), *"Für diesen Beruf müssen Sie gut ausgebildet sein"* (CSV), *"Ich kenne Ihr System nicht"* (CSV)
- **Deliberately absent:** `Ausbildung` (9)

### Scene 6 — Nachhilfe

- **Premise:** First week of January, the Brandts' kitchen table. Jule gives Leon Nachhilfe
  in Mathe before his Klassenarbeit.
- **Angle:** Jule's explanations get longer and louder. Leon solves the task with
  Bruckner's train timetable and tells his future teacher to be more patient.
- **Words (9):** die Nachhilfe, die Klassenarbeit, die Note, die Aufgabe, erklären, die Erklärung, die Geduld, das Beispiel, der Bleistift
- **Chunks:** `Nachhilfe(Akk.) geben` (566), `Geduld(Akk.) verlieren` (568), `ein(e) gute(r) Note` (1803), *"Die Erklärung der Lehrerin ist besser als die Erklärung im Buch"* (CSV)

### Scene 7 — Ohne Pünktchen

- **Premise:** The second Monday in January, 9 a.m., a German Intensivkurs for adults.
  Frau Martens is the teacher; Bruckner is her new volunteer helper; Herr Moreno is a learner.
- **Angle:** Frau Martens practises the Ü, so the learner turns "Bruckner" into "Brückner".
  Bruckner insists: no dots, all his life, and spells it out. Herr Moreno gets it via *Brücke*.
- **Words (10):** der Kurs, der Intensivkurs, der Kursleiter / die Kursleiter, anwesend, abwesend, das Alphabet, aussprechen, die Aussprache, der Lerner / die Lernerin, international
- **Chunks:** *"Der Intensivkurs findet täglich von 9 bis 12 Uhr statt"* (CSV), *"Wie spricht man dieses Wort aus?"* (CSV), *"Die Teilnehmenden in unserem Kurs sind ganz international"* (CSV)
- **Note:** a German course for adults, so every line stays German.

### Scene 8 — Frau Wagner

- **Premise:** The next day, Tuesday, 8 a.m., Herr Krämer's class. Jule's first lesson.
- **Angle:** Krämer introduces "Frau Wagner"; Amir shouts "Jule!". Krämer was Jule's own
  teacher, and she still says Sie to him. The lesson is about how a chick develops
  in the egg, and the class wants to know only about the trip.
- **Words (7):** unterrichten, der Unterricht, der Schüler / die Schülerin, entwickeln, besichtigen, buchen, der Eintritt
- **Chunks:** `Unterricht beginnen(t)` (198), `in Unterricht schlafen` (54), *"Der Eintritt ist frei"* (CSV), *"Im Urlaub haben wir Schloss Schönbrunn besichtigt"* (CSV pattern)

### Scene 9 — Eine gelbe Tür

- **Premise:** A week later, after class. Amir writes his Lebenslauf for a pupils'
  Praktikum; Jule helps.
- **Angle:** Amir wants cars, not the Abitur. Krämer told Jule the same thing years ago;
  look where she is. Under "Geburtsort" Amir has written the sea and a yellow door.
- **Words (7):** der Lebenslauf, die Lehrstelle, der Abschluss, die Ausbildung, das Abitur, der Bereich, erstellen
- **Chunks:** `Lebenslauf(Akk.) schreiben` (47), `in stehen … Lebenslauf` (114), *"In welchem Bereich möchten Sie arbeiten?"* (CSV), `Ausbildung(Akk.) machen` (930)

### Scene 10 — Das Fest

- **Premise:** The last Friday in January, the course's interkulturelles Fest. Frau Wolf
  has come with cake.
- **Angle:** Every learner presents their country. Bruckner presents the model railway.
  Frau Martens praises his progress: he now lets people finish their sentences. Frau Wolf
  signs up for the next course so she can keep an eye on him.
- **Words (6):** die Präsentation, präsentieren, interkulturell, der Fortschritt, die Übung, fortsetzen
- **Chunks:** *"Präsentieren Sie Ihre Ergebnisse bitte im Kurs"* (CSV), `Fortschritt(Akk.) machen` (3394), *"Mir fehlt die Übung"* (CSV), *"ein interkulturelles Fest"* (CSV)

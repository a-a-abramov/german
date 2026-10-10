# Batch 11 — Reisen & Urlaub · Szenenplan

48 target words, **ten scenes**, two to eight words each. The batch is Julia and Tobi's
two weeks on the Ostsee island that Frau Wolf talked them into (Batch 9, Text 14), told in
order: the booking disaster, the rescue, the packing, the ferry, the arrival, the island,
and the return. Bruckner's first trip abroad is the "other characters' holidays" part of
the slot; it is told in the last text and announced in Text 9.

The topic's hazard is the **travel-agency inventory**: Hotel, Pension, Unterkunft,
Halbpension, Reservierung, Rezeption, Aufenthalt could all be recited at one counter.
They are split over four texts, each with a different person behind the counter: a
travel agent with nothing left (1), Frau Wolf on the phone (2), Frau Claasen at her
kitchen table (6), Herr Behrens at dinner (7).

## Sense decisions made against the CSV

- **`die Pension`** is the guesthouse (*"Im Urlaub haben wir in einer kleinen Pension
  gewohnt"*), Text 2. **`in Pension gehen/sein`** is retirement (*"Mein Nachbar ist seit
  zehn Jahren in Pension"*), Text 7. In Germany it is the Beamte's word, so it goes to Herr
  Behrens, a retired guest. The two senses meet in one line on purpose: *"In Pension und in
  der Pension."* The homonym is the joke and the memory hook.
- **`pensioniert werden/sein`** is said by Frau Claasen, a retired teacher (*"jetzt bin ich
  pensioniert"*), Text 6. It is kept out of Text 7 because it is a synonym of *in Pension
  sein*. Both are standard in Germany for civil servants; the corpus already uses *in Rente*
  for Bruckner (Batch 7), and he keeps it.
- **`die Kabine`**: the CSV's only example is a voting booth, which has no place in a holiday.
  The text uses the nearest everyday sense, a changing cubicle (*"Bist du noch in der
  Kabine?"*), Text 8. Not a ship's cabin: an island ferry has none.
- **`die Tropfen`** is medicine (*"Hast du die Tropfen schon genommen?"*), Frau Wolf's drops
  for the stomach on the ferry, Texts 3–4. Not raindrops.
- **`die Auskunft`** is CSV sense 1 (*"Ich hätte gern eine Auskunft"*), not directory
  enquiries. Text 5.
- **`der Aufenthalt`** is CSV sense 2, the hotelier's wish (*"einen schönen Aufenthalt"*),
  Text 6. Not a train's stop.
- **`erreichen`** is reaching somebody by phone (*"Ich habe gerade Frau Claasen erreicht"*),
  Text 2. The corpus's top senses (Ziel, Küste, Hafen) would have been a third harbour line.
- **`das Viertel`** is the city quarter (*"in einem alten Viertel"*), never *Viertel nach*.
- **`erfahren`** is *to find out* (*"habe ich erfahren"*), Text 9; **`die Erfahrung`** is the
  experience (*"Das war eine Erfahrung"*), Text 7.
- **`verreisen`** is *being away* (*"Herr Bruckner ist verreist"*, the CSV's *"ist zurzeit
  verreist"*), Text 9.

## Synonym / near-pair check

| set | kind | texts | ruling |
|---|---|:-:|---|
| `buchen` / `reservieren` | near-synonyms | 1 / 2 | **split.** Tobi *bucht* online (1), Frau Wolf *reserviert* by phone (2). Text 6 says *reserviert* and avoids *gebucht*: Tobi *"hat das Hotel ausgesucht"* |
| `die Reservierung` / `reservieren` | derivational | 6 / 2 | different texts anyway; Text 6 repeats *reserviert* next to *Reservierung*, which the skill allows |
| `das Hotel` / `die Pension` / `die Unterkunft` | specific / specific / superordinate | 1 / 2 / 1 | Hotel + Unterkunft together is superordinate + specific (*"eine Unterkunft … Ein Hotel"*). **Pension split** from Hotel. Text 5's *"wie im Hotel"* is a comparison, not a name for the Pension |
| `reisen` / `verreisen` | near-synonyms | 3 / 9 | **split** |
| `die Reise` / `der Urlaub` | near-pair | 4 / 1 | **split** |
| `das Schiff` / `das Boot` | size pair | 4 / 8 | **split.** The ferry is a *Schiff*, the excursion a *Boot* |
| `der Wohnort` / `der Wohnsitz` | synonyms | 6 / 7 | **split.** *Wohnort* is the form's field; *Wohnsitz* is Behrens's wife's *"zweiter Wohnsitz"* |
| `in Pension sein` / `pensioniert sein` | synonyms | 7 / 6 | **split** |
| `das Viertel` / `der Vorort` | contrast | 7 / 7 | **left together on purpose.** It is the contrast of the exchange: Julia lives *mitten in der Stadt, in einem alten Viertel*, Behrens *in einem Vorort*. Not two names for one place |
| `der Koffer` / `das Gepäck` | specific / superordinate | 3 / 3 | allowed (*"dein ganzes Gepäck? … in meinem Koffer"*) |
| `der Transport` / `transportieren` | derivational | 5 / 5 | together, per the skill |
| `ankommen` / `die Ankunft` | derivational | 5 / 5 | together |
| `besuchen` / `der Besuch` | derivational | 10 / 2 | different texts |
| `die Rezeption` / `das Reisebüro` | different counters | 6 / 1 | — |

## Scene order is ownership order

The scanner records first sightings, so:

- **No `Reise`, `Reis`, `reist` in Texts 1–2.** The scanner reads *Reis* as a form of both
  `die Reise` and `reisen`; Text 2's callback to Batch 8's burnt rice therefore says *"die
  Sache mit der Feuerwehr"*. `reisen` belongs to Text 3, `die Reise` to Text 4.
- **No `Koffer` or `Gepäck` before Text 3**, **no `Schiff` before Text 4** (Text 3's drops are
  *"wenn das Wasser unruhig ist"*), **no `Boot` before Text 8**, **no `Bus`, `Ausland`,
  `Toilette` before Text 10.** Text 6's room has no bathroom line.
- **No separable *kommen … an* or *packen … ein* outside their owners** (5 and 3).
- **`Pension` first appears in Text 2.** Text 1 has only the hotel.

Scanner artefacts fixed by hand after `scan --apply`:

- **`in Pension gehen/sein`**: `variants()` emits `sein`, so the first *seine* (Text 9, *"seine
  Katze"*) claims it. Owner Text 7, recorded with `vocab.py use --batch 11 --text 7`. The
  scanner's Text 9 row comes back on every rescan and is ignored. Card line: *"Und seit ich
  in Pension bin, bleiben wir sechs Wochen."*
- **`besuchen`** is credited to Text 2 by the noun *Besuch*. Owner Text 10 (*"Besucht haben wir
  nur die Restaurants."*), recorded with `use --text 10`; card from Text 10.
- **`die Pension`** is also matched in Text 7; its owner is Text 2 (*"Sie hat eine kleine
  Pension auf der Insel"*).

## Continuity

Checked against continuity.md (Batches 1–10) and the dialogues it cites.

| fact this batch touches | source |
|---|---|
| The island, two weeks in August; Frau Wolf and her husband went every year; his photo was taken at its harbour; no cars, windy | B9 T14; B2 T12 ("Achtundachtzig, am Meer") |
| Tobi was told to book *"heute noch"* | B9 T14 |
| The trip starts no earlier than Sat 8 Aug; B10 ends Thu 6 Aug and did no packing | B10 sc calendar |
| Frau Wolf hears everything through the wall; says **du / Kind** to Julia, **Sie / junger Mann** to Tobi, *ihr/euch* to both | B4 T1, B7 T6, B9 T14 |
| Tobi burnt the rice and the Feuerwehr came | B8 T1 |
| Tobi has his own flat but is always at Julia's: *"Du wohnst hier auch nicht"* | B1 T10, B4 T1 |
| Julia: fourth floor, no lift | B1 T1, B10 T7 |
| Tobi's surname Wagner; plays football | B2 T5, B9 T7; B7 T6 |
| Frau Wolf's balcony plants, overwatered | B3 T4, B9 T3 |
| Bruckner: retired, EG, cat; went to the sea every summer; building a model railway | B7 T10; B9 T11; B10 T9 |
| Bruckner says **du** to Tobi, Sie to Julia; Julia and Tobi say Sie to him | slots.md resolution; B10 T5 |
| Tobi owns a car; transport habits belong to B10 | B10 T1; slots.md. **This batch never says how they reached the coast** |
| Tobi's parents flew back 28 Jul, Gisela will never fly again | B10 T6. Not touched |

Decisions made as a result:

- **Tobi did book, just the wrong thing.** B10's plan reads B9 T14 as "booked", so Text 1 keeps
  that true: he booked a hotel on the mainland coast *"mit Blick auf die Insel"*.
- **Frau Wolf solves it by phone** through her old landlady (Text 2), and reserves under her
  own name (Text 6, *"eine Reservierung auf den Namen Wolf"*).
- **Frau Wolf's watering habit** returns in Text 9: *"Einmal am Tag."*
- **Bruckner's model railway** gives Text 10 its last line.
- No year numbers, no city name, no jobs for Julia or Tobi (B14), no money talk beyond a tip.

## New standing facts

- **Julia and Tobi spent Sat 8 – Sat 22 Aug on the island**, in **Frau Claasen's Pension**
  **at the beach** (*"direkt am Strand"*, Text 2), twenty minutes' walk from the harbour, booked by Frau Wolf after Tobi's hotel turned out to be on the mainland.
- **Frau Claasen**: runs the Pension (has done for thirty summers), was a teacher for forty
  years, now *pensioniert*. Her kitchen table is the reception. She meets every ferry with a
  luggage cart; the walk from the harbour is twenty minutes. Frau Wolf has known her for over
  thirty years and talks to her **every evening** on the phone.
- **Herr Behrens and his wife**: guests there for twenty summers, six weeks a year since he
  retired (*in Pension*). They live in a Vorort; went south once and never again.
- **On the island**: a Kiosk on the mainland harbour, a Hallenbad, a boat excursion that is
  cancelled in wind, a bench in front of a Fischladen at the harbour where Frau Wolf's
  husband sat every evening.
- Tobi gets seasick despite *"mir wird nie schlecht"*; he took Frau Wolf's drops.
- Julia's flat is described as *"mitten in der Stadt, in einem alten Viertel"*.
- **Bruckner's first trip abroad**: a five-day bus tour, four countries, fifteen cities, in
  the second half of August while Julia and Tobi were away. Frau Wolf fed his cat. Next year
  he wants to go to the sea again.
- **Frau Wolf watered Julia's flowers** while they were away (once a day).

## Calendar

| when | text |
|---|---|
| Fri 7 Aug, morning | 1. the third travel agency |
| Fri 7 Aug, afternoon | 2. Frau Wolf has phoned Frau Claasen |
| Fri 7 Aug, evening | 3. packing |
| Sat 8 Aug | 4. the ferry; 5. the harbour; 6. the kitchen table; 7. first dinner with Herr Behrens |
| a rainy day in the first week | 8. the Hallenbad |
| Thu 20 Aug, evening | 9. the bench at the harbour; Bruckner is away (bus tour about 17–21 Aug) |
| Sun 23 Aug | 10. both back; Bruckner in the courtyard |

Text 1 is on Friday 7 Aug, the day after B10's last text, and takes place before the slot's
first travel day as preparation only.

## Cast

| speaker | role | address |
|---|---|---|
| Julia, Tobi | du to each other | |
| Reisebüro clerk | unnamed woman | Sie both ways |
| Frau Wolf | du + *Kind* to Julia; Sie + *junger Mann* to Tobi; *euch* to both | Julia, Tobi → Sie |
| Frau Claasen | Pension owner | Sie both ways; *junger Mann* to Tobi |
| Herr Behrens | guest | Sie both ways; *junger Mann* to Tobi |
| Mann vom Hallenbad | unnamed | Sie, *junger Mann* |
| Herr Bruckner | du to Tobi, Sie + *Julia* to Julia | both → Sie |

---

### Scene 1 — Mit Blick auf die Insel

- **Premise:** Fri 7 Aug, the third travel agency of the morning. They leave tomorrow and need
  a room on the island.
- **Angle:** Tobi did book, *heute noch*, as ordered: a hotel on the coast *mit Blick auf die
  Insel*. The view is included; the island is not.
- **Words (8):** das Reisebüro, buchen, das Hotel, die Unterkunft, die Halbpension, inklusive, der Urlaub, die Küste
- **Chunks:** `Hotel(Akk.) buchen` (173), `Urlaub(Akk.) verbringen` (234), *"Der Zimmerpreis ist
  inklusive Frühstück"* (CSV, here *Blick … inklusive*), *"Wir möchten ein Hotel mit
  Halbpension"* (CSV), `Unterkunft(Akk.) suchen/finden` (156/184)

### Scene 2 — Frau Wolf hat telefoniert

- **Premise:** Fri afternoon, Julia's flat. Frau Wolf has heard everything through the wall.
- **Angle:** Three travel agencies found nothing; one phone call from Frau Wolf did. The price:
  Frau Claasen already knows *everything*, including the Feuerwehr.
- **Words (4):** erreichen, die Pension, reservieren, der Besuch
- **Chunks:** `erreichen + auf Handy` (197), `wohnen in … Pension` (106), `reservieren +
  Zimmer(Akk.)` (356), *"sich auf den Besuch freuen"*
- **Deliberately absent:** *Reis* (scanner reads it as `Reise`)

### Scene 3 — Leichtes Gepäck

- **Premise:** Fri evening, packing.
- **Angle:** Tobi travels light because his things are in Julia's suitcase. He will never need
  Frau Wolf's drops.
- **Words (5):** das Gepäck, reisen, der Koffer, einpacken, die Tropfen
- **Chunks:** `mit leichtem Gepäck reisen` (109 + 114), `Koffer ist voll`, *"Hast du die
  Tropfen schon genommen?"* (CSV)

### Scene 4 — Fünf Minuten

- **Premise:** Sat 8 Aug, the mainland harbour, five minutes to departure.
- **Angle:** Tobi goes to the kiosk for a fish roll, makes the ferry, and asks for the drops.
- **Words (3):** das Schiff, der Kiosk, die Reise
- **Chunks:** `ein(e) lange(r) Reise` (1843), *"Das bekommen Sie im Kiosk"* (CSV), `Schiff
  fahren` (508)

### Scene 5 — Der Wagen am Hafen

- **Premise:** The island harbour. A woman with a luggage cart.
- **Angle:** Tobi tips the porter. The porter owns the Pension.
- **Words (7):** die Auskunft, ankommen, der Treffpunkt, die Ankunft, der Transport, transportieren, das Trinkgeld
- **Chunks:** *"Ich hätte gern eine Auskunft"* (CSV), *"Was kostet der Transport?"* (CSV),
  *"Ich habe dem Kellner zwei Euro Trinkgeld gegeben"* (CSV), `bei … Ankunft` (138)

### Scene 6 — Der Küchentisch

- **Premise:** The Pension's kitchen table, which is the reception.
- **Angle:** Tobi writes Julia's address as his *Wohnort* (*"Du wohnst hier auch nicht"*,
  B1 T10, now in reverse). The retired teacher refuses to correct it.
- **Words (5):** die Rezeption, die Reservierung, der Wohnort, pensioniert werden/sein, der Aufenthalt
- **Chunks:** *"Geben Sie bitte den Schlüssel an der Rezeption ab"* (CSV), `Reservierung + auf
  Name` (31), *"Tragen Sie bitte auch Ihren Wohnort ein"* (CSV), `ein(e) schöne(r)
  Aufenthalt` (139)

### Scene 7 — Zwei Pensionen

- **Premise:** First dinner (Halbpension). Herr Behrens at the next table.
- **Angle:** *In Pension und in der Pension.* Twenty summers in the same house, and his wife has
  already planned their two weeks; they only wanted the beach.
- **Words (5):** in Pension gehen/sein, der Wohnsitz, das Viertel, der Vorort, die Erfahrung
- **Chunks:** *"Mein Nachbar ist seit zehn Jahren in Pension"* (CSV), *"Wir wohnen in einem
  Vorort von Köln"* (CSV), *"Wir wohnen in einem schönen Viertel"* (CSV), `Erfahrung machen`

### Scene 8 — Kabine sieben

- **Premise:** A rainy day; the boat excursion is cancelled; the Hallenbad.
- **Angle:** Behrens's advice twice over, and Tobi trapped by a door that says *drücken*.
- **Words (5):** die Kabine, der Ausflug, das Boot, das Hallenbad, die Sehenswürdigkeit
- **Chunks:** `Ausflug fallen(t)` (47, *fällt aus*), *"Sie geht jeden Tag zum Schwimmen ins
  Hallenbad"* (CSV), *"Welche Sehenswürdigkeiten gibt es hier?"* (CSV), `in … Kabine sein` (424)

### Scene 9 — Die Bank am Hafen

- **Premise:** Near the end, Julia phones Frau Wolf from the bench where the photo was taken.
- **Angle:** A quiet moment that Frau Wolf turns into news: she has already *erfahren* about the
  cubicle from Frau Claasen. She waters Julia's flowers *"einmal am Tag"*.
- **Words (2):** erfahren, verreisen
- **Chunks:** *"Frau Dr. Müller ist zurzeit verreist"* (CSV), *"Wann erfahren wir das
  Ergebnis?"* (CSV)

### Scene 10 — Vier Länder in fünf Tagen

- **Premise:** Back home, the courtyard. Bruckner is back from a bus tour.
- **Angle:** Fifteen cities seen through a window and one broken toilet for fifty people. Next
  time abroad only on his model railway.
- **Words (4):** der Bus, das Ausland, besuchen, die Toilette
- **Chunks:** *"Wir fahren im Urlaub meistens ins Ausland"* (CSV), *"Besucht haben wir nur die Restaurants"*

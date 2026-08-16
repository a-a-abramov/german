# Batch 1 — In der Wohnung & Zuhause · Szenenplan

142 target words grouped **by situation** into 11 scenes (10–16 words each). This replaces
the retired alphabetical slicing: every scene below is a place and a moment two people
could actually be standing in, and the words were pulled to it from wherever they sat in
the list.

Recurring cast, so the batch reads as one flat and one week:
**Nadja** (moves in), **Herr Bruckner** (the caretaker/Hausmeister),
**Tobi** (friend who helps and eats), **Frau Wolf** (the neighbour from next door).

**Standard German only.** The Goethe list's Austrian and Swiss doublets (Stiege,
Stiegenhaus, Eck, Fauteuil, Abwart) are out of scope and excluded from the ledger — the
five they replace (Treppe, Treppenhaus, Ecke, Sessel, Hausmeister) carry those meanings.

---

### Scene 1 — Die Wohnungsbesichtigung
- **Premise:** Nadja views an empty flat; the caretaker walks her through it, selling the central location and quietly downplaying the broken lift.
- **Angle:** He calls the fourth floor "sportlich" and the lift "gerade in Reparatur" — for two years.
- **Words (11):** die Wohnung, wohnen, zentral, das Zentrum, der Raum, das Zimmer, der Stock, der Aufzug, der Hausmeister / die Hausmeisterin, möbliert, die Einrichtung

### Scene 2 — Der Umzugstag
- **Premise:** Moving day. Everything has to go from the truck at the gate, through the entrance, up the stairs.
- **Angle:** The neighbour quotes the house rules at everyone while carrying nothing at all.
- **Words (12):** der Umzug, umziehen, packen, die Schachtel, das Tor, der Eingang, die Treppe, das Treppenhaus, der Flur, die Halle, die Etage, der Kuli

### Scene 3 — Ausgesperrt
- **Premise:** Nadja is locked out on the first evening; Tobi is on the phone; the plan involves the neighbour's balcony.
- **Angle:** The note she leaves for the caretaker gets longer than the problem, and the spare key was in her pocket.
- **Words (12):** der Schlüssel, das Schloss, die Tür, öffnen, das Schild, der Balkon, der Zettel, der Stift, der Kugelschreiber, das Blatt, das Papier, das Stockwerk

### Scene 4 — Das Regal aus dem Karton
- **Premise:** Two people assemble flatpack shelving without reading the instructions.
- **Angle:** It stands — leaning on the wall, one screw short, and nobody is allowed to touch it.
- **Words (15):** die Anleitung, das Möbel, einrichten, das Regal, der Schrank, der Tisch, der Stuhl, der Hammer, der Nagel, locker, die Wand, der Boden, der Platz, die Mitte, der Rand

### Scene 5 — Der gute Sessel
- **Premise:** Film evening. There is one armchair everybody wants and one everybody avoids.
- **Angle:** The good armchair is objectively the worst piece of furniture in the flat, and its owner defends it like an heirloom.
- **Words (12):** der Sessel, das Sofa, das Kissen, der Teppich, die Lampe, das Licht, ausmachen, die Kerze, das Streichholz, die Vase, das Wohnzimmer, die Tafel

### Scene 6 — Sonntag in der Küche
- **Premise:** Cooking together in a kitchen with one pot, and the washing-up negotiation that follows.
- **Angle:** Whoever cooks doesn't wash up — so both suddenly want to cook, and nobody has started.
- **Words (14):** die Küche, der Herd, derOfen, der Kühlschrank, der Topf, die Schüssel, das Geschirr, abwaschen, das Messer, der Löffel, das Glas, die Flasche, das Brot, die Dose

### Scene 7 — Der Frühjahrsputz
- **Premise:** A whole Saturday of cleaning, sorting and labelling.
- **Angle:** Three hours in, the flat is dirtier than at the start because everything is now on the floor "in order".
- **Words (14):** putzen, sauber, schmutzig, der Schmutz, der Staub, das Tuch, die Bürste, die Ordnung, ordnen, der Ordner, das Heft, das Lager, die Ecke, der Korridor

### Scene 8 — Der Mülltag
- **Premise:** Bin day: the wrong bin, the wrong day, and a neighbour who knows the rules by heart.
- **Angle:** The bin is full and the lorry does not come until Thursday; the sack lives in the garden shed until then, next to the caretaker's own.
- **Words (16):** der Müll, die Mülltonne, die Müllabfuhr, der Abfall, der Abfalleimer, der Sack, das Haus, der Haushalt, der Keller, die Garage, die Hütte, der Garten, das Dach, die Büchse, der Zugang, die Terrasse

### Scene 9 — Waschtag
- **Premise:** Laundry day in the shared basement machine, plus the pile of things that need mending or the dry cleaner.
- **Angle:** He can sew exactly one thing. Nadja's childhood doll goes through the machine once a year on purpose and survives every time.
- **Words (13):** die Wäsche, das Waschmittel, die Reinigung, reinigen, die Socke, die Nadel, nähen, die Schere, die Garderobe, sich umziehen, der Schirm, die Puppe, das Wasser

### Scene 10 — Die kalte Wohnung
- **Premise:** The heating dies in November. Nadja and Tobi want a bath; Bruckner is already in it, "testing whether the hot water still works".
- **Angle:** The one man who could fix the heating is the reason nobody can get warm.
- **Words (13):** das Bad, die Badewanne, baden, besetzen, die Heizung, heizen, die Zahnbürste, das Bett, der Schlaf, schlafen, die Decke, die Couch, das Heim

### Scene 11 — Die Einweihungsparty
- **Premise:** Housewarming: a bar improvised on the kitchen table, guests at the window, a building site outside.
- **Angle:** At six the building site starts up again, punctually, like an alarm clock. That is the housewarming's parting gift.
- **Words (10):** die Bar, das Zuhause, das Apartment, das Fenster, die Scheibe, außen, der Bau, bauen, die Baustelle, die Uhr

---

**Which text owns a word (for card-cutting): this file.** The ledger's `uses.text_no`
records where `vocab.py scan` *first saw* a word, which is not the same thing — 12 of the
142 appear incidentally in an earlier dialogue before the scene that owns them:

| word | first seen | owned by |
|---|---:|---:|
| die Treppe | Text 1 | Scene 2 |
| die Küche | Text 1 | Scene 6 |
| das Haus | Text 1 | Scene 8 |
| der Schrank | Text 2 | Scene 4 |
| sich umziehen | Text 2 | Scene 9 |
| die Uhr | Text 2 | Scene 11 |
| außen | Text 3 | Scene 11 |
| das Fenster | Text 4 | Scene 11 |
| die Socke | Text 5 | Scene 9 |
| schmutzig | Text 6 | Scene 7 |
| der Keller | Text 7 | Scene 8 |
| die Baustelle | Text 7 | Scene 11 |

Each of the twelve also appears in its own scene's dialogue, so every cloze can still be
cut verbatim from the owning text. Incidental earlier hits are a bonus, not a reassignment.

`sich umziehen` was set by hand to Text 9 (`Zieh dich um`): in Text 2 the scanner folds
*ziehe … um* out of `umziehen` (move house) and cannot tell the two apart.

_Partition verified against the ledger: 142 assigned, 0 duplicated, 0 left over._

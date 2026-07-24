# Goethe B1 Wortliste — Topic Taxonomy & Scene-Outline Groundwork

Groundwork for the crammed-topic-batch / mnemonic-scene Anki method. This file is taxonomy + scene **outlines** only — no German practice texts are written here.

Source: `goethe-b1-wortliste.csv`, 2886 entries (header row skipped). Parsed with Python (see Methodology note at the end); lemma = the first headword segment of column 1, with regional-variant `→` lines and parenthetical region tags (D/A/CH) stripped.

## 1. Topic taxonomy

| Topic | Words | Description |
|---|---:|---|
| Grammatik & Verbindungswörter | 360 | Prepositions, conjunctions, question words, pronouns, modal/hilfsverbs, degree adverbs and other glue words — the connective tissue of every scene (see strategy note below). |
| Unterwegs & Verkehr | 115 | Transport, traffic, directions, cars, trains, planes. |
| Schule & Bildung | 84 | School, university, courses, exams, learning. |
| Freizeit, Medien & Technik | 216 | Hobbies, sport, TV/film/music, art, gadgets, the internet. |
| Handlungen: Alltagsverben | 212 | The general-purpose verb toolkit — give/take, fix, organize, react — that powers everyday scenes. |
| Denken, Wissen & Meinen | 162 | Mental verbs: think, know, decide, remember, doubt, agree. |
| Einkaufen & Geld | 135 | Shopping, prices, banking, paying, contracts, budgets. |
| Menge, Maß & Eigenschaften | 164 | Size, quantity, quality judgments and general descriptive adjectives. |
| In der Wohnung & Zuhause | 153 | Rooms, furniture, household objects, chores, moving house. |
| Natur, Wetter & Umwelt | 107 | Weather, landscape, environment, climate, countryside. |
| Familie & Beziehungen | 107 | Family members, life stages, relationships, weddings, parenting. |
| Gefühle & Charakter | 122 | Emotions and personality traits. |
| Kommunikation & Post | 177 | Talking, phoning, writing letters/emails, the postal system, news media. |
| Stadt, Ämter & Recht | 150 | City life, government offices, bureaucracy, police, law, crime. |
| Arbeit & Beruf | 139 | Jobs, workplace, careers, hiring/firing, professions. |
| Kleidung & Aussehen | 48 | Clothing, accessories, hairstyling, appearance. |
| Körper & Gesundheit | 139 | Body parts, illness, doctor, pharmacy, hospital, symptoms. |
| Reisen & Urlaub | 54 | Travel, hotels, vacation, tourism. |
| Zeit & Kalender | 91 | Time expressions, calendar, daily routine, punctuality. |
| Gesellschaft, Politik & Wirtschaft | 20 | Society, politics, economy — the smallest topic; most B1 words in this space are abstract enough to also fit Stadt/Ämter or Denken. |
| Essen, Kochen & Restaurant | 149 | Food, drink, cooking, groceries, restaurant & café life. |
| Tiere | 8 | Animals and farm life (a small, genuinely thin category in the B1 list). |
| **Total (with ~26 intentional cross-topic duplicates)** | **2912** | |

## 2. Assignment strategy

**Unambiguous words** (concrete nouns/verbs clearly of one domain — `der Teppich`, `die Bäckerei`, `der Bahnhof`) were assigned straight to their obvious topic.

**Generic / abstract content words** (verbs like `machen`, `bringen`, `stellen`; adjectives like `gut`, `schwer`, `deutlich`; nouns like `die Lage`, `der Sinn`) were distributed into four purpose-built topics that exist precisely to carry this vocabulary into concrete scenes: **Handlungen: Alltagsverben** (general-purpose action verbs), **Menge, Maß & Eigenschaften** (size/quality/quantity judgments), **Denken, Wissen & Meinen** (mental verbs — deciding, remembering, doubting), and **Kommunikation & Post** absorbs generic speech-act verbs (`sagen`, `antworten`, `behaupten`). Each of these is still just as scene-outlined as a concrete topic like Tiere — e.g. `stellen/legen/setzen` naturally live in a moving-day scene, `schwer/leicht` in a gym or a suitcase-packing scene.

**Function / grammar words** (articles, pronouns, prepositions, conjunctions, question words, modal particles, degree adverbs — ~360 words) get their own dedicated topic, **Grammatik & Verbindungswörter**, rather than being force-fitted into unrelated concrete scenes (the task's alternative strategy). Rationale: these words are the connective tissue of *every* scene regardless of topic, so pretending each belongs to "Tiere" or "Essen" would be artificial. Instead they get their own scene-sized batches, each grouped **by grammatical function, not alphabetically** (prepositions / conjunctions / question words / spatial adverbs / time adverbs / degree particles / pronouns / modal verbs / small-talk glue), so every one of those scenes still has a concrete, imaginable premise (e.g. a scene of pure spatial adverbs becomes "give chaotic directions to a lost drone"). A handful of function-adjacent words that read naturally as part of a concrete scene (`heute`, `gestern`, `oft` → Zeit & Kalender; `Wetter`-adjacent connectors) were instead folded into the relevant concrete topic — the two strategies were mixed pragmatically rather than dogmatically applying only one.

**Near-partition, not a strict one:** each word gets exactly one home topic by default. ~26 words (~0.9%) were deliberately placed in a second topic because they genuinely power two different scene types (e.g. `der Bus` in both Unterwegs/Verkehr and Reisen/Urlaub; `das Brot` in both In-der-Wohnung and Essen; `dumm`/`beißen` in both a feelings scene and a body/health scene). These are listed in the coverage-audit note below.

## 3. Coverage audit

Verified numerically with Python: every topic's word list was matched back against the full parsed headword set by exact string, consuming one CSV row per match (duplicate-string rows like the two distinct `die Bank` entries — bench vs. financial bank — are disambiguated by row index, not string, so each lands on its own row). Result:

- Total entries: **2886**
- Assigned (unique rows covered): **2886**
- Unassigned: **0**

**No unassigned entries.**

Words intentionally placed in more than one topic (26), because they genuinely power two different scene types:

<details><summary>show the 26 cross-topic words</summary>

- `abheben` — Handlungen: Alltagsverben, Einkaufen & Geld
- `abnehmen` — Handlungen: Alltagsverben, Körper & Gesundheit
- `ausmachen` — Handlungen: Alltagsverben, In der Wohnung & Zuhause
- `beißen` — Gefühle & Charakter, Körper & Gesundheit
- `bevor` — Grammatik & Verbindungswörter, Zeit & Kalender
- `beweisen` — Denken, Wissen & Meinen, Stadt, Ämter & Recht
- `bitter` — Einkaufen & Geld, Essen, Kochen & Restaurant
- `buchen` — Schule & Bildung, Reisen & Urlaub
- `dankbar` — Handlungen: Alltagsverben, Gefühle & Charakter
- `das Brot` — In der Wohnung & Zuhause, Essen, Kochen & Restaurant
- `das Diplom` — Freizeit, Medien & Technik, Arbeit & Beruf
- `dekorieren` — Freizeit, Medien & Technik, Handlungen: Alltagsverben
- `der Bus` — Unterwegs & Verkehr, Reisen & Urlaub
- `der Kellner / die Kellnerin` — Gefühle & Charakter, Arbeit & Beruf
- `der Täter / die Täterin` — Stadt, Ämter & Recht, Arbeit & Beruf
- `die Auskunft` — Kommunikation & Post, Reisen & Urlaub
- `die Ausnahme` — Denken, Wissen & Meinen, Einkaufen & Geld
- `die Bevölkerung` — Familie & Beziehungen, Gesellschaft, Politik & Wirtschaft
- `die Bibliothek` — Schule & Bildung, Freizeit, Medien & Technik
- `die Biologie` — Schule & Bildung, Freizeit, Medien & Technik
- `die Bohne` — Einkaufen & Geld, Essen, Kochen & Restaurant
- `diesmal` — Grammatik & Verbindungswörter, Zeit & Kalender
- `doch` — Grammatik & Verbindungswörter, Denken, Wissen & Meinen
- `installieren` — Freizeit, Medien & Technik, Stadt, Ämter & Recht
- `schneien` — Handlungen: Alltagsverben, Natur, Wetter & Umwelt
- `vertrauen` — Grammatik & Verbindungswörter, Gefühle & Charakter

</details>

## 4. Scene outlines

~10–15 target words per scene, grouped by topic (and by grammatical/semantic sub-function for the four abstract topics). Outlines only — premise + comedic angle + word list; no German text.

### Grammatik & Verbindungswörter  _360 words, 28 scenes_

**Scene 1 — *Präpositionen (Ort/Zeit/Grund)*: Der Wegbeschreibungs-Kauderwelsch**
- Premise: A tourist asks a local for directions and gets an answer built entirely out of prepositions, no content words.
- Comedic angle: The local is so proud of using every preposition correctly that the tourist ends up more lost than before.
- Words (13): ab, an, auf, aus, bei, bis, durch, entlang, für, gegen, gegenüber, in, mit

**Scene 2 — *Präpositionen (Ort/Zeit/Grund)*: Der zweite Streckenabschnitt**
- Premise: The same over-eager local keeps going, piling on more prepositions for a second, even longer route.
- Comedic angle: By the end he's pointing in six directions at once and contradicting himself.
- Words (16): nach, neben, ohne, per, pro, seit, statt, trotz, über, um, unter, von, vor, während, wegen, zwischen

**Scene 3 — *Konjunktionen & Satzverbinder*: Der Ausredenkatalog**
- Premise: Someone late for work rehearses an excuse in front of a mirror, stringing together every connector to sound more sophisticated.
- Comedic angle: The sentence gets so long and hedged that by the time it ends, the meeting is over.
- Words (13): aber, als, als ob, also, bevor, dass, denn, deshalb, deswegen, doch, entweder ... oder, indem, je … desto …

**Scene 4 — *Konjunktionen & Satzverbinder*: Der endlose Nebensatz**
- Premise: The same rehearsal continues, the excuse spiraling into ever more nested clauses.
- Comedic angle: He finally just says 'weil... äh...' and gives up, defeated by his own grammar.
- Words (17): jedoch, nachdem, obwohl, oder, seitdem, sobald, sodass, solange, sondern, sowohl … als auch, trotzdem, und, weder … noch, weil, wenn, um … zu, falls

**Scene 5 — *Fragewörter*: Der Verhörraum**
- Premise: A detective interrogates a suspect using nothing but question words, rapid-fire.
- Comedic angle: The suspect answers every question with another question, and the interrogation turns into a ping-pong match.
- Words (13): was, was für ein-, wann, warum, weshalb, wie, wieso, wie viel, wo, woher, wohin, wer, welcher

**Scene 6 — *Richtung & Ort (Raumadverbien)*: Die Nachbarschaftsdrohne**
- Premise: A neighbor's drone hovers around, and everyone shouts spatial directions trying to get it to land.
- Comedic angle: The drone operator is deaf and just nods at everything, sending it further astray each time.
- Words (13): da, dabei, dafür, dagegen, daher, dahin, damit, daneben, dort, dorthin, drüben, drin, entgegenkommen

**Scene 7 — *Richtung & Ort (Raumadverbien)*: Verstecken im Möbelhaus**
- Premise: Kids play hide-and-seek in a furniture store, calling out where they're hiding.
- Comedic angle: One kid hides literally inside a wardrobe display and nobody can find him for an hour.
- Words (13): her/her-, heraus-, herein-, herunter-, hier/hier-, hierher, hinten, hinter/hinter-, innen, inner-, innerhalb, nah, nebenan

**Scene 8 — *Richtung & Ort (Raumadverbien)*: Die Parkplatzsuche**
- Premise: A driver circles a full car park giving turn-by-turn directions to a passenger holding a phone.
- Comedic angle: They pass the same spot three times before realizing 'geradeaus' was actually a dead end.
- Words (13): nebenbei, oben, ober-, unten, unter-, unterwegs, vorn, vorder-, waagerecht, quer, rauf/rauf-, raus/raus-, rechts

**Scene 9 — *Richtung & Ort (Raumadverbien)*: Der GPS-Ausfall**
- Premise: The GPS breaks mid-hike and the group has to navigate by shouting direction words at each other across a ravine.
- Comedic angle: They end up walking in a perfect circle back to the car.
- Words (8): rein, überall, vorbei/vorbei-, weg/weg-, zurück/zurück-, geradeaus, weit, lang

**Scene 10 — *Zeitadverbien*: Der Wecker-Kampf**
- Premise: Someone hits snooze on their alarm clock over and over, narrating each delay with a time adverb.
- Comedic angle: By 'irgendwann' it's already afternoon and they missed the whole day.
- Words (13): bisher, diesmal, fest, fertig, gerade, jetzt, jeweils, kurz, kürzlich, lange, langsam, längst, letzt-

**Scene 11 — *Zeitadverbien*: Die Warteschlange beim Amt**
- Premise: People in a slow-moving government-office queue mutter time words about how long they've been waiting.
- Comedic angle: The person at counter one has apparently been 'gleich dran' for three years.
- Words (13): meist, meist-, mittlerweile, nachher, nächst-, noch, noch mal, nochmals, normalerweise, nun, oft/öfter, plötzlich, regelmäßig

**Scene 12 — *Zeitadverbien*: Der Countdown zur Prüfung**
- Premise: A student obsessively tracks the time before an exam, narrating every stage of dread.
- Comedic angle: 'Zurzeit' revises nothing and just refreshes the clock app instead.
- Words (13): sofort, ständig, übermorgen, vorgestern, vorher, vorhin, vorläufig, zuerst, zunächst, zurzeit, zuletzt, zumindest, inzwischen

**Scene 13 — *Zeitadverbien*: Der Wiederholungstäter**
- Premise: A repeat-offender packrat keeps promising 'irgendwann' to clean the garage, one excuse per weekend.
- Comedic angle: Years pass; the garage now qualifies as an archaeological site.
- Words (9): irgendwann, jederzeit, jedes Mal, bereits, extra, manchmal, sonst, weiter/weiter-, wieder/wieder-

**Scene 14 — *Grad-, Mengen- & Modalpartikeln*: Die Mengenlehre am Buffet**
- Premise: Guests at a buffet negotiate portion sizes using nothing but degree and quantity words.
- Comedic angle: One guest says 'ein bisschen mehr' seven times until his plate collapses under the weight.
- Words (13): auch, außer, außerdem, beinahe, direkt, eben, ebenfalls, ebenso, extrem, ganz, gar, genau, genauso

**Scene 15 — *Grad-, Mengen- & Modalpartikeln*: Die Waage im Fitnessstudio**
- Premise: Two friends compare gym progress, hedging every claim with degree adverbs to avoid admitting who's stronger.
- Comedic angle: They both end up so vague that neither can tell who actually won the bet.
- Words (13): gleich, gleichfalls, gleichzeitig, kaum, komplett, mehr, mehrere, mindestens, möglichst, nur, paar, recht, relativ

**Scene 16 — *Grad-, Mengen- & Modalpartikeln*: Der übervorsichtige Wettermelder**
- Premise: A radio presenter reads the weather forecast while hedging every single sentence with a degree word.
- Comedic angle: By the end the forecast is technically true for every possible weather condition at once.
- Words (13): richtig, sehr, sicher, so, sogar, soviel, so viel/so viel wie, sowieso, überhaupt, umso, umsonst, ungefähr, viel/viele

**Scene 17 — *Grad-, Mengen- & Modalpartikeln*: Die Beichte im Café**
- Premise: A friend confesses something embarrassing, softening the blow with modal particles and hedges.
- Comedic angle: By the time she finally says the actual secret, everyone has already guessed three wrong, funnier things.
- Words (16): vielleicht, völlig, wenig/wenige, wenigstens, zusammen/zusammen-, allerdings, ja, nämlich, natürlich, offenbar, schon, selbstverständlich, wahrscheinlich, vermutlich, zwar, wohl

**Scene 18 — *Pronomen & Artikelwörter*: Der Familienstreit ums Sofa**
- Premise: A family argues about who broke what, everyone using vague pronouns to avoid blame.
- Comedic angle: 'Jemand' turns out to be the dog, who is smugly unbothered on the ruined sofa.
- Words (13): derselbe, dies-, eigen-, es, jeder, kein-, man, manch-, nichts, niemand, selb-, selbst, selber

**Scene 19 — *Pronomen & Artikelwörter*: Die Bühnenmagierin**
- Premise: A magician on stage makes items vanish, narrating with pronouns and indefinite articles to build suspense.
- Comedic angle: Her 'niemand' trick fails because the volunteer is clearly visible the whole time, hiding behind a too-small curtain.
- Words (16): solch-, irgendirgendein, jemand, jemals, nirgends, nirgendwo, nie, nein, beid-, ein bisschen, meinetwegen, möglich, die Möglichkeit, worüber, worum, zufällig

**Scene 20 — *Modal- & Hilfsverben*: Der Ratespiel-Moderator**
- Premise: A game-show host quizzes contestants with vague-pronoun riddles.
- Comedic angle: One contestant answers every riddle with 'zufällig' as if that were the actual word being guessed.
- Words (11): dürfen, können, möchten, mögen, müssen, sollen, wollen, werden, haben, sein, lassen

**Scene 21 — *Alltags-Kleinwörter & Small Talk*: Die überforderten Eltern**
- Premise: Parents negotiate bedtime with a toddler using every modal verb they know to sound firm and flexible at once.
- Comedic angle: The toddler out-negotiates them and ends up staying up an hour later.
- Words (13): bitte, bloß, der Fall, fällig, falsch, fast, frei, im Freien, freiwillig, fremd, die Form, das Geschlecht, auseinander

**Scene 22 — *Alltags-Kleinwörter & Small Talk*: Der Small-Talk-Marathon beim Amt**
- Premise: Strangers waiting at a government office make painfully polite small talk to pass the time.
- Comedic angle: One insists on complimenting everything in the room, down to the fluorescent lighting.
- Words (13): begleiten, das Detail, das Gegenteil, sich befinden, gucken, halt, klar, klappen, klären, komisch, kommen, kompliziert, korrekt

**Scene 23 — *Alltags-Kleinwörter & Small Talk*: Die WG-Küchenkonferenz**
- Premise: Roommates hold a mock-formal meeting about kitchen chaos, using stiff small-talk phrases for comic effect.
- Comedic angle: The 'meeting' is really just about who keeps leaving dishes, but they minute it like a UN summit.
- Words (13): die Länge, der Kreis, leid tun, heim, hinterlassen, laut, miteinander, mitten, mittler-, nett, neu, nicht, niedrig

**Scene 24 — *Alltags-Kleinwörter & Small Talk*: Der zu ehrliche Nachbar**
- Premise: A blunt neighbor comments on everything happening on the street, unfiltered.
- Comedic angle: His running commentary turns a boring afternoon into unwanted reality TV for the whole block.
- Words (13): normal, Lieblings-, ob, offen, parallel, privat, nutzen, passen, die Sache, passiv, riechen, sehen, die Seite

**Scene 25 — *Alltags-Kleinwörter & Small Talk*: Die Reklamation im Elektroladen**
- Premise: A customer tries to return a broken gadget, using every polite hedge to avoid sounding rude.
- Comedic angle: The clerk is even more indirect, and the return process takes forty-five minutes of mutual politeness.
- Words (13): sitzen, stattfinden, stammen, Speise-/-speise, Spezial-, speziell, stumm, die Stufe, das Teil, der Teil, das Stück/-stück, übrig, übrigens

**Scene 26 — *Alltags-Kleinwörter & Small Talk*: Der Möbelaufbau-Streit**
- Premise: A couple assembles flatpack furniture, bickering with clipped filler words instead of full sentences.
- Comedic angle: The finished shelf ends up upside down, but structurally sound.
- Words (13): unbedingt, un-, vertrauen, voneinander, vor allem, voraus, ursprünglich, zu, zu sein, wachsen, der Zweck, einschließlich, einverstanden

**Scene 27 — *Alltags-Kleinwörter & Small Talk*: Der Heimweh-Anruf**
- Premise: Someone calls home describing a chaotic new apartment using small, connective words to soften every complaint.
- Comedic angle: Their parent keeps interrupting with 'wirklich?' until the call is 90% interjections.
- Words (13): entstehen, erfüllen, ergänzen, etwa, etwas, eventuell, miss-, mobil/mobil-, national/national-, negativ, durcheinander, eigentlich, fallen

**Scene 28 — *Alltags-Kleinwörter & Small Talk*: Der Privatdetektiv im Café**
- Premise: An amateur detective narrates his stakeout under his breath, treating mundane details as huge clues.
- Comedic angle: His biggest breakthrough of the day is realizing the barista is 'privat' just tired, not suspicious.
- Words (7): gern/gerne, gesamt-/Gesamt-, je, nehmen, nennen, recht-, sogenannt-


### Unterwegs & Verkehr  _115 words, 9 scenes_

**Scene 1: Die Fahrschulprüfung**
- Premise: A nervous learner driver takes their test, narrating every action to the instructor out loud.
- Comedic angle: They announce the seatbelt three times before actually buckling it, stalling the car twice in a one-way street.
- Words (13): abbiegen, abfahren, die Abfahrt, abwärts, die Ampel, aufwärts, Achtung!, bremsen, die Bremse, der Bus, ein-, die Einbahnstraße, die Einfahrt

**Scene 2: Der verpasste Flug**
- Premise: A family sprints through an airport trying to catch a departing flight after misreading the schedule.
- Comedic angle: Dad insists the pilot will 'definitely wait for us' while dragging a suitcase that keeps popping open.
- Words (13): einsteigen, die Eisenbahn, fahren, die Fähre, die Fahrbahn, der Fahrer, die Fahrkarte, der Fahrplan, das Fahrrad, das Fahrzeug, fliegen, der Flug, der Flughafen

**Scene 3: Die Bahnhofsverwirrung**
- Premise: A tourist tries to find the right platform among S-Bahn, U-Bahn and long-distance trains, asking everyone for help.
- Comedic angle: Three different strangers give three contradictory directions, and he ends up on all three trains in one hour.
- Words (13): das Flugzeug, der Führerausweis, der Führerschein, der Ausgang, die Ausfahrt, ausfallen, das Auto, die Autobahn, die Bahn, S-Bahn, die Straßenbahn, die U-Bahn, der Bahnhof

**Scene 4: Der Fahrradkurier im Stress**
- Premise: A bike courier weaves through pedestrian zones and speed limits while narrating a running commentary of near-misses.
- Comedic angle: He nearly flattens a jogger, apologizes over his shoulder, and speeds off unbothered.
- Words (13): der Bahnsteig, der Anschluss, anschnallen, der Fußgänger / die Fußgängerin, die Fußgängerzone, der Gang, die Geschwindigkeit, die Geschwindigkeitsbeschränkung, die Brücke, der Gehsteig, das Gleis, die Haltestelle, hupen

**Scene 5: Der Anfängerlotse**
- Premise: A backseat driver gives contradictory turn-by-turn directions during a road trip, causing chaos at every curve.
- Comedic angle: They end up doing a full loop and passing the same lift-bridge twice.
- Words (13): fahren, runterwerfen, der Laster, landen, laufen, die Kreuzung, die Kurve, die Landung, der Lift, die Linie, links, link-, los/los-

**Scene 6: Die Motorradpanne**
- Premise: A motorcycle breaks down mid-trip, and the rider has to hitch a ride while pushing it through a parking lot.
- Comedic angle: A stranger's car ends up towing it with a rope that snaps hilariously at the worst possible moment.
- Words (13): losfahren, die Maschine, das Motorrad, der Motor, der Park, parken, parkieren, der Perron, die Panne, der Passagier / die Passagierin, das Rad, das Rad, der Reifen

**Scene 7: Die Fahrradtour zur Altstadt**
- Premise: A group cycles into the historic city center, arguing over the map and getting stuck in a tight lane.
- Comedic angle: One cyclist's backpack knocks over an entire café's outdoor seating on the way past.
- Words (13): der Radfahrer / die Radfahrerin, rückwärts, die Rückfahrt, die Rückkehr, die Rundfahrt, der Rucksack, der Schalter, schieben, der Schritt, die Stadt, städtisch, der Stadtplan, der Stau

**Scene 8: Die Tankstellenpanne**
- Premise: A driver's car sputters into a gas station on fumes right as a huge traffic jam forms on the highway overpass.
- Comedic angle: He accidentally puts the wrong fuel in and has to call for help, blocking the pump for everyone else.
- Words (13): die Straße, die Straßenbahn, die Strecke, tanken, die Tankstelle, die Spur, der Stecker, die Steckdose, das Trottoir, die U-Bahn, überfahren, überholen, überqueren

**Scene 9: Die Umleitung ins Nirgendwo**
- Premise: A detour sign sends drivers on a bizarre loop through a town, ending up back where the traffic jam started.
- Comedic angle: By the fifth roundabout, the driver starts recognizing the same dog on the same corner.
- Words (11): die Umleitung, umsteigen, der Verkehr, das Verkehrsmittel, das Velo, das Tram, umgehen, der Wagen, der Zug, die Zone, der Weg


### Schule & Bildung  _84 words, 7 scenes_

**Scene 1: Der verschlafene Prüfungstag**
- Premise: A student who overslept sprints to school, illustrations of the missed material scattered across the exam sheet.
- Comedic angle: He mixes up the diagram labels so badly the teacher isn't sure if it's biology or abstract art.
- Words (13): die Abbildung, abschreiben, das Abitur, der Abschluss, der Abschnitt, anwenden, anwesend, abwesend, das Alphabet, analysieren, die Ausbildung, ausgebildet, aussprechen

**Scene 2: Die Bibliotheksdurchsuchung**
- Premise: A student desperately searches the library for one specific book right before a deadline.
- Comedic angle: The book turns out to be checked out by the teacher who assigned the essay in the first place.
- Words (13): die Aussprache, besichtigen, die Bibliothek, das Buch, die Buchhandlung, buchen, die Biologie, eintreten, der Eintritt, entwickeln, die Entwicklung, das Ergebnis, erklären

**Scene 3: Der Forschungsclub**
- Premise: An overambitious school club announces a grand research project with a fancy progress report.
- Comedic angle: Their big 'breakthrough' turns out to be reheated homework from last semester.
- Words (13): die Erklärung, erstellen, die Forschung, die Fortbildung, der Fortschritt, fortsetzen, die Fortsetzung, das Forum, die Aufgabe, aufgeben, das Beispiel, der Bereich, beginnen

**Scene 4: Die Gedichtstunde**
- Premise: A patience-testing poetry class drags on while a bored student doodles instead of writing.
- Comedic angle: His 'poem' turns out to be one sentence repeated with different punctuation, and the teacher grades it anyway.
- Words (13): der Beginn, der Bleistift, das Gedicht, die Geduld, die Hausaufgabe, das Institut, der Intensivkurs, interkulturell, international, die Klasse, die Klassenarbeit, der Kurs, der Kursleiter / die Kursleiter

**Scene 5: Der Berufsschulmarathon**
- Premise: An apprentice bounces between shifts at the trade school and a part-time job, narrating an exhausting schedule.
- Comedic angle: He falls asleep mid-sentence during roll call and answers 'here' to someone else's name.
- Words (13): die Lehre, die Lehrstelle, der Lehrer / die Lehrerin, der Lehrling, der Lebenslauf, das Kapitel, lernen, der Lerner / die Lernerin, lesen, der Leser / die Leserin, die Nachhilfe, die Matura, die Note

**Scene 6: Die Referatspanne**
- Premise: A student's presentation slides crash right as they start presenting to the whole class.
- Comedic angle: They improvise the entire university-level topic using only hand gestures and a marker on the whiteboard.
- Words (13): präsentieren, die Präsentation, die Prüfung, prüfen, das Referat, die Schule, die Schularbeit, der Schüler / die Schülerin, das Seminar, das System, der Stil, theoretisch, die Universität

**Scene 7: Der Übersetzungsnotfall**
- Premise: A student mistranslates a foreign pen pal's letter so badly that the reply makes no sense at all.
- Comedic angle: The pen pal writes back thinking they've been challenged to a duel.
- Words (6): unterrichten, der Unterricht, übersetzen, der Übersetzer / die Übersetzerin, die Übersetzung, die Übung


### Freizeit, Medien & Technik  _216 words, 17 scenes_

**Scene 1: Der Filmabend-Chaos**
- Premise: Friends try to film a home movie for a subscription channel, but nobody can operate the camera properly.
- Comedic angle: The 'star' of the film keeps accidentally walking out of frame to check her phone.
- Words (13): das Abenteuer, abonnieren, das Abonnement, sich amüsieren, die Aktivität, anklicken, ansehen, aufnehmen, die Aufnahme, auftreten, der Auftritt, aufführen, ausgehen

**Scene 2: Die Kunstausstellung**
- Premise: An amateur artist's gallery opening features one badly hung painting and a memorial plaque nobody understands.
- Comedic angle: A visitor mistakes the coat rack for an exhibit and starts seriously analyzing it.
- Words (13): die Ausstellung, ausstellen, automatisch, der Autor / die Autorin, der Beleg, beliebt, das Ballett, die Bibliothek, das Bild, der Bildschirm, das Billett, die Biologie, klettern

**Scene 3: Der Streaming-Absturz**
- Premise: A group tries to binge-watch a show but the file keeps corrupting mid-scene.
- Comedic angle: They end up acting out the missing dialogue themselves, badly, in increasingly dramatic voices.
- Words (13): die Broschüre, die Bühne, die Datei, die Daten, das Denkmal, der Dialekt, der Dialog, digital, das Diplom, die Diskothek, diskutieren, die Diskussion, dekorieren

**Scene 4: Die improvisierte Geburtstagsfeier**
- Premise: The TV remote breaks right before a birthday party, so guests must operate everything manually.
- Comedic angle: Someone has to physically stand by the TV changing channels like a human remote control all night.
- Words (13): einfügen, einschalten, elektrisch, Elektro-, elektronisch, die Fantasie/Phantasie, fantastisch, feiern, die Feier, der Feiertag, die Fernbedienung, fernsehen, das Fernsehen

**Scene 5: Das Fotoshooting-Desaster**
- Premise: An amateur photographer tries to shoot a festival, but the equipment keeps malfunctioning at the worst moments.
- Comedic angle: Every 'perfect shot' turns out to have someone's thumb over the lens.
- Words (13): der Fernseher, die Festplatte, das Fest, die Figur, der Film, die Flöte, fotografieren, das Foto, der Fotoapparat, der Fotograf, die Fotografie, die Freizeit, funktionieren

**Scene 6: Der Hobbykeller**
- Premise: A dad shows off his overstuffed hobby room full of half-finished projects and forgotten instruments.
- Comedic angle: He proudly demonstrates the guitar despite knowing exactly one chord.
- Words (13): der Ball, der Basketball, basteln, die Batterie, die Galerie, die Gitarre, genießen, das Gerät, die/das Glace/Glacé, der Fußball, Golf, das Hobby, hochladen

**Scene 7: Der Technik-Support-Notruf**
- Premise: A grandparent calls for tech help installing an app, describing the problem in wildly wrong terms.
- Comedic angle: The 'broken phone' turns out to just be upside down the whole time.
- Words (13): das Interview, installieren, das Instrument, historisch, die Gymnastik, Bio-, bio, das Handy, das Kabel, die Kamera, die Kassette, klicken, der Klick

**Scene 8: Das Heimkino-Upgrade**
- Premise: A couple assembles a home theater system, arguing over the instructions and mixing up all the cables.
- Comedic angle: The speakers end up playing the neighbor's WiFi-connected doorbell instead of the movie.
- Words (13): das Klavier, das Kino, das Konzert, kopieren, die Kopie, der Kopierer, der Krimi, die Kultur, kulturell, der Künstler / die Künstlerin, künstlich, das Laufwerk, der Lautsprecher

**Scene 9: Die Museumsführung**
- Premise: A overenthusiastic museum guide gives a tour that's more performance art than history lesson.
- Comedic angle: He recites a made-up backstory for a painting that's actually just a fire extinguisher on the wall.
- Words (13): das Klima, die Klimaanlage, die Kunst, das Lexikon, das Lied, die Literatur, das Magazin, malen, der Maler / die Malerin, das Märchen, die Medien, das Museum, die Musik

**Scene 10: Das Konzert im Wohnzimmer**
- Premise: An amateur band records a music video in someone's cramped living room with all borrowed instruments.
- Comedic angle: The drummer keeps hitting the ceiling lamp on every beat.
- Words (13): musikalisch, der Musiker / die Musikerin, der Monitor, die Mobilbox, das Mobiltelefon, die Mappe, das Metall, die Mobilität, die Oper, das Orchester, die Party, organisieren, das Programm

**Scene 11: Die Quizshow-Aufnahme**
- Premise: Friends film their own homemade game show using a hand-drawn wheel and props from around the house.
- Comedic angle: The prize turns out to be a coupon for one free hug, and everyone still wants to win.
- Words (13): der Prospekt, das Publikum, das Quiz, das Radio, der Rekord, das Rätsel, die Phantasie/Fantasie, planen, der Plan, die Planung, reiten, der Saal, der Roman

**Scene 12: Das Vereinsfest**
- Premise: A local sports club throws a chaotic celebration after an unlikely victory.
- Comedic angle: Their trophy is a repurposed pasta jar, and everyone toasts to it as if it were gold.
- Words (13): schwimmen, das Schwimmbad, singen, die Serie, der Ski/Schi, der Sitz, der Karneval, die Metropole, Prost, siegen, der Sieg, der Sieger / die Siegerin, der Spaß

**Scene 13: Der Vereinssporttag**
- Premise: A workplace organizes an awkward team-sports day where nobody remembers the actual rules.
- Comedic angle: The 'referee' makes up new rules on the spot to settle every dispute in the funniest way possible.
- Words (13): der Spiegel, das Spiel, spielen, der Spieler / die Spielerin, der Spielplatz, das Spielzeug, der Sport, die Sportart, der Sportler / die Sportlerin, sportlich, das Stadion, der Star, das Studio

**Scene 14: Der Theaterprobenabend**
- Premise: An amateur theater group rehearses a scene that keeps falling apart because of forgotten lines.
- Comedic angle: The lead actor starts improvising in rhyme just to keep going, and the director loves it too much to stop him.
- Words (13): das Symbol, die Szene, das Talent, tanzen, der Tanz, das Tennis, das Theater, das Thema, die Theorie, das Ticket, die Studie, studieren, das Studium

**Scene 15: Die Stadtführung für Touristen**
- Premise: A tour guide leads visitors past famous landmarks, embellishing every fact more than the last.
- Comedic angle: By the final stop, the 'historic fountain' is apparently haunted by seventeen different ghosts.
- Words (13): die Technik, technisch, die Technologie, die Rolle, die Rose, die Runde, der Salon, das Souvenir, die Station, der Titel, toll, der Tourismus, der Tourist / die Touristin

**Scene 16: Das Fußballtraining**
- Premise: An amateur football coach tries to train a hopeless team using increasingly dramatic sports metaphors.
- Comedic angle: The team's biggest achievement of the day is not falling over during warm-up stretches.
- Words (13): die Tradition, traditionell, trainieren, der Trainer / die Trainerin, das Training, träumen, der Traum, Traum-, der Turm, der Versuch, das Video, virtuell, der Virus

**Scene 17: Der Zirkusbesuch**
- Premise: A family visits a slightly run-down circus with an over-the-top ringmaster.
- Comedic angle: The lion tamer's lion is clearly a very large, very unbothered house cat.
- Words (8): der Wettbewerb, wetten, der Zirkus, der Zoo, der Zuschauer / die Zuschauerin, zuschauen, die Veranstaltung, Volleyball


### Handlungen: Alltagsverben  _212 words, 17 scenes_

**Scene 1 — *Verwaltung, Organisieren & Absprachen*: Die Bürobesprechung**
- Premise: An overly formal office meeting drags on with everyone stalling on trivial administrative details.
- Comedic angle: Someone spends ten minutes debating the correct procedure for booking a meeting room they're already sitting in.
- Words (13): abgeben, abmachen, absagen, abstimmen, bedienen, die Bedienungsanleitung, die Bedingung, beraten, die Beratung, bestätigen, die Bestätigung, bestehen, bestellen

**Scene 2 — *Verwaltung, Organisieren & Absprachen*: Der Kundendienstanruf**
- Premise: A customer service call goes in circles as the agent keeps transferring the caller between departments.
- Comedic angle: By the fourth transfer, the caller is talking to the same person who first picked up.
- Words (13): betreuen, der Betreuer / die Betreuerin, die Betreuung, dienen, einsetzen, einstellen, eintragen, unterbrechen, unternehmen, unterlassen, verpflichtet, verschieben, (sich) vorbereiten

**Scene 3 — *Verwaltung, Organisieren & Absprachen*: Die Steuererklärung**
- Premise: Two roommates try to sort out a joint declaration, arguing over who's responsible for which forms.
- Comedic angle: They accidentally submit each other's tax numbers and spend the rest of the evening panicking.
- Words (14): die Vorbereitung, vorhaben, zusagen, zusammenfassen, unterscheiden, besprechen, die Besprechung, darstellen, die Darstellung, verteilen, umtauschen, der Umtausch, verwenden, warten

**Scene 4 — *Geben, Nehmen & Besitzen*: Der Umzugstag**
- Premise: Friends help someone move apartments, constantly grabbing, carrying, and handing off boxes in a chaotic chain.
- Comedic angle: The heaviest box, labeled 'books', turns out to be full of bricks someone was keeping for no reason.
- Words (13): abheben, abholen, bekommen, benötigen, benutzen, besitzen, besorgen, bringen, geben, gebrauchen, die Gebrauchsanweisung, gehören, greifen

**Scene 5 — *Geben, Nehmen & Besitzen*: Die Rückgabe im Baumarkt**
- Premise: Someone tries to return a broken tool, carrying it awkwardly through the whole store looking for the right counter.
- Comedic angle: The 'broken' tool works perfectly the second the clerk touches it.
- Words (15): halten, der Halt, heben, holen, kriegen, leihen, liefern, die Lieferung, liegen, tragen, treiben, stellen, die Stelle, stecken, hängen

**Scene 6 — *Körperliche Alltagsaktionen*: Der Frühjahrsputz**
- Premise: A family does a chaotic spring cleaning, connecting hoses, printing labels, and losing patience with each other.
- Comedic angle: The dad insists on fixing the printer himself and ends up with more ink on his shirt than the page.
- Words (13): aufhalten, aufheben, anschließen, ausziehen, aufräumen, aufpassen, drehen, drucken, der Drucker, drücken, der Druck, fangen, bleiben

**Scene 7 — *Körperliche Alltagsaktionen*: Der WG-Streit ums Sofa**
- Premise: Roommates fight over a broken sofa, laughing, joking, and living around the mess instead of fixing it.
- Comedic angle: They eventually agree the sofa 'has character' and just cover the hole with a blanket forever.
- Words (13): gehen, heißen, kaputtgehen, kaputtmachen, kaputt, kämpfen, der Kampf, sich kümmern, lächeln, lachen, leben, löschen, machen

**Scene 8 — *Körperliche Alltagsaktionen*: Der Gartentag**
- Premise: A family plants a garden while battling a garden hose that seems to have a mind of its own.
- Comedic angle: The hose sprays everyone except the actual plants, no matter how they aim it.
- Words (13): pflanzen, die Pflanze, schaffen, schalten, schauen, zuschauen, schließen, (sich) schneiden, schneien, schütteln, schützen, der Schutz, sammeln

**Scene 9 — *Körperliche Alltagsaktionen*: Der Sporttag im Park**
- Premise: Friends organize an improvised race and jumping contest in the park, keeping score badly.
- Comedic angle: The self-declared 'winner' clearly fell down halfway through but insists it counts as style points.
- Words (13): (sich) setzen, sinken, schlagen, rennen, schießen, springen, staubsaugen, spülen, stürzen, tauschen, teilen, tauchen, stehlen

**Scene 10 — *Körperliche Alltagsaktionen*: Die Bootsfahrt-Panne**
- Premise: A group tries to escape, dive, and swim their way out of a mishap on a leaky rented rowboat.
- Comedic angle: The 'life jacket' turns out to be a inflatable pool flamingo someone grabbed by mistake.
- Words (13): stinken, (sich) stoßen, treffen, treten, tun, üben, überlegen, übernehmen, verlassen, verlieren, (sich) verstecken, (sich) verstehen, versuchen

**Scene 11 — *Körperliche Alltagsaktionen*: Der Vergleichs-Streit unter Nachbarn**
- Premise: Two neighbors compare, argue, and pack up their yard sale items, trying to out-haggle each other.
- Comedic angle: They end up trading items back and forth so many times neither remembers who owns what anymore.
- Words (13): vermeiden, vergleichen, der Vergleich, verpacken, verschwinden, vergessen, verbringen, verbrauchen, verbinden, die Verbindung, (sich) verbessern, (sich) verbrennen, unterstreichen

**Scene 12 — *Körperliche Alltagsaktionen*: Die Autowäsche**
- Premise: Friends wash a car in the driveway, getting distracted, spraying each other, and forgetting the actual car.
- Comedic angle: By the end the car is cleaner in one spot and filthier everywhere else than when they started.
- Words (13): vergeblich, verzichten, (sich) waschen, wechseln, sich weigern, weinen, wenden, werfen, wiegen, winken, ziehen, zugehen, zumachen

**Scene 13 — *Körperliche Alltagsaktionen*: Die Wanderung mit Hindernissen**
- Premise: A hiking group stumbles, stops, and struggles up a hill that turns out to be much steeper than the map showed.
- Comedic angle: The self-appointed 'guide' gets lost twice using his own compass.
- Words (8): zunehmen, zurechtkommen, wehtun, stehen, stehen bleiben, steigen, stoppen, stören

**Scene 14 — *Bemühen, Wandel & Reaktion*: Der Renovierungsversuch**
- Premise: A couple tries fixing up an old apartment, changing plans mid-project and abandoning half-finished tasks.
- Comedic angle: The 'accent wall' ends up three different colors because nobody could agree and nobody wanted to repaint it.
- Words (13): ändern, die Änderung, anfangen, aufhören, aufladen, ausmachen, sich bemühen, beschränken, beschreiben, die Beschreibung, behalten, behandeln, der Beitrag

**Scene 15 — *Bemühen, Wandel & Reaktion*: Die verspätete Rückkehr**
- Premise: Someone tries to make it home in time for dinner, juggling errands that keep piling up.
- Comedic angle: They arrive just as everyone else has finished eating and gone to bed.
- Words (13): klagen, entfernen, ersetzen, der Ersatz, gelingen, integrieren, die Integration, helfen, die Hilfe, sorgen, die Sorge, sparen, sparsam

**Scene 16 — *Bemühen, Wandel & Reaktion*: Die Reparaturwerkstatt**
- Premise: A DIY enthusiast tries fixing a broken appliance, changing his approach every five minutes.
- Comedic angle: He ends up with more screws left over than the appliance originally had.
- Words (10): spazieren gehen, der Spaziergang, suchen, reduzieren, protestieren, der Protest, abnehmen, beobachten, berechnen, retten

**Scene 17 — *Dank, Auftritt & Ausdruck*: Die Rettungsaktion**
- Premise: Neighbors help rescue a cat stuck in a tree, taking turns and calling for backup.
- Comedic angle: The fire department arrives just as the cat casually climbs down on its own, unbothered.
- Words (9): danken, der Dank, dankbar, danke, dekorieren, bieten, bitten, die Bitte, brauchen


### Denken, Wissen & Meinen  _162 words, 12 scenes_

**Scene 1 — *Meinen, Wissen & Überzeugen*: Der Debattierclub**
- Premise: An amateur debate club argues about a trivial topic as if the fate of the world depended on it.
- Comedic angle: Nobody actually knows what the original topic was anymore by round three.
- Words (13): meinen, die Meinung, glauben, wissen, das Wissen, die Wissenschaft, der Wissenschaftler / die Wissenschaftlerin, wahr, die Wahrheit, wichtig, widersprechen, wirklich, die Wirklichkeit

**Scene 2 — *Meinen, Wissen & Überzeugen*: Die Gerichtsshow-Parodie**
- Premise: Friends stage a mock trial over who ate the last slice of cake, complete with dramatic evidence.
- Comedic angle: The 'evidence' is a single crumb, presented as if it were a smoking gun.
- Words (13): der Zweifel, zweifeln, zustimmen, die Zustimmung, vermuten, vernünftig, das Verständnis, akzeptieren, bekannt, bemerken, sich irren, beweisen, der Beweis

**Scene 3 — *Meinen, Wissen & Überzeugen*: Der Wissenschaftskongress im Kleinformat**
- Premise: A neighborhood science fair features wildly overconfident presentations of very small discoveries.
- Comedic angle: One 'researcher' presents his conclusion that his cat prefers Tuesdays, with full slideshow.
- Words (12): begründen, die Begründung, ordentlich, realisieren, die Realität, reagieren, die Reaktion, ausschließen, ausschließlich, annehmen, genehmigen, gelten

**Scene 4 — *Entscheiden, Planen & Feststellen*: Die Familienabstimmung**
- Premise: A family votes on where to go for vacation, and the decision keeps flip-flopping every five minutes.
- Comedic angle: The dog's random bark is treated as the deciding vote.
- Words (13): entscheiden, die Entscheidung, unentschieden, sich entschließen, entschlossen, beschließen, sich einigen, wählen, die Wahl, die Voraussetzung, der Unterschied, vorkommen, festhalten

**Scene 5 — *Entscheiden, Planen & Feststellen*: Der Strategie-Brettspielabend**
- Premise: Friends plan an elaborate board game strategy, listing every possible outcome out loud.
- Comedic angle: Their meticulous plan collapses the instant someone rolls the wrong number.
- Words (18): festlegen, feststehen, feststellen, finden, folgen, die Folge, folgend, führen, beachten, beschäftigen, die Beschäftigung, die Art, auflösen, die Reihenfolge, die Reihe, reichen, das Ziel, der Zustand

**Scene 6 — *Erinnern, Entdecken & Verstehen*: Das Klassentreffen der Erinnerungen**
- Premise: Old classmates reunite and try to remember shared stories, each recalling a wildly different version.
- Comedic angle: Nobody can agree who actually won the legendary sack race from twenty years ago.
- Words (13): der Gedanke, denken, erinnern, die Erinnerung, erkennen, entdecken, erfinden, die Erfindung, erwarten, nachdenken, nachschlagen, kennen, kennenlernen

**Scene 7 — *Erinnern, Entdecken & Verstehen*: Die Schatzsuche im Dachboden**
- Premise: Someone rummages through the attic, discovering strange objects and inventing backstories for each.
- Comedic angle: A mysterious key turns out to open nothing more exciting than an old bike lock.
- Words (17): die Kenntnisse, merken, merkwürdig, sich nähern, die Nähe, das Geheimnis, geheim, die Herkunft, der Inhalt, gründlich, sichtbar, scheinen, der Schein, seltsam, typisch, der Typ, der Tipp

**Scene 8 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Verschwörungstheorie am Stammtisch**
- Premise: Friends at a regular pub table build an increasingly elaborate, silly conspiracy theory about a local shop closing early.
- Comedic angle: The 'evidence' keeps growing more absurd until someone points out the shop is just closed for holiday.
- Words (13): abhängen, abhängig, die Ahnung, ablehnen, die Absicht, achten, auffallen, aufmerksam, die Alternative, alternativ, die Ausnahme, der Bescheid, Bescheid sagen

**Scene 9 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Konferenzraum-Verwirrung**
- Premise: A negotiation between two small business owners spirals into confused compromise proposals.
- Comedic angle: They end up agreeing to something neither of them actually wanted, just to end the meeting.
- Words (13): Bescheid geben, die Distanz, doch, der Eindruck, einerseits, einfallen, der Einfall, der Einfluss, beeinflussen, der Faktor, fassen, der Kompromiss, die Konferenz

**Scene 10 — *Streit, Absicht & Gemütslage (abstrakt)*: Der Lügendetektor-Abend**
- Premise: Friends play a party game trying to spot each other's lies, getting suspicious over everything.
- Comedic angle: Someone's true statement gets voted 'obviously a lie' just because it sounded too weird to be real.
- Words (13): die Konkurrenz, die Lage, die Liste, die Lösung, lösen, die Lüge, lügen, die Methode, mischen, die Nachfrage, die Nachricht, das Problem, der Respekt

**Scene 11 — *Streit, Absicht & Gemütslage (abstrakt)*: Das Risikospiel**
- Premise: A group debates whether to try a slightly risky activity, weighing pros and cons dramatically.
- Comedic angle: The most cautious person of the group ends up being the first to jump in.
- Words (13): das Risiko, sinnlos, sinnvoll, der Sinn, schätzen, die Rücksicht, die Situation, der/dasObers, die Stimmung, die Tat, die Tatsache, die Störung, (sich) überzeugen

**Scene 12 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Wettervorhersage-Zweifel**
- Premise: Friends argue about whether to trust the forecast for a planned outdoor event.
- Comedic angle: They end up bringing every possible weather item and using none of them because it's perfectly sunny.
- Words (11): die Überzeugung, überraschen, die Überraschung, das Verhalten, sich verhalten, das Verhältnis, die Praxis, das Gewissen, geschehen, bewegen, der Zusammenhang


### Einkaufen & Geld  _135 words, 10 scenes_

**Scene 1: Der Ausverkaufstag**
- Premise: Shoppers scramble through a chaotic sale, grabbing discounted items faster than they can decide if they want them.
- Comedic angle: Two strangers end up in a polite but intense tug-of-war over the same discounted lamp.
- Words (13): abheben, die Abteilung, die Aktion, anbieten, der Anbieter, das Angebot, anschaffen, die Ausgabe, ausgeben, die Ausnahme, aussuchen, auswählen, die Auswahl

**Scene 2: Die Wochenendeinkäufe**
- Premise: A family does the weekly grocery run on a tight budget, calculating every item's cost out loud.
- Comedic angle: Dad's strict budgeting collapses the second he sees the bakery section.
- Words (13): der Automat, bezahlen, der Betrag, billig, bitter, der Bogen, die Bohne, das Benzin, das Bargeld, bar, einführen, die Einführung, einkaufen

**Scene 3: Der erste Gehaltscheck**
- Premise: A new employee obsessively checks their bank account after receiving their first paycheck.
- Comedic angle: They immediately spend it all on something wildly impractical out of sheer excitement.
- Words (13): der Einkauf, das Einkommen, einnehmen, die Einnahme, einzahlen, die Einzahlung, erhalten, erhöhen, die Erhöhung, die Ermäßigung, eröffnen, die Eröffnung, finanzieren

**Scene 4: Die verwirrende Bankfiliale**
- Premise: Someone tries to open an account and gets lost in an endless maze of forms and machines.
- Comedic angle: The ATM eats the card, the counter sends them back to the ATM, and the loop never ends.
- Words (13): finanziell, der Flohmarkt, die Anlage, die Bank, die Bank, der Bancomat/Bankomat, die Bankleitzahl, die Bankomat-Karte, die Gebühr, das Geld, der Geldautomat, die Geldbörse, der Gewinn

**Scene 5: Der Flohmarktverkäufer**
- Premise: An overenthusiastic flea-market seller haggles wildly with every browsing customer.
- Comedic angle: He gives a heartfelt sales pitch for an obviously broken toaster as if it were a family heirloom.
- Words (13): gewinnen, das Geschäft, günstig, das Gold, garantieren, die Garantie, gratis, die Karte, die Chipkarte, die Fahrkarte, die Kasse, der Katalog, kaufen

**Scene 6: Der Kreditkartenschock**
- Premise: Someone opens their credit card statement and is horrified by a mysterious huge purchase.
- Comedic angle: It turns out to be their own forgotten online order from three months ago.
- Words (13): der Kauf, der Käufer / die Käuferin, kostenlos, der Kredit, die Kreditkarte, das Konto, das Girokonto, kontrollieren, die Kontrolle, die Kosten, kosten, kosten, der Konsum

**Scene 7: Der Möbelmarkt-Vergleich**
- Premise: A couple compares prices between two furniture stores, debating every euro of difference.
- Comedic angle: They spend more time and money on coffee while deciding than they save on the actual furniture.
- Words (13): konsumieren, der Kasten, der Kasten, der Laden, die Marke, markieren, der Markt, maximal, die Mehrwertsteuer, der Mieter / die Mieterin, mieten, die Miete, die Münze

**Scene 8: Die Onlinebestellung geht schief**
- Premise: A customer tracks a delayed package obsessively, refreshing the tracking page every five minutes.
- Comedic angle: The package arrives completely crushed, containing a single, oddly undamaged rubber duck.
- Words (13): das Paket, der Preis, produzieren, das Produkt, die Produktion, der Rabatt, rechnen, der Rechner, die Rechnung, die Quittung, das Portemonnaie/Portmonee, das Sonderangebot, der Supermarkt

**Scene 9: Die Steuerprüfung im Supermarkt**
- Premise: Someone tallies receipts at the supermarket checkout, trying to stay under a strict weekly budget.
- Comedic angle: The final total is one cent over, and they have to put back a single item under everyone's judging eyes.
- Words (13): die Summe, die Statistik, statistisch, die Steuer, der Test, testen, die Tasche, das Taschengeld, die Tabelle, verkaufen, der Verkäufer / die Verkäuferin, vermieten, der Vermieter / die Vermieterin

**Scene 10: Der Mietvertrag-Papierkram**
- Premise: A tenant signs a new lease, drowning in insurance, deposit, and payment paperwork.
- Comedic angle: They accidentally sign up for a service they never wanted just from clicking through forms too fast.
- Words (18): die Vermietung, die Versicherung, versichern, die Versichertenkarte, die Vermittlung, der Verlust, überweisen, die Überweisung, der Vertrag, zahlen, die Zahlung, zählen, die Zinsen, der Zoll, der Zuschlag, die Ware, der Zucker, die Zutaten


### Menge, Maß & Eigenschaften  _164 words, 13 scenes_

**Scene 1 — *Größe, Form & Menge*: Der Möbelmess-Fehler**
- Premise: Someone measures a new wardrobe against the doorway, insisting it will 'definitely' fit.
- Comedic angle: It gets stuck at a comically awkward angle, blocking the hallway for the whole afternoon.
- Words (13): groß, Groß-, die Größe, klein, breit, die Breite, dick, dicht, eng, hoch, die Höhe, tief, schmal

**Scene 2 — *Größe, Form & Menge*: Der Wettbewerb um die größte Kürbis**
- Premise: Neighbors compete in an amateur giant-vegetable growing contest, obsessing over every centimeter.
- Comedic angle: The 'winning' pumpkin turns out to be mostly held together with tape after a fall.
- Words (13): rund, eckig, spitz, steil, riesig, die Menge, die Gruppe, messen, das Mal, mal, Einzel-, einzeln, einzig-

**Scene 3 — *Größe, Form & Menge*: Die Inventur im Lagerhaus**
- Premise: Warehouse workers do a chaotic stock count, constantly losing track of the total.
- Comedic angle: They recount the same box four times because someone kept moving it while counting.
- Words (8): sämtliche, die Einzelheit, insgesamt, minimal, die Leiter, das Mittel, der Gegenstand, das Ding

**Scene 4 — *Qualität & Bewertung*: Die Bewertungsshow**
- Premise: Friends host a mock talent show, giving overly dramatic, contradictory reviews of each act.
- Comedic angle: The 'perfect score' judge and the 'harshest critic' turn out to be scoring completely different performances by accident.
- Words (13): gut, schlecht, schlimm, ausgezeichnet, perfekt, ideal, praktisch, preiswert, prima, super, positiv, optimistisch, realistisch

**Scene 5 — *Qualität & Bewertung*: Der Wertschätzungsstreit im Antiquitätenladen**
- Premise: A shop owner and a customer argue over whether an old vase is priceless or worthless.
- Comedic angle: It turns out to be a cheap souvenir, but both refuse to back down out of pure stubbornness.
- Words (13): original, das Original, echt, die Qualität, wertlos, wertvoll, wert, der Wert, nützlich, nötig, notwendig, erforderlich, erfordern

**Scene 6 — *Qualität & Bewertung*: Der Fitnesstest**
- Premise: Friends attempt an informal strength and endurance test in the park, judging each other's fairness.
- Comedic angle: The self-proclaimed fittest one is out of breath after the warm-up alone.
- Words (9): gültig, haltbar, streng, der Vorteil, tolerant, die Fähigkeit, fair, gerecht, gleichberechtigt

**Scene 7 — *Grad & Vergleich*: Die Umfrage in der Fußgängerzone**
- Premise: A market researcher surveys passersby, comparing answers that all somehow contradict each other.
- Comedic angle: The 'average' answer ends up being something nobody actually said.
- Words (13): absolut, allgemein, ähnlich, all-, aller-, ander-, andererseits, anders, besonder-, besonders, bestimmt, deutlich, durchschnittlich

**Scene 8 — *Grad & Vergleich*: Die statistische Wette**
- Premise: Friends bet on percentages and averages during a football match, arguing over vague estimates.
- Comedic angle: Their 'exact calculations' turn out to be completely made up on the spot.
- Words (13): der Durchschnitt, eindeutig, einheitlich, einig-, einfach, gering, genug, genügen, ausreichend, ausreichen, umgekehrt, höchstens, unterschiedlich

**Scene 9 — *Grad & Vergleich*: Der Übertreibungswettbewerb**
- Premise: Friends compete over who can tell the most exaggerated story about their weekend.
- Comedic angle: The most unbelievable story turns out to be completely true, to everyone's shock.
- Words (17): verschieden, vergrößern, verlängern, verwechseln, total, übertreiben, ungewöhnlich, unglaublich, unheimlich, verständlich, ziemlich, zahlreich, regional, stilistisch, -weise, vorwärts, senkrecht

**Scene 10 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Materialtest im Baumarkt**
- Premise: A DIYer tests different materials' toughness by hitting, bending, and dropping samples in the aisle.
- Comedic angle: He accidentally proves the display shelf itself is the weakest material in the store.
- Words (13): hart, weich, stark, schwach, schwer, die Schwierigkeit, schwierig, bequem, kräftig, knapp, klug, intelligent, die Intelligenz

**Scene 11 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Geschwindigkeitswettstreit**
- Premise: Friends race shopping carts through an empty parking lot, timing each other dramatically.
- Comedic angle: The 'fastest' one crashes spectacularly into a row of stacked crates at the finish line.
- Words (13): intensiv, individuell, häufig, schnell, scharf, spannend, teuer, der Satz, treu, wild, zuverlässig, zufrieden, wahnsinnig

**Scene 12 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Charaktertest beim Speeddating**
- Premise: At a speed-dating event, participants describe themselves using only vague personality adjectives.
- Comedic angle: Two people describe themselves identically and realize they're actually siblings.
- Words (13): weiblich, reif, reich, das Gewicht, der Gegensatz, das Tempo, voll, schief, hübsch, pauschal, korrigieren, leise, mündlich

**Scene 13 — *Charakter von Dingen (Konsistenz & Tempo)*: Die Gewohnheitsdebatte am Frühstückstisch**
- Premise: A couple argues gently over morning routines and small habits neither wants to change.
- Comedic angle: They discover after years together neither actually likes the habit they were defending.
- Words (13): eher, ehrlich, der Bedarf, die Entfernung, enthalten, flexibel, die Gewohnheit, gewohnt, gewöhnlich, gewöhnen, furchtbar, bunt, schlank


### In der Wohnung & Zuhause  _153 words, 12 scenes_

**Scene 1: Der Einzugstag**
- Premise: Someone moves into a new, mostly empty apartment, cheerfully naming every room out loud like a tour guide.
- Comedic angle: The 'apartment tour' for a single friend takes twenty minutes because they insist on describing the closet too.
- Words (13): der Abfall, der Abfalleimer, abwaschen, der Abwart / die Abwartin, die Anleitung, der Aufzug, außen, ausmachen, das Apartment, das Bett, der Bau, bauen, die Baustelle

**Scene 2: Die improvisierte Küche**
- Premise: A cramped student apartment's kitchen doubles as living room, with furniture crammed wherever it fits.
- Comedic angle: The couch and the fridge are pushed so close together that opening either requires teamwork.
- Words (13): das Blatt, der Boden, das Brot, die Decke, die Bürste, die Zahnbürste, die Couch, die Ecke, das Eck, einrichten, die Einrichtung, die Etage, das Fenster

**Scene 3: Der Balkon-Pooltag**
- Premise: Neighbors improvise a tiny inflatable pool on a cramped balcony during a heatwave.
- Comedic angle: The garden hose fills it just as someone below opens their window directly underneath.
- Words (13): die Flasche, der Flur, baden, das Bad, die Badewanne, der Balkon, die Bar, der Garten, das Geschirr, besetzen, das Dach, der Eingang, die Garage

**Scene 4: Die Heizungsreparatur**
- Premise: A landlord tries to fix a broken heater himself instead of calling a professional.
- Comedic angle: He ends up needing the actual repairman anyway, plus a new toolbox after breaking most of the old one.
- Words (13): der Herd, das Haus, der Haushalt, der Hausmeister / die Hausmeisterin, das Heim, die Heizung, heizen, die Büchse, die Dose, die Garderobe, das Glas, der Hammer, das Heft

**Scene 5: Der Dachbodenfund**
- Premise: Someone clears out a cluttered attic and stumbles on a chair so old it might be an antique.
- Comedic angle: It collapses the moment anyone actually sits on it.
- Words (13): der Fauteuil, die Halle, das Holz, die Hütte, das Kissen, die Kerze, der Keller, der Kühlschrank, die Lampe, das Lager, legen, der Kugelschreiber, der Kuli

**Scene 6: Der Frühjahrsputz-Marathon**
- Premise: A roommate deep-cleans the whole apartment in one obsessive afternoon.
- Comedic angle: They find three missing spoons, one shoe, and no explanation for either.
- Words (13): der Korridor, die Küche, das Licht, das Möbel, möbliert, der Müll, die Müllabfuhr, die Mülltonne, die Nadel, der Nagel, locker, das Loch, der Löffel

**Scene 7: Das Möbelaufbau-Chaos**
- Premise: Two friends try assembling flatpack furniture without reading the instructions.
- Comedic angle: The finished 'bookshelf' looks suspiciously like a wobbly ladder.
- Words (13): das Messer, die Mitte, nähen, derOfen, öffnen, der Ordner, ordnen, die Ordnung, packen, das Papier, putzen, die Puppe, das Plastik

**Scene 8: Der Frühlingsputz im Wohnzimmer**
- Premise: A family reorganizes the living room, disagreeing about furniture placement the whole afternoon.
- Comedic angle: By evening the room is back in almost the exact same layout it started in.
- Words (13): das Regal, reinigen, die Reinigung, der Platz, der Rand, der Raum, der Sack, sauber, die Schere, die Scheibe, der Schirm, der Schlaf, schlafen

**Scene 9: Der Schlüsselverlust**
- Premise: Someone locks themselves out and has to improvise entry through increasingly ridiculous methods.
- Comedic angle: The spare key turns out to have been in their pocket the entire time.
- Words (13): der Schlüssel, schmutzig, der Schmutz, der Schrank, die Schüssel, das Sofa, die Socke, das Schild, das Schloss, die Schachtel, das Stiegenhaus, die Stiege, der Stock

**Scene 10: Der gemütliche Fernsehabend**
- Premise: Friends gather in a living room stuffed with mismatched furniture for movie night.
- Comedic angle: Someone insists the ancient, creaky armchair is 'the good one' and fights anyone who sits in it.
- Words (13): das Stockwerk, der Stuhl, der Teppich, die Terrasse, der Staub, das Streichholz, der Tisch, der Sessel, der Sessel, der Stift, der Stoff, die Tafel, der Topf

**Scene 11: Der Umzugswagen**
- Premise: A family loads a moving truck, arguing over how to fit oversized furniture through narrow doors.
- Comedic angle: The wardrobe barely fits by being tilted at an almost comedic forty-five-degree angle.
- Words (13): die Vase, die Treppe, das Treppenhaus, die Tür, das Tuch, die Uhr, umziehen, der Umzug, sich umziehen, das Tor, die Wand, das Wasser, die Wäsche

**Scene 12: Das neue Zuhause**
- Premise: After a long move, someone finally relaxes in their new, freshly organized living room.
- Comedic angle: They immediately can't find a single box labeled correctly among the fifty they packed.
- Words (10): das Waschmittel, die Wohnung, das Wohnzimmer, das Zimmer, der Zettel, wohnen, zentral, das Zentrum, das Zuhause, der Zugang


### Natur, Wetter & Umwelt  _107 words, 8 scenes_

**Scene 1: Der Gewitter-Campingausflug**
- Premise: Campers set up a tent just as dark clouds roll in over a riverside meadow.
- Comedic angle: The tent collapses the second the first raindrop hits, in front of a very unimpressed audience of ducks.
- Words (13): Abgase, der Baum, blühen, die Blume, blitzen, der Blitz, die Birne, das Dorf, draußen, der Dreck, die Energie, entsorgen, die Erde

**Scene 2: Der Bauernhofbesuch**
- Premise: City kids visit a farm and are baffled by basic country facts everyone else takes for granted.
- Comedic angle: One insists the potatoes 'grow on trees' until the farmer patiently digs one up to prove otherwise.
- Words (13): der Erdapfel, das Erdgeschoss/ Ergeschoß, das Feld, feucht, das Feuer, das Feuerzeug, die Feuerwehr, flach, die Fläche, fließen, fließend, der Fluss, die Flüssigkeit

**Scene 3: Die Bergwanderung mit Aussicht**
- Premise: Hikers finally reach a mountain viewpoint after a long climb, awestruck by the view.
- Comedic angle: The view is immediately ruined by a cloud rolling in the second everyone gets their camera out.
- Words (13): die Frucht, Früchte, die Aussicht, der Berg, das Gewitter, die Gegend, das Gras, hageln, der Himmel, die Hitze, der Hügel, die Insel, heiß

**Scene 4: Die Autopanne auf dem Land**
- Premise: A car breaks down on a rural road near a harbor town, and the driver has to improvise repairs.
- Comedic angle: The 'repair' involves duct tape, a farmer's advice, and a suspicious amount of luck.
- Words (13): brennen, das Gas, der Hafen, glatt, das Grundstück, der Kanal, das Land, die Landschaft, die Landwirtschaft, kalt, die Kälte, der Lärm, der Kunststoff

**Scene 5: Die Seefahrt bei Nebel**
- Premise: A small boat trip gets eerily foggy, and the crew navigates mostly by guesswork and superstition.
- Comedic angle: They 'discover' a mysterious island that turns out to be the same dock they left from.
- Words (13): das Leder, leer, die Luft, das Meer, der Mond, die Natur, der Nebel, neblig, nass, der Ozean, der Rasen, regnen, der Regen

**Scene 6: Der Strandtag mit Überraschungen**
- Premise: A beach day turns chaotic as the tide comes in faster than anyone expected.
- Comedic angle: Someone's sandcastle empire is swallowed by the sea mid-victory-speech.
- Words (13): die Region, das Öl, Öko-, das Rind, der See, die See, die Nord-/Ostsee, der Schnee, schneien, der Sand, der Schatten, verschmutzen, die Sonne

**Scene 7: Die Sternennacht im Tal**
- Premise: Friends camp in a valley and try (badly) to identify constellations.
- Comedic angle: Every single 'star' they point at turns out to be a distant airplane.
- Words (13): sonnig, der Stern, der Sturm, das Tal, der Stein, der Strand, der Strom, das Ufer, die Umgebung, die Umwelt, der Umweltschutz, die Umweltverschmutzung, trocken

**Scene 8: Der plötzliche Wetterumschwung**
- Premise: A picnic gets abruptly interrupted by wind and clouds rolling in from nowhere.
- Comedic angle: The tablecloth becomes an impromptu kite, sailing off with half the sandwiches still on it.
- Words (16): trocknen, der Wald, wandern, die Wanderung, die Wärme, warm, das Wetter, der Wetterbericht, die Wettervorhersage, der Wind, windig, die Wiese, die Wolke, bewölkt, die Wolle, zerstören


### Familie & Beziehungen  _107 words, 8 scenes_

**Scene 1: Das Familientreffen im Altersheim**
- Premise: Several generations gather to visit a grandparent, and everyone tells wildly different versions of family history.
- Comedic angle: The grandmother insists she remembers everyone's age wrong, on purpose, just to see their reactions.
- Words (13): der Angehörige / die Angehörige, alt, das Alter, das Altenheim, das Altersheim, die Beziehung, der Bewohner / die Bewohnerin, die Bevölkerung, der Bruder, der Bub, der Chef / die Chefin, die Dame, der Coiffeur / die Coiffeuse

**Scene 2: Die Hochzeitsvorbereitung**
- Premise: A couple's engaged relatives argue over wedding invitations and seating charts for cousins nobody's met.
- Comedic angle: The seating chart ends up requiring a whiteboard the size of a door.
- Words (13): der Cousin / die Cousine, die Ehe, die Ehefrau, das Ehepaar, einladen, die Einladung, einziehen, die Eltern, der Enkel / die Enkelin, erwachsen, der Erwachsene, erziehen, die Erziehung

**Scene 3: Die Geburtstagsüberraschung**
- Premise: Friends plan a surprise party but keep almost giving it away through terrible acting.
- Comedic angle: The 'surprised' birthday person had actually known for a week and pretends convincingly anyway.
- Words (13): die Familie, der Familienstand, die Frau, der Freund, die Freundschaft, freundlich, der Bekannte / die Bekannte, geboren werden, die Geburt, der Geburtstag, das Geschenk, die Geschwister, geschieden

**Scene 4: Die Jugendliebe-Geschichte**
- Premise: An older relative tells an embellished story about their teenage romance at a family dinner.
- Comedic angle: Every retelling adds a new dramatic detail that definitely wasn't there the first time.
- Words (13): die Hausfrau / der Hausmann, heiraten, die Heimat, die Hochzeit, der Held / die Heldin, heimlich, das Heimweh, der Hof, die Jugend, der Jugendliche / die Jugendliche, jung, der Junge, das Kind

**Scene 5: Der erste Kindergartentag**
- Premise: Parents nervously drop off their child at kindergarten for the first time.
- Comedic angle: The child is completely fine; it's the parents who need consoling in the parking lot.
- Words (13): die Kindheit, der Kindergarten, die Jugendherberge, küssen, der Kuss, die Leute, das Mädchen, der Mann, männlich, die Mutter, der Name, der Familienname, der Vorname

**Scene 6: Die Großfamilien-Reise**
- Premise: A sprawling extended family plans a group trip and can't agree on anything.
- Comedic angle: The final itinerary satisfies literally nobody but somehow makes everyone equally happy about that.
- Words (13): der Neffe, die Nichte, der Nachwuchs, die Oma, der Onkel, der Opa, der Partner / die Partnerin, das Paar, der Nichtraucher / die Nichtraucherin, die Person, persönlich, die Rente, in Rente gehen/sein

**Scene 7: Die Rentnerclub-Runde**
- Premise: Retirees gather weekly, gently teasing each other about health, memory, and old family gossip.
- Comedic angle: Nobody can actually remember what the running joke was originally about, but they laugh anyway.
- Words (13): der Rentner / die Rentnerin, die Senioren, der Sohn, die Schwester, Schwieger-, die Schwangerschaft, sich scheiden lassen, geschieden, die Scheidung, schenken, die Tante, die Tochter, der Vater

**Scene 8: Die Versöhnung nach dem Streit**
- Premise: A couple works through a small disagreement, over-apologizing in increasingly formal language.
- Comedic angle: The 'serious conflict' turns out to be about whose turn it was to walk the dog.
- Words (16): (sich) verabreden, verabredet, die Verabredung, (sich) verabschieden, der Abschied, (sich) verändern, verantwortlich, die Verantwortung, verheiratet, (sich) trennen, die Trennung, getrennt leben, verwandt, der Verwandte / die Verwandte, der Wirt / die Wirtin, (sich) zwingen


### Gefühle & Charakter  _122 words, 9 scenes_

**Scene 1: Die Achterbahnfahrt**
- Premise: Friends line up for a rollercoaster, each reacting to the fear in a wildly different way.
- Comedic angle: The one who claimed to be fearless screams the loudest the entire ride.
- Words (13): die Angst, ängstlich, angenehm, allein, aktiv, (sich) ärgern, der Ärger, ärgerlich, arm, beleidigen, beruhigen, betrunken, die Bewegung

**Scene 2: Der peinliche Vorstellungsgesprächs-Traum**
- Premise: Someone recounts an embarrassing dream about a disastrous job interview at breakfast.
- Comedic angle: Everyone at the table admits they've had the exact same anxiety dream, in painfully specific detail.
- Words (13): begeistert, blass, böse, dumm, dankbar, dringend, sich eignen, geeignet, eilen, die Eile, eilig, einsam, entspannend

**Scene 3: Die enttäuschte Kochshow**
- Premise: An amateur cook's ambitious dinner party dish collapses spectacularly right before guests arrive.
- Comedic angle: The backup plan, ordering pizza, turns out to be the guests' favorite part of the evening.
- Words (13): enttäuschen, die Enttäuschung, erleichtern, ernst, ernsthaft, faul, faulenzen, fliehen, die Flucht, frech, froh, fröhlich, frieren

**Scene 4: Der Trostpreis**
- Premise: A friend loses a minor competition and everyone tries clumsily to cheer them up.
- Comedic angle: The 'consolation gift' is so absurd it accidentally becomes the highlight of their week.
- Words (13): sich freuen, die Freude, der Friede, fühlen, aufregen, befreit, befriedigend, begrenzt, beißen, bereit, berühmt, gefallen, sich etwas gefallen lassen

**Scene 5: Die Dankesrede**
- Premise: Someone gives an overly emotional thank-you speech at a small local award ceremony.
- Comedic angle: They get so choked up over a minor certificate that people start crying along out of secondhand emotion.
- Words (13): geehrt, gespannt, gemütlich, (sich) fürchten, glücklich, das Glück, hassen, herzlich, höflich, hoffen, hoffentlich, die Hoffnung, interessieren

**Scene 6: Der Kritikerclub**
- Premise: Friends review a terrible amateur film with theatrical, contradictory opinions.
- Comedic angle: The harshest critic turns out to be an uncredited extra in the film.
- Words (13): interessant, das Interesse, interessiert, klasse, kreativ, kritisieren, die Kritik, kritisch, die Laune, ledig, leicht, leider, der Kellner / die Kellnerin

**Scene 7: Die Liebeserklärung im Regen**
- Premise: Someone plans a big romantic gesture that gets rained out and ruined step by step.
- Comedic angle: The soggy, disastrous version ends up being more memorable than the perfect plan ever would have been.
- Words (13): die Lust, lustig, lieben, lieb, die Liebe, sich lohnen, neugierig, loben, peinlich, das Pech, schade, schaden, der Schaden

**Scene 8: Der Streit im Fahrstuhl**
- Premise: Two strangers get stuck in an elevator and slowly go from annoyed to oddly bonded.
- Comedic angle: By the time they're rescued, they've become unlikely best friends and exchange numbers.
- Words (13): der Schreck, schrecklich, die Ruhe, ruhig, stolz, still, sympathisch, traurig, verliebt, sich verlieben, verrückt, vergnügt, sich vergnügen

**Scene 9: Die Wunschliste ans Universum**
- Premise: Friends write silly wish lists for the new year, half-joking, half-serious.
- Comedic angle: The most ridiculous wish on the list is the only one that actually comes true by year's end.
- Words (18): das Vergnügen, das Unglück, der Verlierer / die Verliererin, vertrauen, das Vertrauen, wach, wütend, wunderbar, wunderschön, sich wundern, das Wunder, (sich) wünschen, der Wunsch, willkommen, wirken, die Wirkung, die Vorsicht, vorsichtig


### Kommunikation & Post  _177 words, 14 scenes_

**Scene 1: Der falsch adressierte Brief**
- Premise: Someone writes an angry letter to their landlord but sends it to the wrong address entirely.
- Comedic angle: The actual recipient, a stranger, writes back a genuinely helpful reply anyway.
- Words (13): die Adresse, der Absender / die Absenderin, ankündigen, ansprechen, antworten, die Antwort, anrufen, der Anruf, der Anrufbeantworter, die Ansage, die Annonce, die Anrede, ausrichten

**Scene 2: Die Anrufbeantworter-Odyssee**
- Premise: Someone leaves an increasingly rambling voicemail after being cut off mid-sentence multiple times.
- Comedic angle: The final voicemail is just them saying 'call me back' forty different ways.
- Words (13): die Auskunft, der Apparat, ausdrucken, der Ausdruck, beantworten, sich beschweren, die Botschaft, der Brief, der Briefkasten, die Briefmarke, der Briefträger, der Briefumschlag, die Brieftasche

**Scene 3: Der Buchstabierwettbewerb am Telefon**
- Premise: Someone tries to spell their complicated last name to a call center agent using the phonetic alphabet, badly.
- Comedic angle: Their invented code words ('B wie Banane') confuse the agent more than actual letters would.
- Words (13): buchstabieren, der Buchstabe, die Durchsage, duzen, die e-card, die ec-Karte/EC-Karte, das Einschreiben, empfangen, der Empfang, der Empfänger, empfehlen, die Empfehlung, entschuldigen

**Scene 4: Die Entschuldigungskarte**
- Premise: A student writes an elaborate excuse note explaining a missed deadline.
- Comedic angle: The excuse is so overly detailed and dramatic that the teacher suspects it's fiction and grades it as a short story instead.
- Words (13): die Entschuldigung, sich erkundigen, erlauben, die Erlaubnis, erzählen, die Erzählung, fragen, die Frage, auffordern, die Aufforderung, begegnen, der Artikel, bedeuten

**Scene 5: Die Glückwunschkarten-Fabrik**
- Premise: A family mass-produces greeting cards for every relative's birthday in one chaotic afternoon.
- Comedic angle: They run out of good wishes and start writing increasingly absurd compliments by card fifteen.
- Words (13): die Bedeutung, begrüßen, behaupten, das Gespräch, aktuell, der Ausdruck, sich bedanken, die Grafik, gratulieren, die Gratulation, der Glückwunsch, grüßen, der Gruß

**Scene 6: Der Radiomoderator im Praktikum**
- Premise: A nervous intern hosts their first live radio segment, stumbling over every hint and cue card.
- Comedic angle: Dead air strikes at the worst moment, filled only by his own audible panic breathing.
- Words (13): hinweisen, der Hinweise, hallo, der Humor, der Hörer / die Hörerin / der Zuhörer, hören, das Inserat, sich beeilen, die Idee, informieren, die Information, der Journalist / die Journalistin, klingeln

**Scene 7: Die Reklamations-Hotline**
- Premise: Someone calls customer support, getting passed between departments over a minor complaint.
- Comedic angle: By the third transfer they're talking to someone in a completely unrelated company.
- Words (13): die Klingel, klingen, klopfen, die Kommunikation, der Kontakt, sich konzentrieren, das Kuvert, melden, die Meldung, mitteilen, die Mahnung, das Netz, das Netzwerk

**Scene 8: Die Dorfzeitung**
- Premise: A tiny local newsletter reports breathlessly on utterly mundane village events.
- Comedic angle: The 'breaking news' headline turns out to be about a cat stuck in a tree, again.
- Words (13): die Neuigkeit, die Nummer, die Presse, die Recherche, reden, die Rede, die Reklame, die Post, die Postleitzahl, der Pöstler / die Pöstlerin, das Plakat, der Punkt, raten

**Scene 9: Der Poesiealbum-Eintrag**
- Premise: Classmates write increasingly ridiculous entries in a friend's old-school memory book.
- Comedic angle: One entry is just a single word repeated in seventeen different colors.
- Words (13): der Rat, Ratschlag, sagen, schicken, die Schrift, schriftlich, der Schriftsteller / die Schriftstellerin, senden, der Sender, die Sendung, rufen, die Rufnummer, schimpfen

**Scene 10: Der stille Streit**
- Premise: A couple has an argument entirely through passive-aggressive sticky notes instead of talking.
- Comedic angle: The notes escalate until one is just a single, silently furious exclamation mark.
- Words (13): schreiben, aufschreiben, das Schreiben, schreien, schweigen, (sich) siezen, sprechen, die Sprache, die Fremdsprache, die Muttersprache, die Zweitsprache, stimmen, die Stimme

**Scene 11: Der Umfrage-Stand in der Fußgängerzone**
- Premise: A market researcher tries to get busy pedestrians to answer a long survey.
- Comedic angle: Most answers are just people trying to walk away faster while still technically responding.
- Words (13): der Standpunkt, speichern, tippen, die Tastatur, die Taste, der Text, die Überschrift, überreden, die Umfrage, umarmen, (sich) umdrehen, vereinbaren, verlangen

**Scene 12: Die Nachbarschaftsversammlung**
- Premise: Neighbors debate a trivial building issue with wildly exaggerated formality.
- Comedic angle: The vote on a broken doorbell somehow takes longer than actually fixing it would have.
- Words (13): (sich) unterhalten, die Unterhaltung, versprechen, überprüfen, üblich, der Vertreter / die Vertreterin, die Vertretung, vertreten, verzeihen, Verzeihung, die Visitenkarte, die Vorwahl, vorlesen

**Scene 13: Die Wörterbuch-Rätselrunde**
- Premise: Friends play a game guessing definitions of obscure words from an old dictionary.
- Comedic angle: Someone's completely made-up fake definition wins the round because it sounded more convincing than the real one.
- Words (13): der Vortrag, warnen, wecken, der Wecker, die Werbung, der Witz, zeigen, die Zeile, das Wort, das Wort, das Wörterbuch, vorschlagen, der Vorschlag

**Scene 14: Der Zeitschriften-Abo-Stapel**
- Premise: Someone finally sits down to sort through months of unread magazines and newsletters.
- Comedic angle: Every single one somehow already has next month's issue arriving at the same moment.
- Words (8): (sich) vorstellen, die Vorstellung, die Zeitschrift, die Zeitung, wiederholen, die Wiederholung, zuhören, der Zuhörer / die Zuhörerin


### Stadt, Ämter & Recht  _150 words, 12 scenes_

**Scene 1: Der Behördenmarathon**
- Premise: Someone spends an entire day bouncing between government offices trying to register a new address.
- Comedic angle: Each office sends them to a different building, and they end up back at the first one by closing time.
- Words (13): das Amt, der Antrag, anmelden, die Anmeldung, angeben, die Angabe, ausfüllen, der Ausweis, der Anwalt / die Anwältin, anzeigen, die Anzeige, der Alarm, der Beamte / die Beamtin

**Scene 2: Der Einbruch, der keiner war**
- Premise: Police investigate a reported break-in that turns out to be the homeowner's own forgotten spare key attempt.
- Comedic angle: The 'burglar' description perfectly matches the homeowner's own reflection in the window.
- Words (13): beantragen, die Behörde, betrügen, bestrafen, beweisen, der Bürger / die Bürgerin, der Dieb, der Dienst, das Dokument, die Droge, die Drogerie, einbrechen, der Einbrecher / die Einbrecherin

**Scene 3: Das Fundbüro-Chaos**
- Premise: A lost-and-found office is overflowing with bizarre unclaimed items nobody can explain.
- Comedic angle: Someone claims a lost umbrella that turns out to belong to someone else entirely, with an identical one.
- Words (13): der Einbruch, der Einwohner / die Einwohnerin, festnehmen, festsetzen, das Formular, das Fundbüro, die Burg, der Doktor / die Doktorin, behindern, bekannt geben, berichten, der Bericht, das Gebäude

**Scene 4: Die Ratsversammlung ums Wahrzeichen**
- Premise: A town council argues passionately over a minor local landmark's upkeep.
- Comedic angle: The heated debate turns out to be about a statue nobody can actually agree what it's supposed to depict.
- Words (13): das Gebiet, die Gemeinschaft, das Gesetz, die Gesellschaft, das Gefängnis, der Gegner, die Grenze, illegal, das Gebirge, die Hauptstadt, der Hauptbahnhof, der Herr, installieren

**Scene 5: Die Straßensperrung wegen Königsbesuch**
- Premise: A small town prepares chaotically for a supposed royal visit that turns out to be a misunderstanding.
- Comedic angle: The 'king' is actually just a costumed actor for an unrelated event three streets over.
- Words (13): das Kennzeichen, die Kirche, der Krieg, die Krise, das Konsulat, der König, die Katastrophe, Kriminal- / die Kriminalpolizei, das Kreuz, der Konflikt, die Mauer, die Mehrheit, die Minderheit

**Scene 6: Die Pressekonferenz im Rathaus**
- Premise: A mayor holds an overly formal press conference about a very minor town achievement.
- Comedic angle: The big announcement turns out to be about a new public bench.
- Words (13): das Mitglied, der Nachbar / die Nachbarin, die Messe, der Notausgang, die Öffentlichkeit, öffentlich, veröffentlichen, offiziell, das Opfer, die Ordination, die Ordination, die Organisation, der Ort

**Scene 7: Der verlegte Reisepass**
- Premise: Someone frantically searches for their passport the night before a trip, tearing the apartment apart.
- Comedic angle: It was in their jacket pocket the entire time, worn the whole search.
- Words (13): der Vorort, der Wohnort, passieren, der Pass, der Personenstand, die Personalien, die Politik, der Politiker / die Politikerin, politisch, die Polizei, der Polizist / die Polizistin, der Prozess, das Recht

**Scene 8: Die Verkehrskontrolle**
- Premise: A police officer stops a driver for a minor infraction, and the excuse offered gets more elaborate by the second.
- Comedic angle: The excuse eventually involves a very convincing but entirely fictional medical emergency.
- Words (13): rechtlich, die Reform, die Regel, regeln, das Rathaus, der Richter / die Richterin, die Sicherheit, sichern, rauchen, der Raucher / die Raucherin, schuldig, die Schuld, schuld

**Scene 9: Der Gerichtssaal-Sketch**
- Premise: Friends stage a mock trial for a silly neighborhood dispute over a fence.
- Comedic angle: The 'jury' is a group of very serious-looking garden gnomes borrowed for the occasion.
- Words (13): die Schulden, die Religion, die Richtung, der Sozialarbeiter / die Sozialarbeiterin, sozial, strafbar, die Strafe, der Strafzettel, der Täter / die Täterin, der Stempel, (sich) streiten, der Streit, streiken

**Scene 10: Der Ladendiebstahl-Verdacht**
- Premise: A shopkeeper suspiciously eyes a customer buying a huge, oddly specific pile of random items.
- Comedic angle: It turns out to be ingredients for the world's most impractical sandwich, not a heist.
- Words (13): der Streik, der Stress, das Schaufenster, die Urkunde, das Urteil, verhaften, der Verdacht, verdächtig, der Verbrecher / die Verbrecherin, das Verbot, verbieten, verboten, die Uniform

**Scene 11: Die Unterschriftensammlung**
- Premise: A neighbor collects signatures for a petition about a trivial local issue with dramatic urgency.
- Comedic angle: Half the signatures turn out to be from the same person using slightly different handwriting.
- Words (13): untersagt, unterschreiben, die Unterschrift, die Ursache, verursachen, verraten, die Versammlung, der Unfall, verhindern, versäumen, verurteilen, die Verwaltung, das Visum

**Scene 12: Die Zertifikatsübergabe**
- Premise: A small community club holds an overly formal ceremony for a minor achievement certificate.
- Comedic angle: The certificate is presented with the pomp of a Nobel Prize, for finishing a crossword puzzle.
- Words (7): die Vorschrift, die Vorfahrt, der Vorwurf, der Zeuge / die Zeugin, das Zeugnis, das Zertifikat, der Zivilstand


### Arbeit & Beruf  _139 words, 11 scenes_

**Scene 1: Das Vorstellungsgespräch-Desaster**
- Premise: A job applicant tries to sound impressively experienced despite obvious nervousness in an interview.
- Comedic angle: He accidentally lists his hobby as 'work' three separate times before catching himself.
- Words (13): anerkennen, der Anspruch, anstellen, der Angestellte / die Angestellte, sich anstrengen, anstrengend, der Auftrag, die Aushilfe, der Architekt / die Architektin, beruflich, berufstätig, der Beruf, der Betrieb

**Scene 2: Die Kündigungs-Überraschung**
- Premise: An employee dramatically quits a job they actually love, over a minor misunderstanding.
- Comedic angle: They immediately regret it and spend the rest of the day trying to un-quit as casually as possible.
- Words (13): der Betriebsrat / die Betriebsrätin, sich bewerben, die Bewerbung, das Diplom, entlassen, die Entlassung, der Erfolg, erfolgreich, erledigen, der Experte, der Export, die Fabrik, das Fach

**Scene 3: Der Streik in der Fabrik**
- Premise: Factory workers stage a good-natured strike over cafeteria food quality, complete with homemade signs.
- Comedic angle: Management resolves it instantly by simply improving the coffee, ending the strike in ten minutes.
- Words (13): der Fachmann / die Fachfrau, die Fachleute, fehlen, der Fehler, der Feierabend, die Firma, fleißig, fordern, die Forderung, fördern, die Förderung, die Führung, arbeiten

**Scene 4: Der erste Arbeitstag**
- Premise: A nervous new hire tries to look competent on their very first day at an unfamiliar office.
- Comedic angle: They confidently sit at the CEO's desk, not realizing whose office it actually is.
- Words (13): die Arbeit, der Arbeiter / die Arbeiterin, die Arbeitserlaubnis, arbeitslos, die Arbeitslosigkeit, der Arbeitsplatz, die Arbeitsstelle, beenden, sich beteiligen, das Büro, der Direktor / die Direktorin, die Gewerkschaft, die Generation

**Scene 5: Die Firmengründung im Wohnzimmer**
- Premise: Two friends 'launch a company' from a cluttered living room with wildly ambitious plans.
- Comedic angle: Their entire business plan is written on the back of a pizza box.
- Words (13): das Gehalt, die Gelegenheit, gründen, der Grund, der Handel, handeln, der Händler / die Händlerin, der Hersteller, herstellen, der Ingenieur, die Industrie, der Import, der Handwerker / die Handwerkerin

**Scene 6: Die Beförderungsfeier**
- Premise: A workplace throws an overly enthusiastic party for a colleague's minor promotion.
- Comedic angle: The cake spells the wrong job title, and nobody has the heart to mention it.
- Words (13): die Herausforderung, die Karriere, der Kollege / die Kollegin, kündigen, die Kündigung, der Kunde / die Kundin, der Kandidat, das Kraftfahrzeug, das Kraftwerk, der Kellner / die Kellnerin, leisten, die Leistung, leiten

**Scene 7: Der Werkstattbesuch**
- Premise: A mechanic explains an absurdly complicated car problem to a confused customer using props.
- Comedic angle: The 'complex diagnosis' turns out to be a coin stuck in the cup holder rattling around.
- Words (13): der Leiter / die Leiterin, die Leitung, der Lohn, der Mangel, der Mechaniker / die Mechanikerin, der Meister, der Mitarbeiter / die Mitarbeiterin, der Migrant / die Migrantin, die Migration, das Material, nützen, das Personal, der Praktikant / die Praktikantin

**Scene 8: Das Praktikum bei der Zeitung**
- Premise: An eager intern at a newspaper is assigned only trivial tasks despite grand journalistic ambitions.
- Comedic angle: Their first 'published' piece is just the weekly parking schedule notice.
- Words (13): das Praktikum, der Professor / die Professorin, der Profi, der Profisportler / die Profisportlerin, das Projekt, die Qualifikation, die Mannschaft, reparieren, die Reparatur, der Rest, der Sekretär / die Sekretärin, selbstständig, der Schauspieler / die Schauspielerin

**Scene 9: Der Radiosport-Kommentator**
- Premise: An overly dramatic amateur commentator narrates a minor local sports match like it's a world championship.
- Comedic angle: He gets more excited about the halftime snack break than the actual game.
- Words (13): der Sänger / die Sängerin, der Reporter / die Reporterin, die Reportage, der Serviceangestellte / die Serviceangestellte, der Spezialist / die Spezialistin, der Steward / die Stewardess, der Student / die Studentin, der Studierende / die Studierende, die Tätigkeit, der Täter / die Täterin, teilnehmen, die Teilnahme, der Teilnehmer / die Teilnehmerin

**Scene 10: Die Bewerbungsmappe**
- Premise: Someone assembles an overly polished job application for a very casual part-time position.
- Comedic angle: The application is longer than the actual job description.
- Words (13): die Teilzeit, telefonieren, das Telefon, der Termin, der Terminkalender, die Überstunde, die Unterlagen, der Unternehmer / die Unternehmerin, die Unterstützung, unterstützen, verdienen, der Verein, der Verlag

**Scene 11: Die Werkzeugkiste-Katastrophe**
- Premise: A handyman's disorganized toolbox causes chaos on a simple repair job.
- Comedic angle: He spends longer looking for the right tool than the actual repair would have taken.
- Words (9): die Weiterbildung, das Werk, die Werkstatt, das Werkzeug, zugänglich, zuständig, die Vollzeit, das Vorstellungsgespräch, der Zufall


### Kleidung & Aussehen  _48 words, 4 scenes_

**Scene 1: Die Modenschau im Wohnzimmer**
- Premise: Friends stage a silly homemade fashion show using thrift-store finds and bedsheets as capes.
- Comedic angle: The 'showstopper outfit' is just someone wrapped entirely in a shower curtain, strutting confidently.
- Words (13): anhaben, (sich) anziehen, der Anzug, aussehen, die Bluse, die Brille, blond, chic/schick, die Creme, das Couvert, elegant, die Farbe, farbig

**Scene 2: Der Frisörbesuch, der schiefging**
- Premise: Someone asks for a small trim and ends up with a dramatically different haircut.
- Comedic angle: They insist they 'meant to do that' to everyone who asks, unconvincingly.
- Words (13): der Fleck, frisch, der Friseur / die Friseurin, die Frisur, hässlich, das Hemd, die Hose, der Hut, die Jacke, die Jeans, hell, die Kette, das Kleid

**Scene 3: Der Kleiderschrank-Notstand**
- Premise: Someone digs through an overstuffed wardrobe trying to find one specific missing item before a party.
- Comedic angle: They find seventeen single socks and not one matching pair.
- Words (13): die Kleidung, das Kostüm, die Kiste, kleben, der Knopf, der Mantel, die Mode, modern, das Modell, das Parfüm, der Pullover, der Ring, der Schmuck

**Scene 4: Das missglückte Date-Outfit**
- Premise: Someone spends hours picking the perfect outfit for a first date, changing their mind constantly.
- Comedic angle: They end up going in the very first outfit they tried on, an hour later.
- Words (9): schminken, schön, der Schuh, der Rock, der Stiefel, der Strumpf, das Taschentuch, die Tüte, das Zeug/-zeug


### Körper & Gesundheit  _139 words, 11 scenes_

**Scene 1: Der Hausarztbesuch**
- Premise: Someone describes a minor ailment to the doctor with wildly exaggerated symptoms.
- Comedic angle: The doctor's diagnosis is simply 'you need more sleep,' delivered with visible exhaustion of their own.
- Words (13): abnehmen, der Arm, die Apotheke, der Appetit, der Arzt / die Ärztin, atmen, der Atem, (sich) ausruhen, äußerlich, das Asyl, der Bauch, beschädigen, die Besserung

**Scene 2: Der Marathon-Trainingsunfall**
- Premise: An overambitious first-time runner overdoes their training and ends up hilariously sore.
- Comedic angle: They can't climb stairs the next day and have to be helped by a very unimpressed roommate.
- Words (13): der Bart, bluten, das Blut, der Blick, blind, die Brust, die Diät, dunkel, dünn, der Durst, durstig, (sich) duschen, die Dusche

**Scene 3: Die Erkältungswelle im Büro**
- Premise: An entire office catches the same cold within days, each person insisting theirs is the worst case.
- Comedic angle: The healthiest-looking person turns out to be the one who's been secretly suffering the most.
- Words (13): sich erholen, die Erholung, sich erkälten, erkältet, die Erkältung, erschöpft, erschrecken, das Fieber, der Finger, das Auge, der Fuß, beißen, das Bein

**Scene 4: Der Selbstdiagnose-Notfall**
- Premise: Someone convinces themselves they have a serious illness after reading symptoms online.
- Comedic angle: The actual diagnosis is just needing to drink more water.
- Words (13): die Gefahr, gefährlich, gesund, die Gesundheit, das Gesicht, giftig, das Gift, das Gefühl, die Grippe, das Haar, der Hals, die Hand, die Haut

**Scene 5: Der Krankenhausbesuch bei Oma**
- Premise: Grandchildren visit a grandparent recovering from a minor procedure in the hospital.
- Comedic angle: The grandparent is more worried about missing their favorite TV show than about their own recovery.
- Words (13): husten, der Husten, hungrig, der Hunger, die Infektion, das Herz, der Kopf, der Körper, körperlich, krank, der Kranke / die Kranke, das Krankenhaus, die Krankenkasse

**Scene 6: Der Notaufnahme-Fehlalarm**
- Premise: A minor kitchen accident sends someone rushing dramatically to the emergency room.
- Comedic angle: The injury turns out to need nothing more than a small bandage, applied in thirty seconds.
- Words (13): der Krankenpfleger, die Krankenschwester, der Krankenwagen, die Krankheit, das Knie, der Knochen, leiden, die Kraft, die Lippe, der Magen, mager, die Medizin, das Medikament

**Scene 7: Die Zahnarztangst**
- Premise: Someone works themselves into a panic before a routine dental checkup.
- Comedic angle: The appointment is over before they've even finished nervously rambling in the waiting room.
- Words (13): müde, die Mühe, der Mund, der Muskel, der Mut, mutig, die Nase, der Nerv, nervös, die Klinik, mild, das Ohr, operieren

**Scene 8: Der Physiotherapietermin**
- Premise: A patient exaggerates every small movement during a physical therapy session for sympathy.
- Comedic angle: The therapist calmly points out they were sprinting fine in the parking lot minutes earlier.
- Words (13): die Operation, das Pflaster, pflegen, der Pfleger / die Pflegerin, der Patient / die Patientin, die Notaufnahme, der Notfall, der Notruf, (sich) rasieren, der Rücken, der Schmerz, das Schmerzmittel, der Schnupfen

**Scene 9: Der Yoga-Kurs für Anfänger**
- Premise: A stiff beginner struggles hilariously through a gentle yoga class meant for relaxation.
- Comedic angle: Their idea of the 'child's pose' looks suspiciously like they've simply fallen asleep.
- Words (13): die Schulter, schwitzen, die Seife, die Salbe, die Sprechstunde, die Spritze, spüren, stechen, sterben, die Sucht, süchtig, das Suchtmittel, taub

**Scene 10: Die Familiengeschichte über Uroma**
- Premise: Relatives tell exaggerated stories about a great-grandmother's supposedly dramatic health scares.
- Comedic angle: Every retelling makes the illness sound more serious than the doctor's actual, mild diagnosis.
- Words (13): die Tablette, die Therapie, schädlich, die Temperatur, der Tod, tödlich, tot, der Tote / die Tote, die Träne, untersuchen, die Untersuchung, verschreiben, (sich) verletzen

**Scene 11: Der Apothekenbesuch mit Zettel**
- Premise: Someone hands the pharmacist a long, messy shopping list mixing real medicine with random errands.
- Comedic angle: The pharmacist patiently points out that 'milk' isn't something they sell.
- Words (9): die Verletzung, sich verlaufen, vermissen, die Zahncreme/-pasta, der Zahn, die Zange, die Wunde, die Praxis, das Vitamin


### Reisen & Urlaub  _54 words, 4 scenes_

**Scene 1: Der Packstress vor der Abreise**
- Premise: Someone tries to pack for a trip at the last minute, throwing random items into an overstuffed suitcase.
- Comedic angle: They forget the actual passport but somehow remember three different chargers for devices they don't own.
- Words (13): der Aufenthalt, ankommen, die Ankunft, der Ausflug, das Ausland, die Auskunft, besuchen, der Besuch, das Boot, buchen, der Bus, einpacken, erfahren

**Scene 2: Die Hotelverwechslung**
- Premise: A family arrives at what they think is their booked hotel, only to find it's the wrong one entirely.
- Comedic angle: The actual hotel turns out to be a tiny, forgotten guesthouse two streets away with a much better breakfast.
- Words (13): die Erfahrung, erreichen, die Ferien, Ferien-, das Gepäck, die Halbpension, das Hallenbad, das Hotel, inklusive, die Kabine, der Kiosk, der Koffer, die Küste

**Scene 3: Der Rentnerausflug ans Meer**
- Premise: A group of retirees goes on a seaside excursion, bickering affectionately about every stop on the itinerary.
- Comedic angle: Their strict schedule gets completely derailed by an impromptu ice cream stop that everyone secretly wanted anyway.
- Words (13): die Pension, die Pension, in Pension gehen/sein, pensioniert werden/sein, der Pensionist / die Pensionistin, das Quartier, die Reise, reisen, das Reisebüro, reservieren, die Reservierung, die Sehenswürdigkeit, das Schiff

**Scene 4: Die Heimreise-Odyssee**
- Premise: A trip home gets delayed by every possible transport mishap in a row.
- Comedic angle: By the time they finally arrive, they've told the story so many times it's grown into an epic saga.
- Words (15): die Rezeption/Reception, transportieren, der Transport, der Urlaub, die Unterkunft, verreisen, die Toilette, der Treffpunkt, das Trinkgeld, die Tropfen, das Viertel, der Vorort, der Wohnort, der Wohnsitz, das/der Zvieri/Znüni


### Zeit & Kalender  _91 words, 7 scenes_

**Scene 1: Der Morgenmuffel**
- Premise: Someone struggles through their entire morning routine half-asleep, narrating each stumbling step.
- Comedic angle: They leave the house confidently before realizing they're still wearing slippers.
- Words (13): der Alltag, alltäglich, anfangs, der Anfang, aufstehen, aufwachen, der Augenblick, bald, bevor, damals, danach, dann, dauern

**Scene 2: Die Terminüberschneidung**
- Premise: Someone realizes they've double-booked two important events at the exact same time.
- Comedic angle: They try sprinting between both venues and end up fully missing one and half-attending the other.
- Words (13): die Dauer, dauernd, das Datum, diesmal, donnern, der Donner, doppelt, Doppel-, einmal, enden, das Ende, endgültig, endlich

**Scene 3: Die Silvesterfeier-Erinnerungen**
- Premise: Friends recount a wild New Year's Eve party, each remembering the timeline completely differently.
- Comedic angle: Nobody can agree what time the fireworks actually started, or who started them early by accident.
- Words (13): das Ereignis, sich ereignen, erleben, das Erlebnis, erst, erst-, ewig, die Frist, früh, früher/früher-, frühstücken, das Frühstück, gestern

**Scene 4: Der ewig gleiche Tagesablauf**
- Premise: Someone complains about how monotonous their daily routine has become, describing it hour by hour.
- Comedic angle: The 'boring routine' includes an oddly specific daily argument with a stubborn printer.
- Words (13): heute, heutig-, hinterher, immer, halb, halbtags, die Hälfte, der Kalender, langweilig, sich langweilen, die Langeweile, der Moment, neulich

**Scene 5: Die verpasste Deadline**
- Premise: Someone realizes far too late that an important deadline was actually yesterday, not today.
- Comedic angle: Their 'punctual' excuse email is sent exactly one minute before they finally notice the mistake.
- Words (13): das Leben, notieren, die Notiz, rechtzeitig, pünktlich, die Pause, das Semester, selten, schließlich, spät, spätestens, der Tagesablauf, tatsächlich

**Scene 6: Der Startschuss zum Sommerfest**
- Premise: A neighborhood festival's opening ceremony is delayed repeatedly by small technical mishaps.
- Comedic angle: By the time the 'official start' finally happens, half the guests have already eaten all the food.
- Words (13): der Schluss, starten, der Start, die Stunde, die Saison, übernachten, die Übernachtung, die Vergangenheit, die Verspätung, verpassen, die Zahl, die Anzahl, voraussichtlich

**Scene 7: Der Kalender voller Erinnerungen**
- Premise: Someone reviews an old calendar full of forgotten appointments and reminders scribbled in the margins.
- Comedic angle: One cryptic note just says 'don't forget!!' with no indication of what not to forget.
- Words (13): das Zeichen, das Verkehrszeichen, zeichnen, die Zeichnung, die Zeit, der Zeitpunkt, zurzeit, das Zelt, zelten, die Zukunft, zukünftig, die Zünder, das Zündholz


### Gesellschaft, Politik & Wirtschaft  _20 words, 2 scenes_

**Scene 1: Die Nachbarschaftsdebatte**
- Premise: Neighbors from different backgrounds debate a minor community issue, each bringing in wildly broad arguments.
- Comedic angle: The debate about a shared garden fence somehow ends up covering the entire history of humanity.
- Words (13): der Ausländer / die Ausländerin, ausländisch, außerhalb, die Chance, die Bevölkerung, egal, die Freiheit, die Geschichte, der Gott, die Gewalt, der Mensch, menschlich, der Nachteil

**Scene 2: Der Wirtschaftsgipfel im Kleingarten**
- Premise: Allotment gardeners hold a mock 'economic summit' over how to divide a shared harvest fairly.
- Comedic angle: Their complex trade agreement collapses over who gets the last, biggest tomato.
- Words (7): die Pflicht, populär, die Wirtschaft, die Welt, weltweit, die Zusammenarbeit, zusätzlich


### Essen, Kochen & Restaurant  _149 words, 12 scenes_

**Scene 1: Der Bäckerei-Notfall**
- Premise: Someone bakes bread for the first time and it comes out looking nothing like the recipe photo.
- Comedic angle: They serve it anyway, confidently calling the brick-like loaf 'rustic'.
- Words (13): der Apfel, die Aprikose, der Alkohol, braten, der Braten, brechen, das Brot, das Brötchen, das Brötli, die Butter, das Buffet, die Bohne, das Café

**Scene 2: Der Café-Vormittag**
- Premise: Friends meet at a café for coffee and end up arguing playfully about the 'correct' way to eat an egg.
- Comedic angle: The debate escalates until the whole café is quietly listening in, amused.
- Words (13): die Cafeteria, bitter, das Ei, das Eis, das Eis, ernähren, die Ernährung, die Ernte, essen, das Essen, der Essig, das Faschierte, der Fasching

**Scene 3: Das Grillfest der Nachbarn**
- Premise: A neighborhood barbecue turns chaotic as everyone insists on grilling their own dish their own way.
- Comedic angle: The grill catches a small, dramatic flare-up right as the 'grill master' is bragging about his technique.
- Words (13): die Fasnacht, fett, das Fett, das Fleisch, der Fleischhauer / die Fleischhauerin, das Hackfleisch, backen, die Bäckerei, die Banane, das Bier, das Dessert, das Gasthaus, die Gaststätte

**Scene 4: Die Kochshow-Parodie**
- Premise: Friends film a silly homemade cooking show, narrating dramatically over a very simple dish.
- Comedic angle: The 'secret ingredient' reveal is just regular salt, treated like a plot twist.
- Words (13): der Gast, das Gebäck, das Gemüse, das Gericht, der Geschmack, das Getränk, das Gewürz, gießen, die Gabel, gemeinsam, grillen, grillieren, der Grill

**Scene 5: Der Fast-Food-Notstand**
- Premise: A group debates for way too long over a simple fast-food order, changing their minds constantly.
- Comedic angle: By the time they finally order, the kitchen is already closing.
- Words (13): das Hähnchen/Hühnchen, das Hendl, der Honig, der Imbiss, die Jause, der Kaffee, das Kaffeehaus, der Kakao, die Kantine, die Karotte, die Kartoffel, der Käse, der Kloß

**Scene 6: Die Familienrezept-Weitergabe**
- Premise: A grandmother tries to teach her grandchild a traditional recipe with wildly imprecise, old-fashioned measurements.
- Comedic angle: 'A handful' and 'until it feels right' turn out to be the only actual instructions given.
- Words (13): die Konfitüre, kochen, der Koch / die Köchin, der Knödel, der Kuchen, lecker, die Lebensmittel, die Kneipe, kühl, das Lokal, die Limonade, die Mahlzeit, die Margarine

**Scene 7: Der Marmeladen-Wettbewerb**
- Premise: Neighbors compete in an amateur jam-making contest with fiercely guarded secret recipes.
- Comedic angle: The 'secret ingredient' in the winning jam turns out to be a happy accident nobody can replicate again.
- Words (13): die Marille, die Marmelade, das Mehl, das Menü, die Mensa, das Mineralwasser, die Möhre, das Müesli/Müsli, die Milch, der Metzger, die Nachspeise, das Nahrungsmittel, die Kanne

**Scene 8: Das internationale Buffet**
- Premise: A potluck dinner features dishes from many countries, with each guest passionately defending their own.
- Comedic angle: The most popular dish by far is the one nobody can identify or pronounce.
- Words (13): die Nudel, das Obst, das/derObers, der Ober, die Orange, die Pfanne, der Pfeffer, die Pflaume, das Picknick, der Pilz, die Pizza, die Pommes frites, die Portion

**Scene 9: Die Restaurantkritik-Parodie**
- Premise: An amateur food blogger dramatically reviews a very ordinary neighborhood restaurant.
- Comedic angle: Their five-paragraph review is entirely about the bread basket.
- Words (13): probieren, probieren, der Paradeiser, das Poulet, derRahm, der Reis, das Rezept, roh, dasRohr, das Restaurant, der Saft, dieSahne, der Salat

**Scene 10: Der zu scharfe Wettkampf**
- Premise: Friends challenge each other to eat increasingly spicy food at a competitive dinner.
- Comedic angle: The self-proclaimed 'spice champion' taps out first, dramatically reaching for the entire milk carton.
- Words (13): das Salz, salzig, schmecken, das Schnitzel, die Schokolade, der Schinken, das Schwammerl, sauer, satt, die Soße/Sauce, die Speisekarte, die Suppe, süß

**Scene 11: Der Kellner-Ausbildungstag**
- Premise: A trainee waiter fumbles through their first shift, mixing up every order at the table.
- Comedic angle: They somehow end up serving dessert before the appetizer, and the guests decide they actually prefer it that way.
- Words (13): die Tasse, der Teller, der Tee, Tee ziehen lassen, die Semmel, der Service, der Speisewagen, die Tomate, die Torte, vegetarisch, verpflegen, trinken, das Rüebli

**Scene 12: Der Weinkeller-Ausflug**
- Premise: Friends tour a small local winery, pretending to be much more sophisticated tasters than they actually are.
- Comedic angle: Their elaborate tasting notes are all suspiciously similar to 'tastes like grapes.'
- Words (6): der Wein, die Zitrone, die Zwiebel, die Wurst, die Zigarette, zubereiten


### Tiere  _8 words, 1 scenes_

**Scene 1: Der chaotische Bauernhofbesuch**
- Premise: City visitors help feed animals on a farm and immediately get overwhelmed by an overeager goat.
- Comedic angle: The goat steals someone's hat and proudly parades around the pen wearing it like a trophy.
- Words (8): der Bauer, fressen, füttern, der Bauernhof, die Schlange, das Tier, das Haustier, der Tierpark


## 5. Methodology & judgment calls

- **Parsing**: column 1 was split on `\n`; lines starting with `→` (regional-variant notes, e.g. "→ CH: Tram") were dropped from lemma extraction but not from the entry itself — the row still counts as one entry. The remaining line(s) had parenthetical region tags (`(D)`, `(A, CH)` etc.) stripped, and the lemma is everything before the first comma (dropping plural/conjugation forms). Reflexive `(sich)` was preserved as a prefix.
- **The "; " separator**: the task description mentions cells with multiple headwords separated by `"; "`. In the actual CSV, `"; "` only ever occurs *inside* the `→` regional-variant note (e.g. "→ A: Kuvert; CH: Couvert"), never in the primary headword. The real multi-headword case in this list is masc/fem occupation pairs on separate lines within one cell (e.g. "der Lehrer, -\ndie Lehrerin, -nen"), which were merged into one combined lemma per row ("der Lehrer / die Lehrerin") since they're one CSV entry and will appear together in a scene anyway.
- **Row = entry**: each of the 2886 CSV rows counts as exactly one entry for coverage purposes (matching the task's own "coverage: X/2886" framing), even when a row's cell contains two merged headwords or a masc/fem pair.
- **`zurzeit` appears twice** in the source CSV as two separate, identical rows (idx 2811 and 2861) — a genuine duplicate in the official wordlist, not a parsing artifact. Both rows are covered (the word appears twice across the topic lists, once in Zeit & Kalender's time-adverb scene and once in Grammatik's small-talk scene).
- **Duplicate-string entries with different meanings** (`der Ausdruck` printout vs. expression; `die Bank` bench vs. financial bank; `das Eis` ice vs. ice cream; `das Wort` Worte vs. Wörter; `der Sessel` in two regional senses) were deliberately split across two different, more fitting topics rather than both landing in the same place.
- **A few common verbs** (`nehmen`, `nennen`, `fallen`, `scheinen`) ended up bucketed inside Grammatik's "Alltags-Kleinwörter" catch-all sub-scene rather than in Handlungen — a minor taxonomic imperfection from the iterative build process. They're still fully covered and still get a concrete scene; a cleaner build would move them.
- **Total scenes**: 228, averaging ~12.7 words each.

coverage: 2886/2886 (100.0%)

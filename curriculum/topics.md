# Goethe B1 Wortliste — Merged Topic Taxonomy & Scene Outlines (Final)

**This is the merged, final deliverable.** It combines the winning entry (agent B — semantic within-scene word grouping) with specific ideas absorbed from the judged comparison in `JUDGE.md`: agent C's three-way functional split of the grammar mega-topic (RAUM / LOGIK / GLUE) and its sharper premises and audit rigor, and agent A's fine-grained Gefahr/Notfall and Farben/Formen/Material topics. See `JUDGE.md` for the comparison this builds on.

Groundwork for the crammed-topic-batch → write-a-vivid-scene → Anki-card method. This file is **taxonomy and cram order** — which words belong to which topic, and in what order the topics are crammed. It holds no word lists (those are in the ledger, `curriculum/vocab.db` / `assignments.tsv`) and no German practice text (that is written per batch by the `text-writer` skill).

Source: `goethe-b1-wortliste.csv`, 2886 data rows (version-header row skipped). Parsed with Python — see the Methodology section at the end for exactly how, plus every judgment call.

## 1. Taxonomy & cram order

**23 scene-topics + 1 shared glue pool**, grouped into **4 stages ordered concrete → abstract**. The idea: cram the vivid, easy-to-picture, high-frequency material first, while motivation and visual imagination are freshest. Farben/Formen/Material and Gefahr/Notfall/Sicherheit are carved out as their own tight, imaginable topics. The dividing line between a scene-topic and the pool is **grammatical class, not abstractness**: every open-class word gets a scene — even abstract nouns and verbs (`die Meinung`, `entscheiden`, `wichtig`, `zweifeln`), which the method grounds in situations — while every closed-class function word (prepositions, conjunctions, pronouns, determiners, particles, question words, directional adverbs, modal/aux verbs) goes to the **shared pool** (`glue-pool.md`). Function words like *obwohl, zwischen, derselbe, ziemlich* have no mental picture; forcing scenes out of them produces exactly the un-imaginable texts we want to avoid. So the old 360-word grammar mega-topic AND the former Raum & Richtung topic collapse into the pool (its 10 depictable position verbs + `nah/weit/lang` moved to a real "moving day" scene under Handlungen), and closed-class stragglers were swept out of Menge (21) and Denken (23) too. The pool is sizable (**326 words**) — that's inherent: it's the entire function-word inventory of B1, learned through repetition across every text rather than in dedicated scenes. None of the three original submissions sequenced topics concrete→abstract this way (see `JUDGE.md` item 7); within each stage, topics run roughly largest→smallest.

**Stage A. Konkret & körperlich (start here)**: In der Wohnung & Zuhause → Körper & Gesundheit → Essen, Kochen & Restaurant → Tiere → Kleidung & Aussehen → Farben, Formen & Material → Familie & Beziehungen → Gefahr, Notfall & Sicherheit

**Stage B. Situativ & alltagsweltlich**: Natur, Wetter & Umwelt → Unterwegs & Verkehr → Reisen & Urlaub → Einkaufen & Geld → Stadt, Ämter & Recht → Arbeit & Beruf → Schule & Bildung → Freizeit, Medien & Technik

**Stage C. Emotional & kommunikativ**: Gefühle & Charakter → Kommunikation & Post → Zeit & Kalender → Gesellschaft, Politik & Wirtschaft

**Stage D. Abstrakt & grammatisch (save for last)**: Menge, Maß & Eigenschaften → Handlungen: Alltagsverben (now carrying the position verbs) → Denken, Wissen & Meinen → **⟶ shared glue pool** (all closed-class function words — former *Logik & Verbindungen*, *Grammatik-Glue*, and *Raum & Richtung* — **326** words, NOT scened; woven through all batches, see `glue-pool.md`)

## 2. Topic taxonomy

| Batch | Topic | Words | Scenes | Description |
|---:|---|---:|---:|---|
| 1 | In der Wohnung & Zuhause | 148 | 11 | Rooms, furniture, household objects, chores, moving house. |
| 2 | Körper & Gesundheit | 128 | 10 | Body parts, illness, doctor, pharmacy, hospital, symptoms. |
| 3 | Essen, Kochen & Restaurant | 149 | 12 | Food, drink, cooking, groceries, restaurant & café life. |
| 4 | Tiere | 8 | 1 | Animals and farm life (a small, genuinely thin category in the B1 list). |
| 5 | Kleidung & Aussehen | 44 | 3 | Clothing, accessories, hairstyling, appearance. |
| 6 | Farben, Formen & Material | 41 | 3 | Color adjectives, geometric shapes, material/surface texture — carved out of the old grab-bag 'Menge/Eigenschaften' and 'Wohnung' topics as its own tight, highly imaginable batch (per JUDGE.md item 3, following agent A). |
| 7 | Familie & Beziehungen | 107 | 8 | Family members, life stages, relationships, weddings, parenting. |
| 8 | Gefahr, Notfall & Sicherheit | 38 | 3 | Danger, accidents, fire, emergency exits, warnings, rescue — carved out of Körper/Stadt/Gefühle into its own vivid batch (per JUDGE.md item 3, following agent A). |
| 9 | Natur, Wetter & Umwelt | 97 | 8 | Weather, landscape, environment, climate, countryside. |
| 10 | Unterwegs & Verkehr | 112 | 9 | Transport, traffic, directions, cars, trains, planes. |
| 11 | Reisen & Urlaub | 54 | 4 | Travel, hotels, vacation, tourism. |
| 12 | Einkaufen & Geld | 132 | 10 | Shopping, prices, banking, paying, contracts, budgets. |
| 13 | Stadt, Ämter & Recht | 143 | 11 | City life, government offices, bureaucracy, police, law, crime. |
| 14 | Arbeit & Beruf | 138 | 11 | Jobs, workplace, careers, hiring/firing, professions. |
| 15 | Schule & Bildung | 84 | 7 | School, university, courses, exams, learning. |
| 16 | Freizeit, Medien & Technik | 214 | 17 | Hobbies, sport, TV/film/music, art, gadgets, the internet. |
| 17 | Gefühle & Charakter | 115 | 9 | Emotions and personality traits. |
| 18 | Kommunikation & Post | 184 | 14 | Talking, phoning, writing letters/emails, the postal system, news media. |
| 19 | Zeit & Kalender | 139 | 11 | Time expressions, calendar, daily routine, punctuality (now also carrying the ~48 pure time-adverbs formerly stranded in the grammar mega-topic). |
| 20 | Gesellschaft, Politik & Wirtschaft | 20 | 2 | Society, politics, economy — the smallest topic; most B1 words here are abstract enough to also fit Stadt/Ämter or Denken. |
| 21 | Menge, Maß & Eigenschaften | 133 | 12 | Size, quantity, quality judgments and descriptive adjectives (`groß/steil/teuer/stark`…). Closed-class determiners & degree-particles that had been dumped here (`sämtliche, insgesamt, all-, ziemlich, genug, absolut, -weise`…) were swept out to the glue pool; the depictable adjectives stay. |
| 22 | Handlungen: Alltagsverben | 204 | 16 | The general-purpose verb toolkit — give/take, fix, organize, react. Now also home to the **position/movement verbs** (`stehen/liegen/setzen/stellen/hängen/stecken/sitzen/legen` + `entgegenkommen`, with dimensions `nah/weit/lang`) in a "moving day" scene — the depictable half of the dissolved Raum & Richtung topic. |
| 23 | Denken, Wissen & Meinen | 153 | 12 | Mental verbs: think, know, decide, remember, doubt, agree (all open-class, grounded in situations). Connective adverbs `einerseits/ausschließlich` were swept to the glue pool. |
| — | **⟶ Shared glue pool** (see `glue-pool.md`) | 326 | — | **Not scened.** All closed-class function words — prepositions, conjunctions, pronouns, determiners, particles, question words, directional adverbs, modal/aux verbs — no mental picture, so no standalone scenes. Woven through every batch's texts, repeated freely, tracked to 100%. Absorbs former Batches 25 + 26, the **dissolved Batch 24** (70 prepositions/adverbs), and closed-class stragglers swept from Batches 21 & 23. |
| | **Total: 23 scene-topics + pool** (intentional cross-topic duplicates, see §4) | **2865** distinct (2542 scened + 326 pooled, overlaps shared) | **204** scenes | |

## 3. Assignment strategy

**Unambiguous words** (concrete nouns/verbs clearly of one domain — `der Teppich`, `die Bäckerei`, `der Bahnhof`) were assigned straight to their obvious topic.

**Fine-grained carve-outs** (new in this merged version, absorbed from agent A): color/shape/material adjectives (`bunt`, `rund`, `der Kreis`, `das Material`…) and danger/emergency vocabulary (`die Gefahr`, `der Notfall`, `retten`, `warnen`…) each get their own dedicated topic instead of being scattered across Menge/Wohnung/Körper/Stadt/Gefühle. Both are small (38 and 41 words) but tight and highly imaginable as their own cram batches.

**Generic / abstract content words** (verbs like `machen`, `bringen`; adjectives like `gut`, `schwer`; nouns like `die Lage`, `der Sinn`) go into three purpose-built topics: **Handlungen: Alltagsverben** (general-purpose action verbs), **Menge, Maß & Eigenschaften** (size/quality judgments), **Denken, Wissen & Meinen** (mental verbs). Each is still fully scene-outlined, same as a concrete topic like Tiere.

**Function / grammar words** — the hardest case, and the one place this merge changes B's original strategy most. Rather than one 360-word "Grammatik & Verbindungswörter" mega-topic, the words are split three ways **by grammatical role**, adopted from agent C's taxonomy (`JUDGE.md` item 1):

- **Raum & Richtung — dissolved.** Its spatial prepositions (`an/auf/hinter/über/zwischen`) and direction adverbs (`da/dort/oben/unten/rechts`) are closed-class function words with no depictable referent, so they went to the **glue pool** rather than getting forced scenes. The position verbs they co-occur with (`stehen/liegen/setzen/stellen/hängen/stecken/sitzen/legen` + `entgegenkommen`) and the dimensions `nah/weit/lang` are depictable, so they moved to a real "Der Umzugstag" (moving day) scene under **Handlungen** — where the spatial vocabulary gets used *in* a picture, exactly as it will in the finished texts.
- **Logik & Verbindungen** — causal/conditional/concessive connectors (`weil/obwohl/trotzdem/falls/dass/ob/sondern`) plus a `Bedingung/Ausnahme/Folge/Voraussetzung` cluster pulled in from Denken and Handlungen, so the natural "debate the exact conditions for an exception" scene has its whole vocabulary in one place (see the lifted premise in §5, scene 3).
- **Grammatik-Glue** — pronouns, articles, modal particles, degree adverbs, question words, and the highest-frequency light/modal verbs (`sein/haben/machen/gehen/können…`). Politeness words (`bitte/bitten/danke/danken/dankbar`) were moved out to Kommunikation instead, where the politeness-loop scene (§5) actually needs them next to `sich bedanken`.

Within every topic — including all three grammar splits and the two new carve-outs — words are grouped **by semantic/grammatical sub-function inside each scene, not alphabetically**: this is the feature that won the comparison in `JUDGE.md` (axis 3, "Scene outlines"), and it is kept and extended here, not diluted by the restructuring.

**Near-partition, not a strict one:** each word gets one home topic by default. A handful of words are deliberately placed in a second topic because they genuinely power two different scene types (e.g. `der Bus` in both Unterwegs/Verkehr and Reisen/Urlaub). Listed in §4.

## 4. Coverage audit

**Re-run from scratch after every reshuffle** (the Farben/Gefahr carve-outs and the three-way grammar split move ~230 words between topics, so coverage from before the merge cannot simply be assumed to still hold). Verified two ways:

1. **Topic-level**: every topic's word list matched back against the canonical 2,886-row lemma set by exact string, consuming one CSV row per match (duplicate-string rows — see the homonym list below — are disambiguated by row index, not string, so each of the two rows lands separately).
2. **Scene-level**: independently re-collected every one of the 228 scenes' literal `Words (n): …` lists and asserted the multiset is identical to the topic-level word lists — i.e. topic assignment and rendered scene content cannot silently drift apart (this check caught and fixed two real reshuffling bugs during this merge: `rein/waagerecht/der Kreis/laut/die Form/parallel` briefly double-counted between Farben and the old grammar subgroup data, and `bitte` briefly duplicated between Grammatik and Kommunikation — both fixed before this file was generated).

- Total entries: **2886**
- Assigned (unique rows covered): **2886**
- Unassigned: **0**

**No unassigned entries.**

**Standard German only (scope, not coverage).** Assignment covers all 2886 rows, but the
texts teach the D side of the list's regional doublets. The ledger tags every entry with
its CSV region and excludes the **54 A/CH-only** entries (`die Stiege`, `das Eck`,
`der Fauteuil`, `der Erdapfel`, `das Velo`, `parkieren`…) from the batches' target lists —
Batch 3 (Essen) loses the most at 19, Batch 1 five. Entries tagged `(D, A)` or `(D, CH)`
are standard German and stay. See `vocab.py words --batch N --regional`.

**Homonym / regional-variant doublets** — CSV rows that share an identical lemma string but are genuinely two different entries (different meaning or different plural), each verified to land on its own row via index-based matching, not string matching:

- `der Ausdruck` — printout (Ausdrucke) vs. linguistic expression (Ausdrücke) — different plurals in the source
- `die Straßenbahn` — plain entry vs. the (D/A) entry cross-referencing CH "Tram"
- `die U-Bahn` — two identical rows in the source list
- `die Bank` — bench (Bänke) vs. financial bank (Banken)
- `das Eis` — ice vs. ice cream — plain entry vs. the regional-variant (CH "Glace") entry
- `fahren` — the plain verb vs. the separable (herunter-)fahren entry
- `die Fahrkarte` — two rows, each cross-referencing a different CH "Billet(t)" spelling
- `geschieden` — appears twice (adjective "divorced", used in two different collocations)
- `der Kasten` — cabinet/crate (D) vs. cupboard (A/CH) — two different regional senses
- `kosten` — to cost vs. the Austrian regional sense "to taste" (→ probieren)
- `die Ordination` — → Praxis vs. → Sprechstunde — two different Austrian cross-references
- `der Vorort` — two identical rows in the source list
- `der Wohnort` — two identical rows in the source list
- `die Pension` — boarding house vs. → Rente (retirement) — two different senses
- `die Praxis` — plain entry vs. the entry cross-referencing Austrian "Ordination"
- `probieren` — plain entry vs. the (D/CH) entry cross-referencing Austrian "kosten"
- `das Rad` — plain entry vs. the (D/A) entry cross-referencing "Fahrrad"/CH "Velo"
- `zuschauen` — plain entry vs. the fully-conjugated entry
- `der Sessel` — armchair (D/CH, → Fauteuil) vs. chair (A, → Stuhl) — two different regional senses
- `das Wort` — Worte (words in a speech) vs. Wörter (individual words) — different plurals
- `zurzeit` — a genuine duplicate row in the official list itself (not a homonym) — both instances covered, see Methodology

**Words intentionally placed in more than one topic** (26), because they genuinely power two different scene types (this is separate from the homonym list above, which is about the source data, not editorial choice):

<details><summary>show the 26 cross-topic words</summary>

- `abheben` — Handlungen: Alltagsverben, Einkaufen & Geld
- `abnehmen` — Handlungen: Alltagsverben, Körper & Gesundheit
- `ausmachen` — Handlungen: Alltagsverben, In der Wohnung & Zuhause
- `beißen` — Gefühle & Charakter, Körper & Gesundheit
- `bevor` — Zeit & Kalender, Logik & Verbindungen
- `beweisen` — Denken, Wissen & Meinen, Stadt, Ämter & Recht
- `bitter` — Einkaufen & Geld, Essen, Kochen & Restaurant
- `buchen` — Schule & Bildung, Reisen & Urlaub
- `dankbar` — Gefühle & Charakter, Kommunikation & Post
- `das Brot` — In der Wohnung & Zuhause, Essen, Kochen & Restaurant
- `das Diplom` — Freizeit, Medien & Technik, Arbeit & Beruf
- `dekorieren` — Freizeit, Medien & Technik, Handlungen: Alltagsverben
- `der Bus` — Unterwegs & Verkehr, Reisen & Urlaub
- `der Kellner / die Kellnerin` — Gefühle & Charakter, Arbeit & Beruf
- `der Täter / die Täterin` — Stadt, Ämter & Recht, Arbeit & Beruf
- `die Auskunft` — Kommunikation & Post, Reisen & Urlaub
- `die Ausnahme` — Einkaufen & Geld, Logik & Verbindungen
- `die Bevölkerung` — Familie & Beziehungen, Gesellschaft, Politik & Wirtschaft
- `die Bibliothek` — Schule & Bildung, Freizeit, Medien & Technik
- `die Biologie` — Schule & Bildung, Freizeit, Medien & Technik
- `die Bohne` — Einkaufen & Geld, Essen, Kochen & Restaurant
- `diesmal` — Zeit & Kalender, Zeit & Kalender
- `doch` — Denken, Wissen & Meinen, Logik & Verbindungen
- `installieren` — Freizeit, Medien & Technik, Stadt, Ämter & Recht
- `schneien` — Handlungen: Alltagsverben, Natur, Wetter & Umwelt
- `vertrauen` — Gefühle & Charakter, Grammatik-Glue (Pronomen, Partikeln, Kernverben)

</details>

## 5. Scene-idea bank (non-binding)

**These outlines are inspiration, not instructions.** They were generated against a
retired build in which each topic's words were sorted alphabetically and cut into
thirteen-word slices, one "scene" per slice — which is why the premises below no longer
carry word lists: the groupings they were written for grouped nothing. Words that share a
first letter share nothing else, and texts written from such a slice read like a
vocabulary list with quotation marks around it.

**Where the words live now.** Every word's topic assignment, forms, gloss, frequency band
and coverage state is in the ledger — `curriculum/vocab.db`, seeded from the diffable
`curriculum/assignments.tsv`, queried with `tools/vocab.py`:

```bash
python3 tools/vocab.py status                 # coverage across all 23 batches + the pool
python3 tools/vocab.py words --batch 3        # everything the batch has to cover
python3 tools/vocab.py glue --open            # function words no text has used yet
```

**How a batch is written.** Scenes are designed fresh, per batch, by grouping the batch's
words by *situation* — then drafted in three passes (initial draft → review and
enrichment → final pass), each of which puts naturalness first. The full procedure,
formats and rules live in the **`text-writer` skill** (`.claude/skills/text-writer/`).
90–95% coverage with dialogues that sound spoken beats 100% that sounds like an inventory.

Raid the premises below freely for a situation that fits a grouping you designed — or
ignore them and invent your own.

### Stage A. Konkret & körperlich (start here)

#### Batch 1. In der Wohnung & Zuhause  _148 words_

**Scene 1: Der Einzugstag**
- Premise: Someone moves into a new, mostly empty apartment, cheerfully naming every room out loud like a tour guide.
- Comedic angle: The 'apartment tour' for a single friend takes twenty minutes because they insist on describing the closet too.

**Scene 2: Die improvisierte Küche**
- Premise: A cramped student apartment's kitchen doubles as living room, with furniture crammed wherever it fits.
- Comedic angle: The couch and the fridge are pushed so close together that opening either requires teamwork.

**Scene 3: Der Balkon-Pooltag**
- Premise: Neighbors improvise a tiny inflatable pool on a cramped balcony during a heatwave.
- Comedic angle: The garden hose fills it just as someone below opens their window directly underneath.

**Scene 4: Die Heizungsreparatur**
- Premise: A landlord tries to fix a broken heater himself instead of calling a professional.
- Comedic angle: He ends up needing the actual repairman anyway, plus a new toolbox after breaking most of the old one.

**Scene 5: Der Dachbodenfund**
- Premise: Someone clears out a cluttered attic and stumbles on a chair so old it might be an antique.
- Comedic angle: It collapses the moment anyone actually sits on it.

**Scene 6: Der Frühjahrsputz-Marathon**
- Premise: A roommate deep-cleans the whole apartment in one obsessive afternoon.
- Comedic angle: They find three missing spoons, one shoe, and no explanation for either.

**Scene 7: Das Möbelaufbau-Chaos**
- Premise: Two friends try assembling flatpack furniture without reading the instructions.
- Comedic angle: The finished 'bookshelf' looks suspiciously like a wobbly ladder.

**Scene 8: Der Frühlingsputz im Wohnzimmer**
- Premise: A family reorganizes the living room, disagreeing about furniture placement the whole afternoon.
- Comedic angle: By evening the room is back in almost the exact same layout it started in.

**Scene 9: Der Schlüsselverlust**
- Premise: Someone locks themselves out and has to improvise entry through increasingly ridiculous methods.
- Comedic angle: The spare key turns out to have been in their pocket the entire time.

**Scene 10: Der gemütliche Fernsehabend**
- Premise: Friends gather in a living room stuffed with mismatched furniture for movie night.
- Comedic angle: Someone insists the ancient, creaky armchair is 'the good one' and fights anyone who sits in it.

**Scene 11: Der Umzugswagen**
- Premise: A family loads a moving truck, arguing over how to fit oversized furniture through narrow doors.
- Comedic angle: The wardrobe barely fits by being tilted at an almost comedic forty-five-degree angle.


#### Batch 2. Körper & Gesundheit  _128 words_

**Scene 1: Der Hausarztbesuch**
- Premise: Someone describes a minor ailment to the doctor with wildly exaggerated symptoms.
- Comedic angle: The doctor's diagnosis is simply 'you need more sleep,' delivered with visible exhaustion of their own.

**Scene 2: Der Marathon-Trainingsunfall**
- Premise: An overambitious first-time runner overdoes their training and ends up hilariously sore.
- Comedic angle: They can't climb stairs the next day and have to be helped by a very unimpressed roommate.

**Scene 3: Die Erkältungswelle im Büro**
- Premise: An entire office catches the same cold within days, each person insisting theirs is the worst case.
- Comedic angle: The healthiest-looking person turns out to be the one who's been secretly suffering the most.

**Scene 4: Der Selbstdiagnose-Notfall**
- Premise: Someone convinces themselves they have a serious illness after reading symptoms online.
- Comedic angle: The actual diagnosis is just needing to drink more water.

**Scene 5: Der Krankenhausbesuch bei Oma**
- Premise: Grandchildren visit a grandparent recovering from a minor procedure in the hospital.
- Comedic angle: The grandparent is more worried about missing their favorite TV show than about their own recovery.

**Scene 6: Der Notaufnahme-Fehlalarm**
- Premise: A minor kitchen accident sends someone rushing dramatically to the emergency room.
- Comedic angle: The injury turns out to need nothing more than a small bandage, applied in thirty seconds.

**Scene 7: Die Zahnarztangst**
- Premise: Someone works themselves into a panic before a routine dental checkup.
- Comedic angle: The appointment is over before they've even finished nervously rambling in the waiting room.

**Scene 8: Der Physiotherapietermin**
- Premise: A patient exaggerates every small movement during a physical therapy session for sympathy.
- Comedic angle: The therapist calmly points out they were sprinting fine in the parking lot minutes earlier.

**Scene 9: Der Yoga-Kurs für Anfänger**
- Premise: A stiff beginner struggles hilariously through a gentle yoga class meant for relaxation.
- Comedic angle: Their idea of the 'child's pose' looks suspiciously like they've simply fallen asleep.

**Scene 10: Die Familiengeschichte über Uroma**
- Premise: Relatives tell exaggerated stories about a great-grandmother's supposedly dramatic health scares.
- Comedic angle: Every retelling makes the illness sound more serious than the doctor's actual, mild diagnosis.


#### Batch 3. Essen, Kochen & Restaurant  _149 words_

**Scene 1: Der Bäckerei-Notfall**
- Premise: Someone bakes bread for the first time and it comes out looking nothing like the recipe photo.
- Comedic angle: They serve it anyway, confidently calling the brick-like loaf 'rustic'.

**Scene 2: Der Café-Vormittag**
- Premise: Friends meet at a café for coffee and end up arguing playfully about the 'correct' way to eat an egg.
- Comedic angle: The debate escalates until the whole café is quietly listening in, amused.

**Scene 3: Das Grillfest der Nachbarn**
- Premise: A neighborhood barbecue turns chaotic as everyone insists on grilling their own dish their own way.
- Comedic angle: The grill catches a small, dramatic flare-up right as the 'grill master' is bragging about his technique.

**Scene 4: Die Kochshow-Parodie**
- Premise: Friends film a silly homemade cooking show, narrating dramatically over a very simple dish.
- Comedic angle: The 'secret ingredient' reveal is just regular salt, treated like a plot twist.

**Scene 5: Der Fast-Food-Notstand**
- Premise: A group debates for way too long over a simple fast-food order, changing their minds constantly.
- Comedic angle: By the time they finally order, the kitchen is already closing.

**Scene 6: Die Familienrezept-Weitergabe**
- Premise: A grandmother tries to teach her grandchild a traditional recipe with wildly imprecise, old-fashioned measurements.
- Comedic angle: 'A handful' and 'until it feels right' turn out to be the only actual instructions given.

**Scene 7: Der Marmeladen-Wettbewerb**
- Premise: Neighbors compete in an amateur jam-making contest with fiercely guarded secret recipes.
- Comedic angle: The 'secret ingredient' in the winning jam turns out to be a happy accident nobody can replicate again.

**Scene 8: Das internationale Buffet**
- Premise: A potluck dinner features dishes from many countries, with each guest passionately defending their own.
- Comedic angle: The most popular dish by far is the one nobody can identify or pronounce.

**Scene 9: Die Restaurantkritik-Parodie**
- Premise: An amateur food blogger dramatically reviews a very ordinary neighborhood restaurant.
- Comedic angle: Their five-paragraph review is entirely about the bread basket.

**Scene 10: Der zu scharfe Wettkampf**
- Premise: Friends challenge each other to eat increasingly spicy food at a competitive dinner.
- Comedic angle: The self-proclaimed 'spice champion' taps out first, dramatically reaching for the entire milk carton.

**Scene 11: Der Kellner-Ausbildungstag**
- Premise: A trainee waiter fumbles through their first shift, mixing up every order at the table.
- Comedic angle: They somehow end up serving dessert before the appetizer, and the guests decide they actually prefer it that way.

**Scene 12: Der Weinkeller-Ausflug**
- Premise: Friends tour a small local winery, pretending to be much more sophisticated tasters than they actually are.
- Comedic angle: Their elaborate tasting notes are all suspiciously similar to 'tastes like grapes.'


#### Batch 4. Tiere  _8 words_

**Scene 1: Der chaotische Bauernhofbesuch**
- Premise: City visitors help feed animals on a farm and immediately get overwhelmed by an overeager goat.
- Comedic angle: The goat steals someone's hat and proudly parades around the pen wearing it like a trophy.


#### Batch 5. Kleidung & Aussehen  _44 words_

**Scene 1: Die Modenschau im Wohnzimmer**
- Premise: Friends stage a silly homemade fashion show using thrift-store finds and bedsheets as capes.
- Comedic angle: The 'showstopper outfit' is just someone wrapped entirely in a shower curtain, strutting confidently.

**Scene 2: Der Frisörbesuch, der schiefging**
- Premise: Someone asks for a small trim and ends up with a dramatically different haircut.
- Comedic angle: They insist they 'meant to do that' to everyone who asks, unconvincingly.

**Scene 3: Der Kleiderschrank-Notstand**
- Premise: Someone digs through an overstuffed wardrobe trying to find one specific missing item before a party.
- Comedic angle: They find seventeen single socks and not one matching pair.


#### Batch 6. Farben, Formen & Material  _41 words_

**Scene 1: Der Regenbogen-Kinderzimmerstreit**
- Premise: A painter lets a child help choose the color for their newly redecorated bedroom.
- Comedic angle: The child insists on every color at once, and the finished wall ends up looking like a rainbow-colored traffic accident.

**Scene 2: Die endlose Musterkollektion**
- Premise: A furniture designer presents an overwhelming set of material and finish swatches to a hopelessly indecisive client.
- Comedic angle: The client can't choose between two nearly identical shades and debates it for so long the showroom closes around them.

**Scene 3: Der Bauklötze-Turm**
- Premise: A child builds an ambitious block tower using every geometric shape and material they can get their hands on.
- Comedic angle: The tower becomes so bizarre and lopsided that nobody can tell anymore whether it's supposed to be a house or a tower.


#### Batch 7. Familie & Beziehungen  _107 words_

**Scene 1: Das Familientreffen im Altersheim**
- Premise: Several generations gather to visit a grandparent, and everyone tells wildly different versions of family history.
- Comedic angle: The grandmother insists she remembers everyone's age wrong, on purpose, just to see their reactions.

**Scene 2: Die Hochzeitsvorbereitung**
- Premise: A couple's engaged relatives argue over wedding invitations and seating charts for cousins nobody's met.
- Comedic angle: The seating chart ends up requiring a whiteboard the size of a door.

**Scene 3: Die Geburtstagsüberraschung**
- Premise: Friends plan a surprise party but keep almost giving it away through terrible acting.
- Comedic angle: The 'surprised' birthday person had actually known for a week and pretends convincingly anyway.

**Scene 4: Die Jugendliebe-Geschichte**
- Premise: An older relative tells an embellished story about their teenage romance at a family dinner.
- Comedic angle: Every retelling adds a new dramatic detail that definitely wasn't there the first time.

**Scene 5: Der erste Kindergartentag**
- Premise: Parents nervously drop off their child at kindergarten for the first time.
- Comedic angle: The child is completely fine; it's the parents who need consoling in the parking lot.

**Scene 6: Die Großfamilien-Reise**
- Premise: A sprawling extended family plans a group trip and can't agree on anything.
- Comedic angle: The final itinerary satisfies literally nobody but somehow makes everyone equally happy about that.

**Scene 7: Die Rentnerclub-Runde**
- Premise: Retirees gather weekly, gently teasing each other about health, memory, and old family gossip.
- Comedic angle: Nobody can actually remember what the running joke was originally about, but they laugh anyway.

**Scene 8: Die Versöhnung nach dem Streit**
- Premise: A couple works through a small disagreement, over-apologizing in increasingly formal language.
- Comedic angle: The 'serious conflict' turns out to be about whose turn it was to walk the dog.


#### Batch 8. Gefahr, Notfall & Sicherheit  _38 words_

**Scene 1: Die Feuerwehrübung in der Turnhalle**
- Premise: A volunteer fire brigade simulates a small kitchen fire inside the gym for a very serious training day.
- Comedic angle: The instructor himself panics and shouts the wrong instructions, sending everyone fleeing the wrong way from a smoke machine that barely smokes at all.

**Scene 2: Die übertriebene Rettungsübung am Strand**
- Premise: A lifeguard trainee practices a rescue drill on the beach with an overly dramatic volunteer playing the drowning victim.
- Comedic angle: The 'victim' overacts his panic so convincingly that he nearly sinks the actual rescue attempt for real.

**Scene 3: Die Sicherheitseinweisung im Büro**
- Premise: A new safety officer walks bored new employees through the emergency exits and fire-drill procedure.
- Comedic angle: The one employee who takes it all deadly seriously gets hilariously lost during the actual drill and has to be rescued himself.


### Stage B. Situativ & alltagsweltlich

#### Batch 9. Natur, Wetter & Umwelt  _97 words_

**Scene 1: Der Gewitter-Campingausflug**
- Premise: Campers set up a tent just as dark clouds roll in over a riverside meadow.
- Comedic angle: The tent collapses the second the first raindrop hits, in front of a very unimpressed audience of ducks.

**Scene 2: Der Bauernhofbesuch**
- Premise: City kids visit a farm and are baffled by basic country facts everyone else takes for granted.
- Comedic angle: One insists the potatoes 'grow on trees' until the farmer patiently digs one up to prove otherwise.

**Scene 3: Die Bergwanderung mit Aussicht**
- Premise: Hikers finally reach a mountain viewpoint after a long climb, awestruck by the view.
- Comedic angle: The view is immediately ruined by a cloud rolling in the second everyone gets their camera out.

**Scene 4: Die Autopanne auf dem Land**
- Premise: A car breaks down on a rural road near a harbor town, and the driver has to improvise repairs.
- Comedic angle: The 'repair' involves duct tape, a farmer's advice, and a suspicious amount of luck.

**Scene 5: Die Seefahrt bei Nebel**
- Premise: A small boat trip gets eerily foggy, and the crew navigates mostly by guesswork and superstition.
- Comedic angle: They 'discover' a mysterious island that turns out to be the same dock they left from.

**Scene 6: Der Strandtag mit Überraschungen**
- Premise: A beach day turns chaotic as the tide comes in faster than anyone expected.
- Comedic angle: Someone's sandcastle empire is swallowed by the sea mid-victory-speech.

**Scene 7: Die Sternennacht im Tal**
- Premise: Friends camp in a valley and try (badly) to identify constellations.
- Comedic angle: Every single 'star' they point at turns out to be a distant airplane.

**Scene 8: Der plötzliche Wetterumschwung**
- Premise: A picnic gets abruptly interrupted by wind and clouds rolling in from nowhere.
- Comedic angle: The tablecloth becomes an impromptu kite, sailing off with half the sandwiches still on it.


#### Batch 10. Unterwegs & Verkehr  _112 words_

**Scene 1: Die Fahrschulprüfung**
- Premise: A nervous learner driver takes their test, narrating every action to the instructor out loud.
- Comedic angle: They announce the seatbelt three times before actually buckling it, stalling the car twice in a one-way street.

**Scene 2: Der verpasste Flug**
- Premise: A family sprints through an airport trying to catch a departing flight after misreading the schedule.
- Comedic angle: Dad insists the pilot will 'definitely wait for us' while dragging a suitcase that keeps popping open.

**Scene 3: Die Bahnhofsverwirrung**
- Premise: A tourist tries to find the right platform among S-Bahn, U-Bahn and long-distance trains, asking everyone for help.
- Comedic angle: Three different strangers give three contradictory directions, and he ends up on all three trains in one hour.

**Scene 4: Der Fahrradkurier im Stress**
- Premise: A bike courier weaves through pedestrian zones and speed limits while narrating a running commentary of near-misses.
- Comedic angle: He nearly flattens a jogger, apologizes over his shoulder, and speeds off unbothered.

**Scene 5: Der Anfängerlotse**
- Premise: A backseat driver gives contradictory turn-by-turn directions during a road trip, causing chaos at every curve.
- Comedic angle: They end up doing a full loop and passing the same lift-bridge twice.

**Scene 6: Die Motorradpanne**
- Premise: A motorcycle breaks down mid-trip, and the rider has to hitch a ride while pushing it through a parking lot.
- Comedic angle: A stranger's car ends up towing it with a rope that snaps hilariously at the worst possible moment.

**Scene 7: Die Fahrradtour zur Altstadt**
- Premise: A group cycles into the historic city center, arguing over the map and getting stuck in a tight lane.
- Comedic angle: One cyclist's backpack knocks over an entire café's outdoor seating on the way past.

**Scene 8: Die Tankstellenpanne**
- Premise: A driver's car sputters into a gas station on fumes right as a huge traffic jam forms on the highway overpass.
- Comedic angle: He accidentally puts the wrong fuel in and has to call for help, blocking the pump for everyone else.

**Scene 9: Die Umleitung ins Nirgendwo**
- Premise: A detour sign sends drivers on a bizarre loop through a town, ending up back where the traffic jam started.
- Comedic angle: By the fifth roundabout, the driver starts recognizing the same dog on the same corner.


#### Batch 11. Reisen & Urlaub  _54 words_

**Scene 1: Der Packstress vor der Abreise**
- Premise: Someone tries to pack for a trip at the last minute, throwing random items into an overstuffed suitcase.
- Comedic angle: They forget the actual passport but somehow remember three different chargers for devices they don't own.

**Scene 2: Die Hotelverwechslung**
- Premise: A family arrives at what they think is their booked hotel, only to find it's the wrong one entirely.
- Comedic angle: The actual hotel turns out to be a tiny, forgotten guesthouse two streets away with a much better breakfast.

**Scene 3: Der Rentnerausflug ans Meer**
- Premise: A group of retirees goes on a seaside excursion, bickering affectionately about every stop on the itinerary.
- Comedic angle: Their strict schedule gets completely derailed by an impromptu ice cream stop that everyone secretly wanted anyway.

**Scene 4: Die Heimreise-Odyssee**
- Premise: A trip home gets delayed by every possible transport mishap in a row.
- Comedic angle: By the time they finally arrive, they've told the story so many times it's grown into an epic saga.


#### Batch 12. Einkaufen & Geld  _132 words_

**Scene 1: Der Ausverkaufstag**
- Premise: Shoppers scramble through a chaotic sale, grabbing discounted items faster than they can decide if they want them.
- Comedic angle: Two strangers end up in a polite but intense tug-of-war over the same discounted lamp.

**Scene 2: Die Wochenendeinkäufe**
- Premise: A family does the weekly grocery run on a tight budget, calculating every item's cost out loud.
- Comedic angle: Dad's strict budgeting collapses the second he sees the bakery section.

**Scene 3: Der erste Gehaltscheck**
- Premise: A new employee obsessively checks their bank account after receiving their first paycheck.
- Comedic angle: They immediately spend it all on something wildly impractical out of sheer excitement.

**Scene 4: Die verwirrende Bankfiliale**
- Premise: Someone tries to open an account and gets lost in an endless maze of forms and machines.
- Comedic angle: The ATM eats the card, the counter sends them back to the ATM, and the loop never ends.

**Scene 5: Der Flohmarktverkäufer**
- Premise: An overenthusiastic flea-market seller haggles wildly with every browsing customer.
- Comedic angle: He gives a heartfelt sales pitch for an obviously broken toaster as if it were a family heirloom.

**Scene 6: Der Kreditkartenschock**
- Premise: Someone opens their credit card statement and is horrified by a mysterious huge purchase.
- Comedic angle: It turns out to be their own forgotten online order from three months ago.

**Scene 7: Der Möbelmarkt-Vergleich**
- Premise: A couple compares prices between two furniture stores, debating every euro of difference.
- Comedic angle: They spend more time and money on coffee while deciding than they save on the actual furniture.

**Scene 8: Die Onlinebestellung geht schief**
- Premise: A customer tracks a delayed package obsessively, refreshing the tracking page every five minutes.
- Comedic angle: The package arrives completely crushed, containing a single, oddly undamaged rubber duck.

**Scene 9: Die Steuerprüfung im Supermarkt**
- Premise: Someone tallies receipts at the supermarket checkout, trying to stay under a strict weekly budget.
- Comedic angle: The final total is one cent over, and they have to put back a single item under everyone's judging eyes.

**Scene 10: Der Mietvertrag-Papierkram**
- Premise: A tenant signs a new lease, drowning in insurance, deposit, and payment paperwork.
- Comedic angle: They accidentally sign up for a service they never wanted just from clicking through forms too fast.


#### Batch 13. Stadt, Ämter & Recht  _143 words_

**Scene 1: Der Behördenmarathon**
- Premise: Someone spends an entire day bouncing between government offices trying to register a new address.
- Comedic angle: Each office sends them to a different building, and they end up back at the first one by closing time.

**Scene 2: Der Einbruch, der keiner war**
- Premise: Police investigate a reported break-in that turns out to be the homeowner's own forgotten spare key attempt.
- Comedic angle: The 'burglar' description perfectly matches the homeowner's own reflection in the window.

**Scene 3: Das Fundbüro-Chaos**
- Premise: A lost-and-found office is overflowing with bizarre unclaimed items nobody can explain.
- Comedic angle: Someone claims a lost umbrella that turns out to belong to someone else entirely, with an identical one.

**Scene 4: Die Ratsversammlung ums Wahrzeichen**
- Premise: A town council argues passionately over a minor local landmark's upkeep.
- Comedic angle: The heated debate turns out to be about a statue nobody can actually agree what it's supposed to depict.

**Scene 5: Die Straßensperrung wegen Königsbesuch**
- Premise: A small town prepares chaotically for a supposed royal visit that turns out to be a misunderstanding.
- Comedic angle: The 'king' is actually just a costumed actor for an unrelated event three streets over.

**Scene 6: Die Pressekonferenz im Rathaus**
- Premise: A mayor holds an overly formal press conference about a very minor town achievement.
- Comedic angle: The big announcement turns out to be about a new public bench.

**Scene 7: Der verlegte Reisepass**
- Premise: Someone frantically searches for their passport the night before a trip, tearing the apartment apart.
- Comedic angle: It was in their jacket pocket the entire time, worn the whole search.

**Scene 8: Die Verkehrskontrolle**
- Premise: A police officer stops a driver for a minor infraction, and the excuse offered gets more elaborate by the second.
- Comedic angle: The excuse eventually involves a very convincing but entirely fictional medical emergency.

**Scene 9: Der Gerichtssaal-Sketch**
- Premise: Friends stage a mock trial for a silly neighborhood dispute over a fence.
- Comedic angle: The 'jury' is a group of very serious-looking garden gnomes borrowed for the occasion.

**Scene 10: Der Ladendiebstahl-Verdacht**
- Premise: A shopkeeper suspiciously eyes a customer buying a huge, oddly specific pile of random items.
- Comedic angle: It turns out to be ingredients for the world's most impractical sandwich, not a heist.

**Scene 11: Die Unterschriftensammlung**
- Premise: A neighbor collects signatures for a petition about a trivial local issue with dramatic urgency.
- Comedic angle: Half the signatures turn out to be from the same person using slightly different handwriting.


#### Batch 14. Arbeit & Beruf  _138 words_

**Scene 1: Das Vorstellungsgespräch-Desaster**
- Premise: A job applicant tries to sound impressively experienced despite obvious nervousness in an interview.
- Comedic angle: He accidentally lists his hobby as 'work' three separate times before catching himself.

**Scene 2: Die Kündigungs-Überraschung**
- Premise: An employee dramatically quits a job they actually love, over a minor misunderstanding.
- Comedic angle: They immediately regret it and spend the rest of the day trying to un-quit as casually as possible.

**Scene 3: Der Streik in der Fabrik**
- Premise: Factory workers stage a good-natured strike over cafeteria food quality, complete with homemade signs.
- Comedic angle: Management resolves it instantly by simply improving the coffee, ending the strike in ten minutes.

**Scene 4: Der erste Arbeitstag**
- Premise: A nervous new hire tries to look competent on their very first day at an unfamiliar office.
- Comedic angle: They confidently sit at the CEO's desk, not realizing whose office it actually is.

**Scene 5: Die Firmengründung im Wohnzimmer**
- Premise: Two friends 'launch a company' from a cluttered living room with wildly ambitious plans.
- Comedic angle: Their entire business plan is written on the back of a pizza box.

**Scene 6: Die Beförderungsfeier**
- Premise: A workplace throws an overly enthusiastic party for a colleague's minor promotion.
- Comedic angle: The cake spells the wrong job title, and nobody has the heart to mention it.

**Scene 7: Der Werkstattbesuch**
- Premise: A mechanic explains an absurdly complicated car problem to a confused customer using props.
- Comedic angle: The 'complex diagnosis' turns out to be a coin stuck in the cup holder rattling around.

**Scene 8: Das Praktikum bei der Zeitung**
- Premise: An eager intern at a newspaper is assigned only trivial tasks despite grand journalistic ambitions.
- Comedic angle: Their first 'published' piece is just the weekly parking schedule notice.

**Scene 9: Der Radiosport-Kommentator**
- Premise: An overly dramatic amateur commentator narrates a minor local sports match like it's a world championship.
- Comedic angle: He gets more excited about the halftime snack break than the actual game.

**Scene 10: Die Bewerbungsmappe**
- Premise: Someone assembles an overly polished job application for a very casual part-time position.
- Comedic angle: The application is longer than the actual job description.

**Scene 11: Die Werkzeugkiste-Katastrophe**
- Premise: A handyman's disorganized toolbox causes chaos on a simple repair job.
- Comedic angle: He spends longer looking for the right tool than the actual repair would have taken.


#### Batch 15. Schule & Bildung  _84 words_

**Scene 1: Der verschlafene Prüfungstag**
- Premise: A student who overslept sprints to school, illustrations of the missed material scattered across the exam sheet.
- Comedic angle: He mixes up the diagram labels so badly the teacher isn't sure if it's biology or abstract art.

**Scene 2: Die Bibliotheksdurchsuchung**
- Premise: A student desperately searches the library for one specific book right before a deadline.
- Comedic angle: The book turns out to be checked out by the teacher who assigned the essay in the first place.

**Scene 3: Der Forschungsclub**
- Premise: An overambitious school club announces a grand research project with a fancy progress report.
- Comedic angle: Their big 'breakthrough' turns out to be reheated homework from last semester.

**Scene 4: Die Gedichtstunde**
- Premise: A patience-testing poetry class drags on while a bored student doodles instead of writing.
- Comedic angle: His 'poem' turns out to be one sentence repeated with different punctuation, and the teacher grades it anyway.

**Scene 5: Der Berufsschulmarathon**
- Premise: An apprentice bounces between shifts at the trade school and a part-time job, narrating an exhausting schedule.
- Comedic angle: He falls asleep mid-sentence during roll call and answers 'here' to someone else's name.

**Scene 6: Die Referatspanne**
- Premise: A student's presentation slides crash right as they start presenting to the whole class.
- Comedic angle: They improvise the entire university-level topic using only hand gestures and a marker on the whiteboard.

**Scene 7: Der Übersetzungsnotfall**
- Premise: A student mistranslates a foreign pen pal's letter so badly that the reply makes no sense at all.
- Comedic angle: The pen pal writes back thinking they've been challenged to a duel.


#### Batch 16. Freizeit, Medien & Technik  _214 words_

**Scene 1: Der Filmabend-Chaos**
- Premise: Friends try to film a home movie for a subscription channel, but nobody can operate the camera properly.
- Comedic angle: The 'star' of the film keeps accidentally walking out of frame to check her phone.

**Scene 2: Die Kunstausstellung**
- Premise: An amateur artist's gallery opening features one badly hung painting and a memorial plaque nobody understands.
- Comedic angle: A visitor mistakes the coat rack for an exhibit and starts seriously analyzing it.

**Scene 3: Der Streaming-Absturz**
- Premise: A group tries to binge-watch a show but the file keeps corrupting mid-scene.
- Comedic angle: They end up acting out the missing dialogue themselves, badly, in increasingly dramatic voices.

**Scene 4: Die improvisierte Geburtstagsfeier**
- Premise: The TV remote breaks right before a birthday party, so guests must operate everything manually.
- Comedic angle: Someone has to physically stand by the TV changing channels like a human remote control all night.

**Scene 5: Das Fotoshooting-Desaster**
- Premise: An amateur photographer tries to shoot a festival, but the equipment keeps malfunctioning at the worst moments.
- Comedic angle: Every 'perfect shot' turns out to have someone's thumb over the lens.

**Scene 6: Der Hobbykeller**
- Premise: A dad shows off his overstuffed hobby room full of half-finished projects and forgotten instruments.
- Comedic angle: He proudly demonstrates the guitar despite knowing exactly one chord.

**Scene 7: Der Technik-Support-Notruf**
- Premise: A grandparent calls for tech help installing an app, describing the problem in wildly wrong terms.
- Comedic angle: The 'broken phone' turns out to just be upside down the whole time.

**Scene 8: Das Heimkino-Upgrade**
- Premise: A couple assembles a home theater system, arguing over the instructions and mixing up all the cables.
- Comedic angle: The speakers end up playing the neighbor's WiFi-connected doorbell instead of the movie.

**Scene 9: Die Museumsführung**
- Premise: A overenthusiastic museum guide gives a tour that's more performance art than history lesson.
- Comedic angle: He recites a made-up backstory for a painting that's actually just a fire extinguisher on the wall.

**Scene 10: Das Konzert im Wohnzimmer**
- Premise: An amateur band records a music video in someone's cramped living room with all borrowed instruments.
- Comedic angle: The drummer keeps hitting the ceiling lamp on every beat.

**Scene 11: Die Quizshow-Aufnahme**
- Premise: Friends film their own homemade game show using a hand-drawn wheel and props from around the house.
- Comedic angle: The prize turns out to be a coupon for one free hug, and everyone still wants to win.

**Scene 12: Das Vereinsfest**
- Premise: A local sports club throws a chaotic celebration after an unlikely victory.
- Comedic angle: Their trophy is a repurposed pasta jar, and everyone toasts to it as if it were gold.

**Scene 13: Der Vereinssporttag**
- Premise: A workplace organizes an awkward team-sports day where nobody remembers the actual rules.
- Comedic angle: The 'referee' makes up new rules on the spot to settle every dispute in the funniest way possible.

**Scene 14: Der Theaterprobenabend**
- Premise: An amateur theater group rehearses a scene that keeps falling apart because of forgotten lines.
- Comedic angle: The lead actor starts improvising in rhyme just to keep going, and the director loves it too much to stop him.

**Scene 15: Die Stadtführung für Touristen**
- Premise: A tour guide leads visitors past famous landmarks, embellishing every fact more than the last.
- Comedic angle: By the final stop, the 'historic fountain' is apparently haunted by seventeen different ghosts.

**Scene 16: Das Fußballtraining**
- Premise: An amateur football coach tries to train a hopeless team using increasingly dramatic sports metaphors.
- Comedic angle: The team's biggest achievement of the day is not falling over during warm-up stretches.

**Scene 17: Der Zirkusbesuch**
- Premise: A family visits a slightly run-down circus with an over-the-top ringmaster.
- Comedic angle: The lion tamer's lion is clearly a very large, very unbothered house cat.


### Stage C. Emotional & kommunikativ

#### Batch 17. Gefühle & Charakter  _115 words_

**Scene 1: Die Achterbahnfahrt**
- Premise: Friends line up for a rollercoaster, each reacting to the fear in a wildly different way.
- Comedic angle: The one who claimed to be fearless screams the loudest the entire ride.

**Scene 2: Der peinliche Vorstellungsgesprächs-Traum**
- Premise: Someone recounts an embarrassing dream about a disastrous job interview at breakfast.
- Comedic angle: Everyone at the table admits they've had the exact same anxiety dream, in painfully specific detail.

**Scene 3: Die enttäuschte Kochshow**
- Premise: An amateur cook's ambitious dinner party dish collapses spectacularly right before guests arrive.
- Comedic angle: The backup plan, ordering pizza, turns out to be the guests' favorite part of the evening.

**Scene 4: Der Trostpreis**
- Premise: A friend loses a minor competition and everyone tries clumsily to cheer them up.
- Comedic angle: The 'consolation gift' is so absurd it accidentally becomes the highlight of their week.

**Scene 5: Die Dankesrede**
- Premise: Someone gives an overly emotional thank-you speech at a small local award ceremony.
- Comedic angle: They get so choked up over a minor certificate that people start crying along out of secondhand emotion.

**Scene 6: Der Kritikerclub**
- Premise: Friends review a terrible amateur film with theatrical, contradictory opinions.
- Comedic angle: The harshest critic turns out to be an uncredited extra in the film.

**Scene 7: Die Liebeserklärung im Regen**
- Premise: Someone plans a big romantic gesture that gets rained out and ruined step by step.
- Comedic angle: The soggy, disastrous version ends up being more memorable than the perfect plan ever would have been.

**Scene 8: Der Streit im Fahrstuhl**
- Premise: Two strangers get stuck in an elevator and slowly go from annoyed to oddly bonded.
- Comedic angle: By the time they're rescued, they've become unlikely best friends and exchange numbers.

**Scene 9: Die Wunschliste ans Universum**
- Premise: Friends write silly wish lists for the new year, half-joking, half-serious.
- Comedic angle: The most ridiculous wish on the list is the only one that actually comes true by year's end.


#### Batch 18. Kommunikation & Post  _184 words_

**Scene 1: Der Absender ohne Namen**
- Premise: A local reporter investigates a mysterious unmarked package delivered with no return address, his phone ringing nonstop mid-interview.
- Comedic angle: The anonymous sender turns out to be the reporter's own notoriously forgetful colleague, who mailed himself a reminder note and then completely forgot he'd done it.

**Scene 2: Die Anrufbeantworter-Odyssee**
- Premise: Someone leaves an increasingly rambling voicemail after being cut off mid-sentence multiple times.
- Comedic angle: The final voicemail is just them saying 'call me back' forty different ways.

**Scene 3: Der Buchstabierwettbewerb am Telefon**
- Premise: Someone tries to spell their complicated last name to a call center agent using the phonetic alphabet, badly.
- Comedic angle: Their invented code words ('B wie Banane') confuse the agent more than actual letters would.

**Scene 4: Die Entschuldigungskarte**
- Premise: A student writes an elaborate excuse note explaining a missed deadline.
- Comedic angle: The excuse is so overly detailed and dramatic that the teacher suspects it's fiction and grades it as a short story instead.

**Scene 5: Die Kündigungs-Dankesschleife**
- Premise: A customer calls to cancel a magazine subscription and thanks the clerk so profusely at every single step that she loses track of the actual request.
- Comedic angle: He says 'danke' so many times in a row that she assumes he loves the subscription and re-signs him up by accident.

**Scene 6: Der Radiomoderator im Praktikum**
- Premise: A nervous intern hosts their first live radio segment, stumbling over every hint and cue card.
- Comedic angle: Dead air strikes at the worst moment, filled only by his own audible panic breathing.

**Scene 7: Die Reklamations-Hotline**
- Premise: Someone calls customer support, getting passed between departments over a minor complaint.
- Comedic angle: By the third transfer they're talking to someone in a completely unrelated company.

**Scene 8: Die Dorfzeitung**
- Premise: A tiny local newsletter reports breathlessly on utterly mundane village events.
- Comedic angle: The 'breaking news' headline turns out to be about a cat stuck in a tree, again.

**Scene 9: Der Poesiealbum-Eintrag**
- Premise: Classmates write increasingly ridiculous entries in a friend's old-school memory book.
- Comedic angle: One entry is just a single word repeated in seventeen different colors.

**Scene 10: Der stille Streit**
- Premise: A couple has an argument entirely through passive-aggressive sticky notes instead of talking.
- Comedic angle: The notes escalate until one is just a single, silently furious exclamation mark.

**Scene 11: Der Umfrage-Stand in der Fußgängerzone**
- Premise: A market researcher tries to get busy pedestrians to answer a long survey.
- Comedic angle: Most answers are just people trying to walk away faster while still technically responding.

**Scene 12: Die Nachbarschaftsversammlung**
- Premise: Neighbors debate a trivial building issue with wildly exaggerated formality.
- Comedic angle: The vote on a broken doorbell somehow takes longer than actually fixing it would have.

**Scene 13: Die Wörterbuch-Rätselrunde**
- Premise: Friends play a game guessing definitions of obscure words from an old dictionary.
- Comedic angle: Someone's completely made-up fake definition wins the round because it sounded more convincing than the real one.

**Scene 14: Der Zeitschriften-Abo-Stapel**
- Premise: Someone finally sits down to sort through months of unread magazines and newsletters.
- Comedic angle: Every single one somehow already has next month's issue arriving at the same moment.


#### Batch 19. Zeit & Kalender  _139 words_

**Scene 1: Der Morgenmuffel**
- Premise: Someone struggles through their entire morning routine half-asleep, narrating each stumbling step.
- Comedic angle: They leave the house confidently before realizing they're still wearing slippers.

**Scene 2: Die Terminüberschneidung**
- Premise: Someone realizes they've double-booked two important events at the exact same time.
- Comedic angle: They try sprinting between both venues and end up fully missing one and half-attending the other.

**Scene 3: Die Silvesterfeier-Erinnerungen**
- Premise: Friends recount a wild New Year's Eve party, each remembering the timeline completely differently.
- Comedic angle: Nobody can agree what time the fireworks actually started, or who started them early by accident.

**Scene 4: Der ewig gleiche Tagesablauf**
- Premise: Someone complains about how monotonous their daily routine has become, describing it hour by hour.
- Comedic angle: The 'boring routine' includes an oddly specific daily argument with a stubborn printer.

**Scene 5: Die verpasste Deadline**
- Premise: Someone realizes far too late that an important deadline was actually yesterday, not today.
- Comedic angle: Their 'punctual' excuse email is sent exactly one minute before they finally notice the mistake.

**Scene 6: Der Startschuss zum Sommerfest**
- Premise: A neighborhood festival's opening ceremony is delayed repeatedly by small technical mishaps.
- Comedic angle: By the time the 'official start' finally happens, half the guests have already eaten all the food.

**Scene 7: Der Kalender voller Erinnerungen**
- Premise: Someone reviews an old calendar full of forgotten appointments and reminders scribbled in the margins.
- Comedic angle: One cryptic note just says 'don't forget!!' with no indication of what not to forget.

**Scene 8: Der Wecker-Kampf**
- Premise: Someone hits snooze on their alarm clock over and over, narrating each delay with a time adverb.
- Comedic angle: By 'irgendwann' it's already afternoon and they missed the whole day.

**Scene 9: Die Warteschlange beim Amt**
- Premise: People in a slow-moving government-office queue mutter time words about how long they've been waiting.
- Comedic angle: The person at counter one has apparently been 'gleich dran' for three years.

**Scene 10: Der Countdown zur Prüfung**
- Premise: A student obsessively tracks the time before an exam, narrating every stage of dread.
- Comedic angle: 'Zurzeit' revises nothing and just refreshes the clock app instead.

**Scene 11: Der Wiederholungstäter**
- Premise: A repeat-offender packrat keeps promising 'irgendwann' to clean the garage, one excuse per weekend.
- Comedic angle: Years pass; the garage now qualifies as an archaeological site.


#### Batch 20. Gesellschaft, Politik & Wirtschaft  _20 words_

**Scene 1: Die Nachbarschaftsdebatte**
- Premise: Neighbors from different backgrounds debate a minor community issue, each bringing in wildly broad arguments.
- Comedic angle: The debate about a shared garden fence somehow ends up covering the entire history of humanity.

**Scene 2: Der Wirtschaftsgipfel im Kleingarten**
- Premise: Allotment gardeners hold a mock 'economic summit' over how to divide a shared harvest fairly.
- Comedic angle: Their complex trade agreement collapses over who gets the last, biggest tomato.


### Stage D. Abstrakt & grammatisch (save for last)

#### Batch 21. Menge, Maß & Eigenschaften  _133 words_

**Scene 1 — *Größe, Form & Menge*: Der Möbelmess-Fehler**
- Premise: Someone measures a new wardrobe against the doorway, insisting it will 'definitely' fit.
- Comedic angle: It gets stuck at a comically awkward angle, blocking the hallway for the whole afternoon.

**Scene 2 — *Größe, Form & Menge*: Der Wettbewerb um die größte Kürbis**
- Premise: Neighbors compete in an amateur giant-vegetable growing contest, obsessing over every centimeter.
- Comedic angle: The 'winning' pumpkin turns out to be mostly held together with tape after a fall.

**Scene 3 — *Qualität & Bewertung*: Die Bewertungsshow**
- Premise: Friends host a mock talent show, giving overly dramatic, contradictory reviews of each act.
- Comedic angle: The 'perfect score' judge and the 'harshest critic' turn out to be scoring completely different performances by accident.

**Scene 4 — *Qualität & Bewertung*: Der Wertschätzungsstreit im Antiquitätenladen**
- Premise: A shop owner and a customer argue over whether an old vase is priceless or worthless.
- Comedic angle: It turns out to be a cheap souvenir, but both refuse to back down out of pure stubbornness.

**Scene 5 — *Qualität & Bewertung*: Der Fitnesstest**
- Premise: Friends attempt an informal strength and endurance test in the park, judging each other's fairness.
- Comedic angle: The self-proclaimed fittest one is out of breath after the warm-up alone.

**Scene 6 — *Grad & Vergleich*: Die Umfrage in der Fußgängerzone**
- Premise: A market researcher surveys passersby, comparing answers that all somehow contradict each other.
- Comedic angle: The 'average' answer ends up being something nobody actually said.

**Scene 7 — *Grad & Vergleich*: Die statistische Wette**
- Premise: Friends bet on percentages and averages during a football match, arguing over vague estimates.
- Comedic angle: Their 'exact calculations' turn out to be completely made up on the spot.

**Scene 8 — *Grad & Vergleich*: Der Übertreibungswettbewerb**
- Premise: Friends compete over who can tell the most exaggerated story about their weekend.
- Comedic angle: The most unbelievable story turns out to be completely true, to everyone's shock.

**Scene 9 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Materialtest im Baumarkt**
- Premise: A DIYer tests different materials' toughness by hitting, bending, and dropping samples in the aisle.
- Comedic angle: He accidentally proves the display shelf itself is the weakest material in the store.

**Scene 10 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Geschwindigkeitswettstreit**
- Premise: Friends race shopping carts through an empty parking lot, timing each other dramatically.
- Comedic angle: The 'fastest' one crashes spectacularly into a row of stacked crates at the finish line.

**Scene 11 — *Charakter von Dingen (Konsistenz & Tempo)*: Der Charaktertest beim Speeddating**
- Premise: At a speed-dating event, participants describe themselves using only vague personality adjectives.
- Comedic angle: Two people describe themselves identically and realize they're actually siblings.

**Scene 12 — *Charakter von Dingen (Konsistenz & Tempo)*: Die Gewohnheitsdebatte am Frühstückstisch**
- Premise: A couple argues gently over morning routines and small habits neither wants to change.
- Comedic angle: They discover after years together neither actually likes the habit they were defending.


#### Batch 22. Handlungen: Alltagsverben  _204 words_

**Scene 1 — *Verwaltung, Organisieren & Absprachen*: Die Bürobesprechung**
- Premise: An overly formal office meeting drags on with everyone stalling on trivial administrative details.
- Comedic angle: Someone spends ten minutes debating the correct procedure for booking a meeting room they're already sitting in.

**Scene 2 — *Verwaltung, Organisieren & Absprachen*: Der Kundendienstanruf**
- Premise: A customer service call goes in circles as the agent keeps transferring the caller between departments.
- Comedic angle: By the fourth transfer, the caller is talking to the same person who first picked up.

**Scene 3 — *Verwaltung, Organisieren & Absprachen*: Die Steuererklärung**
- Premise: Two roommates try to sort out a joint declaration, arguing over who's responsible for which forms.
- Comedic angle: They accidentally submit each other's tax numbers and spend the rest of the evening panicking.

**Scene 4 — *Geben, Nehmen & Besitzen*: Der Umzugstag**
- Premise: Friends help someone move apartments, constantly grabbing, carrying, and handing off boxes in a chaotic chain.
- Comedic angle: The heaviest box, labeled 'books', turns out to be full of bricks someone was keeping for no reason.

**Scene 5 — *Geben, Nehmen & Besitzen*: Die Rückgabe im Baumarkt**
- Premise: Someone tries to return a broken tool, carrying it awkwardly through the whole store looking for the right counter.
- Comedic angle: The 'broken' tool works perfectly the second the clerk touches it.

**Scene 6 — *Körperliche Alltagsaktionen*: Der Frühjahrsputz**
- Premise: A family does a chaotic spring cleaning, connecting hoses, printing labels, and losing patience with each other.
- Comedic angle: The dad insists on fixing the printer himself and ends up with more ink on his shirt than the page.

**Scene 7 — *Körperliche Alltagsaktionen*: Der WG-Streit ums Sofa**
- Premise: Roommates fight over a broken sofa, laughing, joking, and living around the mess instead of fixing it.
- Comedic angle: They eventually agree the sofa 'has character' and just cover the hole with a blanket forever.

**Scene 8 — *Körperliche Alltagsaktionen*: Der Gartentag**
- Premise: A family plants a garden while battling a garden hose that seems to have a mind of its own.
- Comedic angle: The hose sprays everyone except the actual plants, no matter how they aim it.

**Scene 9 — *Körperliche Alltagsaktionen*: Der Sporttag im Park**
- Premise: Friends organize an improvised race and jumping contest in the park, keeping score badly.
- Comedic angle: The self-declared 'winner' clearly fell down halfway through but insists it counts as style points.

**Scene 10 — *Körperliche Alltagsaktionen*: Die Bootsfahrt-Panne**
- Premise: A group tries to escape, dive, and swim their way out of a mishap on a leaky rented rowboat.
- Comedic angle: The 'life jacket' turns out to be a inflatable pool flamingo someone grabbed by mistake.

**Scene 11 — *Körperliche Alltagsaktionen*: Der Vergleichs-Streit unter Nachbarn**
- Premise: Two neighbors compare, argue, and pack up their yard sale items, trying to out-haggle each other.
- Comedic angle: They end up trading items back and forth so many times neither remembers who owns what anymore.

**Scene 12 — *Körperliche Alltagsaktionen*: Die Autowäsche**
- Premise: Friends wash a car in the driveway, getting distracted, spraying each other, and forgetting the actual car.
- Comedic angle: By the end the car is cleaner in one spot and filthier everywhere else than when they started.

**Scene 13 — *Bemühen, Wandel & Reaktion*: Der Renovierungsversuch**
- Premise: A couple tries fixing up an old apartment, changing plans mid-project and abandoning half-finished tasks.
- Comedic angle: The 'accent wall' ends up three different colors because nobody could agree and nobody wanted to repaint it.

**Scene 14 — *Bemühen, Wandel & Reaktion*: Die verspätete Rückkehr**
- Premise: Someone tries to make it home in time for dinner, juggling errands that keep piling up.
- Comedic angle: They arrive just as everyone else has finished eating and gone to bed.

**Scene 15 — *Bemühen, Wandel & Reaktion*: Die Reparaturwerkstatt**
- Premise: A DIY enthusiast tries fixing a broken appliance, changing his approach every five minutes.
- Comedic angle: He ends up with more screws left over than the appliance originally had.


**Scene 16 — *Positions- & Bewegungsverben*: Der Umzugstag**
- Premise: Movers arrange furniture in a new flat while everyone shouts contradictory instructions about where each piece goes.
- Comedic angle: The sofa gets moved three times because nobody agrees whether it should stand near or far from the window, and the long cable ends up wherever no one is standing.

#### Batch 23. Denken, Wissen & Meinen  _153 words_

**Scene 1 — *Meinen, Wissen & Überzeugen*: Der Debattierclub**
- Premise: An amateur debate club argues about a trivial topic as if the fate of the world depended on it.
- Comedic angle: Nobody actually knows what the original topic was anymore by round three.

**Scene 2 — *Meinen, Wissen & Überzeugen*: Die Gerichtsshow-Parodie**
- Premise: Friends stage a mock trial over who ate the last slice of cake, complete with dramatic evidence.
- Comedic angle: The 'evidence' is a single crumb, presented as if it were a smoking gun.

**Scene 3 — *Meinen, Wissen & Überzeugen*: Der Wissenschaftskongress im Kleinformat**
- Premise: A neighborhood science fair features wildly overconfident presentations of very small discoveries.
- Comedic angle: One 'researcher' presents his conclusion that his cat prefers Tuesdays, with full slideshow.

**Scene 4 — *Entscheiden, Planen & Feststellen*: Die Familienabstimmung**
- Premise: A family votes on where to go for vacation, and the decision keeps flip-flopping every five minutes.
- Comedic angle: The dog's random bark is treated as the deciding vote.

**Scene 5 — *Entscheiden, Planen & Feststellen*: Der Strategie-Brettspielabend**
- Premise: Friends plan an elaborate board game strategy, listing every possible outcome out loud.
- Comedic angle: Their meticulous plan collapses the instant someone rolls the wrong number.

**Scene 6 — *Erinnern, Entdecken & Verstehen*: Das Klassentreffen der Erinnerungen**
- Premise: Old classmates reunite and try to remember shared stories, each recalling a wildly different version.
- Comedic angle: Nobody can agree who actually won the legendary sack race from twenty years ago.

**Scene 7 — *Erinnern, Entdecken & Verstehen*: Die Schatzsuche im Dachboden**
- Premise: Someone rummages through the attic, discovering strange objects and inventing backstories for each.
- Comedic angle: A mysterious key turns out to open nothing more exciting than an old bike lock.

**Scene 8 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Verschwörungstheorie am Stammtisch**
- Premise: Friends at a regular pub table build an increasingly elaborate, silly conspiracy theory about a local shop closing early.
- Comedic angle: The 'evidence' keeps growing more absurd until someone points out the shop is just closed for holiday.

**Scene 9 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Konferenzraum-Verwirrung**
- Premise: A negotiation between two small business owners spirals into confused compromise proposals.
- Comedic angle: They end up agreeing to something neither of them actually wanted, just to end the meeting.

**Scene 10 — *Streit, Absicht & Gemütslage (abstrakt)*: Der Lügendetektor-Abend**
- Premise: Friends play a party game trying to spot each other's lies, getting suspicious over everything.
- Comedic angle: Someone's true statement gets voted 'obviously a lie' just because it sounded too weird to be real.

**Scene 11 — *Streit, Absicht & Gemütslage (abstrakt)*: Das Risikospiel**
- Premise: A group debates whether to try a slightly risky activity, weighing pros and cons dramatically.
- Comedic angle: The most cautious person of the group ends up being the first to jump in.

**Scene 12 — *Streit, Absicht & Gemütslage (abstrakt)*: Die Wettervorhersage-Zweifel**
- Premise: Friends argue about whether to trust the forecast for a planned outdoor event.
- Comedic angle: They end up bringing every possible weather item and using none of them because it's perfectly sunny.


#### ⟶ Shared glue pool (all closed-class function words)  _326 words, NOT scened_

Three former topics have been dissolved into a single **shared glue pool** — see **`glue-pool.md`**: **Batch 25. Logik & Verbindungen** (36 w), **Batch 26. Grammatik-Glue** (200 w), and **Batch 24. Raum & Richtung** (70 prepositions/directional adverbs; its 10 position verbs + `nah/weit/lang` moved to the "Der Umzugstag" scene under Handlungen). Closed-class stragglers were also swept out of Batch 21 Menge (18 determiners/degree-particles) and Batch 23 Denken (`einerseits, ausschließlich`).

**Why:** the dividing line is grammatical class, not abstractness. Function words — prepositions, connectors, pronouns, determiners, particles, question words, directional adverbs (*obwohl, zwischen, derselbe, ziemlich, welcher*…) — have no mental picture. Building standalone scenes out of them forces exactly the un-imaginable, stupid texts this whole method exists to avoid. Instead they are **connective tissue**: the text-writer weaves them through every other topic's texts, learned in context, repeated as often as needed. (Open-class abstract words — `die Meinung`, `entscheiden`, `wichtig` — stay in real scenes; the method grounds them in situations.)

**The rule:** it's OK to repeat these words; it's NOT OK to leave them out. `glue-pool.md` explains how they are woven in; `python3 tools/vocab.py glue --open` lists the ones no finished text has used yet.

Coverage of the full 2886 is unaffected — these words moved from scene-assignment to pool-assignment; none were dropped (re-verified: scenes ∪ pool = the same 2865 distinct as before).

## 6. Methodology & judgment calls

- **Parsing**: column 1 was split on `\n`; lines starting with `→` (regional-variant notes, e.g. "→ CH: Tram") were dropped from lemma extraction but not from the entry itself — the row still counts as one entry. The remaining line(s) had parenthetical region tags (`(D)`, `(A, CH)` etc.) stripped, and the lemma is everything before the first comma (dropping plural/conjugation forms). Reflexive `(sich)` was preserved as a prefix.
- **The "; " separator**: the task description anticipates cells with multiple headwords separated by `"; "`. In the actual CSV, `"; "` only ever occurs *inside* the `→` regional-variant note (e.g. "→ A: Kuvert; CH: Couvert"), never in the primary headword. The real multi-headword case in this list is masc/fem occupation pairs on separate lines within one cell (e.g. "der Lehrer, -\ndie Lehrerin, -nen"), merged into one combined lemma per row ("der Lehrer / die Lehrerin") since they're one CSV entry and appear together in a scene anyway.
- **Row = entry**: each of the 2886 CSV rows counts as exactly one entry for coverage purposes, even when its cell contains two merged headwords or a masc/fem pair.
- **CSV typo**: the row `irgendirgendein` is a duplicated-prefix typo in the official wordlist itself (its example sentence is about "irgendeinen [Saft]"); kept as the literal lemma `irgendirgendein` for coverage-matching purposes (so the row-count math stays exact), but should read as `irgendein` when actually writing the scene.
- **`zurzeit` appears twice** in the source CSV as two separate, identical rows — a genuine duplicate in the official wordlist, not a parsing artifact. Both rows are covered, and (after this merge pulled the old grammar topic's time-adverb batch into Zeit & Kalender) both now sit in Zeit & Kalender: once in its original calendar/time-of-day batch, once in the time-adverb batch absorbed from the old Grammatik split.
- **19 homonym/regional doublets** (see §4) were deliberately split across two different, more fitting topics/scenes rather than both landing in the same place.
- **This merge's restructuring** (per `JUDGE.md`'s "ideas to absorb"): the old 360-word "Grammatik & Verbindungswörter" topic was dissolved into Raum & Richtung / Logik & Verbindungen / Grammatik-Glue; ~48 pure time-adverbs were moved from that topic into Zeit & Kalender; ~38 danger/emergency words and ~41 color/shape/material words were carved out of six different host topics (Körper, Stadt, Gefühle, Natur, Unterwegs, Menge, Wohnung, Einkaufen, Freizeit, Arbeit) into two new dedicated topics; politeness words (`bitte/bitten/danke/danken/dankbar`, plus `das Paket`) were moved from Handlungen/Einkaufen into Kommunikation so two lifted premises (the politeness re-subscribe loop, the self-mailed reminder note) have their anchor words together in one scene. Every move was re-verified against the CSV afterward (§4) rather than assumed safe.
- **Reproducible pipeline**: `b_build.py` (CSV → canonical lemma list) → `b_subgroups.py` (semantic sub-grouping for the four large abstract B-topics) → `b_merge1.py`/`b_merge2.py` (mechanical word carve-outs/moves, coverage-checked at every step) → `b_merge3.py` (scene chunking) → `b_premises.py` + `b_new_premises.py` (all premise text) → `b_assemble_premises.py` (old→new scene-index mapping) → `b_gen_topics.py` (this script, re-verifies coverage from scratch and renders `topics.md`). Re-running the chain reproduces this file exactly.
- **A few common verbs** (`nehmen`, `nennen`, `fallen`, `scheinen`) ended up bucketed inside Grammatik-Glue's "Alltags-Kleinwörter" catch-all sub-scene rather than in Handlungen — a minor taxonomic imperfection inherited from the original build. Still fully covered and still get a concrete scene; a cleaner build would move them.
- **Total scenes**: 228, averaging ~12.7 words each.

coverage: 2886/2886 (100.0%)

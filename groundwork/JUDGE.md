# Judgment — Goethe-B1 Groundwork, Best-of-3 (A vs B vs C)

Comparison of three independent groundwork deliverables (topic taxonomy + full word assignment + scene OUTLINES, no German text yet) for the cram-topic → write-vivid-scene → Anki method.

- A: `/Users/andrey/anki/groundwork/agent-a.md` — 25 topics, 231 scenes
- B: `/Users/andrey/anki/groundwork/agent-b.md` — 22 topics, 228 scenes
- C: `/Users/andrey/anki/groundwork/agent-c.md` — 21 topics, 221 scenes

## Coverage verification (independent Python audit, claims DISTRUSTED)

I re-parsed `goethe-b1-wortliste.csv` from scratch (2,886 data rows after the version header), built a canonical lemma set (article + text-before-first-comma, parentheticals like `(A, CH)` / `(sich)` / `(Schlag-)` stripped *before* comma-splitting), then extracted every scene's target-word list from each file and diffed. Findings, after normalizing away purely cosmetic differences (`sich` prefixes, `(sich)`/`(Back-)`/`(Schlag-)` parentheticals, `der X / die Xin` person-pair notation):

- **Agent A**: 0 canonical lemmas unaccounted for. Complete. (2,972 raw target-word tokens — A keeps every parenthetical literal and counts masc/fem pairs separately, so it slightly over-lists.)
- **Agent B**: 6 apparent residuals (`Obers`, `Ofen`, `Rahm`, `Rohr`, `Sahne` regional cream/oven variants) — all confirmed *present* in the file, just written in combined regional-variant lines my matcher couldn't split. Effectively complete.
- **Agent C**: 1 residual — `irgendirgendein`, which is a duplicated-prefix **typo in the official CSV itself**; C documents this and lists the corrected `irgendein`. Otherwise an exact match to the canonical row set (2,865 clean lemma tokens ≈ 2,886 rows minus documented homonym doublets).

**Verdict on the "100% Python-verified" claims: all three are TRUE.** No hallucinated words, no real gaps in any file. Coverage is therefore *not* a differentiator; the decision rests on the other four axes. C's audit is the most rigorous and best-documented (it independently reconstructs the row list, asserts topic-level and scene-level coverage cannot drift apart, and documents the homonym doublets, the typo, and a reproducible `render.py`).

## Scores (1–5)

| Axis | A | B | C |
|---|:-:|:-:|:-:|
| 1. Coverage (verified, not trusted) | 5 | 5 | 5 |
| 2. Taxonomy quality | 4 | 4 | 5 |
| 3. Scene outlines (imaginability / writability) | 2 | 5 | 4 |
| 4. Practicality for cram→Anki | 3 | 5 | 4 |
| 5. Clarity / structure | 4 | 5 | 5 |
| **Total** | **18** | **24** | **23** |

### Axis notes

**Taxonomy.** C is best: 21 well-balanced topics (max 210 words) and the smartest handling of the hard function-word case — a three-way *functional* split (RAUM = spatial prepositions + position verbs; LOGIK = causal/conditional/concessive connectors; GLUE = pronouns/articles/particles/light verbs) instead of one undifferentiated glue bucket. B is good but dumps all ~360 function words into a single "Grammatik & Verbindungswörter" mega-topic and has a 212-word "Handlungen" bucket. A is clean and has genuinely useful *fine-grained* small topics (Farben/Formen/Material, Gefahr/Notfall/Sicherheit, Orte-vs-Verkehr as distinct) but carries a very large 294-word "Denken/abstrakt" bucket.

**Scene outlines — the decisive axis.** The method's expensive step is turning ~13 target words into one coherent imaginable story; a vivid premise is cheap to invent, a coherent story from a semantically-random word-set is not. This is where the files diverge sharply, *and the divergence is concentrated in the hardest buckets*:
- **A** orders words *alphabetically within scenes even in the abstract and glue topics*, with only a thin premise wrapper. E.g. Denken scene Ab-1 = `abhängen, ablehnen, Abschnitt, Absicht, achten, Ahnung, Aktion, akzeptieren, alternativ, Alternative, analysieren` — a pure A-alphabet slice with no single imaginable situation. Writing a vivid scene from that is arbitrary work. Weakest.
- **C** has vivid, specific, groundable premises and tight thematic topics, but *also* orders many scenes alphabetically/by-article. In tight *content* topics this is nearly harmless (a job scene using `der Angestellte/Anwalt/Arbeiter/Architekt` still coheres — the topic already fenced the domain). It bites only in the abstract/connector topics: LOGIK scene 123 alphabetizes connectors mixed with content cognition verbs (`aber, abhängen, abhängig, allerdings, annehmen, ausschließen, beeinflussen`), which has no unified scene.
- **B** groups words by *semantic sub-function* inside every topic, including the hardest ones: Denken splits into "Meinen/Wissen/Überzeugen", "Entscheiden/Planen/Feststellen", "Erinnern/Entdecken/Verstehen"; the 212-verb Handlungen topic splits into "Geben/Nehmen/Besitzen" (`abheben, abholen, bekommen, benötigen, besitzen, besorgen, bringen, geben, gehören, greifen`), "Verwaltung/Organisieren", "Körperliche Alltagsaktionen"; function words are grouped by grammatical role (a prepositions scene, a question-words interrogation, a spatial-adverb drone chase). Every scene is a semantically writable set. B front-loads the expensive combinatorial work that A and C leave to the future writer. (Only B's small "remainder" scenes, e.g. Denken scene 8, fall back to alphabetical.)

**Practicality.** B is easiest to pick up: each scene has a sub-function label *and* a title ("Der Umzugstag", "Der Debattierclub") plus a coherent word-set, so you can sit down and write immediately. C is close — global scene numbering, `TOPIC n/m` tags, reproducible render — but the alphabetical word-sets in its abstract topics add friction. A's alphabetical bags cost the most writing effort, and it front-loads the two hardest topics (glue, abstract) first.

**Ordering (sub-point of practicality).** None of the three earns credit here: all order topics essentially by size/theme, and none sequences pedagogically (concrete→abstract, frequency-first, easy→hard). A and B actually put the hardest material (glue / 360-word grammar) *first*. This is an open opportunity for the winner (see ideas below).

## WINNER: Agent B — `/Users/andrey/anki/groundwork/agent-b.md`

B wins where writing is hardest. All three achieve genuine 100% coverage, so the pick turns on how well the groundwork sets up the future scene-writing. B's signature move — grouping every scene's words by semantic sub-function rather than alphabetically — directly removes the most expensive part of that future work: assembling ~13 words that can plausibly share one imaginable situation. C matches or beats B on taxonomy elegance, premise vividness, and audit rigor, but hands the writer alphabetical word-slices in exactly the abstract/connector topics where cohesion is hardest to manufacture; A does this everywhere and is a clear third. Because a vivid premise is cheap to invent but a coherent story from a random word-set is not, B's advantage is the higher-leverage one for this method. It's a narrow win over C (24 vs 23) and a decisive one over A.

## IDEAS TO ABSORB (for B, from C and A)

### From C (the stronger runner-up)

1. **Split B's 360-word "Grammatik & Verbindungswörter" mega-topic into C's three role-based topics.** This is arguably better than B's own function-word handling. Adopt: **RAUM** (spatial prepositions `an/auf/hinter/über/zwischen` pulled *together with position verbs* `stehen/liegen/setzen/stellen/hängen` — a genuine improvement, since preps + position verbs co-occur in every location sentence and share the hide-and-seek / lost-tourist / delivery-driver framings), **LOGIK** (causal/conditional/concessive connectors under debate/argument framings), and **GLUE** (pronouns/articles/particles + the ~15 highest-frequency light verbs `sein/haben/machen/gehen/nehmen` under deliberately-vague-dialogue framings where the vagueness *is* the joke). Keep B's within-scene semantic grouping while adopting C's topic-level split.

2. **Lift C's most groundable specific premises** (B's premises are good but a notch more generic):
   - The self-mailed reminder note: a package's "anonymous sender" turns out to be the reporter's own forgetful colleague mailing himself a reminder (Kommunikation) — anchors `Absender/Empfänger/Paket/Anruf`.
   - The cat-prefers-Tuesdays slideshow: a neighborhood science-fair "researcher" presents, with full slideshow, that his cat prefers Tuesdays (Denken/Wissen) — anchors `beweisen/Beweis/begründen/Realität`.
   - The politeness-loop re-subscribe: a customer thanks a clerk so many times over cancelling a subscription that she re-signs him up by accident (Kommunikation) — anchors `bitte/bitten/danke/danken/dankbar`.
   - The over-complicated exception rule: a committee debates the exact *conditions for an exception* until the rule is too complex for anyone, including them, to follow (LOGIK) — anchors `Bedingung/Ausnahme/Folge/Voraussetzung`.

3. **Adopt C's audit-documentation rigor**: explicitly list the ~19 homonym/regional doublets (`die Bank` bench vs bank, `kosten` cost vs Austrian "taste", `das Rad`, `der Kasten`), note the `irgendirgendein` CSV typo, and ship a reproducible `render.py` so coverage can be re-verified. B's audit is correct but thinner than C's.

4. **Adopt C's cleaner lemma formatting** for the word lists (strip `(sich)`/`(Schlag-)`/regional parentheticals to a clean canonical lemma) so the future writer sees `verstehen`, `Sahne`, `Ofen` rather than `(sich) verstehen`, `(Schlag-)Sahne`.

### From A (third place, but not empty)

5. **Carve out A's fine-grained small topics** that B currently lumps: **Gefahr, Notfall & Sicherheit** (~38 words: Unfall, Notruf, Brand, warnen, retten) is a vivid, coherent cram batch on its own and is currently scattered across B's Körper/Stadt topics. Also consider A's separate **Farben, Formen & Material** (~41) rather than folding colors into a "Menge/Eigenschaften" bucket. These give tighter, more imaginable batches.

6. **Steal A's remainder-scene *framing devices*** (A's word-grouping is weak, but several of its premises are reusable comedic engines): the roommate grocery-argument that escalates into a pedantic grammar debate (glue), the answering-machine-greeting re-record by a flustered intern (politeness floskeln), the grandfather's story with nested flashbacks that need their own flashbacks (tense/time words), the "Warum?"-child driving a grandfather's explanations up to quantum physics (causal chains). Attach these to B's already-coherent word-sets.

### Winner's own gap to fix (neither runner-up solved it either)

7. **Impose a pedagogical topic ordering.** No file sequences meaningfully; B even opens with its hardest 360-word grammar block. Reorder so early batches are concrete/high-imagery (Wohnung, Essen, Körper, Kleidung) and abstract/function topics (Denken, LOGIK/GLUE) come later once the learner has momentum — or offer an explicit "suggested cram order" independent of the taxonomy table's size ordering.

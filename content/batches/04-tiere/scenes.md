# Batch 4 — Tiere · Szenenplan

8 target words. This is by far the smallest batch in the corpus, and its shape creates two
problems the bigger batches never had.

**Problem 1: eight words is not enough to hide a word list behind.** In a 127-word batch a
weak scene is diluted by eleven good ones. Here, one dialogue that exists only to house
`der Tierpark` is a quarter of the batch. So the test was applied harder than usual: every
scene below has a premise that would survive if the vocabulary were deleted, and the target
words are the things the speakers happen to be arguing about, never the reason for the turn.

**Problem 2: the coverage floor has no slack.** 90% of 8 is 7.2 — one skipped word puts the
batch at 87.5% and under the skill's floor. So nothing is parked here. All eight words have
an obvious natural home, and each is owned by exactly one scene.

**`die Schlange` is a queue, not a snake.** The word sits in the Tiere batch because of its
literal sense, but the Goethe list teaches the other one — both of its example sentences are
queues (*"Auf der Post gibt es immer eine lange (Warte-)Schlange"*, *"Stell dich bitte schon
mal in die Schlange an der Kasse"*), and the corpus agrees: `Schlange stehen` is the single
commonest thing done to this word (598 hits), against `Schlange fangen` at 27. Scene 4
therefore teaches the queue, at the Tierpark ticket window — the one place where the animal
sense is present in the room and never spoken. **No line in this batch puns on the two
senses.** A joke whose punchline needs the learner to hold both meanings at once is the
self-glossing failure one level up: it buys a laugh and costs the clean encoding.

**Four scenes, not eight.** The skill's 8–14 is calibrated for ~130 words. Eight words across
eight scenes would mean one target word per dialogue, which is the list driving the structure
again with a very short list. Four scenes of 6–8 turns each carry the batch and leave room
for the glue pool, which is where most of this batch's actual work happens — and it did:
**the glue pool went 263 → 277 of 326 (81% → 85%) on four dialogues.** Fourteen function
words against eight target words is the inverse of every batch so far, and it is the honest
description of what this batch is for.

Cast carried over from Batches 1–3, same house, now early summer:
**Julia** (fourth floor), **Tobi** (the friend who eats), **Frau Wolf** (next door, widowed),
**Herr Bruckner** (the caretaker, shoulder operated and still being careful with it),
**Jule** (Tobi's sister, the student). New this batch: **Herr Kessler**, a farmer, addressed
by name and never as "Bauer" — nobody is called that to their face.

**Standard German only.** No word in this batch carries an A/CH cross-reference, so nothing
had to be split on regional grounds and no speaker remarks on naming.

**Synonym check.** This batch has no true synonym pair. Two near-pairs were checked anyway:

| pair | kind | scenes | ruling |
|---|---|---|---|
| `das Tier` / `das Haustier` | superordinate + specific | 4 / 1 | split anyway — the general word deserves its own encoding |
| `der Bauer` / `der Bauernhof` | derivational family | 3 / 3 | left together; a farmer and their farm in one conversation is ordinary German |
| `fressen` / `füttern` | different argument structures (the animal eats / a person feeds) | 2 / 2 | left together on purpose — Scene 2 turns on the difference |

**Supporting animals were checked against the A1∪A2∪B1 lemma lists**, not chosen freely:
`Katze`, `Hund`, `Vogel`, `Fisch`, `Schwein`, `Pferd`, `Zoo` are all in. `Kaninchen`, `Käfig`,
`Futter`, `Eimer`, `Karton`, `Kuh`, `Stall`, `Napf` are **not**, and none of them appears in a
text — which is why the farmer hands over a *Sack* and the cat eats off a *Teller*.

**Scene order is ownership order.** The scanner records a word at its first occurrence, so the
texts are sequenced such that first occurrence and designed owner are the same text for all
eight words — no scene reuses a word before the scene that owns it. That is why the two verbs
come second, before the farm and the Tierpark that both reuse them.

---

### Scene 1 — Die Kiste vor der Tür
- **Premise:** Tobi is at Julia's door with a cardboard box that is moving. He needs somewhere to keep an animal over the summer, and has chosen her flat because his own lease forbids it.
- **Angle:** He negotiates in the past tense — the decision was made before he rang the bell. Frau Wolf, who hears everything through the wall, ends the argument by opening the box herself, and there are two animals in it.
- **Words (1):** das Haustier *(owner)*
- **Deliberately absent:** `das Tier` and `fressen`, both of which would fit here and are owned by later scenes.
- **Glue:** *worum*, *weshalb*, *absolut*, *nebenan*, *vielleicht*, *so etwas*, *bevor*, *doch*, *ja*

### Scene 2 — Die Katze frisst nicht
- **Premise:** Bruckner is at physiotherapy and Julia has agreed to feed his cat. The cat has not touched the plate.
- **Angle:** He coaches her by phone and every instruction is more elaborate than the last — the cat doesn't trust her, she smells wrong, the meat is the wrong meal. It ends with the cat eating out of Tobi's hand, because Tobi is sitting on the kitchen floor eating the same sausage.
- **Words (2):** fressen *(owner)*, füttern *(owner)*
- **Chunks:** `die Katze füttern` (233), `aus der Hand fressen` (231), `den Fisch füttern` (173), `die Katze frisst` (35)
- **Note:** the scene exists to separate the two verbs by argument structure — Bruckner's first question is literally *gefüttert* vs. *hingestellt*. That is the one context where putting them in one breath is not stacking.
- **Glue:** *genauso*, *vertrauen*, *fremd*, *dasselbe*, *irgendwann*, *ab morgen*

### Scene 3 — Sonntag beim Kessler
- **Premise:** Julia and Jule drive out to a farm on a Sunday morning to buy eggs straight from the producer. The eggs went at six.
- **Angle:** Jule, who studies, explains to a working farmer that he should grow more vegetables and keep fewer pigs. He does not argue back; he sends her to go and feed them. She is wearing white shoes, and Julia is the one who tells her she has lost.
- **Words (2 owned + 1):** der Bauer *(owner)*, der Bauernhof *(owner)*, füttern
- **Weak declension is the point:** `der Bauer, -n` takes *-n* through the whole singular. The text says **beim Bauern** (the CSV's own example sentence is *Wir kaufen unser Gemüse beim Bauern*) and **der Bauer** in the nominative, so both forms are on the page.
- **Chunks:** `auf dem Bauernhof arbeiten` (24), `vom Bauernhof kommen` (28), `der Bauer verkauft` (28), `die Schweine füttern` (72)
- **Glue:** *kompliziert*, *geradeaus*, *übrigens*, *wieso*, *danach*
- **Deliberately absent:** `das Tier` — the animals here are *Schweine*, by name.

### Scene 4 — Samstag im Tierpark
- **Premise:** Frau Wolf has taken Bruckner and two children from the house to the Tierpark. The queue at the ticket window runs around the building.
- **Angle:** Bruckner is sent to stand in it — with the shoulder — while everyone else studies the map. By the time he reaches the window, the children have found birds on the grass outside, decided that is the whole day, and nobody wants to go in any more.
- **Words (3 owned + 1):** der Tierpark *(owner)*, die Schlange *(owner)*, das Tier *(owner)*, füttern
- **Chunks:** `Schlange stehen` (598), `eine lange Schlange` (248), `die Schlange ist lang` (193), `das Ende der Schlange` (96), `die Vögel füttern` (111), `Tiere im Zoo` (57)
- **Glue:** *voraus*, *geradeaus*, *vorwärts*, *nirgendwo*, *hierher*, *überhaupt*
- **Note:** `die Schlange` appears three times and always as a queue. Never as an animal, never remarked on.

---

## Ownership table (for the carding pass)

Designed owner and scanner first-occurrence agree for all eight words, so there is no
discrepancy to resolve at Step 5.

| word | owner | also appears in |
|---|:-:|---|
| das Haustier | 1 | — |
| fressen | 2 | — |
| füttern | 2 | 3, 4 |
| der Bauer | 3 | — |
| der Bauernhof | 3 | — |
| der Tierpark | 4 | — |
| die Schlange | 4 | — |
| das Tier | 4 | — |

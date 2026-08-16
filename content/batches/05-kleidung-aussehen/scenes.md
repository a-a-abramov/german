# Batch 5 — Kleidung & Aussehen · Szenenplan

43 target words. A mid-size batch, and an unusually **adjective-heavy** one: five of the
43 words (`schön`, `hässlich`, `elegant`, `chic/schick`, `modern`) are evaluations of how
something looks, and they are the batch's main design problem — not the nouns.

**Seven scenes, not the skill's 8–14.** That range is calibrated for ~130-word batches.
43 words across twelve scenes would be three or four target words per dialogue, which is
the word list driving the structure again. Seven scenes of 5–8 words each keep every
dialogue at seven or eight turns and leave room for the glue pool, which is where a batch this size
does most of its work.

**Sense decisions made against the CSV, not against the topic name.** Two words in this
batch are not the word the topic makes you expect:

- **`das Modell` is a product model, not a fashion model.** The CSV's only example is
  *"Wie findest du dieses Auto? – Dieses Modell gefällt mir nicht."* So `Modell` is taught
  in a shoe shop, as the thing that has been discontinued — never as a person on a
  catwalk. (The corpus does carry `Modell stehen` "to pose", 179 hits; it is not used.)
- **`das Kostüm` is a costume, not a woman's suit.** CSV: *"In dem Film tragen die Leute
  bunte Kostüme."* Scene 6 is therefore a costume party. It is deliberately **not** a
  carnival: `Fasching` is (D, A) and `Fasnacht` is CH, and only `Karneval` would be
  writable — a generic *Kostümparty* avoids the question entirely.

**`der Rock` is a skirt.** The corpus mixes the music sense in (`Rock hören`, `Rock
spielen`); no line in this batch uses it.

**`die Kiste` is in scope** — the CSV tags it `(A, D)`, which is the shared-entry case, not
an A-only one. It has already appeared once in Batch 4 ("Die Kiste vor der Tür"), so
Scene 1 is built on a deliberately different situation: a cellar being cleared out, not a
box at a doorway.

**Standard German only.** No A/CH-only word is written, and no speaker remarks on regional
naming.

---

## The five evaluative adjectives: one per scene

Grouping "by meaning" would put `schön`, `schick`, `elegant` and `modern` in the same
dialogue, and no German says three of them in one breath about one garment. They are
distributed one per scene, each to the situation whose speakers would actually reach for
that word:

| word | scene | why that scene |
|---|:-:|---|
| `schön` | 1 | Frau Wolf defending her mother's coat — the word for what a thing *was* |
| `hässlich` | 2 | the only honest verdict on a botched haircut |
| `elegant` | 3 | the borrowed suit; the word a wedding brings out |
| `chic/schick` | 4 | a salesperson's word for a boot |
| `modern` | 5 | the fashion argument — what is *currently* worn |

`frisch` is not part of this family (fresh, not good-looking) and rides with the shirt in
Scene 3, where `ein frisches Hemd` is attested 142 times.

## Synonym / near-pair check

| pair | kind | scenes | ruling |
|---|---|:-:|---|
| `der Anzug` / `das Kostüm` | different garments, both "the formal outfit" | 3 / 6 | split |
| `die Jacke` / `der Mantel` | near-pair (outerwear) | 7 / 1 | split |
| `(sich) anziehen` / `anhaben` | near-pair (put on / have on) | 3 / 7 | split — the two most confusable verbs in the batch, kept four texts apart |
| `die Hose` / `die Jeans` | superordinate + specific | 5 / 7 | split anyway |
| `der Schuh` / `der Stiefel` | superordinate + specific | 4 / 4 | **left together on purpose.** This is the pattern the skill explicitly allows ("Hast du einen Stift?" / "Nimm den Kugelschreiber") and a shoe shop is the one room where it is the normal exchange: the customer asks for *Schuhe*, the salesperson answers *Stiefel* |
| `der Schmuck` / `die Kette` | superordinate + specific | 6 / 6 | left together; `der Ring` was moved out to Scene 3 so the jewellery scene carries two, not three |
| `der Friseur` / `die Frisur` | derivational family | 2 / 2 | left together — the CSV's own example does exactly this (*"Du hast eine tolle Frisur! Warst du beim Friseur?"*) |
| `die Kleidung` / `das Zeug` | superordinate + colloquial | 1 / 7 | split — `Zeug` next to `Kleidung` invites self-glossing |

## Scene order is ownership order

The scanner records a word at its **first** sighting, so a word must not appear in any text
before the one that owns it. Two consequences shaped the order:

- **`aussehen` (band 4) is owned by Scene 1**, not by the hairdresser scene where it is
  most at home. It is far too common to keep out of a dialogue about a box of old clothes,
  and the safe fix is to own it early and reuse it freely afterwards.
- **`schön` (band 5) is owned by Scene 1** for the same reason; `hässlich`, which has no
  business in a cellar, took its place in Scene 2.

Everything else is kept out of the texts that precede its owner by hand: Scenes 1–2 avoid
`anziehen`, Scenes 1–4 avoid `Kleid`/`Hose`/`modern`, Scenes 1–6 avoid `Jacke`/`Zeug`.

Cast carried over from Batches 1–4, same house, now September — Tobi is back from the
summer he spent away in Batch 4: **Julia** (fourth floor), **Tobi**, **Frau Wolf**
(next door, widowed), **Herr Bruckner** (the caretaker), **Jule** (Tobi's sister, the
student). New this batch: **Frau Reiter**, a hairdresser, and an unnamed
**Schuhverkäuferin**, recoverable from her first turn as the person who works there.

---

### Scene 1 — Der Keller muss leer werden
- **Premise:** Bruckner has given the house a week to clear the cellar corridor. Frau Wolf's box of old clothes is the one that has stood there longest, and Julia is holding the bag for the clothing bank.
- **Angle:** Every item Frau Wolf gives away she takes back one turn later, so she ends the sorting carrying more than was in the box — and Bruckner, who came to enforce the deadline, walks off wearing the hat.
- **Words (8):** die Kiste *(owner)*, die Kleidung *(owner)*, der Mantel *(owner)*, der Hut *(owner)*, der Pullover *(owner)*, schön *(owner)*, die Tüte *(owner)*, aussehen *(owner)*
- **Chunks:** `eine alte Kiste` (188), `Kiste im Keller` (21), `in die Tüte packen` (69), `warme Kleidung` (90), `Kleidung tragen` (930), `einen Mantel tragen` (323), `den Hut abnehmen` (106), `einen Hut aufhaben` (331), `einen Pullover tragen` (144)
- **Deliberately absent:** `anziehen` (Scene 3 owns it — the clothes here are given away, not put on), `die Jacke` (Scene 7), `hässlich` (Scene 2), `frisch` (Scene 3)
- **Glue:** *innerhalb*, *sich befinden*, *stammen*, *solch-*, *das Teil*, *auseinander*, *dorthin*, *außerdem*, *derselbe*

### Scene 2 — Zwei Zentimeter
- **Premise:** Jule asked for the ends trimmed and left the chair with a short blonde cut. Julia came along and has said nothing for an hour.
- **Angle:** Jule defends the result to everyone, but wants the one verdict nobody will give her — and she took her glasses off before it started, so she is the last person in the room to have seen it.
- **Words (5):** der Friseur / die Friseurin *(owner)*, die Frisur *(owner)*, blond *(owner)*, die Brille *(owner)*, hässlich *(owner)*
- **Chunks:** `eine neue Frisur` (725), `eine schlechte Frisur` (44), `blonde Haare` (1068), `ohne Brille sehen` (161), `die Brille aufsetzen` (117), `zum Friseur gehen` (362), `beim Friseur sein` (309)
- **Glue:** *stumm*, *begleiten*, *negativ*, *um … zu*, *sowieso*
- **Note:** `hässlich` is the word Jule forces out of Julia, which is the only way a batch gets that word into speech without an insult.

### Scene 3 — Der Anzug vom Bruder
- **Premise:** Tobi's cousin marries at eleven tomorrow and Tobi is carrying the rings. The suit is his brother's; the shirt is missing a button.
- **Angle:** He wants to glue the button. Julia explains that a button is sewn on — and he glues it anyway, so the scene ends with his finger stuck to the shirt he has to wear in front of the whole hall.
- **Words (8):** der Anzug *(owner)*, das Hemd *(owner)*, frisch *(owner)*, der Knopf *(owner)*, kleben *(owner)*, elegant *(owner)*, (sich) anziehen *(owner)*, der Ring *(owner)*
- **Chunks:** `ein grauer Anzug` (195), `einen Anzug anziehen` (180), `ein frisches Hemd` (142), `ein sauberes Hemd` (149), `ein Knopf fehlt` (98), `einen Knopf annähen` (21), `an der Hand kleben` (571), `die Ringe tauschen` (87), `einen Ring am Finger tragen` (356)
- **Glue:** *der Zweck*, *erfüllen*, *fällig*, *vorbei*, *außerdem*, *derselbe*
- **Deliberately absent:** `chic/schick` (Scene 4 owns it — this scene has `elegant`), `die Jacke` (Scene 7), although the CSV's own `Knopf` example is *"An meiner Jacke fehlt ein Knopf"*; the button is moved to the shirt so the coat word stays with its own scene.

### Scene 4 — Vor elf Jahren
- **Premise:** Bruckner walks into a shoe shop wanting the exact pair he bought there eleven years ago. Two speakers only.
- **Angle:** He rejects the successor model for being red, is talked into boots, and blames the boots for the hole in his sock — the boots are still standing next to him, unworn.
- **Words (5):** der Schuh *(owner)*, der Stiefel *(owner)*, das Modell *(owner)*, der Strumpf *(owner)*, chic/schick *(owner)*
- **Chunks:** `ein Paar Schuhe` (28), `Schuhe kaufen` (653), `die Schuhe ausziehen` (575), `schicke Schuhe` (72), `Stiefel anziehen` (42), `das alte Modell` (206), `ein neues Modell` (579), `ein Loch im Strumpf` (6)
- **Glue:** *soviel*, *voneinander*, *mittler-*, *per*, *entstehen*, *irgendein*
- **Note:** `Strumpf` and `Creme` are the two words in this batch with **no usable Wortprofil** — `Strumpf` returns four rows at `--min-freq 5 --all` (`ein Loch im Strumpf`, freq 6, is the one used here) and `Creme` returns two, one of them non-B1. Both lines were written rather than harvested.

### Scene 5 — Modenschau im Wohnzimmer
- **Premise:** Jule is emptying her wardrobe by modelling each item while Julia votes keep or give away. Frau Wolf is there to agree with Julia and does not.
- **Angle:** Jule's argument for keeping the dress is that it is back in fashion. Frau Wolf confirms it, from the wrong direction: she owned exactly that dress in 1975, with the skirt to match — and then keeps the last word, which is not the confirmation Jule was after.
- **Words (6):** die Mode *(owner)*, modern *(owner)*, das Kleid *(owner)*, der Rock *(owner)*, die Bluse *(owner)*, die Hose *(owner)*
- **Chunks:** `ein schönes Kleid` (935), `ein Kleid tragen` (2078), `eine weiße Bluse` (88), `ein kurzer Rock` (134), `eine schwarze Hose` (137), `eine enge Hose` (169), `die neue Mode` (184), `in Mode sein` (448), `aus der Mode kommen` (211)
- **Glue:** *die Möglichkeit*, *einig-*, *die Länge*, *zurück*, *solch-*, *ebenfalls*
- **Deliberately absent:** `das Kostüm` (Scene 6) — a fashion show is exactly where a costume would sneak in.

### Scene 6 — Vor der Kostümparty
- **Premise:** Julia and Jule are getting ready in Julia's flat. Frau Wolf has come over to lend a necklace and stayed to supervise it.
- **Angle:** Jule has spent an hour on make-up for a costume that will leave only her eyes visible; Julia has no costume at all and has decided that smelling expensive is a costume. (The batch's one seven-turn dialogue; the other six run to eight.)
- **Words (6):** das Kostüm *(owner)*, schminken *(owner)*, das Parfüm *(owner)*, der Schmuck *(owner)*, die Kette *(owner)*, die Creme *(owner)*
- **Chunks:** `eine Kette um den Hals` (63), `eine Kette schenken` (128), `echter Schmuck` (33), `teurer Schmuck` (72), `ein Kostüm anziehen` (120), `nach Parfüm riechen` (47), `billiges Parfüm` (56), `die Augen schminken` (30)
- **Glue:** *das Detail*, *nebenbei*, *zurück*, *ganz*
- **Note:** `die Creme` is hand cream here, the CSV's first sense (*"Ich hätte gern eine Creme für die Hände"*), not the pastry sense its second example carries.

### Scene 7 — Ohne Jacke im September
- **Premise:** Tobi turns up at Julia's door soaked through, having cycled home in the rain without a coat.
- **Angle:** He negotiates from the doormat, claims the jeans are nearly dry, and asks for a tissue to deal with two litres of water. He leaves in the holey pullover Frau Wolf rescued from the cellar in Text 1.
- **Words (5):** die Jacke *(owner)*, die Jeans *(owner)*, anhaben *(owner)*, das Taschentuch *(owner)*, das Zeug *(owner)*
- **Chunks:** `eine warme Jacke` (41), `eine Jacke anziehen` (66), `eine enge Jeans` (40), `Jeans tragen` (100), `eine Hose anhaben` (93), `das ganze Zeug` (1946), `das Zeug holen` (384)
- **Glue:** *quer*, *daher*, *umso*, *irgendwann*
- **Note:** the closing callback to Text 1's pullover is the batch's only cross-text link, and it is deliberate — it gives the last dialogue a place to end that is not a summary.

---

## Ownership table (for the carding pass)

**Generated, not hand-written** — every row below comes from running the ledger's own
matcher (`variants` + `csv_forms` + `phrase_matches`, the same three functions `site.py`
imports) over all 43 lemmas × all 7 texts, so "owner" is literally what `scan` records and
"also appears in" is every later sighting. Designed owner and scanner first-sighting agree
for all 43 words; where they disagreed, the text was changed, not the table.

| word | owner | also appears in |
|---|:-:|---|
| (sich) anziehen | 3 | 4, 5, 7 |
| anhaben | 7 | — |
| aussehen | 1 | — |
| blond | 2 | — |
| chic/schick | 4 | 5 |
| das Hemd | 3 | — |
| das Kleid | 5 | — |
| das Kostüm | 6 | — |
| das Modell | 4 | — |
| das Parfüm | 6 | — |
| das Taschentuch | 7 | — |
| das Zeug/-zeug | 7 | — |
| der Anzug | 3 | — |
| der Friseur / die Friseurin | 2 | — |
| der Hut | 1 | — |
| der Knopf | 3 | — |
| der Mantel | 1 | — |
| der Pullover | 1 | 7 |
| der Ring | 3 | — |
| der Rock | 5 | — |
| der Schmuck | 6 | — |
| der Schuh | 4 | — |
| der Stiefel | 4 | — |
| der Strumpf | 4 | — |
| die Bluse | 5 | — |
| die Brille | 2 | — |
| die Creme | 6 | — |
| die Frisur | 2 | — |
| die Hose | 5 | — |
| die Jacke | 7 | — |
| die Jeans | 7 | — |
| die Kette | 6 | — |
| die Kiste | 1 | — |
| die Kleidung | 1 | — |
| die Mode | 5 | — |
| die Tüte | 1 | — |
| elegant | 3 | — |
| frisch | 3 | — |
| hässlich | 2 | — |
| kleben | 3 | — |
| modern | 5 | — |
| schminken | 6 | — |
| schön | 1 | — *(the matcher also fires on* schon *in Text 3; not a real use)* |

---

## What landed

`vocab.py scan --apply` on the finished texts: **43/43 target words (100%)**, nothing
skipped, and designed owner equals scanner first-sighting for every word in the table
above. Two texts had to be edited to make that true — the matcher reduces `anhaben` to a
bare `an` (its `haben` half is filtered as an auxiliary), so a stray `an` in Texts 3 and 4
was claiming the word four texts before its owner.

The **glue pool went 277 → 309 of 326 (85% → 95%)**: 32 function words on seven dialogues,
the largest single-batch glue yield so far. What is left open is mostly unwritable in a
kitchen-table dialogue (`national`, `passiv`, `das Geschlecht`, `mobil`, `Spezial-`,
`gesamt-`, `sogenannt-`, `einschließlich`) and will need a batch with an official or
technical register — Stadt & Ämter or Arbeit & Beruf.

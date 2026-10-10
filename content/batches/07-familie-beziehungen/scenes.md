# Batch 7 — Familie & Beziehungen · Szenenplan

104 target words, the largest batch since Batch 3 — and the one whose **whole semantic
field is already a list**. Nobody has to sort *Onkel, Tante, Neffe, Nichte, Cousin,
Enkel, Schwiegermutter* into an order: the vocabulary arrives pre-sorted as a family
tree, and a family tree recited aloud is exactly the text this method exists to avoid.
Every design decision below is a way of *not* writing that recital.

**Twelve scenes**, back to the Batch 1–3 count, because 104 words over seven scenes
would be fifteen relatives per dialogue. Nine to eleven words per scene, one situation
each.

## The design problem: the field is a list, so the scenes must be arguments

The fix is that **no scene enumerates kinship — every scene has something at stake that
happens to require the words.** Concretely:

| scene | the thing at stake | why the kinship words come out |
|:-:|---|---|
| 1 | Julia is about to meet Tobi's family and needs to know who she must be nice to | a napkin diagram drawn *under time pressure* |
| 2 | two people who must not sit at the same table | a seating plan, not a family tree |
| 3 | a buffet queue where Julia has forgotten every name | the aunt re-identifies people by what is on their plate |
| 9 | Oma has a schedule and her visitors are in the way | she lists her descendants as a *complaint* |

Where a scene could not find a stake, it got fewer words rather than a longer list.

## Sense decisions made against the CSV, not against the corpus

- **`der Hof` is the courtyard the children play in** — the CSV's only example is *"Die
  Kinder spielen am liebsten im Hof."* The corpus's `Hof` is a farm or a royal court
  (`auf dem Hof arbeiten` 106, `Hof des/der König` 46, `Hof des/der Eltern` 44); none of
  that is written. Scene 4 uses the courtyard of the same house as Batches 1–6, which is
  where Batch 6's Text 4 already put it.
- **`der Nachwuchs` is a couple's own baby**, per the CSV's second example (*"Die Katze
  hat Nachwuchs bekommen"* — the *offspring* sense, not the corpus's *young talent*
  sense). Scene 5 announces it: *"Wir bekommen Nachwuchs."*
- **`der Wirt / die Wirtin` runs a Lokal**, per the CSV (*"Ich kenne die Wirtin von diesem
  Lokal"*). Scene 3's wedding reception is held in one, which is the only situation in
  this batch that produces the word at all.
- **`der Held` is somebody playing the hero**, per the CSV's *"Er spielt gern den
  Helden"* — Scene 12 uses it as a refusal (*"Ich bin kein Held"*), not as a compliment
  about a rescue.
- **`die Bevölkerung` is the statistic**, per the CSV (*"11 % der Bevölkerung wurden nicht
  im Inland geboren"*). Scene 10 has Frau Wolf quote a newspaper line about the population
  ageing — it is the only register that word has.

## Synonym / near-pair check

The batch's real hazard. Eleven sets, every one of them split:

| pair | kind | scenes | ruling |
|---|---|:-:|---|
| `das Altenheim` / `das Altersheim` | true synonyms — the CSV prints the **same example sentence** for both | 9 / 10 | **split.** Scene 9 is inside one and says *Altenheim* throughout; Scene 10 only names the institution in the abstract, and says *Altersheim* |
| `die Leute` / `die Person` | near-synonyms | 6 / 5 | **split.** `Person` is the counting word on a form (*"Eintritt pro Person"*), `Leute` is the guest list |
| `der Rentner` / `die Senioren` | near-synonyms | 10 / 9 | **split.** `Senioren` is what the home's noticeboard calls them, `Rentner` is what Bruckner will be |
| `das Paar` / `das Ehepaar` | near-synonyms | 7 / 2 | **split.** A wedding is exactly where *"das Paar"* would slip in, so Scene 2 says *die beiden* and never *Paar* |
| `der Freund` / `der Partner` | near-synonyms in the *boyfriend* sense | 7 / 8 | **split.** Scene 7's is the boyfriend Jule denies; Scene 8's is the register in which two people discuss a separation |
| `die Beziehung` / `die Freundschaft` | near-synonyms | 8 / 12 | **split** |
| `der Bekannte` / `der Verwandte` / `der Angehörige` | three ways to say *someone connected to you* | 6 / 3 / 9 | **split three ways.** `Angehörige` keeps its CSV register — the one the staff of an institution uses (*"Auskunft nur an Angehörige"*) |
| `die Trennung` / `die Scheidung` | near-synonyms, and the CSV's own `Trennung` example contrasts them | 8 / 8 | **the one pair left together, deliberately** — see below |
| `die Frau` / `die Ehefrau` | superordinate + specific | 2 / 8 | split |
| `der Vorname` / `der Familienname` | contrastive pair | 5 / 5 | **left together on purpose.** Like Batch 6's antonyms: the contrast *is* the utterance — a form asks for one and the speaker gives the other |
| `die Heimat` / `das Heimweh` | derivational | 11 / 11 | left together; Scene 11 turns on the gap between them |

**The one deliberate pairing.** `die Trennung` and `die Scheidung` share Scene 8, against
the rule, because the CSV's own example makes the distinction the point: *"Meine Kollegin
ist noch nicht geschieden, aber sie lebt in Trennung."* Two people who have separated and
are not divorced is a state German has two words for, and a speaker who has to explain the
downstairs flat needs both in one breath. Guarded against self-glossing: neither speaker
defines either word — the *floor plan* does.

Derivational families left together, per the skill: `küssen`/`der Kuss` (7),
`erwachsen`/`der Erwachsene` (11), `verwandt`/`der Verwandte` (3),
`(sich) verabreden`/`verabredet` (7), `erziehen`/`die Erziehung` (4),
`verantwortlich`/`die Verantwortung` (4), `einladen`/`die Einladung` (6),
`schenken`/`das Geschenk` (6), `jung`/`der Junge` (4), `die Rente`/`in Rente gehen` (10).

## Scene order is ownership order

The scanner records a word at its **first** sighting, so a word must not appear in any
text before the one that owns it. This batch is the most exposed in the corpus so far,
because a wedding and a family gathering will pull in half the list unbidden. The
avoidances that cost something:

- **Texts 1–5 never say `Leute`, `Geschenk`, `schenken`, `einladen`, `eingeladen` or
  `Einladung`** — all owned by Text 6 (and Texts 1–4 never say `Person`, owned by Text 5), and all five earlier scenes
  (especially the wedding) want them. Text 2 says *auf der Liste*, Text 3 says *die Gäste*.
- **Text 2 never says `Paar`, `Kuss`, `küssen`, `Dame`, `verändert` or `Freund`.** A
  wedding is the natural home of every one of them — *das junge Paar*, *der erste Kuss*,
  *meine Damen und Herren*, *du hast dich gar nicht verändert*, *Freunde der Familie* —
  and all five are owned by Texts 7 and 12. This is the single most expensive avoidance
  in the batch, and it is why Text 2 is a logistics conversation and not a celebration.
- **Texts 1–3 never say `jung`, `Junge` or `Mädchen`** (Text 4), which costs Text 3 the
  obvious *"die Kinder sitzen hinten"* line; it says *die Kleinen* instead.
- **Text 4 never says `erwachsen`** (Text 11) — Frau Wolf says *"wenn sie groß sind"*.
- **Text 4 owns `der Sohn`, Text 9 owns `die Tochter`**, so Text 1's family diagram names
  everybody by name and by *Bruder/Schwester*, never by *Sohn/Tochter* — which is how a
  person actually describes their own siblings anyway.
- **Texts 1–8 never say `alt`** (bare), `Alter`, `Oma`, `Opa`, `Bewohner`, `Senioren`,
  `Angehörige`, `geboren` (Text 9), or `Rente`, `Rentner`, `Chef`, `Bevölkerung`,
  `Hausfrau`, `Hausmann`, `Altersheim` (Text 10).
- **Text 2 never says `Scheidung`, `getrennt`, `Trennung`, `Partner`, `Beziehung` or
  `Ehefrau`** (Text 8). It says *"die beiden haben sich scheiden lassen"* and
  *"geschieden"*, which are its own.
- **Text 11 never says `Abschied` or `verabschieden`** (Text 12), even though the last
  morning of a class trip is where they live.
- **Text 1 never says `Frau` or `Mann`** (Text 2) — which also means Frau Wolf cannot
  appear in it. Text 1 is the only dialogue in the batch without a neighbour in it.

Three scanner artefacts to correct by hand after `scan --apply`, all caused by the
matcher rather than by the prose:

- **`in Rente gehen/sein`** — the ledger's headword is the slash form, so `variants()`
  emits `sein` as a spelling of it, and the first utterance in the batch containing
  *sein/seine* claims the word. It belongs to Text 10.
  Recorded with `vocab.py use --batch 7 --text 10`; the scanner's own Text 1 row
  (*"Bei ihr musst du am nettesten sein"*) comes back on every rescan and is ignored.
  The card is cut from Text 10: *"Ich will in Rente gehen, einundzwanzig Jahre sind genug."*
- **`das Altenheim` / `das Altersheim`** need checking against their owner texts rather
  than the scan, since the CSV prints one example for both.
- **`irgendirgendein`**, the glue pool's last open entry, is a typo in the official
  Goethe list and matches nothing the scanner can be shown. It stays open forever; the
  batch writes *irgendein* anyway, in Text 3.

## Continuity with Batches 1–6

Checked against every dialogue in Batches 1–6 before writing. The facts this batch must
not contradict:

| fact | source |
|---|---|
| The story is about a year on from Julia's move-in; Batches 5 and 6 were September and October | implied by the Batch 1–6 headers |
| Bruckner has been caretaker *"seit zwanzig Jahren"* at the move-in — **twenty-one years** now | Batch 1, Text 1; Batch 2, Text 3 |
| **Bruckner lives alone**, in the house, with a cat | Batch 3, Text 3; Batch 4, Text 2 |
| Bruckner's door is near the courtyard | implied by Batch 3, Text 9 (*"Das Schild hängt an Ihrer eigenen Tür"*) |
| Bruckner: operated knee and left shoulder, no alcohol since; deaf on the right ear | Batch 2, Texts 3 and 7; Batch 3, Text 9 |
| The lift has been broken since two years before the move-in — three years now | Batch 1, Text 1 |
| Frau Wolf: widowed six years, nursed her husband two; has known Bruckner fourteen years | Batch 2, Text 12; Batch 6, Text 4 |
| Frau Wolf says **du** and *Kind* to Julia and Jule; Julia says **Sie** to her | Batch 5, Texts 1 and 5; Batch 6, Text 2 |
| Bruckner says **du** to Tobi, **Sie** to Julia; both say Sie to him | Batch 4, Text 2; Batch 6, Text 1 |
| Frau Wolf says **Sie** and *junger Mann* to Tobi | Batch 4, Text 1 |
| Tobi's family (new here) says **du** to Julia from the first meeting, and Julia says du back to everyone except Oma Erna, whom she calls Sie | decided in this batch |
| Tobi is Julia's boyfriend, has his own flat, a job with a Chef, does not smoke; surname **Wagner** | Batch 1, Text 10; Batch 2, Texts 5 and 10; Batch 3, Text 10; Batch 4, Text 1 |
| Tobi has a brother (the suit) and a sister, Jule, who studies | Batch 3, Text 11; Batch 5, Text 3 |
| **Tobi's cousin married in September**; Tobi held the rings, button glued on | Batch 5, Text 3 |
| Children around the house (Frau Wolf takes *die Kinder* to the zoo); the courtyard has the bike stands and the fence | implied by Batch 4, Text 4; Batch 6, Text 4 |
| The café is *gegenüber*; the Lokal *unten an der Ecke* tasted of old fat | Batch 3, Texts 6 and 8 |

Fixed in this plan as a result:

- **Kevin's wedding (Texts 2–3)** is the same cousin's wedding as Batch 5. The September
  date was the Standesamt, in a full Saal; the November event is the postponed party.
  Kevin is already married in these texts.
- **Bruckner has no wife** (Scene 10). The angle that relied on one now rests on his living
  alone with the cat.
- **Bruckner's tenure is twenty-one years** (Scene 10), not nineteen.
- **The divided flat (Scene 8) is on the third floor**, directly under Julia, as its title
  says; it had been placed on the first floor.
- **Scene 1's café is the one across the street**, and Julia has already met Jule.
- **Oma Erna is Werner's mother**, so the "mother-in-law" of Scene 2 and the Oma of
  Scene 9 are one person.
- **The boy in Scene 4 is a neighbour family's son**, not Frau Wolf's. She has no
  children on record, and Batch 2, Text 12 has her nursing her husband alone.

## Calendar

| when | text |
|---|---|
| Thursday, early November | 1 — napkin in the café, two evenings before the Feier |
| Friday | 2 — Gisela's final seating plan |
| Saturday | 3 — the Feier. Julia meets Oma Erna here for the first time |
| the Saturday after | 4 — the courtyard window |
| the following week | 5, 7 (a Friday), 8 |
| a Saturday later in November | 6 — the guest list is written for Julia's birthday that Saturday |
| a Wednesday in late November | 9 — Altenheim; Erna has met Julia once, at the Feier |
| late November | 10 — Bruckner announces he stops at the end of the year |
| late November | 11 — Jule's class trip |
| December | 12 — the farewell in the courtyard |

## Cast

Same house as Batches 1–6, now November. **Julia** (fourth floor), **Tobi**, **Jule**
(Tobi's sister, the student), **Frau Wolf** (next door, widowed), **Herr Bruckner** (the
caretaker). This is the batch where the house acquires relatives, so it is also the only
one that adds people:

- **Gisela** and **Werner Wagner** — Tobi's parents (Tobi is *Herr Wagner* at the dentist,
  Batch 2, Text 5). **Kai**, his older brother, whose suit Tobi wore in Batch 5.
- **Elke** (Tobi's aunt, Werner's sister) and **Rolf** (his uncle); their son **Kevin** —
  the cousin who married in September (Batch 5, Text 3) — and their daughter **Sandra**,
  who is divorced from **Micha**.
- **Oma Erna**, 84, Werner's and Elke's mother, in the Altenheim (Text 9). Gisela's
  mother-in-law in Text 2 is Erna.
- **Frau Sattler**, pregnant, and her husband, who move into the second floor (Text 5).
- **Herr Krämer**, the teacher on Jule's class trip, and **Amir**, thirteen (Text 11).

---

### Scene 1 — Die Serviette

- **Premise:** The café across the street (Batch 3, Text 8), two evenings before Julia
  meets Tobi's family — everybody except Jule, whom she knows — for the first time. She has asked him to draw the family; he is drawing it on a napkin while
  the coffee arrives.
- **Angle:** The diagram grows a line every time he remembers somebody, until the napkin
  is full and the last figure is squeezed into a corner — and that squeezed figure is the
  one Julia has to be nice to. Tobi's own family is news to Tobi twice.
- **Words (9):** die Familie *(owner)*, die Eltern *(owner)*, die Mutter *(owner)*,
  der Vater *(owner)*, das Kind *(owner)*, der Bruder *(owner)*, die Schwester *(owner)*,
  die Geschwister *(owner)*, der Name *(owner)*
- **Chunks:** `Familie und Kind` (649), `Familie und Eltern` (110), `zu Familie gehören`,
  `Wie ist Ihr Name?` (CSV), `an den Namen erinnern` (CSV)
- **Deliberately absent:** `Frau`, `Mann` (Text 2 — and therefore no Frau Wolf),
  `der Sohn` (Text 4), `die Tochter` (Text 9), `Leute` (Text 6), `jung` (Text 4)
- **Glue:** *wieso*, *überhaupt*, *nämlich*, *eben*, *irgendwann*, *und zwar*

### Scene 2 — Der Sitzplan

- **Premise:** Kevin married at the Standesamt in September — that is the ceremony where
  Tobi held the rings in front of the whole Saal with a glued-on button (Batch 5, Text 3).
  The party was put off to November (*"die Hochzeit feiern wir im November nach"* — the
  bare *Hochzeit*, since the scanner does not read it inside *Hochzeitsfeier*), and Gisela is doing its seating plan at the
  kitchen table. Tobi has been given the job of carrying the cards from one pile to the
  other. Kevin is therefore already *verheiratet* in this text, which is what the word is
  for.
- **Angle:** Every arrangement solves one problem and creates the next. Sandra and Micha
  are divorced and cannot sit together; Micha's new partner cannot sit near Gisela's
  mother-in-law; and the only chair nobody objects to is at the children's table.
- **Words (10):** die Hochzeit *(owner)*, heiraten *(owner)*, verheiratet *(owner)*,
  die Ehe *(owner)*, das Ehepaar *(owner)*, sich scheiden lassen *(owner)*,
  geschieden *(owner)*, Schwieger- *(owner)*, der Mann *(owner)*, die Frau *(owner)*
- **Chunks:** `eine Hochzeit planen` (612), `die Hochzeit findet statt` (378),
  `zur Hochzeit kommen` (743), `die Ehe der Eltern` (139), `Wir besuchen morgen meine
  Schwiegereltern` (CSV), `Das Ehepaar unter uns hat zwei Kinder` (CSV)
- **Deliberately absent:** `das Paar`, `der Kuss`, `küssen`, `der Freund` (Text 7),
  `die Dame`, `(sich) verändern` (Text 12), `die Scheidung`, `die Trennung`,
  `getrennt`, `der Partner`, `die Beziehung`, `die Ehefrau` (Text 8),
  `die Einladung`, `einladen` (Text 6), `jung` (Text 4)
- **Glue:** *entweder … oder*, *sonst*, *bloß*, *deswegen*, *auf keinen Fall*, *entfernt*

### Scene 3 — Am Büfett

- **Premise:** The Feier itself, Saturday evening, in a Lokal. Julia is in the buffet queue
  with Tobi's aunt Elke, having been introduced to about thirty people and retained none.
- **Angle:** Elke re-identifies everybody by what is on their plate, which works
  perfectly and explains nothing; and she will not let Julia past the table until she has
  taken a second helping. Rolf watches the national side on his phone behind a pillar.
- **Words (9):** der Onkel *(owner)*, die Tante *(owner)*, der Cousin / die Cousine
  *(owner)*, der Neffe *(owner)*, die Nichte *(owner)*, der / die Verwandte *(owner)*,
  verwandt *(owner)*, (sich) zwingen *(owner)*, der Wirt / die Wirtin *(owner)*
- **Chunks:** `Zu meinem Geburtstag kommen alle Verwandten` (CSV), `Ich kenne die Wirtin
  von diesem Lokal` (CSV), `Bitte zwing mich nicht etwas zu essen` (CSV),
  `Eltern und Onkel` (31), `Eltern und Tante` (29)
- **Deliberately absent:** `die Leute` (Text 6 — the scene says *die Gäste*),
  `das Mädchen`, `der Junge` (Text 4 — *die Kleinen*), `der Name` is Text 1's but may
  recur here, `die Person` (Text 5)
- **Glue:** *irgendein*, *national-*, *beziehungsweise*, *jeweils*, *weder … noch*,
  *ausgerechnet*
- **Note:** carries the glue word `national-` (`die Nationalmannschaft`) and the batch's
  one *irgendein* — the form the official list misprints as `irgendirgendein`.

### Scene 4 — Die Kinder im Hof

- **Premise:** Frau Wolf and Julia at Frau Wolf's kitchen window, which looks onto the
  courtyard (her bedroom faces the street, Batch 6, Text 6), on a Saturday. Four children
  are playing below; one of them is standing on the bicycle rack.
- **Angle:** Frau Wolf delivers a complete theory of modern child-rearing, and the boy
  she has just written off as badly brought up is the one who comes up two minutes later
  to carry her shopping. She does not retract a word.
- **Words (10):** der Hof *(owner)*, der Junge *(owner)*, jung *(owner)*, das Mädchen
  *(owner)*, der Sohn *(owner)*, der Kindergarten *(owner)*, erziehen *(owner)*,
  die Erziehung *(owner)*, verantwortlich *(owner)*, die Verantwortung *(owner)*
- **Chunks:** `Die Kinder spielen am liebsten im Hof` (CSV), `eine gute Erziehung` (242),
  `eine strenge Erziehung` (26), `die Erziehung der Kinder` (130),
  `Verantwortung übernehmen` (5475), `Verantwortung tragen` (2795),
  `Sie tragen die Verantwortung für Ihre Kinder` (CSV), `In der Schulklasse sind 15
  Jungen und 10 Mädchen` (CSV)
- **Deliberately absent:** `erwachsen`, `der Erwachsene` (Text 11 — she says
  *wenn sie groß sind*), `der Nachwuchs` (Text 5), `die Person` (Text 5)
- **Glue:** *anscheinend*, *dauernd*, *neulich*, *zumindest*, *nach wie vor*, *hinunter*

### Scene 5 — Die Anmeldung an der Tür

- **Premise:** The second-floor flat has been empty since summer. Bruckner catches the
  new tenant in the doorway with the Verwaltung's registration sheet while two men carry
  a wardrobe past them.
- **Angle:** He asks the form's questions in the form's order; she answers the question
  after the one he asked, because she is watching the wardrobe. The number of residents
  is the last field and the only one that turns out to be wrong.
- **Words (10):** einziehen *(owner)*, der Familienname *(owner)*, der Vorname *(owner)*,
  der Familienstand *(owner)*, männlich *(owner)*, die Person *(owner)*, persönlich
  *(owner)*, die Schwangerschaft *(owner)*, der Nachwuchs *(owner)*, die Geburt *(owner)*
- **Chunks:** `Ludin ist mein Familienname` (CSV), `Mein Vorname ist Thomas` (CSV),
  `Bei "Familienstand" musst du "ledig" ankreuzen` (CSV), `Kreuzen Sie bitte an:
  "weiblich" oder "männlich"` (CSV), `Eintritt pro Person` (CSV), `Ich muss Herrn Meier
  persönlich sprechen` (CSV), `Wir gratulieren zur Geburt eures Kindes` (CSV)
- **Deliberately absent:** `die Leute` (Text 6), `die Familie` recurs freely (Text 1),
  `die Hausfrau / der Hausmann` (Text 10)
- **Glue:** *ledig*, *ankreuzen*, *folgend-*, *jeweils*, *momentan*, *und so weiter*
- **Note:** ten words, and the second form-filling scene in the corpus after Batch 6's
  Text 4. Deliberately given the opposite texture: nobody is sitting down, the sheet is
  on a wardrobe, and each answer is interrupted. A form is still the one situation in
  which a second speaker asks eight consecutive questions without it being a drill.

### Scene 6 — Die Liste für Samstag

- **Premise:** Julia's birthday is on Saturday. She and Jule are writing the invitations
  at the kitchen table, which means writing the guest list, which has not converged.
- **Angle:** Nobody is added because Julia wants them; every addition is a debt. The
  list grows by obligation until the flat is too small, and the one name Jule adds
  without asking is the one Julia would never have dared leave off.
- **Words (8):** die Einladung *(owner)*, einladen *(owner)*, der Geburtstag *(owner)*,
  das Geschenk *(owner)*, schenken *(owner)*, die Leute *(owner)*, der / die Bekannte
  *(owner)*, freundlich *(owner)*
- **Chunks:** `eine Einladung bekommen` (453), `eine Einladung schicken` (308),
  `eine freundliche Einladung` (48), `zur Hochzeit einladen` (560), `ein Geschenk
  besorgen` (258), `ein Geschenk mitbringen` (457), `Herzlichen Glückwunsch zum
  Geburtstag` (CSV), `In Hannover wohnen Bekannte von mir` (CSV)
- **Deliberately absent:** `die Person` (Text 5 owns it — the list counts *Leute*),
  `der Freund` (Text 7), `die Freundschaft` (Text 12), `die Dame` (Text 12)
- **Glue:** *unbedingt*, *meinetwegen*, *höchstens*, *ohnehin*, *zumal*, *einverstanden*

### Scene 7 — Die Schuhe

- **Premise:** Friday evening. Jule has come by to return a book and is leaving again
  after four minutes. Julia notices the shoes.
- **Angle:** Jule denies having anywhere to be, in a pair of shoes she has never worn to
  return a book. Every denial adds a detail nobody asked for. Tobi, arriving as she
  leaves, settles it: he has just seen her kiss somebody in the street. `das Paar` is the
  couple sense (*"Die sind doch ein Paar!"*); the shoes are never called a *Paar*.
- **Words (8):** (sich) verabreden *(owner)*, verabredet *(owner)*, die Verabredung
  *(owner)*, küssen *(owner)*, der Kuss *(owner)*, heimlich *(owner)*, das Paar *(owner)*,
  der Freund *(owner)*
- **Chunks:** `Gib der Mama einen Kuss!` (CSV), `Ina und Pedro sind ein Paar` (CSV),
  `Gestern habe ich gehört, dass mein Sohn heimlich raucht` (CSV — the *heimlich*
  register, not the smoking), `zum Abschied küssen` (120)
- **Deliberately absent:** `der Partner`, `die Beziehung` (Text 8), `die Freundschaft`
  (Text 12), `der Abschied` (Text 12)
- **Glue:** *bloß*, *angeblich*, *doch*, *sowieso*, *na also*, *offenbar*

### Scene 8 — Die Wohnung unter Julia

- **Premise:** Bruckner is fitting a second doorbell to the third-floor flat, directly
  under Julia's. Julia asks why one flat needs two.
- **Angle:** The flat has been divided rather than vacated — he lists which room now
  belongs to whom, and the kitchen is shared on alternate weeks. Bruckner's position is
  that this is none of his business, held while giving the complete floor plan.
- **Words (7):** (sich) trennen *(owner)*, die Trennung *(owner)*, getrennt leben
  *(owner)*, der Partner / die Partnerin *(owner)*, die Beziehung *(owner)*,
  die Scheidung *(owner)*, die Ehefrau *(owner)*
- **Chunks:** `Die Trennung von der Familie war schwierig` (CSV), `Meine Kollegin ist
  noch nicht geschieden, aber sie lebt in Trennung` (CSV), `Wann war die Scheidung?`
  (CSV), `eine feste Beziehung` (571), `eine komplizierte Beziehung` (147),
  `Wir haben gute Beziehungen zu unseren Nachbarn` (CSV)
- **Deliberately absent:** `geschieden`, `sich scheiden lassen` (Text 2 owns both — this
  text says *Scheidung* and *getrennt* and never the participle)
- **Glue:** *offenbar*, *inzwischen*, *jeweils*, *angeblich*, *das geht mich nichts an*,
  *abwechselnd*

### Scene 9 — Besuchszeit

- **Premise:** Julia has driven Tobi to the Altenheim to visit Oma Erna. It is Wednesday,
  and Wednesday at four is chair gymnastics.
- **Angle:** They came to cheer her up. She has a schedule, three friends waiting, and
  a firm view on which of her descendants actually visits — delivered as a complaint
  while she is putting her shoes on to leave. The visit lasts as long as she allows.
- **Words (11):** die Oma *(owner)*, der Opa *(owner)*, das Altenheim *(owner)*,
  der Bewohner / die Bewohnerin *(owner)*, der Enkel / die Enkelin *(owner)*,
  alt *(owner)*, das Alter *(owner)*, die Senioren *(owner)*, der / die Angehörige
  *(owner)*, die Tochter *(owner)*, geboren werden *(owner)*
- **Chunks:** `Die Großeltern unserer Nachbarn sind im Altenheim` (CSV), `Alle meine
  Enkel gehen schon zur Schule` (CSV), `Der Arzt darf nur Familienangehörigen Auskunft
  geben` (CSV — but the text must say the **bare** *Angehörige*, since *Familienangehörige*
  does not match), `Dieser Computerkurs ist für Senioren` (CSV), `Wir sind etwa im
  gleichen Alter` (CSV), `Ich kenne die anderen Hausbewohner nicht` (CSV — again, the
  text says the bare *Bewohner*)
- **Deliberately absent:** `das Altersheim` (Text 10), `der Rentner`, `die Rente`
  (Text 10), `die Verwandten` (Text 3)
- **Glue:** *mobil-*, *rechtzeitig*, *vorbei-*, *inzwischen*, *ausgerechnet*, *na ja*
- **Note:** the batch's fullest scene at eleven, and the only one where a list of people
  is in character: Erna is *counting who comes and who does not*, which is a complaint,
  not an enumeration. Carries the glue word `mobil-`.

### Scene 10 — Bruckner hört auf

- **Premise:** Bruckner tells Frau Wolf on the stairs that he is stopping at the end of
  the year. He has been the caretaker for twenty-one years (*"seit zwanzig Jahren"* when
  Julia moved in, Batch 1, Text 1, a year ago).
- **Angle:** Frau Wolf takes it as a personal betrayal and negotiates — first for two
  more years, then for one. What finally reconciles her is the discovery that he is not
  moving away: he lives alone with the cat (Batch 3, Text 3; Batch 4, Text 2), so he will
  be at home all day with nothing to do and can therefore still be phoned. `Hausmann` is
  what he announces he will become — for himself and the cat.
- **Words (7):** die Rente *(owner)*, in Rente gehen / sein *(owner)*, der Rentner /
  die Rentnerin *(owner)*, das Altersheim *(owner)*, der Chef / die Chefin *(owner)*,
  die Bevölkerung *(owner)*, die Hausfrau / der Hausmann *(owner)*
- **Chunks:** `in Rente gehen` (568), `in Rente sein` (580), `Rente bekommen` (132),
  `Ich gehe Ende des Jahres in Rente` (CSV), `Mein Nachbar ist seit zehn Jahren in Rente`
  (CSV), `Das kann ich nicht allein entscheiden, da muss ich erst die Chefin fragen`
  (CSV), `Mein Mann ist Hausmann und kümmert sich um die Kinder` (CSV), `11 % der
  Bevölkerung wurden nicht im Inland geboren` (CSV)
- **Deliberately absent:** `das Altenheim` (Text 9), `die Senioren` (Text 9),
  `der Abschied` (Text 12 — this is the announcement, Text 12 is the party)
- **Glue:** *demnächst*, *keineswegs*, *stattdessen*, *insgesamt*, *ach was*, *nachdem*
- **Note:** three of its seven words share the root *Rente*. Guarded by giving each a
  different speaker and a different grammatical shape — *"ich gehe in Rente"* (his plan),
  *"Von der Rente?"* (her objection), *"ein armer Rentner"* (what he calls himself, shrugging
  off her objection).

### Scene 11 — Zweite Nacht, Jugendherberge

- **Premise:** The class trip Jule is helping to supervise. Half past ten, the corridor
  of a youth hostel, Jule and Herr Krämer outside a door somebody is crying behind.
- **Angle:** Jule is twenty-one, on the trip as a paid Betreuerin (a student job, which is
  why she is there at all), and has been adopted by the thirteen-year-olds as one of
  them, which is fine until she has to be the one who turns the lights out. And Amir's
  homesickness is for a city he left when he was four — he is missing a childhood rather
  than a place, which Jule recognises because she did the same thing in the same hostel.
- **Words (8):** der / die Jugendliche *(owner)*, die Jugend *(owner)*,
  die Jugendherberge *(owner)*, erwachsen *(owner)*, der Erwachsene *(owner)*,
  das Heimweh *(owner)*, die Heimat *(owner)*, die Kindheit *(owner)*
- **Chunks:** `Wo habt ihr übernachtet? – In einer Jugendherberge` (CSV), `Ich habe oft
  Heimweh nach meiner Familie` (CSV), `Das ist meine neue Heimat` (CSV), `Jugend und
  Kindheit` (70), `in meiner Jugend` (57), `Die Jugendlichen gehen gerne in die Disko`
  (CSV), `Erwachsene zahlen 5 Euro, für Kinder ist der Eintritt frei` (CSV)
- **Deliberately absent:** `der Abschied`, `(sich) verabschieden` (Text 12 — the last
  morning of a class trip is where both live, and this text is the second night for
  exactly that reason)
- **Glue:** *halb*, *irgendwo*, *bisher*, *vorhin*, *im Grunde*, *damals*

### Scene 12 — Der Hof im Dezember

- **Premise:** Frau Wolf has organised a farewell for Bruckner in the courtyard. Thirty
  people, a folding table, and Bruckner, who was told it was a meeting about the bins.
- **Angle:** He hates it, says so, and cannot leave. Being called the house's hero is the
  thing he objects to most; his counter-argument is a list of things he never fixed. The
  farewell he does manage is to the courtyard rather than to anybody in it.
- **Words (7):** der Abschied *(owner)*, (sich) verabschieden *(owner)*,
  die Freundschaft *(owner)*, der Held / die Heldin *(owner)*, der Nichtraucher /
  die Nichtraucherin *(owner)*, (sich) verändern *(owner)*, die Dame *(owner)*
- **Chunks:** `Abschied nehmen` (1654), `der Abschied fällt schwer` (168 + CSV: *"Der
  Abschied von meinen Freunden fiel mir schwer"*), `Es ist schon 23 Uhr. Ich möchte mich
  verabschieden` (CSV), `Er spielt gern den Helden` (CSV), `Sie ist die Heldin des Tages`
  (CSV), `In unserer Familie sind alle Nichtraucher` (CSV), `Wir haben uns lange nicht
  gesehen. Aber du hast dich gar nicht verändert` (CSV), `Sie ist eine nette alte Dame`
  (CSV)
- **Glue:** *passiv*, *ehrlich gesagt*, *allmählich*, *dermaßen*, *im Übrigen*, *bloß*
- **Note:** the last text owns the five words every earlier text had to avoid
  (`Abschied`, `Held`, `Dame`, `Freundschaft`, `verändern`), which is why it is last.
  Carries the glue word `passiv`.

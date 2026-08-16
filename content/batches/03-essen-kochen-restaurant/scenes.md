# Batch 3 — Essen, Kochen & Restaurant · Szenenplan

127 target words grouped **by situation** into 12 scenes.

The shape of this batch is a trap of its own. It holds **eleven eating-institution words**
— `Restaurant, Lokal, Gaststätte, Kneipe, Café, Cafeteria, Kantine, Mensa, Imbiss,
Speisewagen, Buffet` — and the obvious move is one scene per institution. That is the word
list driving the structure again, only with synonym-avoidance as the new sort key instead
of the alphabet. So the test applied to every scene below was: **would this premise exist
if the vocabulary didn't need housing?** Four candidates failed it and were cut; their
words are mentions inside scenes that pass (`der Speisewagen` is one line in Scene 12,
`die Kantine` one line in Scene 9, `die Gaststätte` one line in Scene 4). A mention is a
sighting, and coverage needs exactly one.

The second shape problem: ~55 of these words are edible nouns, and a scene that walks
through food is a menu, not a conversation. The rule applied throughout: **a foodstuff
appears only where somebody wants it, refuses it, or has ruined it** — never because it is
the next item on a shelf.

Cast carried over from Batches 1 and 2, same house, now late winter into spring:
**Julia** (fourth floor), **Tobi** (the friend who eats), **Frau Wolf** (next door, widowed),
**Herr Bruckner** (the caretaker, whose shoulder finally got operated on). New this batch:
**Frau Aydin** (the baker), **Herr Pohl** (the butcher), **Jule** (Tobi's sister, a student),
and an **Ober** who is addressed as such and never named.

**Standard German only.** `Kloß`/`Knödel`, `Karotte`/`Möhre`, `der Ober`, `das Brötchen`,
`die Aprikose`, `der Fasching` all carry A/CH cross-references in the source list. The pairs
are split across distant texts — and **no speaker ever remarks on the naming.** No
"bei uns sagt man …" line exists in this batch.

**Synonym sets, and where they landed** (checked before a line was written):

| set | scenes |
|---|---|
| `der Kloß` / `der Knödel` | 6 / 7 |
| `die Karotte` / `die Möhre` | 4 / 5 |
| `das Dessert` / `die Nachspeise` | 8 / 7 |
| `die Lebensmittel` / `das Nahrungsmittel` | 4 / 11 |
| `ernähren` / `verpflegen` | 1 / 12 |
| `das Essen` / `die Mahlzeit` | 6 / 12 |
| `Restaurant` / `Lokal` / `Gaststätte` / `Kneipe` | 7 / 6 / 4 / 10 |
| `Café` / `Cafeteria` / `Kantine` / `Mensa` | 8 / 12 / 9 / 11 |

`die Butter` and `die Margarine` share Scene 1 on purpose: they are two different substances
and the line is a **correction** (*"Das ist keine Butter."*), which is the one context where
German actually puts a near-pair in one breath.

---

### Scene 1 — Frühstück im vierten Stock
- **Premise:** Julia's first real breakfast in the new flat. Tobi has emptied the honey jar and is now explaining nutrition to her.
- **Angle:** He lectures on `Ernährung` with a spoon in the jar; the margarine he bought to save money is the one thing nobody will touch.
- **Words (15):** das Brötchen, die Butter, die Margarine, die Marmelade, der Honig, der Kaffee, die Milch, die Kanne, die Tasse, der Tee, Tee ziehen lassen, das Müsli, süß, die Ernährung, ernähren
- **Glue:** *entweder … oder*, *statt*, *nämlich*, *unbedingt*, *möchten*, *mögen*, *Lieblings-*, *übrig*

### Scene 2 — Bäckerei am Faschingsdienstag
- **Premise:** Frau Aydin's bakery, seven in the morning, the counter half empty because of Fasching. Julia wants the plain loaf; there is only the sweet stuff left.
- **Angle:** The bread she finally gets is two days old, and she nearly breaks a tooth on it — the second dental emergency of her tenancy.
- **Words (10):** die Bäckerei, das Brot, das Gebäck, der Kuchen, die Torte, backen, das Mehl, der Fasching, brechen, die Sahne
- **Glue:** *woher*, *sondern*, *allerdings*, *beinahe*, *klar*, *höchstens*
- **Note:** `brechen` in the CSV's own sense (*sein Bein ist gebrochen*) — a tooth, not bread.

### Scene 3 — Beim Metzger
- **Premise:** Herr Pohl's counter. Bruckner, who lives alone, is buying a roast for six people.
- **Angle:** He will not admit it is all for him, so he invents guests; Pohl keeps adding to the order for the guests.
- **Words (10):** der Metzger, das Fleisch, das Hackfleisch, der Schinken, die Wurst, das Schnitzel, der Braten, das Hähnchen, roh, fett
- **Glue:** *wie viel*, *pro*, *mindestens*, *natürlich*, *selbstverständlich*, *die Bedingung*, *komisch*

### Scene 4 — Auf dem Markt, nach einem schlechten Jahr
- **Premise:** Saturday market with Frau Wolf, who has an opinion about this year's harvest and buys everything anyway.
- **Angle:** She condemns every crate, tastes from three of them, and blames the weather — then admits her own balcony tomatoes died because she watered them daily.
- **Words (16):** das Obst, das Gemüse, der Apfel, die Banane, die Orange, die Zitrone, die Pflaume, die Aprikose, die Ernte, sauer, die Tomate, probieren, die Lebensmittel, die Karotte, die Gaststätte, gießen
- **Glue:** *je … desto*, *trotz*, *deswegen*, *offenbar*, *zwar*, *manch-*, *entlang*, *vermutlich*
- **Note:** `gießen` in the CSV sense (*ich muss meine Blumen gießen*), not "pour tea".

### Scene 5 — Abendessen nach Rezept
- **Premise:** Julia's kitchen. Tobi is cooking from a recipe on his phone and reading the steps in the wrong order.
- **Angle:** He salts twice because he forgot he already had, then tries to fix it with vinegar, then with more spices.
- **Words (13):** kochen, das Rezept, zubereiten, die Zwiebel, der Pilz, das Fett, das Gewürz, das Salz, der Pfeffer, salzig, der Essig, schmecken, die Möhre
- **Glue:** *nachdem*, *bevor*, *indem*, *sodass*, *gleichzeitig*, *total*, *durcheinander*, *die Folge*
- **Note:** the text has only *anbraten*, a different lemma, so **both `braten` and
  `der Braten` are owned by Scene 3** (*"gebraten ist es hervorragend"* / *"ich brauche
  einen Braten"*). Cut both cloze cards from Text 3.

### Scene 6 — Sonntagsessen bei Frau Wolf
- **Premise:** Frau Wolf has cooked for four and three people came. Bruckner is on his third plate and she is not finished serving.
- **Angle:** He says he is full at the beginning of the meal and keeps eating for another twenty minutes; she treats *satt* as a challenge.
- **Words (9):** das Essen, essen, die Kartoffel, der Kloß, die Bohne, die Soße/Sauce, das Lokal, satt, das Gericht
- **Glue:** *solange*, *als ob*, *jemals*, *besonders*, *ebenfalls*, *meinetwegen*, *das Gegenteil*
- **Note:** the `Lokal` line is Frau Wolf on the place at the corner that closed — one mention.

### Scene 7 — Im Restaurant
- **Premise:** Julia and Tobi's first evening out. The Ober recommends exactly one dish and it is the one that is finished.
- **Angle:** He defends the kitchen's honour at length while the food does not arrive; Tobi eventually orders the thing he was talked out of.
- **Words (10):** das Restaurant, die Speisekarte, der Ober, der Gast, das Menü, der Knödel, der Wein, der Service, die Nachspeise, das Buffet
- **Glue:** *weder … noch*, *jedoch*, *während*, *relativ*, *wahrscheinlich*, *die Ausnahme*, *klappen*, *eventuell*

### Scene 8 — Im Café gegenüber
- **Premise:** Frau Wolf and Julia in the café across the street. Frau Wolf orders the darkest thing on the menu and has strong views on what children drink.
- **Angle:** She insists she likes bitter chocolate, tastes it, and quietly orders ice cream.
- **Words (8):** das Café, der Kakao, die Schokolade, das Dessert, das Eis, bitter, der Geschmack, trinken
- **Glue:** *gegenüber*, *je*, *zufällig*, *selber*, *derselbe*, *nett*, *extrem*

### Scene 9 — Grillen im Hof
- **Premise:** First warm evening. Bruckner has dragged a grill into the courtyard, which is against every rule of the building he himself enforces.
- **Angle:** He has brought a crate of beer and forgotten anything to eat; Tobi arrives with salad only, which Bruckner treats as an insult.
- **Words (11):** der Grill, grillen, das Bier, der Alkohol, die Limonade, der Saft, kühl, der Käse, der Salat, die Kantine, das Getränk
- **Glue:** *im Freien*, *sowohl … als auch*, *ausschließlich*, *mehrere*, *sicher*, *freiwillig*, *die Voraussetzung*
- **Note:** the `Kantine` line is Bruckner on twenty years of works-canteen food — one mention.

### Scene 10 — Kneipe, danach Imbiss
- **Premise:** Half past eleven, Tobi wants one more round, Julia wants to go home. They compromise on the snack stand at the corner.
- **Angle:** Julia has been drinking water all evening and is the only one who remembers the conversation; Tobi orders a whole pizza and eats the chips.
- **Words (6):** die Kneipe, die Zigarette, der Imbiss, die Pommes frites, die Pizza, das Mineralwasser
- **Glue:** *worüber*, *nirgends*, *stattfinden*, *komplett*, *wohl*, *seitdem*, *privat*

### Scene 11 — In der Mensa
- **Premise:** Jule shows Tobi how the student canteen works: three counters, one queue, and a cook who has heard every complaint already.
- **Angle:** Tobi orders the vegetarian option to impress his sister and is served the one thing he cannot identify.
- **Words (7):** die Mensa, das Nahrungsmittel, der Reis, die Nudel, der Koch / die Köchin, vegetarisch, die Portion
- **Glue:** *einerseits … andererseits*, *insgesamt*, *möglichst*, *niedrig*, *nutzen*, *speziell*, *korrekt*

### Scene 12 — Frau Wolfs Picknick in der Cafeteria
- **Premise:** Bruckner's shoulder finally got operated on. Frau Wolf and Julia visit; the hospital cafeteria's food is on the table and Frau Wolf will not have it.
- **Angle:** She unpacks a complete picnic from her bag — plates, forks, boiled eggs, a thermos — and lays it out on the cafeteria table while Bruckner, in a dressing gown, is happier than he has been in years.
- **Words (11):** die Cafeteria, das Picknick, das Ei, der Teller, die Gabel, die Suppe, lecker, verpflegen, die Mahlzeit, gemeinsam, der Speisewagen
- **Glue:** *miteinander*, *statt*, *ursprünglich*, *unbedingt*, *hinterlassen*, *die Sache*, *ergänzen*
- **Note:** the `Speisewagen` line is Julia on the train she took to get there — one mention.
  `verpflegen` in the institutional sense (*das Krankenhaus verpflegt vierhundert Patienten*),
  which is why it lives here and not next to `ernähren` in Scene 1.

---

## Re-applying coverage after any rewrite

`vocab.py scan` recomputes rather than increments, so it **drops the two words it cannot
match** every time it runs. After every `scan --apply` on this batch, re-run both:

```bash
python3 tools/vocab.py use --batch 3 --text 8  "das Café"
python3 tools/vocab.py use --batch 3 --text 12 "das Ei"
```

Both are genuinely in the texts (*"wir gehen ins Café gegenüber"*, *"Sechs Eier, hart
gekocht"*); the matcher misses the accented headword and the *-er* plural. Without these
two lines the batch reads 125/127 instead of 127/127.

## Owning scene per word (for Step 5)

With twelve food dialogues, `Kaffee`, `Brot`, `Fleisch`, `essen` and `schmecken` recur across
texts, so `vocab.py scan`'s first-sighting will not always be the scene that owns the word.
**Cut each cloze from the scene listed above**, not from wherever the scanner logged it.
Where the two differ, the scene list here is the answer.

# DWDS-Wortprofil — a working guide

**For:** using www.dwds.de/wp to make the cramming texts in this repo more idiomatic.
**Premise this serves:** it is better to learn *chunks* (word combinations that really
co-occur) than isolated words — and better to learn *frequent* chunks than rare ones.
Wortprofil is the single best free tool for finding out which chunks those are in German.

Everything below was verified against a live Wortprofil page (`Tasse`, saved to
`dwds-cache/Tasse.html`) and the DWDS API docs at https://www.dwds.de/d/api.
Where I'm inferring rather than quoting, it says so.

---

## Part 0 — What Wortprofil actually is

A **Wortprofil** (word profile) is a précis of everything a word does syntactically in a
large corpus. DWDS parsed billions of tokens of German, and for each headword recorded
every other word it entered a *grammatical relation* with, plus how often and how
distinctively.

The critical difference from a plain "collocation list" — and the reason it's worth
learning properly — is that **Wortprofil keeps the grammatical relation**. It doesn't
tell you "*Tasse* goes with *trinken*." It tells you *Tasse* is the **accusative object
of** *trinken*. That's the difference between two words sitting near each other and a
chunk you can actually write down:

> `Tasse` + `trinken` → useless
> `Tasse` **ist Akkusativ-Objekt von** `trinken` → **eine Tasse trinken** ← a chunk

That relation label is where all the value is. Do not throw it away.

**What it is not:** a dictionary (that's `/wb/`), a frequency counter (that's `/api/frequency`),
or a grammar checker. It will not tell you the *case* a preposition governs, and it will
happily show you literary or journalistic combinations far above B1.

---

# PART ONE — BASICS

## 1.1 Getting a page

The URL shape is either of these (they're equivalent):

```
https://www.dwds.de/wp/Tasse
https://www.dwds.de/wp/?q=Tasse
```

Start with the plain one. Then add controls (Part Two).

## 1.2 The anatomy of the page

You get **one table per grammatical relation**, plus one summary table:

| Table | What's in it |
|---|---|
| **Überblick** | The strongest collocates across *all* relations, merged and re-ranked. Each row carries a small **?** icon whose tooltip says `aus der Relation »…«` — that's how you recover which relation a row came from. |
| One table per relation | e.g. `hat Adjektivattribut`, `ist Akkusativ-Objekt von`, `ist in Koordination mit` … |

**Start with Überblick to get the feel of a word, then go to the specific relation
tables to actually harvest chunks.** Überblick is a mixed bag by design; the relation
tables are where chunks are cleanly typed.

## 1.3 The two numbers — and the trap

Every row has exactly two numbers, and beginners misread them constantly.

| Column | What it means | Range |
|---|---|---|
| **logDice** | **Association strength.** "How much more than chance do these two words attract each other?" Corpus-size independent, so comparable across words. | ~0–14; in practice 3 is weak-but-real, 5 is strong, 7+ is near-fixed |
| **Freq.** | **Raw count.** How many times this exact combination was actually seen. | 1 → millions |

**The trap:** logDice rewards *exclusivity*, not usefulness. A word that appears only
ever next to your headword scores enormously even if it occurs 12 times in the whole
corpus. Real rows from `Tasse`:

| collocate | logDice | Freq | verdict |
|---|---:|---:|---|
| `trinken` | 7.8 | 1767 | **gold** — strong *and* common |
| `heiß` | 4.5 | 218 | **gold** — moderate score, but very common |
| `henkellos` | 4.3 | 21 | trap — scores like *heiß*, means "handle-less" |
| `getöpfert` | 3.5 | 12 | trap — "thrown on a potter's wheel" |

Sorting by logDice alone puts `henkellos` and `getöpfert` in your text. Sorting by
frequency alone drowns you in `sein`, `haben`, `werden`.

> ### The two-floor rule
> **Set a floor on *both*, then rank by logDice.**
> For B1 cramming texts: `Freq ≥ 20` **and** `logDice ≥ 3.0`.
> Then read top-down and stop when it stops being imaginable.

This is exactly what `tools/wortprofil.py` implements (`--min-freq` / `--min-dice`).

## 1.4 The relation → chunk mapping (the core skill)

Wortprofil offers 24 relations. Which ones you get depends on the headword's part of
speech. This matrix is copied verbatim from the page's own legend:

| Relation | Substantive | Verben | Adjektive |
|---|:-:|:-:|:-:|
| Überblick | × | × | × |
| hat Adverbialbestimmung | | × | × |
| ist Adverbialbestimmung von | | | × |
| hat Akkusativ-Objekt | | × | |
| ist Akkusativ-Objekt von | × | | |
| hat Dativ-/Genitiv-Objekt | | × | |
| ist Dativ-/Genitiv-Objekt von | × | | |
| hat Präpositionalgruppe | × | × | |
| ist in Präpositionalgruppe | × | | |
| hat Prädikativ | | × | |
| ist Prädikativ von | × | × | × |
| mit Prädikativ | × | | × |
| ist Prädikativ zu | × | × | × |
| hat vergleichende Wortgruppe | × | × | × |
| ist in vergleichender Wortgruppe | × | | |
| hat Adjektivattribut | × | | |
| ist Adjektivattribut von | | | × |
| hat Subjekt | | × | |
| ist Subjekt von | × | | |
| hat Passivsubjekt | | × | |
| ist Passivsubjekt von | × | | |
| hat Genitivattribut | × | | |
| ist Genitivattribut von | × | | |
| ist in Koordination mit | × | × | × |
| tritt auf mit | × | × | × |

Note the **`hat …` / `ist … von`** pairing. It's the same relation seen from the two
ends. Look up the noun `Tasse` and you get `ist Akkusativ-Objekt von → trinken`; look up
the verb `trinken` and you get `hat Akkusativ-Objekt → Tasse, Kaffee, Bier…`. **Which
end you search from determines which list you get** — this is the single most useful
mechanical fact about the tool. Cramming a noun batch? Search the nouns. Cramming the
verb batch (22)? Search the verbs, and you get the objects they take.

Now, the part that turns a table row into German you can write:

| Relation (headword = **L**, collocate = **c**) | Surfaces as | Example from `Tasse` |
|---|---|---|
| hat Adjektivattribut | *ein(e) **c**e **L*** | **eine heiße Tasse** |
| ist Akkusativ-Objekt von | ***L*** *(Akk.)* + ***c*** | **eine Tasse trinken** |
| ist Dativ-/Genitiv-Objekt von | ***L*** *(Dat./Gen.)* + ***c*** | |
| ist Subjekt von | ***L*** ***c****-t* | **die Tasse kostet …** |
| ist Passivsubjekt von | ***L*** *wird* ***c*** | |
| ist in Präpositionalgruppe | ***c*** *… **L*** | **aus der Tasse trinken**, **in die Tasse gießen** |
| hat Präpositionalgruppe | ***L*** *+* ***c*** | **die Tasse im Schrank**, **eine Tasse aus Porzellan** |
| hat Genitivattribut | ***L*** *+* ***c*** | **eine Tasse Kaffee** |
| ist in Koordination mit | ***L*** *und* ***c*** | **Tassen und Teller** |
| hat vergleichende Wortgruppe | ***L*** *wie* ***c*** | |
| tritt auf mit | ***L*** *…* ***c*** (loose, same sentence) | |

> ⚠️ **These are patterns, not finished text — you inflect them.** Two things the data
> never supplies:
>
> **Adjective endings.** The tool's `chunk` column writes `ein(e) heiße(r) Tasse` by
> appending to the stem. That happens to be right for `heiß`, but `hoch` → *hoche* and
> `teuer` → *teuere* are wrong (they're **ein hoher Schrank**, **eine teure Wohnung**),
> and both are on the B1 list. Decline the adjective yourself.
>
> **Case.** `ist in Präpositionalgruppe → gießen in`
> is *in die Tasse* (Akk., direction) but `hat Präpositionalgruppe → in Schrank` is
> *im Schrank* (Dat., location). The tool gives you the pattern; you supply the case.
> This is the one place the data will actively let you write wrong German.

Also note the `hat Genitivattribut` label is a parser artifact for measure phrases: it
reports `Tasse` + `Kaffee`, which surfaces as the plain apposition **eine Tasse Kaffee**,
not *eine Tasse des Kaffees*. Read the label as "these two nouns stack", not literally.

## 1.5 A first pass, start to finish

Task: make `die Tasse` idiomatic.

1. Open `https://www.dwds.de/wp/Tasse`.
2. Skim **Überblick**: `trinken 7.8/1767`, `nippen an 7.0/161`, `Teller 7.0/323`,
   `in Schrank 6.9/290`, `dampfend 6.6/121`, `gießen in 6.3/180`.
3. Apply the two-floor rule and drop what's above B1 (`nippen`, `dampfend`, `schlürfen`).
4. Read off chunks *with their relation*:
   - eine **heiße** Tasse
   - eine Tasse **trinken** / **kochen** / **bestellen** / **spülen**
   - **aus** der Tasse trinken · **in** die Tasse gießen
   - die Tasse **im Schrank**
   - Tassen **und Teller**
   - eine Tasse **Kaffee** / **Tee**
5. Write the scene out of those chunks instead of out of the bare word.

That list is not a vocabulary list. It's a set of sentence skeletons.

---

# PART TWO — ADVANCED

## 2.1 Every control on the page

These are the real form fields, read off the page source — this is the complete set:

| Parameter | Widget | Values | Default | What it does |
|---|---|---|---|---|
| `q` | text | any lemma | — | the headword |
| `pos` | select | `Substantiv`, `Verb`, `Adjektiv`, … (only the ones the word actually has) | auto | disambiguates homographs and picks the relation set |
| `comp` | text | another lemma | *(empty)* | **the comparison word** — see 2.2 |
| `comp-method` | select | `diff` = "Unterschiede zu", `intersection` = "Gemeinsamkeiten mit" | `diff` | how to combine the two profiles |
| `display` | select | `lemma`, `form` = "häufigste Oberflächenform" | `lemma` | show the dictionary form, or the most frequent *inflected* form |
| `by` | select | `logDice`, `Frequency` | `logDice` | sort key (per table; the ⇅ icons in each header toggle it) |
| `minstat` | number | float | `0` | **floor on the association score** (logDice) |
| `minfreq` | number | int | `5` | **floor on raw frequency** |
| `limit` | text | int | `20` (`10` in some links) | rows per relation table |
| `view` | hidden | `table` | `table` | rendering mode |
| `mode` | hidden | `full` | `full` | `full` = show every relation table, not just Überblick |

`minstat` + `minfreq` are the two-floor rule built into the URL. This is the workhorse
URL for this project — paste it and swap the word:

```
https://www.dwds.de/wp/?q=Tasse&pos=Substantiv&minfreq=20&minstat=3&limit=25&by=logDice&view=table&mode=full
```

`display=form` is quietly excellent for a cramming project. Set it and instead of the
lemma `gießen` you see the form actually most used in that slot — you learn the chunk in
the shape you'll meet it in.

## 2.2 Comparison mode — the real advanced feature

Fill in `comp` and you get **two words profiled against each other**. Two methods:

- **`comp-method=diff` ("Unterschiede zu")** — what belongs to *this* word and not the
  other. This is how you learn near-synonyms apart.
- **`comp-method=intersection` ("Gemeinsamkeiten mit")** — the shared ground, i.e. the
  contexts where the two really are interchangeable.

```
https://www.dwds.de/wp/?q=Tasse&comp=Becher&comp-method=diff&pos=Substantiv&mode=full
https://www.dwds.de/wp/?q=Tasse&comp=Becher&comp-method=intersection&pos=Substantiv&mode=full
```

Note that the URL your teacher's example used had `comp-method=diff&comp=` — with `comp`
**empty**, which is just the ordinary single-word view. The feature only engages once
`comp` has a word in it.

**Why this matters more than anything else here for B1:** the B1 wordlist is full of
near-synonym pairs that a learner cannot separate by definition alone, only by
distribution. Run `diff` on these and you get the answer directly from usage:

| pair | the question it settles |
|---|---|
| `Tasse` vs `Becher` vs `Glas` | which vessel takes which drink and which verb |
| `Wohnung` vs `Haus` vs `Zimmer` | batch 1 — which one *mietet* you, which one *baut* you |
| `sagen` vs `sprechen` vs `reden` vs `erzählen` | batch 18 |
| `sehen` vs `schauen` vs `gucken` | |
| `Arbeit` vs `Beruf` vs `Stelle` vs `Job` | batch 14 |
| `Reise` vs `Fahrt` vs `Urlaub` | batch 11 |
| `bekommen` vs `erhalten` vs `kriegen` | batch 22 |

Each such run yields a **contrast pair** you can build one comedic scene around — which
is precisely this repo's method. A text whose joke *is* the distinction between
*mieten* and *vermieten* teaches the distinction better than two separate texts.

## 2.3 Mehrwortausdrücke (`?mwe=`) — chunks of three and more

This is the most on-premise feature on the whole site and it is nearly invisible.

Some collocation rows carry a small **letter icon** (`letter-mwa.svg`) whose tooltip
reads *"für diese Mehrwortverbindung kann ein eigenes Wortprofil angezeigt werden"* —
"a separate word profile can be shown for this multi-word combination." Clicking it goes to:

```
https://www.dwds.de/wp/Tasse/?mwe=10171104
```

What you get is **the Wortprofil of the two-word chunk itself** — i.e. what a *third*
word attaches to *eine heiße Tasse*, or to *aus der Tasse trinken*. That's how you get
from 2-word chunks to 3- and 4-word chunks, which is where German actually lives.

In the saved `Tasse` page, 46 of the 160 parsed rows carry this icon — and **20 of the
28 rows that survive the B1 filter** do, including `trinken`, `heiß`, `gießen in`,
`trinken aus`, `in Schrank`, `Teller`, `Kaffee`, `Tee`. So most of the chunks you'd
actually want can be expanded one level further.

**Use it sparingly and late.** Two-word chunks first; expand only the handful you've
decided a text will be built around.

## 2.4 From a collocation to real sentences

Each collocate is a clickable element carrying a `data-wp-ccid` (collocation id) — the
handle the page uses to pull **the actual corpus sentences** for that combination.
(I read this off the markup rather than clicking through, since fetching `/wp` is off
limits — see §3.2 — but the ccid attribute leaves little doubt. Confirm it in a browser.)
Those sentences are your source of authentic, attested example material, and they show
you the case that Wortprofil's own label omits (§1.4).

For this project the KWIC sentences are usually too hard to use verbatim (newspaper
prose, well above B1), but they are the right place to **check** a chunk you're unsure of.

## 2.5 Traps to know before you trust the output

1. **Corpus skew.** The base corpora are heavily journalistic and written. Spoken,
   domestic, everyday-conversational German is under-represented — which is exactly the
   register batches 1–8 need. `Tasse` gives you `dampfend` and `trüb` from feature
   writing, not from anyone's kitchen. Filter hard by frequency, and sanity-check
   against the Goethe list.
2. **Parser artifacts.** `ist in Koordination mit → Tasse` (self-coordination) appeared
   in the real data. Ignore rows where the collocate is the headword.
3. **Homographs.** Always set `pos` for words like `Bank`, `Schloss`, `Gericht`, `Ton`.
4. **Lemma ≠ the form you write.** `display=form` fixes this; otherwise remember
   Wortprofil is showing you dictionary forms.
5. **No case information.** Restated because it's the one that produces wrong German.
6. **Frequency ≠ level.** High corpus frequency does not mean B1. `Bundesregierung` is
   very frequent. This is why the B1 intersection in Part Three exists.

---

# PART THREE — THE API QUESTION

## 3.1 What DWDS publishes as an API

Documented at https://www.dwds.de/d/api. The endpoints that work and are relevant:

| Endpoint | Gives you | Use in this repo |
|---|---|---|
| `/api/frequency/?q=WORT` | `hits`, `total`, and `frequency` (0–6 log scale) | rank a batch's words by how common they are, so the highest-value words get the most text real estate |
| `/api/wb/snippet/?q=WORT` | existence of a dictionary entry + `wortart` | catch invented words and get part of speech |
| `/api/lemma/goethe/A1.json`<br>`/api/lemma/goethe/A2.json`<br>`/api/lemma/goethe/B1.json` | the official Goethe wordlists with genders + articles | second, independent validation source next to `goethe-b1-wortliste.csv` |
| `/api/wb/random` | 5 random dictionary lemmas | — |
| **`/lemma/csv`** *(and `/lemma/json`)* | **the whole Lemmadatenbank — 279 346 lemmas with a `frequenzklasse` column**, as one 27 MB offered download | rank *every* word in *every* batch by frequency, in **one** request |

### The bulk frequency dataset — the thing worth knowing about

Linked from https://www.dwds.de/lemma/list (and only hinted at in the API docs, under
the frequency section: *"In der Lemmadatenbank … können Sie auch einen kompletten
Datensatz herunterladen"*). It serves with `Content-Disposition: attachment` — an
offered download, not something scraped — and `/lemma` is **not** robots-disallowed.

```csv
"lemma","url","wortklasse","artikeldatum","artikeltyp","frequenzklasse"
"Haus","https://www.dwds.de/wb/Haus","Substantiv","1969","Vollartikel","5"
"Tasse","https://www.dwds.de/wb/Tasse","Substantiv","2023-10-27","Vollartikel","3"
```

`frequenzklasse` is the same 0–6 log band as `/api/frequency`'s `frequency`, precomputed
for every lemma. **One request replaces one-per-word API calls for the entire 2 886-word
Goethe list.** Distribution: band 0 → 111 672 lemmas, 1 → 75 411, 2 → 36 241, 3 → 9 380,
4 → 2 043, 5 → 199, 6 → 43, `n/a` → 44 357.

**Higher = more frequent** (`Haus` 5, `Wohnung` 4, `Tasse` 3, `abwaschen` 2,
`henkellos` 0) — note this is the *opposite* direction from the Leipzig-style
"Häufigkeitsklasse" you may have seen elsewhere, where lower means commoner.

Two limits, both real:

- **It's coarse.** Seven bands over 279k lemmas, so ties are enormous. Use bands to sort
  a batch into tiers; use `/api/frequency`'s raw `hits` to order *within* a tier.
- **Homographs come back `n/a`.** `Schloss` is `n/a` in both its rows because DWDS can't
  attribute the count between *castle* and *lock*. That is "unattributable", **not**
  "rare" — `/api/frequency/?q=Schloss` happily returns 3 368 716 hits, because it
  lemmatises and cumulates. Same for `locker`, `möbliert`. Cross-check `n/a` words
  against the API rather than assuming they're obscure.

> **`/api/frequency` gotcha, found the hard way.** When the input is ambiguous the API
> lemmatises to *several* lemmas, returns them tab-separated, and reports **`hits: 0`**:
> ```json
> /api/frequency/?q=locker → {"lemma":"locker\tlockern","hits":0,"frequency":0,…}
> ```
> `locker` is obviously not a zero-frequency word. **`hits: 0` means "could not
> attribute", not "absent".** Always check whether `lemma` contains a tab before
> believing a zero. `tools/wordfreq.py` flags these as `ambiguous` rather than 0.

Multiple lemmas can be piped: `?q=Haus|Baum`. Both verified live:

```jsonc
// /api/frequency/?q=Tasse
{"frequency":3,"hits":669794,"lemma":"Tasse","q":"Tasse","total":"53217038820"}
// /api/wb/snippet/?q=Tasse|Schrank
[{"url":"…/wb/Tasse","input":"Tasse","wortart":"Substantiv","lemma":"Tasse"},
 {"lemma":"Schrank","wortart":"Substantiv","input":"Schrank","url":"…/wb/Schrank"}]
```

`frequency` is a coarse 0–6 log band, not a rank — `Tasse` and `Schrank` will both come
back as 3. Use `hits` when you need to actually order the words within a batch.

> **Gotcha worth writing down:** those three Goethe lists are **incremental, not
> cumulative**. `B1.json` has 1 842 entries and does **not** contain `trinken` or `heiß`
> — those are A1. A B1 candidate's actual vocabulary is the **union: 3 308 lemmas**.
> Any tool that validates "is this word B1-legal?" against `B1.json` alone will reject
> half the everyday language. `tools/wortprofil.py` unions all three.

## 3.2 There is no *collocation* API — and scraping it is off-limits

**Be precise about what is and isn't available**, because these are two different things:

| | available? | how |
|---|---|---|
| **Frequency** data | **yes, fully** | `/lemma/csv` in bulk, `/api/frequency` per word |
| **Collocation** (Wortprofil) data | **no** | must be read off the rendered `/wp` page |

Everything in Part One and Two is about the second row. Here's what I checked:

- Five plausible endpoints (`/api/wp/relations`, `/api/wp/profile`, `/api/wp/lemma`,
  `/api/wordprofile/relations`, `/api/wp/hits`) all return **404**.
- `/wp/?q=Tasse&format=json` returns **404** — no JSON mode.
- `dwds.min.js` contains **no XHR call** for word profiles. The `/wp/` page is entirely
  server-rendered; the collocation tables are in the HTML you receive.
- The **CSV download icon** on each relation table is pure client-side JavaScript — it
  reads the rendered table and builds the file in your browser. There is no server CSV
  endpoint behind it. (It also exports **only the collocate column** — no logDice, no
  frequency. Noted below.)
- The Wortprofil *software* is open source (GPL-3.0,
  github.com/zentrum-lexikographie/wordprofile), but the DWDS collocation *database*
  is not published as a downloadable release.
- **dstar**, the DWDS corpus platform the API docs point to for "many further research
  options and APIs", lives on two other hosts — and both close the door:
  `ddc.dwds.de/robots.txt` is `Disallow /` for **every** user-agent, and
  `kaskade.dwds.de/robots.txt` disallows `/dstar/` for everyone plus `ClaudeBot`,
  `Claude-Web`, `Claude-SearchBot` and `anthropic-ai` sitewide. The docs also note many
  dstar corpora are login-gated.
- The Zenodo DOI in the docs (10.5281/zenodo.14013687) is the *etymological* headword
  list, not frequency or collocation data.

So the data is only available by rendering the page. And rendering it automatically is
explicitly prohibited:

```
# https://www.dwds.de/robots.txt
User-agent: *
Disallow: /wp                     ← the Wortprofil path, for every user-agent
...
User-agent: anthropic-ai
Disallow: /                       ← the whole site

# Legal Notice: ... Unauthorized use of robots or other automated mechanisms
# to access dwds.de or to gather or mine data is strictly forbidden without
# explicit consent from DWDS. DWDS may, at its discretion, allow specific
# automated access to designated dwds.de pages. To request permission for
# crawling dwds.de, data collection, or usage, please contact <dwds@bbaw.de>.
```

And `dwds_static/tdm-policy.json` grants `tdm:mine` only under an `obtainConsent` duty.

**So: no bulk scraper.** Not "no scraper because it's rude" — the site names the
prohibition and names the exception process. Two legitimate routes remain, and the
second one is worth taking:

1. **You browse, the script parses.** You open the Wortprofil page yourself — an
   ordinary human page view, which is what the site is for — and save it. The script
   reads the saved file and never touches `/wp`. This is what's built.
2. **Ask for consent.** DWDS explicitly invites requests at **dwds@bbaw.de**, and this
   is a personal, non-commercial language-learning use with no redistribution. That's
   about as easy a "yes" as a research institute ever gives. If you get it, the same
   parser flips to fetching directly with a two-second delay and a disk cache — a
   ten-line change. **I'd send the mail; it turns a 148-page manual job into one command.**

## 3.3 What got built instead

`tools/wortprofil.py` — parses saved Wortprofil pages into B1-filtered chunk tables.

```bash
# 1. In your browser, open (swap the word):
#    https://www.dwds.de/wp/?q=Tasse&pos=Substantiv&minfreq=20&minstat=3&limit=25&view=table&mode=full
# 2. Cmd-S → "Web Page, HTML Only" → dwds-cache/Tasse.html
# 3.
python3 tools/wortprofil.py dwds-cache/Tasse.html
python3 tools/wortprofil.py dwds-cache/*.html --tsv > chunks.tsv
python3 tools/wortprofil.py dwds-cache/Tasse.html --all --min-freq 50
```

It:
- extracts `(relation, collocate, logDice, freq, has-MWE)` from every relation table;
- applies the two-floor rule (`--min-freq 20 --min-dice 3.0` by default);
- **intersects the collocates with the Goethe A1∪A2∪B1 lemma set** (via the documented
  API) plus this repo's `goethe-b1-wortliste.csv`, so what survives is *B1-legal*;
- renders each surviving row as a **ready-to-use chunk** via the relation→pattern map
  of §1.4, not as a bare word;
- flags rows that have a Mehrwortausdruck profile available (§2.3).

Note it deliberately does *not* use the site's own CSV export, which drops logDice and
frequency — the two numbers the whole method depends on. Save the HTML instead.

> Non-obvious bit in the B1 filter, in case you ever touch it: collocates arrive as
> `nippen an`, `in Schrank`, `Teelöffel auf` — content word plus preposition, in either
> order. Testing "any token is B1" passes *everything*, because prepositions are always
> B1; that let `aus Porzellan` and `mit Henkel` through on the first run. It tests the
> **content** tokens only, and requires all of them.

---

# PART FOUR — HOW THIS CHANGES THE TEXTS

## 4.1 The actual output, on real data

Run on the saved `Tasse` page, B1-filtered, floors at Freq ≥ 20 / logDice ≥ 3.0:

```
### hat Adjektivattribut
| ein(e) heiße(r) Tasse   | heiß      | 4.5 |  218 |

### ist Akkusativ-Objekt von
| Tasse(Akk.) trinken     | trinken   | 7.8 | 1767 |
| Tasse(Akk.) kochen      | kochen    | 4.2 |   74 |
| Tasse(Akk.) bestellen   | bestellen | 4.0 |  118 |
| Tasse(Akk.) spülen      | spülen    | 4.0 |   31 |

### ist in Präpositionalgruppe
| gießen in … Tasse       | gießen in | 6.3 |  180 |
| trinken aus … Tasse     | trinken aus | 5.4 | 341 |

### hat Präpositionalgruppe
| Tasse + in Schrank      | in Schrank | 6.9 | 290 |

### ist in Koordination mit
| Tasse und Teller        | Teller    | 7.0 |  323 |
| Tasse und Glas          | Glas      | 5.1 |  197 |
| Tasse und Löffel        | Löffel    | 4.2 |   28 |

### hat Genitivattribut
| Tasse Kaffee            | Kaffee    | 4.7 |  143 |
| Tasse Tee               | Tee       | 4.7 |   78 |
```

160 rows were parsed; **28 survived**. Thrown out by the *B1 filter* despite clearing
both floors: `nippen an` (7.0/161), `dampfend` (6.6/121), `trüb` (6.1/134),
`eingießen` (5.9/66), `einschenken` (5.9/76), `rühren in` (5.5/154), `Untertasse`,
`schlürfen`, `servieren`, `abstellen`, `füllen`, `aus Porzellan`, `mit Henkel`,
`henkellos` — 51 rows in all. Thrown out by the *frequency floor*: `getöpfert` (3.5/12),
`geblümt` (3.4/12). Every one of those would have looked attractive on a
logDice-sorted list, and several would have looked like perfectly ordinary German.

## 4.2 Before / after

Batch 1, Text 1 currently contains:

> … wasche schnell **zwei Tassen ab** …

Nothing is wrong with it. But `zwei Tassen` is an arrangement I invented to give the
target word `abwaschen` something to act on. The chunk table offers attested
alternatives — subject to **two constraints that outrank idiomaticity**:

- **the scene's target words must survive** (`abwaschen` is batch 1's target here — it stays);
- **no cross-batch imports.** `Teller`, `Kaffee` and `spülen` are batch 3 (Essen); pulling
  them into a batch-1 text breaks the concrete→abstract cram order. Of `Tasse`'s
  collocates, only `Schrank`, `Glas` and `Löffel` are batch-1 words.

Under those constraints:

> … **wasche** die **Tassen, Gläser und Löffel ab** und stelle sie **in den Schrank** …

`Tasse und Glas` (5.1/197), `Tasse und Löffel` (4.2/28), `in Schrank` (6.9/290) — three
attested units, target word intact, no vocabulary borrowed from a later batch. And
*in den Schrank* drills accusative-of-direction, which the original clause didn't touch.

**That's the argument.** Same scene, same target word, but the grammar *between* the
words is now attested rather than merely plausible. Memorizing the text installs the
collocational grammar too — the part that keeps learners sounding foreign long after
their vocabulary is fine.

> **Caveat on this very example:** `Tasse` is a batch-3 word; I used it because it's the
> one profile saved in `dwds-cache/`. A real Step 2b harvests profiles for the batch's
> **own** load-bearing words (for batch 1: `Wohnung`, `Schrank`, `Fenster`, `Miete`,
> `putzen`, `umziehen`…), and the chunks then fall inside the batch by construction.

## 4.3 Where it plugs into the pipeline

One new optional step, between **Step 2 (freeze wordlist)** and **Step 3 (write texts)**
of `TEXT-WRITER.md`:

> **Step 2b — Harvest chunks (optional but recommended).** For the ~10–20 *load-bearing*
> nouns and verbs of the batch (not all 148 words — the ones the scenes actually turn
> on), open the Wortprofil URL, save the page to `dwds-cache/`, and run
> `tools/wortprofil.py`. Write the surviving chunks into `batch-NN-*/chunks.md`. In
> Step 3, build sentences **out of those chunks** rather than out of bare words.

Two cheap wins to layer on later:

- **Order the batch by frequency** — `tools/wordfreq.py` does this, and unlike the
  collocation side it needs no manual page-saving at all. On batch 1 it separates
  `Haus`/`Platz`/`Uhr` (band 5) from `Fauteuil`/`Stiegenhaus` (band 1) — so the scene
  can give the common words the prominent, most-memorable positions instead of whatever
  position the alphabet handed them.

  ```bash
  python3 tools/wordfreq.py batch-01-in-der-wohnung/wordlist.md   # bulk CSV, 0 requests
  python3 tools/wordfreq.py --words Schloss locker --hits         # spot-check the n/a's
  ```

  **Don't sweep a whole wordlist with `--hits`.** 148 sequential automated requests is
  the thing robots.txt's legal notice names, documented endpoint or not — and the bulk
  CSV already banded every word, so the sweep buys almost nothing. The tool refuses runs
  over 25 uncached words for exactly this reason.
- **Use `comp-method=diff` on the near-synonym pairs** in §2.2 to generate one
  contrast-scene per pair. Those are the texts that will pay off most per minute.

## 4.4 The honest limitation

Wortprofil's corpus is journalistic. It is authoritative on *"how does educated written
German combine these words"* and weak on *"what would someone say in their kitchen."*
For batches 1–8 (Wohnung, Körper, Essen, Kleidung, Familie) expect to discard a lot and
to cross-check the survivors against the Goethe list's own example sentences in
`goethe-b1-wortliste.csv` column 2, which are pitched at exactly the right register.
Use Wortprofil to *rank and validate* candidate chunks — not to source them blindly.

---

---

# PART FIVE — GETTING COLLOCATIONS PROGRAMMATICALLY (NOT FROM DWDS)

DWDS won't give you collocations by API. Other people will. Here is the landscape, all
of it checked rather than remembered.

| Source | Relation-typed? | Programmatic? | Licence | Verdict |
|---|:-:|:-:|---|---|
| **DWDS-Wortprofil** | **yes** | ✗ robots-blocked | — | best data, manual only |
| **Leipzig Corpora Collection API** | no (window) | **✓ yes, today** | **CC BY 4.0** | **use this** |
| **UD German treebanks + your own script** | **yes** | ✓ (offline) | CC BY-SA 4.0 | best DIY; real work |
| Sketch Engine (German Word Sketch) | yes | ✓ API | commercial | costs money |
| IDS Mannheim (KorAP / CCDB) | ? | ? | ? | **not investigated** — see below |

*On the IDS row: all I established is that `korap.ids-mannheim.de/api/v1.0/` and the CCDB
root both return HTTP 200, and that `ids-mannheim.de/robots.txt` only disallows `/typo3/`.
That is not evidence of collocation capability or of what registration gates. IDS holds
DeReKo, the largest German corpus, and COSMAS II has a Kookkurrenzanalyse — so this is
the most promising unexplored lead, but I haven't checked it and you shouldn't treat the
row as verified.*

## 5.1 Leipzig Corpora Collection — the one that just works

```
https://api.wortschatz-leipzig.de/ws/v3/api-docs           ← full OpenAPI 3 spec
https://api.wortschatz-leipzig.de/ws/swagger-ui/index.html ← try it in a browser
```

The spec **declares its own licence as CC BY 4.0** (terms: wortschatz-leipzig.de/usage),
the API host carries no robots restriction, and the description says it exists so you can
access the data "by using a software of your choice". No key, no login. Endpoints:

```
/ws/corpora/availableCorpora                              # 104 corpora, 8 German
/ws/cooccurrences/{corpus}/cooccurrences/{word}?limit=25  # sentence-window
/ws/cooccurrences/{corpus}/leftcooccurrences/{word}       # immediate left neighbour
/ws/cooccurrences/{corpus}/rightcooccurrences/{word}      # immediate right neighbour
/ws/sentences/{corpus}/sentences/{word}                   # example sentences
```

German corpora: `deu_news_2012_3M` (biggest), `deu_news_2012_1M`, `deu_news_2010_1M`,
`deu_wikipedia_2010_1M`, plus 100K/10K samples.

> ### ⚠️ Do not rank by the API's `sig` — and don't carry §1.3's instincts over
> Each row returns `freq` (pair count) and `sig`. The OpenAPI spec documents `sig` as a
> bare `number` with **no description**, so I measured it over the cached results:
> **Pearson r(pair-frequency, sig) = 0.55** — it is frequency-scaled. The preposition
> `in` scores `sig` 1982 on volume alone; `der` scores 474.
>
> That is the **opposite** failure mode from logDice (§1.3). logDice over-rewards
> exclusivity, so you floor the frequency; `sig` over-rewards volume, so ranking by it
> promotes the common and unremarkable. Ranked by `sig`, `Wohnung`'s top collocate is
> `Polizei` (645); `Mieter` (529) sits below it.
>
> **The fix:** the response also carries `w1.freq` and `w2.freq`, so logDice is
> computable — `14 + log2(2·f_AB / (f_A + f_B))`. `tools/leipzig.py` computes and ranks
> by it, which puts `Mieter` (9.1) above `Polizei` (8.4) and makes the *same* two-floor
> reading from §1.3 apply here. The raw `sig` is still printed, for reference only.
>
> **Never compare logDice numbers across the two tools.** Wortprofil counts
> dependency-typed pairs, Leipzig counts sentence-window pairs, so the same word pair
> scores differently. Compare ranks *within* one tool. For the same reason the tool
> applies **no** default logDice floor: window pairs score ~8–9 and immediate-neighbour
> pairs ~5–6, so a single absolute floor silently empties the neighbour tables — which
> is exactly where the verbs are.

**`tools/leipzig.py`** wraps it — same B1 filtering as the Wortprofil tool, plus it drops
closed-class words using this repo's own `groundwork/glue-pool.md` as the stoplist:

```bash
python3 tools/leipzig.py Tasse
python3 tools/leipzig.py Wohnung Schrank Fenster
python3 tools/leipzig.py Wohnung --corpus deu_wikipedia_2010_1M --tsv
```

Real output for `Wohnung` (logDice, glue dropped) — note the right-neighbour table,
which is where the verbs are:

```
window : Mieter 9.1 · tot 8.9 · Fenster 8.5 · Frau 8.5 · Balkon 8.4 · Polizei 8.4
         Mutter 8.3 · Haus 8.3 · Vermieter 8.3 · Uhr 7.6
right  : verlassen 6.5 · kaufen 5.3 · mieten 5.1 · an der 4.5
left   : Ihre 6.2 · seine 6.1 · ihre 5.7
```

`eine Wohnung mieten` / `kaufen` / `verlassen` are exactly the chunks you want, and they
only surface in the right-neighbour table — a reminder to read all three, not just the
big one.

**Three honest limitations:**

1. **No grammatical relation.** This is the big one. You get "*Wohnung* and *mieten* go
   together", not "*mieten* takes *Wohnung* as accusative object". Left/right position is
   a crude substitute — for a noun, right-neighbours skew towards the verb or the noun it
   heads, left-neighbours towards determiners and adjectives.
2. **Small corpora.** 3M sentences vs. DWDS's billions of tokens. `Tasse` occurs 139
   times here; DWDS saw `Tasse`+`trinken` alone 1 767 times. Thin tails just vanish.
3. **News skew, badly.** `tot` (8.9) and `Polizei` (8.4) rank near the top for `Wohnung`
   — that's crime reporting, not domestic life, and logDice doesn't rescue you from it
   because the skew is in the corpus, not the statistic. Worse than DWDS for batches 1–8.
   `--corpus deu_wikipedia_2010_1M` gives a different (not better) bias. This is the
   limitation §5.2 exists to solve.

**Attribution:** CC BY 4.0 means if you ever publish anything derived from it, credit
*Leipzig Corpora Collection, https://wortschatz-leipzig.de/*. The tool prints this.

*(The Leipzig **website** — the bulk-download portal at wortschatz-leipzig.de — sits
behind an anti-scraping proof-of-work challenge. That's for humans in browsers; don't
try to script around it. The API host is the sanctioned programmatic route and is
completely open.)*

## 5.2 The DIY route — the only way to get relation-typed data

If you want what Wortprofil actually has — `ist Akkusativ-Objekt von` — you have to
compute it, which is entirely doable because it's just: parse a corpus, count
head–dependent pairs per relation, score with logDice.

- **Corpus + parses, free:** `UD_German-HDT` and `UD_German-GSD`
  (github.com/UniversalDependencies), both **CC BY-SA 4.0**, already dependency-parsed —
  HDT is ~3.7 GB. No parsing needed, just counting.
- **Or parse your own:** spaCy's `de_core_news_lg` over any text you like.
- **The scoring is not a mystery:** logDice = `14 + log2(2·f_AB / (f_A + f_B))`. The
  relation inventory to aim at is the matrix in §1.4.
- **Or don't write it:** DWDS's own Wortprofil software is **GPL-3.0** at
  github.com/zentrum-lexikographie/wordprofile. It's the exact pipeline that produced
  everything in Part One — only the *database* is unpublished, not the code. Point it at
  a corpus you're allowed to have.

**And this is where you fix the register problem.** Every corpus in this guide is
journalistic. The batches you're cramming first (Wohnung, Körper, Essen, Kleidung) are
domestic and spoken. **OpenSubtitles German via OPUS** (opus.nlpl.eu) is free, enormous,
and is film dialogue — the closest freely available thing to how people actually talk in
a kitchen. Parsing that with spaCy and counting dependency pairs would give you
collocations *better suited to this project than DWDS's*, and completely unencumbered.

That's a weekend project, not an afternoon. But it's the honest answer to "surely this is
possible programmatically": yes — by computing it from a corpus you're licensed to hold,
which is exactly what DWDS did.

> **→ Written up in full as `groundwork/diy-wortprofil-opensubtitles.md`** — verified
> corpus URL and size (950M tokens), spaCy model choice, the extraction loop, the logDice
> scoring, and the costing. Designed and priced, not yet run.

## 5.3 What I'd actually do

1. **Now:** `tools/leipzig.py` for a quick scriptable signal on any word, and DWDS
   Wortprofil saved by hand for the ~10–20 load-bearing words per batch, where the
   relation labels genuinely matter.
2. **Cheap and high-value:** email **dwds@bbaw.de** for permission. Personal,
   non-commercial, no redistribution — and they explicitly invite the request. It's one
   email against a 148-page manual job.
3. **If you get keen:** the DIY pipeline on OpenSubtitles, which beats every option here
   on register for exactly the batches you're cramming first.

---

## Appendix — quick reference

```bash
# The workhorse URL (swap WORT, set pos for homographs)
https://www.dwds.de/wp/?q=WORT&pos=Substantiv&minfreq=20&minstat=3&limit=25&by=logDice&view=table&mode=full

# Near-synonym contrast
https://www.dwds.de/wp/?q=A&comp=B&comp-method=diff&mode=full          # what's unique to A
https://www.dwds.de/wp/?q=A&comp=B&comp-method=intersection&mode=full  # shared ground

# Documented APIs (no consent needed, these are published for programmatic use)
https://www.dwds.de/lemma/csv                            # ALL 279k lemmas + frequency band
https://www.dwds.de/api/frequency/?q=Tasse               # raw hits for one word
https://www.dwds.de/api/wb/snippet/?q=Tasse|Becher
https://www.dwds.de/api/lemma/goethe/{A1,A2,B1}.json     # incremental — union them

# Leipzig Corpora Collection — CC BY 4.0, fully open, no key (see Part Five)
https://api.wortschatz-leipzig.de/ws/v3/api-docs
https://api.wortschatz-leipzig.de/ws/cooccurrences/deu_news_2012_3M/cooccurrences/Tasse?limit=25

# Local
python3 tools/leipzig.py   Tasse Wohnung                 # collocations, scriptable
python3 tools/wortprofil.py dwds-cache/*.html            # collocations (needs saved pages)
python3 tools/wordfreq.py  batch-01-*/wordlist.md        # frequency (fully automatic)
python3 tools/wordfreq.py  batch-01-*/wordlist.md --hits
```

**Rules of thumb**
0. *Frequency* is fully available by API. *Collocations* are too — just not from DWDS:
   Leipzig (CC BY 4.0) is scriptable today, DWDS-Wortprofil is manual-only but is the
   only one that labels the grammatical relation. See Part Five.
1. Two floors, then rank by logDice. Never rank by one number alone.
2. Keep the relation label — it *is* the chunk.
3. Search from the end you're cramming (noun batch → look up nouns; verb batch → verbs).
4. The chunk column is a **pattern**. You supply the case and the adjective ending.
5. Frequent ≠ B1. Intersect with the Goethe list (all three levels).
   And B1-legal ≠ *this* batch — don't import a later batch's vocabulary into an
   earlier batch's text just because the collocation is attested.
6. Don't automate `/wp`. Browse and save — or email dwds@bbaw.de and get permission.

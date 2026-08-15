# Wortprofil — your own collocation database

**What it is:** a relation-typed German collocation database built from 514 million tokens
of film dialogue, sitting on your disk as `data/wortprofil.db`. It answers *"which words really
go with this word, and in what grammatical relation?"* — the same question DWDS-Wortprofil
answers, but queryable from the command line and in a **spoken, domestic register** rather
than a journalistic one.

It exists because DWDS blocks programmatic access (`robots.txt: Disallow /wp`) and Leipzig
gives no grammatical relations. This gives you both, plus **case information that neither
of them publishes**.

> Built from OpenSubtitles, whose licensing is murkier than Leipzig's CC BY 4.0.
> Fine for personal study on your own disk. **Don't redistribute the database.**

---

## Quick start

```bash
python3 tools/wortprofil_db.py Wohnung
```

```
### ist Akkusativ-Objekt von

| chunk                     | collocate  | Kasus | logDice | Freq | B1 |
| Wohnung(Akk.) mieten      | mieten     |       |     9.4 |  519 | ✓  |
| Wohnung(Akk.) verlassen   | verlassen  |       |     8.4 |  932 | ✓  |
| Wohnung(Akk.) suchen      | suchen     |       |     8.3 | 1090 | ✓  |
```

More words, tighter filter, one relation, raw output:

```bash
python3 tools/wortprofil_db.py Wohnung Küche Bad --top 10
python3 tools/wortprofil_db.py Bett --min-freq 50 --min-dice 5
python3 tools/wortprofil_db.py Schrank --relations Präpositional
python3 tools/wortprofil_db.py Wohnung --tsv > chunks.tsv
python3 tools/wortprofil_db.py --info          # what this database was built from
```

---

## Reading the output

| column | meaning |
|---|---|
| **chunk** | the collocation as a droppable pattern — this is the point of the whole thing |
| **collocate** | the partner word alone |
| **Kasus** | case of the noun in a prepositional group. **DWDS does not show this.** |
| **logDice** | association strength. Same statistic DWDS uses. ~6+ is strong, ~4 solid, ~3 weak |
| **Freq** | raw co-occurrence count in the corpus |
| **B1** | `✓` a B1 candidate is assumed to know it (Goethe A1∪A2∪B1), `·` not |

**The chunk column is patterns, not finished German** — exactly as in `tools/wortprofil.py`.
Two things the corpus can't supply: adjective endings (`ein(e) kleine(r) Wohnung`) and,
outside prepositional groups, case. Decline before writing.

### Relations you'll see

`ist/hat Subjekt` · `ist/hat Akkusativ-Objekt` · `ist/hat Dativ-/Genitiv-Objekt` ·
`ist/hat Passivsubjekt` · `ist/hat Adjektivattribut` · `ist/hat Genitivattribut` ·
`ist/hat Prädikativ` · `ist/hat Präpositionalgruppe` · `ist in Koordination mit`

Every relation appears from **both sides**, so `Wohnung` shows you *"Wohnung mieten"* and
`mieten` shows you *"mieten + Wohnung(Akk.)"*. Query whichever word you're writing around.

### The case column, which is the thing DWDS can't do

```bash
python3 tools/wortprofil_db.py Bett --relations Präpositional --top 6
```

```
in liegen … Bett     Dat.  10.2  3811   →  im Bett liegen     (location)
in gehen … Bett      Akk.  10.1  6423   →  ins Bett gehen     (direction)
in schlafen … Bett   Dat.   9.9  2115
in bringen … Bett    Akk.   9.2  2089
```

(Rows come back sorted by logDice, not frequency — `in gehen` is commoner but `in liegen`
is the tighter association.)

Two-way prepositions (`in, an, auf, über, unter, vor, hinter, neben, zwischen`) take
accusative for direction and dative for location. This column tells you which one the
corpus actually uses with that verb — so you don't have to guess when writing a text.

---

## Choosing the filters

Defaults are `--min-freq 20 --min-dice 3.0`, inherited from DWDS. Those were tuned on
*billions* of tokens; this database has 514 million, so they're worth adjusting.

| setting | rows in database | use when |
|---|---:|---|
| `--min-freq 10` | 1,220,952 | a rarer word returns almost nothing |
| `--min-freq 20` (default) | 568,594 | normal |
| `--min-dice 3` (default) | 3,115,036 | you want light verbs too (*Tasse haben/nehmen*) |
| **`--min-dice 4`** | 2,258,626 | **recommended** — cuts light verbs, keeps real collocations |

**Start with `--min-freq 20 --min-dice 4`.** If a word comes back thin, drop to
`--min-freq 10` before touching logDice.

The database itself is stored **unfiltered down to freq 3**, so these are free to change —
nothing needs rebuilding.

### Turning off the B1 filter

```bash
python3 tools/wortprofil_db.py Wohnung --all
```

By default only collocates a B1 candidate is assumed to know are shown. `--all` keeps
everything and marks non-B1 rows `·`:

```
| Wohnung(Akk.) durchsuchen | durchsuchen |  9.7 | 761 | · |    ← added by --all
| Wohnung(Akk.) mieten      | mieten      |  9.4 | 519 | ✓ |
```

**Gotcha:** `--top` applies *after* filtering, so `--all` can push B1 rows off the bottom
of a short list. Raise `--top` when you use it.

---

## One thing to know about this corpus

It's film dialogue, so it leans crime and drama. `Wohnung` returns **`durchsuchen`**
(dice 9.7, f=761) *above* `mieten` (9.4, f=519) — that's police-procedural German.

The domestic vocabulary you actually want is there and strong (`mieten`, `renovieren`,
`vermieten`, `Wohnung ist klein/frei/leer/teuer`, `Wohnung und Job/Auto/Büro`), and it's
far closer to everyday spoken German than any newspaper corpus. But **skim the top rows
before pulling chunks** rather than trusting rank order blindly.

Other noise to expect: character names (proper nouns are kept), and occasional
capitalised imperatives showing up as nouns (`Geh` from *Geh ins Bett!*). The B1 filter
removes both, which is a good reason to leave it on for text-writing.

---

## Raw SQL, when the tool isn't enough

One table. No B1 filtering is applied at this level.

```bash
sqlite3 -header -column data/wortprofil.db \
  "SELECT collocate, case_, freq, round(logdice,1) dice FROM colloc
   WHERE headword='Küche' AND relation='ist in Präpositionalgruppe'
   AND freq>=30 ORDER BY logdice DESC LIMIT 15;"
```

```sql
colloc(headword, relation, collocate, logdice, freq, case_)
```

Useful one-liners:

```bash
# which of a batch's words have usable data?
for w in Wohnung Zimmer Küche Bad Schrank Bett; do
  printf "%-10s %s\n" "$w" "$(sqlite3 data/wortprofil.db \
    "SELECT count(*) FROM colloc WHERE headword='$w' AND freq>=20 AND logdice>=4;")"
done

# what does this word coordinate with? (good for topic-adjacent vocabulary)
sqlite3 data/wortprofil.db "SELECT collocate, freq FROM colloc
  WHERE headword='Teller' AND relation='ist in Koordination mit'
  ORDER BY freq DESC LIMIT 10;"
```

---

## Rebuilding it

You shouldn't need to — but the machinery is still on `atlas` and is resumable.

```bash
ssh andrey@192.168.88.5 '/home/andrey/opus-de/code/launch.sh'   # start or resume
ssh andrey@192.168.88.5 '/home/andrey/opus-de/code/morning.sh'  # full status report
scp andrey@192.168.88.5:/home/andrey/opus-de/work/merged/wp.db data/wortprofil.db
```

The last build: 200 shards, 0 failures, 514M tokens, **5.2 hours**, 5.36M rows.

`launch.sh` skips shards that already finished, so re-running after a crash or reboot
picks up where it stopped. If only the final merge failed, the per-shard counts survive
and re-merging costs **minutes, not another night** — the command is in
`tools/opus/IMPLEMENTATION.md`.

Server disk currently holds `work/shards` (1.1 GB) and `work/counts` (0.97 GB). Counts are
what make a cheap re-merge possible; shards only matter for a full re-parse. Both are
deletable if you need the space.

---

## Troubleshooting

| symptom | cause / fix |
|---|---|
| `no database at .../wp.db` | copy it from the server (above), or pass `--db` |
| `# Wort: no rows` | word absent, or below the floors — try `--min-freq 5 --all` |
| a headword's rows look mangled | `de_core_news_sm` lemma error; check with `--all` and see if a mis-lemmatised variant holds the real counts |
| everything looks weakly associated | you're reading logDice against DWDS intuitions; this corpus is 100× smaller, so compare rows *within* this database |

---

## How this fits the repo

`tools/wortprofil_db.py` renders **the same format** as `tools/wortprofil.py`, so the
chunk-harvesting step of the `text-writer` skill doesn't change — it just stops needing
manually saved DWDS pages.

- `docs/collocations-method.md` — *why* texts are built from attested chunks, and
  how to read a Wortprofil. **Still the conceptual reference; read it first.**
- `docs/collocations-build.md` — the original recipe for this build.
  Note its Step 3 dependency-label table was checked and found wrong in four ways; the
  corrections are in `tools/opus/IMPLEMENTATION.md`.
- `tools/opus/IMPLEMENTATION.md` — for whoever maintains or rebuilds the pipeline.

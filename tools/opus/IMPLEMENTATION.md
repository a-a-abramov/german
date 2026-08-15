# Wortprofil build — implementation notes

**Audience: the agent maintaining or rebuilding this.** For how to *use* the result, see
`docs/collocations-query.md` in the repo root. This file records data structures, the empirical
relation model, and the reasoning behind choices that look arbitrary from the code.

Built 2026-08-13. Implements `docs/collocations-build.md`, **and departs
from it in seven places** — all of them documented below with the evidence.

---

## 1. What exists

```
atlas (192.168.88.5), 4 cores, 11 GB RAM, rootless podman, nothing installed on host
/home/andrey/opus-de/
├── de.txt.gz              1.57 GB   OPUS OpenSubtitles de v2024 (user-supplied)
├── code/                            rsync target for tools/opus/*
└── work/
    ├── shards/            1.1 GB    200 × shard_NNNN.txt.gz + prepare-meta.json
    ├── counts/            0.97 GB   per-shard count tables + .done + .log + run_state.json
    ├── merged/wp.db       1.46 GB   the product
    └── logs/night-*.log             driver log, symlinked as latest.log
```

Image `localhost/wortprofil:de` — python 3.12.13, spaCy 3.8.15, de_core_news_sm 3.8.0,
model baked in at build time. `loginctl enable-linger andrey` is **required** — without it
rootless podman containers die when the last ssh session closes, which is exactly what an
unattended run does. It was `Linger=no` by default here.

---

## 2. Pipeline and data flow

```
de.txt.gz ──prepare.py──> 200 shards ──parse_shard.py──> 3 count tables/shard
                                            (×200, 3 workers)        │
                                                                     ▼
                          wp.db  <──merge_score.py── streaming k-way merge + SQLite join
```

`run_night.py` drives stages 2–3; `launch.sh` starts it detached; `morning.sh` reports.

### prepare.py — sampling and deduplication

Two passes over the corpus were run: `--count-only` (to size the sample) then the real one.

| measurement | value |
|---|---|
| lines surviving cleaning | 80,630,928 |
| **unique** after normalisation | **54,083,133** |
| duplicate rate | **32.9%** |
| words in output | 423,576,358 (7.83/sentence) |
| runtime | 20 min single-threaded |

**Deduplication is a statistics-correctness issue, not tidiness.** OpenSubtitles carries
several subtitle versions of the same film plus heavy line repetition; a third of the
corpus is duplicates, and they inflate logDice for stock phrases specifically — the exact
rows a collocation database is for.

Selection is by **hash of the normalised sentence**, which does sampling and dedup in one
step and bounds memory by the *sample* size rather than the corpus size (a `set` over all
80M survivors would be several GB):

```python
h = blake2b(normalised, digest_size=8)      # normalised = casefold, strip non-alnum
if h % 1_000_000 >= thresh: skip            # uniform sample; duplicates share a hash
if h in seen: skip                          # so a dup is always-in or always-out
```

The recipe's `itertools.islice(f, limit)` reads a **prefix** — the first few hundred films
— skewing era, genre and register. Hash selection is uniform over the whole corpus.

In the end `thresh = 1_000_000` (keep everything): the benchmark showed the full corpus
was parseable in one night, so no subsampling was needed.

**Round-robin sharding** (`sentence i → shard i % 200`) makes every shard an unbiased
sample of the whole corpus, so a partial run is a smaller sample rather than a biased one.
This is what makes the driver's deadline safe.

### parse_shard.py — one shard, one process

Deliberately **not** `nlp.pipe(n_process=N)`: that ships Docs back to a single parent that
does all the counting, so on 4 cores the parent becomes the bottleneck and pickling costs
more than the parse. Independent processes over independent shards scale linearly and
checkpoint for free.

`spacy.load("de_core_news_sm", exclude=["ner"])` — NER is the only component droppable;
tagger, morphologizer (needed for `Case`), parser and lemmatizer are all load-bearing.

Measured: **11,634 tok/s per worker** (the recipe guessed 1–3k), 220 s per 2.57M-token
shard, peak 2.49 GB for all three workers against a 7 GB cap.

---

## 3. Data structures

Three tables per shard, gzipped, **sorted by key**, written `.tmp` → renamed:

| file | key | value |
|---|---|---|
| `<shard>.pairs.tsv.gz` | `relation \t headword \t collocate \t case` | count — f(a,b) |
| `<shard>.hm.tsv.gz` | `relation \t headword` | count — f(a) |
| `<shard>.cm.tsv.gz` | `relation \t collocate` | count — f(b) |
| `<shard>.done` | — | JSON: sentences, tokens, rows, distinct_pairs, seconds, tok/s |

Keys are **tab-joined strings, not tuples**. A single `str` costs far less than a 4-tuple
of `str` at a few million distinct keys per worker, and it makes writing a `write(k + ...)`.
Tab is safe as separator because no lemma can contain one.

Sorted output is what permits `heapq.merge` at the merge stage — bounded memory regardless
of corpus size.

### Two invariants that must not be broken

1. **Nothing is pruned at the shard level.** Obvious optimisation, silently wrong here:
   a collocation occurring 30× corpus-wide appears 1–2× per shard, so a "drop count < 2
   per shard" rule deletes exactly the frequency band the `freq >= 20` floor exists to
   keep. Pruning happens once, at merge, against global counts.
2. **Marginals are never pruned at all.** They are logDice's denominator; pruning them
   biases every score.

### Key ordering subtlety (verified, don't re-derive)

Pair keys sort as `rel \t head \t colloc \t case`. `\t` (0x09) sorts below every printable
character, so `"in"` cannot interleave with `"in wohnen"` — case-collapse groups stay
contiguous during the streaming merge. `merged()` collapses runs of equal keys, so no
duplicate key can ever reach the `UNIQUE` indexes on the marginal tables.

---

## 4. The relation model — EMPIRICAL, not the recipe's table

The recipe's mapping table is flagged in it as unverified. It is **wrong in four ways**,
each found by running `probe_labels.py` / `probe2.py` against the real model. Each
produces well-formed, plausible-looking, worthless rows — nothing raises.

### 4.1 The auxiliary hop

```
Der Mieter hat die Wohnung gemietet.
    Mieter    sb -> hat/AUX        ← NOT 'mieten'
    gemietet  oc -> hat/AUX
```

In every periphrastic tense the subject attaches to the finite auxiliary. Counted
naively this yields *"Mieter ist Subjekt von **haben**"* for a large share of all German
sentences. **Every relation resolves AUX → its `oc` child** (`content_verb()`).

### 4.2 Passive vs. future

`werden` + participle → the `sb` is a *Passivsubjekt* (different relation, different chunk
pattern: "Schrank wird gekauft", not "Schrank kauft"). `werden` + **infinitive** is future
tense and is *not* passive. Distinguished by `VerbForm` on the `oc` child.

### 4.3 Coordination goes through the conjunction

```
Brot und Kaese:   und cd-> Brot,   Kaese cj-> und
```

A bare `cj` rule links *Kaese* to *und*. `first_conjunct()` hops the `cd`. Also: spaCy
splits capitalised nouns between NOUN and PROPN (*Kaese* is PROPN here) and predicative
adjectives between ADJ and ADV, so coordination compares **POS classes**, not tags.

### 4.4 Predicatives hang off the copula

```
Die Wohnung ist teuer.
    Wohnung  sb -> ist/AUX
    teuer    pd -> ist/AUX      and teuer is tagged ADV, not ADJ
```

The described noun must be fetched as the copula's `sb` child, and a `pos_ == "ADJ"` test
drops nearly all predicatives.

### 4.5 The full mapping as implemented

| trigger | forward relation (from dependent) | inverse relation |
|---|---|---|
| `sb`, non-copula, resolved verb | ist Subjekt von | hat Subjekt |
| `sb` under `werden`+Part | ist Passivsubjekt von | hat Passivsubjekt |
| `oa` | ist Akkusativ-Objekt von | hat Akkusativ-Objekt |
| `da`, `og` | ist Dativ-/Genitiv-Objekt von | hat Dativ-/Genitiv-Objekt |
| `ag` (NOUN→NOUN) | ist Genitivattribut von | hat Genitivattribut |
| `nk`, ADJ→NOUN | ist Adjektivattribut von | hat Adjektivattribut |
| `pd` under copula, via its `sb` | ist Prädikativ zu | hat Prädikativ |
| `cj` via `cd` | ist in Koordination mit | *(symmetric — same name)* |
| ADP with `mo`/`op`/`pg`/`mnr` + `nk` child | ist in Präpositionalgruppe | hat Präpositionalgruppe |

Two deliberate suppressions:

- **Copular subjects are dropped.** "Wohnung ist Subjekt von sein" is true of every noun
  in the language. The informative half of a copular clause is the predicative.
- **Possessives are dropped from Adjektivattribut.** spaCy tags *dein/mein/ihr* as ADJ,
  producing "ein(e) deine(r) Wohnung". Filtered by `NOT_ADJECTIVES` + `Poss` morph.

### 4.6 Both directions, and why

`tools/wortprofil.py:RELATION_PATTERNS` renders `ist Akkusativ-Objekt von` as
`"{L}(Akk.) {c}"`. Storing only the recipe's dependent→head direction renders
**"mieten(Akk.) Wohnung"** — garbage. Every inverse name needed already exists in that
map, which is strong evidence the intended model was bidirectional all along.

logDice is symmetric under swapping f(a)/f(b), so both directions carry the same score.
Confirmed empirically: `(Haus, ist Akkusativ-Objekt von, mieten, 8.1, 5)` and
`(mieten, hat Akkusativ-Objekt, Haus, 8.1, 5)`.

Row counts confirm the symmetry held across the whole build — every non-symmetric relation
has exactly equal counts in both directions, and `2 × 2,427,827 + 505,096 = 5,360,750`
matches `rows_written` exactly.

### 4.7 Prepositional groups

The recipe proposes a relation named `in+wohnen`. **`RELATION_PATTERNS` doesn't know that
string**, so the renderer would silently fall back to `"{L} … {c}"`. Instead:

- collocate is a two-word string, `"in wohnen"` / `"in Wohnung"` — the exact shape
  `wortprofil.py:in_b1()` was already written to strip prepositions out of;
- **case rides in its own column**, aggregated *out* of the score.

Case-in-its-own-column matters: `in die Wohnung` (Acc, direction) and `in der Wohnung`
(Dat, location) are one collocation with two meanings. Splitting them into two rows would
halve both frequencies; collapsing them without recording case would lose the distinction
DWDS itself doesn't publish. The dominant case wins the column.

The payoff, from the finished database:

```
Bett  in gehen      Acc  6423    ins Bett gehen
Bett  in liegen     Dat  3811    im Bett liegen
```

---

## 5. Scoring and the merge

```
logDice(a,b) = 14 + log2( 2·f(a,b) / (f(a) + f(b)) )
```

Same statistic DWDS uses, so the guide's §1.3 two-floor reasoning transfers.

**The join runs inside SQLite, not in Python dicts.** This is the single most important
robustness choice in the file. The merge runs at the *end* of a 5-hour unattended job, so
an OOM there costs the whole night. The marginal tables are 4.4M and 6.1M keys; held as
Python dicts that is several GB on an 11 GB box also running grafana, prometheus and a ZFS
ARC. SQLite does the same join on disk with a 256 MB page cache. Slower, and it finishes.

**File lists are derived from `.done` markers, never from globbing each family separately.**
`parse_shard.py` writes pairs → hm → cm → `.done`; a worker killed mid-write leaves a
complete pairs file with no marginals. Independent globs would then either drop those rows
silently (inner join finds nothing) or keep marginals whose pairs are missing — which
inflates f(a)/f(b) against f(a,b) and pushes every logDice for that shard's headwords
silently **down**. `.done` is the only atomic completion signal, so it decides.

`VACUUM` is wrapped in try/except: it is cosmetic, and letting it raise would skip the
final rename and strand a finished database in `wp.db.tmp` while the driver reports
MERGE FAILED.

### Output schema

```sql
CREATE TABLE colloc (
    headword  TEXT, relation TEXT, collocate TEXT,
    logdice   REAL, freq     INTEGER,
    case_     TEXT DEFAULT ''      -- Nom/Acc/Dat/Gen, PP relations only
);
CREATE INDEX idx_head ON colloc(headword);
CREATE INDEX idx_head_rel ON colloc(headword, relation);
CREATE TABLE meta (k TEXT PRIMARY KEY, v TEXT);
```

**Stored unfiltered at `freq >= 3`.** DWDS's `freq >= 20 / logDice >= 3.0` were tuned on
billions of tokens; at 513M they are wrong by an unknown factor in an unknown direction.
Baking them in means re-running the night to change them. `tools/wortprofil_db.py` applies
them at query time, where retuning costs a second.

---

## 6. Unattended-run design

- **Deadline, not shard count.** At `--deadline-hours` the driver stops *launching* shards,
  lets running ones finish, then merges. Round-robin sharding is what makes an early stop
  cost sample size rather than representativeness.
- **One subprocess per shard, not a pool.** A `ProcessPoolExecutor` raises
  `BrokenProcessPool` if a child is OOM-killed and takes down every sibling. A subprocess
  just returns non-zero; the driver logs it and continues. Model load (~3 s) is noise
  against a 220 s shard.
- **Resumable.** Shards with a `.done` marker are skipped. Safe to re-run after a crash,
  a reboot, or a deliberate stop.
- **The log must explain itself the next morning.** Run manifest, 5-minute heartbeat with
  cgroup memory / disk / ETA, and the tail of any failed worker's own log **inlined** — not
  a pointer to a file that may itself be the problem. `run_state.json` mirrors it for
  machine reading. Log is tee'd to `work/logs/` because `podman logs` dies with the
  container.
- `--jobs 3` under `--cpus=3.5`: 300% demand against a 350% cap, leaving a core for the
  host's grafana/prometheus/ZFS. 4 workers would throttle.

---

## 7. Measured results (2026-08-13 run)

| | |
|---|---|
| shards | 200/200, **0 failures** |
| sentences / tokens | 54,083,133 / **513,716,483** |
| triples extracted | 129,731,052 |
| distinct pairs before prune | 47,806,522 |
| **rows written** (freq ≥ 3) | **5,360,750** over 152,551 headwords |
| marginals | 4,417,997 headword keys, 6,050,912 collocate keys |
| parse phase | 5.10 h (3 workers) |
| merge phase | **7 min** (I had budgeted 30–45) |
| total | 5.22 h |
| peak memory | 2.49 GB / 7 GB cap |
| database | 1.46 GB |

Rows per relation (both directions shown separately):

| rows | relation |
|---:|---|
| 785,516 ×2 | in Präpositionalgruppe |
| 596,629 ×2 | Akkusativ-Objekt |
| 505,096 | in Koordination mit *(symmetric)* |
| 421,010 ×2 | Subjekt |
| 353,276 ×2 | Adjektivattribut |
| 114,919 ×2 | Genitivattribut |
| 97,314 ×2 | Prädikativ |
| 36,979 ×2 | Dativ-/Genitiv-Objekt |
| 22,184 ×2 | Passivsubjekt |

---

## 8. Known noise, and where it comes from

- **`de_core_news_sm` lemma errors.** *Tasse* → *Tas* in the measure-noun frame *eine
  Tasse Kaffee*. Aggregation buried it — 0 rows for `Tas` in the final database — but it
  is the first suspect if a headword looks mangled.
- **Imperatives become capitalised pseudo-nouns.** *Geh ins Bett!* yields a headword
  `Geh`. The B1 intersection removes these at query time.
- **Proper nouns are kept**, so character names appear. Same mitigation.
- **Register skew.** Film dialogue is crime- and drama-heavy: `Wohnung durchsuchen`
  (dice 9.7, f=761) outranks `Wohnung mieten` (9.4, f=519). This is a property of the
  corpus, not a bug, and it is still far closer to domestic/spoken German than DWDS's
  newspaper corpora. Worth stating to the user rather than silently filtering.
- **No multi-word-expression handling.** DWDS has it; this doesn't.

## 9. If rebuilding or extending

- Changing `extract.py` invalidates existing counts — **delete `work/counts/*` entirely**
  rather than mixing rule sets across shards.
- Changing only `MIN_PAIR` or the scoring needs **no re-parse**: re-run `merge_score.py`
  against the existing counts (minutes).
- `test_extract.py` is the gate — 21 assertions, including forbidden rows that encode the
  four recipe errors above. It renders through the real `RELATION_PATTERNS`, so a reversed
  row fails there instead of surfacing in a text weeks later. Run it in the container after
  any `extract.py` change.
- If accuracy ever matters more than speed, `de_core_news_lg` is ~3× slower — which this
  box can afford, since the whole corpus took 5 h with `sm`. The label mapping above is
  TIGER-scheme and would **not** transfer to a UD-trained model.
- DWDS's own implementation (GPL-3.0, github.com/zentrum-lexikographie/wordprofile) is
  production-grade and handles MWEs, but needs MariaDB, expects gzipped CoNLL-U input, and
  uses UD-trained ZDL models — so the empirical label work above would have to be redone
  against UD labels, not reused.

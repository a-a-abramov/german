#!/usr/bin/env python3
"""
vocab.py — the vocabulary ledger for this repo.

WHY THIS EXISTS: bookkeeping and instructions used to live in the same markdown files
(`topics.md` carried 204 hand-sliced word lists, `glue-pool.md` carried 326 checkboxes,
every batch carried a `wordlist.md`). Tracking state inside prose meant the writing
agent had to read — and rewrite — thousands of lines of ledger just to write eight
dialogues, and it nudged the texts toward whatever slice the list happened to hold.

So the ledger moved here: one SQLite file, `groundwork/vocab.db`, holding

    words   every B1 word: its batch (topic), its CSV forms, gloss, frequency band
    uses    which text of which batch used a word  (= coverage)
    skips   words deliberately left out, with a reason  (90-95% coverage is a pass)
    cards   which words have been carded into Anki

and the prose files went back to being prose.

USAGE

    python3 tools/vocab.py init --force              # rebuild the DB from assignments.tsv
    python3 tools/vocab.py status                    # corpus-wide coverage
    python3 tools/vocab.py words --batch 2           # the batch's word list, with status
    python3 tools/vocab.py words --batch 2 --open    # only what is still uncovered
    python3 tools/vocab.py glue --open --group Frage # still-missing question words
    python3 tools/vocab.py scan batch-02-*/texts.md --batch 2          # dry run
    python3 tools/vocab.py scan batch-02-*/texts.md --batch 2 --apply  # record coverage
    python3 tools/vocab.py use   --batch 2 --text 3 "die Grippe"       # manual override
    python3 tools/vocab.py skip  --batch 2 "das Asyl" --reason "no natural home"
    python3 tools/vocab.py card  --batch 2 --all                       # after carding
    python3 tools/vocab.py find Grippe                                 # look one word up

SCAN IS ADVISORY. German morphology is matched by folded stems plus the principal
parts printed in the CSV — good enough to save the writer a manual tally, not a
lemmatizer. Read the `missing` list; fix false negatives with `use`, false positives
with `unuse`. Nothing here is authoritative except what you confirm.
"""

import argparse
import csv
import os
import re
import sqlite3
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(ROOT, "groundwork", "vocab.db")
CSV_PATH = os.path.join(ROOT, "goethe-b1-wortliste.csv")
SEED = os.path.join(ROOT, "groundwork", "assignments.tsv")

SCHEMA = """
CREATE TABLE words (
    id       INTEGER PRIMARY KEY,
    lemma    TEXT NOT NULL,            -- headword as the plan writes it
    kind     TEXT NOT NULL,            -- 'target' (scened) | 'glue' (pooled)
    batch    INTEGER,                  -- target: topic-batch number; glue: NULL
    topic    TEXT NOT NULL,            -- target: topic name; glue: functional group
    forms    TEXT,                     -- exact col-1 string of the Goethe CSV
    gloss    TEXT,                     -- short English gloss (filled while writing)
    band     INTEGER,                  -- DWDS frequency band 0-6, higher = commoner
    region   TEXT,                     -- CSV region tag: NULL/'D…' = standard German,
                                       -- 'A'/'CH'/'A, CH' = out of scope (see is_standard)
    note     TEXT,
    UNIQUE(lemma, kind, batch)
);
CREATE TABLE uses (
    word_id  INTEGER NOT NULL REFERENCES words(id),
    batch    INTEGER NOT NULL,         -- batch whose texts.md used it
    text_no  INTEGER,
    title    TEXT,
    surface  TEXT,                     -- the form it actually appeared in
    source   TEXT NOT NULL DEFAULT 'scan',   -- 'scan' (re-derivable) | 'manual' (kept)
    PRIMARY KEY (word_id, batch, text_no)
);
CREATE TABLE skips (
    word_id  INTEGER PRIMARY KEY REFERENCES words(id),
    reason   TEXT
);
CREATE TABLE cards (
    word_id  INTEGER PRIMARY KEY REFERENCES words(id),
    text_no  INTEGER
);
CREATE INDEX words_batch ON words(batch);
CREATE INDEX uses_word ON uses(word_id);
"""

# ---------------------------------------------------------------- normalisation

FOLD = str.maketrans({"ä": "a", "ö": "o", "ü": "u", "Ä": "a", "Ö": "o", "Ü": "u", "ß": "ss"})
# endings a German inflection may add to a stem; used only for stems of 4+ chars
INFL = {"", "e", "en", "er", "es", "em", "n", "s", "st", "t", "te", "ten", "et", "ern", "nen", "ne"}
ARTICLES = ("der ", "die ", "das ", "dasder ", "der/das ")
AUX = {"ist", "hat", "sich", "sein", "haben", "werden", "etwas", "jemanden", "jemandem"}
SEPARABLE = ("ab", "an", "auf", "aus", "bei", "ein", "fest", "her", "hin", "los", "mit",
             "nach", "raus", "rein", "runter", "statt", "teil", "um", "vor", "weg", "zu",
             "zurück", "zusammen")


def fold(s):
    return unicodedata.normalize("NFC", s).lower().translate(FOLD)


def csv_head(head):
    """'der Abfall, ¨-e' -> 'der Abfall'; 'abbiegen, biegt ab, …' -> 'abbiegen'.

    The CSV prints the headword and its forms in one cell: forms after a comma,
    masculine/feminine pairs on separate lines, cross-references on a `→` line.
    """
    segs = []
    for line in re.split(r"[\n]| / ", head):
        line = line.strip()
        if not line or line.startswith("→"):
            continue
        segs.append(line.split(",")[0].strip())
    return " / ".join(segs)


def bare(lemma):
    """Strip article, reflexive, regional tags and forms — leave the headword itself."""
    s = lemma.strip()
    s = re.sub(r"\s*\((D|A|CH)(,\s*(D|A|CH))*\)\s*", " ", s)
    s = re.sub(r"\s*\(Pl\.\)\s*", " ", s)
    s = re.sub(r"^\((sich|ein)\)\s*", "", s)
    s = re.sub(r"^sich\s+", "", s)
    for a in ARTICLES:
        if s.lower().startswith(a):
            s = s[len(a):]
            break
    # source typos glue the article to the noun: 'derOfen', 'das/derObers'
    s = re.sub(r"^(der|die|das)(/(der|die|das))*(?=[A-ZÄÖÜ])", "", s)
    return s.strip()


REGION_RE = re.compile(r"\((D|A|CH)(?:,\s*(?:D|A|CH))*\)")


def region_of(head):
    """The CSV's region tag for a headword: 'D, A', 'CH', … or None when it carries none."""
    if not head:
        return None
    # drop the "→ D, A: Hausmeister" cross-reference lines, keep every headword line:
    # masc/fem pairs carry the tag on the second one ("die Abwartin, -nen (CH)")
    body = "\n".join(l for l in head.split("\n") if not l.strip().startswith("→"))
    m = REGION_RE.search(body)
    return m.group(0).strip("()") if m else None


def is_standard(region):
    """
    Is this entry standard German usage?

    The Goethe list tags the regional doublets: `die Treppe, -n (D, CH) → A: Stiege` and
    `die Stiege, -n (A) → D, CH: Treppe` are the same rung of the same staircase. This
    corpus teaches the D side only, so an entry counts when its tag names D — or when it
    carries no tag at all, which is the list's way of saying "used everywhere".
    """
    return region is None or "D" in region


def is_noun(s):
    """German nouns carry an article or a capital — enough to tell `der Arm` from `arm`."""
    return s.strip().lower().startswith(("der ", "die ", "das ", "der/", "das/")) or bare(s)[:1].isupper()


def norm_key(lemma):
    """The primary key a headword is matched on: folded letters only, article kept."""
    return sorted(norm_keys(lemma))[0]


def norm_keys(lemma):
    """
    All keys a headword may legitimately be matched on.

    The two sides spell the same word differently often enough that one key is not
    enough: the plan writes `der Ofen`, the CSV writes `der (Back-)Ofen, ¨- (D, CH)`;
    the plan writes `das Hendl`, the CSV writes `das Hend(e)l, - (A)`. So optional
    parentheses are expanded both ways, qualifier parentheses (`(nur Pl.)`,
    `(siehe auch viel)`) are dropped, and everything but letters is stripped.
    """
    s = csv_head(bare(lemma))
    s = re.sub(r"\s*→.*$", "", s)
    s = re.sub(r"\((?=[^)]*[ .])[^)]*\)", " ", s)      # qualifier parens: drop entirely
    forms = {s}
    while True:
        grown = set()
        for f in forms:
            m = re.search(r"\(([^)]*)\)", f)
            if m:
                grown.add(f[: m.start()] + m.group(1) + f[m.end():])
                grown.add(f[: m.start()] + f[m.end():])
        if not grown - forms:
            break
        forms |= grown
    out = set()
    for f in forms:
        for variant in re.split(r"\s*/\s*", f):
            k = re.sub(r"[^a-zäöüß]", "", fold(variant))
            if k:
                out.add(k)
    return out or {fold(lemma)}


ARTICLE_KEYS = ("der", "die", "das")


def short_key(key):
    """The same key with a glued-on article removed: 'derofen' -> 'ofen'."""
    for a in ARTICLE_KEYS:
        if key.startswith(a) and len(key) > len(a) + 2:
            return key[len(a):]
    return key


def variants(lemma):
    """Surface spellings a word may legitimately appear as, from the headword alone."""
    out = []
    s = bare(lemma)
    s = re.sub(r"\s*→.*$", "", s)
    for part in re.split(r"\s*/\s*", s):
        part = bare(part.strip())   # each variant carries its own article: "der X / die Xin"
        if not part:
            continue
        # (herunter-)fahren -> herunterfahren + fahren ; (ein) paar -> ein paar + paar
        m = re.match(r"^\((.+?)\)\s*(.+)$", part)
        if m:
            head, rest = m.group(1), m.group(2)
            joiner = "" if head.endswith("-") else " "
            out.append(head.rstrip("-") + joiner + rest)
            out.append(rest)
        else:
            out.append(part)
    # a separable verb usually stands apart in a main clause ("machen Sie das Licht aus"),
    # so add a two-part form the utterance matcher can find at any distance
    for v in list(out):
        for pre in SEPARABLE:
            if v.startswith(pre) and len(v) > len(pre) + 3 and v.endswith(("en", "ern", "eln")):
                out.append(f"{v[len(pre):]} {pre}")
                break
    return [v.strip() for v in out if v.strip()]


def csv_forms(forms):
    """Extra surface forms printed in the CSV headword column (verb principal parts)."""
    if not forms:
        return []
    out = []
    for piece in forms.split(","):
        piece = piece.strip()
        if not piece or piece.startswith("→") or "→" in piece:
            continue
        piece = re.sub(r"\s*\((D|A|CH)(,\s*(D|A|CH))*\)\s*", " ", piece).strip()
        if not piece or piece.startswith("-") or piece.startswith("¨") or piece == "-":
            continue          # plural markers: covered by stem matching
        if re.search(r"[A-Za-zÄÖÜäöüß]{2,}", piece):
            out.append(piece)
    return out[1:] if len(out) > 1 else []   # [0] is the headword itself


def token_matches(token, part, loose=False):
    """Does one text token realise one part of a headword?"""
    t, p = fold(token), fold(part)
    if p.endswith("-"):                       # 'dies-', 'heraus-' : prefix entries
        p = p[:-1]
        if not t.startswith(p):
            return False
        rest = t[len(p):]
        return rest in INFL or (len(p) >= 5 and len(rest) >= 3)
    if p.startswith("-"):                     # '-weise' : suffix entries
        return t.endswith(p[1:])
    if t == p:
        return True
    if len(p) < 4 and not loose:
        return False                          # short function words: exact only
    bases = {p}
    for suf in ("en", "n", "e", "ten", "te", "st", "et", "t"):
        if p.endswith(suf) and len(p) - len(suf) >= 4:
            bases.add(p[: -len(suf)])
    return any(t.startswith(b) and t[len(b):] in INFL for b in bases)


def phrase_matches(tokens, phrase):
    """Every content token of a (possibly multi-word) form appears in this utterance."""
    parts = [p for p in re.split(r"[\s…]+", phrase) if p and p not in ("...", "…")]
    parts = [p for p in parts if fold(p) not in AUX] or parts
    if not parts:
        return None
    hits = []
    for p in parts:
        # German capitalises nouns, so a capitalised part may only match a capitalised
        # token — this alone keeps `der Schlaf` from matching "schläfst".
        cands = [t for t in tokens if not p[:1].isupper() or t[:1].isupper()]
        m = next((t for t in cands if token_matches(t, p)), None)
        if m is None:
            return None
        hits.append(m)
    return max(hits, key=len)


# ---------------------------------------------------------------- source parsing

def read_csv_rows():
    rows = []
    with open(CSV_PATH, encoding="utf-8") as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0 or not row or not row[0].strip():
                continue
            rows.append((row[0].strip(), row[1] if len(row) > 1 else ""))
    return rows





def read_seed():
    """
    The checked-in, diffable copy of every word's topic assignment.

    `init` prefers this over re-parsing the prose files: once `topics.md` stops carrying
    word lists, this TSV — not the binary DB — is the plain-text record of which word
    belongs to which batch.
    """
    out = []
    with open(SEED, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            cells = (line.rstrip("\n").split("\t") + ["", ""])[:6]
            lemma, kind, batch, topic, gloss, note = cells
            out.append((lemma, kind, int(batch) if batch else None, topic,
                        gloss or None, note or None))
    return out


def cmd_export(args):
    """Write the assignment seed back out — run after any change to words."""
    con = connect()
    rows = con.execute("SELECT lemma, kind, batch, topic, gloss, note FROM words"
                       " ORDER BY kind DESC, batch, lemma COLLATE NOCASE")
    with open(SEED, "w", encoding="utf-8") as f:
        f.write("# lemma\tkind\tbatch\ttopic\tgloss\tnote"
                "  — the plain-text seed `vocab.py init` reads; regenerate with `vocab.py export`\n")
        n = 0
        for r in rows:
            f.write("\t".join([r["lemma"], r["kind"], str(r["batch"] or ""), r["topic"],
                                (r["gloss"] or "").replace("\t", " "),
                                (r["note"] or "").replace("\t", " ")]).rstrip("\t") + "\n")
            n += 1
    print(f"{SEED}: {n} words")


def load_bands():
    try:
        sys.path.insert(0, HERE)
        import wordfreq
        return wordfreq.load_bands()
    except Exception as e:                       # noqa: BLE001 - bands are a nicety
        sys.stderr.write(f"note: frequency bands unavailable ({e})\n")
        return {}


# ---------------------------------------------------------------- commands

def connect(create=False):
    if not create and not os.path.isfile(DB):
        sys.exit(f"no database at {DB} — run: python3 tools/vocab.py init")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con


def carry_over():
    """
    What a rebuild must NOT lose.

    Coverage is re-derivable (rescan the texts) and assignments come from the seed, but
    a `skip` reason, a hand-confirmed `use` and a card record exist nowhere else — and a
    gloss or note written since the last `export` is newer than the seed's copy.
    """
    if not os.path.isfile(DB):
        return {}, {}, [], {}
    con = connect()
    key = "w.lemma, w.kind, w.batch"
    written = {(r[0], r[1], r[2]): (r[3], r[4]) for r in con.execute(
        f"SELECT {key}, w.gloss, w.note FROM words w WHERE w.gloss IS NOT NULL OR w.note IS NOT NULL")}
    skips = {(r[0], r[1], r[2]): r[3] for r in con.execute(
        f"SELECT {key}, s.reason FROM skips s JOIN words w ON w.id=s.word_id")}
    cards = {(r[0], r[1], r[2]): r[3] for r in con.execute(
        f"SELECT {key}, c.text_no FROM cards c JOIN words w ON w.id=c.word_id")}
    manual = [tuple(r) for r in con.execute(
        f"SELECT {key}, u.batch, u.text_no, u.title, u.surface FROM uses u"
        " JOIN words w ON w.id=u.word_id WHERE u.source='manual'")]
    con.close()
    return skips, cards, manual, written


def restore(con, skips, cards, manual, written):
    def wid(lemma, kind, batch):
        r = con.execute("SELECT id FROM words WHERE lemma=? AND kind=? AND batch IS ?",
                        (lemma, kind, batch)).fetchone()
        return r["id"] if r else None
    for (lemma, kind, batch), reason in skips.items():
        if (i := wid(lemma, kind, batch)):
            con.execute("INSERT OR REPLACE INTO skips VALUES (?,?)", (i, reason))
    for (lemma, kind, batch), text_no in cards.items():
        if (i := wid(lemma, kind, batch)):
            con.execute("INSERT OR REPLACE INTO cards VALUES (?,?)", (i, text_no))
    for lemma, kind, batch, ubatch, text_no, title, surface in manual:
        if (i := wid(lemma, kind, batch)):
            con.execute("INSERT OR REPLACE INTO uses VALUES (?,?,?,?,?,'manual')",
                        (i, ubatch, text_no, title, surface))
    for (lemma, kind, batch), (gloss, note) in written.items():
        if (i := wid(lemma, kind, batch)):
            con.execute("UPDATE words SET gloss=COALESCE(?, gloss), note=COALESCE(?, note)"
                        " WHERE id=?", (gloss, note, i))
    con.commit()
    return len(skips), len(cards), len(manual), len(written)


def cmd_init(args):
    if os.path.isfile(DB) and not args.force:
        sys.exit(f"{DB} exists — pass --force to rebuild (coverage is re-derived, not kept)")
    kept = carry_over()
    if os.path.isfile(DB):
        os.remove(DB)
    con = connect(create=True)
    con.executescript(SCHEMA)

    rows = read_csv_rows()
    by_key = {}
    for head, _ex in rows:
        for k in norm_keys(head):
            by_key.setdefault(k, []).append(head)

    bands = load_bands()
    unmatched = []

    def lookup(lemma, table):
        ks = list(norm_keys(lemma))
        hit = next((table[k] for k in ks if k in table), None)
        if hit is None:                   # fall back on source typos: 'derOfen'
            hit = next((table[short_key(k)] for k in ks if short_key(k) in table), None)
        if not isinstance(hit, list):
            return hit
        # `der Arm` and `arm` share a key; keep the one whose part of speech matches
        return next((h for h in hit if is_noun(h) == is_noun(lemma)), hit[0])

    def insert(lemma, kind, batch, topic, gloss=None, note=None):
        forms = lookup(lemma, by_key)
        if forms is None:
            unmatched.append(lemma)
        band = None
        for v in variants(lemma):
            band = bands.get(bare(v).strip("-"))
            if band is not None:
                break
        con.execute(
            "INSERT OR IGNORE INTO words (lemma, kind, batch, topic, forms, gloss, band,"
            " region, note) VALUES (?,?,?,?,?,?,?,?,?)",
            (lemma, kind, batch, topic, forms, gloss, band, region_of(forms), note),
        )

    if not os.path.isfile(SEED):
        sys.exit(f"missing {SEED} — the assignment seed is the plain-text master copy.\n"
                 "Recover it from git (`git checkout groundwork/assignments.tsv`) or, for a\n"
                 "one-off rebuild from the retired prose lists, from an older revision of\n"
                 "topics.md + glue-pool.md.")
    src = f"seed {os.path.relpath(SEED, ROOT)}"
    for lemma, kind, batch, topic, gloss, note in read_seed():
        insert(lemma, kind, batch, topic, gloss, note)
    con.commit()

    # Coverage is re-derived from the finished texts themselves, never carried over from
    # the old checkbox ticks: a tick on a sentence that was later rewritten is a word
    # silently marked covered that no text actually contains.
    seeded = []
    for d in sorted(os.listdir(ROOT)):
        m = re.match(r"^batch-(\d+)-", d)
        path = os.path.join(ROOT, d, "texts.md")
        if not m or not os.path.isfile(path):
            continue
        batch = int(m.group(1))
        _texts, _pool, found = scan_file(con, path, batch)
        record(con, found, batch)
        seeded.append(f"batch {batch}: {len(found)}")

    n_t = con.execute("SELECT COUNT(*) c FROM words WHERE kind='target'").fetchone()["c"]
    n_g = con.execute("SELECT COUNT(*) c FROM words WHERE kind='glue'").fetchone()["c"]
    n_b = con.execute("SELECT COUNT(*) c FROM words WHERE band IS NOT NULL").fetchone()["c"]
    n_gl = con.execute("SELECT COUNT(*) c FROM words WHERE gloss IS NOT NULL").fetchone()["c"]
    n_batches = con.execute("SELECT COUNT(DISTINCT batch) c FROM words WHERE kind='target'").fetchone()["c"]
    print(f"{DB}  (from {src})\n  {n_t} target words in {n_batches} batches, {n_g} glue words")
    print(f"  {n_b} with a frequency band, {n_gl} with a gloss")
    print("  coverage re-derived from existing texts — " + ("; ".join(seeded) or "no texts.md yet"))
    n_s, n_c, n_m, n_w = restore(con, *kept)
    if n_s or n_c or n_m or n_w:
        print(f"  carried over {n_s} skips, {n_c} card records, {n_m} manual coverage marks,"
              f" {n_w} glosses/notes")
    if unmatched:
        print(f"  !! {len(unmatched)} headwords with no CSV match: {', '.join(unmatched[:12])}"
              + (" …" if len(unmatched) > 12 else ""))


def status_of(con, row):
    if con.execute("SELECT 1 FROM skips WHERE word_id=?", (row["id"],)).fetchone():
        return "skip"
    u = con.execute("SELECT batch, text_no FROM uses WHERE word_id=? ORDER BY batch, text_no",
                    (row["id"],)).fetchall()
    if not u:
        return "open"
    return ",".join(f"{r['batch']}.{r['text_no']}" for r in u)


REGIONAL_SQL = " AND (region IS NULL OR region LIKE '%D%')"


def select_words(con, args):
    q = "SELECT * FROM words WHERE 1=1"
    p = []
    if not getattr(args, "regional", False):
        q += REGIONAL_SQL
    if getattr(args, "batch", None):
        q += " AND kind='target' AND batch=?"
        p.append(args.batch)
    elif getattr(args, "glue_only", False):
        q += " AND kind='glue'"
    if getattr(args, "group", None):
        q += " AND topic LIKE ?"
        p.append(f"%{args.group}%")
    q += " ORDER BY band IS NULL, band DESC, lemma COLLATE NOCASE"
    out = []
    for r in con.execute(q, p):
        st = status_of(con, r)
        if getattr(args, "open", False) and st != "open":
            continue
        if getattr(args, "used", False) and st in ("open", "skip"):
            continue
        out.append((r, st))
    return out


def flat(s):
    """CSV form strings carry newlines (masc/fem pairs) — never let them break a row."""
    return re.sub(r"\s*\n\s*", " · ", (s or "").strip())


def render(rows, fmt):
    if fmt == "list":
        print(" · ".join(r["lemma"] for r, _ in rows))
        return
    if fmt == "tsv":
        for r, st in rows:
            print("\t".join([r["lemma"], flat(r["forms"]), r["gloss"] or "",
                             str(r["band"] if r["band"] is not None else ""), st]))
        return
    print("| word | forms | gloss | band | used in |")
    print("|---|---|---|---:|---|")
    for r, st in rows:
        print(f"| {r['lemma']} | {flat(r['forms'])} | {r['gloss'] or ''} | "
              f"{r['band'] if r['band'] is not None else ''} | {st} |")


def cmd_words(args):
    con = connect()
    rows = select_words(con, args)
    render(rows, args.format)
    print(f"\n_{len(rows)} words shown._", file=sys.stderr)


def cmd_glue(args):
    args.glue_only = True
    args.batch = None
    con = connect()
    rows = select_words(con, args)
    if args.format == "md" and not args.group:
        by_group = {}
        for r, st in rows:
            by_group.setdefault(r["topic"], []).append((r, st))
        for g, rs in by_group.items():
            print(f"\n### {g} ({len(rs)})")
            print(" · ".join(r["lemma"] for r, _ in rs))
        return
    render(rows, "list" if args.format == "md" else args.format)


def parse_texts(path):
    """[(text_no, title, [utterance, ...]), ...] from a batch texts.md."""
    texts, cur = [], None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^##\s+Text\s+(\d+)\s*[—–-]\s*(.+)$", line.strip())
        if m:
            cur = (int(m.group(1)), m.group(2).strip(), [])
            texts.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^[A-Z]:\s+(.*)$", line.strip())
        if m:
            cur[2].append(m.group(1))
    return texts


def scan_file(con, path, batch):
    """(texts, pool, found) — which of the batch's targets and which glue words appear."""
    texts = parse_texts(path)
    pool = list(con.execute(
        "SELECT * FROM words WHERE (kind='glue' OR (kind='target' AND batch=?))"
        + REGIONAL_SQL, (batch,)))
    keys = {}
    for r in pool:
        forms = variants(r["lemma"]) + csv_forms(r["forms"])
        keys[r["id"]] = (r, list(dict.fromkeys(forms)))

    found = {}          # word_id -> (text_no, title, surface)
    for no, title, utterances in texts:
        toks = [re.findall(r"[A-Za-zÄÖÜäöüß-]+", u) for u in utterances]
        for wid, (r, forms) in keys.items():
            if wid in found:
                continue
            for tokens in toks:
                hit = next((h for f in forms if (h := phrase_matches(tokens, f))), None)
                if hit:
                    found[wid] = (no, title, hit)
                    break
    return texts, pool, found


def record(con, found, batch):
    for wid, (no, title, surface) in found.items():
        con.execute("INSERT OR REPLACE INTO uses (word_id, batch, text_no, title, surface, source)"
                    " VALUES (?,?,?,?,?,'scan')", (wid, batch, no, title, surface))
    con.commit()


def cmd_scan(args):
    con = connect()
    texts, pool, found = scan_file(con, args.file, args.batch)
    if not texts:
        sys.exit(f"no '## Text N — Title' sections found in {args.file}")

    tgt = [r for r in pool if r["kind"] == "target"]
    glue = [r for r in pool if r["kind"] == "glue"]
    tgt_hit = [r for r in tgt if r["id"] in found]
    glue_hit = [r for r in glue if r["id"] in found]
    missing = [r for r in tgt if r["id"] not in found]

    print(f"{args.file}: {len(texts)} texts")
    pct = 100.0 * len(tgt_hit) / max(len(tgt), 1)
    print(f"  batch {args.batch} targets: {len(tgt_hit)}/{len(tgt)} ({pct:.0f}%)")
    print(f"  glue words seen in this file: {len(glue_hit)}")
    if missing:
        print(f"  missing ({len(missing)}): " + ", ".join(r["lemma"] for r in missing))
    if args.verbose:
        for no, title, _ in texts:
            hits = [f"{r['lemma']}→{found[r['id']][2]}" for r in tgt if found.get(r["id"], (None,))[0] == no]
            print(f"  Text {no} — {title}: {len(hits)} targets\n    " + ", ".join(hits))

    if args.apply:
        # recompute, don't increment — but never drop a hit the writer confirmed by hand
        con.execute("DELETE FROM uses WHERE batch=? AND source='scan'", (args.batch,))
        record(con, found, args.batch)
        print(f"  recorded {len(found)} uses in {DB}")
    else:
        print("  (dry run — pass --apply to record)")


def resolve(con, lemma, batch=None):
    q = "SELECT * FROM words WHERE lemma=? OR lemma LIKE ?"
    rows = list(con.execute(q, (lemma, f"%{lemma}%")))
    if batch:
        pref = [r for r in rows if r["batch"] == batch or r["kind"] == "glue"]
        rows = pref or rows
    exact = [r for r in rows if bare(r["lemma"]).lower() == bare(lemma).lower()]
    return (exact or rows)[0] if (exact or rows) else None


def cmd_use(args):
    con = connect()
    for lemma in args.words:
        r = resolve(con, lemma, args.batch)
        if not r:
            print(f"  ?? unknown word: {lemma}")
            continue
        con.execute("INSERT OR REPLACE INTO uses (word_id, batch, text_no, title, surface, source)"
                    " VALUES (?,?,?,?,?,'manual')", (r["id"], args.batch, args.text, None, None))
        con.execute("DELETE FROM skips WHERE word_id=?", (r["id"],))
        print(f"  used: {r['lemma']} → batch {args.batch}, text {args.text}")
    con.commit()


def cmd_unuse(args):
    con = connect()
    for lemma in args.words:
        r = resolve(con, lemma, args.batch)
        if r:
            con.execute("DELETE FROM uses WHERE word_id=? AND batch=?", (r["id"], args.batch))
            print(f"  cleared: {r['lemma']}")
    con.commit()


def cmd_skip(args):
    con = connect()
    for lemma in args.words:
        r = resolve(con, lemma, args.batch)
        if not r:
            print(f"  ?? unknown word: {lemma}")
            continue
        con.execute("INSERT OR REPLACE INTO skips (word_id, reason) VALUES (?,?)",
                    (r["id"], args.reason))
        print(f"  skipped: {r['lemma']} ({args.reason})")
    con.commit()


def cmd_unskip(args):
    con = connect()
    for lemma in args.words:
        r = resolve(con, lemma, args.batch)
        if r:
            con.execute("DELETE FROM skips WHERE word_id=?", (r["id"],))
            print(f"  back in play: {r['lemma']}")
    con.commit()


def cmd_card(args):
    con = connect()
    if args.all:
        rows = con.execute(
            "SELECT w.id, w.lemma FROM words w JOIN uses u ON u.word_id=w.id"
            " WHERE w.kind='target' AND w.batch=?", (args.batch,)).fetchall()
    else:
        rows = [r for r in (resolve(con, w, args.batch) for w in args.words) if r]
    for r in rows:
        con.execute("INSERT OR REPLACE INTO cards (word_id, text_no) VALUES (?, NULL)", (r["id"],))
    con.commit()
    print(f"  carded {len(rows)} words in batch {args.batch}")


def cmd_gloss(args):
    con = connect()
    r = resolve(con, args.word, args.batch)
    if not r:
        sys.exit(f"unknown word: {args.word}")
    con.execute("UPDATE words SET gloss=? WHERE id=?", (args.gloss, r["id"]))
    con.commit()
    print(f"  {r['lemma']}: {args.gloss}")
    cmd_export(args)


def cmd_note(args):
    con = connect()
    r = resolve(con, args.word, args.batch)
    if not r:
        sys.exit(f"unknown word: {args.word}")
    con.execute("UPDATE words SET note=? WHERE id=?", (args.note, r["id"]))
    con.commit()
    print(f"  {r['lemma']}: {args.note}")
    cmd_export(args)


def cmd_find(args):
    con = connect()
    rows = list(con.execute("SELECT * FROM words WHERE lemma LIKE ?", (f"%{args.word}%",)))
    if not rows:
        print("no match")
        return
    for r in rows:
        where = f"batch {r['batch']}" if r["kind"] == "target" else f"glue · {r['topic']}"
        if not is_standard(r["region"]):
            where += f" · REGIONAL ({r['region']}) — out of scope, write the D form"
        print(f"{r['lemma']}  [{where}]  {r['forms'] or '—'}\n  gloss: {r['gloss'] or '—'}"
              f"  band: {r['band'] if r['band'] is not None else '—'}  status: {status_of(con, r)}")
        if r["note"]:
            print(f"  note: {r['note']}")


def cmd_status(args):
    con = connect()
    print("batch  topic                              words  covered   %")
    q = ("SELECT batch, topic, COUNT(*) n,"
         " SUM(EXISTS(SELECT 1 FROM uses WHERE uses.word_id=words.id)) c,"
         " SUM(EXISTS(SELECT 1 FROM skips WHERE skips.word_id=words.id)) s"
         " FROM words WHERE kind='target'" + REGIONAL_SQL
         + (" AND batch=?" if args.batch else "") +
         " GROUP BY batch ORDER BY batch")
    tot = cov = 0
    for r in con.execute(q, (args.batch,) if args.batch else ()):
        pct = 100.0 * r["c"] / max(r["n"], 1)
        tot += r["n"]
        cov += r["c"]
        skipped = f"  ({r['s']} skipped)" if r["s"] else ""
        print(f"{r['batch']:>5}  {r['topic'][:34]:<34} {r['n']:>5}  {r['c']:>7}  {pct:>3.0f}%{skipped}")
    print(f"{'':>5}  {'TOTAL targets':<34} {tot:>5}  {cov:>7}  {100.0*cov/max(tot,1):>3.0f}%")
    g = con.execute("SELECT COUNT(*) n,"
                    " SUM(EXISTS(SELECT 1 FROM uses WHERE uses.word_id=words.id)) c"
                    " FROM words WHERE kind='glue'" + REGIONAL_SQL).fetchone()
    print(f"{'':>5}  {'glue pool':<34} {g['n']:>5}  {g['c']:>7}  {100.0*g['c']/max(g['n'],1):>3.0f}%")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="build groundwork/vocab.db from groundwork/assignments.tsv")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("words", help="a batch's target words with coverage status")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--open", action="store_true", help="only words not yet used or skipped")
    p.add_argument("--used", action="store_true", help="only words already used")
    p.add_argument("--format", choices=["md", "tsv", "list"], default="md")
    p.add_argument("--regional", action="store_true",
                   help="also show A/CH-only entries, which are out of scope by default")
    p.set_defaults(fn=cmd_words)

    p = sub.add_parser("glue", help="the shared function-word pool")
    p.add_argument("--open", action="store_true")
    p.add_argument("--used", action="store_true")
    p.add_argument("--group", help="filter by functional group, e.g. Frage, Konjunk, Modal")
    p.add_argument("--format", choices=["md", "tsv", "list"], default="md")
    p.add_argument("--regional", action="store_true")
    p.set_defaults(fn=cmd_glue)

    p = sub.add_parser("scan", help="match a texts.md against the ledger")
    p.add_argument("file")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--apply", action="store_true", help="record the hits as coverage")
    p.add_argument("--verbose", "-v", action="store_true", help="per-text hit list")
    p.set_defaults(fn=cmd_scan)

    p = sub.add_parser("use", help="mark words as covered by hand")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--text", type=int, default=0)
    p.add_argument("words", nargs="+")
    p.set_defaults(fn=cmd_use)

    p = sub.add_parser("unuse", help="undo a coverage record")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("words", nargs="+")
    p.set_defaults(fn=cmd_unuse)

    p = sub.add_parser("skip", help="deliberately leave words out, with a reason")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--reason", required=True)
    p.add_argument("words", nargs="+")
    p.set_defaults(fn=cmd_skip)

    p = sub.add_parser("unskip", help="put a skipped word back in play")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("words", nargs="+")
    p.set_defaults(fn=cmd_unskip)

    p = sub.add_parser("card", help="record that words have been carded into Anki")
    p.add_argument("--batch", type=int, required=True)
    p.add_argument("--all", action="store_true", help="every covered target word of the batch")
    p.add_argument("words", nargs="*")
    p.set_defaults(fn=cmd_card)

    p = sub.add_parser("gloss", help="set a word's English gloss")
    p.add_argument("word")
    p.add_argument("gloss")
    p.add_argument("--batch", type=int)
    p.set_defaults(fn=cmd_gloss)

    p = sub.add_parser("note", help="attach a judgment call to a word (which sense, why)")
    p.add_argument("word")
    p.add_argument("note")
    p.add_argument("--batch", type=int)
    p.set_defaults(fn=cmd_note)

    p = sub.add_parser("export", help="write groundwork/assignments.tsv, the seed init reads")
    p.set_defaults(fn=cmd_export)

    p = sub.add_parser("find", help="look a word up")
    p.add_argument("word")
    p.set_defaults(fn=cmd_find)

    p = sub.add_parser("status", help="coverage across batches and the glue pool")
    p.add_argument("--batch", type=int)
    p.set_defaults(fn=cmd_status)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

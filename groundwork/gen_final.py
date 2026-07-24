import datetime
from build import TOPICS, load_entries
from subgroups import SUBGROUPS
from premises import PREMISES, TOPIC_META
from gen_doc import TOPIC_SCENES, chunk

entries = load_entries()
by_string = {}
for e in entries:
    by_string.setdefault(e['canonical'], []).append(e['idx'])

# ---- coverage audit (re-derived exactly as build.py does it) ----
assigned_idx = set()
claimed_by = {}
for topic, words in TOPICS.items():
    for w in words:
        candidates = by_string.get(w)
        unused = [c for c in candidates if c not in assigned_idx]
        idx = unused[0] if unused else candidates[-1]
        assigned_idx.add(idx)
        claimed_by.setdefault(idx, []).append(topic)
all_idx = set(e['idx'] for e in entries)
missing = sorted(all_idx - assigned_idx)
coverage_n = len(assigned_idx)
coverage_total = len(entries)
coverage_pct = round(100 * coverage_n / coverage_total, 1)

lines = []
lines.append("# Goethe B1 Wortliste — Topic Taxonomy & Scene-Outline Groundwork")
lines.append("")
lines.append("Groundwork for the crammed-topic-batch / mnemonic-scene Anki method. "
              "This file is taxonomy + scene **outlines** only — no German practice texts are written here.")
lines.append("")
lines.append(f"Source: `goethe-b1-wortliste.csv`, {coverage_total} entries (header row skipped). "
              "Parsed with Python (see Methodology note at the end); lemma = the first headword segment of "
              "column 1, with regional-variant `→` lines and parenthetical region tags (D/A/CH) stripped.")
lines.append("")

# ---------------------------------------------------------------
# 1. Taxonomy table
# ---------------------------------------------------------------
lines.append("## 1. Topic taxonomy")
lines.append("")
lines.append("| Topic | Words | Description |")
lines.append("|---|---:|---|")
for topic in TOPICS:
    n = len(TOPICS[topic])
    desc = TOPIC_META.get(topic, "")
    lines.append(f"| {topic} | {n} | {desc} |")
lines.append(f"| **Total (with ~26 intentional cross-topic duplicates)** | **{sum(len(v) for v in TOPICS.values())}** | |")
lines.append("")

# ---------------------------------------------------------------
# 2. Assignment strategy
# ---------------------------------------------------------------
lines.append("## 2. Assignment strategy")
lines.append("")
lines.append("**Unambiguous words** (concrete nouns/verbs clearly of one domain — `der Teppich`, `die Bäckerei`, "
              "`der Bahnhof`) were assigned straight to their obvious topic.")
lines.append("")
lines.append("**Generic / abstract content words** (verbs like `machen`, `bringen`, `stellen`; adjectives like "
              "`gut`, `schwer`, `deutlich`; nouns like `die Lage`, `der Sinn`) were distributed into four "
              "purpose-built topics that exist precisely to carry this vocabulary into concrete scenes: "
              "**Handlungen: Alltagsverben** (general-purpose action verbs), **Menge, Maß & Eigenschaften** "
              "(size/quality/quantity judgments), **Denken, Wissen & Meinen** (mental verbs — deciding, "
              "remembering, doubting), and **Kommunikation & Post** absorbs generic speech-act verbs "
              "(`sagen`, `antworten`, `behaupten`). Each of these is still just as scene-outlined as a concrete "
              "topic like Tiere — e.g. `stellen/legen/setzen` naturally live in a moving-day scene, `schwer/leicht` "
              "in a gym or a suitcase-packing scene.")
lines.append("")
lines.append("**Function / grammar words** (articles, pronouns, prepositions, conjunctions, question words, "
              "modal particles, degree adverbs — ~360 words) get their own dedicated topic, "
              "**Grammatik & Verbindungswörter**, rather than being force-fitted into unrelated concrete "
              "scenes (the task's alternative strategy). Rationale: these words are the connective tissue of "
              "*every* scene regardless of topic, so pretending each belongs to \"Tiere\" or \"Essen\" would be "
              "artificial. Instead they get their own scene-sized batches, each grouped **by grammatical "
              "function, not alphabetically** (prepositions / conjunctions / question words / spatial adverbs / "
              "time adverbs / degree particles / pronouns / modal verbs / small-talk glue), so every one of "
              "those scenes still has a concrete, imaginable premise (e.g. a scene of pure spatial adverbs "
              "becomes \"give chaotic directions to a lost drone\"). A handful of function-adjacent words that "
              "read naturally as part of a concrete scene (`heute`, `gestern`, `oft` → Zeit & Kalender; "
              "`Wetter`-adjacent connectors) were instead folded into the relevant concrete topic — the two "
              "strategies were mixed pragmatically rather than dogmatically applying only one.")
lines.append("")
lines.append("**Near-partition, not a strict one:** each word gets exactly one home topic by default. "
              "~26 words (~0.9%) were deliberately placed in a second topic because they genuinely power two "
              "different scene types (e.g. `der Bus` in both Unterwegs/Verkehr and Reisen/Urlaub; `das Brot` "
              "in both In-der-Wohnung and Essen; `dumm`/`beißen` in both a feelings scene and a body/health "
              "scene). These are listed in the coverage-audit note below.")
lines.append("")

# ---------------------------------------------------------------
# 3. Coverage audit
# ---------------------------------------------------------------
lines.append("## 3. Coverage audit")
lines.append("")
lines.append("Verified numerically with Python: every topic's word list was matched back against the full "
              f"parsed headword set by exact string, consuming one CSV row per match (duplicate-string rows "
              f"like the two distinct `die Bank` entries — bench vs. financial bank — are disambiguated by "
              f"row index, not string, so each lands on its own row). Result:")
lines.append("")
lines.append(f"- Total entries: **{coverage_total}**")
lines.append(f"- Assigned (unique rows covered): **{coverage_n}**")
lines.append(f"- Unassigned: **{len(missing)}**")
lines.append("")
if missing:
    lines.append("Unassigned entries:")
    for idx in missing:
        lines.append(f"- `{entries[idx]['canonical']}`")
else:
    lines.append("**No unassigned entries.**")
lines.append("")

dup = {idx: ts for idx, ts in claimed_by.items() if len(ts) > 1}
lines.append(f"Words intentionally placed in more than one topic ({len(dup)}), because they genuinely power "
              "two different scene types:")
lines.append("")
lines.append("<details><summary>show the {} cross-topic words</summary>".format(len(dup)))
lines.append("")
for idx in sorted(dup, key=lambda i: entries[i]['canonical']):
    ts = dup[idx]
    lines.append(f"- `{entries[idx]['canonical']}` — {', '.join(ts)}")
lines.append("")
lines.append("</details>")
lines.append("")

# ---------------------------------------------------------------
# 4. Scene outlines
# ---------------------------------------------------------------
lines.append("## 4. Scene outlines")
lines.append("")
lines.append("~10–15 target words per scene, grouped by topic (and by grammatical/semantic sub-function for "
              "the four abstract topics). Outlines only — premise + comedic angle + word list; no German text.")
lines.append("")

scene_counter_total = 0
for topic in TOPICS:
    n_words = len(TOPICS[topic])
    scenes = TOPIC_SCENES[topic]
    lines.append(f"### {topic}  _{n_words} words, {len(scenes)} scenes_")
    lines.append("")
    for i, (label, words) in enumerate(scenes, 1):
        scene_counter_total += 1
        key = (topic, i)
        title, premise, angle = PREMISES[key]
        sub = f" — *{label}*" if label else ""
        lines.append(f"**Scene {i}{sub}: {title}**")
        lines.append(f"- Premise: {premise}")
        lines.append(f"- Comedic angle: {angle}")
        lines.append(f"- Words ({len(words)}): {', '.join(words)}")
        lines.append("")
    lines.append("")

# ---------------------------------------------------------------
# 5. Methodology & judgment calls
# ---------------------------------------------------------------
lines.append("## 5. Methodology & judgment calls")
lines.append("")
lines.append("- **Parsing**: column 1 was split on `\\n`; lines starting with `→` (regional-variant notes, e.g. "
              "\"→ CH: Tram\") were dropped from lemma extraction but not from the entry itself — the row still "
              "counts as one entry. The remaining line(s) had parenthetical region tags (`(D)`, `(A, CH)` etc.) "
              "stripped, and the lemma is everything before the first comma (dropping plural/conjugation forms). "
              "Reflexive `(sich)` was preserved as a prefix.")
lines.append("- **The \"; \" separator**: the task description mentions cells with multiple headwords separated "
              "by `\"; \"`. In the actual CSV, `\"; \"` only ever occurs *inside* the `→` regional-variant note "
              "(e.g. \"→ A: Kuvert; CH: Couvert\"), never in the primary headword. The real multi-headword case in "
              "this list is masc/fem occupation pairs on separate lines within one cell (e.g. \"der Lehrer, -\\n"
              "die Lehrerin, -nen\"), which were merged into one combined lemma per row (\"der Lehrer / die "
              "Lehrerin\") since they're one CSV entry and will appear together in a scene anyway.")
lines.append("- **Row = entry**: each of the 2886 CSV rows counts as exactly one entry for coverage purposes "
              "(matching the task's own \"coverage: X/2886\" framing), even when a row's cell contains two "
              "merged headwords or a masc/fem pair.")
lines.append("- **`zurzeit` appears twice** in the source CSV as two separate, identical rows (idx 2811 and "
              "2861) — a genuine duplicate in the official wordlist, not a parsing artifact. Both rows are "
              "covered (the word appears twice across the topic lists, once in Zeit & Kalender's time-adverb "
              "scene and once in Grammatik's small-talk scene).")
lines.append("- **Duplicate-string entries with different meanings** (`der Ausdruck` printout vs. expression; "
              "`die Bank` bench vs. financial bank; `das Eis` ice vs. ice cream; `das Wort` Worte vs. Wörter; "
              "`der Sessel` in two regional senses) were deliberately split across two different, more fitting "
              "topics rather than both landing in the same place.")
lines.append("- **A few common verbs** (`nehmen`, `nennen`, `fallen`, `scheinen`) ended up bucketed inside "
              "Grammatik's \"Alltags-Kleinwörter\" catch-all sub-scene rather than in Handlungen — a minor "
              "taxonomic imperfection from the iterative build process. They're still fully covered and still "
              "get a concrete scene; a cleaner build would move them.")
lines.append(f"- **Total scenes**: {scene_counter_total}, averaging ~{round(coverage_total/scene_counter_total,1)} "
              "words each.")
lines.append("")
lines.append(f"coverage: {coverage_n}/{coverage_total} ({coverage_pct}%)")
lines.append("")

with open('/Users/andrey/anki/groundwork/agent-b.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print("wrote agent-b.md")
print(f"coverage: {coverage_n}/{coverage_total} ({coverage_pct}%)")
print(f"total scenes: {scene_counter_total}")

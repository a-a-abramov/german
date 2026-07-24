import pickle
from b_build import load_entries

with open('/Users/andrey/anki/groundwork/b_final_scenes.pkl', 'rb') as f:
    d = pickle.load(f)
FINAL = d['FINAL']
ORDER = d['ORDER']
TOPIC_SCENES = d['TOPIC_SCENES']

with open('/Users/andrey/anki/groundwork/b_final_premises.pkl', 'rb') as f:
    PREMISES = pickle.load(f)

entries = load_entries()
by_string = {}
for e in entries:
    by_string.setdefault(e['canonical'], []).append(e['idx'])

# ---- INDEPENDENT RE-VERIFICATION of coverage after all reshuffling ----
assigned_idx = set()
claimed_by = {}
for topic, words in FINAL.items():
    for w in words:
        cands = by_string.get(w)
        if not cands:
            raise SystemExit(f"FATAL: {w!r} (topic {topic}) not found in CSV-derived lemma set")
        unused = [c for c in cands if c not in assigned_idx]
        idx = unused[0] if unused else cands[-1]
        assigned_idx.add(idx)
        claimed_by.setdefault(idx, []).append(topic)
all_idx = set(e['idx'] for e in entries)
missing = sorted(all_idx - assigned_idx)
coverage_n = len(assigned_idx)
coverage_total = len(entries)
coverage_pct = round(100 * coverage_n / coverage_total, 2)

dup = {idx: ts for idx, ts in claimed_by.items() if len(ts) > 1}

# ---- also independently re-verify against the rendered scene word-lists,
# not just the FINAL topic dict (catches chunking/wiring bugs the topic-level
# check can't see) -----------------------------------------------------
scene_words = []
for topic in ORDER:
    for label, ws in TOPIC_SCENES[topic]:
        scene_words.extend(ws)
from collections import Counter
scene_counts = Counter(scene_words)
final_counts = Counter(w for ws in FINAL.values() for w in ws)
assert scene_counts == final_counts, "scene-level word lists drifted from topic-level FINAL dict!"

# batch / stage labels (concrete -> abstract cram order)
STAGES = [
    ("A. Konkret & körperlich (start here)", [
        'In der Wohnung & Zuhause', 'Körper & Gesundheit', 'Essen, Kochen & Restaurant',
        'Tiere', 'Kleidung & Aussehen', 'Farben, Formen & Material',
        'Familie & Beziehungen', 'Gefahr, Notfall & Sicherheit']),
    ("B. Situativ & alltagsweltlich", [
        'Natur, Wetter & Umwelt', 'Unterwegs & Verkehr', 'Reisen & Urlaub',
        'Einkaufen & Geld', 'Stadt, Ämter & Recht', 'Arbeit & Beruf',
        'Schule & Bildung', 'Freizeit, Medien & Technik']),
    ("C. Emotional & kommunikativ", [
        'Gefühle & Charakter', 'Kommunikation & Post', 'Zeit & Kalender',
        'Gesellschaft, Politik & Wirtschaft']),
    ("D. Abstrakt & grammatisch (save for last)", [
        'Menge, Maß & Eigenschaften', 'Handlungen: Alltagsverben', 'Denken, Wissen & Meinen',
        'Raum & Richtung', 'Logik & Verbindungen',
        'Grammatik-Glue (Pronomen, Partikeln, Kernverben)']),
]
assert [t for _, ts in STAGES for t in ts] == ORDER

TOPIC_META = {
    'In der Wohnung & Zuhause': "Rooms, furniture, household objects, chores, moving house.",
    'Körper & Gesundheit': "Body parts, illness, doctor, pharmacy, hospital, symptoms.",
    'Essen, Kochen & Restaurant': "Food, drink, cooking, groceries, restaurant & café life.",
    'Tiere': "Animals and farm life (a small, genuinely thin category in the B1 list).",
    'Kleidung & Aussehen': "Clothing, accessories, hairstyling, appearance.",
    'Farben, Formen & Material': "Color adjectives, geometric shapes, material/surface texture — carved out of the old grab-bag 'Menge/Eigenschaften' and 'Wohnung' topics as its own tight, highly imaginable batch (per JUDGE.md item 3, following agent A).",
    'Familie & Beziehungen': "Family members, life stages, relationships, weddings, parenting.",
    'Gefahr, Notfall & Sicherheit': "Danger, accidents, fire, emergency exits, warnings, rescue — carved out of Körper/Stadt/Gefühle into its own vivid batch (per JUDGE.md item 3, following agent A).",
    'Natur, Wetter & Umwelt': "Weather, landscape, environment, climate, countryside.",
    'Unterwegs & Verkehr': "Transport, traffic, directions, cars, trains, planes.",
    'Reisen & Urlaub': "Travel, hotels, vacation, tourism.",
    'Einkaufen & Geld': "Shopping, prices, banking, paying, contracts, budgets.",
    'Stadt, Ämter & Recht': "City life, government offices, bureaucracy, police, law, crime.",
    'Arbeit & Beruf': "Jobs, workplace, careers, hiring/firing, professions.",
    'Schule & Bildung': "School, university, courses, exams, learning.",
    'Freizeit, Medien & Technik': "Hobbies, sport, TV/film/music, art, gadgets, the internet.",
    'Gefühle & Charakter': "Emotions and personality traits.",
    'Kommunikation & Post': "Talking, phoning, writing letters/emails, the postal system, news media.",
    'Zeit & Kalender': "Time expressions, calendar, daily routine, punctuality (now also carrying the ~48 pure time-adverbs formerly stranded in the grammar mega-topic).",
    'Gesellschaft, Politik & Wirtschaft': "Society, politics, economy — the smallest topic; most B1 words here are abstract enough to also fit Stadt/Ämter or Denken.",
    'Menge, Maß & Eigenschaften': "Size, quantity, quality judgments and general descriptive adjectives (color/shape/material adjectives were carved out to their own topic, see Farben above).",
    'Handlungen: Alltagsverben': "The general-purpose verb toolkit — give/take, fix, organize, react — that powers everyday scenes (position verbs stehen/liegen/setzen/stellen/hängen were carved out to Raum & Richtung, see below).",
    'Denken, Wissen & Meinen': "Mental verbs: think, know, decide, remember, doubt, agree (Bedingung/Ausnahme/Folge/Voraussetzung were carved out to Logik & Verbindungen).",
    'Raum & Richtung': "Spatial prepositions and direction adverbs (an/auf/hinter/über/zwischen, da/dort/oben/unten) pulled together with the position verbs they always co-occur with (stehen/liegen/setzen/stellen/hängen/stecken/sitzen/legen) — adopted from agent C's taxonomy (JUDGE.md item 1): preposition + position-verb scenes cohere far better than either alone (hide-and-seek, lost-tourist, delivery-driver framings).",
    'Logik & Verbindungen': "Causal, conditional and concessive connectors (weil/obwohl/trotzdem/falls/dass/ob/sondern) plus the Bedingung/Ausnahme/Folge/Voraussetzung cluster pulled in from Denken and Handlungen so the 'exception to a rule' scene has its natural vocabulary in one place — adopted from agent C (JUDGE.md item 1).",
    'Grammatik-Glue (Pronomen, Partikeln, Kernverben)': "Pronouns, articles, modal particles, degree adverbs, question words and the highest-frequency light/modal verbs (sein/haben/machen/gehen/können…) — what's left of the old 360-word mega-topic once Raum, Logik and the Zeit-adverbs were carved out (JUDGE.md item 1). Politeness words (bitte/bitten/danke/danken/dankbar) were moved out to Kommunikation, where the politeness-loop scene actually needs them.",
}

lines = []
lines.append("# Goethe B1 Wortliste — Merged Topic Taxonomy & Scene Outlines (Final)")
lines.append("")
lines.append("**This is the merged, final deliverable.** It combines the winning entry (agent B — semantic "
             "within-scene word grouping) with specific ideas absorbed from the judged comparison in "
             "`JUDGE.md`: agent C's three-way functional split of the grammar mega-topic (RAUM / LOGIK / GLUE) "
             "and its sharper premises and audit rigor, and agent A's fine-grained Gefahr/Notfall and "
             "Farben/Formen/Material topics. See `JUDGE.md` for the comparison this builds on.")
lines.append("")
lines.append("Groundwork for the crammed-topic-batch → write-a-vivid-scene → Anki-card method. This file is "
             "taxonomy + scene **outlines** only — no German practice text is written here; that comes later, "
             "by hand, from these outlines.")
lines.append("")
lines.append(f"Source: `goethe-b1-wortliste.csv`, {coverage_total} data rows (version-header row skipped). "
             "Parsed with Python — see the Methodology section at the end for exactly how, plus every judgment "
             "call.")
lines.append("")

# ---------------------------------------------------------------
# Intro: concrete -> abstract cram order
# ---------------------------------------------------------------
lines.append("## 1. Taxonomy & cram order")
lines.append("")
lines.append("**26 topics** (up from 22: Farben/Formen/Material and Gefahr/Notfall/Sicherheit are carved out "
             "as new topics, and the old 360-word grammar mega-topic is split three ways into Raum & Richtung / "
             "Logik & Verbindungen / Grammatik-Glue), grouped into **4 stages ordered concrete → abstract**. "
             "The idea: cram the vivid, easy-to-picture, high-frequency material first, while motivation and "
             "visual imagination are freshest, and save the connective-tissue grammar words — which are "
             "necessary but inherently harder to hang a mental picture on — for last, once the concrete "
             "batches have already supplied a stock of scenes/characters those grammar words can be slotted "
             "into. None of the three original submissions sequenced topics this way (see `JUDGE.md` item 7); "
             "within each stage, topics still run roughly largest→smallest.")
lines.append("")
for stage_label, topics in STAGES:
    lines.append(f"**Stage {stage_label}**: " + " → ".join(topics))
    lines.append("")

# ---------------------------------------------------------------
# 2. Topic taxonomy table (batch-numbered)
# ---------------------------------------------------------------
lines.append("## 2. Topic taxonomy")
lines.append("")
lines.append("| Batch | Topic | Words | Scenes | Description |")
lines.append("|---:|---|---:|---:|---|")
batch_n = 0
for stage_label, topics in STAGES:
    for topic in topics:
        batch_n += 1
        n = len(FINAL[topic])
        ns = len(TOPIC_SCENES[topic])
        desc = TOPIC_META.get(topic, "")
        lines.append(f"| {batch_n} | {topic} | {n} | {ns} | {desc} |")
lines.append(f"| | **Total** ({len(dup)} intentional cross-topic duplicates, see §4) | **{sum(len(v) for v in FINAL.values())}** | **{sum(len(v) for v in TOPIC_SCENES.values())}** | |")
lines.append("")

# ---------------------------------------------------------------
# 3. Assignment strategy
# ---------------------------------------------------------------
lines.append("## 3. Assignment strategy")
lines.append("")
lines.append("**Unambiguous words** (concrete nouns/verbs clearly of one domain — `der Teppich`, `die Bäckerei`, "
             "`der Bahnhof`) were assigned straight to their obvious topic.")
lines.append("")
lines.append("**Fine-grained carve-outs** (new in this merged version, absorbed from agent A): color/shape/"
             "material adjectives (`bunt`, `rund`, `der Kreis`, `das Material`…) and danger/emergency "
             "vocabulary (`die Gefahr`, `der Notfall`, `retten`, `warnen`…) each get their own dedicated topic "
             "instead of being scattered across Menge/Wohnung/Körper/Stadt/Gefühle. Both are small "
             "(38 and 41 words) but tight and highly imaginable as their own cram batches.")
lines.append("")
lines.append("**Generic / abstract content words** (verbs like `machen`, `bringen`; adjectives like `gut`, "
             "`schwer`; nouns like `die Lage`, `der Sinn`) go into three purpose-built topics: "
             "**Handlungen: Alltagsverben** (general-purpose action verbs), **Menge, Maß & Eigenschaften** "
             "(size/quality judgments), **Denken, Wissen & Meinen** (mental verbs). Each is still fully "
             "scene-outlined, same as a concrete topic like Tiere.")
lines.append("")
lines.append("**Function / grammar words** — the hardest case, and the one place this merge changes B's "
             "original strategy most. Rather than one 360-word \"Grammatik & Verbindungswörter\" mega-topic, "
             "the words are split three ways **by grammatical role**, adopted from agent C's taxonomy "
             "(`JUDGE.md` item 1):")
lines.append("")
lines.append("- **Raum & Richtung** — spatial prepositions (`an/auf/hinter/über/zwischen`) and direction "
             "adverbs (`da/dort/oben/unten/rechts`) pulled together *with* the position verbs they always "
             "co-occur with in a location sentence (`stehen/liegen/setzen/stellen/hängen/stecken/sitzen/legen`, "
             "carved out of Handlungen). Framing devices: hide-and-seek, lost tourists, confused delivery "
             "drivers, a runaway drone — spatial vocabulary *is* the entire joke.")
lines.append("- **Logik & Verbindungen** — causal/conditional/concessive connectors (`weil/obwohl/trotzdem/"
             "falls/dass/ob/sondern`) plus a `Bedingung/Ausnahme/Folge/Voraussetzung` cluster pulled in from "
             "Denken and Handlungen, so the natural \"debate the exact conditions for an exception\" scene has "
             "its whole vocabulary in one place (see the lifted premise in §5, scene 3).")
lines.append("- **Grammatik-Glue** — pronouns, articles, modal particles, degree adverbs, question words, and "
             "the highest-frequency light/modal verbs (`sein/haben/machen/gehen/können…`). Politeness words "
             "(`bitte/bitten/danke/danken/dankbar`) were moved out to Kommunikation instead, where the "
             "politeness-loop scene (§5) actually needs them next to `sich bedanken`.")
lines.append("")
lines.append("Within every topic — including all three grammar splits and the two new carve-outs — words are "
             "grouped **by semantic/grammatical sub-function inside each scene, not alphabetically**: this is "
             "the feature that won the comparison in `JUDGE.md` (axis 3, \"Scene outlines\"), and it is kept "
             "and extended here, not diluted by the restructuring.")
lines.append("")
lines.append("**Near-partition, not a strict one:** each word gets one home topic by default. A handful of "
             "words are deliberately placed in a second topic because they genuinely power two different "
             "scene types (e.g. `der Bus` in both Unterwegs/Verkehr and Reisen/Urlaub). Listed in §4.")
lines.append("")

# ---------------------------------------------------------------
# 4. Coverage audit
# ---------------------------------------------------------------
lines.append("## 4. Coverage audit")
lines.append("")
lines.append("**Re-run from scratch after every reshuffle** (the Farben/Gefahr carve-outs and the three-way "
             "grammar split move ~230 words between topics, so coverage from before the merge cannot simply "
             "be assumed to still hold). Verified two ways:")
lines.append("")
lines.append("1. **Topic-level**: every topic's word list matched back against the canonical 2,886-row lemma "
             "set by exact string, consuming one CSV row per match (duplicate-string rows — see the homonym "
             "list below — are disambiguated by row index, not string, so each of the two rows lands "
             "separately).")
lines.append("2. **Scene-level**: independently re-collected every one of the 228 scenes' literal `Words (n): "
             "…` lists and asserted the multiset is identical to the topic-level word lists — i.e. topic "
             "assignment and rendered scene content cannot silently drift apart (this check caught and fixed "
             "two real reshuffling bugs during this merge: `rein/waagerecht/der Kreis/laut/die Form/parallel` "
             "briefly double-counted between Farben and the old grammar subgroup data, and `bitte` briefly "
             "duplicated between Grammatik and Kommunikation — both fixed before this file was generated).")
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

lines.append("**Homonym / regional-variant doublets** — CSV rows that share an identical lemma string but are "
             "genuinely two different entries (different meaning or different plural), each verified to land "
             "on its own row via index-based matching, not string matching:")
lines.append("")
homonym_notes = {
    'der Ausdruck': "printout (Ausdrucke) vs. linguistic expression (Ausdrücke) — different plurals in the source",
    'die Straßenbahn': "plain entry vs. the (D/A) entry cross-referencing CH \"Tram\"",
    'die U-Bahn': "two identical rows in the source list",
    'die Bank': "bench (Bänke) vs. financial bank (Banken)",
    'das Eis': "ice vs. ice cream — plain entry vs. the regional-variant (CH \"Glace\") entry",
    'fahren': "the plain verb vs. the separable (herunter-)fahren entry",
    'die Fahrkarte': "two rows, each cross-referencing a different CH \"Billet(t)\" spelling",
    'geschieden': "appears twice (adjective \"divorced\", used in two different collocations)",
    'der Kasten': "cabinet/crate (D) vs. cupboard (A/CH) — two different regional senses",
    'kosten': "to cost vs. the Austrian regional sense \"to taste\" (→ probieren)",
    'die Ordination': "→ Praxis vs. → Sprechstunde — two different Austrian cross-references",
    'der Vorort': "two identical rows in the source list",
    'der Wohnort': "two identical rows in the source list",
    'die Pension': "boarding house vs. → Rente (retirement) — two different senses",
    'die Praxis': "plain entry vs. the entry cross-referencing Austrian \"Ordination\"",
    'probieren': "plain entry vs. the (D/CH) entry cross-referencing Austrian \"kosten\"",
    'das Rad': "plain entry vs. the (D/A) entry cross-referencing \"Fahrrad\"/CH \"Velo\"",
    'zuschauen': "plain entry vs. the fully-conjugated entry",
    'der Sessel': "armchair (D/CH, → Fauteuil) vs. chair (A, → Stuhl) — two different regional senses",
    'das Wort': "Worte (words in a speech) vs. Wörter (individual words) — different plurals",
    'zurzeit': "a genuine duplicate row in the official list itself (not a homonym) — both instances covered, see Methodology",
}
for w, note in homonym_notes.items():
    lines.append(f"- `{w}` — {note}")
lines.append("")

dup = {idx: ts for idx, ts in claimed_by.items() if len(ts) > 1}
lines.append(f"**Words intentionally placed in more than one topic** ({len(dup)}), because they genuinely power "
             "two different scene types (this is separate from the homonym list above, which is about the "
             "source data, not editorial choice):")
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
# 5. Scene outlines
# ---------------------------------------------------------------
lines.append("## 5. Scene outlines")
lines.append("")
lines.append("~10–15 target words per scene (a few run leaner or richer where the natural grouping called for "
             "it). Grouped by topic in cram-batch order; abstract topics are further grouped by "
             "semantic/grammatical sub-function per scene. Outlines only — premise + comedic angle + word "
             "list, no German text.")
lines.append("")

batch_n = 0
scene_counter_total = 0
for stage_label, topics in STAGES:
    lines.append(f"### Stage {stage_label}")
    lines.append("")
    for topic in topics:
        batch_n += 1
        n_words = len(FINAL[topic])
        scenes = TOPIC_SCENES[topic]
        lines.append(f"#### Batch {batch_n}. {topic}  _{n_words} words, {len(scenes)} scenes_")
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
# 6. Methodology & judgment calls
# ---------------------------------------------------------------
lines.append("## 6. Methodology & judgment calls")
lines.append("")
lines.append("- **Parsing**: column 1 was split on `\\n`; lines starting with `→` (regional-variant notes, e.g. "
             "\"→ CH: Tram\") were dropped from lemma extraction but not from the entry itself — the row still "
             "counts as one entry. The remaining line(s) had parenthetical region tags (`(D)`, `(A, CH)` etc.) "
             "stripped, and the lemma is everything before the first comma (dropping plural/conjugation forms). "
             "Reflexive `(sich)` was preserved as a prefix.")
lines.append("- **The \"; \" separator**: the task description anticipates cells with multiple headwords "
             "separated by `\"; \"`. In the actual CSV, `\"; \"` only ever occurs *inside* the `→` "
             "regional-variant note (e.g. \"→ A: Kuvert; CH: Couvert\"), never in the primary headword. The "
             "real multi-headword case in this list is masc/fem occupation pairs on separate lines within one "
             "cell (e.g. \"der Lehrer, -\\ndie Lehrerin, -nen\"), merged into one combined lemma per row "
             "(\"der Lehrer / die Lehrerin\") since they're one CSV entry and appear together in a scene anyway.")
lines.append("- **Row = entry**: each of the 2886 CSV rows counts as exactly one entry for coverage purposes, "
             "even when its cell contains two merged headwords or a masc/fem pair.")
lines.append("- **CSV typo**: the row `irgendirgendein` is a duplicated-prefix typo in the official wordlist "
             "itself (its example sentence is about \"irgendeinen [Saft]\"); kept as the literal lemma "
             "`irgendirgendein` for coverage-matching purposes (so the row-count math stays exact), but should "
             "read as `irgendein` when actually writing the scene.")
lines.append("- **`zurzeit` appears twice** in the source CSV as two separate, identical rows — a genuine "
             "duplicate in the official wordlist, not a parsing artifact. Both rows are covered, and (after "
             "this merge pulled the old grammar topic's time-adverb batch into Zeit & Kalender) both now sit "
             "in Zeit & Kalender: once in its original calendar/time-of-day batch, once in the time-adverb "
             "batch absorbed from the old Grammatik split.")
lines.append("- **19 homonym/regional doublets** (see §4) were deliberately split across two different, more "
             "fitting topics/scenes rather than both landing in the same place.")
lines.append("- **This merge's restructuring** (per `JUDGE.md`'s \"ideas to absorb\"): the old 360-word "
             "\"Grammatik & Verbindungswörter\" topic was dissolved into Raum & Richtung / Logik & "
             "Verbindungen / Grammatik-Glue; ~48 pure time-adverbs were moved from that topic into Zeit & "
             "Kalender; ~38 danger/emergency words and ~41 color/shape/material words were carved out of six "
             "different host topics (Körper, Stadt, Gefühle, Natur, Unterwegs, Menge, Wohnung, Einkaufen, "
             "Freizeit, Arbeit) into two new dedicated topics; politeness words (`bitte/bitten/danke/danken/"
             "dankbar`, plus `das Paket`) were moved from Handlungen/Einkaufen into Kommunikation so two "
             "lifted premises (the politeness re-subscribe loop, the self-mailed reminder note) have their "
             "anchor words together in one scene. Every move was re-verified against the CSV afterward (§4) "
             "rather than assumed safe.")
lines.append("- **Reproducible pipeline**: `b_build.py` (CSV → canonical lemma list) → `b_subgroups.py` "
             "(semantic sub-grouping for the four large abstract B-topics) → `b_merge1.py`/`b_merge2.py` "
             "(mechanical word carve-outs/moves, coverage-checked at every step) → `b_merge3.py` (scene "
             "chunking) → `b_premises.py` + `b_new_premises.py` (all premise text) → "
             "`b_assemble_premises.py` (old→new scene-index mapping) → `b_gen_topics.py` (this script, "
             "re-verifies coverage from scratch and renders `topics.md`). Re-running the chain reproduces "
             "this file exactly.")
lines.append("- **A few common verbs** (`nehmen`, `nennen`, `fallen`, `scheinen`) ended up bucketed inside "
             "Grammatik-Glue's \"Alltags-Kleinwörter\" catch-all sub-scene rather than in Handlungen — a minor "
             "taxonomic imperfection inherited from the original build. Still fully covered and still get a "
             "concrete scene; a cleaner build would move them.")
lines.append(f"- **Total scenes**: {scene_counter_total}, averaging "
             f"~{round(coverage_total/scene_counter_total,1)} words each.")
lines.append("")
lines.append(f"coverage: {coverage_n}/{coverage_total} ({coverage_pct}%)")
lines.append("")

with open('/Users/andrey/anki/groundwork/topics.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print("wrote topics.md")
print(f"coverage: {coverage_n}/{coverage_total} ({coverage_pct}%)")
print(f"total topics: {batch_n}, total scenes: {scene_counter_total}")

# -*- coding: utf-8 -*-
import csv, re, json, importlib.util

# ---------- 1. Re-derive the canonical 2886-row lemma list straight from the CSV ----------
with open('/Users/andrey/anki/goethe-b1-wortliste.csv', encoding='utf-8') as f:
    rows = list(csv.reader(f))
data = rows[1:]

def clean_lemma(cell):
    first_line = cell.split('\n')[0]
    no_paren = re.sub(r'\([^()]*\)', '', first_line)
    lemma = no_paren.split(',')[0].strip()
    lemma = re.sub(r'\s+', ' ', lemma).strip()
    return lemma

all_lemmas = [clean_lemma(row[0]) for row in data]
all_lemmas = ['irgendein' if l == 'irgendirgendein' else l for l in all_lemmas]
assert len(all_lemmas) == 2886, len(all_lemmas)

# ---------- 2. Load classification + scenes + premises ----------
assigned = json.load(open('/Users/andrey/anki/groundwork/assigned1.json', encoding='utf-8'))
scenes_raw = json.load(open('/Users/andrey/anki/groundwork/scenes_raw.json', encoding='utf-8'))

spec = importlib.util.spec_from_file_location('premises', '/Users/andrey/anki/groundwork/premises.py')
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)
PREMISES = pm.PREMISES

TOPIC_NAMES = {
 'WOHNEN': 'In der Wohnung & Haushalt',
 'KOERPER': 'Körper & Gesundheit',
 'TIERE': 'Natur: Tiere & Pflanzen',
 'WETTER': 'Wetter, Landschaft & Umwelt',
 'ESSEN': 'Essen, Kochen & Restaurant',
 'FAMILIE': 'Familie, Beziehungen & Lebensereignisse',
 'ARBEIT': 'Arbeit, Beruf & Bewerbung',
 'VERKEHR': 'Unterwegs & Verkehr',
 'EINKAUFEN': 'Einkaufen, Geld & Bank',
 'GEFUEHLE': 'Gefühle & Charakter',
 'SCHULE': 'Schule, Ausbildung & Sprache lernen',
 'FREIZEIT': 'Freizeit, Sport & Medien/Technik',
 'REISEN': 'Reisen & Urlaub',
 'ZEIT': 'Zeit & Kalender',
 'KOMMUNIKATION': 'Kommunikation & Meinung',
 'STADT': 'Stadt, Ämter, Recht & Polizei',
 'MENGE': 'Menge, Maß, Vergleich & allgemeine Eigenschaften',
 'RAUM': 'Raum & Richtung',
 'LOGIK': 'Konnektoren: Grund, Bedingung & Gegensatz',
 'GESELLSCHAFT': 'Gesellschaft, Wirtschaft & Politik',
 'GLUE': 'Funktionswörter: Pronomen, Kernverben & Partikeln',
}

TOPIC_DESC = {
 'WOHNEN': 'Rooms, furniture, appliances, household chores and moving house.',
 'KOERPER': 'Body parts, illness, the doctor, pharmacy and physical states.',
 'TIERE': 'Animals, plants, farm and garden vocabulary (a small, thin topic in the B1 list).',
 'WETTER': 'Weather, landscape, climate and environmental protection.',
 'ESSEN': 'Food, drink, cooking, kitchen tools and restaurants.',
 'FAMILIE': 'Family members, relationships, life events (birth, marriage, divorce).',
 'ARBEIT': 'Jobs, professions, hiring, workplace life and careers.',
 'VERKEHR': 'Cars, public transport, traffic, roads and travel logistics.',
 'EINKAUFEN': 'Shops, money, banking, prices, paying and clothes shopping.',
 'GEFUEHLE': 'Emotions, personality traits and social/emotional reactions.',
 'SCHULE': 'School, studying, courses, language learning and academic life.',
 'FREIZEIT': 'Sport, hobbies, arts, entertainment, media and everyday technology.',
 'REISEN': 'Travel, hotels, sightseeing and vacations.',
 'ZEIT': 'Time expressions, calendar, frequency and sequencing.',
 'KOMMUNIKATION': 'Talking, phone, mail, media, opinions and persuasion.',
 'STADT': 'City life, public offices, bureaucracy, law, crime and police.',
 'MENGE': 'Quantities, measurements, comparison and general-purpose adjectives.',
 'RAUM': 'Spatial prepositions, directions and position verbs.',
 'LOGIK': 'Causal, conditional, concessive and contrastive connector words.',
 'GESELLSCHAFT': 'Politics, economy, culture, nationality and society at large.',
 'GLUE': 'Pronouns, articles, modal particles and the highest-frequency core verbs.',
}

# ---------- 3. Assemble scenes with topic, number, words, premise, angle ----------
scenes = []
for sid_str, sc in scenes_raw.items():
    sid = int(sid_str)
    premise, angle = PREMISES[sid]
    scenes.append({
        'sid': sid, 'topic': sc['topic'], 'num': sc['num'], 'of': sc['of'],
        'words': sc['words'], 'premise': premise, 'angle': angle,
    })
scenes.sort(key=lambda s: s['sid'])

# ---------- 4. COVERAGE AUDIT ----------
scene_word_union = set()
for s in scenes:
    scene_word_union.update(s['words'])

assigned_union = set(assigned.keys())
assert scene_word_union == assigned_union, (
    f"Scene words vs assigned dict mismatch: "
    f"{scene_word_union - assigned_union} | {assigned_union - scene_word_union}"
)

covered_rows = [l for l in all_lemmas if l in scene_word_union]
uncovered_rows = [l for l in all_lemmas if l not in scene_word_union]
n_covered = len(covered_rows)
n_total = len(all_lemmas)
pct = round(100 * n_covered / n_total, 2)

print(f"COVERAGE: {n_covered}/{n_total} ({pct}%)")
print("Uncovered:", uncovered_rows)

for s in scenes:
    assert s['premise'].strip(), s['sid']
    assert s['angle'].strip(), s['sid']
    assert 1 <= len(s['words']) <= 25, (s['sid'], len(s['words']))

# ---------- 5. Topic word counts (from `assigned`, i.e. the scene-derived union) ----------
from collections import defaultdict, Counter
topic_words = defaultdict(list)
for w, t in assigned.items():
    topic_words[t].append(w)
topic_row_counts = Counter()
for l in all_lemmas:
    if l in assigned:
        topic_row_counts[assigned[l]] += 1

json.dump({
    'n_covered': n_covered, 'n_total': n_total, 'pct': pct,
    'uncovered': uncovered_rows,
}, open('/Users/andrey/anki/groundwork/coverage_report.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print("Topic scene counts:", Counter(s['topic'] for s in scenes))
print("Total scenes:", len(scenes))
print("OK - ready to render markdown")

# stash for the markdown-writing step
import pickle
with open('/Users/andrey/anki/groundwork/render_state.pkl', 'wb') as f:
    pickle.dump({
        'scenes': scenes, 'topic_words': dict(topic_words),
        'topic_row_counts': dict(topic_row_counts),
        'n_covered': n_covered, 'n_total': n_total, 'pct': pct,
        'uncovered': uncovered_rows, 'TOPIC_NAMES': TOPIC_NAMES, 'TOPIC_DESC': TOPIC_DESC,
    }, f)

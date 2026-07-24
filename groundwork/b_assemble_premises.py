"""Build FINAL_PREMISES[(topic, new_scene_idx)] = (title, premise, angle)
by reusing old premises.py entries wherever the scene content is still the
same domain (mapped by explicit, verified old->new index correspondence),
and using b_new_premises.NEW for brand-new / restructured scenes.
"""
import pickle
from b_premises import PREMISES as OLD
from b_new_premises import NEW

with open('/Users/andrey/anki/groundwork/b_final_scenes.pkl', 'rb') as f:
    d = pickle.load(f)
TOPIC_SCENES = d['TOPIC_SCENES']
ORDER = d['ORDER']

FINAL_PREMISES = {}

def copy_range(topic, old_topic, mapping):
    """mapping: dict new_idx -> old_idx (same topic name unless old_topic given)"""
    ot = old_topic or topic
    for new_i, old_i in mapping.items():
        FINAL_PREMISES[(topic, new_i)] = OLD[(ot, old_i)]

# ---- topics unaffected: identical scene count & content --------------
for t in ['Familie & Beziehungen', 'Tiere', 'Reisen & Urlaub',
          'Gesellschaft, Politik & Wirtschaft', 'Schule & Bildung',
          'Essen, Kochen & Restaurant', 'Unterwegs & Verkehr',
          'Einkaufen & Geld', 'Arbeit & Beruf', 'Freizeit, Medien & Technik',
          'Gefühle & Charakter', 'Denken, Wissen & Meinen']:
    n = len(TOPIC_SCENES[t])
    copy_range(t, None, {i: i for i in range(1, n + 1)})

# ---- topics with a few words trimmed off the end: reuse premises 1..new_n
for t in ['In der Wohnung & Zuhause', 'Körper & Gesundheit', 'Kleidung & Aussehen',
          'Stadt, Ämter & Recht', 'Natur, Wetter & Umwelt']:
    n = len(TOPIC_SCENES[t])
    copy_range(t, None, {i: i for i in range(1, n + 1)})

# ---- Menge: Größe/Form lost 1 scene (old 1-3 -> new 1-2), everything
# after shifts by -1
copy_range('Menge, Maß & Eigenschaften', None, {
    1: 1, 2: 2,
    3: 4, 4: 5, 5: 6,
    6: 7, 7: 8, 8: 9,
    9: 10, 10: 11, 11: 12, 12: 13,
})

# ---- Handlungen: Verwaltung(1-3) & Geben/Nehmen(4-5) unchanged;
# Körperliche loses 1 scene at the tail (old 6-13 -> new 6-12); Bemühen
# shifts -1 (old 14-16 -> new 13-15); Dank(old17) dropped (its 3 leftover
# words folded silently into new15's word list)
copy_range('Handlungen: Alltagsverben', None, {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
    6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12,
    13: 14, 14: 15, 15: 16,
})

# ---- Zeit & Kalender: scenes 1-7 unchanged; scenes 8-11 = former
# Grammatik "Zeitadverbien" scenes 10-13
copy_range('Zeit & Kalender', None, {i: i for i in range(1, 8)})
copy_range('Zeit & Kalender', 'Grammatik & Verbindungswörter', {8: 10, 9: 11, 10: 12, 11: 13})

# ---- Raum & Richtung: Präp(1-2) + Richtung(3-6, from old 6-9) unchanged;
# scene 7 (Positionsverben) is brand new
copy_range('Raum & Richtung', 'Grammatik & Verbindungswörter', {1: 1, 2: 2, 3: 6, 4: 7, 5: 8, 6: 9})
FINAL_PREMISES[('Raum & Richtung', 7)] = NEW[('Raum & Richtung', 7)]

# ---- Logik & Verbindungen: Konjunktionen(1-2, from old 3-4) unchanged;
# scene 3 (Bedingungen/Ausnahmen) is brand new
copy_range('Logik & Verbindungen', 'Grammatik & Verbindungswörter', {1: 3, 2: 4})
FINAL_PREMISES[('Logik & Verbindungen', 3)] = NEW[('Logik & Verbindungen', 3)]

# ---- Grammatik-Glue: Fragewörter(1, old5), Grad(2-5, old14-17),
# Pronomen(6-7, old18-19), Modal(8, old20), Kleinwörter(9-14, old21-26);
# scene 15 merges old27+old28 (reuse old27's premise, its word list already
# includes what used to be old28's leftover words after chunk merging)
copy_range('Grammatik-Glue (Pronomen, Partikeln, Kernverben)', 'Grammatik & Verbindungswörter', {
    1: 5,
    2: 14, 3: 15, 4: 16, 5: 17,
    6: 18, 7: 19,
    8: 20,
    9: 21, 10: 22, 11: 23, 12: 24, 13: 25, 14: 26, 15: 27,
})

# ---- Farben & Gefahr: entirely new
for t in ['Farben, Formen & Material', 'Gefahr, Notfall & Sicherheit']:
    n = len(TOPIC_SCENES[t])
    for i in range(1, n + 1):
        FINAL_PREMISES[(t, i)] = NEW[(t, i)]

# ---- Kommunikation & Post: scenes 1 & 5 are the two lifted-C premises;
# everything else maps old 2,3,4,6,7,8,9,10,11,12,13,14 -> new
# 2,3,4,6,7,8,9,10,11,12,13,14 (identity, just skipping the 2 replaced slots)
FINAL_PREMISES[('Kommunikation & Post', 1)] = NEW[('Kommunikation & Post', 1)]
FINAL_PREMISES[('Kommunikation & Post', 5)] = NEW[('Kommunikation & Post', 5)]
copy_range('Kommunikation & Post', None, {i: i for i in [2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]})

# ---------------------------------------------------------------
# verify: every scene in TOPIC_SCENES has a premise
missing = []
for t in ORDER:
    for i in range(1, len(TOPIC_SCENES[t]) + 1):
        if (t, i) not in FINAL_PREMISES:
            missing.append((t, i))
print("missing premises:", len(missing))
for m in missing:
    print("  ", m)

with open('/Users/andrey/anki/groundwork/b_final_premises.pkl', 'wb') as f:
    pickle.dump(FINAL_PREMISES, f)
print("saved b_final_premises.pkl")

import pickle
from build import load_entries

with open('/Users/andrey/anki/groundwork/final_topics2.pkl', 'rb') as f:
    d = pickle.load(f)
FINAL = d['FINAL']
FINAL_SUBGROUPS = d['FINAL_SUBGROUPS']

entries = load_entries()

def chunk(lst, n=13, min_tail=6):
    out = []
    for i in range(0, len(lst), n):
        out.append(lst[i:i+n])
    if len(out) >= 2 and len(out[-1]) < min_tail:
        out[-2].extend(out[-1])
        out.pop()
    return out

# concrete -> abstract cram order
ORDER = [
    'In der Wohnung & Zuhause',
    'Körper & Gesundheit',
    'Essen, Kochen & Restaurant',
    'Tiere',
    'Kleidung & Aussehen',
    'Farben, Formen & Material',
    'Familie & Beziehungen',
    'Gefahr, Notfall & Sicherheit',
    'Natur, Wetter & Umwelt',
    'Unterwegs & Verkehr',
    'Reisen & Urlaub',
    'Einkaufen & Geld',
    'Stadt, Ämter & Recht',
    'Arbeit & Beruf',
    'Schule & Bildung',
    'Freizeit, Medien & Technik',
    'Gefühle & Charakter',
    'Kommunikation & Post',
    'Zeit & Kalender',
    'Gesellschaft, Politik & Wirtschaft',
    'Menge, Maß & Eigenschaften',
    'Handlungen: Alltagsverben',
    'Denken, Wissen & Meinen',
    'Raum & Richtung',
    'Logik & Verbindungen',
    'Grammatik-Glue (Pronomen, Partikeln, Kernverben)',
]

assert set(ORDER) == set(FINAL.keys()), (set(ORDER) ^ set(FINAL.keys()))

TOPIC_SCENES = {}
for topic in ORDER:
    if topic in FINAL_SUBGROUPS:
        scenes = []
        for label, ws in FINAL_SUBGROUPS[topic]:
            for c in chunk(ws):
                scenes.append((label, c))
        TOPIC_SCENES[topic] = scenes
    else:
        TOPIC_SCENES[topic] = [(None, c) for c in chunk(FINAL[topic])]

total = sum(len(v) for v in TOPIC_SCENES.values())
print("TOTAL SCENES:", total)
print()
for topic in ORDER:
    print(f"## {topic} ({len(FINAL[topic])} words, {len(TOPIC_SCENES[topic])} scenes)")
    for i, (label, ws) in enumerate(TOPIC_SCENES[topic], 1):
        print(f"  scene {i} [{label}] ({len(ws)}): {', '.join(ws)}")
    print()

with open('/Users/andrey/anki/groundwork/final_scenes.pkl', 'wb') as f:
    pickle.dump({'FINAL': FINAL, 'ORDER': ORDER, 'TOPIC_SCENES': TOPIC_SCENES}, f)

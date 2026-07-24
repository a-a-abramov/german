"""Step 2: fine-tune word ORDER within a few flat topics so that specific
lifted-premise anchor words end up clustered in the same scene after chunking
(Kommunikation's two lifted C premises need Absender/Empfänger/Paket/Anruf
together, and bitte/bitten/danke/danken/dankbar/die Bitte together).
Then produce the full scene scaffold for every topic/subgroup and save it.
"""
import pickle, re
from build import load_entries
from subgroups import SUBGROUPS

with open('/Users/andrey/anki/groundwork/final_topics.pkl', 'rb') as f:
    FINAL = pickle.load(f)

entries = load_entries()

def chunk(lst, n=13, min_tail=6):
    out = []
    for i in range(0, len(lst), n):
        out.append(lst[i:i+n])
    if len(out) >= 2 and len(out[-1]) < min_tail:
        out[-2].extend(out[-1])
        out.pop()
    return out

# ---------------------------------------------------------------
# Kommunikation & Post: reorder so lifted premises get clustered
# ---------------------------------------------------------------
komm = FINAL['Kommunikation & Post']
tail_added = ['danken', 'der Dank', 'dankbar', 'danke', 'bitten', 'die Bitte', 'das Paket', 'bitte']
for w in tail_added:
    komm.remove(w)

def insert_after(lst, anchor, items):
    idx = lst.index(anchor)
    for i, it in enumerate(items):
        lst.insert(idx + 1 + i, it)

# cluster 1: self-mailed reminder note (Absender/Empfänger/Paket/Anruf)
insert_after(komm, 'der Anrufbeantworter', ['das Paket'])
komm.remove('der Empfänger')
insert_after(komm, 'das Paket', ['der Empfänger'])

# cluster 2: politeness re-subscribe loop (bitte/bitten/danke/danken/dankbar)
insert_after(komm, 'sich bedanken', ['bitte', 'bitten', 'die Bitte', 'danke', 'danken', 'dankbar'])

FINAL['Kommunikation & Post'] = komm

# ---------------------------------------------------------------
# Build subgroup structures for the topics that need them
# ---------------------------------------------------------------
gram = dict(SUBGROUPS['Grammatik & Verbindungswörter'])
POSITION_VERBS = ['liegen', 'stellen', 'stecken', 'hängen', 'stehen', 'stehen bleiben',
                  '(sich) setzen', 'sitzen', 'legen']
LOGIK_PULL = ['die Bedingung', 'die Ausnahme', 'die Folge', 'folgen', 'folgend', 'die Voraussetzung']

FINAL_SUBGROUPS = {}

# IMPORTANT: gram's subgroup lists are the ORIGINAL, pre-carve-out word
# lists (die Form / der Kreis / laut / parallel / rein / waagerecht were
# pulled out to FARBEN in merge1.py, and this stale `gram` copy still
# contains them) -- every subgroup built from `gram` below MUST be filtered
# against FINAL['Raum & Richtung'] / FINAL['Grammatik-Glue ...'] (the
# already-carved-out flat lists) so none of those 6 words leak back in as
# duplicates.
raum_present = set(FINAL['Raum & Richtung'])
FINAL_SUBGROUPS['Raum & Richtung'] = [
    ("Präpositionen (Ort/Zeit/Grund)", [w for w in gram['Präpositionen (Ort/Zeit/Grund)'] if w in raum_present]),
    ("Richtung & Ort (Raumadverbien)", [w for w in gram['Richtung & Ort (Raumadverbien)'] if w in raum_present]),
    ("Positionsverben (stehen/liegen/setzen/stellen/hängen)", list(POSITION_VERBS)),
]

FINAL_SUBGROUPS['Logik & Verbindungen'] = [
    ("Konjunktionen & Satzverbinder", gram['Konjunktionen & Satzverbinder']),
    ("Bedingungen, Ausnahmen & Folgen", LOGIK_PULL),
]

glue_present = set(FINAL['Grammatik-Glue (Pronomen, Partikeln, Kernverben)'])
klein = [w for w in gram['Alltags-Kleinwörter & Small Talk'] if w in glue_present]
FINAL_SUBGROUPS['Grammatik-Glue (Pronomen, Partikeln, Kernverben)'] = [
    ("Fragewörter", gram['Fragewörter']),
    ("Grad-, Mengen- & Modalpartikeln", gram['Grad-, Mengen- & Modalpartikeln']),
    ("Pronomen & Artikelwörter", gram['Pronomen & Artikelwörter']),
    ("Modal- & Hilfsverben", gram['Modal- & Hilfsverben']),
    ("Alltags-Kleinwörter & Small Talk", klein),
]

# Denken / Handlungen / Menge keep their existing subgroup labels, with
# affected subgroups already shrunk by the removals in merge1.py; reuse the
# ORIGINAL SUBGROUPS words list but filtered down to what's still actually
# present in FINAL[topic] (drops removed words automatically, preserves
# original sub-theme order).
for topic in ('Denken, Wissen & Meinen', 'Handlungen: Alltagsverben', 'Menge, Maß & Eigenschaften'):
    still_present = set(FINAL[topic])
    new_groups = []
    for label, ws in SUBGROUPS[topic]:
        filtered = [w for w in ws if w in still_present]
        if filtered:
            new_groups.append((label, filtered))
    FINAL_SUBGROUPS[topic] = new_groups

# merge Handlungen's now-thin "Dank, Auftritt & Ausdruck" remainder into
# "Bemühen, Wandel & Reaktion" (dekorieren/bieten/brauchen leftover)
hg = FINAL_SUBGROUPS['Handlungen: Alltagsverben']
dank_leftover = None
for i, (label, ws) in enumerate(hg):
    if label == 'Dank, Auftritt & Ausdruck':
        dank_leftover = ws
        del hg[i]
        break
if dank_leftover:
    for i, (label, ws) in enumerate(hg):
        if label == 'Bemühen, Wandel & Reaktion':
            ws.extend(dank_leftover)
            break

# sanity: every word in FINAL_SUBGROUPS[topic] must be in FINAL[topic], and
# vice versa (multiset-equal)
from collections import Counter
for topic, groups in FINAL_SUBGROUPS.items():
    flat = [w for _, ws in groups for w in ws]
    a = Counter(flat)
    b = Counter(FINAL[topic])
    if a != b:
        print(f"MISMATCH in {topic}: missing_from_groups={list((b-a).elements())} extra_in_groups={list((a-b).elements())}")
    else:
        print(f"OK {topic}: {len(flat)} words, groups match FINAL exactly")

with open('/Users/andrey/anki/groundwork/final_topics2.pkl', 'wb') as f:
    pickle.dump({'FINAL': FINAL, 'FINAL_SUBGROUPS': FINAL_SUBGROUPS}, f)
print("saved final_topics2.pkl")

"""Step 1: mechanical restructuring of TOPICS -> FINAL_TOPICS (flat word lists,
no scene chunking yet). Verifies coverage stays at 2886/2886 throughout.
"""
import copy
from b_build import TOPICS, load_entries
from b_subgroups import SUBGROUPS

entries = load_entries()
canon_set = set(e['canonical'] for e in entries)
by_string = {}
for e in entries:
    by_string.setdefault(e['canonical'], []).append(e['idx'])

def coverage_check(topics_dict, label):
    assigned = set()
    for topic, words in topics_dict.items():
        for w in words:
            cands = by_string.get(w)
            if not cands:
                print(f"  !! NOT IN CSV: {w!r} (topic {topic})")
                continue
            unused = [c for c in cands if c not in assigned]
            idx = unused[0] if unused else cands[-1]
            assigned.add(idx)
    total = len(entries)
    print(f"[{label}] assigned {len(assigned)}/{total}")
    return assigned

print("=== baseline (original B) ===")
coverage_check(TOPICS, "baseline")

GEFAHR = ['Achtung!','der Alarm','beschädigen','brennen','das Feuer','die Feuerwehr','fliehen','die Flucht',
'die Gefahr','gefährlich','das Gift','giftig','kaputt','kaputtgehen','kaputtmachen','die Katastrophe',
'der Lärm','der Notausgang','der Notfall','der Notruf','retten','das Risiko','schaden','der Schaden',
'schädlich','schützen','der Schutz','die Sicherheit','sichern','tödlich','überfahren','der Unfall',
'das Unglück','(sich) verbrennen','die Vorsicht','vorsichtig','warnen','zerstören']

FARBEN = ['der Bogen','breit','bunt','dicht','dunkel','dünn','eckig','eng','die Farbe','farbig','flach',
'der Fleck','die Form','glatt','das Gold','hart','hell','das Holz','der Kreis','das Kreuz','künstlich',
'der Kunststoff','laut','das Leder','leise','die Linie','das Loch','das Material','das Metall','parallel',
'das Plastik','rein','rund','schief','schmal','senkrecht','spitz','der Stoff','waagerecht','weich','die Wolle']

POSITION_VERBS = ['liegen','stellen','stecken','hängen','stehen','stehen bleiben','(sich) setzen','sitzen','legen']
LOGIK_PULL = ['die Bedingung','die Ausnahme','die Folge','folgen','folgend','die Voraussetzung']
DANK_PULL = ['danken','der Dank','dankbar','danke','bitten','die Bitte']  # -> Kommunikation
PAKET_PULL = ['das Paket']  # -> Kommunikation

def remove_word(topics, word):
    for t, ws in topics.items():
        if word in ws:
            ws.remove(word)
            return t
    print(f"  !! could not find {word!r} to remove")
    return None

FINAL = copy.deepcopy(TOPICS)

# --- carve out GEFAHR & FARBEN -----------------------------------------
for w in GEFAHR:
    remove_word(FINAL, w)
for w in FARBEN:
    remove_word(FINAL, w)
FINAL['Gefahr, Notfall & Sicherheit'] = list(GEFAHR)
FINAL['Farben, Formen & Material'] = list(FARBEN)

# --- pull position verbs & bitte/danke/paket before dissolving Grammatik
for w in POSITION_VERBS:
    remove_word(FINAL, w)
for w in LOGIK_PULL:
    remove_word(FINAL, w)
for w in DANK_PULL:
    remove_word(FINAL, w)
for w in PAKET_PULL:
    remove_word(FINAL, w)
remove_word(FINAL, 'bitte')

FINAL.setdefault('Kommunikation & Post', [])
FINAL['Kommunikation & Post'].extend(DANK_PULL)
FINAL['Kommunikation & Post'].extend(PAKET_PULL)
FINAL['Kommunikation & Post'].append('bitte')

# --- dissolve Grammatik & Verbindungswörter into RAUM / LOGIK / GLUE + Zeit
# NB: gram_subgroups comes from the SUBGROUPS module, i.e. the ORIGINAL
# pre-carve-out word lists -- 6 FARBEN words (die Form, der Kreis, laut,
# parallel, rein, waagerecht) were hosted in Grammatik and have already been
# removed from FINAL['Grammatik & Verbindungswörter'] by the FARBEN loop
# above, but that removal doesn't touch the separate, immutable SUBGROUPS
# data. Every piece pulled from gram_subgroups below is therefore filtered
# against `still_in_gram` (the just-cleaned flat list) so none of those 6
# carved-out words can leak back in as duplicates.
still_in_gram = set(FINAL['Grammatik & Verbindungswörter'])
gram_subgroups = dict(SUBGROUPS['Grammatik & Verbindungswörter'])
praep = [w for w in gram_subgroups['Präpositionen (Ort/Zeit/Grund)'] if w in still_in_gram]
richtung = [w for w in gram_subgroups['Richtung & Ort (Raumadverbien)'] if w in still_in_gram]
konj = [w for w in gram_subgroups['Konjunktionen & Satzverbinder'] if w in still_in_gram]
frage = [w for w in gram_subgroups['Fragewörter'] if w in still_in_gram]
zeit = [w for w in gram_subgroups['Zeitadverbien'] if w in still_in_gram]
grad = [w for w in gram_subgroups['Grad-, Mengen- & Modalpartikeln'] if w in still_in_gram]
pron = [w for w in gram_subgroups['Pronomen & Artikelwörter'] if w in still_in_gram]
modal = [w for w in gram_subgroups['Modal- & Hilfsverben'] if w in still_in_gram]
klein = [w for w in gram_subgroups['Alltags-Kleinwörter & Small Talk'] if w in still_in_gram]

assert 'bitte' not in klein and 'sitzen' not in klein

RAUM = list(praep) + list(richtung) + list(POSITION_VERBS)
LOGIK = list(konj) + list(LOGIK_PULL)
GLUE = list(frage) + list(grad) + list(pron) + list(modal) + list(klein)

# remove the old Grammatik topic entirely, replace with the three new ones
del FINAL['Grammatik & Verbindungswörter']
FINAL['Raum & Richtung'] = RAUM
FINAL['Logik & Verbindungen'] = LOGIK
FINAL['Grammatik-Glue (Pronomen, Partikeln, Kernverben)'] = GLUE

# Zeitadverbien -> Zeit & Kalender
FINAL.setdefault('Zeit & Kalender', [])
FINAL['Zeit & Kalender'].extend(zeit)

print("\n=== after restructuring ===")
final_assigned = coverage_check(FINAL, "final")

all_idx = set(e['idx'] for e in entries)
missing = sorted(all_idx - final_assigned)
print("missing:", len(missing))
for idx in missing:
    print("  ", idx, entries[idx]['canonical'])

print("\nTopic word counts:")
for t, ws in FINAL.items():
    print(f"  {t}: {len(ws)}")
print("sum:", sum(len(v) for v in FINAL.values()))

import pickle
with open('/Users/andrey/anki/groundwork/b_final_topics.pkl', 'wb') as f:
    pickle.dump(FINAL, f)
print("\nsaved b_final_topics.pkl")

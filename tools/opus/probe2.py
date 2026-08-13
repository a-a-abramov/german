"""Follow-ups on what probe 1 exposed: aux hops, coordination, the Tasse lemma bug."""
import sys, spacy
model = sys.argv[1] if len(sys.argv) > 1 else "de_core_news_sm"
nlp = spacy.load(model, exclude=["ner"])
print("### MODEL:", model)

LEMMA_CHECK = [
    "Ich trinke eine heisse Tasse Kaffee.", "Die Tasse steht auf dem Tisch.",
    "Er kauft zwei Tassen.", "Der Schrank ist gross.", "Die Betten sind gemacht.",
    "Sie hat die Teller gewaschen.", "Wir haben die Wohnung geputzt.",
]
print("\n--- lemma spot-check (NOUN/VERB only) ---")
for s in LEMMA_CHECK:
    doc = nlp(s)
    print(f"  {s:42} " + "  ".join(f"{t.text}->{t.lemma_}" for t in doc
                                   if t.pos_ in ("NOUN", "VERB", "ADJ")))

print("\n--- aux hop / coordination / predicative structure ---")
for s in ["Der Mieter hat die Wohnung gemietet.", "Die Wohnung kostet viel Geld.",
          "Ich habe Brot und Kaese gekauft.", "Das Zimmer ist hell und gross.",
          "Der Schrank wurde von ihm gekauft.", "Sie muss die Wohnung putzen."]:
    doc = nlp(s)
    print(f"  {s}")
    for t in doc:
        if t.dep_ in ("sb", "oa", "da", "cj", "cd", "pd", "oc", "sbp"):
            print(f"      {t.text:10} {t.lemma_:10} {t.pos_:5} {t.dep_:5} -> "
                  f"{t.head.text}/{t.head.pos_}/{t.head.dep_}")

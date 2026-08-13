"""Step 3a: verify TIGER dependency labels EMPIRICALLY before writing any counting code.
The mapping table in diy-wortprofil-opensubtitles.md is from memory and must not be trusted."""
import spacy

nlp = spacy.load("de_core_news_sm", exclude=["ner"])

SENTS = [
    "Der Mieter hat die kleine Wohnung im Zentrum schnell gemietet.",
    "Er wohnt in der Wohnung.",
    "Er geht in die Wohnung.",
    "Die Wohnung ist teuer.",
    "Der Preis der Wohnung steigt.",
    "Wohnung und Haus sind teuer.",
    "Ich trinke eine heisse Tasse Kaffee.",
    "Sie hilft ihrem Bruder mit dem Schrank.",
    "Der Schrank wurde von ihm gekauft.",
]

for s in SENTS:
    print("=" * 78)
    print(s)
    doc = nlp(s)
    for t in doc:
        morph = str(t.morph)
        print(f"  {t.text:12} {t.lemma_:12} {t.pos_:6} {t.dep_:8} -> {t.head.text:10} "
              f"{'children=' + ','.join(c.text + '/' + c.dep_ for c in t.children):40} {morph}")

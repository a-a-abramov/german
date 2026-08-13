#!/usr/bin/env python3
"""
test_extract.py — the gate that must pass before the overnight run starts.

It checks the two failure modes that produce a full night of unusable rows without
ever raising an error:

  * ROW DIRECTION. Rows are rendered through the same RELATION_PATTERNS map that
    tools/wortprofil.py uses. The expectations below are written as the finished chunk
    ("Wohnung(Akk.) mieten"), so a reversed row fails loudly here instead of showing up
    as "mieten(Akk.) Wohnung" in a text three weeks from now.
  * THE AUX HOP. 'Der Mieter hat die Wohnung gemietet' must produce Mieter->mieten.
    If the auxiliary resolution regresses it produces Mieter->haben, which is still a
    perfectly well-formed row and is silently worthless.
"""
import sys
import spacy
from extract import triples

# The renderer's patterns, inlined so this test runs inside the container without
# needing the repo. Kept identical to tools/wortprofil.py:RELATION_PATTERNS.
PATTERNS = {
    "hat Adjektivattribut": "ein(e) {c}e(r) {L}",
    "ist Adjektivattribut von": "ein(e) {L}e(r) {c}",
    "ist Akkusativ-Objekt von": "{L}(Akk.) {c}",
    "hat Akkusativ-Objekt": "{L} + {c}(Akk.)",
    "ist Dativ-/Genitiv-Objekt von": "{L}(Dat./Gen.) {c}",
    "hat Dativ-/Genitiv-Objekt": "{L} + {c}(Dat./Gen.)",
    "ist Subjekt von": "{L} {c}(t)",
    "hat Subjekt": "{c} {L}(t)",
    "ist Passivsubjekt von": "{L} wird {c}",
    "hat Passivsubjekt": "{c} wird {L}",
    "ist in Präpositionalgruppe": "{c} … {L}",
    "hat Präpositionalgruppe": "{L} + {c}",
    "hat Genitivattribut": "{L} des/der {c}",
    "ist Genitivattribut von": "{c} des/der {L}",
    "hat Prädikativ": "{L} ist/wird {c}",
    "ist Prädikativ zu": "{c} ist/wird {L}",
    "ist in Koordination mit": "{L} und {c}",
}

CASES = [
    ("Der Mieter hat die kleine Wohnung gemietet.", [
        ("Wohnung", "ist Akkusativ-Objekt von", "mieten", ""),
        ("mieten", "hat Akkusativ-Objekt", "Wohnung", ""),
        ("Mieter", "ist Subjekt von", "mieten", ""),      # aux hop, NOT 'haben'
        ("klein", "ist Adjektivattribut von", "Wohnung", ""),
        ("Wohnung", "hat Adjektivattribut", "klein", ""),
    ]),
    ("Er wohnt in der Wohnung.", [
        ("Wohnung", "ist in Präpositionalgruppe", "in wohnen", "Dat"),
        ("wohnen", "hat Präpositionalgruppe", "in Wohnung", "Dat"),
    ]),
    ("Er geht in die Wohnung.", [
        ("Wohnung", "ist in Präpositionalgruppe", "in gehen", "Acc"),   # case differs!
    ]),
    ("Die Wohnung ist teuer.", [
        ("Wohnung", "hat Prädikativ", "teuer", ""),
        ("teuer", "ist Prädikativ zu", "Wohnung", ""),
    ]),
    # 'Zimmer und Kueche sind hell' — coordination across a NOUN/PROPN tag split
    ("Das Zimmer ist hell und gross.", [
        ("gross", "ist in Koordination mit", "hell", ""),
    ]),
    ("Der Preis der Wohnung steigt.", [
        ("Wohnung", "ist Genitivattribut von", "Preis", ""),
        ("Preis", "hat Genitivattribut", "Wohnung", ""),
    ]),
    ("Ich habe Brot und Kaese gekauft.", [
        ("Brot", "ist Akkusativ-Objekt von", "kaufen", ""),
        ("Kaese", "ist in Koordination mit", "Brot", ""),   # hop through 'und'
    ]),
    ("Der Schrank wurde von ihm gekauft.", [
        ("Schrank", "ist Passivsubjekt von", "kaufen", ""),  # passive, not active sb
    ]),
    ("Sie hilft ihrem Bruder.", [
        ("Bruder", "ist Dativ-/Genitiv-Objekt von", "helfen", ""),
    ]),
]

# Rows that must NEVER appear: the exact shapes the recipe's mapping would produce.
FORBIDDEN = [
    ("Mieter", "ist Subjekt von", "haben", ""),
    ("Wohnung", "ist Subjekt von", "sein", ""),   # copular subject = zero information
    ("Schrank", "ist Subjekt von", "werden", ""),
    ("Kaese", "ist in Koordination mit", "und", ""),
]


def main():
    nlp = spacy.load("de_core_news_sm", exclude=["ner"])
    failures, checked = [], 0
    seen_all = set()

    for sent, expected in CASES:
        got = set(triples(nlp(sent)))
        seen_all |= got
        for want in expected:
            checked += 1
            if want not in got:
                failures.append((sent, want, sorted(got)))

    for bad in FORBIDDEN:
        checked += 1
        if bad in seen_all:
            failures.append(("<forbidden row present>", bad, []))

    for sent, want, got in failures:
        print(f"FAIL  {sent}\n  expected: {want}")
        for g in got:
            print(f"      got: {g}")
        print()

    # Show the rendered chunks — the whole point is that these read like German.
    print("--- rendered chunks (eyeball these) ---")
    for h, rel, c, case in sorted(seen_all):
        pat = PATTERNS.get(rel)
        if pat:
            print(f"  {pat.format(L=h, c=c):38} [{rel}{'|' + case if case else ''}]")

    print(f"\n{checked - len(failures)}/{checked} assertions passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

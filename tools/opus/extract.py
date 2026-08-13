#!/usr/bin/env python3
"""
extract.py — dependency-triple extraction, shared by parse_shard.py and the tests.

THE MAPPING IS EMPIRICAL. Every rule below was read off actual de_core_news_sm output
(tools/opus/probe_labels.py, probe2.py), not from the table in
groundwork/diy-wortprofil-opensubtitles.md. That table is wrong in four ways that would
each have quietly poisoned a whole night of counting:

  1. AUXILIARY HOP. In periphrastic tenses the subject attaches to the finite auxiliary,
     not to the content verb:
         Der Mieter hat die Wohnung gemietet.
             Mieter  sb -> hat/AUX        <- NOT 'mieten'
             gemietet oc -> hat/AUX
     Counting naively yields "Mieter ist Subjekt von haben" for a large fraction of all
     German sentences. Every relation therefore resolves AUX -> its `oc` child.

  2. PASSIVE. `werden` + participle makes the `sb` a PASSIVE subject, which is a
     different relation and a different chunk pattern ("Schrank wird gekauft", not
     "Schrank kauft"). `werden` + infinitive is future tense, not passive — the two are
     told apart by VerbForm on the `oc` child.

  3. COORDINATION goes through the conjunction, not directly:
         Brot und Kaese:  und cd -> Brot,  Kaese cj -> und
     A bare `cj` rule links Kaese to *und*.

  4. PREDICATIVES attach to the copula, so the thing being described has to be fetched
     as the copula's `sb` child. Also, spaCy tags predicative adjectives as ADV
     ("teuer", "hell"), so a pos_ == "ADJ" test drops nearly all of them.

Relation names are exactly the strings in tools/wortprofil.py:RELATION_PATTERNS, and
every relation is emitted in BOTH directions using that file's existing inverse names.
That matters because the renderer formats "ist Akkusativ-Objekt von" as "{L}(Akk.) {c}":
storing only the dependent->head direction the recipe describes would render
"mieten(Akk.) Wohnung" instead of "Wohnung(Akk.) mieten".

Prepositional groups follow the renderer's convention too: the collocate is a two-word
"<preposition> <lemma>" string, which is the shape tools/wortprofil.py:in_b1() already
knows how to strip prepositions out of. Case rides in its own column rather than being
baked into the relation name — that keeps the case information (which DWDS does not
publish) without inventing a relation string the renderer would not recognise.
"""

# (forward relation, inverse relation) — both names taken from RELATION_PATTERNS.
R_SUBJ    = ("ist Subjekt von", "hat Subjekt")
R_PSUBJ   = ("ist Passivsubjekt von", "hat Passivsubjekt")
R_ACC     = ("ist Akkusativ-Objekt von", "hat Akkusativ-Objekt")
R_DAT     = ("ist Dativ-/Genitiv-Objekt von", "hat Dativ-/Genitiv-Objekt")
R_GEN     = ("ist Genitivattribut von", "hat Genitivattribut")
R_ADJ     = ("ist Adjektivattribut von", "hat Adjektivattribut")
R_PRED    = ("ist Prädikativ zu", "hat Prädikativ")
R_PP      = ("ist in Präpositionalgruppe", "hat Präpositionalgruppe")
R_COORD   = ("ist in Koordination mit", "ist in Koordination mit")   # symmetric

CONTENT = {"NOUN", "PROPN", "VERB", "ADJ", "ADV"}
# spaCy tags possessives and a few quantifiers as ADJ, so they surface as
# "eine deine Wohnung" in the Adjektivattribut relation. They are determiners
# semantically and carry no collocational information about the noun.
NOT_ADJECTIVES = {"mein", "dein", "sein", "ihr", "unser", "euer", "Ihr",
                  "welch", "solch", "manch", "jed", "all", "kein", "dies"}
NOMINAL = {"NOUN", "PROPN"}
COPULA = {"sein", "werden", "bleiben"}
# Adjacency prepositions arrive as fused forms (im/zum/ans); spaCy lemmatises those
# back to in/zu/an, which is what we want — case is what distinguishes them.
PP_DEPS = {"mo", "op", "pg", "mnr"}


def norm_lemma(tok):
    """Nouns keep their capital (matches the Goethe list); everything else lowercases.
    Sentence-initial verbs otherwise show up as a separate lemma from mid-sentence ones."""
    lem = tok.lemma_.strip()
    if not lem:
        return ""
    return lem[0].upper() + lem[1:] if tok.pos_ in NOMINAL else lem.lower()


def usable(lem):
    return (len(lem) >= 2 and len(lem) <= 40
            and lem[0].isalpha() and not any(c.isdigit() for c in lem))


def content_verb(tok):
    """Resolve an auxiliary to the verb that carries the meaning.

    Returns (verb_token, is_passive). A finite AUX with an `oc` child is periphrastic —
    the `oc` child is the real predicate. `werden` + participle is passive; `werden` +
    infinitive is future, which is NOT passive.
    """
    if tok.pos_ != "AUX":
        return tok, False
    oc = next((c for c in tok.children if c.dep_ == "oc" and c.pos_ in ("VERB", "AUX")), None)
    if oc is None:
        return tok, False                      # 'haben'/'sein' used as a full verb
    passive = (tok.lemma_ == "werden"
               and "Part" in oc.morph.get("VerbForm", []))
    return oc, passive


def case_of(tok):
    c = tok.morph.get("Case")
    return c[0] if c else ""


def pos_class(pos):
    """For coordination we only want to link like with like — but spaCy scatters
    capitalised nouns between NOUN and PROPN ('Brot und Kaese' makes Kaese a PROPN),
    and predicative adjectives between ADJ and ADV. Compare classes, not tags."""
    if pos in NOMINAL:
        return "N"
    if pos in ("ADJ", "ADV"):
        return "A"
    return pos


def first_conjunct(tok):
    """`cj` hangs off the conjunction (`cd`), whose head is the first conjunct.
    Some parses attach `cj` straight to the first conjunct; handle both shapes."""
    h = tok.head
    return h.head if h.dep_ == "cd" else h


def triples(doc):
    """Yield (headword, relation, collocate, case) — already in BOTH directions.

    `case` is non-empty only for prepositional groups, where it is the case of the noun
    inside the group. That is the one thing DWDS's own display does not give you: it is
    what separates 'in die Wohnung' (Akk., direction) from 'in der Wohnung' (Dat.,
    location).
    """
    def emit(a, rel_pair, b, case=""):
        """a = the dependent/described side, b = the governing side."""
        fwd, inv = rel_pair
        yield a, fwd, b, case
        yield b, inv, a, case

    for t in doc:
        dep, pos = t.dep_, t.pos_

        # ---- subject / passive subject ------------------------------------------
        if dep == "sb" and pos in NOMINAL:
            verb, passive = content_verb(t.head)
            # 'die Wohnung ist teuer' would otherwise also emit "Wohnung ist Subjekt
            # von sein", which is true of every noun in the language and says nothing.
            # The informative half of a copular clause is the predicative, handled below.
            if verb.pos_ in ("VERB", "AUX") and not (verb.lemma_ in COPULA and not passive):
                a, b = norm_lemma(t), norm_lemma(verb)
                if usable(a) and usable(b):
                    yield from emit(a, R_PSUBJ if passive else R_SUBJ, b)

        # ---- accusative object ---------------------------------------------------
        elif dep == "oa" and pos in NOMINAL:
            verb, _ = content_verb(t.head)
            a, b = norm_lemma(t), norm_lemma(verb)
            if verb.pos_ in ("VERB", "AUX") and usable(a) and usable(b):
                yield from emit(a, R_ACC, b)

        # ---- dative object (Wortprofil lumps dative and genitive objects) --------
        elif dep in ("da", "og") and pos in NOMINAL:
            verb, _ = content_verb(t.head)
            a, b = norm_lemma(t), norm_lemma(verb)
            if verb.pos_ in ("VERB", "AUX") and usable(a) and usable(b):
                yield from emit(a, R_DAT, b)

        # ---- genitive attribute:  der Preis der Wohnung --------------------------
        elif dep == "ag" and pos in NOMINAL and t.head.pos_ in NOMINAL:
            a, b = norm_lemma(t), norm_lemma(t.head)
            if usable(a) and usable(b):
                yield from emit(a, R_GEN, b)

        # ---- attributive adjective:  eine kleine Wohnung -------------------------
        elif dep == "nk" and pos == "ADJ" and t.head.pos_ in NOMINAL:
            a, b = norm_lemma(t), norm_lemma(t.head)
            if (usable(a) and usable(b) and a not in NOT_ADJECTIVES
                    and not t.morph.get("Poss")):
                yield from emit(a, R_ADJ, b)

        # ---- predicative:  die Wohnung ist teuer --------------------------------
        # Attaches to the copula; the described noun is the copula's `sb`. spaCy tags
        # these adjectives ADV, so ADJ-only would lose almost all of them.
        elif dep == "pd" and pos in ("ADJ", "ADV", "NOUN", "PROPN"):
            cop = t.head
            if cop.lemma_ in COPULA:
                subj = next((c for c in cop.children
                             if c.dep_ == "sb" and c.pos_ in NOMINAL), None)
                if subj is not None:
                    a, b = norm_lemma(t), norm_lemma(subj)
                    if usable(a) and usable(b):
                        yield from emit(a, R_PRED, b)

        # ---- coordination:  Brot und Kaese --------------------------------------
        elif dep == "cj" and pos in CONTENT:
            other = first_conjunct(t)
            if pos_class(other.pos_) == pos_class(pos):   # coordinate like with like
                a, b = norm_lemma(t), norm_lemma(other)
                if usable(a) and usable(b) and a != b:
                    yield from emit(a, R_COORD, b)

        # ---- prepositional group:  in der Wohnung wohnen ------------------------
        # The ADP heads the group: its `nk` child is the noun, its own head is the
        # content word the group modifies. Two hops, as the recipe says — but the
        # recipe's invented 'in+wohnen' relation name is not one the renderer knows,
        # so the preposition goes into the COLLOCATE instead.
        elif pos == "ADP" and dep in PP_DEPS:
            noun = next((c for c in t.children
                         if c.dep_ == "nk" and c.pos_ in NOMINAL), None)
            if noun is None:
                continue
            gov, _ = content_verb(t.head)
            if gov.pos_ not in ("VERB", "AUX", "NOUN", "PROPN", "ADJ"):
                continue
            prep, n_lem, g_lem = t.lemma_.lower(), norm_lemma(noun), norm_lemma(gov)
            if not (usable(prep) and usable(n_lem) and usable(g_lem)):
                continue
            case = case_of(noun)
            # Direction 1: headword = the noun, collocate = "<prep> <governor>"
            yield n_lem, R_PP[0], f"{prep} {g_lem}", case
            # Direction 2: headword = the governor, collocate = "<prep> <noun>"
            yield g_lem, R_PP[1], f"{prep} {n_lem}", case

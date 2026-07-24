# Functional sub-grouping for the big abstract topics, so scene premises
# have a coherent spine instead of alphabetical word-salad.
# Each SUBGROUPS[topic] is a list of (label, [words]); the union (as a
# multiset) must exactly equal TOPICS[topic] from build.py -- verified by
# check_subgroups().

from build import TOPICS, load_entries

SUBGROUPS = {}

SUBGROUPS['Grammatik & Verbindungswörter'] = [
    ("Präpositionen (Ort/Zeit/Grund)", [
        'ab','an','auf','aus','bei','bis','durch','entlang','für','gegen','gegenüber',
        'in','mit','nach','neben','ohne','per','pro','seit','statt','trotz','über','um',
        'unter','von','vor','während','wegen','zwischen']),
    ("Konjunktionen & Satzverbinder", [
        'aber','als','als ob','also','bevor','dass','denn','deshalb','deswegen','doch',
        'entweder ... oder','indem','je … desto …','jedoch','nachdem','obwohl','oder',
        'seitdem','sobald','sodass','solange','sondern','sowohl … als auch','trotzdem',
        'und','weder … noch','weil','wenn','um … zu','falls']),
    ("Fragewörter", [
        'was','was für ein-','wann','warum','weshalb','wie','wieso','wie viel','wo',
        'woher','wohin','wer','welcher']),
    ("Richtung & Ort (Raumadverbien)", [
        'da','dabei','dafür','dagegen','daher','dahin','damit','daneben','dort','dorthin',
        'drüben','drin','entgegenkommen','her/her-','heraus-','herein-','herunter-',
        'hier/hier-','hierher','hinten','hinter/hinter-','innen','inner-','innerhalb',
        'nah','nebenan','nebenbei','oben','ober-','unten','unter-','unterwegs',
        'vorn','vorder-','waagerecht','quer','rauf/rauf-','raus/raus-','rechts','rein',
        'überall','vorbei/vorbei-','weg/weg-','zurück/zurück-','geradeaus','weit',
        'lang',
        ]),
    ("Zeitadverbien", [
        'bisher','diesmal','fest','fertig','gerade','jetzt','jeweils','kurz','kürzlich',
        'lange','langsam','längst','letzt-','meist','meist-','mittlerweile','nachher',
        'nächst-','noch','noch mal','nochmals','normalerweise','nun','oft/öfter',
        'plötzlich','regelmäßig','sofort','ständig','übermorgen','vorgestern','vorher',
        'vorhin','vorläufig','zuerst','zunächst','zurzeit','zuletzt','zumindest',
        'inzwischen','irgendwann','jederzeit','jedes Mal','bereits','extra',
        'manchmal','sonst','weiter/weiter-','wieder/wieder-']),
    ("Grad-, Mengen- & Modalpartikeln", [
        'auch','außer','außerdem','beinahe','direkt','eben','ebenfalls','ebenso',
        'extrem','ganz','gar','genau','genauso','gleich','gleichfalls','gleichzeitig',
        'kaum','komplett','mehr','mehrere','mindestens','möglichst','nur','paar',
        'recht','relativ','richtig','sehr','sicher','so','sogar','soviel',
        'so viel/so viel wie','sowieso','überhaupt','umso','umsonst','ungefähr',
        'viel/viele','vielleicht','völlig','wenig/wenige','wenigstens',
        'zusammen/zusammen-','allerdings','ja','nämlich','natürlich','offenbar',
        'schon','selbstverständlich','wahrscheinlich','vermutlich','zwar','wohl']),
    ("Pronomen & Artikelwörter", [
        'derselbe','dies-','eigen-','es','jeder','kein-','man','manch-','nichts',
        'niemand','selb-','selbst','selber','solch-','irgendirgendein','jemand',
        'jemals','nirgends','nirgendwo','nie','nein','beid-','ein bisschen',
        'meinetwegen','möglich','die Möglichkeit','worüber','worum','zufällig']),
    ("Modal- & Hilfsverben", [
        'dürfen','können','möchten','mögen','müssen','sollen','wollen','werden',
        'haben','sein','lassen']),
    ("Alltags-Kleinwörter & Small Talk", [
        'bitte','bloß','der Fall','fällig','falsch',
        'fast','frei','im Freien','freiwillig','fremd','die Form','das Geschlecht',
        'auseinander','begleiten','das Detail','das Gegenteil','sich befinden',
        'gucken','halt','klar','klappen','klären','komisch','kommen','kompliziert',
        'korrekt','die Länge','der Kreis','leid tun','heim','hinterlassen','laut',
        'miteinander','mitten','mittler-','nett','neu','nicht','niedrig','normal',
        'Lieblings-','ob','offen','parallel','privat',
        'nutzen','passen','die Sache','passiv','riechen','sehen','die Seite',
        'sitzen','stattfinden','stammen','Speise-/-speise','Spezial-','speziell',
        'stumm','die Stufe','das Teil','der Teil','das Stück/-stück','übrig',
        'übrigens','unbedingt',
        'un-','vertrauen','voneinander','vor allem','voraus','ursprünglich',
        'zu','zu sein','wachsen','der Zweck','einschließlich','einverstanden',
        'entstehen','erfüllen','ergänzen','etwa','etwas','eventuell','miss-',
        'mobil/mobil-','national/national-','negativ','durcheinander','eigentlich',
        'fallen','gern/gerne','gesamt-/Gesamt-','je','nehmen','nennen','recht-',
        'sogenannt-']),
]


SUBGROUPS['Handlungen: Alltagsverben'] = [
    ("Verwaltung, Organisieren & Absprachen", [
        'abgeben','abmachen','absagen','abstimmen','bedienen','die Bedienungsanleitung',
        'die Bedingung','beraten','die Beratung','bestätigen','die Bestätigung','bestehen',
        'bestellen','betreuen','der Betreuer / die Betreuerin','die Betreuung','dienen',
        'einsetzen','einstellen','eintragen','unterbrechen','unternehmen','unterlassen',
        'verpflichtet','verschieben','(sich) vorbereiten','die Vorbereitung','vorhaben',
        'zusagen','zusammenfassen','unterscheiden','besprechen','die Besprechung',
        'darstellen','die Darstellung',
        'verteilen','umtauschen','der Umtausch','verwenden','warten']),
    ("Geben, Nehmen & Besitzen", [
        'abheben','abholen','bekommen','benötigen','benutzen','besitzen','besorgen',
        'bringen','geben','gebrauchen','die Gebrauchsanweisung','gehören','greifen',
        'halten','der Halt','heben','holen','kriegen','leihen','liefern','die Lieferung',
        'liegen','tragen','treiben','stellen','die Stelle','stecken','hängen']),
    ("Körperliche Alltagsaktionen", [
        'aufhalten','aufheben','anschließen','ausziehen','aufräumen','aufpassen',
        'drehen','drucken','der Drucker','drücken','der Druck','fangen','bleiben',
        'gehen','heißen','kaputtgehen','kaputtmachen','kaputt','kämpfen','der Kampf',
        'sich kümmern','lächeln','lachen','leben','löschen','machen','pflanzen',
        'die Pflanze','schaffen','schalten','schauen','zuschauen','schließen',
        '(sich) schneiden','schneien','schütteln','schützen','der Schutz','sammeln',
        '(sich) setzen','sinken','schlagen','rennen','schießen','springen',
        'staubsaugen','spülen','stürzen','tauschen','teilen','tauchen','stehlen',
        'stinken','(sich) stoßen','treffen','treten','tun','üben','überlegen',
        'übernehmen','verlassen','verlieren','(sich) verstecken','(sich) verstehen',
        'versuchen','vermeiden','vergleichen','der Vergleich','verpacken',
        'verschwinden','vergessen','verbringen','verbrauchen','verbinden',
        'die Verbindung','(sich) verbessern','(sich) verbrennen','unterstreichen',
        'vergeblich','verzichten','(sich) waschen','wechseln','sich weigern',
        'weinen','wenden','werfen','wiegen','winken','ziehen','zugehen','zumachen',
        'zunehmen','zurechtkommen','wehtun','stehen','stehen bleiben','steigen',
        'stoppen','stören']),
    ("Bemühen, Wandel & Reaktion", [
        'ändern','die Änderung','anfangen','aufhören','aufladen','ausmachen',
        'sich bemühen','beschränken','beschreiben','die Beschreibung','behalten',
        'behandeln','der Beitrag','klagen','entfernen','ersetzen','der Ersatz',
        'gelingen','integrieren','die Integration','helfen','die Hilfe','sorgen',
        'die Sorge','sparen','sparsam','spazieren gehen','der Spaziergang',
        'suchen','reduzieren','protestieren','der Protest','abnehmen','beobachten',
        'berechnen','retten']),
    ("Dank, Auftritt & Ausdruck", [
        'danken','der Dank','dankbar','danke','dekorieren','bieten','bitten',
        'die Bitte','brauchen']),
]

SUBGROUPS['Menge, Maß & Eigenschaften'] = [
    ("Größe, Form & Menge", [
        'groß','Groß-','die Größe','klein','breit','die Breite','dick','dicht',
        'eng','hoch','die Höhe','tief','schmal','rund',
        'eckig','spitz','steil','riesig','die Menge','die Gruppe','messen',
        'das Mal','mal','Einzel-','einzeln','einzig-','sämtliche','die Einzelheit',
        'insgesamt','minimal','die Leiter','das Mittel',
        'der Gegenstand','das Ding']),
    ("Qualität & Bewertung", [
        'gut','schlecht','schlimm','ausgezeichnet',
        'perfekt','ideal','praktisch','preiswert','prima','super',
        'positiv','optimistisch','realistisch','original','das Original','echt',
        'die Qualität','wertlos','wertvoll','wert','der Wert','nützlich','nötig',
        'notwendig','erforderlich','erfordern','gültig','haltbar','streng',
        'der Vorteil','tolerant','die Fähigkeit','fair','gerecht','gleichberechtigt']),
    ("Grad & Vergleich", [
        'absolut','allgemein','ähnlich','all-','aller-','ander-','andererseits',
        'anders','besonder-','besonders','bestimmt','deutlich','durchschnittlich',
        'der Durchschnitt','eindeutig','einheitlich','einig-','einfach',
        'gering','genug','genügen','ausreichend','ausreichen','umgekehrt','höchstens',
        'unterschiedlich','verschieden','vergrößern','verlängern','verwechseln',
        'total','übertreiben','ungewöhnlich','unglaublich','unheimlich',
        'verständlich','ziemlich','zahlreich','regional','stilistisch','-weise',
        'vorwärts','senkrecht']),
    ("Charakter von Dingen (Konsistenz & Tempo)", [
        'hart','weich','stark','schwach','schwer','die Schwierigkeit','schwierig',
        'bequem','kräftig','knapp','klug','intelligent','die Intelligenz','intensiv',
        'individuell','häufig','schnell','scharf','spannend','teuer','der Satz',
        'treu','wild','zuverlässig','zufrieden','wahnsinnig','weiblich','reif',
        'reich','das Gewicht','der Gegensatz','das Tempo','voll','schief',
        'hübsch','pauschal','korrigieren','leise','mündlich','eher','ehrlich',
        'der Bedarf','die Entfernung','enthalten','flexibel','die Gewohnheit',
        'gewohnt','gewöhnlich','gewöhnen','furchtbar','bunt',
        'schlank']),
]

SUBGROUPS['Denken, Wissen & Meinen'] = [
    ("Meinen, Wissen & Überzeugen", [
        'meinen','die Meinung','glauben','wissen','das Wissen','die Wissenschaft',
        'der Wissenschaftler / die Wissenschaftlerin','wahr','die Wahrheit','wichtig',
        'widersprechen','wirklich','die Wirklichkeit','der Zweifel','zweifeln',
        'zustimmen','die Zustimmung','vermuten','vernünftig','das Verständnis',
        'akzeptieren','bekannt','bemerken','sich irren','beweisen','der Beweis',
        'begründen','die Begründung','ordentlich','realisieren','die Realität',
        'reagieren','die Reaktion','ausschließen','ausschließlich','annehmen',
        'genehmigen','gelten',]),
    ("Entscheiden, Planen & Feststellen", [
        'entscheiden','die Entscheidung','unentschieden','sich entschließen',
        'entschlossen','beschließen','sich einigen','wählen','die Wahl',
        'die Voraussetzung','der Unterschied','vorkommen','festhalten','festlegen',
        'feststehen','feststellen','finden','folgen','die Folge','folgend',
        'führen','beachten','beschäftigen','die Beschäftigung','die Art',
        'auflösen','die Reihenfolge','die Reihe','reichen','das Ziel','der Zustand']),
    ("Erinnern, Entdecken & Verstehen", [
        'der Gedanke','denken','erinnern','die Erinnerung','erkennen','entdecken',
        'erfinden','die Erfindung','erwarten','nachdenken','nachschlagen','kennen',
        'kennenlernen','die Kenntnisse','merken','merkwürdig','sich nähern',
        'die Nähe','das Geheimnis','geheim','die Herkunft','der Inhalt',
        'gründlich','sichtbar','scheinen','der Schein','seltsam','typisch',
        'der Typ','der Tipp']),
    ("Streit, Absicht & Gemütslage (abstrakt)", [
        'abhängen','abhängig','die Ahnung','ablehnen','die Absicht','achten',
        'auffallen','aufmerksam','die Alternative','alternativ','die Ausnahme',
        'der Bescheid','Bescheid sagen','Bescheid geben','die Distanz','doch',
        'der Eindruck','einerseits','einfallen','der Einfall','der Einfluss',
        'beeinflussen','der Faktor','fassen','der Kompromiss','die Konferenz',
        'die Konkurrenz','die Lage','die Liste','die Lösung','lösen','die Lüge',
        'lügen','die Methode','mischen','die Nachfrage','die Nachricht',
        'das Problem','der Respekt','das Risiko','sinnlos','sinnvoll','der Sinn',
        'schätzen','die Rücksicht','die Situation','der/dasObers','die Stimmung',
        'die Tat','die Tatsache','die Störung','(sich) überzeugen','die Überzeugung',
        'überraschen','die Überraschung','das Verhalten','sich verhalten',
        'das Verhältnis','die Praxis','das Gewissen','geschehen','bewegen',
        'der Zusammenhang']),
]


def check_subgroups(topic):
    groups = SUBGROUPS[topic]
    flat = [w for _, ws in groups for w in ws]
    from collections import Counter
    a = Counter(flat)
    b = Counter(TOPICS[topic])
    missing_from_groups = list((b - a).elements())  # in TOPICS but not grouped
    extra_in_groups = list((a - b).elements())       # grouped but not in TOPICS
    return missing_from_groups, extra_in_groups


if __name__ == '__main__':
    for topic in SUBGROUPS:
        missing, extra = check_subgroups(topic)
        print(f"{topic}: missing_from_groups={len(missing)} extra_in_groups={len(extra)}")
        if missing:
            print("  MISSING:", missing)
        if extra:
            print("  EXTRA:", extra)

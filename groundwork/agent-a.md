# Goethe B1 Wortschatz — Themen-Taxonomie & Szenen-Grundlage

Groundwork fuer das mnemonic/scene-basierte Anki-Lernprojekt. Datenquelle: `goethe-b1-wortliste.csv` (2.886 Eintraege, per Python geparst — Spalte 1 wurde in Lemmata zerlegt, Mehrfach-Kopfwoerter pro Zelle wurden getrennt erfasst). Alle Zahlen in diesem Dokument sind Python-verifiziert (siehe Coverage-Audit am Ende).

## 1. Themen-Taxonomie

| Thema | ~Woerter | Beschreibung |
|---|---|---|
| **Glue-Wörter: Grammatik & Funktionswörter** | 194 | Pronomen, Präpositionen, Konjunktionen, Modalverben, Partikeln — das Bindegewebe jedes Satzes. |
| **Denken, Meinung & abstrakte Begriffe** | 294 | Nachdenken, Entscheiden, Meinen, Ursache/Wirkung, Bedeutung, Bürokratie-Sprache. |
| **Kommunikation, Medien & Technik** | 202 | Telefon, Internet, Post, Zeitung, Geräte. |
| **Essen, Trinken & Kochen** | 172 | Lebensmittel, Gerichte, Restaurant, Kochen, Geschmack. |
| **Gefühle & Charakter** | 159 | Emotionen, Persönlichkeitseigenschaften, zwischenmenschliches Verhalten. |
| **Körper & Gesundheit** | 161 | Körperteile, Krankheiten, Arztbesuche, Medikamente, Hygiene. |
| **Freizeit, Kultur & Unterhaltung** | 165 | Hobbys, Sport, Kino, Musik, Feste, Spiele. |
| **In der Wohnung & Haushalt** | 133 | Zimmer, Möbel, Umzug, Hausarbeit und alles rund ums Zuhause. |
| **Staat, Recht & Gesellschaft** | 146 | Ämter, Polizei, Gesetze, Politik, Kriminalität, Formulare. |
| **Einkaufen, Geld & Handel** | 132 | Geschäfte, Preise, Banken, Zahlen, Konsum. |
| **Arbeit & Beruf** | 152 | Berufe, Bewerbung, Büroalltag, Anstellung, Karriere. |
| **Zeit & Kalender** | 116 | Uhrzeit, Datum, Häufigkeit, Dauer, Termine. |
| **Schule & Bildung** | 123 | Unterricht, Prüfungen, Studium, Sprache lernen. |
| **Familie, Beziehungen & Lebensphasen** | 114 | Verwandtschaft, Partnerschaft, Heirat, Kindheit/Alter, Freundschaft. |
| **Orte & räumliche Lage** | 99 | Richtungen, Positionen, Stadtgeografie, 'wo/wohin'. |
| **Menge, Maß & Vergleich** | 94 | Zahlen, Mengenangaben, Vergleiche, Maße. |
| **Verkehr & Unterwegs** | 92 | Verkehrsmittel, Straßenverkehr, Fahren, Ampeln, Staus. |
| **Natur, Wetter & Tiere** | 89 | Landschaft, Klima, Pflanzen, Tiere, Naturphänomene. |
| **Eigenschaften & Bewertung** | 73 | Allgemeine Adjektive zum Beschreiben und Bewerten von Dingen. |
| **Reisen & Urlaub** | 67 | Flughafen, Hotel, Gepäck, Sehenswürdigkeiten, Grenzen. |
| **Alltagshandlungen (allgemeine Verben)** | 62 | Häufige, thematisch neutrale Tätigkeitsverben des Alltags. |
| **Farben, Formen & Material** | 41 | Farbadjektive, geometrische Formen, Materialbeschaffenheit. |
| **Gefahr, Notfall & Sicherheit** | 38 | Unfälle, Notrufe, Brand, Warnungen, Schutz. |
| **Kleidung & Aussehen** | 38 | Kleidungsstücke, Anziehen, äußere Erscheinung. |
| **Umwelt, Energie & Wirtschaft** | 16 | Umweltschutz, Industrie, Ressourcen, Wirtschaft im Großen. |

**Gesamt (mit Mehrfachformen wie Maskulin/Feminin-Paaren gezaehlt): 2972 Lemma-Eintraege ueber 2886 Wortlisten-Zeilen, verteilt auf 25 Themen.**

## 2. Zuordnungsstrategie

**Eindeutige Woerter zuerst:** Konkrete Substantive, Verben und Adjektive mit klarem Sachfeld (Teppich, Bahnsteig, Krankenschwester, backen, husten ...) wurden direkt ihrem thematischen Feld zugeordnet (Wohnung, Verkehr, Gesundheit, Essen, ...).

**Iteration ueber den Rest:** Nach der ersten Zuordnungsrunde blieben drei grosse Restgruppen uebrig, die kein offensichtliches Sachfeld haben. Fuer jede wurde eine eigene, in sich kohaerente Sammelkategorie geschaffen statt einer beliebigen Restekiste:

- **Glue-Woerter (Grammatik & Funktionswoerter)** — Pronomen, Praepositionen, Konjunktionen, Modalverben, Partikeln (aber, weil, vielleicht, sehr, schon, der/die/das, ...). Diese Woerter tauchen als Bindegewebe in JEDER Szene auf; damit trotzdem jedes einzelne Wort einen eigenen Merk-Anker bekommt, sind sie hier in eigene kleine Dialog-/Alltagsszenen gruppiert (siehe Abschnitt 4, Thema 'Glue-Woerter'), die bewusst als Sprech-Situationen (Streit, Small Talk, Durchsage, Verhoer) angelegt sind, in denen genau diese Konnektoren natuerlich vorkommen.

- **Denken, Meinung & abstrakte Begriffe** — Verben und Nomen der Kognition, Bewertung, Kausalitaet und Bürokratiesprache (bedeuten, sich entscheiden, Ursache, Zusammenhang, Voraussetzung, vermutlich, ...). Das ist keine Restekiste, sondern ein eigenes, im B1-Wortschatz sehr grosses und wiederkehrendes semantisches Feld: Meinungsaeusserung, Begruendung und Abwaegen sind Kernkompetenzen auf B1-Niveau. Die Szenen dieses Themas verankern die Abstraktion jeweils in einer konkreten Situation (Gerichtssaal, Streit am Kuechentisch, Wissenschaftsvortrag), damit die Woerter trotzdem bildhaft bleiben.

- **Alltagshandlungen (allgemeine Verben)** — thematisch neutrale Hochfrequenzverben (machen, gehen, nehmen, legen, holen, ...), die in praktisch jeder Szene als Traeger-Verben gebraucht werden. Auch sie bekommen eigene Szenen, damit sie nicht 'unsichtbar' im Hintergrund anderer Themen verschwinden.

**Eigenschaften (Adjektive) und Menge/Vergleich** wurden ebenfalls als eigene Themen belassen statt auf Sachfelder verteilt, weil viele B1-Adjektive/Mengenwoerter (schlimm, gemuetlich, ungefaehr, mehrere, doppelt) fach-uebergreifend sind und sich am besten in Bewertungs- bzw. Vergleichs-Szenen einpraegen.

## 3. Coverage-Audit (Python-verifiziert)

Jede der 2.886 Zeilen der Wortliste wurde per Python-Skript genau einem der 25 Themen zugeordnet (Zuordnung ueber `row_index -> topic_code`, nicht ueber Fuzzy-String-Matching). Die Vereinigung aller Themen-Zeilen wurde gegen die vollstaendige Zeilenmenge der geparsten CSV abgeglichen.

- Zeilen in der Wortliste (Header-Zeile ausgenommen): **2886**
- Zeilen mit Themen-Zuordnung: **2886**
- Nicht zugeordnete Zeilen: **0**

**Keine nicht zugeordneten Zeilen — Coverage 100% ist Python-bestaetigt.**

## 4. Themen mit vollstaendigen Wortlisten & Szenen-Outlines

### Glue-Wörter: Grammatik & Funktionswörter  *(n=194)*

_Pronomen, Präpositionen, Konjunktionen, Modalverben, Partikeln — das Bindegewebe jedes Satzes._

**Scenes: 15**

**Szene G-1** (13 Woerter)
- Prämise: Zwei WG-Mitbewohner streiten sich beim Frühstück darüber, wer zuletzt eingekauft hat.
- Komischer Dreh: Der Streit eskaliert zu einer absurd pedantischen Grammatikdebatte, bei der jeder Satz mit einem anderen Bindewort neu formuliert werden muss, bevor er zählt.
- Zielwoerter: ab, aber, all-, aller-, allerdings, als, als ob, also, an, ander-, andererseits, anders, auch

**Szene G-2** (13 Woerter)
- Prämise: Ein Straßenumfrage-Reporter hält wahllos Passanten das Mikro hin und fragt nach ihrer Meinung zu allem und nichts.
- Komischer Dreh: Die Befragten antworten nur noch in unvollständigen Halbsätzen voller Konjunktionen, sodass niemand je einen Gedanken zu Ende bringt.
- Zielwoerter: auf, aus, ausschließlich, außer, außerdem, bei, beid-, beinahe, bevor, bis, bitte, bloß, dabei

**Szene G-3** (13 Woerter)
- Prämise: Ein Kind übt für ein Schultheaterstück und muss jede Zeile mit einem Füllwort beginnen.
- Komischer Dreh: Das Stück wird immer länger und unfreiwillig komischer, weil das Kind auch mitten im Satz neue Füllwörter einbaut.
- Zielwoerter: dafür, dagegen, daher, die Dame, damit, danke, dass, denn, derselbe, deshalb, deswegen, dies-, doch

**Szene G-4** (13 Woerter)
- Prämise: Ein Ehepaar plant am Küchentisch mit einem Wandkalender die nächste Woche.
- Komischer Dreh: Jeder Programmpunkt wird durch ein 'aber', 'obwohl' oder 'falls' sofort wieder infrage gestellt, sodass am Ende gar nichts geplant ist.
- Zielwoerter: durch, dürfen, eben, ebenfalls, ebenso, egal, eher, eigen-, eigentlich, ein-, einerseits, einig-, einschließlich

**Szene G-5** (13 Woerter)
- Prämise: Ein Roboter-Assistent wurde nur mit Grammatikregeln, aber ohne Wortschatz programmiert.
- Komischer Dreh: Er spricht in perfekt korrekten, aber komplett inhaltsleeren Sätzen voller Pronomen und Präpositionen, was seine Besitzer zur Verzweiflung treibt.
- Zielwoerter: entweder ... oder, es, etwas, eventuell, extra, falls, fast, für, gar, gegen, genauso, gleich, gleichfalls

**Szene G-6** (13 Woerter)
- Prämise: Zwei Freunde spielen ein Ratespiel, bei dem man nur mit Fragewörtern kommunizieren darf.
- Komischer Dreh: Das Spiel wird zum absurden Verhör, weil keiner je eine echte Antwort geben darf.
- Zielwoerter: haben, hallo, halt, heißen, her/her-, heraus-, herein-, der Herr, herunter-, in, indem, inklusive, irgendirgendein

**Szene G-7** (13 Woerter)
- Prämise: Ein Anrufbeantworter-Ansagentext wird von einem gestressten Praktikanten neu aufgenommen.
- Komischer Dreh: Er verhaspelt sich ständig bei den Höflichkeitsfloskeln und produziert immer wildere, unfreiwillig komische Satzkonstruktionen.
- Zielwoerter: ja, je, je … desto …, jeder, jedoch, jemand, jeweils, kaum, kein-, können, lassen, los/los-, mal

**Szene G-8** (13 Woerter)
- Prämise: Beim Familienessen erzählt der Opa eine Geschichte, die er dauernd mit Rückblenden unterbricht.
- Komischer Dreh: Die Rückblenden brauchen selbst wieder Rückblenden, bis niemand mehr weiß, in welcher Zeitform gerade erzählt wird.
- Zielwoerter: man, manch-, meinetwegen, miss-, mit, miteinander, möchten, mögen, möglichst, müssen, nach, nachdem, nämlich

**Szene G-9** (13 Woerter)
- Prämise: Ein Deutschlehrer testet seine Klasse mit einem Lückentext, bei dem nur Funktionswörter fehlen.
- Komischer Dreh: Ein Schüler füllt bewusst alle Lücken mit demselben albernen Wort, was den ganzen Text unfreiwillig komisch macht.
- Zielwoerter: natürlich, nebenbei, nein, nicht, nichts, niemand, noch, noch mal, nochmals, normalerweise, nur, ob, obwohl

**Szene G-10** (13 Woerter)
- Prämise: Zwei Nachbarn tauschen über den Gartenzaun Neuigkeiten aus, die keiner wirklich hören will.
- Komischer Dreh: Das Gespräch wird zur Materialschlacht aus Konjunktionen, weil beide krampfhaft im Gespräch bleiben wollen.
- Zielwoerter: oder, ohne, per, Prost, recht, sehr, sein, seit, seitdem, selb-, selbst, selber, selbstverständlich

**Szene G-11** (13 Woerter)
- Prämise: Ein Zug-Schaffner übt seine Durchsagen vor dem Badezimmerspiegel.
- Komischer Dreh: Er verwechselt ständig Richtungswörter, sodass die Durchsage die Fahrgäste in die völlig falsche Richtung schickt.
- Zielwoerter: so, sobald, sodass, sogenannt-, sogar, solange, solch-, sollen, sondern, sonst, soviel, so viel/so viel wie, sowieso

**Szene G-12** (13 Woerter)
- Prämise: Ein Liebespaar schreibt sich zum ersten Mal SMS und ist furchtbar unsicher in der Wortwahl.
- Komischer Dreh: Jede Nachricht wird vor dem Absenden zehnmal mit anderen Konjunktionen umformuliert, bis die eigentliche Frage komplett verloren geht.
- Zielwoerter: sowohl … als auch, statt, trotz, trotzdem, über, überhaupt, übrigens, um, um … zu, umso, un-, unbedingt, und

**Szene G-13** (13 Woerter)
- Prämise: Ein Zeuge wird von der Polizei zu einem harmlosen Vorfall befragt.
- Komischer Dreh: Seine Aussage besteht nur aus vagen Pronomen ('der', 'die', 'irgendwer'), sodass der Polizist komplett verzweifelt.
- Zielwoerter: unter, vielleicht, von, voneinander, vor, vor allem, während, wann, warum, was, was für ein-, weder … noch, wegen

**Szene G-14** (13 Woerter)
- Prämise: Ein Comedian testet neues Material, das komplett aus Alltagsfloskeln besteht.
- Komischer Dreh: Das Publikum lacht nur, weil die Floskeln so banal aneinandergereiht werden, dass es wie absurdes Theater wirkt.
- Zielwoerter: weil, -weise, weiter/weiter-, welcher, wenn, wer, werden, weshalb, wie, wieder/wieder-, wieso, wie viel, wirklich

**Szene G-15** (12 Woerter)
- Prämise: Ein Vater erklärt seinem Kind zum ersten Mal, wie man einen Drachen steigen lässt.
- Komischer Dreh: Die Anleitung wird immer verwirrender, weil er ständig Richtungs- und Zeitangaben durcheinanderbringt.
- Zielwoerter: wo, woher, wohin, wohl, wollen, worüber, worum, zu, zumindest, zusammen/zusammen-, zwar, zwischen


### Denken, Meinung & abstrakte Begriffe  *(n=294)*

_Nachdenken, Entscheiden, Meinen, Ursache/Wirkung, Bedeutung, Bürokratie-Sprache._

**Scenes: 23**

**Szene Ab-1** (13 Woerter)
- Prämise: Ein Philosophie-Stammtisch in der Eckkneipe diskutiert jeden Donnerstag über den Sinn des Lebens.
- Komischer Dreh: Die Diskussion wird immer abstrakter, bis am Ende niemand mehr weiß, worüber ursprünglich gestritten wurde.
- Zielwoerter: abhängen, abhängig, ablehnen, abmachen, der Abschnitt, die Absicht, achten, die Ahnung, die Aktion, akzeptieren, alternativ, die Alternative, analysieren

**Szene Ab-2** (13 Woerter)
- Prämise: Eine Wissenschaftlerin hält vor gelangweilten Studierenden einen Vortrag über Ursache und Wirkung.
- Komischer Dreh: Sie beweist ihre These ausgerechnet mit dem chaotischsten Alltagsbeispiel, das ihr spontan einfällt.
- Zielwoerter: ändern, die Änderung, anerkennen, angeben, die Angabe, die Anlage, annehmen, ansehen, ansprechen, sich anstrengen, anwenden, die Art, auffallen

**Szene Ab-3** (13 Woerter)
- Prämise: Zwei Detektive besprechen in einem Großraumbüro einen kniffligen Fall.
- Komischer Dreh: Ihre Theorien widersprechen sich ständig, und jede neue Idee wird sofort wieder verworfen.
- Zielwoerter: auffordern, die Aufforderung, aufgeben, aufhalten, auflösen, die Ausnahme, ausschließen, beachten, bedeuten, die Bedeutung, die Bedingung, begründen, die Begründung

**Szene Ab-4** (13 Woerter)
- Prämise: Ein Ehepaar berät am Küchentisch stundenlang über eine wichtige Entscheidung.
- Komischer Dreh: Sie wägen so viele Für und Wider ab, dass am Ende die ursprüngliche Frage komplett vergessen ist.
- Zielwoerter: behalten, behaupten, behindern, das Beispiel, der Beitrag, bekannt, bemerken, sich bemühen, beobachten, der Bereich, beschließen, sich beteiligen, beweisen

**Szene Ab-5** (13 Woerter)
- Prämise: Ein Amtsschreiben voller Fachbegriffe soll von einer Bürgerin verstanden werden.
- Komischer Dreh: Sie liest den Text laut vor und übersetzt ihn absurd wörtlich, bis er völlig sinnfrei klingt.
- Zielwoerter: der Beweis, der Blick, die Chance, darstellen, die Darstellung, denken, der Gedanke, das Detail, dienen, das Ding, sich eignen, der Eindruck, einfallen

**Szene Ab-6** (13 Woerter)
- Prämise: Ein Uni-Seminar diskutiert, ob eine Behauptung wahr oder bloß plausibel ist.
- Komischer Dreh: Ein Student widerspricht grundsätzlich allem, nur um am Ende festzustellen, dass er selbst nichts mehr glaubt.
- Zielwoerter: der Einfall, der Einfluss, beeinflussen, sich einigen, einverstanden, die Einzelheit, empfehlen, die Empfehlung, entdecken, enthalten, entscheiden, die Entscheidung, unentschieden

**Szene Ab-7** (13 Woerter)
- Prämise: Ein Coach hält einen Motivationsvortrag über Ziele und Absichten.
- Komischer Dreh: Seine Beispiele werden immer übertriebener, bis das Publikum nicht mehr weiß, ob er es ernst meint.
- Zielwoerter: sich entschließen, entstehen, entwickeln, die Entwicklung, das Ereignis, sich ereignen, erfahren, die Erfahrung, erfinden, die Erfindung, erforderlich, erfordern, erfüllen

**Szene Ab-8** (13 Woerter)
- Prämise: Zwei Kollegen bereiten eine Präsentation über ein kompliziertes Projekt vor.
- Komischer Dreh: Sie erklären sich gegenseitig denselben Sachverhalt so oft neu, dass am Ende beide völlig verwirrt sind.
- Zielwoerter: das Ergebnis, erinnern, die Erinnerung, erkennen, erlauben, erreichen, ersetzen, der Ersatz, erstellen, erwarten, die Fähigkeit, der Faktor, der Fall

**Szene Ab-9** (13 Woerter)
- Prämise: Ein Kind fragt den Großvater unaufhörlich 'Warum?' zu jedem Satz, den er sagt.
- Komischer Dreh: Die Erklärungen werden mit jeder Antwort abstrakter und absurder, bis der Großvater bei der Quantenphysik landet.
- Zielwoerter: fehlen, der Fehler, festlegen, festsetzen, feststehen, feststellen, finden, folgen, die Folge, folgend, fordern, die Forderung, fördern

**Szene Ab-10** (13 Woerter)
- Prämise: Eine Gerichtsverhandlung dreht sich um eine winzige, fast bedeutungslose Streitfrage.
- Komischer Dreh: Anwalt und Richter analysieren das Problem mit solcher Ernsthaftigkeit, dass die Lächerlichkeit der Sache immer deutlicher wird.
- Zielwoerter: die Förderung, der Fortschritt, fortsetzen, die Fortsetzung, die Freiheit, geeignet, der Gegensatz, der Gegenstand, das Gegenteil, das Geheimnis, geheim, gehören, die Gelegenheit

**Szene Ab-11** (13 Woerter)
- Prämise: Ein Ratgeberbuch verspricht, jedes Problem in drei einfachen Schritten zu lösen.
- Komischer Dreh: Die Beispiele im Buch sind so widersprüchlich, dass die Leserin am Ende mehr Zweifel als vorher hat.
- Zielwoerter: gelingen, gelten, gerecht, geschehen, gewöhnen, die Gewohnheit, gewohnt, gewöhnlich, glauben, der Grund, die Gruppe, heimlich, die Herausforderung

**Szene Ab-12** (13 Woerter)
- Prämise: Zwei Freunde vergleichen ihre gegensätzlichen Meinungen zu einem Filmklassiker.
- Komischer Dreh: Die Diskussion wird zum absurden Grundsatzstreit über Kunst, Wahrheit und den Sinn des Lebens.
- Zielwoerter: die Idee, der Inhalt, sich irren, klappen, klären, klingen, der Kompromiss, der Konflikt, die Krise, kritisieren, die Kritik, kritisch, die Liste

**Szene Ab-13** (13 Woerter)
- Prämise: Ein Unternehmensberater erklärt dem Chef mit vielen Fachbegriffen, warum die Firma umstrukturiert werden muss.
- Komischer Dreh: Am Ende stellt sich heraus, dass sein Vorschlag im Kreis herum wieder beim Ist-Zustand landet.
- Zielwoerter: lösen, die Lösung, meinen, die Meinung, merken, die Methode, das Mittel, das Modell, möglich, die Möglichkeit, die Mühe, nachdenken, der Nachteil

**Szene Ab-14** (13 Woerter)
- Prämise: Ein Ehepaar streitet sich, wer schuld an der verpassten Deadline ist.
- Komischer Dreh: Beide führen so viele Gründe und Ausreden an, dass die eigentliche Ursache völlig unklar bleibt.
- Zielwoerter: nötig, notwendig, nützlich, offenbar, die Ordnung, organisieren, die Organisation, das Original, original, passieren, persönlich, die Pflicht, planen

**Szene Ab-15** (13 Woerter)
- Prämise: Eine Journalistin recherchiert einen Skandal und stößt auf immer neue Widersprüche.
- Komischer Dreh: Jede neue Spur widerlegt die vorherige Theorie, bis der Artikel nur noch aus Fragezeichen besteht.
- Zielwoerter: der Plan, die Planung, das Problem, der Punkt, die Qualität, raten, der Rat, Ratschlag, realisieren, die Realität, realistisch, die Regel, regeln

**Szene Ab-16** (13 Woerter)
- Prämise: Ein Lehrer erklärt der Klasse den Unterschied zwischen Tatsache und Meinung.
- Komischer Dreh: Ein Schüler behauptet stur, seine Meinung sei eine Tatsache, und die Diskussion eskaliert herrlich kleinlich.
- Zielwoerter: die Sache, schaffen, schätzen, die Schuld, schuld, schuldig, die Schwierigkeit, die Seite, sichtbar, der Sinn, sinnlos, sinnvoll, die Situation

**Szene Ab-17** (13 Woerter)
- Prämise: Ein Start-up-Gründer präsentiert Investoren eine vage Geschäftsidee mit vielen großen Wörtern.
- Komischer Dreh: Je mehr Nachfragen kommen, desto mehr Fachbegriffe erfindet er spontan, um keine echte Antwort geben zu müssen.
- Zielwoerter: der Standpunkt, die Statistik, statistisch, stilistisch, stimmen, das Symbol, das System, die Tabelle, das Talent, die Tatsache, tatsächlich, das Thema, theoretisch

**Szene Ab-18** (13 Woerter)
- Prämise: Zwei Nachbarinnen diskutieren, ob ihr Streit über den Gartenzaun eine Ausnahme oder die Regel ist.
- Komischer Dreh: Sie ziehen immer abwegigere Vergleiche heran, um ihre jeweilige Position zu rechtfertigen.
- Zielwoerter: die Theorie, der Tipp, überlegen, überprüfen, (sich) überzeugen, die Überzeugung, üblich, die Umfrage, unterlassen, unterscheiden, der Unterschied, unterschiedlich, die Ursache

**Szene Ab-19** (13 Woerter)
- Prämise: Ein Psychologe testet in einer Sendung, wie Zuschauer Entscheidungen unter Druck treffen.
- Komischer Dreh: Die Kandidaten begründen ihre absurden Entscheidungen mit immer abenteuerlicheren Theorien.
- Zielwoerter: verursachen, (sich) verändern, vergeblich, vergessen, vergleichen, der Vergleich, verhindern, verlangen, verlieren, der Verlust, vermeiden, vermuten, vermutlich

**Szene Ab-20** (13 Woerter)
- Prämise: Eine Bürgerversammlung debattiert stundenlang über eine banale Verwaltungsfrage.
- Komischer Dreh: Am Ende hat sich die Diskussion so verselbstständigt, dass niemand mehr weiß, was überhaupt beschlossen werden sollte.
- Zielwoerter: verpflichtet, verschieden, verschwinden, versprechen, verständlich, das Verständnis, (sich) verstehen, versuchen, der Versuch, verwechseln, verzichten, die Voraussetzung, (sich) vorbereiten

**Szene Ab-21** (13 Woerter)
- Prämise: Ein Behördenformular verlangt eine schriftliche Begründung für einen völlig harmlosen Antrag.
- Komischer Dreh: Der Antragsteller schreibt eine immer philosophischere Begründung, die mit dem eigentlichen Anliegen kaum noch etwas zu tun hat.
- Zielwoerter: die Vorbereitung, vorkommen, vorschlagen, der Vorschlag, (sich) vorstellen, die Vorstellung, der Vorteil, wahr, die Wahrheit, wahrscheinlich, sich weigern, wichtig, widersprechen

**Szene Ab-22** (13 Woerter)
- Prämise: Zwei Wissenschaftler streiten in der Kantine über die Bedeutung eines Versuchsergebnisses.
- Komischer Dreh: Beide interpretieren dieselben Zahlen komplett gegensätzlich und werden dabei zunehmend lauter.
- Zielwoerter: wirken, die Wirkung, die Wirklichkeit, wissen, das Wissen, das Wunder, das Zeichen, das Zeug/-zeug, das Ziel, der Zufall, zufällig, zurechtkommen, zusagen

**Szene Ab-23** (8 Woerter)
- Prämise: Ein Chef erklärt seinem Team in einem endlosen Meeting die neue Unternehmensstrategie.
- Komischer Dreh: Die Erklärung besteht nur aus vagen Absichtserklärungen, sodass am Ende niemand weiß, was konkret zu tun ist.
- Zielwoerter: der Zusammenhang, der Zustand, zustimmen, die Zustimmung, der Zweck, zweifeln, der Zweifel, (sich) zwingen


### Kommunikation, Medien & Technik  *(n=202)*

_Telefon, Internet, Post, Zeitung, Geräte._

**Scenes: 16**

**Szene C-1** (13 Woerter)
- Prämise: Eine Familie versucht gemeinsam, den neuen WLAN-Router einzurichten.
- Komischer Dreh: Jeder gibt widersprüchliche Anweisungen aus einer anderen Anleitung, und am Ende funktioniert nur noch der Toaster.
- Zielwoerter: abonnieren, das Abonnement, der Absender, die Absenderin, die Adresse, anklicken, ankündigen, die Anleitung, die Annonce, die Anrede, anrufen, der Anruf, der Anrufbeantworter

**Szene C-2** (13 Woerter)
- Prämise: Ein Callcenter-Mitarbeiter nimmt Anrufe von zunehmend verzweifelten Kunden entgegen.
- Komischer Dreh: Die Warteschleifenmusik wird so nervig, dass selbst der Mitarbeiter am Ende mitsingt, statt zu helfen.
- Zielwoerter: die Ansage, anschließen, antworten, die Antwort, der Apparat, der Artikel, aufladen, aufnehmen, die Aufnahme, ausdrucken, der Ausdruck, die Auskunft, ausrichten

**Szene C-3** (13 Woerter)
- Prämise: Eine Postbotin sortiert in aller Frühe Briefe und Pakete für ihren Bezirk.
- Komischer Dreh: Ein Umschlag ist so falsch adressiert, dass sie eine kleine Detektivgeschichte braucht, um den Empfänger zu finden.
- Zielwoerter: der Autor, die Autorin, die Batterie, beantworten, die Bedienungsanleitung, begrüßen, bekannt geben, berichten, der Bericht, der Bescheid, Bescheid sagen, Bescheid geben, beschreiben

**Szene C-4** (13 Woerter)
- Prämise: Zwei Freundinnen verabreden sich nur über eine Kette missverständlicher Textnachrichten.
- Komischer Dreh: Jede Nachricht wird völlig anders verstanden als gemeint, bis am Ende drei verschiedene Treffen an drei Orten geplant sind.
- Zielwoerter: die Beschreibung, besprechen, bestätigen, die Bestätigung, der Bildschirm, bitten, die Bitte, die Botschaft, der Brief, der Briefkasten, die Briefmarke, der Briefträger, der Briefumschlag

**Szene C-5** (13 Woerter)
- Prämise: Ein Lokalreporter interviewt Passanten für die Abendnachrichten zu einem Alltagsthema.
- Komischer Dreh: Die Antworten werden so ausschweifend, dass der Bericht am Ende nur noch aus Zwischenrufen des genervten Kameramanns besteht.
- Zielwoerter: die Broschüre, das Couvert, die Datei, die Daten, der Dialog, digital, diskutieren, die Diskussion, drucken, der Drucker, der Druck, die Durchsage, duzen

**Szene C-6** (13 Woerter)
- Prämise: Ein Großvater bekommt sein erstes Smartphone geschenkt und ruft ständig aus Versehen jemanden an.
- Komischer Dreh: Er hält jedes Klingeln für einen Notfall und schreit ins Telefon, bevor überhaupt jemand rangeht.
- Zielwoerter: einfügen, einschalten, das Einschreiben, elektrisch, Elektro-, elektronisch, empfangen, der Empfang, der Empfänger, erklären, die Erklärung, sich erkundigen, erzählen

**Szene C-7** (13 Woerter)
- Prämise: Ein Büroangestellter druckt ein wichtiges Dokument aus, doch der Drucker spinnt.
- Komischer Dreh: Am Ende druckt das Gerät fünfzig leere Seiten und eine einzige, völlig zerknitterte Kopie.
- Zielwoerter: die Erzählung, die Fernbedienung, fernsehen, das Fernsehen, der Fernseher, die Festplatte, das Forum, fragen, die Frage, funktionieren, die Gebrauchsanweisung, geehrt, das Gerät

**Szene C-8** (13 Woerter)
- Prämise: Ein Radiosender sendet eine Live-Verkehrsdurchsage, während im Studio alles schiefgeht.
- Komischer Dreh: Der Moderator improvisiert immer wildere Ausreden für die technischen Pannen im Hintergrund.
- Zielwoerter: das Gespräch, die Grafik, grüßen, der Gruß, das Handy, (herunter-)fahren, hinterlassen, hinweisen, der Hinweise, hochladen, hören, der Hörer, die Hörerin

**Szene C-9** (13 Woerter)
- Prämise: Ein Zeitungsredakteur muss eine Schlagzeile in letzter Minute umschreiben.
- Komischer Dreh: Jede neue Version wird reißerischer, bis die Überschrift mit der eigentlichen Nachricht kaum noch etwas zu tun hat.
- Zielwoerter: der Zuhörer, informieren, die Information, das Inserat, installieren, das Interview, das Kabel, der Kanal, die Kassette, klicken, der Klick, klingeln, die Kommunikation

**Szene C-10** (13 Woerter)
- Prämise: Ein Techniker installiert in einem Altersheim das erste Internet.
- Komischer Dreh: Die Bewohner sind begeistert, verwechseln aber ständig Videoanruf und Fernseher.
- Zielwoerter: kopieren, die Kopie, der Kopierer, das Kuvert, das Laufwerk, der Lautsprecher, löschen, das Magazin, die Maschine, die Medien, melden, die Meldung, mitteilen

**Szene C-11** (13 Woerter)
- Prämise: Eine Studentin schreibt eine Bewerbungs-E-Mail und liest sie zwanzigmal Korrektur.
- Komischer Dreh: Bei jedem Lesen ändert sie die Anrede, bis die E-Mail absurd förmlich klingt.
- Zielwoerter: mobil/mobil-, die Mobilbox, das Mobiltelefon, der Monitor, die Nachricht, nennen, das Netz, das Netzwerk, die Neuigkeit, notieren, die Notiz, die Nummer, veröffentlichen

**Szene C-12** (13 Woerter)
- Prämise: Ein Ehepaar telefoniert aus dem Urlaub mit dem Nachbarn, der auf die Wohnung aufpasst.
- Komischer Dreh: Die Verbindung ist so schlecht, dass jede zweite Anweisung völlig falsch ankommt.
- Zielwoerter: das Paket, das Plakat, die Post, die Postleitzahl, die Presse, das Programm, das Radio, die Recherche, der Rechner, reden, die Rede, die Reklame, die Reportage

**Szene C-13** (13 Woerter)
- Prämise: Ein Museum stellt seine erste digitale Zeitschrift für Besucher vor.
- Komischer Dreh: Der Programmierer hat versehentlich Kunstwerke mit Fantasienamen und übertriebenen Beschreibungen versehen.
- Zielwoerter: der Reporter, die Reporterin, rufen, die Rufnummer, sagen, schalten, schicken, schreiben, aufschreiben, das Schreiben, die Schrift, schriftlich, schweigen

**Szene C-14** (13 Woerter)
- Prämise: Ein Nachbar klopft an, um sich beim Nachbarn über den Fernseherlärm zu beschweren.
- Komischer Dreh: Statt sich zu beschweren, bleibt er stundenlang zum Fernsehen sitzen und vergisst den eigentlichen Grund des Besuchs.
- Zielwoerter: senden, der Sender, die Sendung, (sich) siezen, speichern, sprechen, die Steckdose, der Stecker, die Stimme, die Störung, die Tastatur, die Taste, die Technik

**Szene C-15** (13 Woerter)
- Prämise: Ein Radiomoderator liest live Hörerfragen vor, die per SMS eingehen.
- Komischer Dreh: Die Fragen werden immer kurioser, und er muss live improvisierte Antworten erfinden.
- Zielwoerter: technisch, die Technologie, telefonieren, das Telefon, der Text, tippen, die Überschrift, unterbrechen, (sich) unterhalten, verbinden, die Verbindung, der Verlag, verraten

**Szene C-16** (7 Woerter)
- Prämise: Ein Sekretariat übersetzt spontan ein wichtiges Schreiben für einen ausländischen Geschäftspartner.
- Komischer Dreh: Die Übersetzung wird Wort für Wort so wörtlich, dass am Ende ein völlig anderer Text entsteht.
- Zielwoerter: das Video, virtuell, die Vorwahl, die Zeitschrift, die Zeitung, zuhören, die Zuhörerin


### Essen, Trinken & Kochen  *(n=172)*

_Lebensmittel, Gerichte, Restaurant, Kochen, Geschmack._

**Scenes: 13**

**Szene E-1** (13 Woerter)
- Prämise: Ein Hobbykoch versucht zum ersten Mal, ein Familienrezept seiner Großmutter nachzukochen.
- Komischer Dreh: Er verwechselt Zutaten und Mengenangaben so gründlich, dass am Ende ein völlig neues, unbenennbares Gericht entsteht.
- Zielwoerter: der Alkohol, der Apfel, der Appetit, die Aprikose, backen, die Bäckerei, die Banane, bestellen, betrunken, das Bier, Bio-, bio, die Birne

**Szene E-2** (13 Woerter)
- Prämise: Ein überfülltes Restaurant hat an einem Samstagabend nur einen einzigen Kellner im Dienst.
- Komischer Dreh: Der Kellner bringt aus reiner Verzweiflung allen Gästen zufällige Gerichte, egal was sie bestellt hatten.
- Zielwoerter: bitter, die Bohne, braten, der Braten, das Brot, das Brötchen, das Brötli, die Büchse, das Buffet, die Butter, das Café, die Cafeteria, das Dessert

**Szene E-3** (13 Woerter)
- Prämise: Eine Familie plant einen Grillabend im Garten, doch das Wetter macht nicht mit.
- Komischer Dreh: Sie grillen trotzdem tapfer unter einem viel zu kleinen Regenschirm, während alles langsam durchweicht.
- Zielwoerter: die Diät, die Dose, das Ei, das Eis, der Erdapfel, ernähren, die Ernährung, essen, das Essen, der Essig, das Faschierte, fett, das Fett

**Szene E-4** (13 Woerter)
- Prämise: Ein Kind hilft zum ersten Mal beim Backen und nimmt jede Anweisung wörtlich.
- Komischer Dreh: Es verteilt Zucker, Mehl und Gewürze in absurden Mengen über die ganze Küche.
- Zielwoerter: die Flasche, das Fleisch, die Flüssigkeit, frisch, die Frucht, Früchte, frühstücken, das Frühstück, die Gabel, der Gast, das Gasthaus, die Gaststätte, das Gebäck

**Szene E-5** (13 Woerter)
- Prämise: Zwei Freunde eröffnen für einen Tag einen Imbissstand auf dem Flohmarkt.
- Komischer Dreh: Ihre selbst erfundene Speisekarte wird immer skurriler, weil sie improvisieren müssen, was der Kühlschrank hergibt.
- Zielwoerter: das Gemüse, das Gericht, der Geschmack, das Getränk, das Gewürz, die/das Glace/Glacé, das Glas, grillen, grillieren, der Grill, das Hackfleisch, das Hähnchen/Hühnchen, haltbar

**Szene E-6** (13 Woerter)
- Prämise: Eine Diät-Beraterin erklärt einem widerwilligen Kunden strenge Ernährungsregeln.
- Komischer Dreh: Der Kunde schmuggelt heimlich Süßigkeiten in jede Mahlzeit, die sie ihm vorschreibt.
- Zielwoerter: das Hend(e)l, der Honig, der Imbiss, die Jause, der Kaffee, das Kaffeehaus, der Kakao, die Kanne, die Kantine, die Karotte, die Kartoffel, der Käse, der Kloß

**Szene E-7** (13 Woerter)
- Prämise: Ein Ehepaar isst zum Jahrestag in einem übertrieben edlen Restaurant.
- Komischer Dreh: Sie verstehen die winzigen Portionen und die Speisekarte voller Fachbegriffe überhaupt nicht und bestellen aus Verlegenheit alles doppelt.
- Zielwoerter: der Knödel, kochen, der Koch, die Köchin, die Konfitüre, der Kuchen, lecker, die Lebensmittel, die Limonade, der Löffel, das Lokal, die Mahlzeit, die Margarine

**Szene E-8** (13 Woerter)
- Prämise: Ein Gastwirt bereitet sich auf eine überraschende Lebensmittelkontrolle vor.
- Komischer Dreh: In der Panik versteckt er improvisierte Zutaten an den unmöglichsten Orten der Küche.
- Zielwoerter: die Marille, die Marmelade, das Mehl, die Mensa, das Menü, das Messer, die Milch, das Mineralwasser, mischen, die Möhre, das Müesli/Müsli, die Nachspeise, das Nahrungsmittel

**Szene E-9** (13 Woerter)
- Prämise: Eine Studenten-WG kocht am Monatsende nur noch aus Resten im Kühlschrank.
- Komischer Dreh: Das Ergebnis ist ein absurdes Gericht, das trotzdem überraschend gut schmeckt und zur Legende der WG wird.
- Zielwoerter: die Nudel, das/der (Schlag-)Obers, das Obst, das Öl, die Orange, der Paradeiser, die Pfanne, der Pfeffer, die Pflaume, der Pilz, die Pizza, die Pommes frites, die Portion

**Szene E-10** (13 Woerter)
- Prämise: Ein Marktstand verkauft an einem heißen Sommertag Obst und Gemüse.
- Komischer Dreh: Der Verkäufer ruft immer übertriebenere Werbesprüche, um die schmelzende Ware noch loszuwerden.
- Zielwoerter: das Poulet, probieren, der (Schlag-)Rahm, reif, der Reis, das Restaurant, das Rezept, das Rind, roh, das Rüebli, der Saft, die (Schlag-)Sahne, der Salat

**Szene E-11** (13 Woerter)
- Prämise: Ein Frühstücksbuffet im Hotel wird von hungrigen Kindern regelrecht gestürmt.
- Komischer Dreh: Ein Junge stapelt so viel auf seinen Teller, dass der Turm mitten im Speisesaal zusammenbricht.
- Zielwoerter: das Salz, salzig, satt, sauer, scharf, die Scheibe, der Schinken, der/das (Schlag-)Obers, schmecken, das Schnitzel, die Schokolade, die Schüssel, das Schwammerl

**Szene E-12** (13 Woerter)
- Prämise: Ein Kellner muss einem ausländischen Gast die komplette Speisekarte auf Deutsch erklären.
- Komischer Dreh: Seine Übersetzungsversuche werden immer kreativer und ungenauer, bis der Gast aus Verzweiflung einfach alles bestellt.
- Zielwoerter: die Semmel, der Service, die Soße/Sauce, Speise-/-speise, die Speisekarte, die Suppe, süß, die Tasse, der Tee, Tee ziehen lassen, der Teller, die Tomate, der Topf

**Szene E-13** (16 Woerter)
- Prämise: Ein Kochkurs für Anfänger endet in völligem Küchenchaos.
- Komischer Dreh: Jeder Teilnehmer kocht ein anderes Gericht als geplant, weil alle die Zutaten durcheinandergebracht haben.
- Zielwoerter: die Torte, trinken, das Trinkgeld, vegetarisch, verpflegen, das Wasser, der Wein, der Wirt, die Wirtin, die Wurst, die Zitrone, zubereiten, der Zucker, die Zutaten, das/der Zvieri/Znüni, die Zwiebel


### Gefühle & Charakter  *(n=159)*

_Emotionen, Persönlichkeitseigenschaften, zwischenmenschliches Verhalten._

**Scenes: 12**

**Szene Ge-1** (13 Woerter)
- Prämise: Ein Therapeut leitet eine Selbsthilfegruppe, in der jeder sein größtes Gefühl schauspielern muss.
- Komischer Dreh: Die Übung eskaliert, weil ein Teilnehmer seine Wut so übertrieben darstellt, dass alle anderen anstecken lachen müssen.
- Zielwoerter: allein, angenehm, die Angst, ängstlich, (sich) ärgern, der Ärger, ärgerlich, aufmerksam, aufpassen, aufregen, sich bedanken, begeistert, beleidigen

**Szene Ge-2** (13 Woerter)
- Prämise: Zwei beste Freunde versöhnen sich nach einem albernen Streit über Kleinigkeiten.
- Komischer Dreh: Ihre Entschuldigungen werden immer dramatischer, bis daraus eine komplette Kitsch-Filmszene mitten auf der Straße wird.
- Zielwoerter: beliebt, beruhigen, böse, danken, der Dank, dankbar, ehrlich, einsam, entgegenkommen, entschlossen, entschuldigen, die Entschuldigung, entspannend

**Szene Ge-3** (13 Woerter)
- Prämise: Eine Familie überrascht die Oma mit einer riesigen Geburtstagsparty.
- Komischer Dreh: Die Überraschung schlägt fehl, weil die Oma es längst geahnt hatte und selbst die Kuchenlieferung organisiert hat.
- Zielwoerter: enttäuschen, die Enttäuschung, erleichtern, ernst, ernsthaft, erschrecken, fair, faul, fleißig, frech, freiwillig, fremd, sich freuen

**Szene Ge-4** (13 Woerter)
- Prämise: Ein schüchterner Mann übt vor dem Spiegel, wie er jemanden um ein Date bittet.
- Komischer Dreh: Jeder Übungsversuch wird nervöser und komischer, bis er am Ende sogar dem Spiegel widerspricht.
- Zielwoerter: die Freude, freundlich, froh, fröhlich, fühlen, furchtbar, (sich) fürchten, die Geduld, gefallen, sich etwas gefallen lassen, das Gefühl, gern/gerne, gespannt

**Szene Ge-5** (13 Woerter)
- Prämise: Ein Kind hat schreckliche Angst vor dem ersten Schwimmkurs.
- Komischer Dreh: Es überwindet die Angst erst, als der Schwimmlehrer selbst ins Becken fällt und alle lachen müssen.
- Zielwoerter: das Gewissen, das Glück, glücklich, hassen, das Heimweh, helfen, die Hilfe, herzlich, hoffen, hoffentlich, die Hoffnung, höflich, der Humor

**Szene Ge-6** (13 Woerter)
- Prämise: Zwei Kollegen streiten sich lautstark über eine Kleinigkeit im Büro.
- Komischer Dreh: Der Streit wird so absurd übertrieben, dass am Ende beide gemeinsam lachend zusammenbrechen.
- Zielwoerter: interessieren, das Interesse, interessiert, klagen, komisch, lächeln, lachen, langweilig, sich langweilen, die Langeweile, die Laune, leid tun, leider

**Szene Ge-7** (13 Woerter)
- Prämise: Ein Mann gesteht seiner Angebeteten in einem völlig falsch gewählten Moment seine Liebe.
- Komischer Dreh: Die Gefühle brechen mitten in einer Feuerwehrübung aus ihm heraus, während im Hintergrund eine Sirene heult.
- Zielwoerter: lieb, Lieblings-, loben, lügen, die Lüge, die Lust, lustig, merkwürdig, der Mut, mutig, nervös, nett, neugierig

**Szene Ge-8** (13 Woerter)
- Prämise: Eine Reisegruppe wird vom Busfahrer über eine Verspätung informiert.
- Komischer Dreh: Die Reaktionen reichen von Panik bis Gelassenheit, und die Gruppendynamik eskaliert herrlich kleinlich.
- Zielwoerter: optimistisch, das Pech, peinlich, populär, privat, reagieren, die Reaktion, der Respekt, die Ruhe, ruhig, schade, schimpfen, der Schreck

**Szene Ge-9** (13 Woerter)
- Prämise: Ein Chef versucht, seinem Team nach einem Misserfolg Mut zuzusprechen.
- Komischer Dreh: Seine Aufmunterungsrede wird so übertrieben pathetisch, dass das Team eher amüsiert als motiviert ist.
- Zielwoerter: schrecklich, schreien, seltsam, sicher, sorgen, die Sorge, spannend, der Spaß, spüren, still, die Stimmung, stolz, stören

**Szene Ge-10** (13 Woerter)
- Prämise: Zwei Nachbarn vertragen sich nach jahrelangem Streit endlich wieder.
- Komischer Dreh: Die Versöhnung wird von einer Kette peinlicher Missverständnisse begleitet, die beide immer wieder zum Lachen bringen.
- Zielwoerter: (sich) streiten, der Streit, streng, der Stress, sympathisch, tolerant, die Träne, träumen, der Traum, Traum-, traurig, treu, der Typ

**Szene Ge-11** (13 Woerter)
- Prämise: Ein Kind wird von Mitschülern beim Fußball geärgert und rennt weinend nach Hause.
- Komischer Dreh: Die Mutter tröstet es mit einer so übertriebenen Geschichte, dass das Kind am Ende vor Lachen weint statt vor Kummer.
- Zielwoerter: überraschen, die Überraschung, überreden, übertreiben, umarmen, unheimlich, unterstützen, die Unterstützung, vergnügt, sich verhalten, das Verhalten, vermissen, verrückt

**Szene Ge-12** (16 Woerter)
- Prämise: Eine Braut bekommt kurz vor der Hochzeit Panik und rennt aus der Kirche.
- Komischer Dreh: Der Bräutigam rennt in vollem Ornat hinterher, während die Gäste verwirrt zuschauen.
- Zielwoerter: vertrauen, das Vertrauen, verzeihen, Verzeihung, der Vorwurf, wahnsinnig, weinen, willkommen, winken, der Witz, sich wundern, (sich) wünschen, der Wunsch, wütend, zufrieden, zuverlässig


### Körper & Gesundheit  *(n=161)*

_Körperteile, Krankheiten, Arztbesuche, Medikamente, Hygiene._

**Scenes: 13**

**Szene K-1** (13 Woerter)
- Prämise: Ein Patient wartet nervös im überfüllten Wartezimmer einer Arztpraxis.
- Komischer Dreh: Er hört den anderen Patienten so gespannt zu, dass er am Ende überzeugt ist, an allen möglichen Krankheiten gleichzeitig zu leiden.
- Zielwoerter: abnehmen, die Apotheke, der Arm, der Arzt, die Ärztin, atmen, der Atem, das Auge, (sich) ausruhen, baden, der Bart, der Bauch, behandeln

**Szene K-2** (13 Woerter)
- Prämise: Eine Krankenschwester erklärt einem ängstlichen Kind vor der Spritze, dass alles gut wird.
- Komischer Dreh: Sie erfindet eine immer abenteuerlichere Geschichte, um das Kind abzulenken, bis es die Spritze völlig vergisst.
- Zielwoerter: das Bein, beißen, die Besserung, bewegen, die Bewegung, blass, blind, blond, bluten, das Blut, brechen, die Brille, die Brust

**Szene K-3** (13 Woerter)
- Prämise: Ein Mann erkältet sich mitten im Sommer und wird von der ganzen Familie bemitleidet.
- Komischer Dreh: Er inszeniert seine Erkältung so theatralisch, dass die Familie ihm am Ende kaum noch glaubt.
- Zielwoerter: die Zahnbürste, die Creme, dick, der Doktor, die Doktorin, die Droge, der Durst, durstig, (sich) duschen, einnehmen, sich erholen, die Erholung, sich erkälten

**Szene K-4** (13 Woerter)
- Prämise: Ein Fitnessstudio-Neuling übertreibt es am ersten Tag gewaltig mit dem Training.
- Komischer Dreh: Am nächsten Tag kann er sich vor Muskelkater kaum bewegen und braucht Hilfe beim Anziehen der Socken.
- Zielwoerter: erkältet, die Erkältung, erschöpft, das Fieber, die Figur, der Finger, frieren, der Fuß, das Gesicht, gesund, die Gesundheit, die Grippe, das Haar

**Szene K-5** (13 Woerter)
- Prämise: Ein Zahnarzt erklärt einem Patienten mit Zahnschmerzen geduldig die Behandlung.
- Komischer Dreh: Der Patient stellt aus lauter Angst so viele Ausweichfragen, dass die Behandlung nie beginnt.
- Zielwoerter: der Hals, die Hand, die Haut, das Herz, der Hunger, hungrig, husten, der Husten, die Infektion, die Klinik, das Knie, der Knochen, der Kopf

**Szene K-6** (13 Woerter)
- Prämise: Eine Läuferin verletzt sich beim Stadtlauf leicht und wird von Sanitätern versorgt.
- Komischer Dreh: Sie übertreibt ihre Schmerzen so sehr, dass gleich drei Sanitäter gleichzeitig um sie herumwuseln.
- Zielwoerter: der Körper, körperlich, die Kraft, kräftig, krank, der Kranke, die Kranke, das Krankenhaus, die Krankenkasse, der Krankenpfleger, die Krankenschwester, der Krankenwagen, die Krankheit

**Szene K-7** (13 Woerter)
- Prämise: Ein Notarzt-Team übt einen fiktiven Notfall in einem Rollenspiel für die Ausbildung.
- Komischer Dreh: Der Schauspieler-Patient übertreibt seine Symptome so absurd, dass das Team nicht mehr ernst bleiben kann.
- Zielwoerter: leiden, die Lippe, der Magen, mager, das Medikament, die Medizin, müde, der Mund, der Muskel, die Nase, der Nerv, der Nichtraucher, die Nichtraucherin

**Szene K-8** (13 Woerter)
- Prämise: Ein Kind muss zum ersten Mal zum Zahnarzt und fürchtet sich fürchterlich.
- Komischer Dreh: Es lässt sich erst beruhigen, als der Zahnarzt selbst so tut, als hätte er noch größere Angst.
- Zielwoerter: die Notaufnahme, das Ohr, operieren, die Operation, die Ordination, das Parfüm, der Patient, die Patientin, das Pflaster, pflegen, der Pfleger, die Pflegerin, die Praxis

**Szene K-9** (13 Woerter)
- Prämise: Eine Apothekerin berät einen verwirrten Kunden, der die Packungsbeilage komplett falsch verstanden hat.
- Komischer Dreh: Der Kunde erklärt seine bizarren Selbstdiagnosen mit voller Überzeugung, bis die Apothekerin alles richtigstellen muss.
- Zielwoerter: (sich) rasieren, rauchen, der Raucher, die Raucherin, riechen, der Rücken, die Salbe, schlafen, der Schlaf, schlank, der Schmerz, das Schmerzmittel, schminken

**Szene K-10** (13 Woerter)
- Prämise: Ein älterer Herr geht zur jährlichen Vorsorgeuntersuchung und nimmt eine lange Symptomliste mit.
- Komischer Dreh: Die Liste wird immer länger und absurder, weil er auf dem Weg zur Praxis noch neue 'Beschwerden' erfindet.
- Zielwoerter: (sich) schneiden, der Schnupfen, die Schulter, schwach, die Schwangerschaft, schwitzen, die Seife, die Sprechstunde, die Spritze, stark, die Station, stechen, sterben

**Szene K-11** (13 Woerter)
- Prämise: Ein Sportler bekommt nach einem Sturz beim Skifahren einen Gipsverband.
- Komischer Dreh: Er versucht trotzdem verzweifelt, mit dem Gips weiter Ski zu fahren, was zu einer Slapstick-Szene wird.
- Zielwoerter: stinken, (sich) stoßen, stumm, stürzen, die Sucht, süchtig, das Suchtmittel, die Tablette, das Taschentuch, taub, die Therapie, der Tod, tot

**Szene K-12** (13 Woerter)
- Prämise: Eine Krankenkasse-Mitarbeiterin erklärt am Telefon geduldig eine komplizierte Abrechnung.
- Komischer Dreh: Der Anrufer versteht jedes zweite Wort falsch und stellt immer skurrilere Rückfragen.
- Zielwoerter: der Tote, die Tote, die Tropfen, untersuchen, die Untersuchung, (sich) verletzen, die Verletzung, verschreiben, die Versichertenkarte, der Virus, das Vitamin, wach, wehtun

**Szene K-13** (5 Woerter)
- Prämise: Ein Patient wartet nervös im überfüllten Wartezimmer einer Arztpraxis.
- Komischer Dreh: Er hört den anderen Patienten so gespannt zu, dass er am Ende überzeugt ist, an allen möglichen Krankheiten gleichzeitig zu leiden.
- Zielwoerter: die Wunde, der Zahn, die Zahncreme/-pasta, die Zigarette, zunehmen


### Freizeit, Kultur & Unterhaltung  *(n=165)*

_Hobbys, Sport, Kino, Musik, Feste, Spiele._

**Scenes: 13**

**Szene X-1** (13 Woerter)
- Prämise: Ein Amateur-Fußballverein bereitet sich mit übertriebenem Ehrgeiz auf das Dorfturnier vor.
- Komischer Dreh: Der Trainer plant eine hochkomplexe Taktik, die beim ersten Anpfiff sofort völlig zusammenbricht.
- Zielwoerter: das Abenteuer, die Aktivität, sich amüsieren, aufführen, auftreten, der Auftritt, ausgehen, ausstellen, die Ausstellung, der Ball, das Ballett, die Bar, der Basketball

**Szene X-2** (13 Woerter)
- Prämise: Eine Familie verbringt einen Regentag mit Brettspielen im Wohnzimmer.
- Komischer Dreh: Ein einfaches Kinderspiel eskaliert zu einem erbitterten, viel zu ernst genommenen Wettkampf zwischen den Erwachsenen.
- Zielwoerter: basteln, das Bild, das Buch, die Bühne, die Diskothek, der Eintritt, erleben, das Erlebnis, fangen, die Fantasie/Phantasie, der Fasching, die Fasnacht, faulenzen

**Szene X-3** (13 Woerter)
- Prämise: Ein Amateurtheater probt kurz vor der Premiere ein Stück, bei dem noch nichts klappt.
- Komischer Dreh: Die Souffleuse muss so oft eingreifen, dass sie am Ende fast die ganze Rolle selbst spielt.
- Zielwoerter: feiern, die Feier, das Fest, das Feuerzeug, der Film, die Flöte, fotografieren, das Foto, der Fotoapparat, der Fotograf, die Fotografie, die Freizeit, der Fußball

**Szene X-4** (13 Woerter)
- Prämise: Ein Fotoclub trifft sich zu einem Ausflug, um die perfekte Landschaftsaufnahme zu machen.
- Komischer Dreh: Alle sind so beschäftigt mit der Kamera, dass keiner die eigentliche Landschaft überhaupt richtig ansieht.
- Zielwoerter: die Galerie, der Gegner, genießen, gewinnen, die Gitarre, Golf, die Gymnastik, die Halle, das Hallenbad, der Held, die Heldin, das Hobby, das Instrument

**Szene X-5** (13 Woerter)
- Prämise: Eine Gruppe Freunde organisiert spontan ein Picknick im Park.
- Komischer Dreh: Ein unerwarteter Regenschauer verwandelt das elegante Picknick in eine chaotische Rettungsaktion für Kuchen und Decken.
- Zielwoerter: die Kamera, der Karneval, das Kino, das Klavier, klettern, die Kneipe, das Konzert, der Krimi, die Kultur, kulturell, die Kunst, der Künstler, die Künstlerin

**Szene X-6** (13 Woerter)
- Prämise: Ein Museum veranstaltet eine Quiznacht über Kunstgeschichte.
- Komischer Dreh: Ein Team gewinnt nur, weil es bei jeder Frage die absurdeste, aber zufällig richtige Antwort rät.
- Zielwoerter: lesen, der Leser, die Leserin, das Lied, die Literatur, malen, der Maler, die Malerin, die Mannschaft, das Märchen, das Museum, die Musik, musikalisch

**Szene X-7** (13 Woerter)
- Prämise: Ein Chor probt zum ersten Mal für ein großes Konzert.
- Komischer Dreh: Ein Sänger singt hartnäckig eine völlig falsche Melodie, ohne es selbst zu merken.
- Zielwoerter: der Musiker, die Musikerin, die Oper, das Orchester, der Park, die Party, die Phantasie/Fantasie, das Picknick, der Profi, der Profisportler, die Profisportlerin, das Publikum, die Puppe

**Szene X-8** (13 Woerter)
- Prämise: Eine Gruppe Rentner trifft sich wöchentlich zum Kartenspiel im Vereinsheim.
- Komischer Dreh: Der Wettstreit um die Meisterschaft wird ernster genommen als jede Weltmeisterschaft.
- Zielwoerter: das Quiz, das Rätsel, reiten, der Rekord, rennen, die Rolle, der Roman, die Runde, der Saal, sammeln, der Sänger, die Sängerin, zuschauen

**Szene X-9** (13 Woerter)
- Prämise: Ein Zirkus in der Kleinstadt sucht kurzfristig Verstärkung für die Vorstellung am Abend.
- Komischer Dreh: Ein Zuschauer wird spontan auf die Bühne geholt und wird zum unfreiwilligen Star der Show.
- Zielwoerter: der Schauspieler, die Schauspielerin, schießen, der Schriftsteller, die Schriftstellerin, schwimmen, das Schwimmbad, die Serie, siegen, der Sieg, der Sieger, die Siegerin, singen

**Szene X-10** (13 Woerter)
- Prämise: Ein Wanderclub plant eine anspruchsvolle Tagestour in die Berge.
- Komischer Dreh: Die Route entpuppt sich als viel zu leicht, sodass die Gruppe aus Langeweile eigene, absurde Zusatzaufgaben erfindet.
- Zielwoerter: der Ski/Schi, spazieren gehen, der Spaziergang, spielen, das Spiel, der Spieler, die Spielerin, der Spielplatz, das Spielzeug, der Sport, die Sportart, der Sportler, die Sportlerin

**Szene X-11** (13 Woerter)
- Prämise: Ein Kino zeigt eine Vorpremiere, bei der die Technik ständig streikt.
- Komischer Dreh: Der Film läuft rückwärts, in Zeitlupe und mit falschem Ton, während das Publikum es für Kunst hält.
- Zielwoerter: sportlich, das Stadion, der Star, das Studio, die Szene, tanzen, der Tanz, tauchen, das Tennis, das Theater, der Tierpark, das Tor, trainieren

**Szene X-12** (13 Woerter)
- Prämise: Ein Hobbymusiker tritt zum ersten Mal bei einem Straßenfest auf.
- Komischer Dreh: Seine Gitarre verstimmt sich mitten im Lied, und er improvisiert einen absurd neuen Song daraus.
- Zielwoerter: der Trainer, die Trainerin, das Training, die Unterhaltung, unternehmen, die Veranstaltung, der Verein, sich vergnügen, das Vergnügen, der Verlierer, die Verliererin, Volleyball, wandern

**Szene X-13** (9 Woerter)
- Prämise: Ein Amateur-Fußballverein bereitet sich mit übertriebenem Ehrgeiz auf das Dorfturnier vor.
- Komischer Dreh: Der Trainer plant eine hochkomplexe Taktik, die beim ersten Anpfiff sofort völlig zusammenbricht.
- Zielwoerter: die Wanderung, der Wettbewerb, wetten, zeichnen, die Zeichnung, der Zirkus, der Zoo, der Zuschauer, die Zuschauerin


### In der Wohnung & Haushalt  *(n=133)*

_Zimmer, Möbel, Umzug, Hausarbeit und alles rund ums Zuhause._

**Scenes: 10**

**Szene W-1** (13 Woerter)
- Prämise: Eine Familie zieht am Wochenende in eine neue Wohnung um.
- Komischer Dreh: Der Umzugswagen ist zu klein gebucht, sodass Möbel in immer abenteuerlicheren Türmen gestapelt werden müssen.
- Zielwoerter: der Abfall, der Abfalleimer, abwaschen, das Apartment, aufräumen, der Aufzug, ausziehen, das Bad, die Badewanne, der Balkon, bauen, der Bau, die Baustelle

**Szene W-2** (13 Woerter)
- Prämise: Ein Vermieter zeigt einer Mieterin die Wohnung, bevor sie einzieht.
- Komischer Dreh: Bei jeder Tür, die er öffnet, fällt etwas Unerwartetes heraus, das er hastig wieder wegräumt.
- Zielwoerter: das Bett, der Bewohner, die Bewohnerin, der Boden, die Bürste, die Couch, das Dach, die Decke, dekorieren, der Dreck, die Dusche, einrichten, die Einrichtung

**Szene W-3** (13 Woerter)
- Prämise: Ein Ehepaar streitet liebevoll darüber, wie das Wohnzimmer eingerichtet werden soll.
- Komischer Dreh: Jeder rückt heimlich nachts die Möbel wieder an seinen bevorzugten Platz zurück.
- Zielwoerter: einziehen, das Erdgeschoss/ Ergeschoß, die Etage, der Fauteuil, das Fenster, der Flur, der Gang, die Garage, der Garten, das Gas, das Geschirr, gießen, das Grundstück

**Szene W-4** (13 Woerter)
- Prämise: Ein Untermieter putzt zum ersten Mal seit Monaten gründlich die ganze Wohnung.
- Komischer Dreh: Er findet dabei so viele vergessene Gegenstände, dass daraus eine kleine archäologische Ausgrabung wird.
- Zielwoerter: der Hammer, das Haus, der Haushalt, das Heim, heizen, die Heizung, der Herd, der Hof, der Kasten, der Keller, die Kerze, die Kiste, das Kissen

**Szene W-5** (13 Woerter)
- Prämise: Ein Handwerker soll die kaputte Heizung reparieren, bevor der Winter beginnt.
- Komischer Dreh: Er repariert stattdessen aus Versehen fünf andere Dinge, bevor er überhaupt bei der Heizung ankommt.
- Zielwoerter: die Klimaanlage, die Klingel, der Korridor, die Küche, der Kühlschrank, die Lampe, die Leiter, das Licht, der Lift, die Mauer, mieten, die Miete, der Mieter

**Szene W-6** (13 Woerter)
- Prämise: Eine Studentin richtet ihr erstes eigenes, winziges Zimmer ein.
- Komischer Dreh: Sie stapelt Möbel so kreativ, dass am Ende kaum noch Platz zum Betreten des Zimmers bleibt.
- Zielwoerter: die Mieterin, das Möbel, möbliert, der Müll, die Müllabfuhr, die Mülltonne, der Nagel, der (Back-)Ofen, putzen, das Quartier, das Regal, reinigen, die Reinigung

**Szene W-7** (13 Woerter)
- Prämise: Ein Nachbar bittet um Hilfe, weil sich sein Schlüssel im Schloss verklemmt hat.
- Komischer Dreh: Die improvisierte Rettungsaktion mit Nachbarschaftshilfe wird zur halbstündigen Slapstick-Nummer im Treppenhaus.
- Zielwoerter: reparieren, die Reparatur, das (Back-)Rohr, der Sack, der Salon, sauber, die Schachtel, die Schere, das Schloss, der Schlüssel, der Schmutz, schmutzig, der Schrank

**Szene W-8** (13 Woerter)
- Prämise: Eine Familie räumt gemeinsam den vollgestopften Keller auf.
- Komischer Dreh: Jeder findet ein Erinnerungsstück, das eine völlig andere, oft übertriebene Geschichte dazu erzählt.
- Zielwoerter: der Sessel, das Sofa, der Spiegel, spülen, der Staub, staubsaugen, die Stiege, das Stiegenhaus, der Stock, das Stockwerk, das Streichholz, der Strom, der Stuhl

**Szene W-9** (13 Woerter)
- Prämise: Ein WG-Bewohner übernimmt zum ersten Mal die wöchentliche Küchenputzpflicht.
- Komischer Dreh: Er verwendet dabei so viel Reinigungsmittel, dass die ganze Wohnung tagelang nach Zitrone riecht.
- Zielwoerter: der Teppich, die Terrasse, der Tisch, die Toilette, die Treppe, das Treppenhaus, trocknen, die Tür, umziehen, der Umzug, die Vase, vermieten, der Vermieter

**Szene W-10** (16 Woerter)
- Prämise: Ein Ehepaar bereitet spontan Besuch der Schwiegereltern vor und muss die Wohnung in einer Stunde herrichten.
- Komischer Dreh: Sie verstecken das Chaos in immer absurderen Verstecken, bis kaum noch Platz dafür bleibt.
- Zielwoerter: die Vermieterin, die Vermietung, die Wand, (sich) waschen, die Wäsche, das Waschmittel, das Werkzeug, wohnen, die Wohnung, das Wohnzimmer, die Zange, das Zimmer, das Zuhause, die Zünder (A), das Zündholz, zu sein


### Staat, Recht & Gesellschaft  *(n=146)*

_Ämter, Polizei, Gesetze, Politik, Kriminalität, Formulare._

**Scenes: 11**

**Szene D-1** (13 Woerter)
- Prämise: Ein Bürger steht in einer endlosen Warteschlange im Amt, um ein simples Formular abzugeben.
- Komischer Dreh: Nach Stunden des Wartens schickt ihn der Beamte zu genau dem Schalter zurück, an dem er begonnen hat.
- Zielwoerter: abstimmen, das Amt, anmelden, die Anmeldung, der Anspruch, der Antrag, der Anwalt, die Anwältin, anzeigen, die Anzeige, das Asyl, ausfüllen, der Ausländer

**Szene D-2** (13 Woerter)
- Prämise: Ein Zeuge wird bei einer Gerichtsverhandlung zu einem harmlosen Vorfall befragt.
- Komischer Dreh: Seine Erinnerung wird mit jeder Frage widersprüchlicher und dramatischer.
- Zielwoerter: die Ausländerin, ausländisch, der Ausweis, der Beamte, die Beamtin, beantragen, befreit, die Behörde, beraten, die Beratung, bestrafen, betrügen, die Bevölkerung

**Szene D-3** (13 Woerter)
- Prämise: Eine Polizistin nimmt am Marktplatz die Anzeige eines gestohlenen Fahrrads auf.
- Komischer Dreh: Der Geschädigte beschreibt den Dieb so vage und widersprüchlich, dass am Ende fast jeder Passant verdächtig wirkt.
- Zielwoerter: der Bürger, die Bürgerin, der Dieb, das Dokument, die e-card, einbrechen, der Einbrecher, die Einbrecherin, der Einbruch, eintragen, der Einwohner, die Einwohnerin, die Erlaubnis

**Szene D-4** (13 Woerter)
- Prämise: Ein Politiker hält vor der Gemeinde eine Rede über ein neues Gesetz.
- Komischer Dreh: Er verheddert sich so sehr in Fachbegriffen, dass am Ende niemand mehr versteht, wofür er eigentlich ist.
- Zielwoerter: festnehmen, das Formular, der Friede, das Fundbüro, das Gefängnis, die Gemeinschaft, genehmigen, das Geschlecht, die Gesellschaft, das Gesetz, die Gewalt, gleichberechtigt, der Gott

**Szene D-5** (13 Woerter)
- Prämise: Ein Ausländeramt bearbeitet den Antrag eines Migranten auf eine Aufenthaltsgenehmigung.
- Komischer Dreh: Der Beamte verlangt ein Dokument nach dem anderen, bis der Antragsteller fast einen ganzen Aktenordner mitbringt.
- Zielwoerter: gültig, die Herkunft, illegal, integrieren, die Integration, interkulturell, international, kämpfen, der Kampf, der Kandidat, die Kirche, der König, das Konsulat

**Szene D-6** (13 Woerter)
- Prämise: Eine Bürgerversammlung debattiert über ein neues Verkehrsschild an der Kreuzung.
- Komischer Dreh: Die Diskussion wird hitziger als jede Wahlkampfdebatte, obwohl es nur um ein einziges Schild geht.
- Zielwoerter: kontrollieren, die Kontrolle, der Krieg, Kriminal-, die Kriminalpolizei, die Leute, die Mehrheit, der Mensch, menschlich, der Migrant, die Migrantin, die Migration, die Minderheit

**Szene D-7** (13 Woerter)
- Prämise: Ein Botschaftsangestellter erklärt einem verwirrten Touristen die Visumsregeln.
- Komischer Dreh: Die Erklärung wird mit jedem Satz komplizierter, bis der Tourist beschließt, doch lieber zu Hause zu bleiben.
- Zielwoerter: das Mitglied, der Name, der Familienname, der Vorname, national/national-, öffentlich, die Öffentlichkeit, offiziell, das Opfer, die Person, die Personalien, der Personenstand, die Politik

**Szene D-8** (13 Woerter)
- Prämise: Ein Rathaus veranstaltet einen Tag der offenen Tür, an dem Bürger alle Ämter kennenlernen sollen.
- Komischer Dreh: Ein neugieriger Rentner stellt bei jedem Schalter dieselbe absurde Testfrage, um die Beamten zu prüfen.
- Zielwoerter: der Politiker, die Politikerin, politisch, die Polizei, der Polizist, die Polizistin, protestieren, der Protest, der Prozess, das Rathaus, das Recht, rechtlich, die Reform

**Szene D-9** (13 Woerter)
- Prämise: Ein Anwalt bereitet einen Mandanten auf eine völlig banale Gerichtsverhandlung vor.
- Komischer Dreh: Er behandelt den Bagatellfall mit derart übertriebenem Ernst, dass der Mandant fast an einen Schwerverbrechen glaubt.
- Zielwoerter: die Religion, der Richter, die Richterin, sozial, stammen, stehlen, der Stempel, die Strafe, strafbar, der Strafzettel, die Tat, der Täter, die Täterin

**Szene D-10** (13 Woerter)
- Prämise: Ein Standesamt traut zwei Verliebte, doch die Trauzeugen kommen zu spät.
- Komischer Dreh: Die Verspätung wird mit immer abenteuerlicheren Ausreden erklärt, während das Brautpaar geduldig wartet.
- Zielwoerter: die Tradition, traditionell, die Unterlagen, untersagt, unterschreiben, die Unterschrift, die Urkunde, das Urteil, verbieten, das Verbot, verboten, der Verbrecher, die Verbrecherin

**Szene D-11** (16 Woerter)
- Prämise: Ein Wahllokal zählt am Abend die Stimmen der Gemeindewahl aus.
- Komischer Dreh: Ein einziger unleserlicher Wahlzettel sorgt für eine stundenlange, hitzige Debatte im kleinen Ausschuss.
- Zielwoerter: der Verdacht, verdächtig, verhaften, versichern, die Versicherung, der Vertrag, verurteilen, die Verwaltung, die Vorschrift, wählen, die Wahl, der Wohnsitz, der Zeuge, die Zeugin, der Zivilstand, der Zoll


### Einkaufen, Geld & Handel  *(n=132)*

_Geschäfte, Preise, Banken, Zahlen, Konsum._

**Scenes: 10**

**Szene M-1** (13 Woerter)
- Prämise: Ein Kunde feilscht auf dem Flohmarkt hartnäckig um einen alten Gegenstand.
- Komischer Dreh: Der Verkäufer und der Kunde einigen sich erst nach einem absurd langen, theatralischen Verhandlungsspiel.
- Zielwoerter: abheben, anbieten, der Anbieter, das Angebot, anschaffen, arm, die Ausgabe, ausgeben, (sich etwas) aussuchen, auswählen, die Auswahl, der Automat, die Bank

**Szene M-2** (13 Woerter)
- Prämise: Eine Familie räumt den Supermarkt leer, weil Schnee vorhergesagt wurde.
- Komischer Dreh: Sie kaufen völlig übertriebene Mengen an Dingen, die niemand wirklich braucht, wie hundert Dosen Erbsen.
- Zielwoerter: der Bancomat/Bankomat, die Bankleitzahl, die Bankomat-Karte, bar, das Bargeld, der Bedarf, bedienen, der Beleg, sich beschweren, besitzen, besorgen, der Betrag, bezahlen

**Szene M-3** (13 Woerter)
- Prämise: Ein Bankangestellter erklärt einem verwirrten Rentner die neue Online-Banking-App.
- Komischer Dreh: Der Rentner versteht jeden Schritt komplett falsch und löst dabei fast versehentlich eine große Überweisung aus.
- Zielwoerter: bieten, billig, die Brieftasche, die Buchhandlung, die Drogerie, die ec-Karte/EC-Karte, einkaufen, der Einkauf, die Einnahme, einzahlen, die Einzahlung, die Ermäßigung, eröffnen

**Szene M-4** (13 Woerter)
- Prämise: Ein Verkäufer im Elektronikladen versucht, einem unentschlossenen Kunden ein Gerät schmackhaft zu machen.
- Komischer Dreh: Er erfindet immer unglaublichere Zusatzfunktionen, die das Gerät gar nicht wirklich hat.
- Zielwoerter: die Eröffnung, fällig, finanzieren, finanziell, der Flohmarkt, garantieren, die Garantie, die Gebühr, das Geld, der Geldautomat, die Geldbörse, das Geschäft, der Gewinn

**Szene M-5** (13 Woerter)
- Prämise: Ein Kind spart monatelang sein Taschengeld für ein bestimmtes Spielzeug.
- Komischer Dreh: Als es endlich genug hat, ist der Preis gestiegen, und es beginnt eine kleine, verzweifelte Verhandlung an der Kasse.
- Zielwoerter: gratis, günstig, handeln, der Handel, der Händler, die Händlerin, die Chipkarte, die Kasse, der Katalog, (sich etwas) kaufen, der Kauf, der Käufer, die Käuferin

**Szene M-6** (13 Woerter)
- Prämise: Ein Kunde reklamiert im Geschäft eine kaputte Ware und verlangt sein Geld zurück.
- Komischer Dreh: Er übertreibt den Schaden so sehr, dass die Verkäuferin am Ende fast Mitleid statt Ärger empfindet.
- Zielwoerter: der Kiosk, konsumieren, der Konsum, das Konto, das Girokonto, kosten, die Kosten, kostenlos, der Kredit, die Kreditkarte, der Kunde, die Kundin, der Laden

**Szene M-7** (13 Woerter)
- Prämise: Eine Bankfiliale eröffnet für einen jungen Kunden das erste eigene Konto.
- Komischer Dreh: Der Kunde stellt so viele überängstliche Fragen zu jeder Gebühr, dass die Beraterin die Geduld fast verliert.
- Zielwoerter: das Lager, leihen, liefern, die Lieferung, sich lohnen, die Mahnung, die Marke, der Markt, die Mehrwertsteuer, die Messe, die Münze, die Nachfrage, pauschal

**Szene M-8** (13 Woerter)
- Prämise: Ein Ladenbesitzer plant ein großes Sonderangebot, um alte Ware loszuwerden.
- Komischer Dreh: Die Werbeaktion wird so übertrieben angepriesen, dass am Eröffnungstag eine regelrechte Warteschlange entsteht.
- Zielwoerter: das Portemonnaie/Portmonee, der Preis, preiswert, die Quittung, der Rabatt, die Rechnung, reich, der Schalter, das Schaufenster, der Schein, die Schulden, das Sonderangebot, sparen

**Szene M-9** (13 Woerter)
- Prämise: Zwei Freunde teilen sich die Rechnung nach einem gemeinsamen Essen.
- Komischer Dreh: Die Berechnung, wer was gegessen hat, wird zu einer minutenlangen, absurd genauen Mathe-Diskussion.
- Zielwoerter: sparsam, die Steuer, die Summe, der Supermarkt, tauschen, teuer, die Tüte, überweisen, die Überweisung, umsonst, umtauschen, der Umtausch, verbrauchen

**Szene M-10** (15 Woerter)
- Prämise: Ein Straßenhändler verkauft an Touristen Souvenirs zu völlig überzogenen Preisen.
- Komischer Dreh: Ein cleverer Tourist handelt den Preis so weit herunter, dass der Händler am Ende fast draufzahlt.
- Zielwoerter: verkaufen, der Verkäufer, die Verkäuferin, verpacken, die Ware, wechseln, die Werbung, wert, der Wert, wertlos, wertvoll, zahlen, die Zahlung, die Zinsen, der Zuschlag


### Arbeit & Beruf  *(n=152)*

_Berufe, Bewerbung, Büroalltag, Anstellung, Karriere._

**Scenes: 12**

**Szene A-1** (13 Woerter)
- Prämise: Ein Bewerber übt vor dem Spiegel für sein erstes Vorstellungsgespräch.
- Komischer Dreh: Er antwortet sich selbst so übertrieben selbstbewusst, dass er beim echten Gespräch komplett die Nerven verliert.
- Zielwoerter: die Abteilung, der Abwart, die Abwartin, anstellen, der Angestellte, die Angestellte, arbeiten, die Arbeit, der Arbeiter, die Arbeiterin, die Arbeitserlaubnis, arbeitslos, die Arbeitslosigkeit

**Szene A-2** (13 Woerter)
- Prämise: Ein neuer Praktikant wird an seinem ersten Arbeitstag von niemandem richtig eingewiesen.
- Komischer Dreh: Er improvisiert seine Aufgaben so kreativ, dass er versehentlich die wichtigste Präsentation der Woche rettet.
- Zielwoerter: der Arbeitsplatz, die Arbeitsstelle, der Architekt, die Architektin, der Auftrag, die Aushilfe, der Bauer, der Beruf, beruflich, berufstätig, beschäftigen, die Beschäftigung, die Besprechung

**Szene A-3** (13 Woerter)
- Prämise: Ein Chef hält eine Ansprache zur Firmenfeier, die eigentlich kurz sein sollte.
- Komischer Dreh: Die Rede wird immer länger und emotionaler, während die Mitarbeiter verzweifelt auf das Buffet schielen.
- Zielwoerter: der Betrieb, der Betriebsrat, die Betriebsrätin, sich bewerben, die Bewerbung, das Büro, der Chef, die Chefin, der Coiffeur, die Coiffeuse, der Dienst, der Direktor, die Direktorin

**Szene A-4** (13 Woerter)
- Prämise: Zwei Kollegen bewerben sich beide intern für dieselbe Beförderung.
- Komischer Dreh: Ihr freundlicher Konkurrenzkampf wird immer alberner, bis beide gemeinsam vor dem Chef stehen und sich gegenseitig loben.
- Zielwoerter: einführen, die Einführung, das Einkommen, einsetzen, einstellen, entlassen, die Entlassung, der Erfolg, erfolgreich, der Experte, die Fabrik, der Fachmann, die Fachfrau

**Szene A-5** (13 Woerter)
- Prämise: Ein Betriebsrat verhandelt in einer Sitzung über neue Arbeitszeiten.
- Komischer Dreh: Die Verhandlung dreht sich am Ende nur noch um die Frage, wer die Kaffeepause zuerst nehmen darf.
- Zielwoerter: die Fachleute, der Feierabend, die Firma, der Fleischhauer, die Fleischhauerin, der Friseur, die Friseurin, führen, die Führung, das Gehalt, die Gewerkschaft, gründen, halbtags

**Szene A-6** (13 Woerter)
- Prämise: Ein Handwerksmeister bildet seinen ersten Lehrling in der Werkstatt aus.
- Komischer Dreh: Der Lehrling stellt bei jedem Handgriff so viele Rückfragen, dass die einfachste Reparatur den ganzen Tag dauert.
- Zielwoerter: der Handwerker, die Handwerkerin, der Hausmeister, die Hausmeisterin, herstellen, der Hersteller, der Ingenieur, der Journalist, die Journalistin, die Karriere, der Kellner, die Kellnerin, der Kollege

**Szene A-7** (13 Woerter)
- Prämise: Eine Angestellte kündigt nach Jahren ihren Job, um sich selbstständig zu machen.
- Komischer Dreh: Ihre Abschiedsrede gerät so rührselig, dass sogar der unbeliebteste Kollege am Ende Tränen in den Augen hat.
- Zielwoerter: die Kollegin, die Konferenz, die Konkurrenz, kündigen, die Kündigung, der Lebenslauf, leisten, die Leistung, leiten, der Leiter, die Leiterin, die Leitung, der Lohn

**Szene A-8** (13 Woerter)
- Prämise: Ein Team bereitet sich auf eine wichtige Kundenpräsentation vor, aber die Technik streikt.
- Komischer Dreh: Sie improvisieren die ganze Präsentation mit einer Flipchart und Handzeichen, was überraschend gut ankommt.
- Zielwoerter: der Mechaniker, die Mechanikerin, der Meister, der Metzger, der Mitarbeiter, die Mitarbeiterin, der Ober, in Pension gehen/sein, pensioniert werden/sein, der Pensionist, die Pensionistin, das Personal, der Pöstler

**Szene A-9** (13 Woerter)
- Prämise: Ein Rentner erzählt bei seiner Verabschiedungsfeier von seinem allerersten Arbeitstag vor Jahrzehnten.
- Komischer Dreh: Die Geschichte wird mit jedem Kollegen-Zwischenruf länger und übertriebener.
- Zielwoerter: die Pöstlerin, das Praktikum, der Praktikant, die Praktikantin, präsentieren, die Präsentation, das Projekt, die Qualifikation, die Rente, in Rente gehen/sein, der Rentner, die Rentnerin, der Sekretär

**Szene A-10** (13 Woerter)
- Prämise: Eine Arbeitsvermittlerin bereitet einen Arbeitslosen auf ein Bewerbungsgespräch vor.
- Komischer Dreh: Ihr Rollenspiel als strenger Chef wird so überzeugend, dass der Bewerber am Ende wirklich eingeschüchtert ist.
- Zielwoerter: die Sekretärin, selbstständig, der Serviceangestellte, die Serviceangestellte, der Sozialarbeiter, die Sozialarbeiterin, der Spezialist, die Spezialistin, die Stelle, streiken, der Streik, die Tätigkeit, die Teilzeit

**Szene A-11** (13 Woerter)
- Prämise: Ein Bewerber übt vor dem Spiegel für sein erstes Vorstellungsgespräch.
- Komischer Dreh: Er antwortet sich selbst so übertrieben selbstbewusst, dass er beim echten Gespräch komplett die Nerven verliert.
- Zielwoerter: der Termin, der Terminkalender, übernehmen, die Überstunde, der Unternehmer, die Unternehmerin, verantwortlich, die Verantwortung, verdienen, vereinbaren, die Vermittlung, die Versammlung, vertreten

**Szene A-12** (9 Woerter)
- Prämise: Ein neuer Praktikant wird an seinem ersten Arbeitstag von niemandem richtig eingewiesen.
- Komischer Dreh: Er improvisiert seine Aufgaben so kreativ, dass er versehentlich die wichtigste Präsentation der Woche rettet.
- Zielwoerter: der Vertreter, die Vertreterin, die Vertretung, die Visitenkarte, die Vollzeit, das Vorstellungsgespräch, das Werk, die Zusammenarbeit, zuständig


### Zeit & Kalender  *(n=116)*

_Uhrzeit, Datum, Häufigkeit, Dauer, Termine._

**Scenes: 9**

**Szene Z-1** (13 Woerter)
- Prämise: Ein notorischer Zuspätkommer versucht an einem einzigen Tag, alle verpassten Termine nachzuholen.
- Komischer Dreh: Sein Terminkalender wird so überfüllt, dass er zwischen den Terminen buchstäblich rennen muss.
- Zielwoerter: absagen, aktuell, der Alltag, alltäglich, anfangen, der Anfang, anfangs, aufhören, aufstehen, aufwachen, der Augenblick, ausfallen, bald

**Szene Z-2** (13 Woerter)
- Prämise: Eine Familie plant akribisch den Ablauf eines Sonntags von früh bis spät.
- Komischer Dreh: Der Plan wird schon beim Frühstück komplett über den Haufen geworfen, weil alles länger dauert als gedacht.
- Zielwoerter: sich beeilen, beenden, beginnen, der Beginn, bereits, bisher, damals, danach, dann, das Datum, dauern, die Dauer, dauernd

**Szene Z-3** (13 Woerter)
- Prämise: Ein Wecker klingelt jeden Morgen zur falschen Zeit, weil die Uhr kaputt ist.
- Komischer Dreh: Der Besitzer erfindet immer neue Tricks, um pünktlich zu werden, die alle grandios scheitern.
- Zielwoerter: diesmal, eilen, die Eile, eilig, einmal, enden, das Ende, endgültig, endlich, erst, erst-, ewig, der Feiertag

**Szene Z-4** (13 Woerter)
- Prämise: Zwei Kollegen vereinbaren einen Termin und verwechseln dabei ständig die Uhrzeit.
- Komischer Dreh: Am Ende wartet jeder zur falschen Zeit an einem anderen Ort auf den anderen.
- Zielwoerter: die Frist, früh, früher/früher-, gerade, gestern, gleichzeitig, häufig, heute, heutig-, immer, inzwischen, irgendwann, jederzeit

**Szene Z-5** (13 Woerter)
- Prämise: Ein altes Ehepaar erinnert sich beim Abendessen an vergangene Jahrestage.
- Komischer Dreh: Ihre Erinnerungen widersprechen sich so komisch, dass keiner mehr weiß, was wirklich wann passiert ist.
- Zielwoerter: jedes Mal, jemals, jetzt, der Kalender, kürzlich, lange, längst, letzt-, das Mal, manchmal, mittler-, mittlerweile, der Moment

**Szene Z-6** (13 Woerter)
- Prämise: Ein Reisebüro erstellt einen minutiösen Zeitplan für eine Gruppenreise.
- Komischer Dreh: Der Plan gerät völlig durcheinander, weil ein Reisender ständig zu früh oder zu spät auftaucht.
- Zielwoerter: nachher, neulich, nie, nun, oft/öfter, plötzlich, pünktlich, rechtzeitig, regelmäßig, die Saison, schließlich, der Schluss, schon

**Szene Z-7** (13 Woerter)
- Prämise: Ein Kalenderverkäufer preist auf dem Markt besonders 'zuverlässige' Kalender an.
- Komischer Dreh: Er verwickelt sich dabei selbst in Widersprüche über Wochentage und Feiertage.
- Zielwoerter: selten, sofort, spät, spätestens, ständig, stattfinden, die Stunde, der Tagesablauf, übermorgen, die Uhr, ursprünglich, verbringen, die Vergangenheit

**Szene Z-8** (13 Woerter)
- Prämise: Ein Kind zählt ungeduldig die Tage bis zum Geburtstag auf einem selbstgebastelten Kalender.
- Komischer Dreh: Es rechnet sich die Wartezeit immer wieder falsch aus, mal viel zu kurz, mal viel zu lang.
- Zielwoerter: verlängern, verpassen, versäumen, verschieben, die Verspätung, das Viertel, voraus, voraussichtlich, vorbei/vorbei-, vorgestern, vorhaben, vorher, vorhin

**Szene Z-9** (12 Woerter)
- Prämise: Eine Redaktion arbeitet unter Zeitdruck an der letzten Ausgabe vor dem Feiertag.
- Komischer Dreh: Der Redaktionsschluss wird mehrmals verschoben, während die Chaos-Zeitangaben immer absurder werden.
- Zielwoerter: vorläufig, warten, wecken, der Wecker, die Zeit, der Zeitpunkt, zurzeit, zuerst, die Zukunft, zukünftig, zuletzt, zunächst


### Schule & Bildung  *(n=123)*

_Unterricht, Prüfungen, Studium, Sprache lernen._

**Scenes: 10**

**Szene S-1** (13 Woerter)
- Prämise: Ein Schüler hat die Hausaufgaben vergessen und erfindet eine immer abenteuerlichere Ausrede.
- Komischer Dreh: Die Geschichte wird so unglaubwürdig episch, dass der Lehrer sie am Ende fast bewundert.
- Zielwoerter: die Abbildung, abgeben, abschreiben, das Abitur, der Abschluss, abwesend, das Alphabet, anwesend, die Aufgabe, die Ausbildung, ausgebildet, aussprechen, die Aussprache

**Szene S-2** (13 Woerter)
- Prämise: Eine Klasse bereitet sich nervös auf eine wichtige Prüfung vor.
- Komischer Dreh: Ein Schüler lernt die falschen Kapitel auswendig und muss in der Prüfung improvisieren.
- Zielwoerter: befriedigend, bestehen, die Bibliothek, die Biologie, der Bleistift, buchstabieren, der Buchstabe, der Dialekt, das Diplom, ergänzen, das Fach, fließend, die Forschung

**Szene S-3** (13 Woerter)
- Prämise: Ein Lehrer diktiert der Klasse einen Text, den kaum jemand fehlerfrei mitschreibt.
- Komischer Dreh: Ein Schüler verhört sich bei jedem zweiten Wort und schreibt einen völlig absurden alternativen Text.
- Zielwoerter: die Fortbildung, das Gedicht, die Geschichte, die Hausaufgabe, das Heft, historisch, das Institut, der Intensivkurs, das Kapitel, die Kenntnisse, der Kindergarten, die Klasse, die Klassenarbeit

**Szene S-4** (13 Woerter)
- Prämise: Ein Austauschstudent versucht am ersten Schultag, sich auf Deutsch vorzustellen.
- Komischer Dreh: Seine Aussprache führt zu einer Kette lustiger Missverständnisse über seinen Namen und seine Herkunft.
- Zielwoerter: sich konzentrieren, korrigieren, der Kugelschreiber, der Kuli, der Kurs, der Kursleiter, die Kursleiter, die Lehre, die Lehrstelle, der Lehrer, die Lehrerin, der Lehrling, lernen

**Szene S-5** (13 Woerter)
- Prämise: Eine Studentin büffelt die ganze Nacht vor einer Prüfung in der Bibliothek.
- Komischer Dreh: Sie merkt erst im Prüfungssaal, dass sie versehentlich für das falsche Fach gelernt hat.
- Zielwoerter: der Lerner, die Lernerin, das Lexikon, die Mappe, markieren, die Matura, mündlich, die Nachhilfe, nachschlagen, die Note, der Ordner, das Papier, die Pause

**Szene S-6** (13 Woerter)
- Prämise: Ein Nachhilfelehrer erklärt einem Schüler zum zehnten Mal dasselbe Grammatikproblem.
- Komischer Dreh: Er erfindet immer abwegigere Eselsbrücken, bis der Schüler es sich endlich merkt.
- Zielwoerter: der Professor, die Professorin, prüfen, die Prüfung, das Referat, der Satz, die Schule, die Schularbeit, der Schüler, die Schülerin, das Semester, das Seminar, die Sprache

**Szene S-7** (13 Woerter)
- Prämise: Eine Schulklasse übt für ein Diktat, das der Lehrer besonders schwer gestaltet hat.
- Komischer Dreh: Ein Schüler schreibt aus Verzweiflung ein komplett neues, aber lautmalerisch ähnliches Wort.
- Zielwoerter: die Fremdsprache, die Muttersprache, die Zweitsprache, der Stift, die Studie, studieren, der Student, die Studentin, der Studierende, die Studierende, das Studium, die Tafel, teilnehmen

**Szene S-8** (13 Woerter)
- Prämise: Ein Professor hält eine Vorlesung, während draußen laute Bauarbeiten stattfinden.
- Komischer Dreh: Er improvisiert seinen Vortrag zu einer Pantomime, weil ihn ohnehin keiner hören kann.
- Zielwoerter: die Teilnahme, der Teilnehmer, die Teilnehmerin, testen, der Test, der Titel, üben, die Übung, übersetzen, der Übersetzer, die Übersetzerin, die Übersetzung, die Universität

**Szene S-9** (13 Woerter)
- Prämise: Ein Kindergarten übt mit den Kindern zum ersten Mal das Alphabet.
- Komischer Dreh: Ein Kind erfindet für jeden Buchstaben eine eigene, völlig fantasievolle Bedeutung.
- Zielwoerter: unterrichten, der Unterricht, unterstreichen, (sich) verbessern, vorlesen, der Vortrag, die Weiterbildung, wiederholen, die Wiederholung, die Wissenschaft, der Wissenschaftler, die Wissenschaftlerin, das Wort

**Szene S-10** (6 Woerter)
- Prämise: Ein Schüler hat die Hausaufgaben vergessen und erfindet eine immer abenteuerlichere Ausrede.
- Komischer Dreh: Die Geschichte wird so unglaubwürdig episch, dass der Lehrer sie am Ende fast bewundert.
- Zielwoerter: das Wörterbuch, die Zeile, das Zertifikat, der Zettel, das Zeugnis, zusammenfassen


### Familie, Beziehungen & Lebensphasen  *(n=114)*

_Verwandtschaft, Partnerschaft, Heirat, Kindheit/Alter, Freundschaft._

**Scenes: 9**

**Szene F-1** (13 Woerter)
- Prämise: Eine Großfamilie trifft sich zum jährlichen Familienfest, bei dem alte Streitigkeiten wieder aufflammen.
- Komischer Dreh: Die Diskussion über einen jahrzehntealten Streit wird immer absurder, bis niemand mehr weiß, worum es ursprünglich ging.
- Zielwoerter: das Alter, das Altenheim, das Altersheim, der Angehörige, die Angehörige, begegnen, begleiten, der Bekannte, die Bekannte, besuchen, der Besuch, betreuen, der Betreuer

**Szene F-2** (13 Woerter)
- Prämise: Ein Paar plant zum ersten Mal, die Eltern des anderen kennenzulernen.
- Komischer Dreh: Beide bereiten sich mit so übertriebenen Verhaltensregeln vor, dass das Treffen völlig steif beginnt, bis ein Missgeschick alles auflockert.
- Zielwoerter: die Betreuerin, die Betreuung, die Beziehung, der Bruder, der Bub, der Cousin, die Cousine, die Ehe, die Ehefrau, das Ehepaar, einladen, die Einladung, die Eltern

**Szene F-3** (13 Woerter)
- Prämise: Zwei Geschwister streiten sich beim Aufräumen des Elternhauses um ein altes Erbstück.
- Komischer Dreh: Der Streit um den wertlosen Gegenstand wird ernster geführt als jede Erbschaftsangelegenheit.
- Zielwoerter: der Enkel, die Enkelin, erwachsen, der Erwachsene, erziehen, die Erziehung, die Familie, der Familienstand, die Frau, der Freund, die Freundschaft, geboren werden, die Geburt

**Szene F-4** (13 Woerter)
- Prämise: Eine Familie bereitet eine Überraschungsfeier zur Hochzeit der Eltern vor.
- Komischer Dreh: Die Planung gerät außer Kontrolle, weil jedes Familienmitglied heimlich eine andere Überraschung organisiert.
- Zielwoerter: der Geburtstag, gemeinsam, die Generation, das Geschenk, geschieden, die Geschwister, der Glückwunsch, gratulieren, die Gratulation, die Hausfrau, der Hausmann, die Heimat, heiraten

**Szene F-5** (13 Woerter)
- Prämise: Ein Kind fragt die Eltern beim Abendessen neugierig nach der Familiengeschichte.
- Komischer Dreh: Die Eltern erzählen die Geschichte so unterschiedlich, dass am Ende zwei komplett verschiedene Versionen entstehen.
- Zielwoerter: die Hochzeit, die Jugend, der Jugendliche, die Jugendliche, jung, der Junge, kennen, kennenlernen, das Kind, die Kindheit, der Kontakt, sich kümmern, küssen

**Szene F-6** (13 Woerter)
- Prämise: Ein junges Paar verabredet sich zum ersten Date in einem Café.
- Komischer Dreh: Beide sind so nervös, dass sie stundenlang über das Wetter reden, bevor einer den Mut zur eigentlichen Frage findet.
- Zielwoerter: der Kuss, leben, das Leben, ledig, lieben, die Liebe, das Mädchen, der Mann, männlich, die Mutter, der Nachbar, die Nachbarin, der Nachwuchs

**Szene F-7** (13 Woerter)
- Prämise: Eine Familie verabschiedet den Sohn, der zum Studium in eine andere Stadt zieht.
- Komischer Dreh: Die Verabschiedung am Bahnhof wird immer emotionaler und länger, bis der Zug fast ohne ihn abfährt.
- Zielwoerter: der Neffe, die Nichte, die Oma, der Onkel, der Opa, der Partner, die Partnerin, sich scheiden lassen, die Scheidung, schenken, die Schwester, Schwieger-, die Senioren

**Szene F-8** (13 Woerter)
- Prämise: Zwei entfernte Cousins treffen sich nach Jahren zufällig wieder und erkennen sich kaum.
- Komischer Dreh: Sie erzählen sich gegenseitig ihre Lebensgeschichte so übertrieben, dass keiner mehr weiß, was stimmt.
- Zielwoerter: der Sohn, die Tante, das Taschengeld, die Tochter, treffen, der Treffpunkt, (sich) trennen, die Trennung, getrennt leben, der Vater, (sich) verabreden, verabredet, die Verabredung

**Szene F-9** (10 Woerter)
- Prämise: Eine Familie kümmert sich gemeinsam um die alternde Großmutter im Altersheim.
- Komischer Dreh: Jeder Besuch endet in einer herzerwärmend chaotischen Diskussion darüber, wer sich zuletzt gemeldet hat.
- Zielwoerter: (sich) verabschieden, der Abschied, das Verhältnis, verheiratet, sich verlieben, verliebt, verwandt, der Verwandte, die Verwandte, weiblich


### Orte & räumliche Lage  *(n=99)*

_Richtungen, Positionen, Stadtgeografie, 'wo/wohin'._

**Scenes: 8**

**Szene O-1** (13 Woerter)
- Prämise: Ein Tourist versucht mit einem völlig veralteten Stadtplan, das Rathaus zu finden.
- Komischer Dreh: Er läuft im Kreis um denselben Platz, bis ein Einheimischer ihm den viel kürzeren Weg zeigt.
- Zielwoerter: abwärts, aufwärts, auseinander, der Ausgang, außen, außerhalb, äußerlich, die Bank, sich befinden, besetzen, die Brücke, da, dahin

**Szene O-2** (13 Woerter)
- Prämise: Ein Taxifahrer erklärt einem ungeduldigen Fahrgast umständlich den Weg zum Ziel.
- Komischer Dreh: Die Wegbeschreibung wird so verwirrend, dass sie am Ende an einem völlig falschen Ort landen.
- Zielwoerter: daneben, direkt, das Dorf, dort, dorthin, draußen, drin, drüben, die Ecke, das Eck, der Eingang, eintreten, entlang

**Szene O-3** (13 Woerter)
- Prämise: Zwei Freunde verabreden sich 'irgendwo in der Nähe des Zentrums' und finden sich nicht.
- Komischer Dreh: Beide stehen an entgegengesetzten Ecken desselben Platzes und rufen sich frustriert an.
- Zielwoerter: das Gebäude, die Gegend, gegenüber, geradeaus, die Hauptstadt, heim, hier/hier-, hierher, hinten, hinter/hinter-, hinterher, innen, inner-

**Szene O-4** (13 Woerter)
- Prämise: Ein Kind versteckt sich beim Versteckspiel an einem besonders unauffindbaren Ort im Garten.
- Komischer Dreh: Es versteckt sich so gut, dass die Suchenden fast aufgeben, bevor es selbst gelangweilt herauskommt.
- Zielwoerter: innerhalb, die Lage, liegen, links, link-, die Metropole, die Mitte, mitten, nächst-, nah, die Nähe, sich nähern, neben

**Szene O-5** (13 Woerter)
- Prämise: Ein Wanderer verirrt sich in einem Wald und orientiert sich nur an vagen Wegweisern.
- Komischer Dreh: Jeder Wegweiser zeigt in eine andere Richtung, sodass er am Ende genau am Ausgangspunkt landet.
- Zielwoerter: nebenan, nirgends, nirgendwo, oben, ober-, der Ort, der Vorort, der Wohnort, der Platz, quer, der Rand, der Raum, rauf/rauf-

**Szene O-6** (13 Woerter)
- Prämise: Ein Möbelpacker soll einen riesigen Schrank exakt an die richtige Stelle im Zimmer rücken.
- Komischer Dreh: Nach zehn Versuchen, ihn in jede Ecke zu schieben, landet er wieder an der ursprünglichen Stelle.
- Zielwoerter: raus/raus-, rechts, recht-, die Region, regional, die Richtung, rückwärts, (sich) setzen, sitzen, der Sitz, die Stadt, städtisch, der Stadtplan

**Szene O-7** (13 Woerter)
- Prämise: Ein Stadtführer erklärt einer Reisegruppe die Geografie der Innenstadt.
- Komischer Dreh: Die Gruppe läuft ihm ständig in die falsche Richtung hinterher, weil alle ihn missverstehen.
- Zielwoerter: stehen, die Stufe, tief, überall, die Umgebung, umgekehrt, unten, unter-, sich verlaufen, vorder-, vorn, vorwärts, der Weg

**Szene O-8** (8 Woerter)
- Prämise: Ein Tourist versucht mit einem völlig veralteten Stadtplan, das Rathaus zu finden.
- Komischer Dreh: Er läuft im Kreis um denselben Platz, bis ein Einheimischer ihm den viel kürzeren Weg zeigt.
- Zielwoerter: weg/weg-, wenden, zentral, das Zentrum, die Zone, der Zugang, zugänglich, zurück/zurück-


### Menge, Maß & Vergleich  *(n=94)*

_Zahlen, Mengenangaben, Vergleiche, Maße._

**Scenes: 7**

**Szene Me-1** (13 Woerter)
- Prämise: Ein Bäcker misst für ein Riesenrezept alle Zutaten in völlig falschen Maßeinheiten ab.
- Komischer Dreh: Am Ende wird der Kuchen so riesig, dass er kaum noch durch die Backofentür passt.
- Zielwoerter: ähnlich, ausreichen, ausreichend, begrenzt, benötigen, berechnen, beschränken, ein bisschen, brauchen, die Breite, die Distanz, doppelt, Doppel-

**Szene Me-2** (13 Woerter)
- Prämise: Zwei Freunde streiten sich beim Kochen darüber, wer die genauere Mengenangabe im Rezept richtig liest.
- Komischer Dreh: Beide bestehen stur auf ihrer Version, bis das Gericht doppelt so scharf wird wie geplant.
- Zielwoerter: der Durchschnitt, durchschnittlich, einzeln, Einzel-, einzig-, die Entfernung, erhöhen, die Erhöhung, etwa, die Fläche, ganz, genug, genügen

**Szene Me-3** (13 Woerter)
- Prämise: Ein Handwerker vermisst ein Zimmer für neue Möbel und verrechnet sich mehrmals.
- Komischer Dreh: Der bestellte Schrank ist am Ende viel zu groß und passt nur diagonal durch die Tür.
- Zielwoerter: gering, gesamt-/Gesamt-, das Gewicht, groß, Groß-, die Größe, halb, die Hälfte, hoch, die Höhe, höchstens, insgesamt, klein

**Szene Me-4** (13 Woerter)
- Prämise: Ein Kind vergleicht stolz seine Süßigkeitensammlung mit der des Nachbarskindes.
- Komischer Dreh: Beide übertreiben die Mengenangaben so lächerlich, dass am Ende niemand mehr die Wahrheit sagt.
- Zielwoerter: knapp, komplett, kurz, lang, die Länge, langsam, leer, leicht, der Mangel, maximal, mehr, mehrere, meist-

**Szene Me-5** (13 Woerter)
- Prämise: Ein Statistiker präsentiert dem Team eine komplizierte Vergleichstabelle.
- Komischer Dreh: Die Zahlen werden bei der Präsentation so oft verwechselt, dass am Ende das genaue Gegenteil bewiesen wird.
- Zielwoerter: meist, die Menge, messen, mindestens, minimal, niedrig, (ein) paar, das Paar, pro, rechnen, reduzieren, reichen, die Reihe

**Szene Me-6** (13 Woerter)
- Prämise: Ein Marktverkäufer wiegt Obst für ungeduldige Kunden auf einer alten Waage.
- Komischer Dreh: Die Waage zeigt bei jedem Kunden ein anderes, absurdes Gewicht an, egal was draufliegt.
- Zielwoerter: die Reihenfolge, relativ, der Rest, riesig, sämtliche, schnell, schwer, sinken, das Stück/-stück, teilen, das Teil, der Teil, total

**Szene Me-7** (16 Woerter)
- Prämise: Zwei Nachbarn vergleichen die Größe ihrer selbst gezüchteten Kürbisse.
- Komischer Dreh: Der Wettstreit eskaliert zu einer improvisierten, viel zu ernst genommenen Messzeremonie im Garten.
- Zielwoerter: übrig, ungefähr, vergrößern, viel/viele, voll, völlig, weit, wenig/wenige, wenigstens, wiegen, die Zahl, die Anzahl, zahlreich, zählen, ziemlich, zusätzlich


### Verkehr & Unterwegs  *(n=92)*

_Verkehrsmittel, Straßenverkehr, Fahren, Ampeln, Staus._

**Scenes: 7**

**Szene V-1** (13 Woerter)
- Prämise: Ein Fahranfänger übt zum ersten Mal das Einparken auf einem vollen Parkplatz.
- Komischer Dreh: Nach zehn erfolglosen Versuchen hilft am Ende die ganze wartende Warteschlange mit Handzeichen mit.
- Zielwoerter: abbiegen, abfahren, die Abfahrt, die Ampel, der Anschluss, anschnallen, die Ausfahrt, das Auto, die Autobahn, die Bahn, S-Bahn, die Straßenbahn, die U-Bahn

**Szene V-2** (13 Woerter)
- Prämise: Ein Busfahrer erklärt genervten Fahrgästen die Ursache einer langen Verspätung.
- Komischer Dreh: Seine Erklärung wird mit jedem Satz unglaubwürdiger, bis die Fahrgäste selbst Wetten über die wahre Ursache abschließen.
- Zielwoerter: der Bahnhof, der Bahnsteig, das Benzin, das Boot, bremsen, die Bremse, der Bus, die Einbahnstraße, die Einfahrt, einsteigen, die Eisenbahn, fahren, die Fähre

**Szene V-3** (13 Woerter)
- Prämise: Zwei Radfahrer navigieren gemeinsam durch den dichten Stadtverkehr zur Stoßzeit.
- Komischer Dreh: Sie geraten ständig in die falsche Einbahnstraße und müssen unter Gelächter der Passanten wenden.
- Zielwoerter: die Fahrbahn, der Fahrer, das Fahrrad, das Fahrzeug, der Führerausweis, der Führerschein, der Fußgänger, die Fußgängerin, die Fußgängerzone, der Gehsteig, die Geschwindigkeit, die Geschwindigkeitsbeschränkung, das Gleis

**Szene V-4** (13 Woerter)
- Prämise: Ein Fahrschüler wird von seiner Fahrlehrerin bei der praktischen Prüfung genau beobachtet.
- Komischer Dreh: Er verwechselt in der Aufregung Bremse und Gas und fährt eine unfreiwillige Ehrenrunde um den Parkplatz.
- Zielwoerter: halten, der Halt, die Haltestelle, der Hauptbahnhof, hupen, das Kennzeichen, das Kraftfahrzeug, die Kreuzung, die Kurve, der Laster, losfahren, die Mobilität, der Motor

**Szene V-5** (13 Woerter)
- Prämise: Ein Autofahrer steckt im größten Stau des Jahres fest und verpasst dadurch einen wichtigen Termin.
- Komischer Dreh: Er versucht, per Handzeichen mit dem Nachbarauto Konversation zu betreiben, um sich die Zeit zu vertreiben.
- Zielwoerter: das Motorrad, die Panne, parken, parkieren, der Perron, das Rad, der Radfahrer, die Radfahrerin, der Reifen, die Rücksicht, das Schild, der Speisewagen, die Spur

**Szene V-6** (13 Woerter)
- Prämise: Ein Zugbegleiter kontrolliert die Fahrkarten in einem völlig überfüllten Zugabteil.
- Komischer Dreh: Ein Fahrgast hat sein Ticket so gut versteckt, dass die Suche zu einer minutenlangen Slapstick-Einlage wird.
- Zielwoerter: starten, der Start, der Stau, stehen bleiben, stoppen, die Straße, die Strecke, tanken, die Tankstelle, das Tempo, das Tram, transportieren, der Transport

**Szene V-7** (14 Woerter)
- Prämise: Eine Fahrradkurierin liefert an einem chaotischen Tag Pakete quer durch die Stadt.
- Komischer Dreh: Jede Route wird durch eine neue Baustelle blockiert, sodass sie am Ende Umwege durch halb die Stadt fährt.
- Zielwoerter: das Trottoir, überholen, überqueren, die Umleitung, umsteigen, unterwegs, das Velo, der Verkehr, das Verkehrsmittel, die Vorfahrt, der Wagen, die Werkstatt, das Verkehrszeichen, der Zug


### Natur, Wetter & Tiere  *(n=89)*

_Landschaft, Klima, Pflanzen, Tiere, Naturphänomene._

**Scenes: 7**

**Szene T-1** (13 Woerter)
- Prämise: Ein Bauer beobachtet besorgt den Himmel, weil ein Gewitter die Ernte bedroht.
- Komischer Dreh: Er versucht mit allen möglichen Aberglauben, das Wetter zu beeinflussen, während die Familie ihn amüsiert beobachtet.
- Zielwoerter: der Baum, der Berg, das Blatt, blitzen, der Blitz, blühen, die Blume, donnern, der Donner, die Erde, die Ernte, das Feld, feucht

**Szene T-2** (13 Woerter)
- Prämise: Eine Wandergruppe wird auf einem Berggipfel von plötzlichem Schneefall überrascht.
- Komischer Dreh: Sie improvisieren mit Regenjacken und Picknickdecken eine völlig unpassende Notunterkunft.
- Zielwoerter: fließen, der Fluss, im Freien, fressen, füttern, das Gebiet, das Gebirge, das Gewitter, das Gras, hageln, heiß, der Himmel, die Hitze

**Szene T-3** (13 Woerter)
- Prämise: Ein Tierpfleger im Zoo versucht, ein entlaufenes Tier wieder einzufangen.
- Komischer Dreh: Das Tier führt ihn quer durch den ganzen Park, bis es sich schließlich freiwillig in sein Gehege zurücklegt.
- Zielwoerter: der Bauernhof, der Hügel, die Hütte, die Insel, kalt, die Kälte, das Klima, kühl, die Küste, das Land, die Landwirtschaft, die Landschaft, die Luft

**Szene T-4** (13 Woerter)
- Prämise: Eine Familie campt zum ersten Mal am See und wird nachts von Tiergeräuschen geweckt.
- Komischer Dreh: Jeder erfindet eine immer wildere Theorie, welches Monster wohl vor dem Zelt lauert, bis sich ein Igel als Übeltäter entpuppt.
- Zielwoerter: das Meer, mild, der Mond, nass, die Natur, der Nebel, neblig, der Ozean, pflanzen, die Pflanze, der Rasen, regnen, der Regen

**Szene T-5** (13 Woerter)
- Prämise: Ein Gärtner kämpft den ganzen Sommer gegen hartnäckiges Unkraut in seinem Garten.
- Komischer Dreh: Er entwickelt immer skurrilere Methoden, bis das Unkraut am Ende widerstandsfähiger wirkt als jede Pflanze, die er eigentlich ziehen wollte.
- Zielwoerter: die Rose, der Sand, der Schatten, scheinen, die Schlange, der Schnee, schneien, der See, die See, die Nord-/Ostsee, die Sonne, sonnig, steil

**Szene T-6** (13 Woerter)
- Prämise: Ein Meteorologe muss live im Fernsehen eine völlig falsche Wettervorhersage korrigieren.
- Komischer Dreh: Während er redet, zieht draußen ausgerechnet das genaue Gegenteil seiner Vorhersage auf.
- Zielwoerter: der Stein, der Stern, der Sturm, das Tal, die Temperatur, das Tier, das Haustier, trocken, das Ufer, wachsen, der Wald, warm, die Wärme

**Szene T-7** (11 Woerter)
- Prämise: Ein Angler verbringt einen ganzen Tag am Fluss, ohne einen einzigen Fisch zu fangen.
- Komischer Dreh: Er erzählt am Abend eine immer größere Geschichte über den 'einen, der ihm entwischt ist'.
- Zielwoerter: die Welt, weltweit, das Wetter, der Wetterbericht, die Wettervorhersage, wild, die Wiese, der Wind, windig, die Wolke, bewölkt


### Eigenschaften & Bewertung  *(n=73)*

_Allgemeine Adjektive zum Beschreiben und Bewerten von Dingen._

**Scenes: 6**

**Szene Ei-1** (13 Woerter)
- Prämise: Eine Kritikerin bewertet in ihrer Kolumne ein neu eröffnetes Restaurant.
- Komischer Dreh: Sie findet für jedes Detail ein anderes, immer übertrieberenes Adjektiv, bis die Kritik komplett widersprüchlich wird.
- Zielwoerter: absolut, aktiv, allgemein, alt, anstrengend, ausgezeichnet, automatisch, bequem, bereit, berühmt, besonder-, besonders, bestimmt

**Szene Ei-2** (13 Woerter)
- Prämise: Zwei Freunde bewerten nach dem Kinobesuch denselben Film völlig gegensätzlich.
- Komischer Dreh: Ihr Streit über 'gut' und 'schlecht' wird zur komischen Materialschlacht aus Superlativen.
- Zielwoerter: deutlich, dringend, dumm, durcheinander, echt, eindeutig, einfach, einheitlich, extrem, falsch, fantastisch, fertig, fest

**Szene Ei-3** (13 Woerter)
- Prämise: Ein Immobilienmakler beschreibt einer Kundin eine winzige, wenig einladende Wohnung.
- Komischer Dreh: Er findet für jeden offensichtlichen Mangel ein positiv klingendes Wort, bis die Beschreibung völlig absurd wird.
- Zielwoerter: flexibel, frei, gemütlich, genau, gründlich, gut, hässlich, hübsch, ideal, individuell, intelligent, die Intelligenz, intensiv

**Szene Ei-4** (13 Woerter)
- Prämise: Ein Kind beschreibt der Lehrerin sein Wochenende in immer übertriebeneren Worten.
- Komischer Dreh: Aus einem gewöhnlichen Spaziergang wird in der Erzählung ein episches, gefährliches Abenteuer.
- Zielwoerter: interessant, klar, klasse, klug, kompliziert, korrekt, kreativ, locker, modern, negativ, neu, normal, offen

**Szene Ei-5** (13 Woerter)
- Prämise: Zwei Nachbarn vergleichen stolz ihre frisch renovierten Gärten.
- Komischer Dreh: Jeder übertrumpft die Beschreibung des anderen mit immer superlativischeren Adjektiven.
- Zielwoerter: ordentlich, passiv, perfekt, positiv, praktisch, prima, richtig, schlecht, schlimm, schön, schwierig, Spezial-, speziell

**Szene Ei-6** (8 Woerter)
- Prämise: Ein Verkäufer preist einem Kunden ein mittelmäßiges Produkt in höchsten Tönen an.
- Komischer Dreh: Seine Übertreibungen werden so offensichtlich, dass der Kunde am Ende aus Neugier trotzdem kauft.
- Zielwoerter: super, toll, typisch, ungewöhnlich, unglaublich, vernünftig, wunderbar, wunderschön


### Reisen & Urlaub  *(n=67)*

_Flughafen, Hotel, Gepäck, Sehenswürdigkeiten, Grenzen._

**Scenes: 5**

**Szene R-1** (13 Woerter)
- Prämise: Eine Familie checkt gestresst und mit viel zu viel Gepäck am Flughafenschalter ein.
- Komischer Dreh: Der Koffer ist so überladen, dass er beim Wiegen fast die Anzeige sprengt und alle improvisieren müssen, was rausfliegt.
- Zielwoerter: ankommen, die Ankunft, der Aufenthalt, der Ausflug, das Ausland, die Aussicht, besichtigen, das Billett, buchen, die Burg, das Denkmal, einpacken, die Fahrkarte

**Szene R-2** (13 Woerter)
- Prämise: Ein Hotelrezeptionist begrüßt Gäste, deren Zimmer versehentlich doppelt gebucht wurde.
- Komischer Dreh: Die Lösung des Problems wird zu einer immer komplizierteren Verhandlung über Aussicht, Etage und Frühstückszeiten.
- Zielwoerter: der Fahrplan, die Ferien (Pl.), Ferien-, fliegen, der Flug, der Flughafen, das Flugzeug, das Gepäck, die Grenze, der Hafen, die Halbpension, das Hotel, die Jugendherberge

**Szene R-3** (13 Woerter)
- Prämise: Ein Reiseleiter führt eine Touristengruppe zu einer berühmten Sehenswürdigkeit.
- Komischer Dreh: Die Hälfte der Gruppe verläuft sich prompt und taucht erst beim Abendessen wieder auf, mit einer abenteuerlichen Geschichte.
- Zielwoerter: die Kabine, die Karte, der Koffer, landen, die Landung, packen, der Pass, der Passagier, die Passagierin, die Pension, der Prospekt, reisen, die Reise

**Szene R-4** (13 Woerter)
- Prämise: Eine Familie plant akribisch die Route für einen Roadtrip in den Urlaub.
- Komischer Dreh: Der Plan wird schon am ersten Tag über den Haufen geworfen, weil alle spontan einem Schild zu einer Kuriosität folgen.
- Zielwoerter: das Reisebüro, reservieren, die Reservierung, die Rezeption/Reception, der Rucksack, die Rückfahrt, die Rückkehr, die Rundfahrt, das Schiff, die Sehenswürdigkeit, das Souvenir, der Steward, die Stewardess

**Szene R-5** (15 Woerter)
- Prämise: Ein Backpacker versucht an der Grenze, mit wenigen Wörtern den Zollbeamten zu überzeugen.
- Komischer Dreh: Seine improvisierte Erklärung für den riesigen Rucksack wird immer abenteuerlicher und unglaubwürdiger.
- Zielwoerter: der Strand, die Tasche, das Ticket, der Tourismus, der Tourist, die Touristin, der Turm, übernachten, die Übernachtung, die Unterkunft, der Urlaub, verreisen, das Visum, das Zelt, zelten


### Alltagshandlungen (allgemeine Verben)  *(n=62)*

_Häufige, thematisch neutrale Tätigkeitsverben des Alltags._

**Scenes: 5**

**Szene H-1** (13 Woerter)
- Prämise: Ein Vater bringt seinem Kind zum ersten Mal bei, den Tisch richtig zu decken.
- Komischer Dreh: Das Kind nimmt die Anweisung so wörtlich, dass am Ende jedes Familienmitglied drei Gabeln bekommt.
- Zielwoerter: abholen, aufheben, ausmachen, bekommen, benutzen, bleiben, bringen, drehen, drücken, entfernen, erhalten, erledigen, fallen

**Szene H-2** (13 Woerter)
- Prämise: Zwei Mitbewohner teilen sich zum ersten Mal die Hausarbeit nach einem genauen Plan.
- Komischer Dreh: Der Plan gerät völlig durcheinander, weil beide ständig dieselbe Aufgabe gleichzeitig erledigen wollen.
- Zielwoerter: fassen, festhalten, geben, gebrauchen, gehen, greifen, gucken, hängen, heben, (hinunter) runterwerfen, holen, kleben, klopfen

**Szene H-3** (13 Woerter)
- Prämise: Ein Umzugshelfer trägt schwere Kisten die enge Treppe hinauf.
- Komischer Dreh: Bei jeder Kiste stellt sich heraus, dass der Inhalt viel absurder ist, als das Etikett vermuten lässt.
- Zielwoerter: kommen, kriegen, laufen, legen, machen, nehmen, nutzen, nützen, öffnen, ordnen, schauen, schieben, schlagen

**Szene H-4** (13 Woerter)
- Prämise: Ein Kind räumt widerwillig sein Zimmer auf, bevor Besuch kommt.
- Komischer Dreh: Es stopft alles so kreativ unter das Bett, dass die Aufräumaktion am Ende länger dauert als geplant.
- Zielwoerter: schließen, der Schritt, schütteln, sehen, springen, stecken, steigen, stellen, suchen, treiben, treten, tun, (sich) umdrehen

**Szene H-5** (10 Woerter)
- Prämise: Eine Gruppe Freiwilliger hilft beim Aufbau eines Zeltes für das Stadtfest.
- Komischer Dreh: Die Anleitung wird völlig falsch verstanden, sodass das Zelt am Ende in eine völlig andere Form gebogen wird.
- Zielwoerter: umgehen, verlassen, (sich) verstecken, verteilen, verwenden, werfen, zeigen, ziehen, zugehen, zumachen


### Farben, Formen & Material  *(n=41)*

_Farbadjektive, geometrische Formen, Materialbeschaffenheit._

**Scenes: 3**

**Szene Fa-1** (13 Woerter)
- Prämise: Ein Maler streicht das Kinderzimmer und lässt das Kind die Farbe mitbestimmen.
- Komischer Dreh: Das Kind will unbedingt alle Farben gleichzeitig, und am Ende sieht die Wand aus wie ein Regenbogen-Unfall.
- Zielwoerter: der Bogen, breit, bunt, dicht, dunkel, dünn, eckig, eng, die Farbe, farbig, flach, der Fleck, die Form

**Szene Fa-2** (13 Woerter)
- Prämise: Ein Designer präsentiert dem Kunden Muster für die neue Firmenkollektion.
- Komischer Dreh: Der Kunde kann sich zwischen zwei fast identischen Farbtönen partout nicht entscheiden und diskutiert stundenlang.
- Zielwoerter: glatt, das Gold, hart, hell, das Holz, der Kreis, das Kreuz, künstlich, der Kunststoff, laut, das Leder, leise, die Linie

**Szene Fa-3** (15 Woerter)
- Prämise: Ein Kind baut aus Bauklötzen ein Haus mit möglichst vielen verschiedenen Formen.
- Komischer Dreh: Das Ergebnis wird so bizarr, dass niemand mehr erkennt, ob es ein Haus oder ein Turm sein soll.
- Zielwoerter: das Loch, das Material, das Metall, parallel, das Plastik, rein, rund, schief, schmal, senkrecht, spitz, der Stoff, waagerecht, weich, die Wolle


### Gefahr, Notfall & Sicherheit  *(n=38)*

_Unfälle, Notrufe, Brand, Warnungen, Schutz._

**Scenes: 3**

**Szene N-1** (13 Woerter)
- Prämise: Eine Feuerwehrübung simuliert einen kleinen Küchenbrand in einer Turnhalle.
- Komischer Dreh: Die Übung gerät außer Kontrolle, weil der Trainer selbst in Panik gerät und die falschen Anweisungen ruft.
- Zielwoerter: Achtung!, der Alarm, beschädigen, brennen, das Feuer, die Feuerwehr, fliehen, die Flucht, die Gefahr, gefährlich, das Gift, giftig, kaputt

**Szene N-2** (13 Woerter)
- Prämise: Ein Rettungsschwimmer übt am Strand mit Freiwilligen eine Notfallrettung.
- Komischer Dreh: Der 'gerettete' Freiwillige übertreibt seine Panik so sehr, dass er die eigentliche Rettung fast verhindert.
- Zielwoerter: kaputtgehen, kaputtmachen, die Katastrophe, der Lärm, der Notausgang, der Notfall, der Notruf, retten, das Risiko, schaden, der Schaden, schädlich, schützen

**Szene N-3** (12 Woerter)
- Prämise: Eine Sicherheitsbeauftragte erklärt neuen Mitarbeitern die Fluchtwege im Bürogebäude.
- Komischer Dreh: Ein Mitarbeiter verirrt sich prompt bei der Übung und muss selbst gerettet werden.
- Zielwoerter: der Schutz, die Sicherheit, sichern, tödlich, überfahren, der Unfall, das Unglück, (sich) verbrennen, die Vorsicht, vorsichtig, warnen, zerstören


### Kleidung & Aussehen  *(n=38)*

_Kleidungsstücke, Anziehen, äußere Erscheinung._

**Scenes: 3**

**Szene L-1** (13 Woerter)
- Prämise: Eine Familie sucht panisch die passende Kleidung für eine formelle Hochzeitsfeier.
- Komischer Dreh: Am Ende trägt jeder ein Kleidungsstück, das eigentlich für einen ganz anderen Anlass gedacht war.
- Zielwoerter: anhaben, (sich) anziehen, der Anzug, aussehen, die Bluse, chic/schick, elegant, die Frisur, die Garderobe, das Hemd, die Hose, der Hut, die Jacke

**Szene L-2** (13 Woerter)
- Prämise: Ein Verkäufer in der Boutique hilft einem unsicheren Kunden bei der Anprobe.
- Komischer Dreh: Der Kunde probiert so viele Kombinationen an, dass die Umkleidekabine am Ende aussieht wie ein Kleiderschrank-Chaos.
- Zielwoerter: die Jeans, die Kette, das Kleid, die Kleidung, der Knopf, das Kostüm, der Mantel, die Mode, die Nadel, nähen, passen, der Pullover, der Ring

**Szene L-3** (12 Woerter)
- Prämise: Ein Kind besteht darauf, sich für den Kindergarten völlig allein anzuziehen.
- Komischer Dreh: Das Ergebnis ist eine herrlich schiefe Kombination aus Gummistiefeln, Faschingskostüm und Winterjacke im Sommer.
- Zielwoerter: der Rock, der Schirm, der Schmuck, der Schuh, die Socke, der Stil, der Stiefel, der Strumpf, tragen, das Tuch, sich umziehen, die Uniform


### Umwelt, Energie & Wirtschaft  *(n=16)*

_Umweltschutz, Industrie, Ressourcen, Wirtschaft im Großen._

**Scenes: 1**

**Szene U-1** (16 Woerter)
- Prämise: Eine Umweltgruppe organisiert eine Aufräumaktion am Flussufer.
- Komischer Dreh: Die gefundenen Gegenstände werden immer kurioser, bis eine improvisierte Ausstellung des 'schrägsten Mülls' entsteht.
- Zielwoerter: Abgase, die Energie, entsorgen, der Export, der Import, die Industrie, das Kraftwerk, Öko-, produzieren, das Produkt, die Produktion, verschmutzen, die Umwelt, der Umweltschutz, die Umweltverschmutzung, die Wirtschaft


## 5. Anmerkungen zu Ermessensentscheidungen

- **Regionale Varianten** (D/A/CH-Cross-References mit '→', z. B. 'Brötchen → A: Semmel; CH: Brötli') wurden NICHT als zusaetzliche Lemmata gezaehlt — jede regionale Variante steht in der Wortliste ohnehin als eigene Zeile (Semmel, Brötli, Brötchen sind je eigene Zeilen) und wurde einzeln zugeordnet.

- **Mehrfach-Kopfwoerter** (';'-getrennt, z. B. 'der Hörer, -; die Hörerin, -nen; der Zuhörer') wurden alle als Lemmata in der Wortliste der jeweiligen Zeile erfasst, zaehlen aber fuer die Coverage nur als EINE Zeile (Coverage wird ueber Zeilen, nicht ueber Einzel-Lemmata gemessen — sonst waere '2886' als Nenner nicht konsistent moeglich).

- **Maskulin/Feminin-Formenpaare** (z. B. 'der Lehrer, - / die Lehrerin, -nen') stehen ebenfalls als eine Zeile, aber beide Formen erscheinen im Wortpool der Szenen — so bekommt keine Form 'unsichtbar' den Anki-Karten-Anker verloren.

- **Homonyme** (21 Woerter kommen als eigenstaendige, unterschiedlich bedeutende Zeilen doppelt vor, z. B. 'die Bank' als Sitzbank UND als Geldinstitut, 'das Eis' als Speiseeis UND als gefrorenes Wasser): wo die beiden Bedeutungen klar unterschiedlichen Themen zuzuordnen waren, wurden sie getrennt (Bank-Sitzbank -> Orte, Bank-Geldinstitut -> Einkaufen/Geld). Wo die zweite Bedeutung praktisch identisch blieb (Eis, kosten, Praxis, Pension, Ordination, Rad, Wort, Ausdruck, Zuhörer u. a.), wurden beide Zeilen demselben Thema zugeordnet — leichte Redundanz in der Row-Coverage, aber kein inhaltlicher Fehler.

- **Ambige Woerter** wurden dem Thema zugeordnet, in dem sie in einer B1-Alltagsszene am wahrscheinlichsten vorkommen (z. B. 'der Gang' -> Wohnung/Flur statt Speisefolge; 'das Gericht' -> Essen/Gericht als Speise statt Gericht/Justiz; 'die Praxis' -> Gesundheit als Arztpraxis statt Theorie-vs-Praxis-Abstraktum).

- **Szenengroesse:** Zielgroesse 13 Woerter/Szene (Bereich ca. 10–15 laut Vorgabe); kleine Restgruppen (<5 Woerter) wurden in die vorherige Szene desselben Themas gemergt, damit keine Mini-Szenen mit nur 1–2 Woertern entstehen.

- **Szenen-Praemissen** sind bewusst so gehalten, dass die Situation zum Thema passt, aber nicht wortwoertlich jedes Zielwort vorwegnimmt — die eigentliche deutsche Szene (mit den Zielwoertern eingebaut) folgt in einem spaeteren Schritt.


**coverage: 2886/2886 (100.0%)**

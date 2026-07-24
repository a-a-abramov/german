import csv, re

CSV_PATH = '/Users/andrey/anki/goethe-b1-wortliste.csv'

def clean_line(line):
    line = line.strip()
    line = line.replace('(sich)', '\x00SICH\x00')
    line = re.sub(r'\s*\([^)]*\)', '', line)
    line = line.replace('\x00SICH\x00', '(sich)')
    return line.strip()

def load_entries():
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    rows = rows[1:]
    entries = []
    for i, r in enumerate(rows):
        raw = r[0]
        lines = raw.split('\n')
        headword_lines = [l for l in lines if not l.strip().startswith('→')]
        lemmas = []
        for hl in headword_lines:
            hl = clean_line(hl)
            if not hl:
                continue
            first = hl.split(',')[0].strip()
            if first:
                lemmas.append(first)
        canonical = " / ".join(dict.fromkeys(lemmas))
        entries.append({'idx': i, 'raw': raw, 'canonical': canonical})
    return entries

# ---------------------------------------------------------------------------
# TOPICS: topic_name -> list of canonical lemma strings (must match
# entries[i]['canonical'] exactly). Order of appearance across all topic
# lists is used to greedily consume entry indices for duplicate strings
# (e.g. "die Bank" bench vs bank) so each occurrence lands on a distinct row.
# ---------------------------------------------------------------------------
TOPICS = {}

def add(topic, words):
    TOPICS.setdefault(topic, [])
    TOPICS[topic].extend(words)

# =====================================================================
# CHUNK 1: idx 0-299
# =====================================================================
add('Grammatik & Verbindungswörter', ['ab','aber','als','als ob','also','an','auf','aus'])
add('Unterwegs & Verkehr', ['abbiegen','abfahren','die Abfahrt','abwärts','die Ampel','aufwärts',
    'Achtung!'])
add('Schule & Bildung', ['die Abbildung','abschreiben','das Abitur','der Abschluss','der Abschnitt',
    'anwenden','anwesend','abwesend','das Alphabet','analysieren','die Ausbildung','ausgebildet',
    'aussprechen','die Aussprache'])
add('Freizeit, Medien & Technik', ['das Abenteuer','abonnieren','das Abonnement','sich amüsieren',
    'die Aktivität','anklicken','ansehen','aufnehmen','die Aufnahme','auftreten','der Auftritt',
    'aufführen','ausgehen','die Ausstellung','ausstellen','automatisch','der Autor / die Autorin'])
add('Handlungen: Alltagsverben', ['abgeben','abheben','abholen','abmachen','abnehmen','absagen',
    'abstimmen','ändern','die Änderung','anfangen','aufhalten','aufheben','aufhören','aufladen',
    'ausmachen','anschließen','ausziehen','aufräumen','aufpassen'])
add('Denken, Wissen & Meinen', ['abhängen','abhängig','die Ahnung','ablehnen','die Absicht',
    'achten','auffallen','aufmerksam','ausschließen','ausschließlich','die Alternative',
    'alternativ','die Ausnahme','annehmen'])
add('Einkaufen & Geld', ['abheben','die Abteilung','die Aktion','anbieten','der Anbieter',
    'das Angebot','anschaffen','die Ausgabe','ausgeben','die Ausnahme','aussuchen','auswählen',
    'die Auswahl','der Automat'])
add('Menge, Maß & Eigenschaften', ['absolut','allgemein','ähnlich','all-','aller-','ander-',
    'andererseits','anders','ausgezeichnet','ausreichend','ausreichen'])
add('In der Wohnung & Zuhause', ['der Abfall','der Abfalleimer','abwaschen','der Abwart / die Abwartin',
    'die Anleitung','der Aufzug','außen','ausmachen','das Apartment'])
add('Natur, Wetter & Umwelt', ['Abgase'])
add('Familie & Beziehungen', ['der Angehörige / die Angehörige','alt','das Alter','das Altenheim',
    'das Altersheim'])
add('Gefühle & Charakter', ['die Angst','ängstlich','angenehm','allein','aktiv','(sich) ärgern',
    'der Ärger','ärgerlich','arm'])
add('Kommunikation & Post', ['die Adresse','der Absender / die Absenderin','ankündigen','ansprechen',
    'antworten','die Antwort','anrufen','der Anruf','der Anrufbeantworter','die Ansage',
    'die Annonce','die Anrede','ausrichten','die Auskunft','der Apparat','ausdrucken',
    'der Ausdruck'])
add('Stadt, Ämter & Recht', ['das Amt','der Antrag','anmelden','die Anmeldung','angeben',
    'die Angabe','ausfüllen','der Ausweis','der Anwalt / die Anwältin','anzeigen','die Anzeige',
    'der Alarm'])
add('Arbeit & Beruf', ['anerkennen','der Anspruch','anstellen','der Angestellte / die Angestellte',
    'sich anstrengen','anstrengend','der Auftrag','die Aushilfe','der Architekt / die Architektin'])
add('Kleidung & Aussehen', ['anhaben','(sich) anziehen','der Anzug','aussehen'])
add('Körper & Gesundheit', ['abnehmen','der Arm','die Apotheke','der Appetit','der Arzt / die Ärztin',
    'atmen','der Atem','(sich) ausruhen','äußerlich','das Asyl'])
add('Reisen & Urlaub', ['der Aufenthalt','ankommen','die Ankunft','der Ausflug','das Ausland',
    'die Auskunft'])
add('Zeit & Kalender', ['der Alltag','alltäglich','anfangs','der Anfang','aufstehen','aufwachen',
    'der Augenblick'])
add('Gesellschaft, Politik & Wirtschaft', ['der Ausländer / die Ausländerin','ausländisch',
    'außerhalb'])
add('Essen, Kochen & Restaurant', ['der Apfel','die Aprikose','der Alkohol'])


# =====================================================================
# CHUNK 2: idx 300-599
# =====================================================================
add('Grammatik & Verbindungswörter', ['bevor','bis','bisher','ein bisschen','bitte','bloß',
    'derselbe','dass','denn','deshalb','deswegen','doch','dies-','diesmal'])
add('Denken, Wissen & Meinen', ['bekannt','bemerken','sich irren','beweisen','der Beweis',
    'begründen','die Begründung','beschließen','der Gedanke','denken',
    'der Bescheid','Bescheid sagen','Bescheid geben'])
add('Handlungen: Alltagsverben', ['bekommen','benötigen','benutzen','beobachten','beraten',
    'die Beratung','berechnen','sich bemühen','beschränken','beschreiben','die Beschreibung',
    'besitzen','besorgen','besprechen','die Besprechung','bestätigen','die Bestätigung',
    'bestehen','bestellen','betreuen','der Betreuer / die Betreuerin','die Betreuung',
    'dienen','danken','der Dank','dankbar','danke','darstellen','die Darstellung','dekorieren',
    'behalten','behandeln','der Beitrag','klagen'])
add('Freizeit, Medien & Technik', ['der Beleg','beliebt','das Ballett','die Bibliothek','das Bild',
    'der Bildschirm','das Billett','die Biologie','klettern','die Broschüre','die Bühne',
    'die Datei','die Daten','das Denkmal','der Dialekt','der Dialog','digital','das Diplom',
    'die Diskothek','diskutieren','die Diskussion','dekorieren'])
add('Gefühle & Charakter', ['beleidigen','beruhigen','betrunken','die Bewegung','begeistert',
    'blass','böse','dumm','dankbar'])
add('Körper & Gesundheit', ['der Bauch','beschädigen','die Besserung','der Bart','bluten',
    'das Blut','der Blick','blind','die Brust','die Diät'])
add('Arbeit & Beruf', ['beruflich','berufstätig','der Beruf','der Betrieb',
    'der Betriebsrat / die Betriebsrätin','sich bewerben','die Bewerbung','das Diplom',
    ])
add('Einkaufen & Geld', ['bezahlen','der Betrag','billig','bitter','der Bogen','die Bohne',
    'das Benzin','das Bargeld','bar'])
add('Familie & Beziehungen', ['die Beziehung','der Bewohner / die Bewohnerin','die Bevölkerung',
    'der Bruder',])
add('In der Wohnung & Zuhause', ['das Bett','der Bau','bauen','die Baustelle','das Blatt',
    'der Boden','das Brot',])
add('Natur, Wetter & Umwelt', ['der Baum','blühen','die Blume','blitzen','der Blitz','die Birne',
    ])
add('Tiere', ['der Bauer',])
add('Stadt, Ämter & Recht', ['der Beamte / die Beamtin','beantragen','die Behörde','betrügen',
    'bestrafen','beweisen','der Bürger / die Bürgerin'])
add('Kommunikation & Post', ['beantworten','sich beschweren','die Botschaft','der Brief',
    'der Briefkasten','die Briefmarke','der Briefträger','der Briefumschlag','die Brieftasche',
    'buchstabieren','der Buchstabe'])
add('Schule & Bildung', ['besichtigen','die Bibliothek','das Buch','die Buchhandlung','buchen',
    'die Biologie'])
add('Reisen & Urlaub', ['besuchen','der Besuch','das Boot','buchen','der Bus'])
add('Zeit & Kalender', ['bald','bevor','damals','danach','dann','dauern','die Dauer','dauernd',
    'das Datum','diesmal'])
add('Menge, Maß & Eigenschaften', ['besonder-','besonders','bestimmt','breit','die Breite',
    'bequem','bunt','dick','dicht','deutlich','der Bedarf'])
add('Kleidung & Aussehen', ['die Bluse','die Brille',
    'blond'])
add('In der Wohnung & Zuhause', ['die Decke','die Bürste','die Zahnbürste','die Couch'])
add('Unterwegs & Verkehr', ['bremsen','die Bremse',
    'der Bus'])
add('Essen, Kochen & Restaurant', ['braten','der Braten','brechen','das Brot','das Brötchen',
    'das Brötli','die Butter','das Buffet','die Bohne','das Café','die Cafeteria','bitter',
    ])
add('Gesellschaft, Politik & Wirtschaft', ['die Chance','die Bevölkerung'])
add('Familie & Beziehungen', ['der Bub','der Chef / die Chefin','die Dame','der Coiffeur / die Coiffeuse',
    'der Cousin / die Cousine'])
add('Kleidung & Aussehen', ['chic/schick','die Creme','das Couvert'])
add('Handlungen: Alltagsverben', ['bringen','drehen','drucken','der Drucker','drücken','der Druck'])
add('Denken, Wissen & Meinen', ['die Distanz','doch'])
add('Stadt, Ämter & Recht', ['der Dieb',
    'der Dienst','das Dokument','die Droge','die Drogerie'])
add('Zeit & Kalender', ['donnern','der Donner','doppelt','Doppel-'])
add('Natur, Wetter & Umwelt', ['das Dorf','draußen','der Dreck'])
add('Gefühle & Charakter', ['dringend'])
add('Grammatik & Verbindungswörter', ['dort','dorthin','drüben','drin','durch','durcheinander',
    'dürfen'])
add('Körper & Gesundheit', ['dunkel','dünn','der Durst','durstig','(sich) duschen','die Dusche'])
add('Menge, Maß & Eigenschaften', ['der Durchschnitt','durchschnittlich','echt','eckig'])
add('Kommunikation & Post', ['die Durchsage','duzen','die e-card','die ec-Karte/EC-Karte'])
add('In der Wohnung & Zuhause', ['die Ecke','das Eck'])
add('Gesellschaft, Politik & Wirtschaft', ['egal'])
add('Familie & Beziehungen', ['die Ehe','die Ehefrau','das Ehepaar',])
add('Menge, Maß & Eigenschaften', ['eher','ehrlich'])
add('Essen, Kochen & Restaurant', ['das Ei'])
add('Grammatik & Verbindungswörter', ['eigen-','eigentlich'])
add('Gefühle & Charakter', ['sich eignen','geeignet','eilen','die Eile','eilig'])
add('Unterwegs & Verkehr', ['ein-','die Einbahnstraße','die Einfahrt'])
add('Stadt, Ämter & Recht', ['einbrechen','der Einbrecher / die Einbrecherin','der Einbruch'])
add('Menge, Maß & Eigenschaften', ['eindeutig','einheitlich','einig-'])
add('Denken, Wissen & Meinen', ['der Eindruck','einerseits','sich einigen'])
add('Menge, Maß & Eigenschaften', ['einfach'])
add('Denken, Wissen & Meinen', ['einfallen','der Einfall','der Einfluss','beeinflussen'])
add('Freizeit, Medien & Technik', ['einfügen'])
add('Einkaufen & Geld', ['einführen','die Einführung','einkaufen','der Einkauf','das Einkommen',
    'einnehmen','die Einnahme','einzahlen','die Einzahlung'])
add('Familie & Beziehungen', ['einladen','die Einladung'])
add('Zeit & Kalender', ['einmal'])
add('Reisen & Urlaub', ['einpacken'])
add('In der Wohnung & Zuhause', ['einrichten','die Einrichtung'])
add('Gefühle & Charakter', ['einsam'])
add('Freizeit, Medien & Technik', ['einschalten'])
add('Grammatik & Verbindungswörter', ['einschließlich'])
add('Kommunikation & Post', ['das Einschreiben'])
add('Handlungen: Alltagsverben', ['einsetzen','einstellen','eintragen'])
add('Unterwegs & Verkehr', ['einsteigen'])
add('Schule & Bildung', ['eintreten','der Eintritt'])
add('Grammatik & Verbindungswörter', ['einverstanden'])
add('Stadt, Ämter & Recht', ['der Einwohner / die Einwohnerin'])
add('Menge, Maß & Eigenschaften', ['einzeln','Einzel-','die Einzelheit','einzig-'])
add('Familie & Beziehungen', ['einziehen'])
add('Essen, Kochen & Restaurant', ['das Eis','das Eis'])
add('Unterwegs & Verkehr', ['die Eisenbahn'])
add('Kleidung & Aussehen', ['elegant'])
add('Freizeit, Medien & Technik', ['elektrisch','Elektro-','elektronisch'])
add('Familie & Beziehungen', ['die Eltern'])
add('Kommunikation & Post', ['empfangen','der Empfang','der Empfänger','empfehlen',
    'die Empfehlung'])
add('Zeit & Kalender', ['enden','das Ende','endgültig','endlich'])
add('Natur, Wetter & Umwelt', ['die Energie'])
add('Menge, Maß & Eigenschaften', ['eng'])
add('Familie & Beziehungen', ['der Enkel / die Enkelin'])
add('Denken, Wissen & Meinen', ['entdecken'])
add('Handlungen: Alltagsverben', ['entfernen'])
add('Menge, Maß & Eigenschaften', ['die Entfernung'])
add('Grammatik & Verbindungswörter', ['entgegenkommen','entlang'])
add('Menge, Maß & Eigenschaften', ['enthalten'])
add('Arbeit & Beruf', ['entlassen','die Entlassung'])
add('Denken, Wissen & Meinen', ['entscheiden','die Entscheidung','unentschieden',
    'sich entschließen','entschlossen'])
add('Kommunikation & Post', ['entschuldigen','die Entschuldigung'])
add('Natur, Wetter & Umwelt', ['entsorgen'])
add('Gefühle & Charakter', ['entspannend','enttäuschen','die Enttäuschung'])
add('Grammatik & Verbindungswörter', ['entstehen','entweder ... oder'])
add('Schule & Bildung', ['entwickeln','die Entwicklung'])
add('Natur, Wetter & Umwelt', ['die Erde','der Erdapfel','das Erdgeschoss/ Ergeschoß'])
add('Zeit & Kalender', ['das Ereignis','sich ereignen'])
add('Reisen & Urlaub', ['erfahren','die Erfahrung'])
add('Denken, Wissen & Meinen', ['erfinden','die Erfindung'])
add('Arbeit & Beruf', ['der Erfolg','erfolgreich'])
add('Menge, Maß & Eigenschaften', ['erforderlich','erfordern'])
add('Grammatik & Verbindungswörter', ['erfüllen','ergänzen'])
add('Schule & Bildung', ['das Ergebnis'])
add('Einkaufen & Geld', ['erhalten','erhöhen','die Erhöhung'])
add('Körper & Gesundheit', ['sich erholen','die Erholung','sich erkälten','erkältet',
    'die Erkältung'])
add('Denken, Wissen & Meinen', ['erinnern','die Erinnerung','erkennen'])
add('Schule & Bildung', ['erklären','die Erklärung'])
add('Kommunikation & Post', ['sich erkundigen','erlauben','die Erlaubnis'])
add('Zeit & Kalender', ['erleben','das Erlebnis'])
add('Arbeit & Beruf', ['erledigen'])
add('Gefühle & Charakter', ['erleichtern'])
add('Einkaufen & Geld', ['die Ermäßigung'])
add('Essen, Kochen & Restaurant', ['ernähren','die Ernährung','die Ernte'])
add('Gefühle & Charakter', ['ernst','ernsthaft'])
add('Einkaufen & Geld', ['eröffnen','die Eröffnung'])
add('Reisen & Urlaub', ['erreichen'])
add('Körper & Gesundheit', ['erschöpft','erschrecken'])
add('Handlungen: Alltagsverben', ['ersetzen','der Ersatz'])
add('Zeit & Kalender', ['erst','erst-'])
add('Schule & Bildung', ['erstellen'])
add('Familie & Beziehungen', ['erwachsen','der Erwachsene'])
add('Denken, Wissen & Meinen', ['erwarten'])
add('Kommunikation & Post', ['erzählen','die Erzählung'])
add('Familie & Beziehungen', ['erziehen','die Erziehung'])
add('Grammatik & Verbindungswörter', ['es'])
add('Essen, Kochen & Restaurant', ['essen','das Essen','der Essig'])
add('In der Wohnung & Zuhause', ['die Etage'])
add('Grammatik & Verbindungswörter', ['etwa','etwas','eventuell'])
add('Zeit & Kalender', ['ewig'])
add('Arbeit & Beruf', ['der Experte','der Export'])
add('Grammatik & Verbindungswörter', ['extra','extrem'])
add('Arbeit & Beruf', ['die Fabrik','das Fach','der Fachmann / die Fachfrau','die Fachleute'])
add('Menge, Maß & Eigenschaften', ['die Fähigkeit','fair'])
add('Unterwegs & Verkehr', ['fahren','die Fähre','die Fahrbahn','der Fahrer','die Fahrkarte',
    'der Fahrplan','das Fahrrad','das Fahrzeug'])
add('Denken, Wissen & Meinen', ['der Faktor'])
add('Grammatik & Verbindungswörter', ['der Fall','fallen','fällig','falls','falsch'])
add('Familie & Beziehungen', ['die Familie','der Familienstand'])
add('Handlungen: Alltagsverben', ['fangen'])
add('Freizeit, Medien & Technik', ['die Fantasie/Phantasie','fantastisch'])
add('Kleidung & Aussehen', ['die Farbe','farbig'])
add('Essen, Kochen & Restaurant', ['das Faschierte','der Fasching','die Fasnacht'])
add('Denken, Wissen & Meinen', ['fassen'])
add('Grammatik & Verbindungswörter', ['fast'])
add('Gefühle & Charakter', ['faul','faulenzen'])
add('Reisen & Urlaub', [])
add('Arbeit & Beruf', ['fehlen','der Fehler'])
add('Freizeit, Medien & Technik', ['feiern','die Feier','der Feiertag'])
add('Arbeit & Beruf', ['der Feierabend'])
add('Natur, Wetter & Umwelt', ['das Feld'])
add('In der Wohnung & Zuhause', ['das Fenster'])
add('Reisen & Urlaub', ['die Ferien','Ferien-'])
add('Freizeit, Medien & Technik', ['die Fernbedienung','fernsehen','das Fernsehen','der Fernseher',
    'die Festplatte'])
add('Grammatik & Verbindungswörter', ['fertig','fest'])
add('Freizeit, Medien & Technik', ['das Fest'])
add('Denken, Wissen & Meinen', ['festhalten','festlegen','feststehen','feststellen'])
add('Stadt, Ämter & Recht', ['festnehmen','festsetzen'])
add('Essen, Kochen & Restaurant', ['fett','das Fett'])
add('Natur, Wetter & Umwelt', ['feucht','das Feuer','das Feuerzeug','die Feuerwehr'])
add('Körper & Gesundheit', ['das Fieber'])
add('Freizeit, Medien & Technik', ['die Figur','der Film'])
add('Einkaufen & Geld', ['finanzieren','finanziell'])
add('Denken, Wissen & Meinen', ['finden'])
add('Körper & Gesundheit', ['der Finger'])
add('Arbeit & Beruf', ['die Firma'])
add('Natur, Wetter & Umwelt', ['flach','die Fläche'])
add('In der Wohnung & Zuhause', ['die Flasche'])
add('Kleidung & Aussehen', ['der Fleck'])
add('Essen, Kochen & Restaurant', ['das Fleisch','der Fleischhauer / die Fleischhauerin',
    'das Hackfleisch'])
add('Arbeit & Beruf', ['fleißig'])
add('Menge, Maß & Eigenschaften', ['flexibel'])
add('Unterwegs & Verkehr', ['fliegen','der Flug','der Flughafen','das Flugzeug'])
add('Gefühle & Charakter', ['fliehen','die Flucht'])
add('Natur, Wetter & Umwelt', ['fließen','fließend','der Fluss','die Flüssigkeit'])
add('Einkaufen & Geld', ['der Flohmarkt'])
add('Freizeit, Medien & Technik', ['die Flöte'])
add('In der Wohnung & Zuhause', ['der Flur'])
add('Denken, Wissen & Meinen', ['folgen','die Folge','folgend'])
add('Arbeit & Beruf', ['fordern','die Forderung','fördern','die Förderung'])
add('Grammatik & Verbindungswörter', ['die Form'])
add('Stadt, Ämter & Recht', ['das Formular'])
add('Schule & Bildung', ['die Forschung','die Fortbildung','der Fortschritt','fortsetzen',
    'die Fortsetzung','das Forum'])
add('Freizeit, Medien & Technik', ['fotografieren','das Foto','der Fotoapparat','der Fotograf',
    'die Fotografie'])
add('Familie & Beziehungen', ['die Frau','der Freund','die Freundschaft','freundlich'])
add('Gefühle & Charakter', ['frech','froh','fröhlich','frieren','sich freuen','die Freude',
    'der Friede'])
add('Kommunikation & Post', ['fragen','die Frage'])
add('Grammatik & Verbindungswörter', ['frei','im Freien','freiwillig','fremd'])
add('Gesellschaft, Politik & Wirtschaft', ['die Freiheit'])
add('Freizeit, Medien & Technik', ['die Freizeit'])
add('Tiere', ['fressen'])
add('Kleidung & Aussehen', ['frisch','der Friseur / die Friseurin','die Frisur'])
add('Zeit & Kalender', ['die Frist','früh','früher/früher-','frühstücken','das Frühstück'])
add('Natur, Wetter & Umwelt', ['die Frucht','Früchte'])
add('Gefühle & Charakter', ['fühlen'])
add('Denken, Wissen & Meinen', ['führen'])
add('Unterwegs & Verkehr', ['der Führerausweis','der Führerschein'])
add('Arbeit & Beruf', ['die Führung'])
add('Stadt, Ämter & Recht', ['das Fundbüro'])
add('Freizeit, Medien & Technik', ['funktionieren'])

# =====================================================================
# GAP FILL 1: idx 42-1017 (from coverage-audit missing list)
# =====================================================================
add('Grammatik & Verbindungswörter', ['allerdings','auch','außer','außerdem','bei','beid-',
    'beinahe','bereits','da','dabei','dafür','dagegen','daher','dahin','damit','daneben',
    'direkt','eben','ebenfalls','ebenso','für','gar','ganz','gegen','gegenüber','genau',
    'genauso','gerade','gern/gerne','gesamt-/Gesamt-'])
add('Denken, Wissen & Meinen', ['akzeptieren','auflösen','beachten','beschäftigen',
    'die Beschäftigung','die Art','gelten','genehmigen'])
add('Kommunikation & Post', ['auffordern','die Aufforderung','begegnen','der Artikel',
    'bedeuten','die Bedeutung','begrüßen','behaupten',])
add('Schule & Bildung', ['die Aufgabe','aufgeben','das Beispiel','der Bereich','beginnen',
    'der Beginn','der Bleistift','das Gedicht','die Geduld'])
add('Handlungen: Alltagsverben', ['bedienen','die Bedienungsanleitung','die Bedingung','bieten',
    'bitten','die Bitte','bleiben','brauchen','geben','gebrauchen',
    'die Gebrauchsanweisung','gelingen'])
add('Gefühle & Charakter', ['aufregen','befreit','befriedigend','begrenzt','beißen','bereit',
    'berühmt','gefallen','sich etwas gefallen lassen','geehrt','gespannt','gemütlich'])
add('Körper & Gesundheit', ['das Auge','der Fuß','beißen','das Bein','die Gefahr','gefährlich',
    'gesund','die Gesundheit','das Gesicht'])
add('Unterwegs & Verkehr', ['der Ausgang','die Ausfahrt','ausfallen','das Auto','die Autobahn',
    'die Bahn','S-Bahn','die Straßenbahn','die U-Bahn','der Bahnhof','der Bahnsteig',
    'der Anschluss','anschnallen','der Fußgänger / die Fußgängerin',
    'die Fußgängerzone','der Gang','die Geschwindigkeit','die Geschwindigkeitsbeschränkung'])
add('Natur, Wetter & Umwelt', ['die Aussicht','der Berg',
    'das Gewitter',])
add('Einkaufen & Geld', ['die Anlage','die Bank','die Bank',
    'der Bancomat/Bankomat','die Bankleitzahl','die Bankomat-Karte','die Gebühr','das Geld',
    'der Geldautomat','die Geldbörse',])
add('Freizeit, Medien & Technik', ['der Ball',
    'der Basketball','basteln','die Batterie','die Galerie','die Gitarre','genießen'])
add('In der Wohnung & Zuhause', ['baden','das Bad','die Badewanne','der Balkon','die Bar',
    'der Garten','das Geschirr'])
add('Essen, Kochen & Restaurant', ['backen','die Bäckerei','die Banane','das Bier','das Dessert',
    'das Gasthaus','die Gaststätte','der Gast','das Gebäck','das Gemüse','das Gericht',
    'der Geschmack','das Getränk','das Gewürz','gießen',])
add('Arbeit & Beruf', ['arbeiten','die Arbeit','der Arbeiter / die Arbeiterin',
    'die Arbeitserlaubnis','arbeitslos','die Arbeitslosigkeit','der Arbeitsplatz',
    'die Arbeitsstelle','beenden','sich beteiligen','das Büro','der Direktor / die Direktorin',
    'die Gewerkschaft'])
add('Familie & Beziehungen', ['der Bekannte / die Bekannte','geboren werden','die Geburt',
    'der Geburtstag','das Geschenk','die Geschwister',])
add('Stadt, Ämter & Recht', ['die Burg',
    'der Doktor / die Doktorin','behindern',
    'bekannt geben','berichten','der Bericht','das Gebäude','das Gebiet','die Gemeinschaft',
    'das Gesetz','die Gesellschaft'])
add('Zeit & Kalender', [
    'gestern'])
add('Reisen & Urlaub', [])
add('Menge, Maß & Eigenschaften', ['das Ding',
    'gering',])
add('Denken, Wissen & Meinen', [])
TOPICS['Grammatik & Verbindungswörter'] += []
add('Grammatik & Verbindungswörter', ['geradeaus'])
add('Denken, Wissen & Meinen', ['bewegen',
    'das Gewissen'])
add('Menge, Maß & Eigenschaften', ['gerecht','gewohnt',
    'gewöhnlich','gewöhnen','die Gewohnheit'])
add('Kommunikation & Post', [])
add('Arbeit & Beruf', ['die Generation'])
add('In der Wohnung & Zuhause', ['besetzen'])
add('Freizeit, Medien & Technik', ['das Gerät'])
add('Einkaufen & Geld', ['der Gewinn','gewinnen'])
add('Gesellschaft, Politik & Wirtschaft', ['die Geschichte'])
add('Denken, Wissen & Meinen', ['geschehen'])
add('Familie & Beziehungen', ['geschieden'])
add('Freizeit, Medien & Technik', ['die/das Glace/Glacé',])
add('Körper & Gesundheit', ['giftig','das Gift'])
add('Einkaufen & Geld', ['das Geschäft'])
add('Grammatik & Verbindungswörter', ['das Geschlecht'])
add('Zeit & Kalender', [])
add('Kommunikation & Post', ['das Gespräch'])
add('Menge, Maß & Eigenschaften', ['genug','genügen'])

# =====================================================================
# GAP FILL 2: idx 42-1224
# =====================================================================
add('Kommunikation & Post', ['aktuell','der Ausdruck','sich bedanken','die Grafik',
    'gratulieren','die Gratulation','der Glückwunsch','grüßen','der Gruß',
    'hinweisen','der Hinweise',
    'hallo','der Humor',])
add('Grammatik & Verbindungswörter', ['auseinander','begleiten','das Detail','gleich',
    'gleichfalls','gleichzeitig','her/her-','heraus-','herein-',
    'herunter-','hier/hier-','hierher','hinten','hinter/hinter-','in','indem','innen','inner-',
    'innerhalb','inzwischen','irgendirgendein','irgendwann','ja','je','je … desto …',
    'jeder','jederzeit','jedes Mal','jedoch','jemals','jemand'])
add('Zeit & Kalender', [
    'heute','heutig-','hinterher','immer',])
add('In der Wohnung & Zuhause', ['das Dach','der Eingang',
    'die Garage','der Herd','das Haus','der Haushalt','der Hausmeister / die Hausmeisterin',
    'das Heim','die Heizung','heizen'])
add('Unterwegs & Verkehr', ['die Brücke','der Gehsteig','das Gleis',
    'die Haltestelle','hupen'])
add('Kleidung & Aussehen', [
    'hässlich','das Hemd','die Hose','der Hut'])
add('In der Wohnung & Zuhause', ['die Büchse','die Dose','die Garderobe','das Glas','der Hammer',
    'das Heft'])
add('Menge, Maß & Eigenschaften', ['furchtbar','gleichberechtigt','groß','Groß-','die Größe',
    'gültig','gut','hart','häufig','haltbar','hoch','die Höhe','höchstens','hübsch',
    'ideal','individuell','insgesamt','intelligent','die Intelligenz','intensiv'])
add('Gefühle & Charakter', ['(sich) fürchten','glücklich','das Glück','hassen',
    'herzlich','höflich','hoffen','hoffentlich','die Hoffnung',
    'interessieren','interessant','das Interesse','interessiert'])
add('Freizeit, Medien & Technik', ['der Fußball','Golf',
    'das Hobby','hochladen','das Interview','installieren',
    'das Instrument','historisch'])
add('Körper & Gesundheit', ['das Gefühl',
    'die Grippe','das Haar','der Hals','die Hand','die Haut','husten','der Husten','hungrig',
    'der Hunger','die Infektion','das Herz'])
add('Stadt, Ämter & Recht', ['das Gefängnis','der Gegner','die Grenze',
    'illegal',])
add('Natur, Wetter & Umwelt', ['die Gegend',
    'das Gras',
    'hageln',
    'der Himmel','die Hitze','der Hügel','die Insel'])
add('Grammatik & Verbindungswörter', ['das Gegenteil'])
add('Arbeit & Beruf', ['das Gehalt','die Gelegenheit',
    'gründen','der Grund','der Handel','handeln',
    'der Händler / die Händlerin','der Hersteller','herstellen','der Ingenieur',
    'die Industrie','der Import'])
add('Denken, Wissen & Meinen', ['das Geheimnis','geheim',
    'glauben','gründlich',
    'der Inhalt'])
add('Handlungen: Alltagsverben', ['gehen','gehören','greifen','halten','der Halt','heben',
    'holen','hängen','heißen','integrieren','die Integration'])
add('Reisen & Urlaub', ['das Gepäck','die Halbpension','das Hallenbad','das Hotel',
    'inklusive'])
add('Essen, Kochen & Restaurant', ['die Gabel','gemeinsam',
    'grillen','grillieren','der Grill','das Hähnchen/Hühnchen',
    'das Hendl','der Honig',
    'der Imbiss','die Jause'])
add('Einkaufen & Geld', ['günstig',
    'das Gold',])
add('Freizeit, Medien & Technik', ['die Gymnastik'])
add('Familie & Beziehungen', [
    'die Hausfrau / der Hausmann','heiraten',
    'die Heimat','die Hochzeit','der Held / die Heldin'])
add('Stadt, Ämter & Recht', ['das Gebirge','die Hauptstadt','der Hauptbahnhof','der Herr',
    'installieren'])
add('Gesellschaft, Politik & Wirtschaft', ['der Gott',])
add('Denken, Wissen & Meinen', [])
add('Menge, Maß & Eigenschaften', ['das Gewicht'])
add('Handlungen: Alltagsverben', ['helfen','die Hilfe'])
add('Natur, Wetter & Umwelt', [])
add('Gesellschaft, Politik & Wirtschaft', ['die Gewalt'])
add('In der Wohnung & Zuhause', ['der Fauteuil'])
add('Schule & Bildung', ['die Hausaufgabe','das Institut','der Intensivkurs',
    'interkulturell','international'])
add('Kommunikation & Post', [
    'der Hörer / die Hörerin / der Zuhörer','hören','das Inserat'])
add('Kleidung & Aussehen', ['die Jacke','die Jeans','hell'])
add('Natur, Wetter & Umwelt', ['heiß'])
add('Zeit & Kalender', ['halb','halbtags','die Hälfte'])
add('Familie & Beziehungen', ['heimlich','das Heimweh'])

# =====================================================================
# GAP FILL 3: idx 273-1450
# =====================================================================
add('Kommunikation & Post', ['sich beeilen','die Idee','informieren','die Information',
    'der Journalist / die Journalistin','klingeln','die Klingel','klingen','klopfen',
    'die Kommunikation','der Kontakt','sich konzentrieren'])
add('Grammatik & Verbindungswörter', ['sich befinden','gucken','haben','halt','jetzt','jeweils',
    'kaum','kein-','klar','klappen','klären','komisch','kommen','komplett','kompliziert',
    'können','korrekt','kurz','kürzlich','lang','die Länge','lange','langsam','längst',
    'lassen'])
add('Freizeit, Medien & Technik', ['Bio-','bio','das Handy','das Kabel','die Kamera',
    'die Kassette','klicken','der Klick','das Klavier','das Kino',
    
    'das Konzert','kopieren','die Kopie','der Kopierer','der Krimi','die Kultur','kulturell',
    'der Künstler / die Künstlerin','künstlich','das Laufwerk','der Lautsprecher'])
add('Natur, Wetter & Umwelt', ['brennen','das Gas','der Hafen','glatt','das Grundstück',
    'der Kanal','das Land','die Landschaft','die Landwirtschaft',
    'kalt','die Kälte'])
add('Tiere', ['füttern','der Bauernhof'])
add('Einkaufen & Geld', ['garantieren','die Garantie','gratis','die Karte','die Chipkarte',
    'die Fahrkarte','die Kasse','der Katalog','kaufen','der Kauf','der Käufer / die Käuferin',
    'kostenlos','der Kredit','die Kreditkarte','das Konto','das Girokonto','kontrollieren',
    'die Kontrolle','die Kosten','kosten','kosten',
    'der Konsum','konsumieren'])
add('Menge, Maß & Eigenschaften', ['der Gegensatz','der Gegenstand','die Gruppe','knapp',
    'klein','klug','kräftig',])
add('In der Wohnung & Zuhause', ['die Halle','das Holz','die Hütte','das Kissen','die Kerze',
    'der Keller','der Kühlschrank','die Lampe',
    'das Lager','legen'])
add('Arbeit & Beruf', ['der Handwerker / die Handwerkerin','die Herausforderung','die Karriere',
    'der Kollege / die Kollegin','kündigen','die Kündigung','der Kunde / die Kundin',
    'der Kandidat'])
add('Zeit & Kalender', ['der Kalender',])
add('Unterwegs & Verkehr', ['fahren','runterwerfen',
    'der Laster',
    'landen','laufen'])
add('Denken, Wissen & Meinen', ['die Herkunft',
    'kennen','kennenlernen','die Kenntnisse'])
add('Familie & Beziehungen', ['der Hof','die Jugend','der Jugendliche / die Jugendliche',
    'jung','der Junge','das Kind','die Kindheit','der Kindergarten','die Jugendherberge'])
add('Essen, Kochen & Restaurant', ['der Kaffee','das Kaffeehaus','der Kakao','die Kantine',
    'die Karotte','die Kartoffel','der Käse','der Kloß',
    'die Konfitüre','kochen',
    'der Koch / die Köchin','der Knödel','der Kuchen',
    'lecker','die Lebensmittel',])
add('Reisen & Urlaub', ['die Kabine','der Kiosk','der Koffer','die Küste'])
add('Handlungen: Alltagsverben', ['kaputtgehen','kaputtmachen','kaputt','kämpfen','der Kampf',
    'kriegen','sich kümmern','lächeln','lachen','leben'])
add('Stadt, Ämter & Recht', ['das Kennzeichen','die Kirche',
    'der Krieg','die Krise','das Konsulat','der König',
    'die Katastrophe','Kriminal- / die Kriminalpolizei','das Kreuz'])
add('Kleidung & Aussehen', ['die Kette','das Kleid','die Kleidung','das Kostüm','die Kiste',
    'kleben',])
add('Schule & Bildung', ['die Klasse','die Klassenarbeit','der Kurs','der Kursleiter / die Kursleiter',
    'die Lehre','die Lehrstelle','der Lehrer / die Lehrerin','der Lehrling',
    'der Lebenslauf','das Kapitel'])
add('Körper & Gesundheit', ['der Kopf','der Körper','körperlich','krank','der Kranke / die Kranke',
    'das Krankenhaus','die Krankenkasse','der Krankenpfleger','die Krankenschwester',
    'der Krankenwagen','die Krankheit','das Knie','der Knochen',
    'leiden'])
add('Gefühle & Charakter', ['klasse','kreativ','kritisieren','die Kritik','kritisch',
    'die Laune','ledig','leicht','leider'])
add('Denken, Wissen & Meinen', ['der Kompromiss','die Konferenz','die Konkurrenz'])
add('Grammatik & Verbindungswörter', ['der Kreis'])
add('Unterwegs & Verkehr', ['die Kreuzung','die Kurve'])
add('In der Wohnung & Zuhause', ['der Kugelschreiber','der Kuli'])
add('Kommunikation & Post', ['das Kuvert',])
add('Freizeit, Medien & Technik', ['das Klima','die Klimaanlage',])
add('In der Wohnung & Zuhause', ['der Korridor'])
add('Menge, Maß & Eigenschaften', ['korrigieren',])
add('Arbeit & Beruf', ['das Kraftfahrzeug','das Kraftwerk'])
add('Menge, Maß & Eigenschaften', [])
add('Kleidung & Aussehen', ['der Knopf'])
add('Zeit & Kalender', ['langweilig','sich langweilen','die Langeweile',])
add('Natur, Wetter & Umwelt', ['der Lärm','der Kunststoff','das Leder'])
add('Familie & Beziehungen', ['küssen','der Kuss'])
add('Grammatik & Verbindungswörter', ['leid tun'])

# =====================================================================
# GAP FILL 4: idx 1099-1691
# =====================================================================
add('Grammatik & Verbindungswörter', ['heim','hinterlassen','laut','letzt-','man','manch-',
    'manchmal','meinetwegen','meist-','meist','mit','miteinander','mitten','mittler-',
    'mittlerweile','mögen','möglich','die Möglichkeit','möglichst','nach','nachdem','nachher',
    'nächst-','nah','nämlich','national/national-','natürlich','neben','nebenan','nebenbei',
    'nehmen','nein','nennen','nett','neu','nicht','nichts','nie','niedrig','niemand',
    'nirgends','nirgendwo','noch','noch mal','nochmals','normal','normalerweise','mehr',
    'mehrere','mindestens','miss-','mobil/mobil-','möchten','müssen','negativ'])
add('Einkaufen & Geld', ['der Kasten','der Kasten',
    'der Laden','die Marke','markieren','der Markt',
    'maximal','die Mehrwertsteuer','der Mieter / die Mieterin','mieten','die Miete',
    ])
add('In der Wohnung & Zuhause', ['die Küche',
    'das Licht','das Möbel','möbliert','der Müll','die Müllabfuhr','die Mülltonne',
    'die Nadel','der Nagel','locker','das Loch','der Löffel','das Messer'])
add('Freizeit, Medien & Technik', ['die Kunst',
    'das Lexikon','das Lied','die Literatur',
    'das Magazin','malen','der Maler / die Malerin','das Märchen','die Medien',
    'das Museum','die Musik','musikalisch','der Musiker / die Musikerin','der Monitor',
    'die Mobilbox','das Mobiltelefon',])
add('Körper & Gesundheit', ['die Kraft',
    'die Lippe','der Magen','mager',
    'die Medizin','das Medikament','müde','die Mühe','der Mund',
    'der Muskel','der Mut','mutig','die Nase','der Nerv','nervös'])
add('Denken, Wissen & Meinen', ['die Lage','die Liste','die Lösung','lösen','die Lüge','lügen',
    'meinen','die Meinung','merken','merkwürdig','die Methode','mischen','die Nachfrage',
    'nachdenken','die Nachricht','nachschlagen',])
add('Kommunikation & Post', ['melden','die Meldung',
    'mitteilen',])
add('Gefühle & Charakter', ['der Kellner / die Kellnerin'.replace(" der Kellner / die Kellnerin",''),
    'die Lust','lustig','lieben','lieb','die Liebe','sich lohnen','neugierig',])
add('Essen, Kochen & Restaurant', ['die Kneipe',
    'kühl','das Lokal','die Limonade','die Mahlzeit',
    'die Margarine','die Marille','die Marmelade','das Mehl','das Menü','die Mensa',
    'das Mineralwasser','die Möhre','das Müesli/Müsli','die Milch','der Metzger',
    'die Nachspeise'])
add('Arbeit & Beruf', ['der Kellner / die Kellnerin','leisten','die Leistung','leiten',
    'der Leiter / die Leiterin','die Leitung','der Lohn','der Mangel','der Mechaniker / die Mechanikerin',
    'der Meister','der Mitarbeiter / die Mitarbeiterin','der Migrant / die Migrantin',
    'die Migration'])
add('Stadt, Ämter & Recht', ['der Konflikt','die Mauer','die Mehrheit','die Minderheit',
    'das Mitglied','der Nachbar / die Nachbarin'])
add('Schule & Bildung', ['lernen','der Lerner / die Lernerin','lesen','der Leser / die Leserin',
    'die Nachhilfe'])
add('Familie & Beziehungen', ['die Leute','das Mädchen',
    'der Mann','männlich','die Mutter','der Name','der Familienname','der Vorname',
    'der Neffe','die Nichte'])
add('Menge, Maß & Eigenschaften', ['die Leiter','das Mal','mal','die Menge','messen','das Mittel',
    'minimal',])
add('Unterwegs & Verkehr', ['die Landung','der Lift',
    'die Linie','links','link-','los/los-','losfahren','die Maschine',
    'das Motorrad','der Motor',])
add('Natur, Wetter & Umwelt', ['leer','die Luft','das Meer',
    'der Mond','die Natur','der Nebel','neblig','nass'])
add('Gesellschaft, Politik & Wirtschaft', ['der Mensch','menschlich',
    'der Nachteil'])
add('Kleidung & Aussehen', ['der Mantel','die Mode',
    'modern','das Modell'])
add('Handlungen: Alltagsverben', ['liefern','die Lieferung','liegen','löschen','machen',
    ])
add('Zeit & Kalender', ['der Moment','neulich'])
add('Grammatik & Verbindungswörter', ['Lieblings-',])
add('Freizeit, Medien & Technik', ['die Mappe'])
add('In der Wohnung & Zuhause', ['die Mitte',])
add('Einkaufen & Geld', ['die Münze'])
add('Menge, Maß & Eigenschaften', ['mündlich'])
add('Denken, Wissen & Meinen', ['sich nähern','die Nähe',])
add('Essen, Kochen & Restaurant', ['das Nahrungsmittel'])

# =====================================================================
# GAP FILL 5: idx 1246-1925
# =====================================================================
add('Grammatik & Verbindungswörter', ['nun','nur','ob','oben','ober-','obwohl','oder','offen',
    'offenbar','ohne','oft/öfter','paar','per','pro','quer','rauf/rauf-','raus/raus-',
    'recht','recht-','rechts','regelmäßig','rein'])
add('Essen, Kochen & Restaurant', ['die Kanne',
    'die Nudel','das Obst','das/derObers','der Ober',
    'die Orange','die Pfanne','der Pfeffer','die Pflaume','das Picknick','der Pilz',
    'die Pizza','die Pommes frites','die Portion','probieren','probieren',
    'der Paradeiser','das Poulet',
    'derRahm','der Reis'])
add('Körper & Gesundheit', [
    'die Klinik','mild','das Ohr','operieren','die Operation','das Pflaster',
    'pflegen','der Pfleger / die Pflegerin','der Patient / die Patientin','die Notaufnahme',
    'der Notfall','der Notruf','(sich) rasieren',
    ])
add('Zeit & Kalender', ['das Leben','notieren','die Notiz',
    'rechtzeitig',])
add('Menge, Maß & Eigenschaften', ['leise','nötig','notwendig','nützlich','optimistisch',
    'original','das Original','pauschal','perfekt',
    'positiv','praktisch','preiswert','prima','realistisch',
    'reich','reif','regional'])
add('Gefühle & Charakter', ['loben','peinlich','das Pech',
    ])
add('Kommunikation & Post', ['die Mahnung','das Netz','das Netzwerk','die Neuigkeit',
    'die Nummer','die Presse','die Recherche','reden','die Rede',
    'die Reklame'])
add('Zeit & Kalender', [])
add('Familie & Beziehungen', ['der Nachwuchs','die Oma','der Onkel',
    'der Opa','der Partner / die Partnerin','das Paar','der Nichtraucher / die Nichtraucherin'])
add('In der Wohnung & Zuhause', ['nähen','derOfen',
    'öffnen','der Ordner','ordnen','die Ordnung','packen','das Papier',
    'putzen',
    'die Puppe'])
add('Arbeit & Beruf', ['das Material','nützen','das Personal',
    'der Praktikant / die Praktikantin','das Praktikum','der Professor / die Professorin',
    'der Profi','der Profisportler / die Profisportlerin','das Projekt',
    ])
add('Schule & Bildung', ['die Matura','die Note',
    'präsentieren','die Präsentation','die Prüfung',
    'prüfen','das Referat',])
add('Arbeit & Beruf', ['die Qualifikation'])
add('Menge, Maß & Eigenschaften', [])
add('Freizeit, Medien & Technik', ['das Metall',
    'die Mobilität','die Oper','das Orchester',
    'die Party','organisieren','das Programm','der Prospekt','das Publikum','das Quiz',
    'das Radio','der Rekord','das Rätsel'])
add('Stadt, Ämter & Recht', ['die Messe','der Notausgang','die Öffentlichkeit','öffentlich',
    'veröffentlichen','offiziell','das Opfer','die Ordination','die Ordination',
    'die Organisation','der Ort','der Vorort','der Wohnort',
    'passieren','der Pass','der Personenstand','die Personalien','die Politik',
    'der Politiker / die Politikerin','politisch','die Polizei','der Polizist / die Polizistin',
    'der Prozess','das Recht','rechtlich',
    'die Reform','die Regel','regeln','das Rathaus'])
add('Kommunikation & Post', ['die Post','die Postleitzahl','der Pöstler / die Pöstlerin',
    ])
add('Natur, Wetter & Umwelt', ['der Ozean','der Rasen','regnen','der Regen','die Region',
    'das Öl','Öko-',])
add('Denken, Wissen & Meinen', ['ordentlich','das Problem','die Realität','realisieren',
    'die Reaktion','reagieren','die Reihenfolge','die Reihe','reichen'])
add('Unterwegs & Verkehr', ['der Park','parken','parkieren','der Perron','die Panne',
    'der Passagier / die Passagierin','das Rad','das Rad',
    'der Reifen',])
add('Einkaufen & Geld', ['das Paket','der Preis',
    'produzieren','das Produkt','die Produktion','der Rabatt','rechnen','der Rechner',
    'die Rechnung','die Quittung','das Portemonnaie/Portmonee',])
add('Reisen & Urlaub', ['die Pension','die Pension',
    'in Pension gehen/sein','pensioniert werden/sein','der Pensionist / die Pensionistin',
    'das Quartier','die Reise','reisen','das Reisebüro'])
add('Freizeit, Medien & Technik', ['die Phantasie/Fantasie','planen','der Plan','die Planung',
    'reiten'])
add('In der Wohnung & Zuhause', ['das Plastik','das Regal'])
add('Grammatik & Verbindungswörter', ['plötzlich','parallel','privat'])
add('Handlungen: Alltagsverben', ['pflanzen','die Pflanze','protestieren','der Protest',
    'reduzieren'])
add('Gesellschaft, Politik & Wirtschaft', ['die Pflicht','populär',
    ])
add('Freizeit, Medien & Technik', [])
add('Kleidung & Aussehen', ['das Parfüm','der Pullover'])
add('Zeit & Kalender', ['pünktlich'])
add('In der Wohnung & Zuhause', ['reinigen','die Reinigung'])

# =====================================================================
# GAP FILL 6: idx 1252-2160
# =====================================================================
add('Grammatik & Verbindungswörter', ['nutzen','passen','relativ','richtig','so','sobald',
    'sodass','sofort','sogenannt-','sogar','solange','solch-','sollen','sondern','sonst',
    'schon','sehr','seit','seitdem','selb-','selbst','selber','sicher',])
add('Essen, Kochen & Restaurant', ['das Rezept',
    'roh','dasRohr','das Restaurant',
    'der Saft','dieSahne','der Salat','das Salz','salzig',
    'schmecken','das Schnitzel','die Schokolade',
    'der Schinken','das Schwammerl','sauer','satt','die Soße/Sauce'])
add('Zeit & Kalender', ['die Pause',
    'das Semester','selten',])
add('Menge, Maß & Eigenschaften', ['die Qualität','riesig','rund','sämtliche',
    'schlank','schmal','schwach','schwer','die Schwierigkeit','schwierig','senkrecht',
    ])
add('Kommunikation & Post', ['das Plakat','der Punkt',
    'raten','der Rat','Ratschlag',
    
    'sagen','schicken','die Schrift','schriftlich','der Schriftsteller / die Schriftstellerin',
    'senden','der Sender','die Sendung',])
add('In der Wohnung & Zuhause', ['der Platz','der Rand','der Raum',
    'der Sack','sauber',
    'die Schere','die Scheibe','der Schirm','der Schlaf',
    'schlafen','der Schlüssel','schmutzig','der Schmutz',
    'der Schrank','die Schüssel','das Sofa','die Socke'])
add('Familie & Beziehungen', ['die Person',
    'persönlich','die Rente','in Rente gehen/sein','der Rentner / die Rentnerin',
    'die Senioren','der Sohn','die Schwester','Schwieger-','die Schwangerschaft'])
add('Menge, Maß & Eigenschaften', [])
add('Unterwegs & Verkehr', ['der Radfahrer / die Radfahrerin','rückwärts','die Rückfahrt',
    'die Rückkehr','die Rundfahrt','der Rucksack','der Schalter',
    ])
add('Gefühle & Charakter', ['schade','schaden','der Schaden','der Schreck','schrecklich',
    'die Ruhe','ruhig'])
add('Denken, Wissen & Meinen', ['der Respekt','das Risiko','sinnlos','sinnvoll','der Sinn',
    'schätzen','sichtbar',])
add('Zeit & Kalender', ['schließlich'])
add('Handlungen: Alltagsverben', ['schaffen','schalten','schauen','zuschauen','schließen',
    '(sich) schneiden','schneien',
    'schütteln','schützen','der Schutz','sammeln','(sich) setzen',
    'sinken'])
add('Arbeit & Beruf', ['die Mannschaft',
    'reparieren','die Reparatur','der Rest','der Sekretär / die Sekretärin',
    'selbstständig','der Schauspieler / die Schauspielerin','der Sänger / die Sängerin',
    'der Reporter / die Reporterin','die Reportage',])
add('Freizeit, Medien & Technik', [
    'der Saal','der Roman',
    'schwimmen','das Schwimmbad','singen','die Serie',
    'der Ski/Schi','der Sitz'])
add('Stadt, Ämter & Recht', ['der Richter / die Richterin',
    'die Sicherheit','sichern','rauchen',
    'der Raucher / die Raucherin',
    'schuldig','die Schuld','schuld','die Schulden'])
add('Reisen & Urlaub', ['reservieren','die Reservierung',
    'die Sehenswürdigkeit','das Schiff'])
add('Denken, Wissen & Meinen', ['die Rücksicht','die Situation',
    ])
add('Natur, Wetter & Umwelt', ['das Rind','der See',
    'die See','die Nord-/Ostsee',])
add('Tiere', [
    'die Schlange'])
add('Kleidung & Aussehen', ['der Ring','der Schmuck','schminken',
    'schön','der Schuh','der Rock'])
add('Denken, Wissen & Meinen', [])
add('Kommunikation & Post', ['rufen','die Rufnummer'])
add('Schule & Bildung', ['die Schule','die Schularbeit',
    'der Schüler / die Schülerin',
    ])
add('Grammatik & Verbindungswörter', ['die Sache'])
add('Körper & Gesundheit', ['der Rücken','der Schmerz','das Schmerzmittel','der Schnupfen',
    'die Schulter','schwitzen',
    'die Seife'])
add('Familie & Beziehungen', ['sich scheiden lassen','geschieden','die Scheidung'])
add('Grammatik & Verbindungswörter', [])
add('Denken, Wissen & Meinen', ['scheinen','der Schein'])
add('Familie & Beziehungen', ['schenken'])
add('Unterwegs & Verkehr', ['schieben','der Schritt'])
add('Kommunikation & Post', ['schimpfen'])
add('Zeit & Kalender', [])
add('Handlungen: Alltagsverben', ['schlagen',])
add('Natur, Wetter & Umwelt', ['der Schnee','schneien'])
add('Kommunikation & Post', ['schreiben','aufschreiben','das Schreiben','schreien'])
add('Menge, Maß & Eigenschaften', ['schief','schlecht','schlimm','schnell'])

# =====================================================================
# GAP FILL 7: idx 1252-2365
# =====================================================================
add('Essen, Kochen & Restaurant', [
    'die Speisekarte',
    'die Suppe','süß','die Tasse',
    'der Teller','der Tee','Tee ziehen lassen',
    ])
add('Freizeit, Medien & Technik', ['der Karneval','die Metropole','Prost',
    'siegen',
    'der Sieg','der Sieger / die Siegerin',
    'der Spaß','der Spiegel','das Spiel','spielen','der Spieler / die Spielerin',
    'der Spielplatz','das Spielzeug','der Sport','die Sportart','der Sportler / die Sportlerin',
    'sportlich','das Stadion','der Star',
    'das Studio','das Symbol','die Szene',
    'das Talent','tanzen','der Tanz','das Tennis',
    'das Theater','das Thema','die Theorie','das Ticket'])
add('Körper & Gesundheit', [
    'die Salbe',
    'die Sprechstunde','die Spritze','spüren','stechen','sterben',
    'die Sucht','süchtig','das Suchtmittel','taub',
    'die Tablette','die Therapie'])
add('Grammatik & Verbindungswörter', ['passiv','riechen','sehen','sein','die Seite',
    'selbstverständlich','sitzen','soviel','so viel/so viel wie','sowieso',
    'sowohl … als auch','statt','stattfinden','stammen','ständig','Speise-/-speise',
    'Spezial-','speziell','stumm'])
add('Zeit & Kalender', ['spät','spätestens',
    'der Tagesablauf','tatsächlich'])
add('Natur, Wetter & Umwelt', ['der Sand','der Schatten',
    'verschmutzen','die Sonne','sonnig',
    'der Stern','der Sturm','das Tal'])
add('Stadt, Ämter & Recht', ['die Religion','die Richtung','der Sozialarbeiter / die Sozialarbeiterin',
    'sozial','strafbar','die Strafe','der Strafzettel',
    ])
add('Handlungen: Alltagsverben', ['rennen','schießen',
    'sorgen','die Sorge','sparen','sparsam','spazieren gehen','der Spaziergang',
    'stecken','stehen','stehen bleiben','stellen','die Stelle','steigen','stoppen',
    'stören','springen','staubsaugen','spülen','stürzen','suchen','tauschen'])
add('Kommunikation & Post', ['schweigen',
    
    '(sich) siezen','sprechen','die Sprache','die Fremdsprache','die Muttersprache',
    'die Zweitsprache','stimmen','die Stimme','der Standpunkt','speichern','tippen',
    'die Tastatur','die Taste'])
add('Denken, Wissen & Meinen', ['der/dasObers','seltsam',
    'die Stimmung','die Tat','die Tatsache',])
add('Arbeit & Beruf', ['der Serviceangestellte / die Serviceangestellte','der Spezialist / die Spezialistin',
    'der Steward / die Stewardess','der Student / die Studentin','der Studierende / die Studierende',
    'die Tätigkeit','der Täter / die Täterin'.replace(" der Täter / die Täterin",''),
    'teilnehmen','die Teilnahme','der Teilnehmer / die Teilnehmerin','die Teilzeit',
    'telefonieren','das Telefon','der Termin','der Terminkalender'])
add('Stadt, Ämter & Recht', ['der Täter / die Täterin',])
add('Menge, Maß & Eigenschaften', ['scharf','spannend','spitz','stark','steil',
    'streng','super','tief','stilistisch','teuer'])
add('In der Wohnung & Zuhause', ['das Schild','das Schloss',
    'die Schachtel','das Stiegenhaus','die Stiege','der Stock','das Stockwerk',
    'der Stuhl','der Teppich','die Terrasse',
    'der Staub'])
add('Gefühle & Charakter', ['stolz','still'])
add('Zeit & Kalender', ['der Schluss','starten','der Start','die Stunde'])
add('Unterwegs & Verkehr', [
    'die Stadt','städtisch','der Stadtplan',
    'der Stau',
    'die Straße','die Straßenbahn','die Strecke','tanken','die Tankstelle','die Spur',
    'der Stecker','die Steckdose'])
add('Einkaufen & Geld', [
    'das Sonderangebot','der Supermarkt','die Summe',
    'die Statistik','statistisch','die Steuer','der Test','testen','die Tasche',
    'das Taschengeld','die Tabelle'])
add('In der Wohnung & Zuhause', ['das Streichholz',
    ])
add('Stadt, Ämter & Recht', ['der Stempel','(sich) streiten','der Streit','streiken',
    'der Streik','der Stress',])
add('Natur, Wetter & Umwelt', ['der Stein','der Strand',
    ])
add('Freizeit, Medien & Technik', ['die Studie','studieren','das Studium','die Technik',
    'technisch','die Technologie'])
add('Kleidung & Aussehen', ['der Stiefel','der Strumpf','das Taschentuch'])
add('Gefühle & Charakter', ['sympathisch',])
add('Grammatik & Verbindungswörter', ['die Stufe','das Teil','der Teil','das Stück/-stück'])
add('Freizeit, Medien & Technik', [])
add('Tiere', ['das Tier','das Haustier','der Tierpark'])
add('Denken, Wissen & Meinen', ['der Tipp',])
add('Kommunikation & Post', ['der Text'])
add('Einkaufen & Geld', [])
add('In der Wohnung & Zuhause', ['der Tisch'])
add('Handlungen: Alltagsverben', ['teilen','tauchen'])
add('Kommunikation & Post', [])
add('Familie & Beziehungen', ['die Tante'])

# =====================================================================
# GAP FILL 8: idx 1452-2610
# =====================================================================
add('Grammatik & Verbindungswörter', ['überall','überhaupt','übermorgen','übrig','übrigens',
    'um','um … zu','umso','umsonst','un-','unbedingt','und','ungefähr','unten','unter',
    'unter-','unterwegs','ursprünglich','vermutlich','trotz','trotzdem'])
add('Handlungen: Alltagsverben', ['leihen','retten','stehlen','stinken','(sich) stoßen',
    'tragen','treffen','treiben','treten','tun','üben','überlegen','übernehmen',
    'unterbrechen','unternehmen','unterscheiden','verlassen','verlieren','(sich) verstecken',
    '(sich) verstehen','versuchen','vermeiden','verteilen','vergleichen','der Vergleich',
    'verpacken'])
add('In der Wohnung & Zuhause', ['der Sessel','der Sessel','der Stift','der Stoff',
    'die Tafel','der Topf','die Vase','die Treppe','das Treppenhaus','die Tür',
    'das Tuch','die Uhr'])
add('Freizeit, Medien & Technik', ['die Rolle','die Rose','die Runde','der Salon',
    'das Souvenir','die Station','der Titel',
    'toll','der Tourismus','der Tourist / die Touristin','die Tradition','traditionell',
    'trainieren','der Trainer / die Trainerin','das Training','träumen','der Traum',
    'Traum-','der Turm'])
add('Essen, Kochen & Restaurant', ['die Semmel','der Service','der Speisewagen',
    'die Tomate','die Torte',])
add('Zeit & Kalender', ['die Saison',
    'übernachten','die Übernachtung','die Vergangenheit'])
add('Schule & Bildung', ['das Seminar','das System','der Stil','theoretisch',
    'die Universität','unterrichten','der Unterricht','übersetzen',
    'der Übersetzer / die Übersetzerin','die Übersetzung'])
add('Körper & Gesundheit', [
    'schädlich','die Temperatur','der Tod','tödlich','tot','der Tote / die Tote',
    'die Träne','untersuchen','die Untersuchung'])
add('Reisen & Urlaub', ['die Rezeption/Reception',
    
    'transportieren','der Transport','der Urlaub',
    'die Unterkunft','verreisen'])
add('Denken, Wissen & Meinen', ['die Störung',
    '(sich) überzeugen','die Überzeugung',
    'überraschen','die Überraschung','typisch','der Typ','vermuten','vernünftig'])
add('Stadt, Ämter & Recht', ['das Schaufenster',
    'die Urkunde','das Urteil','verhaften',
    'der Verdacht','verdächtig','der Verbrecher / die Verbrecherin','das Verbot',
    'verbieten','verboten','die Uniform','untersagt','unterschreiben','die Unterschrift',
    'die Ursache','verursachen','verraten','die Versammlung'])
add('Natur, Wetter & Umwelt', ['der Strom','das Ufer','die Umgebung','die Umwelt',
    'der Umweltschutz','die Umweltverschmutzung','trocken','trocknen'])
add('Unterwegs & Verkehr', [
    'das Trottoir','die U-Bahn','überfahren',
    'überholen','überqueren','die Umleitung',
    'umsteigen','der Verkehr','das Verkehrsmittel','das Velo','das Tram'])
add('Menge, Maß & Eigenschaften', ['der Satz','total',
    'treu',
    'übertreiben','umgekehrt','ungewöhnlich',
    'unglaublich','unheimlich','verschieden','verständlich',])
add('Gefühle & Charakter', ['traurig',
    'verliebt','sich verlieben','verrückt',
    'vergnügt','sich vergnügen','das Vergnügen','das Unglück',])
add('Familie & Beziehungen', ['die Tochter','der Vater','(sich) verabreden','verabredet',
    'die Verabredung','(sich) verabschieden','der Abschied','(sich) verändern',
    'verantwortlich','die Verantwortung',
    'verheiratet',
    '(sich) trennen','die Trennung','getrennt leben'])
add('Kommunikation & Post', ['die Überschrift','überreden','die Umfrage',
    'umarmen','(sich) umdrehen','vereinbaren','verlangen',
    '(sich) unterhalten','die Unterhaltung'])
add('Schule & Bildung', ['die Übung',])
add('Grammatik & Verbindungswörter', ['über'])
add('Arbeit & Beruf', ['die Überstunde',
    'die Unterlagen','der Unternehmer / die Unternehmerin','die Unterstützung',
    'unterstützen','verdienen','der Verein','der Verlag',
    ])
add('Zeit & Kalender', [
    'die Verspätung','verpassen'])
add('In der Wohnung & Zuhause', ['umziehen','der Umzug',
    'sich umziehen'])
add('Kleidung & Aussehen', [
    'die Tüte',])
add('Menge, Maß & Eigenschaften', ['unterschiedlich','vergrößern','verlängern'])
add('Handlungen: Alltagsverben', ['unterlassen',
    'verpflichtet','verschieben','verschwinden','vergessen','verbringen','verbrauchen',
    'verbinden','die Verbindung','(sich) verbessern','(sich) verbrennen',
    'unterstreichen','vergeblich','umtauschen','der Umtausch',])
add('Denken, Wissen & Meinen', ['das Verständnis','das Verhalten','sich verhalten',
    'das Verhältnis'])
add('Einkaufen & Geld', ['verkaufen',
    'der Verkäufer / die Verkäuferin','vermieten','der Vermieter / die Vermieterin',
    'die Vermietung','die Versicherung','versichern','die Versichertenkarte',
    'die Vermittlung','der Verlust',])
add('Essen, Kochen & Restaurant', ['vegetarisch','verpflegen'])
add('Zeit & Kalender', [])
add('Menge, Maß & Eigenschaften', [])
add('Körper & Gesundheit', ['verschreiben','(sich) verletzen','die Verletzung',
    'sich verlaufen','vermissen'])
add('Grammatik & Verbindungswörter', [
    'vertrauen',])
add('Gefühle & Charakter', ['der Verlierer / die Verliererin','vertrauen','das Vertrauen'])
add('Kommunikation & Post', ['versprechen'])

# =====================================================================
# GAP FILL 9 (FINAL): idx 1825-2885
# =====================================================================
add('Grammatik & Verbindungswörter', ['von','voneinander','vor','vor allem','voraus',
    'vorbei/vorbei-','vorder-','vorgestern','vorher','vorhin','vorläufig','vorn',
    'wahrscheinlich','während','wann','warum','was','was für ein-','weder … noch',
    'weg/weg-','wegen','weil','weit','weiter/weiter-','welcher','wenig/wenige',
    'wenigstens','wenn','wer','weshalb','wie','wieder/wieder-','wieso','wie viel',
    'wo','woher','wohin','wohl','worüber','worum','zu','zuerst','zufällig','zumindest',
    'zunächst','zurück/zurück-','zurzeit','zusammen/zusammen-','zwar','zwischen',
    'zuletzt','viel/viele','vielleicht','völlig','waagerecht','zu sein','wachsen'])
add('Denken, Wissen & Meinen', ['die Praxis','der Unterschied','die Voraussetzung',
    'wählen','die Wahl','wahr','die Wahrheit','wichtig','widersprechen','wissen',
    'das Wissen','die Wissenschaft','der Wissenschaftler / die Wissenschaftlerin',
    'wirklich','die Wirklichkeit','der Zweifel','zweifeln','der Zusammenhang',
    'zustimmen','die Zustimmung','vorkommen'])
add('Kommunikation & Post', ['überprüfen','üblich','der Vertreter / die Vertreterin',
    'die Vertretung','vertreten','verzeihen','Verzeihung','die Visitenkarte',
    'die Vorwahl','vorlesen','der Vortrag','warnen','wecken','der Wecker',
    'die Werbung','der Witz','zeigen','die Zeile','das Wort','das Wort',
    'das Wörterbuch','vorschlagen','der Vorschlag','(sich) vorstellen',
    'die Vorstellung'])
add('Einkaufen & Geld', ['überweisen','die Überweisung',
    'der Vertrag','zahlen','die Zahlung',
    'zählen',
    'die Zinsen','der Zoll',
    'der Zuschlag',])
add('Stadt, Ämter & Recht', ['der Unfall',
    'verhindern','versäumen','verurteilen','die Verwaltung','das Visum','die Vorschrift',
    'die Vorfahrt','der Vorwurf','der Zeuge / die Zeugin',
    'das Zeugnis','das Zertifikat','der Zivilstand'])
add('Familie & Beziehungen', ['verwandt','der Verwandte / die Verwandte',
    'der Wirt / die Wirtin',])
add('Freizeit, Medien & Technik', ['der Versuch','das Video','virtuell','der Virus',
    'der Wettbewerb',
    'wetten','der Zirkus','der Zoo','der Zuschauer / die Zuschauerin','zuschauen'])
add('Menge, Maß & Eigenschaften', ['verwechseln','tolerant','das Tempo','voll',
    'wahnsinnig','wertlos','wertvoll','wert','der Wert',
    'weiblich','weich','zahlreich','ziemlich','zuverlässig','zufrieden','wild'])
add('Handlungen: Alltagsverben', ['verwenden','verzichten','warten','(sich) waschen',
    'wechseln','sich weigern','weinen','wenden','werfen','wiegen','winken','ziehen',
    'zugehen','zumachen','zunehmen','zurechtkommen','zusagen','zusammenfassen',
    'wehtun','vorhaben','(sich) vorbereiten','die Vorbereitung'])
add('Reisen & Urlaub', ['die Toilette','der Treffpunkt','das Trinkgeld','die Tropfen',
    'das Viertel','der Vorort','der Wohnort','der Wohnsitz',
    'das/der Zvieri/Znüni'])
add('In der Wohnung & Zuhause', ['das Tor',
    'die Wand','das Wasser','die Wäsche','das Waschmittel',
    'die Wohnung','das Wohnzimmer','das Zimmer',
    'der Zettel','wohnen',
    'zentral',])
add('Körper & Gesundheit', ['die Zahncreme/-pasta','der Zahn','die Zange','die Wunde',
    ])
add('Essen, Kochen & Restaurant', ['trinken','das Rüebli','der Wein','die Zitrone',
    'die Zwiebel','die Wurst'])
add('Natur, Wetter & Umwelt', ['der Wald','wandern','die Wanderung','die Wärme',
    'warm','das Wetter','der Wetterbericht','die Wettervorhersage','der Wind',
    'windig','die Wiese','die Wolke','bewölkt','die Wolle','zerstören'])
add('Arbeit & Beruf', ['die Weiterbildung','das Werk','die Werkstatt','das Werkzeug',
    'zugänglich',
    'zuständig'])
add('Unterwegs & Verkehr', ['umgehen','der Wagen',
    'der Zug','die Zone',])
add('Gefühle & Charakter', ['wach',
    'wütend','wunderbar','wunderschön','sich wundern','das Wunder','(sich) wünschen',
    'der Wunsch','willkommen','wirken','die Wirkung'])
add('Zeit & Kalender', ['die Zahl','die Anzahl',
    'voraussichtlich','das Zeichen','das Verkehrszeichen','zeichnen','die Zeichnung',
    'die Zeit','der Zeitpunkt','zurzeit','das Zelt','zelten',
    'die Zukunft','zukünftig','die Zünder','das Zündholz'])
add('Kommunikation & Post', ['die Zeitschrift','die Zeitung','wiederholen',
    'die Wiederholung'])
add('Denken, Wissen & Meinen', [])
add('Gesellschaft, Politik & Wirtschaft', ['die Wirtschaft',
    'die Welt','weltweit','die Zusammenarbeit','zusätzlich'])

# =====================================================================
# GAP FILL 10 (LAST 30)
# =====================================================================
add('Körper & Gesundheit', ['die Praxis','das Vitamin'])
add('Freizeit, Medien & Technik', ['die Veranstaltung','Volleyball'])
add('Arbeit & Beruf', ['die Vollzeit','das Vorstellungsgespräch','der Zufall'])
add('Gefühle & Charakter', ['die Vorsicht','vorsichtig'])
add('Menge, Maß & Eigenschaften', ['der Vorteil','vorwärts','-weise'])
add('Einkaufen & Geld', ['die Ware','der Zucker','die Zutaten'])
add('Unterwegs & Verkehr', ['der Weg'])
add('Grammatik & Verbindungswörter', ['werden','wollen','der Zweck'])
add('In der Wohnung & Zuhause', ['das Zentrum','das Zuhause','der Zugang'])
add('Kleidung & Aussehen', ['das Zeug/-zeug'])
add('Denken, Wissen & Meinen', ['das Ziel','der Zustand'])
add('Essen, Kochen & Restaurant', ['die Zigarette','zubereiten'])
add('Kommunikation & Post', ['zuhören','der Zuhörer / die Zuhörerin'])
add('Familie & Beziehungen', ['(sich) zwingen'])

if __name__ == '__main__':
    entries = load_entries()
    by_string = {}
    for e in entries:
        by_string.setdefault(e['canonical'], []).append(e['idx'])

    assigned_idx = set()
    not_found = []  # (topic, word) pairs whose string doesn't match any entry
    claimed_by = {}  # idx -> list of topics (to detect + report overlaps)

    for topic, words in TOPICS.items():
        for w in words:
            candidates = by_string.get(w)
            if not candidates:
                not_found.append((topic, w))
                continue
            # find first candidate index not yet consumed by an earlier
            # occurrence of this same string; if all consumed, reuse last
            # (means the same word is intentionally listed in >1 topic)
            unused = [c for c in candidates if c not in assigned_idx]
            idx = unused[0] if unused else candidates[-1]
            assigned_idx.add(idx)
            claimed_by.setdefault(idx, []).append(topic)

    all_idx = set(e['idx'] for e in entries)
    missing = sorted(all_idx - assigned_idx)

    print(f"Total entries: {len(entries)}")
    print(f"Assigned (unique rows): {len(assigned_idx)}")
    print(f"Missing: {len(missing)}")
    if not_found:
        print(f"\n=== WORDS NOT FOUND IN CSV ({len(not_found)}) ===")
        for topic, w in not_found:
            print(f"  [{topic}] {w!r}")
    if missing:
        print(f"\n=== MISSING ENTRIES ({len(missing)}) ===")
        for idx in missing:
            print(f"  {idx}\t{entries[idx]['canonical']!r}\t{entries[idx]['raw']!r}")

    multi = {idx: t for idx, t in claimed_by.items() if len(t) > 1}
    print(f"\nEntries claimed by >1 topic: {len(multi)}")

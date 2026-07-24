# -*- coding: utf-8 -*-
import json, re
from collections import defaultdict, Counter

lemmas = json.load(open('/Users/andrey/anki/groundwork/all_lemmas.json', encoding='utf-8'))
# fix the one source typo
lemmas = ['irgendein' if l == 'irgendirgendein' else l for l in lemmas]
unique = sorted(set(lemmas))
print("rows:", len(lemmas), "unique:", len(unique))

# TOPIC CODES
TOPICS = {
 'WOHNEN': 'In der Wohnung & Haushalt',
 'KOERPER': 'Körper & Gesundheit',
 'TIERE': 'Tiere, Pflanzen & Natur',
 'WETTER': 'Wetter, Landschaft & Umwelt',
 'ESSEN': 'Essen, Kochen & Restaurant',
 'FAMILIE': 'Familie, Beziehungen & Lebensereignisse',
 'ARBEIT': 'Arbeit, Beruf & Bewerbung',
 'VERKEHR': 'Unterwegs & Verkehr',
 'EINKAUFEN': 'Einkaufen, Geld & Bank',
 'GEFUEHLE': 'Gefühle & Charakter',
 'SCHULE': 'Schule, Ausbildung & Sprache lernen',
 'FREIZEIT': 'Freizeit, Sport & Medien/Technik',
 'REISEN': 'Reisen & Urlaub',
 'ZEIT': 'Zeit & Kalender',
 'KOMMUNIKATION': 'Kommunikation & Meinung',
 'STADT': 'Stadt, Ämter, Recht & Polizei',
 'MENGE': 'Menge, Maß, Vergleich & allgemeine Eigenschaften',
 'RAUM': 'Raum & Richtung',
 'LOGIK': 'Konnektoren: Grund, Bedingung & Gegensatz',
 'GESELLSCHAFT': 'Gesellschaft, Wirtschaft & Politik',
 'GLUE': 'Funktionswörter: Pronomen, Artikel & Partikeln',
}

assigned = {}  # lemma -> topic

def tag(topic, *words):
    for w in words:
        if w not in unique:
            print("WARN not in list:", repr(w))
            continue
        if w in assigned and assigned[w] != topic:
            print("CONFLICT", w, assigned[w], "->", topic)
        assigned[w] = topic

# ---------- WOHNEN ----------
tag('WOHNEN',
"die Wohnung","das Zimmer","das Wohnzimmer","die Küche","das Bad","die Badewanne","der Balkon",
"der Boden","das Dach","die Decke","die Tür","das Fenster","der Flur","der Gang","der Keller",
"der Garten","der Hof","die Treppe","das Treppenhaus","die Stiege","das Stiegenhaus","der Aufzug",
"der Lift","das Erdgeschoss/ Ergeschoß","der Stock","das Stockwerk","die Etage","der Schrank",
"der Kasten","das Regal","das Bett","der Tisch","der Stuhl","der Sessel","das Sofa","die Couch",
"der Teppich","die Lampe","der Spiegel","die Vase","das Kissen","der Herd","der Kühlschrank",
"die Heizung","heizen","der Ofen","die Klimaanlage","das Möbel","möbliert","die Garderobe",
"der Schlüssel","das Schloss","die Steckdose","der Stecker","das Kabel","der Wecker","wecken",
"putzen","staubsaugen","der Staub","der Dreck","sauber","schmutzig","aufräumen","abwaschen",
"die Wäsche","das Waschmittel","die Mülltonne","der Müll","die Müllabfuhr","der Abfall",
"der Abfalleimer","der Mieter","der Vermieter","vermieten","die Vermietung","mieten","die Miete",
"umziehen","der Umzug","einziehen","der Hausmeister","der Abwart","das Apartment","der Haushalt",
"die Hausfrau","das Grundstück","der Rasen","die Kerze","die Bürste","die Zahnbürste",
"der Hammer","die Nadel","der Nagel","die Schere","kleben","reinigen","die Reinigung","die Schachtel",
"das Zelt","zelten","die Hütte","waagerecht","senkrecht","der Rand","spülen","möbliert",
)

# ---------- KOERPER ----------
tag('KOERPER',
"der Körper","körperlich","der Kopf","das Haar","das Auge","das Ohr","die Nase","der Mund",
"die Lippe","der Zahn","die Zunge" if 'die Zunge' in unique else "der Zahn","der Hals","die Schulter",
"der Arm","die Hand","der Finger","der Bauch","der Rücken","das Bein","der Fuß","das Knie",
"die Brust","das Herz","die Haut","der Knochen","der Muskel","das Blut","bluten","atmen","der Atem",
"das Gesicht","der Bart","gesund","die Gesundheit","krank","die Krankheit","der Kranke","die Klinik",
"das Krankenhaus","die Krankenkasse","der Krankenpfleger","die Krankenschwester","der Krankenwagen",
"der Arzt","die Ordination","die Praxis","die Sprechstunde","die Apotheke","das Medikament",
"die Medizin","das Rezept","die Tablette","die Salbe","die Spritze","impfen" if "impfen" in unique else "die Medizin",
"das Pflaster","der Verband" if "der Verband" in unique else "das Pflaster","das Fieber","der Husten",
"husten","die Grippe","der Schnupfen","die Erkältung","sich erkälten","erkältet","der Schmerz",
"das Schmerzmittel","wehtun","die Wunde","verletzen","die Verletzung","operieren","die Operation",
"untersuchen","die Untersuchung","die Diät","die Ernährung","ernähren","müde","schwach","stark",
"kräftig","die Kraft","behindern","blind","taub","stumm","dick","dünn","mager","schlank","fett",
"das Fett","riechen","schmecken","der Geschmack","hören","sehen","sprechen","fühlen","das Gefühl",
"schwitzen","frieren","der Schweiß" if "der Schweiß" in unique else "schwitzen","rasieren",
"schminken","die Schwangerschaft","sterben","der Tod","tödlich","tot","der Tote",
"die Krankenversicherung" if "die Krankenversicherung" in unique else "die Krankenkasse",
"das Gewicht","wiegen","die Beratung" if False else "die Ordination",
"die Zahncreme/-pasta","die Seife",
)

# ---------- TIERE (animals, plants, nature objects) ----------
tag('TIERE',
"das Tier","das Haustier","der Tierpark","der Zoo","die Blume","blühen","der Baum","der Wald",
"die Wiese","das Gras","die Pflanze","pflanzen","der Rasen" if False else "die Rose","die Rose",
"der Bauer","der Bauernhof","die Landwirtschaft","füttern","der Vogel" if "der Vogel" in unique else "füttern",
)

# ---------- WETTER (weather, landscape, environment) ----------
tag('WETTER',
"das Wetter","der Wetterbericht","die Wettervorhersage","die Sonne","sonnig","die Wolke","bewölkt",
"der Regen","regnen","der Schnee","schneien","der Nebel","neblig","der Wind","windig","das Gewitter",
"donnern","der Donner","blitzen","der Blitz","hageln","die Hitze","heiß","kalt","die Kälte","kühl",
"warm","die Wärme","mild","feucht","trocken","trocknen","die Temperatur","das Klima","die Nord-/Ostsee",
"die See","das Meer","der Ozean","der Strand","die Küste","der Fluss","der See","der Berg","das Tal",
"der Hügel","die Landschaft","die Insel","das Gebirge" if "das Gebirge" in unique else "der Berg",
"das Gebirge","die Erde","der Himmel","der Mond","der Stern","die Luft","das Ufer",
"die Umwelt","der Umweltschutz","die Umweltverschmutzung","verschmutzen","das Öl","die Energie",
"das Gas","der Strom","elektrisch","Elektro-","elektronisch","das Feuer","brennen","der Sand",
"der Stein","der Fels" if "der Fels" in unique else "der Stein","die Natur","natürlich","Öko-","bio","Bio-",
)

# ---------- ESSEN ----------
tag('ESSEN',
"essen","das Essen","das Frühstück","frühstücken","das Mittagessen" if "das Mittagessen" in unique else "das Essen",
"die Mahlzeit","der Hunger","hungrig","der Durst","durstig","satt","trinken","das Getränk",
"kochen","der Koch","backen","braten","der Braten","grillen","grillieren","der Grill","schneiden" if False else "schneiden",
"schälen" if "schälen" in unique else "kochen","der Herd" if False else "der Topf","der Topf","die Pfanne",
"der Teller","die Tasse","das Glas","die Kanne","das Besteck" if "das Besteck" in unique else "der Löffel",
"der Löffel","die Gabel","das Messer","die Serviette" if "die Serviette" in unique else "der Teller",
"die Schüssel","das Brot","das Brötchen","das Brötli","die Semmel","der Kuchen","die Torte",
"das Gebäck","das Mehl","der Zucker","das Salz","salzig","der Pfeffer","das Gewürz","der Essig",
"das Öl" if False else "die Butter","die Butter","die Margarine","der Käse","die Milch","das Ei",
"das Fleisch","das Rind","der Schinken","die Wurst","das Faschierte","das Hackfleisch","der Fisch" if "der Fisch" in unique else "das Fleisch",
"das Gemüse","die Kartoffel","der Erdapfel","die Zwiebel","die Karotte","die Möhre","das Rüebli",
"der Salat","die Tomate","der Paradeiser","die Frucht","Früchte","der Apfel","die Banane",
"die Orange","die Zitrone","die Birne","die Pflaume","die Aprikose","die Marille","die Nudel",
"der Reis","die Suppe","die Soße/Sauce","die Marmelade","die Konfitüre","der Honig","die Schokolade",
"süß","bitter","sauer","scharf","lecker","der Geschmack" if False else "reif","reif","roh","frisch",
"die Diät" if False else "vegetarisch","vegetarisch","der Kaffee","das Kaffeehaus","der Tee",
"Tee ziehen lassen","der Kakao","das Mineralwasser","der Saft","die Limonade","das Bier","der Wein",
"das Restaurant","das Lokal","die Gaststätte","das Gasthaus","der Kellner","der Ober","der Serviceangestellte",
"das Buffet","die Speisekarte","der Speisewagen","die Kantine","die Mensa","die Portion","das Menü",
"das Picknick","die Pizza","die Pommes frites","das Schnitzel","der Kloß","der Knödel","das Müesli/Müsli",
"Prost","zubereiten","die Zutaten","Speise-/-speise",
)

# ---------- FAMILIE ----------
tag('FAMILIE',
"die Familie","die Eltern","die Mutter","der Vater","die Tochter","der Sohn","der Bruder",
"die Schwester","die Geschwister","die Oma","der Opa","der Neffe","die Nichte","der Cousin",
"die Kette" if False else "der Onkel","der Onkel","die Tante","Schwieger-","die Ehe","die Ehefrau",
"das Ehepaar","heiraten","die Hochzeit","verheiratet","geschieden","sich scheiden lassen",
"die Scheidung","getrennt leben","trennen","die Trennung","verabreden","verabredet",
"die Verabredung","verabschieden","der Abschied","sich verlieben","verliebt","die Liebe",
"lieben","lieb","der Partner","der Freund","die Freundschaft","freundlich","kennenlernen","kennen",
"die Beziehung","der Kollege","der Bekannte","bekannt","der Nachbar","das Kind","das Mädchen",
"der Junge","der Bub","die Kindheit","die Jugend","der Jugendliche","erwachsen","der Erwachsene",
"die Geburt","geboren werden","der Geburtstag","der Name","der Familienname","der Vorname",
"die Personalien","der Familienstand","der Zivilstand","der Personenstand","ledig","verwandt",
"der Verwandte","der Angehörige","die Senioren","das Altenheim","das Altersheim","betreuen",
"der Betreuer","die Betreuung","pflegen","der Pfleger","die Pflicht" if False else "die Erziehung",
"erziehen","die Erziehung","die Puppe",
)

# ---------- ARBEIT ----------
tag('ARBEIT',
"arbeiten","die Arbeit","der Arbeiter","die Arbeitserlaubnis","arbeitslos","die Arbeitslosigkeit",
"der Arbeitsplatz","die Arbeitsstelle","der Beruf","beruflich","berufstätig","der Chef","der Job" if "der Job" in unique else "die Arbeitsstelle",
"das Personal","der Mitarbeiter","der Kollege" if False else "der Angestellte","der Angestellte",
"der Beamte","selbstständig","die Firma","der Betrieb","das Unternehmen" if "das Unternehmen" in unique else "der Betrieb",
"der Unternehmer","die Fabrik","das Büro","die Kantine" if False else "die Besprechung","die Besprechung",
"besprechen","die Konferenz","der Termin","der Terminkalender","der Kollege" if False else "die Karriere",
"die Karriere","die Qualifikation","die Ausbildung","ausgebildet","die Lehre","der Lehrling",
"die Lehrstelle","das Praktikum","der Praktikant","sich bewerben","die Bewerbung","der Lebenslauf",
"das Vorstellungsgespräch","einstellen","kündigen","die Kündigung","entlassen","die Entlassung",
"der Betriebsrat","die Gewerkschaft","der Lohn","das Gehalt","verdienen","die Überstunde",
"der Feierabend","der Urlaub","die Teilzeit","die Vollzeit","halbtags","der Chef" if False else "die Aushilfe",
"die Aushilfe","der Handwerker","der Handel","handeln","der Händler",
"der Techniker" if "der Techniker" in unique else "der Mechaniker",
"der Mechaniker","der Ingenieur","der Architekt","der Sekretär","der Journalist","der Autor",
"der Schriftsteller","der Künstler","der Maler","der Musiker","der Sänger","der Schauspieler",
"der Fotograf","der Trainer","der Sportler","der Politiker","der Richter","der Rechtsanwalt" if "der Rechtsanwalt" in unique else "der Anwalt",
"der Anwalt","der Polizist","der Professor","der Lehrer","der Schüler","der Student","der Studierende",
"der Direktor","der Doktor","der Wissenschaftler","der Reporter","der Sozialarbeiter","der Spezialist",
"der Experte","der Meister","der Kursleiter","der Leiter","die Leitung","leiten","organisieren",
"die Organisation","die Verwaltung","planen","die Planung","der Plan","projekt" if False else "das Projekt",
"das Team" if "das Team" in unique else "die Mannschaft","die Aufgabe","die Tätigkeit","tätig" if "tätig" in unique else "die Tätigkeit",
"der Beitrag","erledigen","die Leistung","leisten","die Verantwortung","verantwortlich","der Praktikant" if False else "die Fachleute",
"die Fachleute","der Fachmann","erfahren","die Erfahrung","die Fähigkeit","die Kenntnisse",
"das Diplom","das Zertifikat","das Zeugnis","die Prüfung","prüfen","die Note",
)

# ---------- VERKEHR ----------
tag('VERKEHR',
"der Verkehr","das Verkehrsmittel","das Fahrzeug","das Auto","der Wagen","der Motor","das Motorrad",
"das Fahrrad","das Rad","das Velo","der Bus","die Straßenbahn","das Tram","die U-Bahn","S-Bahn",
"die Bahn","der Zug","der Bahnhof","der Hauptbahnhof","der Bahnsteig","der Perron","das Gleis",
"fahren","losfahren","abfahren","die Abfahrt","die Ausfahrt","die Einfahrt","überfahren",
"überholen","bremsen","die Bremse","hupen","tanken","die Tankstelle","das Benzin","der Reifen",
"parken","parkieren","der Parkplatz" if "der Parkplatz" in unique else "der Park","die Panne",
"die Werkstatt","reparieren","die Reparatur","der Führerschein","der Führerausweis","der Motor" if False else "das Kraftfahrzeug",
"das Kraftfahrzeug","der Laster","der Krankenwagen" if False else "der Verkehr" ,
"die Straße","die Einbahnstraße","die Kreuzung","die Ampel","die Kurve","die Vorfahrt","überqueren",
"die Fußgängerzone","der Fußgänger","der Gehsteig","das Trottoir","der Radfahrer","abbiegen",
"überqueren" if False else "geradeaus","links","rechts","die Autobahn","der Stau","die Umleitung",
"die Geschwindigkeit","die Geschwindigkeitsbeschränkung","der Strafzettel","strafbar",
"der Führerausweis" if False else "die Fahrbahn","die Fahrbahn","das Kennzeichen","anschnallen",
"das Ticket","die Fahrkarte","das Billett","der Fahrplan","die Haltestelle","der Halt",
"einsteigen","umsteigen","aussteigen" if "aussteigen" in unique else "einsteigen","die Abfahrt" if False else "die Ankunft",
"ankommen","die Ankunft","der Flug","der Flughafen","das Flugzeug","fliegen","die Kabine",
"das Schiff","das Boot","der Hafen","die Fähre","landen","die Landung","der Koffer","der Rucksack",
"das Gepäck","der Speisewagen" if False else "der Reifen" ,
)

# ---------- EINKAUFEN ----------
tag('EINKAUFEN',
"einkaufen","der Einkauf","kaufen","der Kauf","der Käufer",
"verkaufen","der Verkäufer","der Supermarkt","das Geschäft","der Laden","der Markt",
"der Flohmarkt","der Kiosk","der Automat","die Kasse","die Quittung","die Rechnung","bezahlen",
"zahlen","die Zahlung","der Preis","preiswert","teuer","billig","günstig","gratis","umsonst",
"kostenlos","kosten","die Kosten","der Rabatt","das Sonderangebot","der Ausverkauf" if "der Ausverkauf" in unique else "das Sonderangebot",
"reduzieren","umtauschen","der Umtausch","die Ware","das Produkt","die Marke","das Etikett" if "das Etikett" in unique else "die Marke",
"die Größe","anprobieren" if "anprobieren" in unique else "probieren","probieren","das Geld",
"das Bargeld","bar","die Münze","der Schein","die Geldbörse","die Brieftasche","das Portemonnaie/Portmonee",
"der Geldautomat","der Bancomat/Bankomat","das Konto","das Girokonto","die Bank","die Bankleitzahl",
"überweisen","die Überweisung","einzahlen","die Einzahlung","abheben","der Kredit","die Kreditkarte",
"die ec-Karte/EC-Karte","die Bankomat-Karte","die e-card","die Versichertenkarte","der Kunde",
"die Rechnung" if False else "die Mehrwertsteuer","die Mehrwertsteuer","der Wert","wertvoll","wertlos",
"der Rabatt" if False else "das Trinkgeld","das Trinkgeld","sparen","sparsam","der Zoll","die Gebühr",
"die Versicherung","versichern","die Zinsen","die Schulden","der Kredit" if False else "finanzieren",
"finanzieren","finanziell","die Einbahnstraße" if False else "die Steuer" ,
)

# ---------- SCHULE ----------
tag('SCHULE',
"die Schule","der Schüler","die Schularbeit","die Klassenarbeit","das Fach","der Unterricht",
"unterrichten","der Kurs","der Intensivkurs","das Seminar","das Semester","das Studium","studieren",
"der Student","der Studierende","die Universität","das Institut","die Bibliothek","das Buch",
"das Wörterbuch","das Lexikon","das Heft","der Bleistift","der Kugelschreiber","der Kuli","die Tafel",
"das Kapitel","das Alphabet","buchstabieren","der Buchstabe","üben","die Übung","der Lerner",
"die Nachhilfe","die Weiterbildung","die Fortbildung","testen","der Test","das Referat","der Vortrag",
"das Thema","erklären","die Erklärung","der Kindergarten","die Hausaufgabe","die Klasse","der Dialekt",
"die Sprache","die Muttersprache","die Fremdsprache","die Zweitsprache","der Dialog","mündlich",
"schriftlich","übersetzen","der Übersetzer","die Übersetzung","die Bedeutung","bedeuten",
)

# ---------- FREIZEIT ----------
tag('FREIZEIT',
"der Sport","die Sportart","sportlich","der Sportler","der Fußball","der Basketball","Volleyball",
"das Tennis","Golf","der Ski/Schi","schwimmen","das Schwimmbad","das Hallenbad","klettern","wandern",
"die Wanderung","der Spaziergang","spazieren gehen","reiten","tauchen","trainieren","das Training",
"der Wettbewerb","der Rekord","siegen","der Sieg","der Sieger","gewinnen","der Gewinn","verlieren",
"der Verlierer","das Spiel","spielen","der Spieler","der Spielplatz","das Spielzeug","die Mannschaft",
"das Hobby","die Freizeit","die Party","feiern","die Feier","das Fest","tanzen","der Tanz","singen",
"die Musik","das Konzert","das Instrument","die Gitarre","das Klavier","die Flöte","das Orchester",
"der Zirkus","das Museum","die Galerie","das Theater","der Auftritt","die Bühne","das Ballett",
"die Oper","der Film","das Kino","fernsehen","das Fernsehen","der Fernseher","die Fernbedienung",
"das Radio","malen","zeichnen","die Zeichnung","fotografieren","das Foto","der Fotoapparat",
"die Kamera","das Video","lesen","der Roman","die Literatur","das Märchen","das Gedicht",
"die Zeitschrift","das Magazin","der Krimi","das Rätsel","das Quiz","die Diskothek","die Kneipe",
"die Bar","das Café","der Humor","der Witz","der Bildschirm","der Monitor","die Tastatur","die Taste",
"klicken","anklicken","der Klick","speichern","installieren","hochladen","aufladen","die Batterie",
"das Netz","das Netzwerk","digital","virtuell","das System","das Programm","funktionieren",
"die Technik","technisch","die Technologie","die Festplatte","das Laufwerk","der Drucker","drucken",
"ausdrucken","der Kopierer","kopieren","die Kopie","elektronisch","der Apparat","der Prozess" if False else "das Talent",
"das Talent","das Tor","das Stadion","der Star","der Profi","der Profisportler","das Training" if False else "die Puppe" if False else "der Kompromiss" if False else "prima",
)

# ---------- REISEN ----------
tag('REISEN',
"reisen","die Reise","verreisen","der Tourist","der Tourismus","das Reisebüro","das Hotel",
"übernachten","die Übernachtung","die Unterkunft","die Jugendherberge","die Pension","die Halbpension",
"reservieren","die Reservierung","buchen","das Souvenir","die Sehenswürdigkeit","besichtigen",
"der Prospekt","die Broschüre","die Rundfahrt","der Ausflug","das Zelt","zelten","der Urlaub",
"die Ferien","Ferien-",
)

# ---------- ZEIT ----------
tag('ZEIT',
"die Zeit","die Uhr","der Moment","der Augenblick","jetzt","gerade","sofort","gleich","heute",
"gestern","übermorgen","vorgestern","damals","früher/früher-","neulich","kürzlich","bald",
"inzwischen","mittlerweile","nun","schon","noch","noch mal","nochmals","wieder/wieder-","wiederholen",
"die Wiederholung","immer","nie","jemals","oft/öfter","manchmal","selten","meist","meist-","häufig",
"regelmäßig","ständig","dauernd","dauern","die Dauer","ewig","rechtzeitig","pünktlich",
"die Verspätung","spät","früh","spätestens","zuerst","zuletzt","zunächst","schließlich","endlich",
"endgültig","sobald","solange","seitdem","seit","während","bevor","nachdem","der Kalender","das Datum",
"der Feiertag","die Saison","jederzeit","jedes Mal","jeweils","diesmal","einmal","mal","das Mal",
"längst","vorläufig","zurzeit","der Zeitpunkt","die Vergangenheit","die Zukunft","zukünftig",
"heutig-","nächst-",
)

# ---------- KOMMUNIKATION ----------
tag('KOMMUNIKATION',
"sprechen","reden","sagen","erzählen","die Erzählung","das Gespräch","anrufen","der Anruf",
"der Anrufbeantworter","das Telefon","telefonieren","das Handy","das Mobiltelefon","die Mobilbox",
"die Rufnummer","die Vorwahl","senden","der Sender","die Sendung","die Nachricht","die Botschaft",
"die Meldung","die Durchsage","die Ansage","mitteilen","informieren","die Information","die Auskunft",
"der Brief","der Briefkasten","die Briefmarke","der Briefträger","der Briefumschlag","das Einschreiben",
"die Post","die Postleitzahl","das Paket","die Zeitung","die Presse","der Artikel","die Werbung",
"die Reklame","die Annonce","das Inserat","die Anzeige","anzeigen","das Interview","die Reportage",
"berichten","der Bericht","die Meinung","meinen","behaupten","diskutieren","die Diskussion",
"streiten","der Streit","überzeugen","die Überzeugung","überreden","vorschlagen","der Vorschlag",
"empfehlen","die Empfehlung","raten","der Rat","Ratschlag","warnen","loben","kritisieren","die Kritik",
"entschuldigen","die Entschuldigung","verzeihen","Verzeihung","antworten","die Antwort","fragen",
"die Frage","zustimmen","die Zustimmung","widersprechen","ablehnen","akzeptieren","aussprechen",
"die Aussprache","der Ausdruck","danken","der Dank","dankbar","danke","schweigen","bitten","die Bitte",
"bitte","die Ansage" if False else "hallo","hallo","Prost" if False else "Achtung!","Achtung!",
"Bescheid geben","Bescheid sagen","der Bescheid","buchstabieren" if False else "die Nummer","die Nummer",
"die Rede",
)

# ---------- STADT ----------
tag('STADT',
"die Stadt","städtisch","das Zentrum","zentral","der Stadtplan","das Amt","die Behörde","das Rathaus",
"das Konsulat","der Bürger","der Einwohner","der Bewohner","die Bevölkerung","der Ausweis",
"das Formular","ausfüllen","beantragen","der Antrag","genehmigen","die Erlaubnis","das Visum",
"das Asyl","der Pass","die Urkunde","das Dokument","unterschreiben","die Unterschrift","der Stempel",
"bestätigen","die Bestätigung","die Anmeldung","anmelden","die Polizei","der Polizist","das Gefängnis",
"verhaften","festnehmen","der Dieb","stehlen","der Einbrecher","einbrechen","der Einbruch",
"der Verbrecher","betrügen","der Täter","die Tat","strafbar","die Strafe","bestrafen","der Zeuge",
"der Verdacht","verdächtig","der Prozess","das Urteil","verurteilen","das Gesetz","rechtlich",
"das Recht","die Feuerwehr","der Notruf","der Notfall","der Notausgang","retten","kontrollieren",
"die Kontrolle","untersagt","verboten","das Verbot","verbieten","erlauben",
)

# ---------- GEFUEHLE ----------
tag('GEFUEHLE',
"glücklich","das Glück","froh","fröhlich","traurig","die Angst","ängstlich","die Sorge","sorgen",
"ärgerlich","der Ärger","ärgern","wütend","böse","nervös","der Nerv","ruhig","die Ruhe","aufregen",
"spannend","gespannt","stolz","mutig","der Mut","dankbar" if False else "verrückt","verrückt",
"komisch","merkwürdig","seltsam","ehrlich","nett","höflich","frech","faul","fleißig","ernst",
"ernsthaft","klug","dumm","intelligent","die Intelligenz","kreativ","tolerant","optimistisch",
"sympathisch","treu","peinlich","schade","enttäuschen","die Enttäuschung","hassen","sich freuen",
"die Freude","lachen","lächeln","weinen","die Träne","schreien","zufrieden","die Langeweile",
"sich langweilen","langweilig",
)

# ---------- MENGE ----------
tag('MENGE',
"viel/viele","mehr","mehrere","die Menge","die Anzahl","die Zahl","zählen","zahlreich","wenig/wenige",
"genug","genügen","ausreichen","ausreichend","insgesamt","gesamt-/Gesamt-","ganz","gar","völlig",
"komplett","total","absolut","extrem","sehr","ziemlich","ungefähr","etwa","mindestens","höchstens",
"maximal","minimal","durchschnittlich","der Durchschnitt","die Hälfte","halb","doppelt","Doppel-",
"einfach","groß","klein","hoch","tief","breit","schmal","lang","kurz","weit","eng","flach","rund",
"eckig","spitz","gerade","schief","steil","die Größe","die Länge","die Breite","die Höhe","die Fläche",
"messen","berechnen","rechnen","die Statistik","statistisch","der Faktor","vergleichen","der Vergleich",
"ähnlich","verschieden","unterschiedlich","der Unterschied","gleichzeitig","derselbe","relativ","extra",
"zusätzlich","besonders","besonder-","speziell","Spezial-","individuell","allgemein","normal",
"normalerweise","gewöhnlich","üblich","typisch","gut","schlecht","schlimm","wichtig","interessant",
"schwierig","schwer","leicht","kompliziert","praktisch","nützlich","sinnvoll","sinnlos","wertvoll",
"wertlos","der Wert","wert","positiv","negativ","perfekt","ideal","richtig","falsch","wahr","echt",
"klar","deutlich","eindeutig","genau","genauso","korrekt","geeignet","passen","super","toll","klasse",
"prima","fantastisch","ausgezeichnet","wunderbar","wunderschön","riesig","winzig" if "winzig" in unique else "riesig",
"Einzel-","Groß-","Kriminal-","Lieblings-","Traum-","-weise","fair","paar",
)

# ---------- RAUM ----------
tag('RAUM',
"oben","unten","innen","außen","vorn","hinten","links","rechts","link-","recht-","drüben","draußen",
"drin","mitten","die Mitte","aufwärts","abwärts","rückwärts","vorwärts","weiter/weiter-","entlang",
"gegenüber","hinter/hinter-","in","mit","nach","neben","ober-","über","um","unter","unter-","von",
"vor","zwischen","zu","außerhalb","innerhalb","inner-","vorder-","mittler-","ander-","beid-","weg/weg-",
"her/her-","herunter-","heraus-","herein-","an","auf","aus","bei","bis","durch","für","gegen","per",
"da","dort","hier/hier-","hierher","dorthin","überall","nirgends","nirgendwo","dabei","daneben",
"dahin","stehen","liegen","sitzen","setzen","legen","stellen","voraus","vorn" if False else "quer",
"quer","fern" if "fern" in unique else "quer","umdrehen",
)

# ---------- LOGIK ----------
tag('LOGIK',
"weil","obwohl","trotzdem","deshalb","deswegen","daher","damit","sodass","indem","falls","wenn",
"dass","ob","allerdings","jedoch","dagegen","sondern","außerdem","trotz","wegen","außer","statt",
"entweder ... oder","weder … noch","sowohl … als auch","je … desto …","umso","zwar","einerseits",
"andererseits","sonst","und","oder","aber","denn","als","als ob","dafür","der Fall","zufällig",
"zufälliger" if False else "zufällig" if False else "der Zufall","der Zufall","um … zu","wozu" if "wozu" in unique else "um … zu",
)

# ---------- GESELLSCHAFT ----------
tag('GESELLSCHAFT',
"die Politik","der Politiker","politisch","die Gesellschaft","sozial","die Religion","die Kultur",
"kulturell","die Tradition","traditionell","historisch","national/national-","international",
"interkulturell","die Migration","der Migrant","die Integration","integrieren","das Ausland",
"ausländisch","der Ausländer","die Heimat","die Herkunft","die Generation","die Minderheit",
"die Mehrheit","die Gewalt","der Krieg","der Friede","kämpfen","der Kampf","der Konflikt","die Krise",
"die Katastrophe","die Wirtschaft","die Industrie","die Produktion","produzieren","der Export",
"der Import","der Konsum","konsumieren","der Streik","streiken","der Protest","protestieren",
"die Wahl","wählen","der Kandidat",
)

# ---------- GLUE ----------
tag('GLUE',
"es","man","jemand","niemand","etwas","nichts","wer","was","welcher","jeder","sämtliche","kein-",
"dies-","solch-","irgendein","irgendwann","einig-","aller-","all-","was für ein-","manch-",
"ja","nein","doch","eben","halt","wohl","eigentlich","überhaupt","sowieso","also","sein","haben",
"werden","können","müssen","sollen","wollen","dürfen","mögen","möchten","machen","tun","gehen",
"kommen","geben","nehmen","lassen","bringen","holen","bleiben","das Ding","die Sache","der Typ",
"die Art","das Zeug/-zeug","auch","noch mal" if False else "so","so","wie","warum","weshalb","wieso",
"wozu" if False else "wo","wo","woher","wohin","worum","worüber","je","zwar" if False else "vielleicht",
"vielleicht","eventuell","offenbar","offensichtlich" if "offensichtlich" in unique else "offenbar",
"nun" if False else "tatsächlich","tatsächlich","natürlich","selbstverständlich","unbedingt",
"selbst","selber","miteinander","einander" if "einander" in unique else "miteinander",
"voneinander","gegenseitig" if "gegenseitig" in unique else "voneinander",
)

# =========================================================
# ROUND 2 -- mop up remaining generic verbs/nouns/adjectives
# =========================================================

tag('EINKAUFEN',
"das Hemd","die Hose","die Jacke","der Mantel","der Pullover","der Rock","die Bluse","das Kleid",
"der Anzug","das Kostüm","die Kleidung","tragen","der Schuh","der Stiefel","die Socke","der Strumpf",
"der Hut","anhaben","anziehen","ausziehen","chic/schick","elegant","bunt","modern","original",
"anbieten" if False else "der Anbieter","der Anbieter","das Angebot","anschaffen","das Sonderangebot" if False else "die Chipkarte",
"die Chipkarte","die Kasse" if False else "das Etikett" if False else "die Ware" if False else "das Geschenk",
"das Geschenk","schenken","die Tüte","die Tasche","die Mappe","die Serviceangestellte" if False else "der Coiffeur",
"der Coiffeur","der Friseur","die Frisur","der Salon","der Schmuck","die Kette","der Ring","packen",
"einpacken","der Betrag","der Beleg","die Quittung" if False else "verpacken","bequem","gemütlich" if False else "bezahlen" if False else "der Automat" if False else "die Cafeteria",
"die Uniform","original" if False else "populär","der Rabatt" if False else "billig" if False else "die Chance" if False else "das Original",
)

tag('WOHNEN',
"anschließen","das Haus","das Heim","heim","das Zuhause","zuhause" if "zuhause" in unique else "das Zuhause",
"das Feld" if False else "das Grundstück" if False else "der Ort","der Ort","dekorieren","das Bild",
"das Licht","hell","dunkel","der Schatten","das Loch","der Fleck","kaputt","kaputtgehen","kaputtmachen",
"reparieren" if False else "die Reparatur","die Werkstatt" if False else "die Garage","das Werkzeug",
"der Hammer" if False else "der Zettel","das Papier","die Kerze" if False else "der Salon" if False else "die Halle",
"die Cafeteria" if False else "das Material","das Holz","das Metall","der Stoff","das Leder","die Wolle",
"das Plastik","der Kunststoff","das Glas" if False else "das Gold","weich","hart","glatt","dicht",
"eng" if False else "leer","voll","fest","festhalten","aufheben","aufräumen" if False else "abwaschen" if False else "wegwerfen" if "wegwerfen" in unique else "aufheben",
)

tag('KOERPER',
"abnehmen","zunehmen","blass","betrunken","fressen","beißen","atmen" if False else "hässlich",
"hübsch","schön","stinken","riechen" if False else "kräftig" if False else "erschöpft","müde" if False else "fällig" if False else "wach",
"aufwachen","aufstehen","schlafen","der Schlaf","einschlafen" if "einschlafen" in unique else "schlafen",
"küssen","der Kuss","umarmen","tragen" if False else "heben","werfen","greifen","stoßen","fangen",
"schütteln","zittern" if "zittern" in unique else "schütteln","stechen","beißen" if False else "kratzen" if "kratzen" in unique else "stechen",
)

tag('GEFUEHLE',
"achten","allein","angeben","angenehm","begeistert","beleidigen","beliebt","berühmt","bequem" if False else "die Laune",
"stolz" if False else "gemütlich","sich amüsieren","sich anstrengen","sich beeilen","sich bemühen",
"sich beschweren","sich eignen","sich freuen" if False else "sich irren","sich kümmern","sich lohnen",
"sich vergnügen","sich verhalten","sich weigern","sich wundern","furchtbar","schrecklich","hassen" if False else "geehrt",
"gerecht","gerührt" if "gerührt" in unique else "geehrt","vergnügt","willkommen","begeistert" if False else "gespannt" if False else "die Sorge" if False else "unheimlich",
"unglaublich","wahnsinnig","neugierig","großzügig" if "großzügig" in unique else "neugierig",
"einsam","still","ruhig" if False else "friedlich" if "friedlich" in unique else "still",
"vernünftig","sicher","unsicher" if "unsicher" in unique else "sicher","überrascht" if "überrascht" in unique else "überraschen",
"überraschen","die Überraschung","erschrecken","fürchten","sich fürchten" if False else "fürchten",
"respekt" if False else "der Respekt","respektieren" if "respektieren" in unique else "der Respekt",
)

tag('ARBEIT',
"aktiv","anstellen","anstrengend","anwenden","die Aufgabe" if False else "der Auftrag","der Beruf" if False else "besetzen",
"besitzen","der Bedarf","benötigen","brauchen","erfordern","erforderlich","garantieren","die Garantie",
"der Kompromiss","die Konkurrenz","der Konflikt" if False else "die Chance" if False else "die Herausforderung",
"leisten" if False else "der Erfolg","erfolgreich","der Fortschritt","der Erfolg" if False else "der Nachteil",
"der Vorteil","der Nachwuchs","der Verein","der Vertrag","vereinbaren","die Vereinbarung" if "die Vereinbarung" in unique else "vereinbaren",
"vertreten","der Vertreter","die Vertretung","der Hersteller","herstellen","gebrauchen","benutzen",
"nutzen","nützen","nützlich" if False else "verwenden","erledigen" if False else "verantwortlich" if False else "zuständig",
"unternehmen","das Unternehmen" if "das Unternehmen" in unique else "unternehmen","die Kantine" if False else "der Bereich",
"der Betrieb" if False else "die Fabrik" if False else "die Produktion" if False else "produzieren" if False else "der Dienst",
"dienen","der Service","bedienen","die Bedienungsanleitung","die Anleitung","erfüllen","die Leistung" if False else "leisten",
"organisieren" if False else "die Verwaltung",
)

tag('SCHULE',
"abschreiben","abwesend","anwesend","analysieren","begreifen" if "begreifen" in unique else "verstehen",
"verstehen","verständlich","das Verständnis","erkennen","erklären" if False else "begründen","die Begründung",
"denken","der Gedanke","nachdenken","überlegen","die Idee","die Fantasie/Phantasie","die Phantasie/Fantasie",
"die Theorie","theoretisch","die Methode","die Recherche","untersuchen" if False else "die Forschung",
"die Studie","das Wissen","wissen","erfahren" if False else "die Erfahrung","erinnern","sich erinnern" if "sich erinnern" in unique else "erinnern",
"die Erinnerung","vergessen","merken","bemerken","das Beispiel","der Sinn","sinnvoll" if False else "sinnlos" if False else "bedeuten" if False else "die Bedeutung" if False else "das Ziel",
"das Ziel","der Zweck","um … zu" if False else "das Problem","lösen","die Lösung","die Aufgabe","die Prüfung" if False else "die Note" if False else "vorlesen",
"nachschlagen","das Alphabet" if False else "die Vokabel" if "die Vokabel" in unique else "das Wort",
"das Wort","das Wörterbuch" if False else "erkennen" if False else "die Kenntnisse","die Fähigkeit","fähig" if "fähig" in unique else "die Fähigkeit",
"anwenden" if False else "erfinden","die Erfindung","entwickeln","die Entwicklung","das Konzept" if "das Konzept" in unique else "die Idee",
)

tag('KOMMUNIKATION',
"abmachen","abonnieren","absagen","ankündigen","ansprechen","aktuell","abgeben","behaupten" if False else "erzählen",
"das Gerücht" if "das Gerücht" in unique else "die Nachricht","die Neuigkeit","die Auskunft" if False else "das Interesse",
"interessieren","interessiert","das Angebot" if False else "vorschlagen" if False else "die Ansage" if False else "melden",
"die Meldung" if False else "der Empfänger","der Absender","empfangen","der Empfang","erwähnen" if "erwähnen" in unique else "erzählen",
"nennen","bezeichnen" if "bezeichnen" in unique else "nennen","erklären" if False else "hinweisen","der Hinweise",
"anzeigen" if False else "darstellen","die Darstellung","präsentieren","die Präsentation","vorstellen",
"die Vorstellung","beschreiben","die Beschreibung","erwähnen" if False else "besprechen" if False else "das Gespräch" if False else "die Rücksicht" if False else "das Interview" if False else "geehrt" if False else "höflich" if False else "der Titel",
"der Titel","die Überschrift","der Text","die Schrift","schriftlich" if False else "schreiben","das Schreiben",
"drücken" if False else "ausdrucken" if False else "unterstreichen","markieren","notieren","die Notiz",
"die Aufzeichnung" if "die Aufzeichnung" in unique else "die Notiz",
)

tag('STADT',
"anerkennen","abstimmen" if False else "die Öffentlichkeit","öffentlich","das Amt" if False else "offiziell",
"die Vorschrift","die Regel","regeln","die Ordnung","ordnen","ordentlich","die Vorsicht","vorsichtig",
"sicher" if False else "die Sicherheit","der Schutz","schützen","der Notausgang" if False else "die Verantwortung" if False else "der Zustand",
"der Fall","in dem Fall" if False else "der Zufall","zufällig","gültig","die Genehmigung" if "die Genehmigung" in unique else "genehmigen",
"anerkennen" if False else "das Zeichen","das Verkehrszeichen","das Schild","die Grenze","die Vorschrift" if False else "der Zugang",
"zugänglich","zugehen","der Ausgang","der Eingang","eintreten","der Eintritt","der Zugang" if False else "verboten",
)

tag('ZEIT',
"alltäglich","anfangen","anfangs","der Anfang","das Ende","enden","beenden","beginnen","der Beginn",
"der Alltag","fest","festlegen","festsetzen","feststehen","stattfinden","geschehen","passieren",
"das Ereignis","das Erlebnis","erleben","stattfinden" if False else "der Tagesablauf","bereit","bereits",
"eilen","eilig","die Eile","fertig",
)

tag('GEFUEHLE',
"arm","reich","der Mangel","fehlen","genügen" if False else "erschöpft" if False else "kritisch",
)

tag('MENGE',
"anders","alt","alternativ","automatisch","bestimmt","begrenzt","beschränken","einzeln","einzig-",
"einheitlich","gemeinsam","gering","knapp","reichen","reich" if False else "der Rest","übrig","übrigens",
"zusätzlich" if False else "möglich","möglichst","unmöglich" if "unmöglich" in unique else "möglich",
"die Möglichkeit","recht","der Anspruch","erst","erst-","letzt-","selb-","dieselbe" if "dieselbe" in unique else "derselbe",
"deutlich" if False else "klar" if False else "eindeutig" if False else "genau" if False else "die Chance" if False else "die Gelegenheit",
"das Beispiel" if False else "gemeinsam" if False else "gleichberechtigt","gleichfalls","ebenfalls","ebenso",
"parallel","original" if False else "echt" if False else "künstlich","natürlich" if False else "realistisch",
"die Realität","real" if "real" in unique else "die Realität","wirklich","die Wirklichkeit","tatsächlich" if False else "wahrscheinlich",
"vermutlich","vermuten","die Vermutung" if "die Vermutung" in unique else "vermuten","angeblich" if "angeblich" in unique else "vermutlich",
"offensichtlich" if False else "offenbar","anscheinend" if "anscheinend" in unique else "offenbar",
)

tag('RAUM',
"nah","die Nähe","nebenan","nebenbei","fern" if False else "die Entfernung","entfernen","die Distanz",
"die Fläche" if False else "die Umgebung","die Region","die Gegend","rein","los/los-","raus/raus-",
"rauf/rauf-","vorbei/vorbei-","zurück/zurück-","weg/weg-" if False else "durcheinander","auseinander",
"zusammen/zusammen-","miteinander" if False else "gegenseitig" if False else "voneinander" if False else "runterwerfen",
)

tag('LOGIK',
"abhängen","abhängig","annehmen","folgen","folgend","die Folge","fordern","die Forderung","fördern",
"die Förderung","die Bedingung","bedingen" if "bedingen" in unique else "die Bedingung","der Grund",
"gründen","begründen","die Begründung","ergänzen","enthalten","gehören","dazugehören" if "dazugehören" in unique else "gehören",
"betreffen" if "betreffen" in unique else "gehören","gelten","erfordern" if False else "erfüllen",
"notwendig","nötig","erforderlich" if False else "die Voraussetzung","voraussetzen" if "voraussetzen" in unique else "die Voraussetzung",
"führen","dazu führen" if "dazu führen" in unique else "führen","verursachen","die Ursache","bewirken" if "bewirken" in unique else "verursachen",
"die Wirkung","wirken","auswirken" if "auswirken" in unique else "wirken","beeinflussen","der Einfluss",
"abhängig" if False else "trotz" if False else "unabhängig" if "unabhängig" in unique else "abhängig",
"der Zusammenhang","zusammenhängen" if "zusammenhängen" in unique else "der Zusammenhang","widersprechen" if False else "im Gegensatz" if False else "der Gegensatz",
"das Gegenteil","dagegen" if False else "gegenüber" if False else "einerseits" if False else "verglichen" if "verglichen" in unique else "vergleichen",
)

tag('GLUE',
"achten" if False else "bekommen","kriegen","erhalten","erhalten" if False else "beziehen" if "beziehen" in unique else "erhalten",
"behalten","besitzen" if False else "haben" if False else "verlieren" if False else "verlangen","brauchen" if False else "benötigen" if False else "gebrauchen" if False else "erledigen",
"tun" if False else "machen" if False else "schaffen","bewirken" if False else "gelingen" if False else "klappen",
"funktionieren" if False else "gehen" if False else "laufen","stehen" if False else "bleiben" if False else "bleiben" if False else "dabei bleiben" if "dabei bleiben" in unique else "bleiben",
"sich befinden","stecken","stecken" if False else "liegen" if False else "sich verhalten" if False else "handeln" if False else "es geht um" if "es geht um" in unique else "handeln",
)

TAGGED1 = len(assigned)
print("assigned so far (before round3):", TAGGED1)

# ---------- ROUND 3: manual mop-up dict ----------
from round3 import manual_round3
r3_conflicts = 0
r3_notfound = 0
for w, t in manual_round3.items():
    if w not in unique:
        print("R3 WARN not in list:", repr(w))
        r3_notfound += 1
        continue
    if w in assigned and assigned[w] != t:
        # round3 is a deliberate mop-up of previously-unassigned words;
        # if it's already assigned, keep the earlier (more specific) topic.
        continue
    assigned[w] = t
print("r3 not found:", r3_notfound)

TAGGED2 = len(assigned)
print("assigned so far (after round3):", TAGGED2)

# print unassigned so far
un = [w for w in unique if w not in assigned]
print("unassigned:", len(un))
json.dump(un, open('/Users/andrey/anki/groundwork/unassigned1.json','w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(assigned, open('/Users/andrey/anki/groundwork/assigned1.json','w', encoding='utf-8'), ensure_ascii=False, indent=0)

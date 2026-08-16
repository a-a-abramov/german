# Batch 4 — Tiere · Chunks

Harvested with `tools/wortprofil_db.py <alle 8 Wörter> --min-freq 20 --min-dice 4 --top 15`.

### Tierpark — nothing usable, written by hand

*(deliberately a `###`: `tools/site.py` reads only `##` headings as chunk words, and a
heading with no five-column table under it is dropped. `Tierpark` has no Wortprofil to
link to, so it does not belong on the chunks page.)*

`Tierpark` came back empty at the standard floors, and the ladder did not rescue it:

| step | result |
|---|---|
| `--min-freq 20 --min-dice 4` | no rows |
| `--min-freq 10 --min-dice 4` | no rows |
| `--all --min-freq 5 --top 25` | 2 rows: `Tierpark und Zoo` (freq 5), `in den Tierpark wollen` (freq 5, logDice 3.1) |
| `tools/leipzig.py Tierpark` | `Pflegerin` (4), `Zoo` (6), `geschlossen` (4), `Hamburger` (4) — nothing to build on |

Expected: it is a compound, and OpenSubtitles is film dialogue, where people say *Zoo*.
The chunks used in Scene 4 are therefore taken from the Goethe list's own example sentence
— **in den Tierpark gehen** (Akk.) — plus **im Tierpark** (Dat.) and **der Tierpark ist
samstags voll**. The one corpus row that is worth anything, `in den Tierpark wollen`, is on
the page: *"… wollen in den Tierpark"*.

`Haustier` and `Bauernhof` are also compounds and also came back thin (3 and 6 rows), but
what they returned is exactly what the scenes needed: `als Haustier halten`, `auf dem
Bauernhof arbeiten / leben / wohnen`, `vom Bauernhof kommen`.

---

## Tier

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### hat Adjektivattribut

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| ein(e) wilde(r) Tier | wild |  | 11.4 | 2359 | ✓ |
| ein(e) hoche(r) Tier | hoch |  | 9.7 | 1478 | ✓ |
| ein(e) tote(r) Tier | tot |  | 8.8 | 562 | ✓ |
| ein(e) arme(r) Tier | arm |  | 8.1 | 378 | ✓ |
| ein(e) kranke(r) Tier | krank |  | 7.9 | 169 | ✓ |
| ein(e) gefährliche(r) Tier | gefährlich |  | 7.8 | 173 | ✓ |
| ein(e) überfahrene(r) Tier | überfahren |  | 7.6 | 90 | ✓ |
| ein(e) seltene(r) Tier | selten |  | 7.2 | 91 | ✓ |
| ein(e) dumme(r) Tier | dumm |  | 6.7 | 107 | ✓ |
| ein(e) große(r) Tier | groß |  | 6.2 | 707 | ✓ |
| ein(e) erwachsene(r) Tier | erwachsen |  | 6.1 | 40 | ✓ |
| ein(e) einzelne(r) Tier | einzeln |  | 6.0 | 47 | ✓ |
| ein(e) intelligente(r) Tier | intelligent |  | 5.9 | 33 | ✓ |
| ein(e) verschiedene(r) Tier | verschieden |  | 5.9 | 75 | ✓ |
| ein(e) seltsame(r) Tier | seltsam |  | 5.8 | 53 | ✓ |

### ist in Koordination mit

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier und Pflanze | Pflanze |  | 11.3 | 430 | ✓ |
| Tier und Mensch | Mensch |  | 10.3 | 754 | ✓ |
| Tier und Vogel | Vogel |  | 9.0 | 91 | ✓ |
| Tier und Natur | Natur |  | 8.2 | 45 | ✓ |
| Tier und Baum | Baum |  | 8.1 | 54 | ✓ |
| Tier und Blume | Blume |  | 6.9 | 26 | ✓ |
| Tier und Kind | Kind |  | 6.7 | 115 | ✓ |
| Tier und Fisch | Fisch |  | 6.7 | 22 | ✓ |
| Tier und Hund | Hund |  | 6.7 | 29 | ✓ |
| Tier und Leute | Leute |  | 5.4 | 29 | ✓ |
| Tier und Mann | Mann |  | 4.6 | 42 | ✓ |
| Tier und Frau | Frau |  | 4.2 | 32 | ✓ |

### hat Genitivattribut

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier des/der Wald | Wald |  | 9.3 | 38 | ✓ |
| Tier des/der Erde | Erde |  | 8.1 | 48 | ✓ |
| Tier des/der Art | Art |  | 7.2 | 21 | ✓ |
| Tier des/der Welt | Welt |  | 6.3 | 107 | ✓ |

### hat Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier + in Zoo | in Zoo | Dat. | 8.6 | 57 | ✓ |
| Tier + in Wald | in Wald | Dat. | 5.7 | 38 | ✓ |
| Tier + auf Welt | auf Welt | Dat. | 4.7 | 21 | ✓ |

### ist Passivsubjekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier wird behandeln | behandeln |  | 8.5 | 31 | ✓ |
| Tier wird verletzen | verletzen |  | 7.6 | 25 | ✓ |

### ist Prädikativ zu

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Pferd ist/wird Tier | Pferd |  | 8.3 | 26 | ✓ |
| Mensch ist/wird Tier | Mensch |  | 8.2 | 101 | ✓ |
| Typ ist/wird Tier | Typ |  | 6.2 | 24 | ✓ |
| Vater ist/wird Tier | Vater |  | 5.9 | 43 | ✓ |
| Mann ist/wird Tier | Mann |  | 5.6 | 44 | ✓ |

### ist Genitivattribut von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Sprache des/der Tier | Sprache |  | 8.3 | 31 | ✓ |
| Verhalten des/der Tier | Verhalten |  | 7.9 | 25 | ✓ |
| König des/der Tier | König |  | 7.5 | 42 | ✓ |
| Zahl des/der Tier | Zahl |  | 7.2 | 20 | ✓ |
| Schutz des/der Tier | Schutz |  | 7.1 | 23 | ✓ |
| Blut des/der Tier | Blut |  | 6.9 | 25 | ✓ |
| Welt des/der Tier | Welt |  | 6.6 | 20 | ✓ |
| Leben des/der Tier | Leben |  | 6.2 | 40 | ✓ |
| Freund des/der Tier | Freund |  | 6.0 | 27 | ✓ |
| Tod des/der Tier | Tod |  | 4.8 | 25 | ✓ |

### ist Akkusativ-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier(Akk.) füttern | füttern |  | 8.2 | 142 | ✓ |
| Tier(Akk.) behandeln | behandeln |  | 7.7 | 152 | ✓ |
| Tier(Akk.) lieben | lieben |  | 6.9 | 313 | ✓ |
| Tier(Akk.) fangen | fangen |  | 6.8 | 79 | ✓ |
| Tier(Akk.) mögen | mögen |  | 6.8 | 237 | ✓ |
| Tier(Akk.) beobachten | beobachten |  | 6.7 | 74 | ✓ |
| Tier(Akk.) essen | essen |  | 6.5 | 126 | ✓ |
| Tier(Akk.) schützen | schützen |  | 6.4 | 72 | ✓ |
| Tier(Akk.) fotografieren | fotografieren |  | 6.4 | 35 | ✓ |
| Tier(Akk.) fressen | fressen |  | 6.3 | 40 | ✓ |
| Tier(Akk.) treiben | treiben |  | 6.2 | 50 | ✓ |
| Tier(Akk.) retten | retten |  | 6.2 | 174 | ✓ |
| Tier(Akk.) schießen | schießen |  | 5.8 | 31 | ✓ |
| Tier(Akk.) beruhigen | beruhigen |  | 5.7 | 25 | ✓ |
| Tier(Akk.) mitnehmen | mitnehmen |  | 5.6 | 40 | ✓ |

### ist Subjekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier fressen(t) | fressen |  | 8.2 | 93 | ✓ |
| Tier leben(t) | leben |  | 7.3 | 244 | ✓ |
| Tier leiden(t) | leiden |  | 7.2 | 73 | ✓ |
| Tier spüren(t) | spüren |  | 7.0 | 43 | ✓ |
| Tier verhalten(t) | verhalten |  | 6.3 | 26 | ✓ |
| Tier sterben(t) | sterben |  | 6.3 | 199 | ✓ |
| Tier bewegen(t) | bewegen |  | 6.2 | 38 | ✓ |
| Tier nutzen(t) | nutzen |  | 6.1 | 31 | ✓ |
| Tier greifen(t) | greifen |  | 6.1 | 32 | ✓ |
| Tier essen(t) | essen |  | 6.0 | 28 | ✓ |
| Tier fühlen(t) | fühlen |  | 6.0 | 46 | ✓ |
| Tier fliehen(t) | fliehen |  | 6.0 | 23 | ✓ |
| Tier fürchten(t) | fürchten |  | 6.0 | 21 | ✓ |
| Tier müssen(t) | müssen |  | 5.8 | 38 | ✓ |
| Tier brauchen(t) | brauchen |  | 5.8 | 119 | ✓ |

### ist in Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| von unterscheiden … Tier | von unterscheiden | Dat. | 8.1 | 96 | ✓ |
| mit umgehen … Tier | mit umgehen | Dat. | 7.5 | 104 | ✓ |
| für Herz … Tier | für Herz | Akk. | 7.3 | 50 | ✓ |
| um kümmern … Tier | um kümmern | Akk. | 7.3 | 234 | ✓ |
| von stammen … Tier | von stammen | Dat. | 7.0 | 74 | ✓ |
| zu werden … Tier | zu werden | Dat. | 6.8 | 162 | ✓ |
| mit arbeiten … Tier | mit arbeiten | Dat. | 6.8 | 95 | ✓ |
| mit kennen … Tier | mit kennen | Dat. | 6.6 | 47 | ✓ |
| zu Liebe … Tier | zu Liebe | Dat. | 6.6 | 37 | ✓ |
| auf schießen … Tier | auf schießen | Akk. | 6.5 | 44 | ✓ |
| mit leben … Tier | mit leben | Dat. | 6.4 | 50 | ✓ |
| mit können … Tier | mit können | Dat. | 6.4 | 36 | ✓ |
| an testen … Tier | an testen | Dat. | 6.3 | 24 | ✓ |
| mit Arbeit … Tier | mit Arbeit | Dat. | 6.2 | 25 | ✓ |
| für sein … Tier | für sein | Akk. | 6.0 | 332 | ✓ |

### hat Prädikativ

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier ist/wird krank | krank |  | 7.5 | 67 | ✓ |
| Tier ist/wird gesund | gesund |  | 7.4 | 28 | ✓ |
| Tier ist/wird gefährlich | gefährlich |  | 7.1 | 37 | ✓ |
| Tier ist/wird Mensch | Mensch |  | 6.5 | 21 | ✓ |
| Tier ist/wird sicher | sicher |  | 5.7 | 22 | ✓ |
| Tier ist/wird groß | groß |  | 5.4 | 36 | ✓ |
| Tier ist/wird alt | alt |  | 5.4 | 20 | ✓ |
| Tier ist/wird wichtig | wichtig |  | 5.3 | 40 | ✓ |
| Tier ist/wird tot | tot |  | 5.2 | 46 | ✓ |

### ist Dativ-/Genitiv-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Tier(Dat./Gen.) helfen | helfen |  | 7.2 | 125 | ✓ |
| Tier(Dat./Gen.) begegnen | begegnen |  | 7.1 | 22 | ✓ |
| Tier(Dat./Gen.) schaden | schaden |  | 7.0 | 22 | ✓ |
| Tier(Dat./Gen.) tun | tun |  | 6.9 | 32 | ✓ |
| Tier(Dat./Gen.) geben | geben |  | 6.6 | 106 | ✓ |
| Tier(Dat./Gen.) gehen | gehen |  | 6.2 | 61 | ✓ |
| Tier(Dat./Gen.) kommen | kommen |  | 6.0 | 20 | ✓ |
| Tier(Dat./Gen.) sein | sein |  | 4.3 | 24 | ✓ |


## Bauer

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### ist in Koordination mit

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Bauer und Arbeiter | Arbeiter |  | 10.5 | 99 | ✓ |
| Bauer und Händler | Händler |  | 8.7 | 23 | ✓ |
| Bauer und Handwerker | Handwerker |  | 8.6 | 20 | ✓ |
| Bauer und König | König |  | 7.6 | 33 | ✓ |

### hat Adjektivattribut

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| ein(e) einfache(r) Bauer | einfach |  | 7.2 | 92 | ✓ |
| ein(e) arme(r) Bauer | arm |  | 6.9 | 109 | ✓ |
| ein(e) reiche(r) Bauer | reich |  | 6.5 | 40 | ✓ |
| ein(e) dumme(r) Bauer | dumm |  | 5.0 | 20 | ✓ |

### ist Prädikativ zu

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Eltern ist/wird Bauer | Eltern |  | 7.1 | 25 | ✓ |
| Vater ist/wird Bauer | Vater |  | 5.7 | 35 | ✓ |
| Name ist/wird Bauer | Name |  | 5.2 | 36 | ✓ |

### ist Genitivattribut von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Sohn des/der Bauer | Sohn |  | 6.6 | 40 | ✓ |
| Tochter des/der Bauer | Tochter |  | 6.3 | 26 | ✓ |
| Frau des/der Bauer | Frau |  | 5.4 | 22 | ✓ |
| Leben des/der Bauer | Leben |  | 5.3 | 20 | ✓ |

### hat Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Bauer + in Spiel | in Spiel | Dat. | 6.2 | 20 | ✓ |

### ist Subjekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Bauer verkaufen(t) | verkaufen |  | 5.8 | 28 | ✓ |
| Bauer kennen(t) | kennen |  | 5.1 | 35 | ✓ |
| Bauer bekommen(t) | bekommen |  | 4.9 | 42 | ✓ |
| Bauer leben(t) | leben |  | 4.8 | 41 | ✓ |
| Bauer suchen(t) | suchen |  | 4.8 | 26 | ✓ |
| Bauer arbeiten(t) | arbeiten |  | 4.6 | 33 | ✓ |
| Bauer fahren(t) | fahren |  | 4.6 | 32 | ✓ |
| Bauer finden(t) | finden |  | 4.6 | 63 | ✓ |
| Bauer bringen(t) | bringen |  | 4.4 | 44 | ✓ |
| Bauer brauchen(t) | brauchen |  | 4.2 | 36 | ✓ |
| Bauer glauben(t) | glauben |  | 4.2 | 22 | ✓ |
| Bauer sprechen(t) | sprechen |  | 4.1 | 27 | ✓ |
| Bauer haben(t) | haben |  | 4.0 | 312 | ✓ |

### ist Dativ-/Genitiv-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Bauer(Dat./Gen.) gehören | gehören |  | 5.2 | 23 | ✓ |
| Bauer(Dat./Gen.) helfen | helfen |  | 5.2 | 30 | ✓ |
| Bauer(Dat./Gen.) geben | geben |  | 4.6 | 27 | ✓ |

### ist Akkusativ-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Bauer(Akk.) schlagen | schlagen |  | 5.1 | 30 | ✓ |
| Bauer(Akk.) heiraten | heiraten |  | 4.9 | 20 | ✓ |
| Bauer(Akk.) sprechen | sprechen |  | 4.2 | 22 | ✓ |

### ist in Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| mit sprechen … Bauer | mit sprechen | Dat. | 4.3 | 37 | ✓ |
| mit reden … Bauer | mit reden | Dat. | 4.1 | 28 | ✓ |


## Haustier

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### ist in Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| als halten … Haustier | als halten | Nom. | 9.5 | 54 | ✓ |
| als haben … Haustier | als haben | Nom. | 5.9 | 23 | ✓ |
| zu machen … Haustier | zu machen | Dat. | 4.7 | 37 | ✓ |

### ist Genitivattribut von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Name des/der Haustier | Name |  | 5.5 | 40 | ✓ |


## Bauernhof

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### ist in Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| auf leben … Bauernhof | auf leben | Dat. | 8.2 | 61 | ✓ |
| auf wohnen … Bauernhof | auf wohnen | Dat. | 8.1 | 24 | ✓ |
| auf arbeiten … Bauernhof | auf arbeiten | Dat. | 7.1 | 24 | ✓ |
| auf machen … Bauernhof | auf machen | Dat. | 4.9 | 21 | ✓ |
| von kommen … Bauernhof | von kommen | Dat. | 4.9 | 28 | ✓ |
| auf sein … Bauernhof | auf sein | Dat. | 4.2 | 112 | ✓ |


## Schlange

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### ist Akkusativ-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange(Akk.) stehen | stehen |  | 10.6 | 598 | ✓ |
| Schlange(Akk.) fangen | fangen |  | 5.9 | 27 | ✓ |
| Schlange(Akk.) hassen | hassen |  | 4.8 | 21 | ✓ |
| Schlange(Akk.) sehen | sehen |  | 4.2 | 205 | ✓ |

### hat Adjektivattribut

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| ein(e) giftige(r) Schlange | giftig |  | 9.8 | 124 | ✓ |
| ein(e) lange(r) Schlange | lang |  | 7.1 | 248 | ✓ |
| ein(e) böse(r) Schlange | bös |  | 6.9 | 26 | ✓ |
| ein(e) falsche(r) Schlange | falsch |  | 6.9 | 197 | ✓ |
| ein(e) tödliche(r) Schlange | tödlich |  | 6.5 | 25 | ✓ |
| ein(e) weiße(r) Schlange | weiß |  | 6.4 | 101 | ✓ |
| ein(e) riesige(r) Schlange | riesig |  | 6.1 | 47 | ✓ |
| ein(e) grüne(r) Schlange | grün |  | 6.0 | 31 | ✓ |
| ein(e) tote(r) Schlange | tot |  | 5.5 | 38 | ✓ |
| ein(e) bösee(r) Schlange | böse |  | 5.5 | 30 | ✓ |
| ein(e) schwarze(r) Schlange | schwarz |  | 4.7 | 32 | ✓ |

### ist Genitivattribut von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Gift des/der Schlange | Gift |  | 9.7 | 30 | ✓ |
| Kopf des/der Schlange | Kopf |  | 8.1 | 53 | ✓ |
| Anfang des/der Schlange | Anfang |  | 7.2 | 24 | ✓ |
| Ende des/der Schlange | Ende |  | 6.5 | 96 | ✓ |
| Tochter des/der Schlange | Tochter |  | 6.0 | 21 | ✓ |

### hat Prädikativ

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange ist/wird lang | lang |  | 9.5 | 193 | ✓ |
| Schlange ist/wird kurz | kurz |  | 7.7 | 28 | ✓ |

### ist Dativ-/Genitiv-Objekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange(Dat./Gen.) stehen | stehen |  | 8.9 | 111 | ✓ |

### hat Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange + in Gras | in Gras | Dat. | 8.8 | 37 | ✓ |
| Schlange + in Garten | in Garten | Dat. | 5.8 | 22 | ✓ |

### ist Subjekt von

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange beißen(t) | beißen |  | 8.7 | 50 | ✓ |
| Schlange stehen(t) | stehen |  | 6.4 | 382 | ✓ |
| Schlange bewegen(t) | bewegen |  | 6.1 | 24 | ✓ |
| Schlange fangen(t) | fangen |  | 5.5 | 21 | ✓ |

### ist in Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| in warten … Schlange | in warten | Dat. | 8.1 | 115 | ✓ |
| in stehen … Schlange | in stehen | Dat. | 7.3 | 318 | ✓ |
| vor Angst … Schlange | vor Angst | Dat. | 7.2 | 99 | ✓ |
| bei stehen … Schlange | bei stehen | Dat. | 7.2 | 29 | ✓ |
| in Platz … Schlange | in Platz | Dat. | 7.0 | 32 | ✓ |
| in stellen … Schlange | in stellen | Akk. | 6.9 | 53 | ✓ |

### ist in Koordination mit

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange und Vogel | Vogel |  | 7.7 | 22 | ✓ |

### hat Genitivattribut

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Schlange des/der Welt | Welt |  | 4.7 | 36 | ✓ |


## fressen

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### hat Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| fressen + aus Hand | aus Hand | Dat. | 10.5 | 231 | ✓ |
| fressen + von Kopf | von Kopf | Dat. | 8.8 | 42 | ✓ |
| fressen + mit Haut | mit Haut | Dat. | 8.7 | 28 | ✓ |
| fressen + zu Frühstück | zu Frühstück | Dat. | 7.2 | 25 | ✓ |

### hat Akkusativ-Objekt

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| fressen + Gras(Akk.) | Gras |  | 8.5 | 94 | ✓ |
| fressen + Fleisch(Akk.) | Fleisch |  | 8.3 | 109 | ✓ |
| fressen + Staub(Akk.) | Staub |  | 8.1 | 55 | ✓ |
| fressen + Dreck(Akk.) | Dreck |  | 7.7 | 61 | ✓ |
| fressen + Fisch(Akk.) | Fisch |  | 7.4 | 69 | ✓ |
| fressen + Pflanze(Akk.) | Pflanze |  | 7.0 | 29 | ✓ |
| fressen + Blatt(Akk.) | Blatt |  | 6.9 | 27 | ✓ |
| fressen + Frucht(Akk.) | Frucht |  | 6.8 | 24 | ✓ |
| fressen + Müll(Akk.) | Müll |  | 6.6 | 29 | ✓ |
| fressen + Vogel(Akk.) | Vogel |  | 6.5 | 28 | ✓ |
| fressen + Tier(Akk.) | Tier |  | 6.3 | 40 | ✓ |
| fressen + Mensch(Akk.) | Mensch |  | 6.2 | 128 | ✓ |
| fressen + Knochen(Akk.) | Knochen |  | 6.1 | 21 | ✓ |
| fressen + Hund(Akk.) | Hund |  | 5.9 | 40 | ✓ |
| fressen + Junge(Akk.) | Junge |  | 5.8 | 40 | ✓ |

### hat Subjekt

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| Fisch fressen(t) | Fisch |  | 8.2 | 60 | ✓ |
| Tier fressen(t) | Tier |  | 8.2 | 93 | ✓ |
| Vogel fressen(t) | Vogel |  | 7.6 | 51 | ✓ |
| Hund fressen(t) | Hund |  | 7.4 | 83 | ✓ |
| Schwein fressen(t) | Schwein |  | 7.4 | 35 | ✓ |
| Katze fressen(t) | Katze |  | 7.3 | 35 | ✓ |
| Pferd fressen(t) | Pferd |  | 6.3 | 21 | ✓ |

### ist in Koordination mit

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| fressen und trinken | trinken |  | 6.4 | 42 | ✓ |
| fressen und schlafen | schlafen |  | 6.2 | 20 | ✓ |


## füttern

*Filter: Freq ≥ 20, logDice ≥ 4.0, B1 lemmas only · source: OpenSubtitles de v2024*

### hat Akkusativ-Objekt

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| füttern + Katze(Akk.) | Katze |  | 9.4 | 233 | ✓ |
| füttern + Fisch(Akk.) | Fisch |  | 8.8 | 173 | ✓ |
| füttern + Vogel(Akk.) | Vogel |  | 8.6 | 111 | ✓ |
| füttern + Hund(Akk.) | Hund |  | 8.3 | 208 | ✓ |
| füttern + Tier(Akk.) | Tier |  | 8.2 | 142 | ✓ |
| füttern + Schwein(Akk.) | Schwein |  | 7.9 | 72 | ✓ |
| füttern + Pferd(Akk.) | Pferd |  | 7.5 | 94 | ✓ |
| füttern + Baby(Akk.) | Baby |  | 6.8 | 107 | ✓ |
| füttern + Computer(Akk.) | Computer |  | 6.3 | 23 | ✓ |
| füttern + Junge(Akk.) | Junge |  | 5.2 | 25 | ✓ |
| füttern + Kind(Akk.) | Kind |  | 4.9 | 102 | ✓ |

### hat Präpositionalgruppe

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| füttern + mit Information | mit Information | Dat. | 9.4 | 74 | ✓ |
| füttern + mit Löffel | mit Löffel | Dat. | 8.3 | 24 | ✓ |
| füttern + mit Lüge | mit Lüge | Dat. | 7.8 | 23 | ✓ |

### ist in Koordination mit

| chunk | collocate | Kasus | logDice | Freq | B1 |
|---|---|:-:|---:|---:|:-:|
| füttern und baden | baden |  | 8.9 | 34 | ✓ |
| füttern und waschen | waschen |  | 8.4 | 41 | ✓ |
| füttern und pflegen | pflegen |  | 8.2 | 24 | ✓ |
| füttern und wechseln | wechseln |  | 7.7 | 22 | ✓ |
| füttern und kümmern | kümmern |  | 6.7 | 24 | ✓ |
| füttern und halten | halten |  | 4.9 | 28 | ✓ |
| füttern und bringen | bringen |  | 4.7 | 31 | ✓ |


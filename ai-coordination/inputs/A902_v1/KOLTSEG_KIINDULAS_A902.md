# A-902 – költségelosztási kiindulás (stílusfüggetlen, v1 · 2026-10-24)

**Státusz: KERETRE ELŐSZŰRT KIINDULÁS – minden szám becslés** (a korábbi koncepció-doksi ársávjai és IKEA/Kave Home árszintek alapján). Ez **nem** terméklista és nem költségvetés; arra szolgál, hogy minden stílus ugyanabból a pénzből induljon, és látsszon, mit honnan vesz el. A konkrét termékárakat Astra kutatja, utána Claude **független forrásból** újraellenőrzi (vizsgálati tábla). Gépi forma: `KOLTSEG_KIINDULAS_A902.csv`.

## Keret-logika
- **20,00 M Ft bruttó, mindennel** (tervezés, asztalos, bútor, konyha + gépek, világítás, textil, terasz, szállítás, szerelés).
- **Tartalék: 2,00 M** (a keret 10%-a – szigorúbb, mint a költés 10%-a) → **tervezhető: 18,00 M**.
- Egy stílus átcsoportosíthat sorok között, **de az összeg nem nőhet**: minden többlethez meg kell mondani, melyik sor csökken.

## Összesítés csoportonként
| Csoport | M Ft | a keret %-a |
|---|---|---|
| Konyha | 2.90 | 14% |
| Nappali + étkező | 3.60 | 18% |
| Master | 2.00 | 10% |
| 05.2 háló | 0.80 | 4% |
| 05.3 | 0.80 | 4% |
| Fürdők + WC | 0.50 | 2% |
| Előtér | 0.50 | 2% |
| Mosó-szárító | 0.45 | 2% |
| Világítás | 1.00 | 5% |
| Falfelületek | 0.50 | 2% |
| Textil, dekor | 0.50 | 2% |
| Terasz | 3.60 | 18% |
| Tervezés | 0.40 | 2% |
| Szállítás, szerelés | 0.45 | 2% |
| **Tervezhető összesen** | **18.00** | 90% |
| Tartalék | 2.00 | 10% |
| **Keret** | **20.00** | 100% |

**Hős-keret** (a „drágának ható" hatás fő hordozói: nappali fal-gesztus, kanapé, master ágyfal, világítás, jakuzzi): **5.35 M** = a tervezhető 30%-a. A csendes helyiségek (05.2, 05.3, fürdők) szándékosan karcsúak.

## Tételes sorok
| Sor | Tétel | Cél M Ft | Sáv | Megjegyzés |
|---|---|---|---|---|
| 01 | Tervezés, felmérés, látványterv-segítség | 0.40 | 0.10–0.80 | külső tervező/IKEA-tervezés díja innen; 0,8 M felett máshonnan kell elvenni |
| 02a | Konyha – korpusz, front, munkalap (IKEA-váz + egyedi/jobb front) | 1.50 | 1.20–2.00 | konyhabútor NINCS a lakásban; L-alak + magasszekrény-sor |
| 02b | Konyha – beépíthető gépek (sütő, főzőlap, páraelszívó, hűtő, mosogatógép, mikró) | 1.10 | 0.90–1.50 | gépek EU-webshopból is jöhetnek |
| 02c | Konyha – mosogató, csaptelep, szerelés, bekötés | 0.30 | 0.20–0.40 | kiállások helye ellenőrizendő |
| 03a | Nappali – fő fal-gesztus (TV-/médiafal, asztalos forma-darab) | 1.10 | 0.70–1.50 | hős-darab; 2–3 asztalos ajánlat kell |
| 03b | Nappali – kanapé (moduláris/íves) | 1.00 | 0.70–1.40 | hős-darab; Kave Home vagy egyenértékű |
| 03c | Nappali – fotel, dohányzó- és kisasztalok | 0.45 | 0.30–0.70 |  |
| 03d | Étkező – asztal + 6 ülőhely (szék/pad) | 0.60 | 0.40–0.90 |  |
| 03e | Nappali/étkező – szőnyeg | 0.20 | 0.10–0.35 |  |
| 03f | Nappali – függöny + sín (4,50 m üvegfal + étkező) | 0.25 | 0.15–0.40 | mennyezeti panel miatt rögzítés ellenőrizendő |
| 04a | Master – ágy + matrac (180×200) | 0.55 | 0.40–0.80 |  |
| 04b | Master – ágyfal / fejvég-burkolat (asztalos vagy panel) | 0.55 | 0.30–0.80 | hős-darab |
| 04c | Master – gardrób (PAX-váz + front vagy asztalos) | 0.45 | 0.35–0.70 |  |
| 04d | Master – éjjelik, olvasólámpák, függöny (3,65 m üveg), textil | 0.45 | 0.30–0.60 |  |
| 05 | 05.2 háló – ágy, gardrób, függöny, lámpa | 0.80 | 0.60–1.00 | csendes szoba, karcsú keret |
| 06 | 05.3 háló/dolgozó – ágy vagy dolgozó, gardrób, függöny | 0.80 | 0.60–1.00 | funkció eldöntendő |
| 07 | Fürdők (06.1, 06.2) + WC – tükör+fény, tároló, kiegészítők, textil | 0.50 | 0.30–0.70 | szaniterek beépítve; bidés WC-csere a fejlesztőé |
| 08 | Előtér + közlekedő – cipős/előszoba-szekrény, pad, tükör | 0.50 | 0.35–0.80 | az első benyomás helye |
| 09 | Mosó-szárító (gépek + elhelyezés) | 0.45 | 0.35–0.60 | hely tisztázandó |
| 10 | Világítás – Hue rendszer, LED-profilok, tápok, villanyszerelő | 1.00 | 0.70–1.40 | hős-tényező; a profil+táp+szerelés is költség |
| 11 | Falfelületek az asztaloson kívül – tapéta, lamella/kőfurnér panel, tapétázó | 0.50 | 0.30–0.80 |  |
| 12 | Textil, dekor, képek, növények, styling | 0.50 | 0.30–0.70 |  |
| 13a | Terasz – jakuzzi (Heissner-szint) | 1.70 | 1.70–2.70 | Correll-szint +1,0 M → máshonnan kell elvenni |
| 13b | Terasz – jakuzzi szállítás, daru/emelés, bekötés | 0.30 | 0.15–0.60 | 9. emelet – BIZONYTALAN, felmérés kell |
| 13c | Terasz – lounge-garnitúra | 0.60 | 0.40–0.90 |  |
| 13d | Terasz – étkező + napozók | 0.55 | 0.35–0.80 |  |
| 13e | Terasz – növények, kaspók, kültéri fény, árnyékoló | 0.45 | 0.30–0.80 |  |
| 14 | Szállítás, összeszerelés, hulladék, végtakarítás | 0.45 | 0.30–0.70 |  |

## Ismert kockázatok
1. **Jakuzzi-szint**: Correll ~2,7 M vs Heissner ~1,7 M (korábbi adat) – a különbözet ~1,0 M, csak átcsoportosítással fér bele.
2. **Jakuzzi emelése a 9. emeletre** (daru/lift/teherbírás) – ár ismeretlen.
3. **Külső tervezői díj**: ha Andi vagy a megkeresett 8 cég egyike tervez, a díj a 01. sort többszörösen meghaladhatja.
4. **Asztalos**: a 03a/04b/08 sorok csak 2–3 ajánlattal válnak valóssá; anyagszabály a GOAL.md 5. pontjában.
5. **Konyhai kiállások, mennyezeti panelek, belmagasság-mérés** ismerete nélkül a konyha és a függesztett elemek ára bizonytalan.
6. **Mosó-szárító helye** nem ismert.

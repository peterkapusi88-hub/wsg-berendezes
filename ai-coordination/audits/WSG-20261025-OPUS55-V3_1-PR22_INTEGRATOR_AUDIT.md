# A-902 · Opus 5.5 V3.1 (PR #22) – független integrátori audit, 1. kapu (Claude integrátor, 2026-10-25)

**Ág:** `integrator/opus55-v3-1-audit-20261025` (a `competition/baseline-20261025-v3` @ `45632b5`-ből). A PR #22 ága, a `main` és az élő Blender-fájl érintetlen. Rendelés, ajánlatkérés, merge és külső kommunikáció nem történt.

## 0. Hatály – mit auditáltam valójában
| | Érték |
|---|---|
| Kért pályamű | PR #22, végső commit `7d3c67f823c646d9daef06b294826e89c1c61467` |
| **Ténylegesen auditált** | `competition/opus55-v3-1-20261025` @ **`b24bee7`** (CP10, 2026-10-25 06:33) – a helyi klón utolsó elérhető állapota |
| Miért | A repó privát. Ebből a munkamenetből a GitHub nem érhető el (nincs hitelesítés), a GitHub Desktop „Fetch” parancsa le volt tiltva (zárolt képernyő). A `7d3c67f` objektum helyben nincs meg. |
| Hiányzó részek | `40_ELEMLISTA_V3_1.csv` (511 tétel), `50_KOLTSEG_ES_KOCKAZAT.md`, a stílusspecifikációk 5–8. fejezete (termék, Hue, költség, kockázat), valamint a b24bee7 utáni termékcserék (pl. S04 Lilo, S05 Melva, S07 Wolke 256 × 118 – a b24bee7-ben az S04 még Wolke L 258 × 167) |
| **Következmény** | Ez az audit **IDEIGLENES**. Az 511 tételes lista és a költségfájl auditja, valamint az S04–S10 méretpróbája a `7d3c67f` lehúzására vár. A szkriptek újrafuttathatók (`03_blender/integrator_opus55/`). |

Olvasott forrásdokumentumok (baseline v3): `GOAL.md` (main `114988f`), `ai-coordination/RENDER_REALITY_GATE.md`, `.agents/skills/wsg-stiluslabor/SKILL.md`, `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md`, `KOZOS_FIX_ALAP_v1.md/.csv`, `HUE_ALAPCSOMAG_v1.md`, `01_alaprajzok/villamos_kiallasok/A902_villamos.csv`, `04_renderek/semleges_v2b/REFERENCIA_KARTYA_A902_Cam02_v2b.md`, `05_promptok/KEP004_ChatGPT_Images_v1/README.md`; Opus: README, napló, manifest, 02, 03, 10 × stílusspecifikáció, 30 TV-fal, 60 prompt.

## 1. Kapuverdikt
| Kapu | Eredmény |
|---|---|
| 1. AUDIT – b24bee7 | **FELTÉTELES / NEM INDÍTHATÓ** – 1 kritikus (hatály), 5 magas (2 képgenerálást blokkol), 12 közepes, 3 alacsony lelet |
| 1. AUDIT – 7d3c67f | **NEM FUTOTT** (a commit nem elérhető) |
| 2. BLENDER – S01/S02 Cam_02 + Cam_12 | **FELTÉTELES PASS** – a kötelező méretek teljesülnek, ha a W02 melletti növény kikerül; részletek: `03_blender/integrator_opus55/BLENDER_JELENTES_OPUS55_S01_S02.md` |
| 2. BLENDER – S04, S05, S07, S08, S09, S10 | **NEM FUTOTT** (a próbázandó termékek csak a 7d3c67f-ben vannak) |

## 2. Hibajegyzék
Súlyosság: KRITIKUS / MAGAS / KÖZEPES / ALACSONY. **KB** = képgenerálást blokkol (az érintett képek a javításig nem indíthatók).

| ID | Súly | KB | Lelet | Bizonyíték | Javítás |
|---|---|---|---|---|---|
| K-01 | KRITIKUS | **KB (mind a 60)** | A végső commit (7d3c67f) nem auditált; az 511 tételes lista és a költségfájl nincs a vizsgált állapotban; a termékcserék (Lilo, Melva, Wolke 256 × 118) nem ellenőrizhetők. A promptverzió nem rögzíthető. | `git cat-file -t 7d3c67f…` → nincs objektum; README: `40_ELEMLISTA_V3_1.csv`, `50_KOLTSEG_…` hivatkozva, de a b24bee7-ben nincs | GitHub Desktop: Repository → Fetch, majd `git diff b24bee7 7d3c67f`. Az audit és a 2D/3D szkriptek újrafuttatása az új állapoton. |
| K-02 | MAGAS | **KB (10 × Cam_02)** | Mind a tíz Cam_02 prompt azt kéri, hogy az ML04 étkezőfüggeszték „a jobb képszélen” világítson. Az ML04 a Cam_02 képkeretén **kívül** van, így a modell elmozdítja vagy kitalálja a lámpát. | Szög a kamera tengelyétől 56,6°, a fél vízszintes látószög 42°; Blender-vetítés: Somar x 1,04–2,33, Brisia x 1,14–1,84 (a 0–1 tartományon kívül) | Csere: „The dining pendant at ML04 is outside this frame; at most its warm light spill reaches the right edge – do not draw a pendant in view.” |
| K-03 | MAGAS | **KB (Cam_12: S01, S02, S04)** | A „W02 melletti DNy-i sarokba” írt magas növény/olajfa a bejárat és a hálók közti fő útba kerül, és Cam_12-ben a W02-műalkotás elé áll. | 2D: hálók felé S01 1,00 → **0,70 m**, S02 0,90 → **elzárva**; 3D: a növény Cam_12-ben x 0,74–0,85, a mű x 0,61–0,82 (átfedés); alaprajzban 3 cm-es ütközés a művel | A növény törlése a W02 mellől (S01, S02, S04 Cam_12 és a spec). Ha kell növény: az étkező ÉK-i sarkába vagy az üvegfal keleti végére, külön méretpróbával. |
| K-04 | MAGAS | – | Teraszajtó: ha csak a keleti, 0,93 m-es szárny nyílik, a 2+2+1+1 nem tartja meg a terasz felé vezető utat. Opus ezt helyesen 5+1-gyel kezeli, de a képek hat széket mutatnak. | 2D: keleti szárny S01 **0,75 m**, S02 **0,70 m**; 5+1 esetén S01 0,95, S02 1,00 m | A kép felirata: „teraszajtó feltételes – hétfői mérés (2026-10-26)”. Nem blokkol, mert a hat szék a középső szárnyas alapesetben igazolt. |
| K-05 | MAGAS | KB (S05 Cam_02/03/12) | Hue-szabály: az S05 ML04-en Kave Home Novae szerepel. A repó saját jegyzete szerint a Novae beépített LED-es (10 W, 3000 K), tehát nem Hue. Az S08 ML04-en Kave Idela függeszték szerepel; az Idela asztali lámpa G9-es, ezért korábban ki volt szűrve. | `05_promptok/KEP004_ChatGPT_Images_v1/README.md` (Novae, Idela); `HUE_ALAPCSOMAG_v1` §1 | Csere E27/E14 foglalatú, igazolt függesztékre, vagy foglalatigazolás dátummal. |
| K-06 | MAGAS | KB (S02 × 3 nappali-nézet) | Az S02 asztala „Westwing Toni oval, black, 160 × 90”. Igazolt csak a világos tölgy Toni 160 × 90 (259 990 Ft, 2026-10-25, GEOMETRIA v2). A fekete változat nem igazolt, és a Westwing ebből a munkamenetből nem volt lekérdezhető. | GEOMETRIA v2 §2; a KEP004 csomag termékképe Toni 200 × 90 világos tölgy | Termékoldal, ár és dátum, vagy csere igazolt fekete 160 × 90-es asztalra (befoglaló x 8,00–8,90 / y 5,40–7,00). |
| K-07 | KÖZEPES | – | Spec ↔ prompt eltérés: S01 ML05 – a spec Ø80-as papírlámpást ír, a prompt Westwing Misaki Ø40 × 70-et (nem igazolt termék); S02 ML04 – a spec 4 gömbös Brisiát, a prompt 1 gömbös Brisia Ø50-et (ez az igazolt, E27); S02 asztal – a spec „40-es lista”, a prompt fekete Toni. | `10_STILUS_SPEC/S01, S02` vs. `20_PROMPTOK` | A promptváltozat a mérvadó; a specifikációt egyeztetni kell. A Misaki-t igazolni kell. |
| K-08 | KÖZEPES | – | A dohányzóasztalok termék és méret nélkül szerepelnek (S01: „low round dark-wood”, S02: „oval smoked-glass inside the U”). Az S02 U belseje csak 0,95 × 0,65 m: a 45–50 cm-es távolsággal az asztal csak a U szájában fér el. | 2D/3D: S02 feltételezett 60 × 60 a x 4,60–5,20 sávban; a TV-pad 0,49 m-re | Nevesített termék és méret (S02: Ø50–60 kerek, vagy két kisasztal). Az RRG B.3 szerint enélkül „nem igazolt”. |
| K-09 | KÖZEPES | – | Márvány dohányzóasztal (S07, S08) és „black marble detail” (S08) nevesített termék nélkül: valódi kő-e, mennyi az ára (RRG A.4, R5). | S07/S08 Cam_02 prompt | Termék vagy „marble-effect” jelölés, ár. |
| K-10 | KÖZEPES | – | **Padló: EL2184 tervezett vs. helyszíni.** A GOAL §2 szerint: Egger **laminált**, Classic 8/32 4V Aqua+, Grey Treviso Oak EL2184 (591760) – IGAZOLT-D (burkolatkiosztási terv). A ME-BAL-080 fotón göcsös, szürkésbarna tölgyhatású laminált látszik azonos dekorú szegőléccel, ami vizuálisan összeillő, de **termékazonosság nincs** (címke/szállítólevél nincs), és deszkaméret, fektetési irány sem igazolt (közeli fotó). A dokumentumok ellentmondanak egymásnak: RRG §A „Egger szürke tölgy **parketta**”, a westside-skill „Egger prémium parketta”, a v2b referenciakártya „IGAZOLT-D + IGAZOLT-F”, a GEOMETRIA v2 §4 „NEM IGAZOLT”. Opus helyesen jár el: terméknév nélkül, a fotó szerint ír. | GOAL §2; RRG §A; `REFERENCIA_KARTYA_A902_Cam02_v2b.md`; fotó `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg` (sha `88f93864…`) | Egységes státuszsor: „TERV: EL2184 laminált (IGAZOLT-D) · HELYSZÍN: vizuálisan megfelel (fotó) · termékkód, deszkaméret, irány: 2026-10-26, címke vagy szállítólevél alapján”. A „parketta” szó cseréje „laminált padló”-ra az RRG-ben és a skillben – Péter jóváhagyásával. A ME-BAL-080 minden képhez kötelező csatolmány. |
| K-11 | KÖZEPES | – | TV-fal-kiállások: a D16, D17, D18, G01–G04 és G08 a TV-bútor mögé kerül. Opus kivehető hátfalat és szervizkivágást ír, ez rendben van. A G01–G04 a rajzon x 3,91–4,03-on áll (nem a falsíkon), így az úszó pad (alja 18/22 cm) alá vagy mögé esik. A fugafény tápja a D18-ról a panel mögött fut – FELTÉTELES. | Validátor: 13–14 figyelmeztetés (lásd Blender-jelentés) | Hétfői mérés: a G-dobozok helye. Az asztalosrajzon szerviznyílás a pad hátfalán. |
| K-12 | KÖZEPES | – | Az ML05 mennyezeti kiállás a HF03 hűtő-fűtő mezőben van. A függeszték csak a kiállás dobozába rögzíthető, hőkamerás ellenőrzés után (Opus jelzi). | v2b referenciakártya | Hétfői hőkamera; a rögzítés módját a reality cardon jelölni kell. |
| K-13 | KÖZEPES | – | S02: valódi füstbronz tükör hátfal a mosogató mögött. Vízkő, tisztítás, és Cam_03-ban tükröződési kockázat (R8). | S02 spec §2 | Javaslat: hátfestett biztonsági üveg; vagy a kockázat kimondása a Cam_03-kártyán. |
| K-14 | KÖZEPES | – | S02 gardrób: füstbronz tükörfrontok PAX-on – súly és zsanérterhelés; BN-A R50 lekerekítés navy postforming HPL-lel. | S02 spec §3; 30 TV-fal BN-A1 | Gyártói igazolás és asztalos-ajánlat (Péter „mehet”-je után). |
| K-15 | KÖZEPES | – | Fürdő: az S01 faliszekrénye a 3D Esagonetta dekorcsempébe fúrva (távtartó kell, csempetörés-kockázat); az S02 tükör mögötti Hue-szalagjának tápja a D43/D44 – látható kábel, fürdőzóna-ellenőrzés (Opus FELTÉTELES-nek jelöli). | S01/S02 spec §4 | Szekrény a sima Geostone felületen; villamos zónaellenőrzés. |
| K-16 | KÖZEPES | – | Nézetek közötti azonosság: a W02-növény a Cam_02 bal szélén is látszana (4,5 % képterület), de a Cam_02 prompt „nothing else stands” mondata szerint nincs ott. A K-03 javítása ezt is megoldja. | 3D képterület | K-03 |
| K-17 | KÖZEPES | – | Fix költség: lásd 3. pont (B-01…B-03). | | |
| K-18 | ALACSONY | – | Fotóazonosító-ütközés: ME-BAL-045 az A-811 erkély és az A-902 nappali fotója is. Rossz csatolmány kockázata. | `08_allapotfelmeres/fotok/A811/10_erkely/…ME-BAL-045…`, `…/A902/04_nappali/…ME-BAL-045…` | Mindig teljes útvonal és sha256 a kártyán. |
| K-19 | ALACSONY | – | S01: vinil falburkolattal bevont PAX-frontok – élkopás. | S01 spec §3 | Gyárilag fóliázott MDF-front. |
| K-20 | ALACSONY | – | A validátor S08-hibája (érzékelő takarása) **téves riasztás**: az eszköz a 05.1 hálóban van, a 10 cm-es fal túloldalán; a 12 cm-es tűrés fogja meg. | `A902_villamos.csv` S08: 05.1 SZOBA, x 3,569 | Nem tervezési hiba; a validátor tűrését falon át nem kellene alkalmazni (Codex-feladat). |

**Ami rendben van (b24bee7):** 60/60 prompt; a státuszsor („CONCEPT – NOT VALIDATED”) mindegyikben szerepel; a kameránkénti fény a GEOMETRIA v2 §3 szerint (Cam_02 kék óra, Cam_12/03/11 nappal, Cam_04 este, Cam_10 műfény); padló terméknév nélkül, a fotó szerint; a C elrendezés (L háttámla x 6,67, U x 6,60, 160 × 90 az ML04 alatt, 2+2+1+1); a kanapé képaránya Cam_12-ben (S01 16,5 %, S02 23,3 % – a prompt „egyötöd”, illetve „egynegyed” leírása egyezik); a TV-fal-szekrények z 2,53-nál megállnak (nincs HF-mező alatti mennyezetig érő test); a Cam_12 állóhelye szabad; a kanapé–TV-bútor távolság S01-ben 0,74, S02-ben 0,89 m (≥ 0,60).

**Javítási állapot (2026-10-25, Péter kérésére):**
- **K-02 és K-03** a négy induló promptban integrátori v1.1-ben javítva: `05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_1/` (a versenyzői fájl változatlan).
- **K-03 a többi helyen nyitott:** S04 Cam_12, valamint a S01/S02 specifikáció növénysorai.
- **K-21 (alacsony, új):** az S02 Cam_12 prompt „brushed-brass rod”-ot ír a Brisiához; a termékadat szerint rozetta és fekete, állítható drót tartja.

## 3. Költség – 18 M tervezhető + 2 M tartalék, a 8,40 M közös fix
A közös fix rész számtana helyes (0,40 + 1,10 + 0,30 + 0,80 + 0,80 + 0,50 + 0,45 + 3,60 + 0,45 = 8,40). A realitásvizsgálat **becslés**: a webshopok ebből a munkamenetből nem voltak lekérdezhetők, dátumozott ár nincs.

| ID | Súly | Tétel | Lelet | Becsült reális sáv |
|---|---|---|---|---|
| B-01 | MAGAS | 02b gépek 1,10 | A főzőlap a nyugati, mellvéd melletti soron van, fal nincs mögötte; az elszívó-dugalj (D05, x 8,97 / y 3,22) ott van. Az elszívó csak mennyezeti (HF-mező / +2,45-ös álmennyezet) vagy pultba épített lehet; a pultba épített, elszívós főzőlap egyedül 0,4–0,9 M. | 1,40–1,80 |
| | | 14 szállítás, szerelés 0,45 | METOD két sor + magas elemek, 3 × PAX (05.1/05.2/05.3), 9. emelet, Kave utcaszinti átadás | 0,60–0,90 |
| | | 13e növény, kültéri fény, árnyékoló 0,45 | 79 m²-es terasz; nagy árnyékoló (konzolos napernyő vagy napvitorla) egyedül 0,15–0,40 | 0,60–0,90 |
| | | 13b jakuzzi-emelés, bekötés 0,30 | 9. emelet, daru; saját sáv 0,15–0,60 | 0,30–0,60 |
| | | 05, 06, 08, 09 | IKEA-szinten tartható, de szűk | 2,55–2,90 |
| | | **Fix összesen** | | **≈ 8,9–10,0 (becslés)** |
| B-02 | MAGAS | Terasz-keret | Három szám ellentmond egymásnak: GOAL §3 „~4 M”, westside-skill „kb. 5 M”, KOZOS_FIX „3,60 M”. | Péter döntse el, melyik a plafon. |
| B-03 | MAGAS | Tartalék | A 2,00 M a 20 M 10,0 %-a, tehát megfelel. De a Correll-jakuzzi „+1,0 M közös kockázata” nem terheli a stílust, a 20 M-os plafont viszont igen: ha bekövetkezik, a tartalék 1,0 M-ra (5 %) esik, ami szabálysértés. | Ha a fix rész igazoltan 9,5 M, a stílusfüggő keret 9,60-ról 8,50 M-ra szűkül (−1,10 M). |
| B-04 | – | Opus 9,60 M stílusfüggő terve, 511 tétel | Nem auditálható (K-01). Ami a b24bee7-ben van: S01 KI-A TV-fal 03a 0,75–0,99 + Hue 0,16–0,22; S02 BN-A 03a 0,90–1,18 + Hue 0,15–0,20 – a 03a 1,10-es célon belül vagy a sáv felső szélén, asztalos-ajánlat nélkül. | – |

## 4. Kivitelezhetőség – összefoglaló
- **TV-falak (S01 KI-A, S02 BN-A):** megépíthetők. Mélység 42–45 cm, a kanapé–TV-bútor távolság ≥ 0,74 m. Szerviznyílás kell a D16/D17/G elé. Az R50-es hajlított él és a tükörrés asztalos-igazolást igényel. A Hue-fugák FELTÉTELESEK (kábelút).
- **Kanapék:** a Lennon L és a JÄTTEBO U a C elrendezésben igazolt. Az S02 U északi karja és az üveg között 0,225 m van – a függöny csak a kávában fut (a káva mélysége hétfőn mérendő).
- **Étkező:** a Toni 160 × 90 befoglalója igazolt. A székkihúzás ≥ 1,05 m, szemöldökbe tett függönnyel 0,93 m. A keleti teraszszárny esete: K-04.
- **Hue-kiállások:** csak meglévő pontok (D16/D17/D18, D19, D21, FL01, FL02). Az FL02 és FL01 tápja FELTÉTELES (Opus is jelöli). A két Hue-szabálysértés: K-05.
- **Asztalos:** a Egger-anyagszabály (laminált, hajlított MDF, legfeljebb egy furnérfelület) S01-ben és S02-ben tartva van. A KARLBY tölgy munkalap az egyetlen furnérfelület; S01-ben a Toni asztal is furnéros, de ez kész bútor, nem asztalosmunka.

## 5. Teendők a kapu zárásához
1. `7d3c67f` lehúzása (Péter: GitHub Desktop → Repository → Fetch), diff a b24bee7-hez, az audit újrafuttatása (különösen az 511 tétel és a `50_KOLTSEG`).
2. Opus / Péter: K-02 és K-03 szövegcsere a promptokban (vagy integrátori patch, lásd a képgenerálási átadást), K-05 és K-06 termékigazolás.
3. Hétfő (2026-10-26): teraszajtó-szárny, kávamélység, G-dobozok helye, padlócímke és deszkairány, HF-mező hőkamera az ML04/ML05-nél.

# A-902 – kameracsomag C: végleges C elrendezés, Cam_03 K1, Cam_12 v3 (r1)

- **Task ID:** WSG-20261025-A902-KAMERACSOMAG-C · **Készítette:** Claude, 2026-10-25 (CET)
- **Megbízás:** Péter 04:08 CET (GOAL 7.).
  - Elfogadva: C elrendezés és K1 Cam_03.
  - Kérve: a Cam_12 kötelező kompozíciós felülvizsgálata, egységes kameracsomag, validátor és Render Reality Gate, majd a végleges méretek és kameraképek bemutatása.
- **Ág:** `kep004/kameracsomag-C-K1`. Tartalmazza a PR #17 (Cam_12 v2) és a PR #18 (alternatívák, Cam_03 jelöltek) teljes tartalmát, plusz ezt a csomagot.
- **Státusz:** `MÉRETPRÓBA` + `KAMERA JAVASLAT` – nem stílusterv, nem kivitelezési terv.
- **Nem engedélyez:** merge-et (PR #17, #18 és ez a csomag külön döntés), képgenerálást.

## 1. Végleges C elrendezés (rögzített továbbtervezési alap)
**Forrás:**
- `03_blender/geometry_v2/elrendezes_C/elrendezes_C_A902_rogzitett.json`;
- szkriptek: `c_hatarhelyzet.py` (érzékenység), `c_vegleges_lap.py` (lap);
- ábra: `04_renderek/A902_kameracsomag_C/A902_C_vegleges_alaprajz_kamerak.png`.

| | **S01 – Lennon L + Toni 160** | **S02 – JÄTTEBO U + Anouk 180** |
|---|---|---|
| Kanapé háttámla (x) | **6,67** (a PR #18-hoz képest +7 cm, hogy a 60 cm-es TV-szekrény is elférjen) | **6,60** |
| Kanapé befoglaló | x 4,87–6,67; y 5,21–7,59 | x 5,00–6,60; y 4,975–7,825 |
| Asztal | **x 8,00–8,90; y 5,40–7,00** (a PR #18-hoz képest 10 cm-rel délebbre, lásd 2.1) | x 8,00–8,90; y 5,35–7,15 (Anouk 180, ahogy a PR #18-ban; **ajánlott: 160 × 90 az S01 befoglalójában**, 2.1 – a táblázat számai és a tömbképek még a 180-assal készültek) |
| Székek | 2–2 a hosszoldalon (y 6,10 / 6,70), 1–1 a végeken (Eamy 55 × 53) | 2–2 (y 6,15 / 6,75), 1–1 a végeken (Ciselia 52,5 × 55) |
| ML04 az asztal közepétől | 0,12 m | 0,10 m |
| Fő utak, betolt székkel (terasz / konyha / folyosó / 05.3) | 0,90 / 1,00 / 0,95 / 0,90 | 0,90 / 0,90 / 0,90 / 0,90 |
| Székkihúzás (min. / északi végszék) | 1,05 / 1,05 | 0,90 / 0,90 |
| Ülő vendégekkel (terasz / konyha / folyosó / 05.3) | 0,70 / 0,75 / 0,95 / 0,70 | 0,75 / 0,70 / 0,90 / 0,70 |
| Szék–kanapé | 0,98 | 1,03 |
| Kanapé–TV-bútor (60 cm / 40 cm) | 0,60 / 0,80 | 0,73 / 0,93 |
| Nézőtáv (képernyő x 3,77) | 2,40 m | 2,33 m |

**Mindkettőn:** a kötelező méretek teljesülnek 40 és 60 cm mély TV-fallal is (fő út ≥ 0,90; székkihúzás ≥ 0,90; kanapé–TV ≥ 0,60).

## 2. Péter feltételeinek ellenőrzése
### 2.1 Az északi székkihúzás 0,90 m-es határhelyzete
- **Függöny nélkül:** a kihúzás az üveg előtti falsíkig (y 8,05) mérve S01-en 0,95, S02-n 0,90 volt.
- **Behúzott függönnyel** (12 cm-es sáv a szemöldök belső síkján – becslés): 0,83 (S01), illetve 0,78 (S02).
- **S01 – megoldva:** az asztalt 10 cm-rel délebbre toltam (y 5,40–7,00).
  - Az északi kihúzás 1,05, függönnyel 0,93 lett.
  - A korábbi 0,90-es keleti szék (az akna sarka felé) is 1,05-re javult.
  - Ára: ülő vendégekkel a 05.3 felé 0,80 helyett 0,70, a konyha felé 0,85 helyett 0,75. A fő utak és az ML04 (0,12) maradnak.
- **S02 – nem tolható:** 5 cm-es déli tolás már a konyha és a 05.3 felé vezető fő utat 0,85-re szűkíti. Marad az északi 0,90, függönnyel 0,78.
  - **Javítás 1 (javaslat):** a függönysín a szemöldök alá, a kávába kerül (a falsík és az üveg között 16 cm-es káva van, y 8,05–8,21). Így a behúzott függöny nem lóg be. A káva mélységét és a profilt hétfőn mérni kell; mennyezeti HF-mezőbe továbbra sem fúrunk.
  - **Javítás 2 – ajánlott:** S02-n is 160 × 90-es asztal, ugyanabban a befoglalóban, mint az S01 (x 8,00–8,90; y 5,40–7,00; oldalszékek y 6,10 / 6,70).
    - Ezzel az északi kihúzás 1,05, függönnyel 0,93.
    - A fő utak: 0,90 / 0,95 / 0,90 / 0,90; ülő vendégekkel: 0,75 / 0,75 / 0,90 / 0,70; ML04 0,12.
    - Ez egyezik a tervverseny közös blokkjával (PR #19: „az étkező 160 × 90-es asztalbefoglalója kötött”).
    - **Termék:** az Anouk étkezőasztalként csak 180 × 90-ben látszik (Westwing, keresés 2026-10-25; a 160-as Anouk dohányzóasztal). Az S02-höz 160-as asztalt kell keresni.
    - Ha a 180-as Anouk marad: az északi kihúzás 0,90, függönnyel 0,78.
- 0,75 m alatt egyik változat sincs. A 0,90 m a kényelmes cél.

### 2.2 Az ülő vendégek melletti 0,70–0,80 m-es szűkületek
- **Hol vannak?**
  - Az asztal keleti és déli széke mögött, a hűtőoszlop sarka (x 9,95; y 5,25) és a 05.3 ajtó felé.
  - Az északi szék mögött, a terasz felé.
- **Mit jelent?** Ülő vendég mögött 0,70 m-en el lehet menni (oldalazva, tálcával szűken). Kényelmes, 0,90 m-es kiszolgálósáv csak a nyugati és a folyosó felőli oldalon van.
- **Betolt székkel** (normál állapot) minden fő út ≥ 0,90 m.
- **Nem javítható** a kötelező méretek rontása nélkül: az asztal bármely irányú tolása valamelyik fő utat 0,90 alá viszi (`c_hatarhelyzet.json`, 80 eset).

### 2.3 A teraszajtó tényleges tolható része (hétfőn ellenőrizendő)
**Vizsgált táblák:** a modell profiljai szerint három üvegtábla van: x 4,47–6,23, x 6,29–7,92 és x 7,98–8,91. Péter (2026-10-24 18:43): a tolható rész a keleti oldalon van.

| Ha a nyíló szárny… | Út betolt székkel (S01 / S02) | Megítélés |
|---|---|---|
| a középső tábla (x 6,29–7,92) | 0,95 / 1,00 | rendben |
| csak a legkeletibb, 0,93 m-es tábla (x 7,98–8,91) | 0,75 / 0,60 – **az északi végszék előtte áll** | nem megfelelő |
| ugyanez, az északi végszék nélkül (5 fix + 1 pótszék) | 0,95 / 0,90 | rendben |

**Következmény:** ha hétfőn kiderül, hogy csak a keleti keskeny szárny nyílik, az északi végszék pótszék lesz (vendégségkor kerül az asztalhoz). Az asztal helye nem változik, hat hely továbbra is van.

### 2.4 A 60 cm-es TV-szekrény – felső lehetőség, nem kötelező
- Mindkét kanapéhely 40 és 60 cm közötti TV-fal-mélységnél is teljesíti a kötelező méreteket. Ezért a kanapé helye nem függ attól, mit tervez a három kreatív résztvevő.
- **Új korlát a Cam_12 miatt** (3. pont): a TV-fal északi végén (y > 7,65) nem lehet mennyezetig érő szekrény; ott legfeljebb alacsony (≤ 0,90 m) elem vagy ≤ 4 cm-es panel kerülhet.
- **Validátor (TV60M tömb):**
  - a déli 60 cm-es szekrény a **D18** dugalj elé kerül → szervizkivágás kell;
  - a TV-alsószekrény a D16, D17, G01–G04 és G08 elé kerül → kivehető, szellőző hátfal kell;
  - hiba nincs.
- **A TV tengelye:** a TV-csatlakozók (G01–G04, D16, D17, G08) y 6,11–6,44 között vannak. Két, szimmetrikus magas szekrény esetén a köztük maradó nyílás ehhez a tengelyhez igazodjon. A próbatömbben (szekrények: y 4,25–5,05 és 6,85–7,65) a 75"-os képernyő 5 cm-rel belelóg az északi szekrénybe → legfeljebb 65–70" vagy szélesebb középső mező (validátor-figyelmeztetés, nem hiba).

### 2.5 A TV képernyősíkja és a nézőtáv
- **Képernyő:** a falsíkon vagy a fülke hátfalán, x ≈ 3,77.
- **Nézőtáv:** 2,40 m (S01), 2,33 m (S02). 65–77"-os képernyőhöz megfelelő (becslés, kb. 35–40°-os látószög).
- **Ha a TV egy 60 cm-es szekrény elejére kerülne:** a nézőtáv 1,8–1,9 m lenne, 2,0 m alatt. Ezt kerülni kell, vagy legfeljebb 55–65"-os képernyő jöhet.

## 3. Cam_12 – kompozíciós felülvizsgálat (Péter 04:08)
**Bizonyítékok:**
- jelöltkör 1 (10 állás) és jelöltkör 2 (36 állás): `03_blender/geometry_v2/cam12_C/`, naplók: `naplok/cam12C_jeloltek_log.json` és `cam12C_jeloltek_r2_log.json`;
- kontaktlap: `04_renderek/A902_kameracsomag_C/A902_Cam12_jeloltek_r1_kontakt.jpg`.

**Mérés:** sugárvetés 160 × 100-as képrácson; hogy a képterület hány százaléka melyik elem, és a falfelületek hány százaléka takaratlan.

**Két ok a változtatásra:**
1. A C elrendezésben a kanapé közelebb került. A v2 állásból a kanapé a kép **26 % (L), illetve 31 % (U)** részét foglalta el.
2. **A v2 kamerahelye (x 3,95) a TV-fal 60 cm-es sávjába esik** (x 3,67–4,27).
   - Ha a TV-fal északi végére mennyezetig érő, 60 cm mély szekrény kerül, az a v2 kép **52–58 %-át** kitölti.
   - Ilyenkor a W02 és a W07 teljesen eltűnik, a konyha láthatósága 0,92-ről 0,61-re esik.
   - Elforgatással, lencsével vagy magasabb állással ez nem javítható (jelöltkör 1, R0–R5, R9).

**Javasolt Cam_12 v3:**
- hely [4,40; 7,88; 1,60] – a TV-faltól 0,73 m-re, a 60 cm-es sávon kívül;
- irány θ −48° (délkelet), vízszintes;
- 22 mm, shift_y −0,05.

| Képterület / láthatóság | v2 régi – S01 | **v3 – S01** | v2 régi – S02 | **v3 – S02** |
|---|---|---|---|---|
| Kanapé a képben | 26 % | **16 %** | 31 % | **23 %** |
| Étkező (asztal + székek) | 5 % | **9 %** | 4 % | **7 %** |
| Konyha (bútor + fal) | 9 % | **11 %** | 9 % | **11 %** |
| W02 a képben / takaratlan | 18 % / 100 % | **22 % / 100 %** | 15 % / 86 % | **18 % / 86 %** |
| W07 a képben / takaratlan | 12 % / 100 % | 10 % / **90 %** | 12 % / 100 % | 10 % / **90 %** |
| W03 + 05.3 ajtó | 7 %, ajtó 80 % | 8 %, ajtó 80 % | 7 %, ajtó 78 % | 8 %, ajtó 78 % |
| Mennyezet | 10 % | 16 % | 10 % | 16 % |
| **60 cm-es TV-szekrénnyel** | **W02 0 %, W07 0 %, szekrény 57 %** | **változatlan (szekrény 0 %)** | **W02 0 %, W07 0 %** | **változatlan** |

**Megítélés:**
- **Előny:** az étkező és a konyha nagyobb és tisztább, a W02 a kép közepének jobb oldalán uralkodik. A kanapé alacsony előtérsávvá válik: a kép tárgya marad, de nem nyomja el a teret. A kamera bármilyen TV-fal-tervvel működik.
- **Ára:**
  - 6 %-kal több mennyezet (a kanapé-előtér helyett). Rejtett LED-es vagy fényárnyékos mennyezeti sávnál ez előny lehet, sima fehér mennyezetnél kevésbé.
  - A W07 egy keskeny csíkja (a közlekedő déli falának töredéke) kiesik a kép jobb széléről.
- **Elvetett alternatívák:**
  - θ −40/−44°: több W02, de a W07 eltűnik;
  - 24 mm: a 05.3 ajtó a bal szélre szorul;
  - shift_y −0,02: a kanapé 10–12 %-ra csökken, de a mennyezet 19–21 % lesz.
- **Feltétel:** a kamerahely (x 4,30–4,50; y 7,75–8,05) környékére nem kerülhet magas bútor vagy állólámpa.

## 4. Cam_03 K1 (Péter: elfogadva)
- **Kamera:**
  - hely [9,45; 7,55; 1,50], dél felé (rot [π/2; 0; −π]), vízszintes;
  - 20 mm, shift_y −0,08; nappali fény.
- **Képterület a C tömbbel:**
  - konyha 29 %, a magas elemek (hűtőoszlop, sütős-mikrós fal) eleje 100 %-ban takaratlan;
  - étkező 12–13 %, kanapé 0 %, mennyezet 6 %.
  - A Cam_12-vel való átfedés a PR #18 szerint 42 % (a régi Cam_03-nál 70 % volt).
- **Mit kell tudni róla:**
  - a K1 egy „galéria” nézet a két pultsor közé;
  - a jobb felső sarokban közel lóg az ML04 függeszték: a függeszték lámpateste a kép része lesz, magasságát és méretét a lámpaválasztásnál ehhez is mérni kell;
  - a konyha keleti pultfala (x 10,55) a keleti sor mögött takarásban van, nem látszik.

## 5. Validátor (v2b-1-k13)
**Fájlok:**
- lock: `03_blender/geometry_lock_A902_v2b.json` – a kamerák frissítve, a régi paraméterek a `javitasok` v2b-1-k13 bejegyzésében;
- blend: `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`, sha256 `e01170d3…0ddbd` (a k12 v2-ből, `03_rogzites_C.py`, másolatként mentve). Csak a két kamera változott; ezt a szkript ellenőrizte.

| Mód | Eredmény | JSON |
|---|---|---|
| üres | **PASS 0/0** – 12 kamera teljes paraméterrel, az új Cam_03/Cam_12 a lock szerint | `03_blender/validator_v2b1k13_ures.json` |
| referencia (beépített szaniterek) | FAIL 6/3 – a régi 6 szaniter-ütközés, nem e csomag tárgya (mint a k12-ben) | `…_referencia.json` |
| master bútor | PASS 0/0 | `…_master_butor.json` |
| C S01 / S02 + TV40 | **PASS 0 hiba / 7 figyelmeztetés** (dugaljak és aljzatok a TV-alsószekrény mögött) | `…_C_S01_TV40.json`, `…_C_S02_TV40.json` |
| C S01 / S02 + TV60M | **PASS 0 hiba / 12 figyelmeztetés** (ugyanezek, valamint a D18 a déli 60 cm-es szekrény mögött; a 75"-os képernyő 5 cm-es átfedése az északi szekrénnyel) | `…_C_S01_TV60M.json`, `…_C_S02_TV60M.json` |

**Futtatás:** a Mac élő Blenderéből indított háttérfolyamat (Blender 5.2.3).
- A forrásfájl sha256-ja a futás előtt és után azonos (`66172d43…`).
- Az élő, nem mentett projektfájlt (`Blender_aktualis_2026-10-24/…`) nem érintettem.

## 6. Render Reality Gate – preflight (reality cardok a két új kamerához)
A Gate B) része szerint. Generált kép nincs, ezért a C) audit nem releváns. Ezek a kártyák a következő promptcsomag kötelező bemenetei.

### RENDER_REALITY_CARD – A-902 · Cam_12_Nappali_Hero v3 · v2b-1-k13 · alapkép: `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png`
| Felület / elem | Állapot | Megjegyzés |
|---|---|---|
| Padló | MEGLÉVŐ / MEGTARTOTT – szürke tölgy, dekor **NEM IGAZOLT** | a kép kb. 4–6 %-a; nem cserélhető, nem színezhető át |
| W03 (bal), a 05.3 szürke ajtóval | MEGLÉVŐ fal / ajtó: világosszürke, fekete kilincs | a falkezelés JAVASOLT / BECSLÉS, a kapcsolók (K07–K09, D12, D13) szabadon maradnak |
| Konyha (középen balra): pultfal és magas elemek | ÚJ / ÁRAZANDÓ – a konyhabútor a stílus része | a terv szerinti sorok (WGR1 18. o.); front, anyag és ár a stílusból |
| W02 (jobb közép, fő felület) | MEGLÉVŐ fehér; kezelése JAVASOLT / BECSLÉS | a kapcsolóoszlop (K10–K12, T01, S01, D19) szabadon |
| W07 (jobb szél, a közlekedő torka) | MEGLÉVŐ fehér; kezelése JAVASOLT / BECSLÉS | K25–K27, D46 szabadon |
| Kanapé (előtér) | ÚJ – S01 Lennon L / S02 JÄTTEBO U (valós termék) | a C szerinti helyen; a konfiguráció a stílusé |
| Étkező (asztal + 6 szék), ML04 függeszték | ÚJ – a stílus valós termékei | C: 2+2+1+1; az ML04 a meglévő kiálláson |
| Mennyezet | MEGLÉVŐ fehér, HF-mezők – nem fúrható | rejtett LED csak a V3.1 kiállás-kerete szerint |
| TV-fal (W01) | nem látszik | a kamera mögött jobbra; a kamerahely környékére nem kerülhet magas elem |
| Üvegfal, terasz | nem látszik | – |

### RENDER_REALITY_CARD – A-902 · Cam_03_Etkezo_konyha K1 · v2b-1-k13 · alapkép: `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png`
| Felület / elem | Állapot | Megjegyzés |
|---|---|---|
| Padló | MEGLÉVŐ / MEGTARTOTT – dekor NEM IGAZOLT | a konyhában is ugyanaz a parketta (terv szerint – helyszínen ellenőrizendő) |
| Konyha: két pultsor, hűtőoszlop (D13), déli magas elemfal (sütő, mikró) | ÚJ / ÁRAZANDÓ – a kép tárgya | front, munkalap, fogantyú, pult- és szekrényvilágítás a stílusból; a gépek helye a kiállások szerint |
| Konyhai falak, szemöldök, álmennyezet (+2,45) | MEGLÉVŐ fehér | az álmennyezet a felsőszekrények magasságát korlátozza (állapotfelmérés D11) |
| Étkező (jobb előtér), ML04 | ÚJ – a stílus valós termékei | a függeszték a kép jobb felső sarkában; a lámpatest mérete és magassága ehhez is mérendő |
| W02 / W03 részlet | MEGLÉVŐ fehér | – |
| Fény | nappali (Péter 02:52) | a pult- és szekrényfény visszafogottan |

**Státusz:** mindkét kamera `ALAPKÉP – BLENDER, TERV SZERINTI GEOMETRIA (helyszínen nem mért)`. Kép nem készült. Az első stílusképek a jóváhagyás után is `KONCEPCIÓ – NEM VALIDÁLT` státuszúak.

## 7. Nyitott tételek
1. **Hétfő (helyszín):**
   - a teraszajtó nyíló szárnya (2.3);
   - a nappali üvegfal kávájának mélysége (függönysín, 2.1);
   - a TV-csatlakozók tényleges helye;
   - a padló dekorja.
2. **S02:** 160-as asztal vagy függöny a kávában (2.1).
3. **Toni 200:** a C-ben már nem kell (S01: Toni 160).
4. **Astra V3.1:** 04:28 CET-kor még nincs CP0 a GitHubon (nincs `astra/creative-upgrade-v3-1-…` ág).
5. **Tervverseny (PR #19, a másik Claude-munkamenet):** a közös §0 blokk a C elrendezést és a K1-et már tartalmazza, a Cam_12 v3-at és a kamera miatti TV-fal-korlátot még nem.
   - Ezek pontos számai: `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v1.md` (ezen az ágon).
   - Javaslat: a §0.1 hivatkozzon erre a fájlra.

## 8. Döntés (Péter)
1. **Cam_12 v3 elfogadása:** [4,40; 7,88; 1,60], θ −48°, 22 mm, shift −0,05; vagy kér-e egy változatot (például több W02-t θ −44°-kal, a W07 rovására).
2. **Közös étkező-befoglaló:** 160 × 90, x 8,00–8,90; y 5,40–7,00, mindkét kanapéval (S01-en 10 cm-rel délebbre, mint a PR #18-ban).
   - Előny: jobb székkihúzás.
   - Ára: az ülő vendégek mögött 0,70 m.
   - S02-höz 160-as asztal kell az Anouk 180 helyett.
3. **Merge:** külön engedéllyel.
   - Ez az ág a PR #17 és a PR #18 tartalmát is hozza, ezért ha ezt olvasztjuk be, a #17 és a #18 lezárható.
   - Merge előtt: Péter „mehet”-je és egy friss validátorfutás a main aktuális állapotán.

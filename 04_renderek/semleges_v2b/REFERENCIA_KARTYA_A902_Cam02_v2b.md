# A-902 · Cam_02 · semleges, alaprajzhű referencia (v2b) – Reality Card

**Státusz: ELŐSZŰRT ALAP – TERV SZERINT, helyszínen NEM mért.** Nem PASS, nem kivitelezési bizonyíték.

A kép üres, bútor nélküli, alaprajzhű összehasonlító alap a stílusképekhez (`WSG-20261024-STYLE4-003`). A geometria a méretezett megvalósulási tervből jön (M1 KORR 2, lock v2b). A helyszíni mérés (hétfő) után ugyanez a szkript újrafuttatható.

- **Készült:** 2026-10-24, Claude.
- **Bemenet:** `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`, sha256 `c27931e053b0…d9c2`. A render egy **másolaton** készült; az élő Blender-fájl és a repóbeli .blend érintetlen.
- **Szkript:** `03_blender/geometry_v2/render_semleges_v2b_referencia.py`. Ellenőrző rajzok: `03_blender/geometry_v2/referencia_v2b_rajzok.py`.
- **Validator v2** (lock v2b + villamos kiállások), a render előtt, ugyanazon a másolaton: **PASS – 0 hiba, 0 figyelmeztetés**.
  - 60 fal, 54 nyílászáró, 17 padló, 43 teraszelem és 9 kamera egyezik a lockkal.
  - Ez azt igazolja, hogy a modell a **tervvel** egyezik, nem azt, hogy a **valósággal** (K6: ±15 cm, hétfői mérés).

## Fájlok

| Fájl | Mi ez |
|---|---|
| `A902_semlegesv2b_1_nappali.png` | **Cam_02** nappali → terasz, 1600×1000, üres, nappali borult fény |
| `A902_semlegesv2b_1_nappali_ellenorzo.png` | ugyanaz rárajzolva: lámpa- és fali kiállások, TV-blokk, HF03 mennyezeti mező, méretek, bizonytalan elemek |
| `A902_semlegesv2b_0_felulnezet_Cam02.png` | felülnézet: falak, nyílások, kiállások, HF-mezők, Cam_02 látómező, Cam_03/04 helye |
| `A902_semlegesv2b_2_etkezo_konyha.png` | Cam_03 – kiegészítő, ellenőrző rárajzolás nélkül (lásd lent) |
| `A902_semlegesv2b_3_master.png` | Cam_04 – kiegészítő, ellenőrző rárajzolás nélkül (lásd lent; a mellvéd-modellhiba miatt egy teraszelem rejtve) |
| `kamera_parameterek.json` | a renderelt kamerák mátrixa, objektív, szenzor, felbontás |
| `validator_v2b_referencia.json` | a Validator teljes kimenete |
| `beallitasok.json` | mi változott a másolaton (rejtés, anyag, fény, render) |

**Kamera (Cam_02, lock v2b):**
- hely [8,30; 4,40; 1,55] m; forgatás [1,479; 0; 0,858] rad (XYZ);
- 20 mm, 36 mm szenzor (AUTO); vízszintes látószög 84°, függőleges 59°; 1600×1000.

**Render:**
- Cycles CPU, adaptív legfeljebb 512 minta, OIDN-zajszűrés;
- AgX (look: None), expozíció +3,3 EV;
- egyenletes, irány nélküli borult ég (nap nincs), a horizont alatt semleges szürke talaj.

## Felületek és elemek – mi igazolt, mi nem

| Elem | A képen | Forrás / státusz | Bizonytalanság |
|---|---|---|---|
| Padló | szürkésbarna tölgy-laminált, 4V horony, É–D deszkairány; a göcsök elmosódott sötét foltként jelennek meg (egyszerűsítés, nem folt) | **Egger Grey Treviso Oak EL2184, Classic 8/32 4V Aqua+ (591760)** – IGAZOLT-D (burkolatkiosztási terv, 21. o.) + IGAZOLT-F (ME-BAL-080) | **Procedurális közelítés**, nem a gyári dekorkép. Deszka 1292×193 mm: Egger Classic 8 mm formátum (UK forgalmazó, Grey Treviso Oak 193×8×1292 mm), a konkrét tételen NEM igazolt. Az irányt a ME-BAL-045/046 fotóból becsültem. A göcsös, erezett rajzolat egyszerűsített. |
| Szegőléc | 6 cm, a padló tónusában, minden parkettás falon | IGAZOLT-F (6 cm, azonos dekor) | egyszerűsített felület; a modellben lockon kívüli elem |
| Falak, mennyezet | semleges fehér (albedó 0,82) | IGAZOLT-F (fehér, glettelt) | festéktípus ismeretlen. A nyugati válaszfalra a v2b fájlban még a Zenit-tapéta volt rendelve: a referencián fehérre javítva. |
| Nyugati válaszfal (TV-fal) | sima fehér, 4,00 m (y 4,05–8,05) | TERV SZERINT; 10 cm vastag | **anyaga ismeretlen** – teherbírás, TV- és panelrögzítés nem igazolt |
| Teraszüvegezés | 4,50 × 2,53 m tolóajtó, osztók x 6,22–6,29 és 7,91–7,98 m; a kép a jobb szélső mezőt nem mutatja | TERV SZERINT | **BIZONYTALAN (K5):** a ME-BAL-045 fotón pillérrel osztott nyílás és küszöb látszhat; nyitható szárnyak, küszöb, fellépés nem validált |
| Nyílászáró-profil | belül fehér | IGAZOLT-F | a küszöb és az alsó profil színe a fotón sötétebb lehet |
| Szemöldök az üveg fölött | 0,37 m (2,53–2,90) | TERV SZERINT | a redőnytok belső látványa nem modellezett |
| Motoros redőny | nincs a képen | R02: motoros redőny kiállása a redőnyszekrénynél – IGAZOLT (műszaki melléklet, 2024.02.13.); a GOAL szerint redőny van | a tok és a vezetősín belső látványa nem modellezett |
| Belmagasság | 2,90 m | IGAZOLT-M: 2,90–2,93 m | – |
| Mennyezeti lámpakiállás ML05 „n,p” | nem látszik; az ellenőrző képen jelölve | TERV SZERINT (x 5,62, y 6,27) | a valós hely ±10 cm. **A kiállás a HF03 hűtő-fűtő mezőn belül van** (a PR #7 kiállás-rétege is ezt jelzi): a lámpa rögzítése csak akkor biztonságos, ha a dobozban van rögzítési pont, és a környezete csőmentes (hőkamera, fűtési üzemben) – hétfői teendő |
| Hűtő-fűtő mező HF03 | nem látszik (födémben); az ellenőrző képen vonalkázva | TERV SZERINT (x 3,77–9,80, y 4,05–8,05; panelszél ±10 cm) | a teljes látható mennyezet ebbe esik → nem fúrható |
| Fali lámpakiállás FL02 | ellenőrző képen | TERV SZERINT, 2,85 m (x 3,68, y 7,85) | – |
| TV-blokk, dugaljak (G01–G04 RJ45, G08 antenna, D15–D18) | ellenőrző képen; a TV-blokk 0,2–0,55 m-en jelölve | TERV SZERINT (x, y) | **magasság nincs a rajzon**; a ME-BAL-046 fotón a dugaljcsoport kb. 0,3–0,5 m-en látszik (becslés). Péter döntése: a TV helye szabad, csak dugalj kell (pl. D19 a déli falon). |
| Kapcsolóoszlop, termosztát, mozgásérzékelő (déli fal, x 7,15) | nem látszik (a kamera mögött van) | TERV SZERINT | nem takarható |
| Terasz | v2 tetőkert: gres (−15 cm), emelt WPC (+62 cm) lépcsőkkel, zöldtető, betonszegély, pálcás korlát | **ELŐZETES** (terv + videó) | K3: szintek, lépcső, szegély, zöldtető-magasság becslés |
| Kilátás | **nincs modellezve**: semleges ég, a horizont alatt szürke | – | a valós Budai-hegy és villanegyed képe: `02_referenciak/A902_helyszin/` – a stílusképekhez külön referenciaként kell megadni |
| Homlokzat kívül | fehér modellfal | – | a valóságban a teraszajtók kávája sötét klinker (ME-BAL-053); a Cam_02-ből alig látszik |
| Fény | borult, irány nélküli | – | nem a valós napállás és nem a valós fényviszony; a tónusok összehasonlításra szolgálnak |

## Cam_03 és Cam_04 (kiegészítő képek) – ami ott látszik és bizonytalan

**Cam_03 – étkező → konyha / előtér** (hely [4,70; 7,70; 1,50], 20 mm, KDK felé):
- Balra a teraszüvegfal; középen a keleti fal a 05.3 ajtajával (világosszürke lap, csukva); jobbra a WC-blokk fala és az előtér felé vezető átjáró a konyha 0,85 m-es alacsony falával. A konyha **üres**: a lakás konyhabútor nélkül került átadásra (K1: 85 cm-es pultköz).
- **BIZONYTALAN:** az előtér–nappali átjáró **2,10 m-es szemöldöke** a v1 brosúrából jön (a v2b-ben az egyetlen ELŐZETES / MÉRENDŐ elem).
  - Az átvételi összesítő szerint az előtérben álmennyezet van (min. 2,40 m), így a valós nyílásmagasság eltérhet.
- Az étkező ML04 „b” kiállása szintén a HF03 mezőben van (lásd fent).

**Cam_04 – master (05.1)** (hely [0,35; 4,30; 1,50], 20 mm, ÉK felé):
- Balra az északi fülke hátfala (y 8,95), középen a fülke keleti pillére (`Pillér_05_1_EK`), jobbra a nappalival közös válaszfal (x 3,57). Ezen a falon vannak az ágy két oldalának kiállásai (K13/D20/D21 y 7,51 körül, K14/D22/D23 y 5,24 körül, 65 cm-en).
- A 3,65 m-es nyugati üvegfal a kamera mögött van, nem látszik.
- **MODELLHIBA (javítandó):** a v2 tetőkert nyugati mellvédje (`v2_Mellved_Ny`, ELŐZETES) **belelóg a 05.1 északi fülkéjébe**.
  - Átfedés: x 2,83–3,02, y 8,50–8,95, a padló fölött 47 cm; a fülke pillérével és északi falával is átfed.
  - Az első Cam_04-renderen 47 cm-es fehér dobozként látszott. A referenciaképen **csak erre a kamerára rejtve** van.
  - A tetőkert-modellben a mellvéd déli vége ennél az x-nél legfeljebb a szerkezeti fal külső síkjáig (y ≈ 9,25) tarthat.
  - A Validator ezt nem fogja meg (a teraszelemeket csak változatlanságra nézi): érdemes egy „terasz ↔ belső tér átfedés” ellenőrzést felvenni.
- **MODELLHIBA (javítandó) 2:** a fülke hátfala (`Kulso_E_05_1_0`) x 2,95-ig tart, a v2b-ben áthelyezett pillér x 3,02-től. Így **7 cm-es rés** maradt a homlokzaton, amely a Cam_04-en fényrésként látszana. A referencián csak a renderhez lezárva. A homlokzat másik rése az előtér déli falán van (x 6,60–6,70). Részletek és javaslat: a Validator-riport.
- A falon maradt `Z_tapeta_greige` a fülke hátfalán (`Kulso_E_05_1_0`) is fehérre javítva.


## Mi kell a PASS-hoz (helyszíni mérés és fotó)

1. **Egy fotó pontosan a Cam_02 helyéről.**
   - Hely: a konyha 85 cm magas alacsony falának északi végétől (ahol az előtérből a nappaliba lépsz) 35 cm-re a nappali felé és 5 cm-re nyugatra; 1,55 m magasan.
   - Irány: nyugat felé, 41°-kal észak felé elfordítva – gyakorlatilag a nappali ÉNy-i sarkára (a nyugati válaszfal és az üvegfal melletti falcsonk találkozására).
   - Telefon 0,5× (ultraszéles) objektívvel, vízszintesen. Ezzel a referencia és a valóság közvetlenül összevethető.
2. **Teraszüvegezés:** a mezők szélessége, osztás vagy pillér, nyitásirány, küszöb és fellépés magassága (ME-BAL-045 nézet).
3. **Padló:**
   - deszkaszélesség és -hossz, fektetési irány nappaliban, étkezőben és masterben;
   - dekorcímke vagy szállítólevél a kóddal.
4. **Fali kiállások magassága:** TV-blokk, D15–D18, FL02; ML05 és ML04 helye.
5. **Nyugati válaszfal anyaga:** tégla, gipszkarton vagy egyéb. Kopogtatás és fotó a dugaljnyílásnál.
6. **Kilátás:** egy fotó a Cam_02 irányában, nyitott függönnyel, 1,55 m magasról.

## Viszony a PR #7 alapképeihez (`04_renderek/A902_alap_v2b/`, a `main`-ben 14:25 óta)
Egy párhuzamos Claude-munkamenet ugyanebből a v2b fájlból bútor nélküli alapképeket készített (PR #7, EEVEE, Péter jóváhagyásával beolvasztva). A PR #7 a .blend-be csak egy renderben rejtett kiállás-réteget tett, a geometria azonos. Eltérések:
- A PR #7 Cam_02-képén a **nyugati válaszfal halványan bézs**. Ennek oka nem a padlóról visszaverődő fény, hanem a v2b fájlban a falon maradt `Z_tapeta_greige` (Zenit-tapéta) anyag. Ez a Gate szerint falszínhiba.
  - Itt a fal fehérre javítva.
- Itt a padlón deszkaminta és 4V horony van (közelítés), valamint 6 cm-es szegőléc; a PR #7-ben sík tónus.
- Itt nincs fekete folt a profilcsatlakozásoknál, és van ellenőrző rárajzolás és felülnézet a látómezővel.
- A PR #7 kiállás-rétege (a Blender-fájlban) ettől független és hasznos.
- **Javaslat:** az összehasonlító stílusképek alapja egyetlen képkészlet legyen. Péter dönt.

## Hogyan használd (Astra / képgenerálás)

- **1. kép:** `A902_semlegesv2b_1_nappali.png` – csak geometria és kamera. A semleges ég és a szürke talaj **helykitöltő**, nem kilátás.
- **Padló anyaga:** ME-BAL-080 fotó.
- **Falszín, ajtószín, terasz anyagai:** ME-BAL-045 fotó.
- **Kilátás:** `02_referenciak/A902_helyszin/`.
- **Bútor:** nincs a képen. Az elrendezést a stílus elrendezés-táblázata alapján Claude tömegmodellezi, és arról külön referenciakép készül.

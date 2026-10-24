# A-902 – bútor nélküli kameraalapok a KEP-004 képfázishoz (v2b-1-k10) · Render Reality Card (2026-10-24)

**Azonosító:** `A902-ALAP-V2B1-20261024` · **Cél:** a négyhelyiséges, tízstílusos képfázis (`WSG-20261024-STYLE10-KEP-004`) hiteles „image 1” bemenetei. Nem látványterv.
**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES` (helyszínen nem mért, ±5 cm; a hétfői, 2026-10-26-i mérés után újrafuttatható).
**Készítette:** Claude, Péter 2026-10-24 21:33-as engedélyével. A régi alapképek (`04_renderek/A902_alap_v2b/`, `semleges_v2b/`) változatlanul megmaradnak.

## Képek

| Fájl | Kamera (lock v2b-1-k10) | Beállítás | Változás a v2b alapképhez képest |
|---|---|---|---|
| `A902_Alap-v2b1_blender_02_nappali-terasz.png` | Cam_02 · [8,30; 4,40; 1,55] · [1,479; 0; 0,858] · 20 mm | EEVEE, egyszínű égbolt 0,86/0,88/0,92, AgX MHC, exp. +0,75 (a v2b-vel azonos) | **pixelre azonos** (átl. eltérés 0,10/255, 0 pixel > 25) – a v2b-1 javítás nem látszik ebből a nézetből |
| `A902_Alap-v2b1_blender_03_etkezo-konyha.png` | Cam_03 · [4,70; 7,70; 1,50] · [1,493; 0; −2,111] · 20 mm | ua. | **pixelre azonos** |
| `A902_Alap-v2b1_blender_04_master.png` | Cam_04 · [0,35; 4,30; 1,50] · [1,434; 0; −0,745] · 20 mm | ua. | 0,11% pixel változott – a 05.1 északi fülkéjénél (v2b-1 homlokzati/mellvéd-javítás); várt változás |
| `A902_Alap-v2b1_blender_10_furdo-06-2.png` | **Cam_10_Furdo_06_2 · [14,50; 6,62; 1,50] · [1,38; 0; −1,5708] · 16 mm** | **Cycles** 128 minta + denoise, AgX MHC, exp. −0,3; **ablaktalan → csak műfény** a meglévő ML10 mennyezeti ponton (~4000 K), világ 0, nappali fény nincs | új; nézet az ajtónyílásból kelet felé – a helyszíni ME-BAL-064 fotóval egyező irány |

Cam_02/03/04: kameraparaméterek változatlanok (a lockkal egyeznek), így **Astra V2 promptjaiban ezekre nincs teendő.**

## Cam_10 – lényeges változás a V3.1 sablon ideiglenes kamerájához képest (külön jelezve)

- A V3.1 sablon §0/§2 *javasolt* Cam_10-e ([14,75; 5,45; 1,55], [1,48; 0; −0,456], 20 mm) **geometriailag érvénytelen**: a pont a WC-csésze befoglalójába esett (ellenőrző kép: `ellenorzes_Cam10_v31_ideiglenes_kamera_WC-ben.png`).
- **Rögzített Cam_10:** [14,50; 6,62; 1,50], [1,38; 0; −1,5708], **16 mm** (a 1,93 × 2,85 m-es térben 20 mm-rel a padló és a zuhany nem fér a képbe), 36×24 AUTO, clip 0,1–200, 1600×1000. A lockban (`cameras.Cam_10_Furdo_06_2`) és a .blend-ben.
- A V3.1 sablont és Astra V2 promptfájlját **nem módosítottam**; a képfázis előtt a Cam_10 fix blokkot a `05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md` szerint kell behelyettesíteni.

## Geometria (lock v2b-1-k10)

- **Új fal:** `Akna_06_2_EK_v2b1k10` [15,45; 5,20; 0; 16,40; 5,81; 2,90] – a 06.2 DK-i sarkába benyúló akna/falblokk a KORR 2 alaprajz (18. o.) és a burkolatkiosztási terv (23. o.) szerint; a v2b téglalapnak vette a fürdőt. A Kémeri-fotó (`ellenorzes_helyszini_foto_Kemeri_20261021_145104_06-2.jpg`, bal oldalt a felénk jövő falsík) megerősíti.
- `rooms.furdo_06_2` → L alak (WC-fülke DNy-on). Nyílások változatlanok.
- **Validator v2** (`03_blender/validator_v2b1_kam10_*.json`): üres állapot **PASS 0/0**; LOCK 61 fal / 54 nyílás / 17 padló 0 eltérés, terasz 0 változás, 10 kamera, villamos takarás 0. A szaniterekkel futtatva 6 ütközés – mind a modell régi, egyszerűsített szaniter-tömbjei (pl. a 06.2 mosdótömb 10 cm-rel a külső falba lóg, a 06.1 törölközőszárító 3 cm-rel); ezeket a 06.2 renderen a terv szerinti render-réteg váltja.

## 06.2 – mi látszik és honnan (részletek: `ai-coordination/inputs/A902_v2b/FURDO_06_2_BEEPITETT_ALLAPOT.md`)

| Elem | A képen | Forrás | Státusz |
|---|---|---|---|
| Padló + falak | Geostone Grigio 60×60 matt, Holdfény fuga, 2,85 m-ig, felette fehér; kiosztás a 23. o. tengelyei szerint | költségvetés + 23. o. + fotó | közelítő eljárásos anyag (szín, rétegzett erezet) – **az anyaghűséget a fotó (image 2) adja** |
| Dekor | Geo Esagonetta Grigio 3D 30×60 a zuhany hátfalán (bal oldali fal) és a WC-előtétfal felett | ua. | a hatszög-domborzat közelítő |
| Zuhany | 5/5 padka alu élvédővel, burkolt padló, 70 cm-es folyóka a K-i fal mentén, **üvegfal nincs** | 18. o. + fotó | ✔ |
| Szerelvények | Cubeo süllyesztett keverő, Cube 250 fejzuhany karral, Tempesta csatlakozó, SmartActive 130 Cube kézizuhany – fekete | költségvetés + fotó | helyük a tervből/fotóból, magasság ±10 cm |
| Mosdó | Smyle Square 60×48 + Cubeo M fekete, tengely y 6,63 | költségvetés + 18. o. | egyszerűsített tömb |
| WC, előtétfal, törölközőszárító | modellezve (fülkében), a Cam_10 nézetből nem látszanak | 18. o. + fotó 145104 | ✔ |
| Tükör | nincs (átadáskor nem volt) | fotó | stílus adja hozzá |
| Fény | csak műfény ML10 | 18. o. „f” pont | ✔ |

## Nem változott

Fehér falak (fürdőn kívül), EL2184 padló, fehér belső profilok, ajtók, terasz, kiállás-réteg (rejtve). Az élő Mac-fájlhoz (`~/Downloads/WSG_A902_stilusok.blend`, nem mentett változásokkal nyitva) nem nyúltam; minden futás külön háttér-Blender folyamatban, munkamásolaton (`~/Downloads/WSG/_claude_kep004_alap_20261024/`).

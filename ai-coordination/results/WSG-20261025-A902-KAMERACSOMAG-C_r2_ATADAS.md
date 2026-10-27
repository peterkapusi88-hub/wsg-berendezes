# A-902 kameracsomag C – r2 átadás a verseny-baseline frissítéséhez (Claude, 2026-10-25 04:50 CET)

**Kinek:** a párhuzamos Claude-munkamenet, amely a `competition/baseline-20261025-v2` (a8ab8d3) baseline-t és a PR #19 közös blokkját viszi. Péter 04:49: a baseline-t a PR #20 végső állapotából frissíti.

**Mi ez:** a PR #20 végső eredményei, Péter 04:39, 04:40 és 04:49 CET döntései szerint. A PR #19-be és a baseline-ba ez a munkamenet nem írt.

**Nem engedély:** merge, képgenerálás.

## 1. Eredmények a PR #20-ban (az r1 óta új)
| Téma | Eredmény | Fájl |
|---|---|---|
| Fénycsere (Péter 04:40/04:49) | **Cam_02 = kék óra / kora este, prémium rétegzett Hue (2200–2700 K, RGB nélkül), a TV-fal a WOW-elem, a terasz felismerhető, nem túl sötét vagy kontrasztos. Cam_12 v3 = nappali, világos luxusenteriőr-összehasonlítás. Cam_03 K1 = nappal.** A Cam_04, Cam_11, Cam_10 változatlan. A kamerák geometriája és a `kep_id` változatlan; a semleges Blender-alapképek maradnak a geometriai kontroll. | `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md` 3. pont |
| A Cam_12 v3 és a TV-fal | **A Cam_12 v3 (x 4,40) a TV-falat (x ≤ 4,27) egyáltalán nem látja.** A falsík a kamera mögött, a képen kívül van, ellenőrizve. Ezért a TV-fal északi vége is szabadon tervezhető, mennyezetig érő szekrénnyel is; nem kell „kamerakorlátként” sem tiltani. Csak a kamera állóhelye marad szabadon (x 4,30–4,50; y 7,75–8,05). Ha egy terv más nézőpontot kíván, Claude második hero kamerát vizsgál. | GEOMETRIA v2 3. pont |
| Kerek asztal – Blender-méretpróba | Ø150 (Nealy) csak sík TV-fallal (≤ 4 cm) és a kanapé legnyugatibb helyén (L x 6,11 / U x 5,91) fér el; az ML04 0,31–0,41 m-re oldalt. Ø140 sík TV-fallal. Ø130 40 cm-es TV-bútorral U-val (ML04 0,21). 60 cm-es TV-szekrénnyel a Ø150 nem fér el. Validátor: PASS 0 hiba. A nyugatra tolt U a Cam_12 előterébe kerül → második hero kamera kell. | `03_blender/geometry_v2/elrendezes_C/c_kerek.py`, `c_kerek2.py`; `cam12_C/05_kerek_meretproba.py`; `04_renderek/A902_kameracsomag_C/A902_kerek_asztal_meretproba_kontakt.jpg`; `03_blender/validator_v2b1k13_kerek_*.json` |
| S02 asztal | A 160 × 90-es helyre bármely 160 × 90-es asztal mindkét kanapéval megfelel (az északi kihúzás függönnyel 0,93 m). Az Anouk étkezőasztalként csak 180 × 90-ben létezik. **Jelöltek** (a magyar ár és a szállítás ellenőrizendő): Westwing Toni 160 (259 990 Ft, 2026-10-25); Kave Home Kesia 160 (220) × 90, bővíthető, dió/fekete; Westwing/KARE Artistico márvány 160 × 90 (kockatalp); Kave Home Argo 160 × 90 | – |
| Teraszajtó, keleti szárny | 96 hatszemélyes eset: ha csak a legkeletibb, 0,93 m-es szárny nyílik, egyik sem tartja meg egyszerre a terasz elérését és minden fő utat. Lehetőségek, mind kompromisszum: 5+1; 3+3 (180-as asztal, a 05.3 felé 0,65–0,70 m); bővíthető asztal. Hétfőn ellenőrizendő. | `elrendezes_C/c_keleti_szarny.py` (.json) |
| Validátor-nyilvántartás | a régi 6 szaniterhiba (06.1/06.2) és a C-figyelmeztetések (D16, D17, D18, G01–G04, G08) külön dokumentálva | `03_blender/validator_nyilvantartas_A902_kameracsomag_C.md` |

## 2. Eltérések a baseline v2 (a8ab8d3) és a PR #20 között – a baseline-ban javítandó
1. **§0.1 CAM_12:** „a TV-fal északi végén (y 7,65–8,05) a mennyezetig érő szekrény tilalma csak kamerahelyből ered”.
   - A v3 kamera a TV-falat nem látja, ezért ez a tilalom sem kell.
   - Csere: „A Cam_12 v3 a TV-falat nem látja; a TV-fal, az északi vége is, szabadon tervezhető. Csak a kamera állóhelyét (x 4,30–4,50; y 7,75–8,05) hagyd szabadon; más nézőponthoz Claude második hero kamerát vizsgál.”
2. **Fény – hiányzik a §0-ból és a kalibrációból:**
   - a §0-ba kell egy KAMERÁK ÉS FÉNY pont (a fenti 1. sor szövege), amely felülírja az r2 brief §11.6 fénytábláját;
   - a §0.6 képsorrend: „minden stílus Cam_12 (nappal), majd Cam_02 (kék óra)”;
   - a három indítóprompt kameránkénti fénymondatai ennek megfelelően cserélendők.
3. **Kalibráció, 61. és 64. prompt (Cam_02)** – a baseline-ban még „daylight, geometric control view” szerepel. Javasolt angol szöveg, ezen a munkameneten belül próbaként megírva:
   - fejléc: `· blue hour / early evening with premium layered Hue lighting – the TV wall is the WOW element.`;
   - a fénymondat helyett: `Blue hour / early evening: the sky above the Buda hills deep blue with a last warm band at the horizon, the first city lights on; the interior lit by layered Philips Hue light at 2200–2700 K, no RGB colours. The image must not be dark or contrasty: wall edges, openings, the floor–wall line, the terrace deck, railing and green roof remain clearly readable; mid-key exposure, no crushed blacks, no blown highlights, soft natural fall-off, neutral-warm white balance.`;
   - a „In this daylight view the strips are off…” mondat helyett: `In this blue-hour view every Hue layer is on and carries the TV wall: the hidden lines … glow evenly from their opal profiles (no visible LED dots); the pendants are dimmed warm. Light comes only from the named fixtures; forms and materials stay readable.`;
   - a C1 „STYLE DNA … brought into daylight” → „… at the blue hour”;
   - a README fény oszlopa: 61, 64 = kék óra / este, Hue.
4. **Kalibrációs térrend (61. és 64.):** a „sofa … with its back towards the terrace glazing” hibás. A C-ben a kanapé háttal keletre, az étkező felé áll, a hosszú ülés észak–déli, nyitott a TV felé, az északi vége szabadon hagyja az üveget.
5. **Kalibrációs termékek:**
   - „Kave Home Nealy oval 160 × 90” nem azonosítható: a Nealy Ø150 kerek és 200/240 × 100-as téglalap. Javaslat: Westwing Toni 160 × 90.
   - **Gala 300 × 225 (C2):** a C-ben 40 cm-es TV-bútorral a 2,25 m-es kar 0,60 m alá kerül → nem fér el, csak ≤ 15 cm-es TV-fal-elemmel szemben. Javaslat: Westwing Wolke L 258 × 167 (25WES29958, 1 050 000 Ft, 2026-10-24), az eredeti Lake Forest-kanapé.
   - **Martina (C1):** a mélysége nem igazolt.
6. **A baseline a PR #20-at 51a1c8d-n emelte be (209517c).** A végső PR #20 commitot (2. pont) újra be kell emelni.

## 3. Nyitott feltételek (hétfő 2026-10-26, helyszín)
- **Teraszajtó:** melyik szárny nyílik – a hat hely és a terasz együtt addig NEM igazolt.
- **Káva mélysége:** a függönysínhez kell; a 0,93 m-es kihúzás behúzott függönnyel, becsült 12 cm-es sávval.
- **TV-csatlakozók tényleges helye:** G01–G04 (a doboz a rajzon bizonytalan).
- **Parketta dekorja:** NEM IGAZOLT.
- **Fürdő 06.2:** a szaniterek mérése.
- **S02:** 160 × 90-es asztal választása, magyar ár.
- **Kerek asztal:** csak a választott stílus TV-fal-mélységével és kanapéjával, külön méretpróbával fogadható el.

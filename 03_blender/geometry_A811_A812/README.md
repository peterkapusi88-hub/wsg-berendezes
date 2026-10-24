# A-811 és A-812 – Blender-alapmodell (geometria v1, ELŐZETES) – 2026-10-24

**Státusz:** `TERV SZERINT – ELŐZETES`. A vektoros méretezett alaprajzból készült, **helyszínen nem mért**. A falsíkok vakolatlan tervsíkok, a kész falsík oldalanként ~1–2 cm-rel beljebb lehet. A végleges változat a hétfői (2026-10-27) helyszíni mérés és fotók után, Péter jóváhagyásával készül.

| | A-811 | A-812 |
|---|---|---|
| Modell | `03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend` | `03_blender/WSG_A812_alaprajz_ELOZETES_20261024.blend` |
| Lock (validátor v2) | `03_blender/geometry_lock_A811.json` | `03_blender/geometry_lock_A812.json` |
| Geometria-adat | `A811_geometria_ELOZETES.json` | `A812_geometria_ELOZETES.json` |
| Ellenőrző kép (terv + modell) | `A811_geometria_ellenorzes.png` | `A812_geometria_ellenorzes.png` |
| Forrásrajz | 5. old., 1:50, M1 (KORR nem készült) | 12. old., 1:100, M1 KORR (2026.04.28.) |
| Belmagasság a modellben | 2,70 m (Kémeri: 2,69–2,72) | 2,70 m (Kémeri: 2,69–2,73) |
| Validátor v2 | PASS – LOCK 0, ERKÉLY 0, kamera rendben | PASS – ua. |
| Alapképek | `04_renderek/A811_alap_v1/` | `04_renderek/A812_alap_v1/` |

## Mi van a modellben
- **Falak, pillérek, aknák** (`<lakás>_Falak`): 43 és 45 falelem, 2 és 5 gépészeti akna (tömör tömb). A homlokzati pilléreken az erkély felé a hőszigetelés is.
- **Szemöldök** minden ajtó (2,10 m) és üvegfal (2,57 m) fölött; mennyezet 2,70-en (`Plafon_*`).
- **Beltéri ajtók** (`<lakás>_Nyilaszarok`): tok és csukott lap, a terv szerinti nyílásban. A szín az A-902 fotója alapján feltételezett: világosszürke lap, szürke tok, belül fehér bejárati ajtó.
- **Homlokzati üvegfalak**:
  - alsó és felső tok, a profilok (tömör sávok az üvegtáblák között), üvegtáblák a rajzi tokvonalakból;
  - a nyíló szárnyak nyitási negyedköre a lockban (`openings_meta`);
  - anyag: belül fehér profil, az A-902-ével azonos.
- **Padló helyiségenként** (`<lakás>_Padlo`):
  - parketta: Egger Grey Soria Oak EL2065 (burkolatkiosztási terv); a tónus BECSLÉS, meleg szürke;
  - kerámia a fürdőkben, a WC-ben és a HTH-ban: Glitch Salt 60×60;
  - padló az ajtónyílásokban (küszöb) és az ablakmélyedésben is.
- **Erkély** (`<lakás>_Erkely_ELOZETES`):
  - lemez a rajzi erkélykontúrból;
  - feltételezett −0,15 m-es szint;
  - 1,10 m-es pálcás korlát, az A-902 tetőterasz-korlátjához hasonló;
  - a szomszéd erkély felé osztó.
  - **Szint, korláttípus és osztómagasság NEM IGAZOLT.**
- **Kamerák:** Cam_02 nappali → erkélyüveg, Cam_03 ablak felől → étkező/konyha, Cam_04 fő háló, Cam_05 második háló. Mind 20 mm, z 1,5 m, mint az A-902-ben. Felülnézet: Cam_01, Cam_06.
- **Kiállás-réteg** (`<lakás>_Villamos_TERV`, renderben rejtve):
  - minden kiállás azonosítóval, a `01_alaprajzok/villamos_kiallasok/<lakás>_villamos.json` szerint;
  - a hűtő-fűtő mezők kerettel és átlóval;
  - a doboz nélküli jelek a legközelebbi falsíkra illesztve, az eredeti pont a jelölő `x_terv`/`y_terv` tulajdonságában.
  - Ellenőrzés: `<lakás>_kiallas_reteg_ellenorzes.json`.
- **Render-beállítás:** semleges, mint az A-902 alapképein. EEVEE sugárkövetéssel, AgX Medium High Contrast, +0,75 expozíció, egyszínű égbolt, nap és lámpa nélkül.

**Nincs a modellben:** bútor, konyha (a lakások konyhabútor nélkül kerültek átadásra), szaniter (kád, zuhany, WC, mosdó), fürdőszobai előtétfalak, álmennyezet, redőnytok, a kilátás és a felettük lévő szerkezet (az erkély fölött égbolt).

## Ellenőrzés a tervvel
**Helyiség-területek** a 8. emeleti megvalósulási terv (2. old., 1:125, 2026.05.20.) m²-ével. A 2. oldalt vonal-korrelációval illesztettük a lakáslapokhoz, a két lakás x-e közös, és y_A812 = y_A811 − 11,85: az A-811 felső fala az A-812 alsó fala. A terv a homlokzati szobák területébe az üvegfal tokjáig tartó ~20 cm-es ablakmélyedést is beszámítja, ezért a modell is így számol.

| A-811 | terv m² | modell m² | + ablakmélyedés | eltérés |
|---|---|---|---|---|
| Nappali+étkező | 30,93 | 30,23 | 30,96 | +0,03 |
| Konyha | 5,80 | 5,82 | 5,82 | +0,02 |
| Előtér | 4,04 | 4,06 | 4,06 | +0,02 |
| Közlekedő | 5,30 | 5,29 | 5,29 | −0,01 |
| Szoba 05.2-3 (gardróbbal) | 18,74 | 18,38 | 18,75 | +0,01 |
| Szoba 05.1 | 13,33 | 12,98 | 13,31 | −0,02 |
| Fürdő 06.2 | 3,82 | 4,26 | 4,26 | +0,44 * |
| Fürdő 06.1 | 4,77 | 4,95 | 4,95 | +0,18 * |
| HTH 09 | 2,48 | 2,45 | 2,45 | −0,03 |
| WC 08 | 1,47 | 1,65 | 1,65 | +0,18 * |

| A-812 | terv m² | modell m² | + ablakmélyedés | eltérés |
|---|---|---|---|---|
| Nappali+étkező | 33,85 | 33,12 | 33,85 | 0,00 |
| Konyha | 6,35 | 6,35 | 6,35 | 0,00 |
| Előtér | 1,78 | 1,79 | 1,79 | +0,01 |
| Közlekedő | 8,63 | 8,63 | 8,63 | 0,00 |
| Közlekedő gardrób része | 1,48 | 1,39 | 1,39 | −0,09 |
| Szoba 05.1 | 8,15 | 7,96 | 8,14 | −0,01 |
| Szoba 05.2 | 9,50 | 8,99 | 9,56 | +0,06 |
| Gardrób 10.2 | 3,21 | 3,14 | 3,14 | −0,07 |
| Szoba 05.3 (+10.3 gardrób) | 16,97 | 16,42 | 16,98 | +0,01 |
| Fürdő 06.2 | 4,31 | 4,77 | 4,77 | +0,46 * |
| HTH 06.1 | 3,45 | 3,62 | 3,62 | +0,17 * |
| Fürdő 08/09 | 4,37 | 4,62 | 4,62 | +0,25 * |

\* A fürdők terve a WC/mosdó előtétfalát (~15–20 cm) levonja; a modellben ez nincs benne. A lakó- és hálóhelyiségek ±0,1 m²-en belül egyeznek.

**Méretszámok a rajzról** (a modell falsíkjai között mérve):
- **A-811:**
  - nappali 6,17 × 4,90 ✓;
  - konyha 2,08 × 3,00 ✓;
  - 05.2-3: 3,22 + 1,70 (gardrób), 5,02, mélysége 2,70 ✓;
  - 05.1 4,42 × 2,70, fülke 0,67 ✓;
  - közlekedő 1,05 ✓;
  - 06.2 1,98 × 2,15 ✓, 06.1 1,98 × 2,50 ✓;
  - HTH 1,65 × 1,49 (rajz: 1,50), WC 0,95 × 1,74 (rajz: 1,75);
  - üvegfalak 3,65 / 3,65 ✓.
  - Az előtér 1,625-ös méretszáma a 8,325-ös síkig mér. A konyha felőli falon az „EL4” elosztó ~12 cm-es beépítése lehet, ez nincs modellezve.
- **A-812:**
  - nappali 3,89 / 7,22 / 5,60 / 4,70 / 5,80 ✓;
  - konyha 2,45 × 2,80 ✓;
  - 05.1 2,75 × 3,09 ✓, 05.2 2,75 × 3,24 ✓;
  - 10.2 2,75 × 1,30 ✓;
  - 05.3 3,10 × 4,09 ✓;
  - közlekedő 1,05 × 7,93 ✓;
  - 06.1 1,40 × 2,83 ✓, 08/09 1,40 × 3,30 ✓;
  - 06.2 2,20 ✓; a 2,29⁵ az előtétfalig mér;
  - ablakok 3,65 / 0,905 / 2,875 / 2,80 ✓.

## Feltételezések és nyitott pontok (hétfőn ellenőrizendő)
1. **Falsíkok, nyílások, belmagasság:** helyszíni mérés (lézer), legalább a nappali, a háló és az üvegfalak.
2. **Erkély:** a padló szintje az előszobapadlóhoz képest, a korlát típusa és magassága, a szomszéd felőli osztó, a lemez széle. Az A-812 erkélyének bal széle a 12. oldalon nincs kirajzolva; az A-811-ével azonos x −2,035 feltételezve.
3. **A-812 hálószobák padlóig érő nyíló ablakai:** francia erkély korlátja a rajzon nincs. Ha van, a képekre is kell.
4. **Mennyezeti lámpakiállás a hűtő-fűtő mezőben:** a lámparögzítés előtt hőkamerával, fűtési üzemben ellenőrizendő, mint az A-902-ben.
   - A-811: ML02–ML07 és ML09 (konyha, nappali, mindkét háló, gardrób).
   - A-812: ML03–ML08, ML17, ML18 (nappali-étkező, mindhárom háló, gardróbok).
5. **Álmennyezet:**
   - A-811: a WC-ben 2,40 m (rajz); Péter összesítője szerint az előtérben és a fürdőkben is van (min. 2,40).
   - A-812: az előtérben 2,50 m, a konyha sarkában 2,45 m (rajz).
   - A kiterjedése nem igazolt, a modellben nincs. A kiállás-réteg ezeken a helyeken a lámpajelölőt álmennyezet-magasságba teszi.
6. **Tájolás** (a rajz É-jele alapján, tájékoztató): a homlokzati üvegfal (−x) ≈ ÉNy felé néz, a rajz +y iránya ≈ ÉK.
7. **Parketta-tónus:** BECSLÉS (Egger: „meleg szürke”), helyszíni fotóval pontosítandó.

## Újrafuttatás
```
python3 a8_geometria.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf     # geometria-JSON (a PDF nincs a repóban)
python3 a8_ellenorzo_kep.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf # ellenőrző kép
WSG_KEZI_FUTTATAS=1 WSG_LAKAS=A811 python3 -c "import sys,bpy; sys.argv=['x','<repo>']; exec(open('build_a8_modell.py').read())"
WSG_LOCK=03_blender/geometry_lock_A811.json WSG_VILLAMOS=01_alaprajzok/villamos_kiallasok/A811_villamos.json python3 -c "import bpy,runpy; bpy.ops.wm.open_mainfile(filepath='03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend'); runpy.run_path('03_blender/geometry_validator_v2.py')"
WSG_KEZI_FUTTATAS=1 <Blender> -b WSG_A811_alaprajz_ELOZETES_20261024.blend --python render_alapkepek_a8.py -- <kimenet>
python3 alapkep_utomunka_a8.py <render-kimenet> <repo>
```
`pdf_kinyeres/ivek.py`: az ajtó-nyitásívek kinyerése, a zsanért és a sugarat adja.

**A validátor v2 bővítése:**
- A lock `gyujtemeny_elotag` kulcsa választja ki a lakást.
- Az A-811/A-812-ben a tetőkert helyett az erkélyt ellenőrzi.
- A nyíló ablakszárnynál csak a nyitási negyedkört vizsgálja.
- A konyha- és a 05.2-ágyvizsgálat csak az A-902-ben fut.
- Az A-902 eredménye változatlan, regressziós próbával ellenőrizve: FAIL 89 / 82, a hibalista azonos.

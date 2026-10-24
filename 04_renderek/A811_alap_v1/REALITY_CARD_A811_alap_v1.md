# A-811 – bútor nélküli alapképek az alaprajzi modellből · Render Reality Card (2026-10-24)

**Azonosító:** `A811-ALAP-V1-20261024` · **Cél:** az Astra-féle B fázis (azonos kamerás stílusképek) geometriai alapja az A-811-hez. Nem látványterv.

**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Nem PASS, mert:
- a padló dekorja nem igazolt;
- a falsík a hétfői helyszíni mérésig terv szerinti;
- az erkély szintje és korlátja feltételezés.

## Bemenet és beállítás
| | |
|---|---|
| Modell | `03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend`. Forrás: a méretezett terv (5. old., 1:50, M1) vektoros falvonalai. Lock: `geometry_lock_A811.json`. Validátor v2: PASS (LOCK 0, ERKÉLY 0, kamera rendben). Leírás: `03_blender/geometry_A811_A812/README.md`. |
| Szkript | `03_blender/geometry_A811_A812/render_alapkepek_a8.py`. Csak a betöltött példányon módosít, nem ment. Utómunka (metaadat törlése, felülnézeti feliratok): `alapkep_utomunka_a8.py`. |
| Render | Blender 5.2.3, EEVEE sugárkövetéssel, 1600 × 1000, AgX + Medium High Contrast, expozíció +0,75. Ugyanaz a „semleges” beállítás, mint az A-902 v2b alapképein. Háttér-Blender a Macen; az élő `WSG_A902_stilusok.blend`-hez nem nyúlt. |
| Fény | Egyenletes, szórt nappali fény: egyszínű égbolt, 0,86/0,88/0,92, erősség 1,0. Nincs nap, mert az iránya nem igazolt; a rajz É-jele szerint az üvegfal ≈ ÉNy felé néz. Belső lámpa nincs. |
| Rejtve | A kiállás-réteg. Bútor, konyha és szaniter nincs a modellben. |
| Kamerák | 20 mm, z 1,5 m:<br>• Cam_02_Nappali_erkely (nappali → erkélyüveg);<br>• Cam_03_Etkezo_konyha (ablak felől → étkező, konyha);<br>• Cam_04_Haloszoba (05.2-3: ágyfal + üvegfal);<br>• Cam_05_Haloszoba_05_1. |

## Felületek – kamera szerint
| Felület | Cam_02 nappali → erkély | Cam_03 étkező → konyha | Cam_04 háló 05.2-3 | Cam_05 háló 05.1 | Státusz |
|---|---|---|---|---|---|
| Padló | meleg szürke sík tónus, sRGB ~152/150/148 | ~149/147/145 | ~151/149/146 | ~149/147/145 | Egger Grey Soria Oak EL2065 a burkolatkiosztási terv szerint. **Deszkaminta nincs modellezve, a tónus BECSLÉS** (nincs helyszíni fotó). |
| Falak | fehér, ~211/212/213 | ~210/211/212 | ~212/213/214 | ~212/213/214 | MEGLÉVŐ fehér festés |
| Mennyezet | fehér | fehér | fehér | fehér | MEGLÉVŐ; a hűtő-fűtő mező nem látszik (a kiállás-rétegben van) |
| Homlokzati üvegfal | 3,65 × 2,57 m:<br>• egyszárnyú erkélyajtó;<br>• beton oszlop;<br>• fix mező;<br>• kétszárnyú erkélyajtó.<br>Belül fehér profil. | – | 3,65 m-es elem 05.2-3 része, erkélyajtóval | 05.1 erkélyajtó + fix mező | TERV SZERINT (rajz); a profil színe a GOAL szerint IGAZOLT-F (belül fehér) |
| Beltéri ajtó | – | bejárati ajtó a háttérben, belül fehér | – | – | TERV SZERINT; a beltéri ajtók színe az A-902 fotója alapján feltételezett |
| Konyha | – | **nincs konyhabútor** (átadás konyha nélkül); a pengefal megszűnt, a konyha nyitott | – | – | TERV SZERINT (M1 vevői módosítás) |
| Erkély | lemez + pálcás korlát | – | korlát látszik | korlát látszik | **ELŐZETES**: a kontúr a rajzból; szint (−0,15), korláttípus és magasság (1,10) NEM IGAZOLT |
| Kilátás | **nincs modellezve** – egyszínű világos égbolt | – | ua. | ua. | a valós kilátás csak helyszíni fotóból; generikus skyline tilos |

## Képek
- `A811_Alap-v1_blender_02_nappali-erkely.png`
- `A811_Alap-v1_blender_03_etkezo-konyha.png`
- `A811_Alap-v1_blender_04_haloszoba.png`
- `A811_Alap-v1_blender_05_haloszoba-2.png`
- `A811_Alap-v1_blender_06_alaprajz-kiallasok.png`: **ellenőrző felülnézet, nem Astrának szól.** Workbench, 1 m-es rács, rajta a 115 kiállás és az 5 hűtő-fűtő mező. Az x/y koordináták megegyeznek a `01_alaprajzok/villamos_kiallasok/A811_villamos.csv` értékeivel.
- `render_log_A811.json`: a futás pontos beállításai.

## Astrának – a B fázis promptjában kötelező
- Őrizze meg:
  - a falakat, az üvegfal osztását és a nyílásokat;
  - a kamera nézetét;
  - a padló meleg szürke tónusát. A padló meglévő szürke tölgy parketta (Egger Grey Soria Oak), nem beton és nem mikrocement.
- Új elem csak a reality card és a tételes lista szerint kerülhet a képre. Lámpa csak a mennyezeti kiállás helyére, kiállás-azonosítóval.
- A konyha üres. Konyhabútor csak a stílusterv tételeként jelenhet meg, méretezve.
- Az erkély korlátja feltételezés. Ha a stílusképen fontos, maradjon semleges, és ne találjon ki üveg- vagy kőkorlátot.
- A kilátás valós forrásból jöjjön, ne kitalált.

## Észrevétel a kiállás-rétegből – tervezést érinti
**Hűtő-fűtő mezőn belül van** a konyha, a nappali, mindkét háló és a gardrób mennyezeti lámpakiállása: **ML02–ML07 és ML09**. A lámpa rögzítése előtt hőkamerával, fűtési üzemben ellenőrizendő, mint az A-902-ben. **Hétfőn ellenőrizendő.**

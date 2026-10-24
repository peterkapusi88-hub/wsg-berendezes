# A-812 – bútor nélküli alapképek az alaprajzi modellből · Render Reality Card (2026-10-24)

**Azonosító:** `A812-ALAP-V1-20261024` · **Cél:** az Astra-féle B fázis (azonos kamerás stílusképek) geometriai alapja az A-812-höz. Nem látványterv.

**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Nem PASS, mert:
- a padló dekorja nem igazolt;
- a falsík a hétfői helyszíni mérésig terv szerinti;
- az erkély és a hálószobai francia erkély korlátja nem igazolt.

## Bemenet és beállítás
| | |
|---|---|
| Modell | `03_blender/WSG_A812_alaprajz_ELOZETES_20261024.blend`. Forrás: a méretezett terv (12. old., 1:100, M1 KORR 2026.04.28.) vektoros falvonalai. Lock: `geometry_lock_A812.json`. Validátor v2: PASS (LOCK 0, ERKÉLY 0, kamera rendben). Leírás: `03_blender/geometry_A811_A812/README.md`. |
| Szkript | `03_blender/geometry_A811_A812/render_alapkepek_a8.py`. Csak a betöltött példányon módosít, nem ment. Utómunka: `alapkep_utomunka_a8.py`. |
| Render | Blender 5.2.3, EEVEE sugárkövetéssel, 1600 × 1000, AgX + Medium High Contrast, expozíció +0,75. Azonos az A-902 és az A-811 alapképeivel. Háttér-Blender a Macen; az élő fájlhoz nem nyúlt. |
| Fény | Egyenletes, szórt nappali fény: egyszínű égbolt, 0,86/0,88/0,92, erősség 1,0. Nincs nap; a homlokzat a rajz É-jele szerint ≈ ÉNy-i. Belső lámpa nincs. |
| Rejtve | A kiállás-réteg. Bútor, konyha és szaniter nincs a modellben; az egyedi sarokkád be van építve (Péter), de nincs modellezve. |
| Kamerák | 20 mm, z 1,5 m:<br>• Cam_02_Nappali_erkely (nappali → erkélyüveg);<br>• Cam_03_Etkezo_konyha (ablak felől → étkező, konyha, előtér);<br>• Cam_04_Haloszoba (05.3 háló: ágyfal + ablakfal);<br>• Cam_05_Haloszoba_05_2. |

## Felületek – kamera szerint
| Felület | Cam_02 nappali → erkély | Cam_03 étkező → konyha | Cam_04 háló 05.3 | Cam_05 háló 05.2 | Státusz |
|---|---|---|---|---|---|
| Padló | meleg szürke sík tónus, sRGB ~153/150/148 | ~152/149/147 | ~153/150/148 | ~153/150/148 | Egger Grey Soria Oak EL2065 a burkolatkiosztási terv szerint (a konyhában és az előtérben is parketta). **Deszkaminta nincs, a tónus BECSLÉS.** |
| Falak | fehér, ~210/211/212 | ~211/212/213 | ~211/212/214 | ~212/213/214 | MEGLÉVŐ fehér festés |
| Mennyezet | fehér | fehér | fehér | fehér | MEGLÉVŐ; az előtérben 2,50 m-es álmennyezet a rajz szerint, **nincs modellezve** |
| Homlokzati üvegfal / ablak | 3,65 × 2,57: kétszárnyú erkélyajtó + fix mező; belül fehér profil | – | 2,80 × 2,57, padlóig érő, 3 nyíló szárny | 2,87 × 2,57, padlóig érő, 4 nyíló szárny | TERV SZERINT; a hálók nyíló szárnyai a rajzon 45°-os ablakjellel |
| Beltéri ajtó | – | bejárati ajtó a háttérben | – | – | TERV SZERINT; a szín az A-902 fotója alapján feltételezett |
| Konyha | – | **nincs konyhabútor**; a konyha nyitott | – | – | TERV SZERINT |
| Erkély / korlát | erkélylemez + pálcás korlát (lépcsős kontúr) | – | **korlát nincs** a padlóig érő ablak előtt | ua. | **ELŐZETES / NEM IGAZOLT**: az erkélyszint (−0,15) és a korlát feltételezés; francia erkély korlátja a rajzon nem szerepel |
| Kilátás | **nincs modellezve** – egyszínű világos égbolt | – | ua. | ua. | a valós kilátás csak helyszíni fotóból; generikus skyline tilos |

## Képek
- `A812_Alap-v1_blender_02_nappali-erkely.png`
- `A812_Alap-v1_blender_03_etkezo-konyha.png`
- `A812_Alap-v1_blender_04_haloszoba.png`
- `A812_Alap-v1_blender_05_haloszoba-2.png`
- `A812_Alap-v1_blender_06_alaprajz-kiallasok.png`: **ellenőrző felülnézet, nem Astrának szól.** Rajta a 121 kiállás és a 8 hűtő-fűtő mező, a `A812_villamos.csv` koordinátáival.
- `render_log_A812.json`

## Astrának – a B fázis promptjában kötelező
- Őrizze meg:
  - a falakat, az ablakok és az üvegfal osztását;
  - a kamera nézetét;
  - a padló meleg szürke tónusát (meglévő szürke tölgy parketta).
- A hálószobák padlóig érő ablaka elé ne tegyen kitalált korlátot vagy erkélyt; a valós állapot hétfőn derül ki.
- A konyha üres. Konyhabútor csak a stílusterv tételeként, méretezve.
- Lámpa csak a mennyezeti kiállás helyére, kiállás-azonosítóval.
- A kilátás valós forrásból.

## Észrevétel a kiállás-rétegből – tervezést érinti
**Hűtő-fűtő mezőn belül van** a nappali-étkező, mindhárom háló és mindkét gardrób mennyezeti lámpakiállása: **ML03–ML08, ML17, ML18**. A lámparögzítés előtt hőkamerás ellenőrzés kell. **Hétfőn ellenőrizendő.**

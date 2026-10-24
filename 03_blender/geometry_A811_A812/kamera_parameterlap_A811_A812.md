# A-811 és A-812 – kamera-paraméterlap (2026-10-24)

A lockba rögzítve (`geometry_lock_A811.json`, `geometry_lock_A812.json` → `cameras`); a validátor v2 minden paramétert ellenőriz. Mind 36 × 24 mm-es szenzor, AUTO illesztés, shift 0/0, clip 0,1–200, render 1600 × 1000 (a felülnézet 1500 × 1700, ill. 1300 × 2100).
Az alapképek (`04_renderek/A811_alap_v2/`, `A812_alap_v2/`, geometria v2) ezekből készültek; a kamerák a v1-hez képest nem változtak; a B fázis stílusképei ugyanezekből a nézetekből készüljenek.

## A-811

| Kamera | Típus | Fókusz mm | Hely [x; y; z] m | Forgatás [rad] | Státusz |
|---|---|---|---|---|---|
| Cam_02_Nappali_erkely | PERSP | 20 | [5,75; 7,15; 1,5] | [1,532; 0; 1,083] | ÖSSZEHASONLÍTÓ – B fázis (nappali → erkélyüveg) |
| Cam_03_Etkezo_konyha | PERSP | 20 | [0,55; 7,05; 1,5] | [1,533; 0; -1,104] | ÖSSZEHASONLÍTÓ – B fázis (ablak felől → étkező, konyha) |
| Cam_04_Haloszoba | PERSP | 20 | [3; 3; 1,5] | [1,5; 0; 0,7188] | ÖSSZEHASONLÍTÓ – B fázis (05.2-3 háló: ágyfal + üvegfal) |
| Cam_05_Haloszoba_05_1 | PERSP | 20 | [4,75; 2,45; 1,5] | [1,511; 0; 1,886] | kiegészítő nézet (05.1) |
| Cam_01_Felulnezet | ORTHO | 50 (ortho 13,09) | [3,232; 5,684; 40] | [0; 0; 0] | ellenőrző felülnézet |
| Cam_06_Alaprajz_lakas | ORTHO | 50 (ortho 12,59) | [3,232; 5,684; 40] | [0; 0; 0] | ellenőrző alaprajz (kiállás-réteggel) |

## A-812

| Kamera | Típus | Fókusz mm | Hely [x; y; z] m | Forgatás [rad] | Státusz |
|---|---|---|---|---|---|
| Cam_02_Nappali_erkely | PERSP | 20 | [5,5; 0,55; 1,5] | [1,532; 0; 1,024] | ÖSSZEHASONLÍTÓ – B fázis (nappali → erkélyüveg) |
| Cam_03_Etkezo_konyha | PERSP | 20 | [0,55; 4,5; 1,5] | [1,531; 0; -2,067] | ÖSSZEHASONLÍTÓ – B fázis (ablak felől → étkező, konyha) |
| Cam_04_Haloszoba | PERSP | 20 | [6,15; 13,05; 1,5] | [1,496; 0; 0,7854] | ÖSSZEHASONLÍTÓ – B fázis (05.3 háló) |
| Cam_05_Haloszoba_05_2 | PERSP | 20 | [5,85; 8,25; 1,5] | [1,484; 0; 0,8262] | kiegészítő nézet (05.2) |
| Cam_01_Felulnezet | ORTHO | 50 (ortho 19,24) | [3,492; 8,045; 40] | [0; 0; 0] | ellenőrző felülnézet |
| Cam_06_Alaprajz_lakas | ORTHO | 50 (ortho 18,51) | [3,492; 8,045; 40] | [0; 0; 0] | ellenőrző alaprajz (kiállás-réteggel) |

Koordináta: x a rajzon jobbra, y a rajzon felfelé (a homlokzati üvegfal a −x oldalon, a rajz É-jele szerint ≈ ÉNy felé néz). A kamerák célpontja és indoka: `geometry_A811_A812/a8_geometria.py` → `kamerak`.

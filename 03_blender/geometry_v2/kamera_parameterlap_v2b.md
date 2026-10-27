# A-902 v2b – kamera-paraméterlap (2026-10-24)

A lockba rögzítve (`geometry_lock_A902_v2b.json` → `cameras`); a validátor v2 minden paramétert ellenőriz.

| Kamera | Típus | Fókusz mm | Szenzor | Illesztés | Shift x/y | Clip | Hely [x; y; z] | Forgatás [rad] | Státusz |
|---|---|---|---|---|---|---|---|---|---|
| Cam_01_Felulnezet | ORTHO | 24 (ortho 23) | 36×24 | AUTO | 0/0 | 0,1–200 | [8,25; 10; 40] | [0; -0; 0] | ellenőrző felülnézet |
| Cam_02_Nappali_terasz | PERSP | 20 | 36×24 | AUTO | 0/0 | 0,1–200 | [8,3; 4,4; 1,55] | [1,479; 0; 0,858] | ÖSSZEHASONLÍTÓ – B fázis |
| Cam_03_Etkezo_konyha | PERSP | 20 | 36×24 | AUTO | 0/**−0,08** | 0,1–200 | **[9,45; 7,55; 1,5]** | **[1,5708; 0; −3,1416]** | **JAVASLAT K1** (v2b-1-k13, kameracsomag C, Péter 2026-10-25 04:08) – konyhaorientált, a konyha tengelyében dél felé, vízszintes; nappali fény. A régi [4,7; 7,7; 1,5], rot [1,493; 0; −2,111] a lock `javitasok` v2b-1-k13 bejegyzésében |
| Cam_04_Master | PERSP | 20 | 36×24 | AUTO | 0/0 | 0,1–200 | [0,35; 4,3; 1,5] | [1,434; -0; -0,745] | ÖSSZEHASONLÍTÓ – B fázis |
| Cam_05_Terasz | PERSP | 24 | 36×24 | AUTO | 0/0 | 0,1–200 | [11,5; 15,5; 1,7] | [1,48; 0; 2,469] | ELAVULT (régi sík teraszra; évelőágyás fölé esik) – nem használandó |
| Cam_06_Alaprajz_lakas | ORTHO | 24 (ortho 18) | 36×24 | AUTO | 0/0 | 0,1–200 | [8,25; 4,5; 40] | [0; -0; 0] | ellenőrző alaprajz |
| Cam_07_Terasz_v2_greslaprol | PERSP | 16 | 36×24 | AUTO | 0/0 | 0,1–1000 | [12,8; 9,3; 1,45] | [1,466; 0; 0,558] | ELŐZETES terasznézet (16 mm, z 1,45 = 1,60 a gres fölött) |
| Cam_08_Terasz_v2_madarnezet | PERSP | 20 | 36×24 | AUTO | 0/0 | 0,1–1000 | [18,5; 23; 9] | [0,908; 0; 2,443] | ellenőrző madártávlat |
| Cam_09_Terasz_v2_felulnezet | ORTHO | 20 (ortho 15,5) | 36×24 | AUTO | 0/0 | 0,1–1000 | [9,85; 14,5; 40] | [0; 0; 0] | ellenőrző felülnézet |
| Cam_10_Furdo_06_2 | PERSP | 16 | 36×24 | AUTO | 0/0 | 0,1–200 | [14,5; 6,62; 1,5] | [1,38; 0; -1,5708] | ÖSSZEHASONLÍTÓ – KEP-004, fürdő 06.2 (ablaktalan, csak műfény); ajtónyílásból kelet felé; v2b-1-k10, 2026-10-24 (a V3.1 sablon ideiglenes [14,75; 5,45] kamerája a WC-be esett) |
| Cam_11_Master_Panorama | PERSP | 20 | 36×24 | AUTO | 0/0 | 0,1–200 | [3,2; 6,1; 1,2] | [1,5708; 0; 1,5708] | **JAVASLAT** (v2b-1-k11, draft PR) – 05.1 az ágy/párnák felől (ülő szemmagasság ≈1,20 m, becslés), vízszintes, nyugat felé az üvegfalra és a valós panorámára; Péter külön jóváhagyásáig NEM összehasonlító master, a Cam_04_Master marad; összevetés: `04_renderek/A902_cam11_javaslat_v1/` |
| Cam_12_Nappali_Hero | PERSP | **22** | 36×24 | AUTO | 0/**−0,05** | 0,1–200 | **[4,40; 7,88; 1,60]** | **[1,5708; 0; −2,4086]** | **JAVASLAT v3** (v2b-1-k13, kameracsomag C): 0,45 m-rel keletebbre és 15 cm-rel magasabbra, θ −48°, a W01 legfeljebb 60 cm mély szekrénye sem takarja ki; `04_renderek/A902_kameracsomag_C/`. Előzmény – **JAVASLAT v2** (v2b-1-k12, draft PR) – nappali HERO az ÉNy-i sarokból (TV-fal + teraszüveg) délkelet felé. Vízszintes kamera, a függőlegesek egyenesek; a shift_y −0,08 kevesebb mennyezetet és több bútort mutat. Látszik: a kanapé eleje, az étkező, a konyha pultfala, a W03 a 05.3 ajtóval, a W02 és a hálószobai közlekedő torka. Péter 01:58/02:06; összevetés: `04_renderek/A902_cam12_hero_javaslat/` |

Render: {"resolution_x": 1600, "resolution_y": 1000, "percentage": 100, "pixel_aspect": [1.0, 1.0], "scene_camera": "Cam_04_Master", "engine": "BLENDER_EEVEE", "view_transform": "AgX", "look": "AgX - Medium High Contrast", "exposure": -1.0, "gamma": 1.0}


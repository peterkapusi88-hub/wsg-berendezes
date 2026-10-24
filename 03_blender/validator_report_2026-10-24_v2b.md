# Validátor-riport – A-902 geometria v2b (2026-10-24)

> **Státusz: ELŐZETES – a geometria TERV SZERINT javítva, a bútorréteg még nem.** PASS csak 0 hibánál; a v2b FAIL a régi bútor és az új falak/kiállások ütközése miatt, ami tervezési feladat, nem geometriai hiba.

- Szkript: `03_blender/geometry_validator_v2.py` · Lock: `geometry_lock_A902_v2b.json` · Kiállások: `01_alaprajzok/villamos_kiallasok/A902_villamos.json` (PR #4)
- Látható stílusréteg: ['Stil_LakeForest'] · aktív kamera: Cam_04_Master

| Futás | Eredmény | Hibák kategóriánként | Figyelmeztetések |
|---|---|---|---|
| v2 alap (előtte) | FAIL – 176 hiba, 82 figyelmeztetés; réteg: ['Stil_LakeForest'] | {'LOCK': 125, 'AJTÓ-FORGÁS': 10, 'VILLAMOS': 41} | {'BURKOLÓ': 23, 'ÁTFEDÉS': 16, 'KONYHA': 1, 'VILLAMOS': 42} |
| **v2b (utána)** | **FAIL – 89 hiba, 82 figyelmeztetés; réteg: ['Stil_LakeForest']** | {'ÜTKÖZÉS': 38, 'AJTÓ-FORGÁS': 10, 'VILLAMOS': 41} | {'BURKOLÓ': 23, 'ÁTFEDÉS': 16, 'KONYHA': 1, 'VILLAMOS': 42} |

A v2 alap 125 LOCK-hibája pontosan a v2b javításai (lásd `geometry_v2/v2b_elteresi_lista.md`); a v2b-ben LOCK 0, TERASZ 0 változás.

## Rendben

- LOCK walls: 60 elem, 0 eltérés
- LOCK openings: 54 elem, 0 eltérés
- LOCK floors: 17 elem, 0 eltérés
- TERASZ v2 (tetőkert): 43 elem, 0 változás
- KAMERA: 9 kamera teljes paraméterrel; aktív: Cam_04_Master
- BURKOLÓ: 195 látható bútorelem
- ÜTKÖZÉS: bútor–fal/nyílászáró 38, bútor–bútor átfedés 16
- AJTÓ: 11 nyílás negyedkörrel/sávval vizsgálva
- VILLAMOS: 130 terv szerinti kiállás vizsgálva; takarás 41, dugalj elé állás 42

## Hibák (v2b)

### VILLAMOS (41)

- L_TVfal_travertin takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7090 takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7135 takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7180 takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7225 takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_TV55 takarja: A902-K10 kapcsolo n,p (x 7.149, y 4.049, ~1.1 m)
- L_TVfal_travertin takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7090 takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7135 takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7180 takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7225 takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_TV55 takarja: A902-K11 kapcsolo c,d (x 7.149, y 4.049, ~1.1 m)
- L_TVfal_travertin takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7090 takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7135 takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7180 takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7225 takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_TV55 takarja: A902-K12 kapcsolo a,b (x 7.149, y 4.049, ~1.1 m)
- L_agyfal_travertin takarja: A902-K13 kapcsolo t (x 3.545, y 7.51, ~0.65 m)
- L_agyfal_travertin takarja: A902-K14 kapcsolo t (x 3.545, y 5.319, ~0.65 m)
- L_gardrob_krem takarja: A902-K15 kapcsolo t (x 2.506, y 4.064, ~1.1 m)
- L_gardrob_krem takarja: A902-K16 kapcsolo u (x 2.506, y 4.064, ~1.1 m)
- Gardrob_05_2_PAX_240 takarja: A902-K17 kapcsolo s (x 2.538, y 2.634, ~1.1 m)
- Ejjeli_05_3_a_lampa takarja: A902-K21 kapcsolo e (x 11.729, y 4.124, ~0.65 m)
- Agy_05_3_180x200_parna_takaro takarja: A902-K22 kapcsolo e (x 13.92, y 4.124, ~0.65 m)
- Agy_05_3_180x200_fejtamla takarja: A902-K22 kapcsolo e (x 13.92, y 4.124, ~0.65 m)
- L_gardrob_krem takarja: A902-G09 BK_doboz BK (x 1.919, y 3.566, ~1.1 m)
- L_TVfal_travertin takarja: A902-S01 hangjelzo_vagy_erzekelo  (x 7.149, y 4.049, ~2.2 m)
- L_lamella_7090 takarja: A902-S01 hangjelzo_vagy_erzekelo  (x 7.149, y 4.049, ~2.2 m)
- L_lamella_7135 takarja: A902-S01 hangjelzo_vagy_erzekelo  (x 7.149, y 4.049, ~2.2 m)
- L_lamella_7180 takarja: A902-S01 hangjelzo_vagy_erzekelo  (x 7.149, y 4.049, ~2.2 m)
- L_lamella_7225 takarja: A902-S01 hangjelzo_vagy_erzekelo  (x 7.149, y 4.049, ~2.2 m)
- L_agyfal_travertin takarja: A902-S08 hangjelzo_vagy_erzekelo  (x 3.569, y 4.049, ~2.2 m)
- L_TVfal_travertin takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7090 takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7135 takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7180 takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_lamella_7225 takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_TV55 takarja: A902-T01 termosztat  (x 7.149, y 4.049, ~1.1 m)
- L_gardrob_krem takarja: A902-T02 termosztat  (x 2.506, y 4.064, ~1.1 m)
- Gardrob_05_2_PAX_240 takarja: A902-T03 termosztat  (x 2.538, y 2.634, ~1.1 m)

### ÜTKÖZÉS (38)

- Gardrob_05_3_PAX_200 ↔ fal Akna_etkezo_05_3 (10.0 cm)
- Konyha_labazat_K ↔ fal Kulso_D_konyha_0 (5.0 cm)
- Konyha_labazat_K ↔ fal Kulso_K_konyha_05_3_0 (9.0 cm)
- Konyha_labazat_K ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- Konyha_huto_labazat ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- Cipos_STALL_eloter ↔ fal Fal_furdo_wc_K_0 (5.0 cm)
- Tukor_eloter ↔ fal Fal_furdo_wc_K_0 (2.0 cm)
- Ulopad_eloter ↔ fal Kulso_D_eloter_0 (4.0 cm)
- Ulopad_lab ↔ fal Kulso_D_eloter_0 (15.0 cm)
- Torolkozoszarito_06_1 ↔ fal Fal_05_2_furdo_0 (3.0 cm)
- Zuhanytalca_06_2_182x85 ↔ fal Kulso_K_06_2_0 (3.0 cm)
- Zuhanyuveg_06_2 ↔ fal Kulso_K_06_2_0 (2.0 cm)
- Mosdoszekreny_06_2 ↔ fal Kulso_K_06_2_0 (10.0 cm)
- Mosdo_06_2 ↔ fal Kulso_K_06_2_0 (10.0 cm)
- Tukor_06_2 ↔ fal Kulso_K_06_2_0 (2.0 cm)
- WC_tartaly_06_2 ↔ fal Akna_06_2 (2.0 cm)
- WC_tartaly_06_2 ↔ fal Fal_06_2_D_v2b (2.0 cm)
- L_TVfal_travertin ↔ fal Fal_wc_E_nappali_0 (1.0 cm)
- L_TVfal_travertin ↔ fal Szemoldok_atjaro_eloter_nappali (1.0 cm)
- L_fuggonysin ↔ fal Akna_etkezo_05_3 (3.0 cm)
- L_konyha_also_K ↔ fal Kulso_D_konyha_0 (5.0 cm)
- L_konyha_also_K ↔ fal Kulso_K_konyha_05_3_0 (9.0 cm)
- L_konyha_also_K ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- L_konyha_munkalap_K ↔ fal Kulso_D_konyha_0 (4.0 cm)
- L_konyha_munkalap_K ↔ fal Kulso_K_konyha_05_3_0 (4.0 cm)
- L_konyha_munkalap_K ↔ fal Fal_konyha_K_csonk_v2b (4.0 cm)
- L_konyha_huto ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- L_konyha_felso_K ↔ fal Kulso_D_konyha_0 (5.0 cm)
- L_konyha_felso_K ↔ fal Kulso_K_konyha_05_3_0 (9.0 cm)
- L_konyha_felso_K ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- L_konyha_hatfal_marvany ↔ fal Kulso_D_konyha_0 (5.0 cm)
- L_konyha_hatfal_marvany ↔ fal Kulso_K_konyha_05_3_0 (9.0 cm)
- L_konyha_hatfal_marvany ↔ fal Fal_konyha_K_csonk_v2b (9.0 cm)
- L_konyha_top_LED ↔ fal Kulso_D_konyha_0 (2.0 cm)
- L_konyha_top_LED ↔ fal Kulso_K_konyha_05_3_0 (2.0 cm)
- L_konyha_top_LED ↔ fal Fal_konyha_K_csonk_v2b (2.0 cm)
- L_konyha_magas ↔ fal Kulso_D_konyha_0 (5.0 cm)
- L_agyfal_travertin ↔ fal Fal_05_1_nappali_0 (5.0 cm)

### AJTÓ-FORGÁS (10)

- L_ejjeli_0 a(z) Ajto_05_1 nyitási negyedkörében (r 0.9 m)
- L_ejjeli_lap_0 a(z) Ajto_05_1 nyitási negyedkörében (r 0.9 m)
- Agy_05_2_160x200_keret a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Agy_05_2_160x200_matrac a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Agy_05_2_160x200_parna_takaro a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Agy_05_2_160x200_fejtamla a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Ejjeli_05_2_b a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Ejjeli_05_2_b_lampa a(z) Ajto_05_2 nyitási negyedkörében (r 0.9 m)
- Cipos_STALL_eloter a(z) Ajto_WC nyitási negyedkörében (r 0.75 m)
- Gardrob_05_3_PAX_200 a(z) Ajto_05_3 nyitási negyedkörében (r 0.9 m)

## Figyelmeztetések (v2b, összesítve)

- **VILLAMOS** (42): Ulopad_lab a(z) A902-D01 dugalj  előtt (x 7.149, y 0.849, ~0.3 m) – hozzáférés ellenőrizendő · L_konyha_also_K a(z) A902-D02 dugalj P előtt (x 10.525, y 3.79, ~0.3 m) – hozzáférés ellenőrizendő · L_konyha_also_K a(z) A902-D03 dugalj P előtt (x 10.525, y 3.709, ~0.3 m) – hozzáférés ellenőrizendő · L_konyha_also_K a(z) A902-D04 dugalj MG előtt (x 10.525, y 3.31, ~0.3 m) – hozzáférés ellenőrizendő · L_konyha_also_Ny a(z) A902-D05 dugalj EL előtt (x 8.973, y 3.224, ~0.3 m) – hozzáférés ellenőrizendő · L_konyha_also_K a(z) A902-D06 dugalj P előtt (x 10.525, y 2.25, ~0.3 m) – hozzáférés ellenőrizendő …
- **BURKOLÓ** (23): Gardrob_05_3_PAX_200 kilóg a helyiségből vagy bútorozható zónából ([11.0, 6.0, 11.6, 7.95]) · Gardrob_05_3_PAX_200_fuga2 kilóg a helyiségből vagy bútorozható zónából ([11.0, 7.3, 11.6, 7.3]) · Konyha_labazat_K kilóg a helyiségből vagy bútorozható zónából ([10.08, 1.3, 10.64, 4.5]) · Konyha_huto_labazat kilóg a helyiségből vagy bútorozható zónából ([10.08, 4.5, 10.64, 5.15]) · Cipos_STALL_eloter kilóg a helyiségből vagy bútorozható zónából ([5.55, 0.3, 5.9, 1.5]) · Tukor_eloter kilóg a helyiségből vagy bútorozható zónából ([5.55, 0.4, 5.57, 1.4]) …
- **ÁTFEDÉS** (16): L_fotel_hat ↔ L_fotel_karfa_a (17.0 cm) · L_fotel_hat ↔ L_fotel_karfa_b (13.6 cm) · L_dohanyzo_lap ↔ L_kanape_ules_3 (3.0 cm) · L_dohanyzo_lap ↔ L_kanape_ules_1 (3.0 cm) · L_TVfal_pad ↔ L_lamella_7270 (2.2 cm) · L_TVfal_pad ↔ L_lamella_7225 (2.2 cm) …
- **KONYHA** (1): pultsorok közti tiszta köz 85 cm (cél ≥ 90; a nyers szerkezeti szélesség 2,10 m → két 62 cm-es pulttal 86 cm)

## Információ

- KAMERA Cam_01_Felulnezet: ellenőrző felülnézet
- KAMERA Cam_02_Nappali_terasz: ÖSSZEHASONLÍTÓ – B fázis
- KAMERA Cam_03_Etkezo_konyha: ÖSSZEHASONLÍTÓ – B fázis
- KAMERA Cam_04_Master: ÖSSZEHASONLÍTÓ – B fázis
- KAMERA Cam_05_Terasz: ELAVULT (régi sík teraszra; évelőágyás fölé esik) – nem használandó
- KAMERA Cam_06_Alaprajz_lakas: ellenőrző alaprajz
- KAMERA Cam_07_Terasz_v2_greslaprol: ELŐZETES terasznézet (16 mm, z 1,45 = 1,60 a gres fölött)
- KAMERA Cam_08_Terasz_v2_madarnezet: ellenőrző madártávlat
- KAMERA Cam_09_Terasz_v2_felulnezet: ellenőrző felülnézet
- 05.2: fejjel a déli falnak, az ajtóforgásokon kívül elférő ágyak (legjobb oldaltávolság): 140 cm x 1.10–2.50, oldalt 110/115 cm, lábnál 60 cm; 160 cm x 1.00–2.60, oldalt 100/105 cm, lábnál 60 cm
- VILLAMOS: a(z) A902-ML04 „b” mennyezeti kiállás alatt: ['L_etkezo_lap']
- VILLAMOS: a(z) A902-ML05 „n,p” mennyezeti kiállás alatt: ['L_kanape_ules', 'L_parna_1']
- VILLAMOS: a(z) A902-ML06 „t” mennyezeti kiállás alatt: ['L_agy_keret', 'L_agy_matrac', 'L_agy_takaro']
- VILLAMOS: a(z) A902-ML07 „s” mennyezeti kiállás alatt: ['Agy_05_2']
- VILLAMOS: a(z) A902-ML08 „e” mennyezeti kiállás alatt: ['Agy_05_3']

## Mit jelent a tervezésnek

- **Konyha:** a régi (LF) konyhasor a javított keleti falba (x 10,55) és a csonkfalba lóg; a két pultsor tiszta köze 85 cm (cél 90). Újratervezendő a v2b falakhoz.
- **Nappali, Lake Forest TV-fal:** a déli falon (x 5,55–7,40) **eltakarja a fő kapcsolóoszlopot, a termosztátot és a mozgásérzékelőt** (A902-K10–K12, T01, S01, fali hely x 7,15 y 4,05). A terv szerinti TV-blokk a nyugati válaszfalon van (y 6,0–6,5).
- **05.1:** a LF ágyfal-travertin a 65 cm-es ágy melletti kapcsolókat (t) és az ajtósarki mozgásérzékelőt (S08, becsült 2,2 m) takarja; a gardrób a 05.1 ajtó melletti kapcsolókat, termosztátot és a BK-dobozt.
- **05.2:** a 160×200-as ágy a jelenlegi helyén az ajtó nyitási negyedkörében van. A forgásokon kívül: 160-as ágy fejjel a déli falnak x 1,00–2,60 (oldalt 100/105 cm, lábnál 60 cm), vagy 140-es x 1,10–2,50. A PAX 240 a 05.2 ajtó melletti kapcsolót (s) és termosztátot takarja.
- **05.3, WC:** a PAX 200 az ajtó negyedkörébe és az étkező-aknába lóg; az előtéri cipős szekrény a WC-ajtó nyitásába.
- **06.2:** a mosdószekrény és a zuhany a javított keleti fal (x 16,40) miatt 2–10 cm-rel ütközik – a valós szaniterek helye hétfőn mérendő.
- A bútorréteget a stílusválasztás után, a v2b geometriára és a kiállásokra kell újraépíteni (Astra B fázis előtt).


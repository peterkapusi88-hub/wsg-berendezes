# KEP-004 · ChatGPT Images · összefűzött promptok – próbakör 1 (v1, 2026-10-25 00:05)

**Mi ez:** a próbakör 16 képének futtatható, összefűzött promptja: 10 stíluskép (S01/S02 × nappali, konyha–étkező, fürdő, master Cam_04 és Cam_11) + 6 Zenit/Lake Forest kalibráció (nappali, master Cam_04, master Cam_11).
- Képenként egy `.prompt.txt`, a ChatGPT-chatbe szó szerint bemásolandó.
- **Képgenerálás nem indult.**
- Végrehajtási terv: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004_CHATGPT_IMAGES_v1.md`.
- A képenkénti csatolmánycsomag a Macen van: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/probakor1_v1_2026-10-24/`.

## Összefűzési sorrend (minden promptban)
1. **Futtatási fejléc** (Claude): kép-ID, verzió, a küldés = Péter jóváhagyása, a csatolt képek sorrendje és szerepe, kimeneti formátum.
2. **Közös FIXED blokk** – v3.1 §1, szó szerint. Csak a markdown idézőjel (`> `) maradt le, a `{ROOM}`/`{STYLE_NAME}` helyőrző kitöltve.
3. **Helyiség-FIXED blokk** – v3.1 §2, szó szerint.
   - **Cam_10:** a rögzített kamerablokk v1 váltja az ideiglenes blokkot (`A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`).
   - **Cam_11:** a kamerablokk-javaslat v1 váltja a Cam_04-blokkot (`A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md`, a draft PR #15 ágáról, változatlanul).
4. **Philips Hue követelmény** – `A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`, szó szerint (Péter, 22:57).
5. **Csak master (Cam_04 és Cam_11):** gardróbfal-döntés – `A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md` blokkja szó szerint (Péter, 22:37–22:40) + a stílus frontsora.
6. **Stílusblokk** – Astra V2 r1, szó szerint (S01/S02). A Cam_11 a master (Cam_04) blokkját kapja; a kép-ID-t a RUN NOTES adja. Kalibrációnál: v3.1 §3 C1/C2 szöveg + a koncepció-doksi A-902-es cellája, szó szerint.
7. **RUN NOTES** (Claude): ahol a stílusblokk „Inputs” sora eltér, ezek érvényesek. Tartalom: régi útvonal, nem 05.1-es fotók, fürdőfotók besorolása, Eamy- és Ciselia-méret, a Brisia-csere, az olvasólámpák, a két master-kamera, Hue-ellenőrzés, a Kave-képek eredete.

**A v1 véglegesítése a futtatás előtt.** Egyik prompt sem futott még. A korábbi állapotok a git-történetben vannak (`61a5410`), a napló a futtatott prompt sha256-ját rögzíti.

- 23:12 – Brisia: a Kave méretrajza szerint mennyezeti lámpa (Ø80 × 26 cm), nem függeszték. RUN NOTES-sor, és a termékleírás javítva.
- 23:25 – Kave Home-termékképek: Péter képernyőképeiből kivágva (6 próbaköri + 14 tétel a 2–3. adaghoz). Ciselia-méret a méretrajzból. Somar: „Hanging method: Wire” (függeszték).
- 23:33–23:39 – Péter döntései:
  - a master mindkét kamerával készül, a Cam_04 mellett a Cam_11-gyel is (+4 csomag: 13–16);
  - az ágy a terv szerinti helyen áll (a két éjjeli dugaljcsoport között);
  - a Brisia helyett választhattam: a Brisia család függesztett, Ø50-es gömbje lett (S02, ML04);
  - az olvasólámpák designosak legyenek, és férjen beléjük Hue-izzó: S01 – Raze, S02 – Aleyla;
  - a Kave-oldalt olvassam a böngészőben, ahogy ő is tette. Innen jöttek a specifikációk és 3 termékkép.

**Nem módosított forrásfájlok (sha256):**

| Fájl | sha256 |
|---|---|
| `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` | `06b28c8e7374e2554d65eeb4bf3c6639f2aab87f4fc54e9ed7ee1f1acfe40d32` |
| `05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md` | `6549a09b61d2131efa68f7d7575a309e379a6665de4b3217228e3881c9456a96` |
| `05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md` | `aebff8b51d988f5f4a0f10c7ceb533be0f03d7251e2329b05733baa7e39ca163` |
| `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md` | `f48745e46e9242e8bdb531baad969aacd0a4a497740347311dd760a8de5274a7` |
| `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md` | `d0e5a843135363c96d815c3eb31b20361b068a93f2a47066be450ad90dd1c8c3` |
| `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` | `3962dba2f88cf61409240aeddf2aebdb7c3f94062cc877777371ba728c0caead` |
| `05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md` (draft PR #15 ág, `ead34d9`) | `624da6aa3f511ba984871ea93985d1dc17e80f540245465e2c1074d2fa5c5bce` |
| `04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png` (draft PR #15 ág) | `66fa4efbcc0d71aa7c45d4a883da702231273f680cb3ebd16c20a505e621c01f` |

## Ellenőrzés (2026-10-24 23:58, `ellenor.py`)
Minden promptban szó szerint megvan a közös FIXED, a helyiség-FIXED, a Hue-blokk, a mastereknél a gardróbblokk és a frontsor, és az Astra-stílusblokk vagy a §3 kalibráció + koncepció-cella. A kép-ID egyezik Astra „Output” sorával, nem maradt helyőrző, a fejléc csatolmánylistája egyezik a csomag fájljaival. **Hiba: 0.**

| # | Kép-ID | Lépés | Karakter | Csatolmány | Kave kézi | prompt sha256 |
|---|---|---|---|---|---|---|
| 01 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | 1a | 8212 | 5 | 0 | `d46f4747ab5c8a15…` |
| 02 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | 1a | 8142 | 5 | 0 | `699a2cefaf536576…` |
| 03 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | 1a | 13583 | 9 | 0 | `9981b35cf6824172…` |
| 04 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | 1a | 14281 | 9 | 0 | `2961e872ac72317a…` |
| 05 | `A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A` | 1a | 12743 | 8 | 0 | `2709099e14f0d8c2…` |
| 06 | `A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A` | 1a | 13318 | 8 | 0 | `e2ae01ba80592f77…` |
| 07 | `A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A` | 1b | 12398 | 3 | 0 | `25a4745aef45715b…` |
| 08 | `A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A` | 1b | 12456 | 3 | 0 | `5c79e72602daed13…` |
| 09 | `A902_C1_Zenit_3_master_Cam_04_A` | 1c | 9565 | 4 | 0 | `831d4b15a262663a…` |
| 10 | `A902_C2_LakeForest_3_master_Cam_04_A` | 1c | 9523 | 4 | 0 | `d1128f0d2766ff9d…` |
| 11 | `A902_S01_KyotoInk_3_master_Cam_04_A` | 1c | 13048 | 5 | 0 | `974b509fdb42d270…` |
| 12 | `A902_S02_BiBoNocturne_3_master_Cam_04_A` | 1c | 13051 | 5 | 0 | `618134824e38f311…` |
| 13 | `A902_C1_Zenit_3_master_Cam_11_A` | 1c | 11610 | 4 | 0 | `4456bf013c34cf94…` |
| 14 | `A902_C2_LakeForest_3_master_Cam_11_A` | 1c | 11573 | 4 | 0 | `494e0ec4ebb56896…` |
| 15 | `A902_S01_KyotoInk_3_master_Cam_11_A` | 1c | 14143 | 4 | 0 | `a680923c7a892d0c…` |
| 16 | `A902_S02_BiBoNocturne_3_master_Cam_11_A` | 1c | 14155 | 4 | 0 | `4d088f4862bb9679…` |

## Csatolmányok képenként (sorrendben; repóútvonal vagy forrás)

### 01 · A902_C1_Zenit_1_nappali-terasz_Cam_02_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam02_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png – Blender-alapkép (geometria, kamera) (sha256 `cb60ec8ebc5b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_helyszin_falak-profilok-terasz.jpg` ← helyszin_kontaktlap_Cam02.jpg – helyszíni fotók: fal, profil, terasz (kontaktlap) (sha256 `2a5ef83f2d6d…`)
4. `04_kep2c_panorama_terasz.jpg` ← 02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg – valós panoráma (sha256 `9d0457ee8479…`)
5. `05_kep3_eredeti_Zenit_referencia.png` ← 04_renderek/ai_chatgpt/A902_Zenit_1_nappali_chatgpt.png – eredeti Zenit-kép (csak hangulat/minőség) (sha256 `c8a16e88b122…`)

### 02 · A902_C2_LakeForest_1_nappali-terasz_Cam_02_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam02_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png – Blender-alapkép (geometria, kamera) (sha256 `cb60ec8ebc5b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_helyszin_falak-profilok-terasz.jpg` ← helyszin_kontaktlap_Cam02.jpg – helyszíni fotók: fal, profil, terasz (kontaktlap) (sha256 `2a5ef83f2d6d…`)
4. `04_kep2c_panorama_terasz.jpg` ← 02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg – valós panoráma (sha256 `9d0457ee8479…`)
5. `05_kep3_eredeti_LakeForest_referencia.png` ← 04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png – eredeti LakeForest-kép (csak hangulat/minőség) (sha256 `52e01cbe544f…`)

### 03 · A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam02_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png – Blender-alapkép (geometria, kamera) (sha256 `cb60ec8ebc5b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_helyszin_falak-profilok-terasz.jpg` ← helyszin_kontaktlap_Cam02.jpg – helyszíni fotók: fal, profil, terasz (kontaktlap) (sha256 `2a5ef83f2d6d…`)
4. `04_kep2c_panorama_terasz.jpg` ← 02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg – valós panoráma (sha256 `9d0457ee8479…`)
5. `05_kep4_termek_ww_Lennon_L_jobbos_szurkesbarna_DEQ21WES12329-168260.jpg` ← ww_Lennon_L_jobbos_szurkesbarna_DEQ21WES12329-168260.jpg – termékfotó: Westwing Lennon modular corner sofa, right-hand chaise, taupe woven fabric (P14) (sha256 `c2814e421f3f…`)
6. `06_kep4_termek_ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg` ← ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg – termékfotó: Westwing Toni oval dining table 200 × 90 cm, light oak veneer (P09) (sha256 `da0652a02a2f…`)
7. `07_kep4_termek_KH_Eamy_szek_vilagosszurke.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Eamy_szek_vilagosszurke.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Eamy chair, light-grey chenille, natural ash (KH-CH-EAMY-LG) – Kave Home, Péter képernyőképéből kivágva (sha256 `3eb2830c3754…`)
8. `08_kep4_termek_KH_Nifelia_szonyeg_200x300.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Nifelia_szonyeg_200x300.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Nifelia beige wool jacquard rug 200 × 300 (KH-RUG-NIFELIA) – Kave Home, Péter képernyőképéből kivágva (sha256 `8071584b73ca…`)
9. `09_kep4_termek_KH_Somar_fuggesztek_76.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Somar_fuggesztek_76.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Somar pendant Ø76 (KH-PL-SOMAR76) – Kave Home, Péter képernyőképéből kivágva (sha256 `ea936eca0ba2…`)

### 04 · A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam02_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png – Blender-alapkép (geometria, kamera) (sha256 `cb60ec8ebc5b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_helyszin_falak-profilok-terasz.jpg` ← helyszin_kontaktlap_Cam02.jpg – helyszíni fotók: fal, profil, terasz (kontaktlap) (sha256 `2a5ef83f2d6d…`)
4. `04_kep2c_panorama_terasz.jpg` ← 02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg – valós panoráma (sha256 `9d0457ee8479…`)
5. `05_kep4_termek_ikea_JATTEBO_U_Samsala_sotetkek_49607648.jpg` ← ikea_JATTEBO_U_Samsala_sotetkek_49607648.jpg – termékfotó: IKEA JÄTTEBO 3.5-seat modular U with two chaises, Samsala dark blue (P04) (sha256 `a9f482e59e27…`)
6. `06_kep4_termek_ww_Anouk_uveg_180x90_23WES68910.jpg` ← ww_Anouk_uveg_180x90_23WES68910.jpg – termékfotó: Westwing Anouk clear glass dining table 180 × 90 cm (P08) (sha256 `1c330875218b…`)
7. `07_kep4_termek_KH_Ciselia_szek_bezs_fekete.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Ciselia_szek_bezs_fekete.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Ciselia chair, beige chenille, black steel legs (KH-CH-CISELIA-BK) – Kave Home, Péter képernyőképéből kivágva (sha256 `3b5449507116…`)
8. `08_kep4_termek_KH_Marely_szonyeg_feher_200x300.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Marely_szonyeg_feher_200x300.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Marely white wool rug 200 × 300 (KH-RUG-MARELY-W) – Kave Home, Péter képernyőképéből kivágva (sha256 `afa79d72147f…`)
9. `09_kep4_termek_KH_Brisia_fuggesztek_1gomb_50_sargarez.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Brisia_fuggesztek_1gomb_50_sargarez.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Brisia pendant: one frosted glass globe Ø50 cm on a brushed-brass canopy and a black adjustable wire (L00152CR05) – Kave Home, a termékoldal fő képe (böngészőből, 2026-10-24) (sha256 `70799d304cf6…`)

### 05 · A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam03_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_03_etkezo-konyha.png – Blender-alapkép (geometria, kamera) (sha256 `f6f3ca25bb06…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_konyhafal_ME-BAL-056.jpg` ← 08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg – helyszíni fotó: konyhafal, kiállások, mellvéd (sha256 `cb316cd7d1de…`)
4. `04_kep2c_nappali_terasz_fele_ME-BAL-045.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg – helyszíni fotó: fal, profil (sha256 `06981c280964…`)
5. `05_kep4_termek_ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg` ← ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg – termékfotó: Westwing Toni oval dining table 200 × 90 cm, light oak veneer (P09) (sha256 `da0652a02a2f…`)
6. `06_kep4_termek_ikea_EKBACKEN_vilagosszurke_beton_40616275.jpg` ← ikea_EKBACKEN_vilagosszurke_beton_40616275.jpg – termékfotó: IKEA EKBACKEN worktop, light-grey concrete-effect laminate (AG-31) (sha256 `8bdae8b0f22b…`)
7. `07_kep4_termek_KH_Eamy_szek_vilagosszurke.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Eamy_szek_vilagosszurke.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Eamy chair, light-grey chenille, natural ash (KH-CH-EAMY-LG) – Kave Home, Péter képernyőképéből kivágva (sha256 `3eb2830c3754…`)
8. `08_kep4_termek_KH_Somar_fuggesztek_76.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Somar_fuggesztek_76.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Somar pendant Ø76 (KH-PL-SOMAR76) – Kave Home, Péter képernyőképéből kivágva (sha256 `ea936eca0ba2…`)

### 06 · A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam03_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_03_etkezo-konyha.png – Blender-alapkép (geometria, kamera) (sha256 `f6f3ca25bb06…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_konyhafal_ME-BAL-056.jpg` ← 08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg – helyszíni fotó: konyhafal, kiállások, mellvéd (sha256 `cb316cd7d1de…`)
4. `04_kep2c_nappali_terasz_fele_ME-BAL-045.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg – helyszíni fotó: fal, profil (sha256 `06981c280964…`)
5. `05_kep4_termek_ww_Anouk_uveg_180x90_23WES68910.jpg` ← ww_Anouk_uveg_180x90_23WES68910.jpg – termékfotó: Westwing Anouk clear glass dining table 180 × 90 cm (P08) (sha256 `1c330875218b…`)
6. `06_kep4_termek_ikea_EKBACKEN_szurke-bezs_ko_20604320.jpg` ← ikea_EKBACKEN_szurke-bezs_ko_20604320.jpg – termékfotó: IKEA EKBACKEN worktop, grey-beige stone-effect laminate (AG-33) (sha256 `41caab249954…`)
7. `07_kep4_termek_KH_Ciselia_szek_bezs_fekete.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Ciselia_szek_bezs_fekete.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Ciselia chair, beige chenille, black steel legs (KH-CH-CISELIA-BK) – Kave Home, Péter képernyőképéből kivágva (sha256 `3b5449507116…`)
8. `08_kep4_termek_KH_Brisia_fuggesztek_1gomb_50_sargarez.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Brisia_fuggesztek_1gomb_50_sargarez.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Brisia pendant: one frosted glass globe Ø50 cm on a brushed-brass canopy and a black adjustable wire (L00152CR05) – Kave Home, a termékoldal fő képe (böngészőből, 2026-10-24) (sha256 `70799d304cf6…`)

### 07 · A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A – INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)
1. `01_kep1_blender_alap_Cam10_v2b1k10.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png – Blender-alapkép (geometria, kamera) (sha256 `25c818fdc30f…`)
2. `02_kep2_furdo06-2_zuhany_mosdo_ME-BAL-064.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg – helyszíni fotó 06.2: zuhany, mosdó, burkolat, dekor (sha256 `6e577ef470a7…`)
3. `03_kep2b_furdo06-2_wc_torolkozoszarito_ajto_ME-BAL-066.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg – helyszíni fotó 06.2: WC, törölközőszárító, ajtó (sha256 `6b50e8a59bf6…`)

### 08 · A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A – INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)
1. `01_kep1_blender_alap_Cam10_v2b1k10.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png – Blender-alapkép (geometria, kamera) (sha256 `25c818fdc30f…`)
2. `02_kep2_furdo06-2_zuhany_mosdo_ME-BAL-064.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg – helyszíni fotó 06.2: zuhany, mosdó, burkolat, dekor (sha256 `6e577ef470a7…`)
3. `03_kep2b_furdo06-2_wc_torolkozoszarito_ajto_ME-BAL-066.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg – helyszíni fotó 06.2: WC, törölközőszárító, ajtó (sha256 `6b50e8a59bf6…`)

### 09 · A902_C1_Zenit_3_master_Cam_04_A – INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_Zenit_referencia.png` ← 04_renderek/ai_chatgpt/A902_Zenit_3_master_chatgpt.png – eredeti Zenit-kép (csak hangulat/minőség) (sha256 `37d17acef38c…`)

### 10 · A902_C2_LakeForest_3_master_Cam_04_A – INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_LakeForest_referencia.png` ← 04_renderek/ai_chatgpt/A902_LakeForest_3_master_chatgpt.png – eredeti LakeForest-kép (csak hangulat/minőség) (sha256 `34b060b88c31…`)

### 11 · A902_S01_KyotoInk_3_master_Cam_04_A – INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)
5. `05_kep4_termek_KH_Raze_asztali_lampa_bezs_marvany.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Raze_asztali_lampa_bezs_marvany.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Raze table lamp: beige marble cylinder base and beige linen drum shade, H54 × Ø22 cm (L0300109PR46) – Kave Home, a termékoldal fő képe (böngészőből, 2026-10-24) (sha256 `a0b75b414e70…`)

### 12 · A902_S02_BiBoNocturne_3_master_Cam_04_A – INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)
5. `05_kep4_termek_KH_Aleyla_asztali_lampa_bordo.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Aleyla_asztali_lampa_bordo.jpg (Kave Home – Péter képernyőképe vagy a böngészőből mentve) – termékfotó: Kave Home Aleyla table lamp: maroon (deep plum-red) metal dome Ø22 cm on a slim black stem and round black base, H33 cm (AA6514R34) – Kave Home, a termékoldal fő képe (böngészőből, 2026-10-24) (sha256 `69d45d46fcf6…`)

### 13 · A902_C1_Zenit_3_master_Cam_11_A – A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)
1. `01_kep1_blender_alap_Cam11_v2b1k11.png` ← PR #15 ág (kep004/cam11-master-panorama-javaslat): 04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png – Blender-alapkép (geometria, kamera) – PR #15 (sha256 `66fa4efbcc0d…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_uvegfal_kilatas_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 üvegfal és valós kilátás (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_Zenit_referencia.png` ← 04_renderek/ai_chatgpt/A902_Zenit_3_master_chatgpt.png – eredeti Zenit-kép (csak hangulat/minőség) (sha256 `37d17acef38c…`)

### 14 · A902_C2_LakeForest_3_master_Cam_11_A – A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)
1. `01_kep1_blender_alap_Cam11_v2b1k11.png` ← PR #15 ág (kep004/cam11-master-panorama-javaslat): 04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png – Blender-alapkép (geometria, kamera) – PR #15 (sha256 `66fa4efbcc0d…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_uvegfal_kilatas_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 üvegfal és valós kilátás (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_LakeForest_referencia.png` ← 04_renderek/ai_chatgpt/A902_LakeForest_3_master_chatgpt.png – eredeti LakeForest-kép (csak hangulat/minőség) (sha256 `34b060b88c31…`)

### 15 · A902_S01_KyotoInk_3_master_Cam_11_A – A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)
1. `01_kep1_blender_alap_Cam11_v2b1k11.png` ← PR #15 ág (kep004/cam11-master-panorama-javaslat): 04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png – Blender-alapkép (geometria, kamera) – PR #15 (sha256 `66fa4efbcc0d…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_uvegfal_kilatas_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 üvegfal és valós kilátás (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)

### 16 · A902_S02_BiBoNocturne_3_master_Cam_11_A – A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)
1. `01_kep1_blender_alap_Cam11_v2b1k11.png` ← PR #15 ág (kep004/cam11-master-panorama-javaslat): 04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png – Blender-alapkép (geometria, kamera) – PR #15 (sha256 `66fa4efbcc0d…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_uvegfal_kilatas_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 üvegfal és valós kilátás (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)
## Termékfotók forrása

- **IKEA:** az IKEA HU keresési API fő termékképe (2026-10-24).
- **Westwing:** a termékoldal og:image képe a Shopify CDN-ről (2026-10-24, változat ellenőrizve). A Toni 200×90 ára most 350 000 Ft (a rekord 320 000 Ft).
- **Kave Home** (a Macen: `00_KAVE_HOME_KEZI_MENTES/`, a repóba nem kerül):
  - 20 tétel termékképe Péter képernyőképeiből kivágva (22:55–23:12). Csak a Kave-oldal része, a csevegőablak, a fülek és a könyvjelzők nélkül. Csökkentett felbontás, alakra, arányra, színre és anyagra szolgál.
  - 3 új tétel (Brisia függeszték Ø50, Raze, Aleyla) a termékoldal fő képe, 900 × 1125 px.
    - Péter kérésére (23:39) a böngészőben olvastam az oldalt.
    - A képet a Macről töltöttem le a Kave képtárából (`d.media.kavehome.com`), 2026-10-24 23:46.
- **Méretek és foglalatok a Kave-oldalakról** (2026-10-24):
  - Eamy: 55 × 53 × 75 cm, ülésmagasság 46 cm;
  - Ciselia: 52,5 × 55 × 75 cm, ülésmagasság 47 cm, ülőlap 46 × 43 cm;
  - Brisia 4 gömbös: mennyezeti, Ø80 × 26 cm, gömbnyílás Ø49 mm;
  - **Brisia függeszték, 1 gömb Ø50** (L00152CR05): 287,10 € (akciós, eredetileg 319 €), drótos, állítható magasságú; kábel 250 cm, teljes magasság legfeljebb 153 cm; E27, max. 25 W, gömbnyílás Ø97 mm;
  - **Raze** (L0300109PR46): 89,99 €, H54 × Ø22 cm, talp Ø10, E27, max. 40 W, dugasz és kézi kapcsoló;
  - **Aleyla, bordó** (AA6514R34): 79,99 €, H33 × Ø22 cm, talp Ø15, E14, max. 25 W, dugasz és kézi kapcsoló.

## Hue-visszaellenőrzés (2026-10-25 00:00, mind a 16 prompt)

Péter kérése (22:57): „a lámpákba kell, hogy belemenjen a helyettesítő Philips Hue izzó … a legvégén ellenőrizd vissza”.
- A Hue-blokk mind a 16 promptban szó szerint szerepel (`ellenor.py`).
- G9, G4 vagy más, Hue nélküli foglalat egyik promptban sincs.
- Nem Hue-s integrált LED csak a kalibrációs koncepciókban van (LED-tükör, LED-szalag). Ezeket a RUN NOTES Hue Lightstripre vagy Hue-izzós lámpára fordítja.

| Lámpa | Hol | Foglalat (forrás: Kave-oldal) | Hue-megoldás | Állapot |
|---|---|---|---|---|
| Kave Somar Ø76, függeszték | S01 · Cam_02, Cam_03 (ML04) | E27, max. 40 W, drótos felfüggesztés | Hue E27 izzó | ✔ |
| **Kave Brisia függeszték, 1 gömb Ø50** (a 4 gömbös mennyezeti helyett) | S02 · Cam_02, Cam_03 (ML04) | E27, max. 25 W, gömbnyílás Ø97 mm | normál Hue E27 (A60) befér | ✔ |
| **Kave Raze asztali lámpa** (olvasólámpa) | S01 · Cam_04 (D20/21, D22/23) | E27, max. 40 W, nyitott vászonbúra | Hue E27 izzó | ✔ |
| **Kave Aleyla asztali lámpa, bordó** (olvasólámpa) | S02 · Cam_04 (D20/21, D22/23) | E14, max. 25 W, a kupola alatt | Hue E14 izzó | ✔ |
| Nappali ML05 | Cam_02 | nincs megnevezett lámpa (Astra: „no additional decorative fixture”) | csak Hue-kompatibilis | a Hue-blokk köti |
| Konyha ML03, munkapult-fény FL01 | Cam_03 | típus, termék nélkül | Hue-izzós lámpa, illetve Hue Lightstrip | a Hue-blokk köti |
| Master ML06, fülkefény D26 | Cam_04, Cam_11 | típus, termék nélkül | Hue-izzós lámpa, illetve Hue Lightstrip | a Hue-blokk köti |
| Fürdő FL04 (mosdó fölött), ML10 (mennyezet) | Cam_10 | kiállás, lámpatest nincs (villamos terv) | nedves zónába minősített, Hue-kompatibilis | a Hue-blokk köti |
| Terasz FL05–07 (meglévő) | Cam_02 (kívül) | ismeretlen | – | hétfői helyszíni ellenőrzés |

**Kiszűrve a Hue miatt:**
- Kave Idela asztali lámpa: G9;
- Westwing Aurelia függeszték: 6 × G9;
- Kave Brisia asztali lámpa: E27, de csak Ø49 mm-es nyílás;
- Kave Shenli: 17 cm magas, olvasásra alacsony;
- Kave Mercadal: Ø45 cm-es búra, nem fér az éjjeliszekrényre.

**A 2–3. adag lámpái (Kave-oldal, 2026-10-24):**
- Ardali Ø50: E27, max. 40 W, drótos, állítható magasságú ✔;
- Madali: E27, max. 40 W, dugasz, padlókapcsoló ✔;
- Drava: **E14**, max. 25 W, a Ø12,5 cm-es kerámiabúra alatt ✔. A bruneau.be viszonteladó E27-et ír; a Kave-oldal az irányadó.
- **Novae: beépített LED** (10 W, 3000 K, IP44) – **nem Hue-kompatibilis**. A 2–3. adag előtt Hue-kompatibilis fürdőlámpára kell cserélni.

## Verziózás

- Promptváltozás csak új verzióval (`…_v2.prompt.txt`, illetve `KEP004_ChatGPT_Images_v2/`).
- A futtatott prompt a kész kép mellé kerül: `04_renderek/ai_chatgpt/STYLE10_KEP004/`.
- A Cam_11-promptok (13–16) a draft PR #15 kamerablokkjával és alapképével készültek. Futtatni csak a PR beolvasztása után lehet, Péter „mehet”-jével. Ha a PR tartalma változik, a 13–16 új verzióban készül.

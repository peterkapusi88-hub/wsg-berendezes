# KEP-004 · ChatGPT Images · összefűzött promptok – próbakör 1 (v1, 2026-10-24 23:30)

**Mi ez:** a próbakör 12 képének (8 stíluskép S01/S02 × 4 helyiség + 4 Zenit/Lake Forest kalibráció) futtatható, összefűzött promptja.
- Képenként egy `.prompt.txt`, a ChatGPT-chatbe szó szerint bemásolandó.
- **Képgenerálás nem indult.**
- Végrehajtási terv: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004_CHATGPT_IMAGES_v1.md`.
- A képenkénti csatolmánycsomag a Macen van: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/probakor1_v1_2026-10-24/`.

## Összefűzési sorrend (minden promptban)
1. **Futtatási fejléc** (Claude): kép-ID, verzió, a küldés = Péter jóváhagyása, a csatolt képek sorrendje és szerepe, kimeneti formátum.
2. **Közös FIXED blokk** – v3.1 §1, szó szerint. Csak a markdown idézőjel (`> `) maradt le, a `{ROOM}`/`{STYLE_NAME}` helyőrző kitöltve.
3. **Helyiség-FIXED blokk** – v3.1 §2, szó szerint. **Cam_10:** a rögzített kamerablokk v1 váltja az ideiglenes blokkot (`A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`).
4. **Philips Hue követelmény** – `A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`, szó szerint (Péter, 22:57).
5. **Csak master (Cam_04):** gardróbfal-döntés – `A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md` blokkja szó szerint (Péter, 22:37–22:40) + a stílus frontsora.
6. **Stílusblokk** – Astra V2 r1, szó szerint (S01/S02). Kalibrációnál: v3.1 §3 C1/C2 szöveg + a koncepció-doksi A-902-es cellája, szó szerint.
7. **RUN NOTES** (Claude): ahol a stílusblokk „Inputs” sora eltér, ezek érvényesek. Tartalom: régi útvonal, nem 05.1-es fotók, fürdőfotók besorolása, Eamy- és Ciselia-méret, a Brisia mennyezeti rögzítése, Hue-ellenőrzés, a Kave-képek eredete.

**A v1 véglegesítése a commit előtt (nem futott még egyik sem):**
- 23:12 – Brisia: a Kave méretrajza szerint mennyezeti lámpa (Ø80 × 26 cm), nem függeszték. RUN NOTES-sor, és a termékleírás javítva.
- 23:25 – Kave Home-termékképek: Péter képernyőképeiből kivágva (6 próbaköri + 14 tétel a 2–3. adaghoz). Ciselia-méret a méretrajzból. Somar: „Hanging method: Wire” (függeszték).

**Nem módosított forrásfájlok (sha256):**

| Fájl | sha256 |
|---|---|
| `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` | `06b28c8e7374e2554d65eeb4bf3c6639f2aab87f4fc54e9ed7ee1f1acfe40d32` |
| `05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md` | `6549a09b61d2131efa68f7d7575a309e379a6665de4b3217228e3881c9456a96` |
| `05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md` | `aebff8b51d988f5f4a0f10c7ceb533be0f03d7251e2329b05733baa7e39ca163` |
| `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md` | `f48745e46e9242e8bdb531baad969aacd0a4a497740347311dd760a8de5274a7` |
| `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md` | `d0e5a843135363c96d815c3eb31b20361b068a93f2a47066be450ad90dd1c8c3` |
| `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` | `3962dba2f88cf61409240aeddf2aebdb7c3f94062cc877777371ba728c0caead` |

## Ellenőrzés (2026-10-24 23:27, `ellenor.py`)
Minden promptban szó szerint megvan a közös FIXED, a helyiség-FIXED, a Hue-blokk, a mastereknél a gardróbblokk és a frontsor, és az Astra-stílusblokk vagy a §3 kalibráció + koncepció-cella. A kép-ID egyezik Astra „Output” sorával, nem maradt helyőrző, a fejléc csatolmánylistája egyezik a csomag fájljaival. **Hiba: 0.**

| # | Kép-ID | Lépés | Karakter | Csatolmány | Kave kézi | prompt sha256 |
|---|---|---|---|---|---|---|
| 01 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | 1a | 8212 | 5 | 0 | `d46f4747ab5c8a15…` |
| 02 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | 1a | 8142 | 5 | 0 | `699a2cefaf536576…` |
| 03 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | 1a | 13568 | 9 | 0 | `3576f547ef537b9e…` |
| 04 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | 1a | 14322 | 9 | 0 | `1c315f2798da6bd2…` |
| 05 | `A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A` | 1a | 12728 | 8 | 0 | `b1ae5f5061fd68d7…` |
| 06 | `A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A` | 1a | 13359 | 8 | 0 | `4424f0ccd87c3a2b…` |
| 07 | `A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A` | 1b | 12398 | 3 | 0 | `25a4745aef45715b…` |
| 08 | `A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A` | 1b | 12456 | 3 | 0 | `5c79e72602daed13…` |
| 09 | `A902_C1_Zenit_3_master_Cam_04_A` | 1c | 9421 | 4 | 0 | `09c3ceaff251ab15…` |
| 10 | `A902_C2_LakeForest_3_master_Cam_04_A` | 1c | 9379 | 4 | 0 | `5ab509e790ea1e87…` |
| 11 | `A902_S01_KyotoInk_3_master_Cam_04_A` | 1c | 11950 | 4 | 0 | `6ba944cc7850e9c1…` |
| 12 | `A902_S02_BiBoNocturne_3_master_Cam_04_A` | 1c | 11958 | 4 | 0 | `dc261d3a9670cc69…` |

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
7. `07_kep4_termek_KH_Eamy_szek_vilagosszurke.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Eamy_szek_vilagosszurke.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Eamy chair, light-grey chenille, natural ash (KH-CH-EAMY-LG) – Kave Home, Péter képernyőképéből kivágva (sha256 `3eb2830c3754…`)
8. `08_kep4_termek_KH_Nifelia_szonyeg_200x300.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Nifelia_szonyeg_200x300.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Nifelia beige wool jacquard rug 200 × 300 (KH-RUG-NIFELIA) – Kave Home, Péter képernyőképéből kivágva (sha256 `8071584b73ca…`)
9. `09_kep4_termek_KH_Somar_fuggesztek_76.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Somar_fuggesztek_76.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Somar pendant Ø76 (KH-PL-SOMAR76) – Kave Home, Péter képernyőképéből kivágva (sha256 `ea936eca0ba2…`)

### 04 · A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam02_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png – Blender-alapkép (geometria, kamera) (sha256 `cb60ec8ebc5b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_helyszin_falak-profilok-terasz.jpg` ← helyszin_kontaktlap_Cam02.jpg – helyszíni fotók: fal, profil, terasz (kontaktlap) (sha256 `2a5ef83f2d6d…`)
4. `04_kep2c_panorama_terasz.jpg` ← 02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg – valós panoráma (sha256 `9d0457ee8479…`)
5. `05_kep4_termek_ikea_JATTEBO_U_Samsala_sotetkek_49607648.jpg` ← ikea_JATTEBO_U_Samsala_sotetkek_49607648.jpg – termékfotó: IKEA JÄTTEBO 3.5-seat modular U with two chaises, Samsala dark blue (P04) (sha256 `a9f482e59e27…`)
6. `06_kep4_termek_ww_Anouk_uveg_180x90_23WES68910.jpg` ← ww_Anouk_uveg_180x90_23WES68910.jpg – termékfotó: Westwing Anouk clear glass dining table 180 × 90 cm (P08) (sha256 `1c330875218b…`)
7. `07_kep4_termek_KH_Ciselia_szek_bezs_fekete.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Ciselia_szek_bezs_fekete.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Ciselia chair, beige chenille, black steel legs (KH-CH-CISELIA-BK) – Kave Home, Péter képernyőképéből kivágva (sha256 `3b5449507116…`)
8. `08_kep4_termek_KH_Marely_szonyeg_feher_200x300.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Marely_szonyeg_feher_200x300.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Marely white wool rug 200 × 300 (KH-RUG-MARELY-W) – Kave Home, Péter képernyőképéből kivágva (sha256 `afa79d72147f…`)
9. `09_kep4_termek_KH_Brisia_fuggesztek_sargarez.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Brisia_fuggesztek_sargarez.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Brisia ceiling-mounted light (not a pendant), brushed brass, four frosted glass globes Ø15 cm, overall Ø80 × 26 cm high (KH-PL-BRISIA) – Kave Home, Péter képernyőképéből kivágva (sha256 `2f18cb176f69…`)

### 05 · A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam03_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_03_etkezo-konyha.png – Blender-alapkép (geometria, kamera) (sha256 `f6f3ca25bb06…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_konyhafal_ME-BAL-056.jpg` ← 08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg – helyszíni fotó: konyhafal, kiállások, mellvéd (sha256 `cb316cd7d1de…`)
4. `04_kep2c_nappali_terasz_fele_ME-BAL-045.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg – helyszíni fotó: fal, profil (sha256 `06981c280964…`)
5. `05_kep4_termek_ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg` ← ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg – termékfotó: Westwing Toni oval dining table 200 × 90 cm, light oak veneer (P09) (sha256 `da0652a02a2f…`)
6. `06_kep4_termek_ikea_EKBACKEN_vilagosszurke_beton_40616275.jpg` ← ikea_EKBACKEN_vilagosszurke_beton_40616275.jpg – termékfotó: IKEA EKBACKEN worktop, light-grey concrete-effect laminate (AG-31) (sha256 `8bdae8b0f22b…`)
7. `07_kep4_termek_KH_Eamy_szek_vilagosszurke.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Eamy_szek_vilagosszurke.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Eamy chair, light-grey chenille, natural ash (KH-CH-EAMY-LG) – Kave Home, Péter képernyőképéből kivágva (sha256 `3eb2830c3754…`)
8. `08_kep4_termek_KH_Somar_fuggesztek_76.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Somar_fuggesztek_76.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Somar pendant Ø76 (KH-PL-SOMAR76) – Kave Home, Péter képernyőképéből kivágva (sha256 `ea936eca0ba2…`)

### 06 · A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A – INDÍTHATÓ – Péter „mehet”-je után (1a lépés)
1. `01_kep1_blender_alap_Cam03_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_03_etkezo-konyha.png – Blender-alapkép (geometria, kamera) (sha256 `f6f3ca25bb06…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_konyhafal_ME-BAL-056.jpg` ← 08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg – helyszíni fotó: konyhafal, kiállások, mellvéd (sha256 `cb316cd7d1de…`)
4. `04_kep2c_nappali_terasz_fele_ME-BAL-045.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg – helyszíni fotó: fal, profil (sha256 `06981c280964…`)
5. `05_kep4_termek_ww_Anouk_uveg_180x90_23WES68910.jpg` ← ww_Anouk_uveg_180x90_23WES68910.jpg – termékfotó: Westwing Anouk clear glass dining table 180 × 90 cm (P08) (sha256 `1c330875218b…`)
6. `06_kep4_termek_ikea_EKBACKEN_szurke-bezs_ko_20604320.jpg` ← ikea_EKBACKEN_szurke-bezs_ko_20604320.jpg – termékfotó: IKEA EKBACKEN worktop, grey-beige stone-effect laminate (AG-33) (sha256 `41caab249954…`)
7. `07_kep4_termek_KH_Ciselia_szek_bezs_fekete.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Ciselia_szek_bezs_fekete.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Ciselia chair, beige chenille, black steel legs (KH-CH-CISELIA-BK) – Kave Home, Péter képernyőképéből kivágva (sha256 `3b5449507116…`)
8. `08_kep4_termek_KH_Brisia_fuggesztek_sargarez.jpg` ← 00_KAVE_HOME_KEZI_MENTES/KH_Brisia_fuggesztek_sargarez.jpg (kivágás Péter Kave-képernyőképéből) – termékfotó: Kave Home Brisia ceiling-mounted light (not a pendant), brushed brass, four frosted glass globes Ø15 cm, overall Ø80 × 26 cm high (KH-PL-BRISIA) – Kave Home, Péter képernyőképéből kivágva (sha256 `2f18cb176f69…`)

### 07 · A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A – INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)
1. `01_kep1_blender_alap_Cam10_v2b1k10.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png – Blender-alapkép (geometria, kamera) (sha256 `25c818fdc30f…`)
2. `02_kep2_furdo06-2_zuhany_mosdo_ME-BAL-064.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg – helyszíni fotó 06.2: zuhany, mosdó, burkolat, dekor (sha256 `6e577ef470a7…`)
3. `03_kep2b_furdo06-2_wc_torolkozoszarito_ajto_ME-BAL-066.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg – helyszíni fotó 06.2: WC, törölközőszárító, ajtó (sha256 `6b50e8a59bf6…`)

### 08 · A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A – INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)
1. `01_kep1_blender_alap_Cam10_v2b1k10.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png – Blender-alapkép (geometria, kamera) (sha256 `25c818fdc30f…`)
2. `02_kep2_furdo06-2_zuhany_mosdo_ME-BAL-064.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg – helyszíni fotó 06.2: zuhany, mosdó, burkolat, dekor (sha256 `6e577ef470a7…`)
3. `03_kep2b_furdo06-2_wc_torolkozoszarito_ajto_ME-BAL-066.jpg` ← 08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg – helyszíni fotó 06.2: WC, törölközőszárító, ajtó (sha256 `6b50e8a59bf6…`)

### 09 · A902_C1_Zenit_3_master_Cam_04_A – BLOKKOLT – a Cam_04/Cam_11 döntésig (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_Zenit_referencia.png` ← 04_renderek/ai_chatgpt/A902_Zenit_3_master_chatgpt.png – eredeti Zenit-kép (csak hangulat/minőség) (sha256 `37d17acef38c…`)

### 10 · A902_C2_LakeForest_3_master_Cam_04_A – BLOKKOLT – a Cam_04/Cam_11 döntésig (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep3_eredeti_LakeForest_referencia.png` ← 04_renderek/ai_chatgpt/A902_LakeForest_3_master_chatgpt.png – eredeti LakeForest-kép (csak hangulat/minőség) (sha256 `34b060b88c31…`)

### 11 · A902_S01_KyotoInk_3_master_Cam_04_A – BLOKKOLT – a Cam_04/Cam_11 döntésig (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)

### 12 · A902_S02_BiBoNocturne_3_master_Cam_04_A – BLOKKOLT – a Cam_04/Cam_11 döntésig (1c lépés)
1. `01_kep1_blender_alap_Cam04_v2b1.png` ← 04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png – Blender-alapkép (geometria, kamera) (sha256 `ee9cdf86748b…`)
2. `02_kep2_padlo_ME-BAL-080.jpg` ← 08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg – helyszíni fotó: padló (sha256 `88f93864ec97…`)
3. `03_kep2b_05-1_szoba_ME-BAL-077.jpg` ← 08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg – helyszíni fotó: 05.1 (fal, fülke, pillér, profil) (sha256 `1fd3ee6db322…`)
4. `04_kep4_termek_ikea_NORDLI_20349853.jpg` ← ikea_NORDLI_20349853.jpg – termékfotó: IKEA NORDLI white storage bed 180 × 200 (P10) (sha256 `9666446a9166…`)
## Termékfotók forrása

- **IKEA:** IKEA HU keresési API fő termékképe (2026-10-24).
- **Westwing:** a termékoldal og:image képe a Shopify CDN-ről (2026-10-24, változat ellenőrizve). A Toni 200×90 ára most 350 000 Ft (a rekord 320 000 Ft).
- **Kave Home:** az oldal tiltja a gépi lekérést, ezért Péter képernyőképeiből vágtam ki a termékképeket (2026-10-24 22:55–23:12).
  - Csak a Kave-oldal részét vágtam ki, a csevegőablak, a fülek és a könyvjelzők nélkül.
  - A képek a Macen vannak: `00_KAVE_HOME_KEZI_MENTES/`, a forrás-képernyőképek a `forras_kepernyokepek_2026-10-24/` mappában. A repóba nem kerülnek.
  - A felbontás csökkentett: a képek alakra, arányra, színre és anyagra szolgálnak.
- **Méretek a Kave-méretrajzokból** (Péter képernyőképei, 2026-10-24):
  - Eamy: 55 × 53 × 75 cm, ülésmagasság 46 cm;
  - Ciselia: 52,5 × 55 × 75 cm, ülésmagasság 47 cm, ülőlap 46 × 43 cm;
  - Brisia: Ø80 × 26 cm, rozetta Ø16, gömbök Ø15.

## Hue-visszaellenőrzés (2026-10-24 23:28, mind a 12 prompt)

Péter kérése (22:57): „a lámpákba kell, hogy belemenjen a helyettesítő Philips Hue izzó … a legvégén ellenőrizd vissza”.
- A Hue-blokk mind a 12 promptban szó szerint szerepel (`ellenor.py`).
- G9, G4 vagy más, Hue nélküli foglalat egyik promptban sincs.
- Nem Hue-s integrált LED csak a kalibrációs koncepciókban van (LED-tükör, LED-szalag). Ezeket a RUN NOTES Hue Lightstripre vagy Hue-izzós lámpára fordítja.

| Lámpa | Hol | Foglalat (forrás) | Hue-megoldás | Állapot |
|---|---|---|---|---|
| Kave Somar Ø76, függeszték | S01 · Cam_02, Cam_03 (ML04) | E27, max. 40 W, drótos felfüggesztés (Kave-specifikáció, képernyőkép 23:02) | Hue E27 izzó | ✔ |
| Kave Brisia, mennyezeti (Ø80 × 26 cm) | S02 · Cam_02, Cam_03 (ML04) | E27, max. 25 W, gömbnyílás Ø49 mm (Kave-specifikáció, képernyőkép 23:02) | Hue Lustre E14 (Ø45 × 77 mm, Philips Hue termékoldal) + E27→E14 adapter | **feltételes**: a befér-e próbája és Péter döntése |
| Nappali ML05 | Cam_02 | nincs megnevezett lámpa (Astra: „no additional decorative fixture”) | csak Hue-kompatibilis | a Hue-blokk köti |
| Konyha ML03, munkapult-fény FL01 | Cam_03 | típus, termék nélkül | Hue-izzós lámpa, illetve Hue Lightstrip | a Hue-blokk köti |
| Master: olvasólámpák D20–D23, ML06, fülkefény D26 | Cam_04 | típus, termék nélkül; **Astra: termék és rögzítés „pre-image gate”** | Hue-izzós lámpa, illetve Hue Lightstrip | **1c-kapu**: termék kell |
| Fürdő FL04 (mosdó fölött), ML10 (mennyezet) | Cam_10 | kiállás, lámpatest nincs (villamos terv) | nedves zónába minősített, Hue-kompatibilis | a Hue-blokk köti |
| Terasz FL05–07 (meglévő) | Cam_02 (kívül) | ismeretlen | – | hétfői helyszíni ellenőrzés |

**A 2–3. adaghoz kell még** (Kave „Specifications → Lampholder”):
- Ardali, Drava, Madali: mindháromnál „Light bulb sold separately”, a foglalat nincs rögzítve.
- Novae: nincs adat, integrált LED is lehet.

## Verziózás

- Promptváltozás csak új verzióval (`…_v2.prompt.txt`, illetve `KEP004_ChatGPT_Images_v2/`).
- A futtatott prompt a kész kép mellé kerül: `04_renderek/ai_chatgpt/STYLE10_KEP004/`.
- A Cam_11 jóváhagyása esetén a 4 master-prompt a `A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md` blokkjával újra-összefűzve, új verzióban készül (PR #15).

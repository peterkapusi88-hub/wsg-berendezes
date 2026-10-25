# S01 Cam_12 – javított ChatGPT Images tesztcsomag (NINCS legenerálva) – 2026-10-25

**Státusz:** KONCEPCIÓ – NEM VALIDÁLT. Ez a csomag előkészítés: képet nem generáltam, ChatGPT-t és Chrome-ot nem használtam.
- Küldés csak Péter „mehet”-je után.
- A képeket ebben a sorrendben kell csatolni: 1 → 1b → 2 → 3. Ezután jön az üzenet szövege (`UZENET_S01_Cam12_v3_KORR.txt`).

| # | Fájl | Szerep | Méret | SHA256 |
|---|---|---|---|---|
| image 1 | `01_image1_A902_Cam12v3_KORR_semleges.png` | **kötelező geometriai és kamera-referencia** (Cam_12 v3, új, olvashatóbb semleges render) | 1600 × 1000 | `8ffd40c0ea76f4473959edd69dfdeb959e8197f3a59418c8fbb27e01fc0d231d` |
| image 1b | `01b_image1b_A902_S01_Cam12v3_KORR_tombrender.png` | ugyanaz a kamera, S01 tömbrender (hely és méret) | 1600 × 1000 | `03068ad637b8dc72f6da1f655401a2dc110234204db5029ce6bf589664323e8b` |
| image 2 | `02_image2_A902_04_ME-BAL-080_parketta_szegely_kozel.jpg` | valódi padló és szegély – csak anyag- és színreferencia | 1200 × 1600 | `88f93864ec97ff2fd9fbd548680dc76fe01b21583599ab378cd49f07b4e3480e` |
| image 3 | `03_image3_A902_04_ME-BAL-046_nappali_eloter_fele.jpg` | helyszíni fotó – csak a meglévő felületek ellenőrzésére, **nem kamera-referencia** | 1600 × 1200 | `d1f35e57d8d57b9088cc045de5ae6b375fe2a1409f2ea66fab03b459dde0b95b` |
| üzenet | `UZENET_S01_Cam12_v3_KORR.txt` | javított burkolóüzenet: képszerepek + GEOMETRY LOCK + a Fable-prompt szó szerint | 12 692 karakter | `222fccf5f93f1a7e790e0cacfd4d60d77d1be0819fd8b5d523d12af1299be0d7` |

## Források és verziók
- **image 1 és 1b:**
  - forrás: a v2b-1-k13 blend másolata (sha256 `e01170d315193f8785bbeee5f7d319ce3c8adec886375962cee83e0a3f70ddbd`);
  - lock v2b-1-k13 (`2ca93735…3d1b`);
  - Blender 5.2.3 LTS, EEVEE, 256 minta, AgX Medium High Contrast;
  - szkript: `03_blender/geometry_v2/cam12_v3_korrekcio/01_render_cam12v3.py`, futásnapló: `naplok/cam12v3_korr_log.json`;
  - a semleges kép validátor-eredménye: PASS 0/0.
- **Kamera:** Cam_12_Nappali_Hero, [4,40; 7,88; 1,60], irány −48° (rot_z −138°), vízszintes, 22 mm, shift_y −0,05, szenzor 36 mm AUTO, 1600 × 1000. Egyezik a `GEOMETRIA_C_KAMERACSOMAG_v2.md` 3. pontjával.
- **image 2 és 3:** `08_allapotfelmeres/fotok/A902/04_nappali/` (2026-10-21), változatlan másolat.
- **Fable-prompt:**
  - `competition/fable51-v3-1-20261025` @ `b44541205cdd79e3d1f33ee8074c2bc280beb7a7`, `05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/A902_S01_KyotoInk_1_nappali-hero_Cam_12_A.prompt.md` (blob `fcbb4e23…`);
  - a BEGIN/END közti szöveg bájtra azonos (7525 bájt, sha256 `55acae0e86d5e550a180846bb65874d1738d90cce3081912a3254c4d937c1afe`);
  - a versenyző fájlját nem módosítottam.
- **Előző, hibás futás referenciája:** `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png` (sha `66a9c6af…1d87e`), ugyanabból a blendből és kamerából, de EEVEE fény nélkül, fehér a fehéren.

## Másolatok
- Mac: `~/Downloads/WSG_CAM12_V3_KORREKCIO/csomag_S01/` (a Chrome-os csatoláshoz).
- Konténer: `/home/claude/wsg-cam12-csomag/` (a Chrome-feltöltő csak `/home/claude` alól olvas).

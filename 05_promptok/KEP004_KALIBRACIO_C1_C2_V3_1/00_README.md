# KEP-004 · C1 Zenit / C2 Lake Forest kalibrációs promptok – V3.1 (v1, 2026-10-25 04:50 CET)

**Mire:** a WSG Design Challenge 2026 (Astra · Fable · Opus) közös mércéje. Péter döntése (2026-10-25 04:03, 04:27): versenyzőnként **60 saját prompt + e 6 közös kalibráció = 66 képes készlet**; a hat kalibrációt **egyszer, Claude** írja, a versenyzők **nem** írnak C1/C2 promptot, de a 66 soros manifestjükben a 61–66. sor `KOZOS` státusszal erre a mappára mutat. A regiszter 61–66. sora (`05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv`), kep_id betű szerint.

**Mit mutat:** a v1 Zenit- és Lake Forest-koncepció (`06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md`) újratervezve a valódi A-902 héjban, V3.1-szinten: minden látható tömör falnak terve van, Hue-fény, C elrendezés (PR #18, Péter döntése), valós termékméretek. **Szerep: a kreatív minimum referenciája, nem versenyző.** Nem helyettesíti az S06 Zenit Atelier és az S07 Lake Forest Couture teljes stílusát.

**Státusz:** `COMPLETE` kreatív prompt, `NEEDS_CLAUDE_VALIDATION` – nem futtatható csomag. Futtatható csomagot Claude a Blender-ellenőrzött FIXED/FRAME LAYOUT blokkokkal és az eredeti helyszíni referenciákkal épít, a stílusképekkel azonos kapukkal.

## Fájlok
| nr | kep_id | kamera | fény | karakter |
|---|---|---|---|---|
| 61 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | Cam_02 | nappal | 5 796 |
| 62 | `A902_C1_Zenit_3_master_Cam_04_A` | Cam_04 | este, Hue | 4 846 |
| 63 | `A902_C1_Zenit_3_master_Cam_11_A` | Cam_11 | nappal | 3 847 |
| 64 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | Cam_02 | nappal | 5 604 |
| 65 | `A902_C2_LakeForest_3_master_Cam_04_A` | Cam_04 | este, Hue | 5 061 |
| 66 | `A902_C2_LakeForest_3_master_Cam_11_A` | Cam_11 | nappal | 3 936 |

Mind a hat `20_PROMPTOK/<kep_id>.prompt.md`, `=== BEGIN PROMPT <kep_id> ===` / `=== END PROMPT <kep_id> ===` jelölőkkel; helykitöltő nincs (gépi ellenőrzés 04:50).

## Közös tények a promptokban (forrás)
- Kamerák: r2 brief §11.11; Cam_11 blokk `05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md`.
- Elrendezés C: `ai-coordination/results/WSG-20261025-A902-ELRENDEZES-ALT_r1.md` (PR #18) – 2+2+1+1 az ML04 alatt, kanapé nyugatabbra, fő utak ≥ 0,90 m; igazolt asztalok: Toni 160 × 90 (L, 180 mély) és Anouk 180 × 90 (U, 160 mély). A kalibrációkban Nealy ovális 160 × 90 szerepel – a Martina (C1) és a Gala U (C2, 225 mély) kanapéval az elférés az integrációnál méretpróbával igazolandó („elrendezésben ellenőrizendő”).
- Gardróbfal 05.1: `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md`.
- Hue-szabály: `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`; fajlagos árak: `ai-coordination/inputs/A902_verseny/HUE_ALAPCSOMAG_v1.md`.
- Termékek és méretek: `ai-coordination/inputs/A902_v2b/KOLTSEG_ELOSZURES_4STILUS_A902.md` (Kave Home webshop, 2026-10-24: Martina, Corvena, Mosi, Nealy, Eamy, Selven, Gala, Sylo, Sheffield, Ciselia, Brisia). A Zenit/LF „eredeti” tételek (ív-állólámpa, gyűrűlámpa, gömb-csillár, pouf, éjjelik, pad) replika/analóg, `becslés` státusszal.
- Padló, nyílászárók, fürdő, terasz: Render Reality Gate A. pont és a v3.1 sablon §1.

## Eltérés a v1 kalibrációs promptoktól (`KEP004_ChatGPT_Images_v1/`)
A v1 „semleges borús fény, fehér falak, P902_24A” szabályát a V3.1 (r2 §11.6, §11.3) és a C elrendezés váltja; a v1 fájlok érintetlenek maradnak.

## Nyitott (Claude, integrációkor)
- A C elrendezés végleges kanapé-koordinátái a kameracsomag (Cam_03 K1 + Cam_12 újrakivágás) validálása után; a promptok a méretezett szándékot adják.
- A Gala U 300 × 225 a C-ben a JÄTTEBO U-befoglalóval (285 × 160) ellenőrzendő: mélysége 225 → a kanapé–TV távolság a `tv_melyseg.py` futtatásával igazolandó.
- Az éjjeli/olvasólámpa betáplálása (D26/D20) a kiállás-CSV-vel egyeztetendő.

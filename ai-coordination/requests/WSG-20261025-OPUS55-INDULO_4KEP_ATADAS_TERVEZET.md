# A-902 · Opus 5.5 V3.1 – négyképes induló tesztcsomag (képgenerálási átadás) – r2, **NEM INDÍTHATÓ, renderengedély nincs**

**Claude integrátor, 2026-10-25.** Képet nem generáltam. Forrás: Opus PR #22 **`7d3c67f`** + integrátori szövegcsere **v1.2**. Kapuk: `ai-coordination/audits/WSG-20261025-OPUS55-V3_1-PR22_INTEGRATOR_AUDIT.md` (r2) és `03_blender/integrator_opus55/BLENDER_JELENTES_OPUS55_S01_S02.md` (5–6. pont). A b24bee7-alapú r1-csomag és a v1.1 promptok elavultak (`05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_1_TERVEZET_b24bee7/` – csak tervezet).

## Indíthatóság
| # | Kép-ID | Állapot | Ami még kell |
|---|---|---|---|
| 1 | `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A` | **technikailag kész, engedély nélkül** | Péter elfogadja a v1.2-t és „mehet”-et ad; push (lásd lent). Blender: W02 100 % takaratlan, minden út OK. |
| 2 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | **technikailag kész, engedély nélkül** | ua.; felirat: „teraszajtó feltételes” (K-04) |
| 3 | `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A` | **BLOKKOLT** | K-05: a látható ML04 Kave Home Idela foglalata nem igazolt (Hue); K-06: fekete Toni visszaellenőrzése |
| 4 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | **BLOKKOLT** | K-06; dohányzóasztal (K-08). Az ML04 itt nem látszik, de a stílus egy terv (Cam_12-vel azonos lámpa) – K-05 is kell. |

Sorrend (GOAL §7): 1 → 2 → 3 → 4, egyesével, ChatGPT Images-szel, hero először.

## Promptverzió (futtatandó fájlok)
`05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_2_7d3c67f/`

| # | Fájl | Forrás (7d3c67f) sha256 | v1.2 sha256 | Karakter |
|---|---|---|---|---|
| 1 | `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A_v1_2.prompt.md` | `914f0b9e…` | `95a34f6998b5fec723f7d1f275f3ce959c970c59807bfc8ce08d328494e9bfa1` | 5601 |
| 2 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_v1_2.prompt.md` | `7096e13f…` | `68f66d63581ff31e18fd0ee267eb8fcde2a942410473dabea812f1a691846651` | 6299 |
| 3 | `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A_v1_2.prompt.md` | `0a1b8cbf…` | `c89b71d1a2f94f60fdbe3c52d0c3422de2ed2ee20020175b35d4cba275f9037e` | 5256 |
| 4 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_v1_2.prompt.md` | `91b2ffb3…` | `bc8b73e6867d9d296ec43d1325771ebfa5e0a8c6cc2d0eb71ff78f2acefa7e99` | 5908 |

Cserék: K-02 (Cam_02: az ML04 a képen kívül, tiltósor), K-03 (Cam_12: a W02-növény törölve, tiltósor). Részletek és újraalkalmazás: a mappa `README.md`-je. A versenyzői fájlok és a stílusdokumentáció változatlanok.

## Csatolmányok (sorrendben)
| Szerep | Cam_12 v3 (1., 3.) | Cam_02 (2., 4.) |
|---|---|---|
| **1. kép – semleges Blender-alap** | `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png` (sha `66a9c6af…`) | `04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png` (sha `cb60ec8e…`) |
| **2. kép – valós padló** | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg` (sha `88f93864…`) | ua. |
| 2b – falak, profilok | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg` (sha `06981c28…`; **az A902-es**) | ua. |
| 2c – **valós terasz, kilátás, káva** | – | `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg` (sha `9d0457ee…`) + `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-053_teraszajto_sotet_tegla_kava.jpg` (sha `e92696e9…`) |
| 3. – termékképek | a Macen (`~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/…`). **S01:** Lennon L jobbos tóp, Toni ovális világos tölgy (a fájl 200 × 90-es fotó: csak anyag és forma), Eamy világosszürke, Nifelia 200 × 300, Somar Ø 76, **Westwing Misaki** (DEQ21WES21200 – új kép kell). **S02:** JÄTTEBO U Samsala sötétkék (IKEA 49607648), Ciselia, Marely, **Westwing Dancing** (DEQ24AUD33907 – új kép kell), **Kave Home Idela** (új kép kell), fekete Toni (nincs igazolt kép) | ua. |

## Render Reality Card – közös rész
| Felület | Állapot | Forrás | Képen |
|---|---|---|---|
| Padló | MEGLÉVŐ / MEGTARTOTT | Egger laminált; terv: EL2184 Grey Treviso Oak, Aqua+ (IGAZOLT-D); fotó ME-BAL-080 vizuálisan megfelel; termékkód és deszkairány a helyszínen NEM IGAZOLT | szürkésbarna, göcsös tölgyhatású laminált + 6 cm-es azonos dekorú szegőléc, a fotó szerint |
| Mennyezet | MEGLÉVŐ | fehér, HF03 hűtő-fűtő mező | rajta csak az ML04/ML05 lámpa |
| Ajtók, profilok | MEGLÉVŐ | világosszürke ajtó, fekete kilincs; profil belül fehér, kívül antracit (IGAZOLT-F) | változatlan |
| Belmagasság | MEGLÉVŐ | 2,90–2,93 m (IGAZOLT-M) | – |
| Bútor | ÚJ / ÁRAZOTT | Opus 40-es lista (7d3c67f) – az árak webes visszaellenőrzése nyitott | a Blender-tömbbel egyező hely és méret |
| Státusz | **KONCEPCIÓ – NEM VALIDÁLT** | RRG §D | a képen és a fájlnévben |

### 1. S01 Cam_12 v3 (nappal)
Új felületek: W02 + W07 washi-hatású vinil, grafit tintavonal-sín z 2,10, W03 szemöldöksáv, W02 tusvonás-mű 120 × 200, konyha METOD + grafit laminált front, KARLBY tölgy, grafit hátfestett üveg. Lámpák: ML04 Somar Ø 76 (árkönyvtár, 246 990), ML05 Misaki Ø 40 × 70 (107 970, ellenőrzött). Blender: kanapé 16,5 %, W02 takaratlan 100 %, állóhely szabad. S01 lakásszint fő: 17,27 M (fix 8,40-nel). Nem igazolt: Somar függesztési magassága; S01 spec ML05-sora (K-07).

### 2. S01 Cam_02 (kék óra)
W01 KI-A washi-lámpásfal (panel ≤ 4 cm, torony 60 × 40 × 253, úszó pad 260 × 42), Hue a fugákban (FELTÉTELES – D18) és a pad alatt (D16/D17). Blender: TV-fal 25,5 %, takaratlan 96,8 %; **ML04 a képen kívül** (v1.2 kezeli). Teraszajtó: hat szék csak középső szárnnyal.

### 3. S02 Cam_12 v3 (nappal)
Navy laminált lábazat 1,8 cm z 1,10-ig, ezüstszürke vinil, kék–szilva mű 140 × 180, navy konyha, füstbronz tükör hátfal. Lámpák: **ML04 Kave Home Idela Ø 26 (FELTÉTELES – foglalat)**, ML05 Westwing Dancing Ø 65 × 38 (E27, 253 980, ellenőrzött). Blender: kanapé 23,3 %, W02 takaratlan 85,7 %, a hálók felé ≈ 0,907 m. S02 lakásszint fő: 17,69 M – a legkisebb tartalék (0,31 M).

### 4. S02 Cam_02 (kék óra)
W01 BN-A éjkék kabinetfal, ezüst mező, két füstbronz tükörrés, Hue-ellenfény (FELTÉTELES – D18). Blender: TV-fal 25,0 %, takaratlan 94,0 %; ML04 a képen kívül (v1.2). Nyitott: dohányzóasztal a U-ban (K-08), fekete Toni (K-06).

## Kép utáni kötelező audit (RRG §C)
Képenként: `elem | forrás | tervezett felület | képen | eltérés | Ft-kockázat | bizonyíték | döntés`. Külön: padló tónusa a ME-BAL-080-hoz; nincs-e lámpa a Cam_02 jobb szélén; nincs-e növény a W02 előtt; tükörreflexió; navy nem lakkfényes.

## Mentés
Csak a saját integrátori ágon: `integrator/opus55-v3-1-audit-20261025`. A main, a PR #22 és a versenyzői ág érintetlen. **Távoli push:** ebből a munkamenetből nem lehetséges (GitHub-hitelesítés nincs) – az ág és a commitok csak helyben léteznek, a távoli visszaolvasás nem igazolt.

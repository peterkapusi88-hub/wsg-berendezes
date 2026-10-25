# A-902 · Opus 5.5 V3.1 – négyképes induló tesztcsomag (képgenerálási átadás) – **TERVEZET, NEM INDÍTHATÓ**

**Claude integrátor, 2026-10-25.** Képet nem generáltam. A csomag csak a két kapu lezárása és Péter „mehet”-je után futtatható. Kapuk: `ai-coordination/audits/WSG-20261025-OPUS55-V3_1-PR22_INTEGRATOR_AUDIT.md` (1., IDEIGLENES) és `03_blender/integrator_opus55/BLENDER_JELENTES_OPUS55_S01_S02.md` (2., FELTÉTELES PASS).

## Indíthatóság
| # | Kép-ID | Most | Feltétel az indításhoz |
|---|---|---|---|
| 1 | `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A` | **BLOKKOLT** | ~~K-03~~ (v1.1-ben javítva) · K-01 (a 7d3c67f-változat egyezése) → **elsőként indítható** |
| 2 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | **BLOKKOLT** | ~~K-02~~ (v1.1-ben javítva) · K-01; a Misaki igazolása ajánlott (K-07) |
| 3 | `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A` | **BLOKKOLT** | ~~K-03~~ (v1.1) · K-01 + **K-06** (fekete Toni 160 × 90 igazolása vagy cseréje) |
| 4 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | **BLOKKOLT** | ~~K-02~~ (v1.1) · K-01 + K-06; dohányzóasztal-termék (K-08) |

Sorrend (GOAL §7, Péter 03:32–04:10): hero először – 1 → 2 → 3 → 4, egyesével, ChatGPT Images-szel.

## Promptverzió
A pontos verzió a **7d3c67f** fájlja lesz; ezt a lehúzás után kell a lenti sha256-okkal összevetni. Ha eltér, a kártya új verziót kap.

| Kép | Fájl (Opus-ág) | sha256 @ b24bee7 | Karakter |
|---|---|---|---|
| 1 | `05_promptok/KEP004_OPUS55_V3_1_r1/20_PROMPTOK/A902_S01_KyotoInk_1_nappali-hero_Cam_12_A.prompt.md` | `914f0b9e8f0cc620e71cf75b3d225b3dac091ee8b31ce5d57283ee4ce9af46f4` | 5670 B |
| 2 | `…/A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A.prompt.md` | `7096e13f81621ea7f400c2985fd8ad1ff8b4b9dcba0437f1928f855d993d369c` | 6230 B |
| 3 | `…/A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A.prompt.md` | `5085ab2c7e70b1fe5cb962ad457dd481cdbedaeb4e873ff5b59b44b5c2287d20` | 5261 B |
| 4 | `…/A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A.prompt.md` | `dfd6ecf0476030151405018aa851cdc8e42c99884cb97ff1200b6d591f12d29f` | 5817 B |

**Futtatandó változat: integrátori v1.1 (K-02, K-03 beépítve, 2026-10-25)** – `05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_1/` (a versenyzői fájl változatlan; leírás és újraalkalmazás a 7d3c67f-re: a mappa `README.md`-je).

| Kép | Futtatandó fájl | sha256 |
|---|---|---|
| 1 | `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A_v1_1.prompt.md` | `95a34f6998b5fec723f7d1f275f3ce959c970c59807bfc8ce08d328494e9bfa1` |
| 2 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_v1_1.prompt.md` | `68f66d63581ff31e18fd0ee267eb8fcde2a942410473dabea812f1a691846651` |
| 3 | `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A_v1_1.prompt.md` | `0e103d813ae481df1a5e2aaa9fde240e92271e248f144b20a80011f0b8e12689` |
| 4 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_v1_1.prompt.md` | `b24fcdcaced164455ba672596259214cd3bd207637c90a92523f1da361e12df6` |

- **K-02 (2. és 4. kép):** az „ML04 a jobb szélen” mondat helyett: „The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; at most a faint warm spill of its light reaches the right edge of the floor and the table.” + tiltósor.
- **K-03 (1. és 3. kép):** a W02 melletti növény/olajfa mondata törölve + tiltósor: „a plant, tree or any object standing in front of W02 or in the mouth of the bedroom corridor”.

## Közös csatolmányok (sorrendben)
| Szerep | Cam_12 v3 (1., 3.) | Cam_02 (2., 4.) |
|---|---|---|
| **1. kép – semleges Blender-alap** (geometria, keret) | `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png` (sha `66a9c6af…`) | `04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png` (sha `cb60ec8e…`) |
| **2. kép – valós padló** | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg` (sha `88f93864…`) | ua. |
| 2b – falak, profilok, ajtó | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg` (sha `06981c28…`; **az A902-es**, nem az A811-es ME-BAL-045) | ua. |
| 2c – **valós terasz és kilátás** | – (a nézetben nincs) | `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg` (sha `9d0457ee…`) + sötét tégla káva: `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-053_teraszajto_sotet_tegla_kava.jpg` (sha `e92696e9…`) |
| 3. – termékképek | a Macen: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/…` (a KEP004 v1 csomag szerint). **S01:** Lennon L jobbos tóp, Toni ovális világos tölgy (a fájl 200 × 90-es fotó: csak anyag és forma, a méretet a prompt adja), Eamy világosszürke, Nifelia 200 × 300, Somar Ø76. **S02:** JÄTTEBO U Samsala sötétkék (IKEA 49607648), Ciselia bézs-fekete, Marely fehér, Brisia 1 gömb Ø50 (L00152CR05), fekete Toni (**nincs igazolt kép**) | ua. |

## Render Reality Card – közös rész (mind a négy kép)
| Felület | Állapot | Forrás | Képen |
|---|---|---|---|
| Padló | MEGLÉVŐ / MEGTARTOTT | Egger laminált, terv: EL2184 Grey Treviso Oak, Aqua+ (IGAZOLT-D); fotó: ME-BAL-080 (vizuálisan megfelel); termékkód és deszkairány a helyszínen NEM IGAZOLT | szürkésbarna, göcsös tölgyhatású laminált + 6 cm-es azonos dekorú szegőléc, a fotó szerint; nem világosabb, nem hidegebb |
| Mennyezet | MEGLÉVŐ | fehér, HF03 hűtő-fűtő mező (nem fúrható) | fehér, rajta semmi; csak ML04/ML05 kiállás |
| Ajtók, profilok | MEGLÉVŐ | világosszürke ajtó, fekete kilincs; profil belül fehér, kívül antracit (IGAZOLT-F) | változatlan |
| Belmagasság | MEGLÉVŐ | 2,90–2,93 m (IGAZOLT-M) | – |
| Kanapé, asztal, székek | ÚJ / ÁRAZOTT – Opus 40-es lista (7d3c67f-ben ellenőrizendő) | lásd a stílusrészt | a Blender-tömbbel egyező hely és méret |
| Státusz | **KONCEPCIÓ – NEM VALIDÁLT** | RRG §D | a képen és a fájlnévben |

### 1. kép – S01 Cam_12 v3 (nappal)
- **Felületek:** W02 + W07 washi-hatású vinil tapéta (ÚJ, 11-es sor, becslés); grafit laminált tintavonal-sín z 2,10 (ÚJ, asztalos); W03 szemöldöksáv grafit laminált (ÚJ); W02 tusvonás-mű 120 × 200 (ÚJ, 12-es sor); konyha METOD + grafit laminált front, KARLBY tölgy, grafit hátfestett üveg (ÚJ, 02a).
- **Blender:** a kanapé a kép 16,5 %-a; a W02 takaratlan 83 % – a növény törlése (v1.1) után ~100 %; ML04 Somar és ML05 Misaki a képen; állóhely szabad.
- **Nem igazolt:** Misaki (termék), Somar függesztési magassága, tintavonal-sín ↔ mű 4 cm-es átfedés (a sín a mű fölött fusson).
- **Költségsáv:** a teljes S01 a 7d3c67f `50_KOLTSEG` szerint – most nem auditált.

### 2. kép – S01 Cam_02 (kék óra)
- **Felületek:** W01 KI-A washi-lámpásfal (6 panel ≤ 4 cm, torony 60 × 40 × 253, úszó pad 260 × 42), Hue Lightstrip Plus a fugákban (FELTÉTELES – táp: D18) és a pad alatt (D16/D17); 03a becslés 0,75–0,99 M + Hue 0,16–0,22 M (Opus, asztalos-ajánlat nélkül).
- **Blender:** a TV-fal 25 %, takaratlan 67 %; ML05 felül középen; **ML04 a képen kívül** (K-02); terasz és kilátás 26 %.
- **Nem igazolt:** teraszajtó-szárny (hat szék csak középső szárnnyal), dohányzóasztal-termék.

### 3. kép – S02 Cam_12 v3 (nappal)
- **Felületek:** navy laminált lábazat 1,8 cm z 1,10-ig a W02-n és a W07-ben (ÚJ, asztalos); ezüstszürke textilhatású vinil fölötte (ÚJ, 11-es sor); kék–szilva mű 140 × 180; konyha navy laminált front + sárgaréz fogantyúléc, EKBACKEN szürke-bézs kőhatású laminált (őszintén laminált), füstbronz tükör hátfal (K-13).
- **Blender:** a kanapé 23,3 %; a W02 takaratlan 72 % – a növény törlése után ~100 %; a hálók felé vezető út a lábazattal ≈ 0,907 m (határeset, megfelel).
- **Nem igazolt:** fekete Toni 160 × 90 (K-06), a sárgaréz-opál ML05 terméke.

### 4. kép – S02 Cam_02 (kék óra)
- **Felületek:** W01 BN-A éjkék kabinetfal (80 × 45 és 70 × 40 × 253, ezüst mező, 2 × 15 cm-es füstbronz tükörrés, úszó pad 220 × 40), Hue-ellenfény (FELTÉTELES, D18), padfény (D16/D17); 03a becslés 0,90–1,18 M + Hue 0,15–0,20 M.
- **Blender:** a TV-fal 25 %, takaratlan 61 %; ML04 a képen kívül (K-02); a U északi karja 0,225 m-re van az üvegtől (a függöny csak a kávában fut – a mélység hétfőn mérendő).
- **Nem igazolt:** fekete Toni, a U-n belüli dohányzóasztal (K-08), R50-es navy postforming (K-14).

## Kép utáni kötelező audit (RRG §C)
Képenként egy sor minden látható elemhez: `elem | forrás | tervezett felület | képen | eltérés | Ft-kockázat | bizonyíték | döntés`. Külön figyelendő: a padló tónusa a ME-BAL-080-hoz képest; nincs-e ML04-lámpa a Cam_02 jobb szélén; nincs-e növény a W02 előtt; a tükörrés reflexiója fizikailag helyes-e; a navy nem lakkfényes-e.

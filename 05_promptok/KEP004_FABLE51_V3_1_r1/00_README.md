A brief verziója r2, ez a kimenet r1.

# WSG DESIGN CHALLENGE 2026 · B versenyző – Claude Fable 5.1 · V3.1 r1

**PR-jelölő:** `WSG-COMPETITION-RESULT: FABLE51-V3_1`
**Versenyző:** B – Claude Fable 5.1 (High effort, önálló Claude-munkamenet, 2026-10-25)
**Bázis-commit (közös verseny-baseline v3):** `45632b5ad5586e1f3f884a8f723c1cc13cda6da3` (ág `competition/baseline-20261025-v3`)
**Kalibrációs forráscommit (csak olvasva, nem másolva):** `2452dfc54f26467791dccbd9ce620cd7af0435bb` (ág `competition/inditas-20261025`, `05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/20_PROMPTOK/`)
**Saját ág:** `competition/fable51-v3-1-20261025` → draft PR a `competition/baseline-20261025-v3` ágra
**Státusz:** a munka checkpointolva készül; az aktuális állapot a `00_CHECKPOINT_NAPLO.md`-ben és a `01_MANIFEST_66.csv`-ben.

## Mit tartalmaz ez a mappa
| Fájl | Tartalom |
|---|---|
| `00_README.md` | ez a fájl |
| `00_CHECKPOINT_NAPLO.md` | checkpointonként: sorszám, idő, tartalom, commit SHA, távoli visszaolvasás eredménye |
| `01_MANIFEST_66.csv` | 66 sor a közös regiszter `kep_id`-jával: 1–60 saját prompt (PENDING / DRAFT / COMPLETE), 61–66 KOZOS kalibráció |
| `02_KOZOS_REALITY_FIXED_elvek.md` | közös reality-elvek angolul (geometria, kamera, meglévő felületek, őszinte anyagnevek, közlekedési méretek; VB.3 fény) |
| `03_KAMERA_KOMPOZICIOK.md` | a hat kamera kompozíciós leírása (VB.3), a látható elemek hierarchiájaként |
| `10_STILUS_SPEC/S01…S10.md` | tíz egységes stílus-specifikáció (DNS, nappali–étkező–konyha, master, fürdő, elemlista, fény, költség) |
| `20_PROMPTOK/<kep_id>.prompt.md` | pontosan 60 saját angol kreatív prompt, BEGIN/END jelölővel |
| `30_TV_FAL_KONCEPCIOK_S01_S02.md` | 3 + 3 TV-fal-koncepció S01/S02-höz, javasolt főváltozattal |
| `40_ELEMLISTA_V3_1.csv` | méretezett, falazonosítós elemlista (r2 §11.7) |
| `50_KOLTSEG_ES_KOCKAZAT.md` | 8,40 M közös fix + 9,60 M stílusfüggő tételesen, fő/gazdaságos, kiváltott tételek, LED/Hue kockázati tábla |

Összefoglaló és integrációs átadás: `ai-coordination/results/WSG-20261025-FABLE51-CREATIVE-UPGRADE-V3_1_r1.md`.

## Források (a bázis-commitban, csak olvasva)
- `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md` – geometria, étkezőváltozatok, kamerák, fény
- `ai-coordination/inputs/A902_verseny/KOZOS_FIX_ALAP_v1.csv` / `.md` – közös költségalap (18,00 = 8,40 fix + 9,60 stílusfüggő)
- `ai-coordination/inputs/A902_verseny/HUE_ALAPCSOMAG_v1.md` – Hue-rendszerelv és fajlagos árak
- `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md` – végleges r2 brief (a VB blokk felülírásaival)
- `ai-coordination/requests/WSG-20261025-ASTRA-V3_1_INPUT_Cam12_falak_vilagitas.md` – falazonosítók, W02+W07, kiállás-mátrix (kamera- és fényadatait a VB.3 felülírja)
- `05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv` – a 66 soros képregiszter
- `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` §1 – reality-elvek alapja (a „painted white” és a „Series A overcast” mondat nem átvéve)
- `05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`, `05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md`, `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md`
- `01_alaprajzok/villamos_kiallasok/A902_villamos.csv` – kiállás-azonosítók (TERV SZERINT)
- `03_blender/validator_nyilvantartas_A902_kameracsomag_C.md` – külön hibanyilvántartás
- Astra V3 r1 (PR #16 ága, `be6b1f3`, csak olvasva) és Astra V2 r1 (`05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md`) – közös kreatív kiindulás, termékrekordok
- Péter feltöltött skilljei: westside-berendezes, wsg-ertekalapu-stiluslabor (`07_skill/`), interior-design-expert, interior-design, product-research, color-palette-generator, ffe-spec-book, product-cut-sheet (szöveges tervezésre; kép- és videóeszközök nem futottak)

## Elavult anyagok, amelyeket nem használtam (VB.1)
GEOMETRIA v1; a V3.1 brief r1; `KEP004_ChatGPT_Images_v1/` C1/C2 promptjai; a 2D kerek-asztal próba; P902_24A és a PR #18 A/B változatai; Cam_12 v2; a régi Cam_03 [4,70; 7,70]; a GOAL.md 7. pontjának 2026-10-25 04:40 előtti fény-, Cam_03-, elrendezés-, étkező- és kalibrációs szabályai; a `WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` korábbi szövege; a `competition/baseline-20261025` és `-v2` ág; a `45d1e4d` forráscommit. A main-t és a GOAL.md újabb változatát a verseny alatt nem olvastam.

## Ami ebben a munkamenetben NEM történt
Blender- és Blender-MCP-használat; írás a main-re, a GOAL.md-be vagy a közös fájlokba; más PR kezelése; más AI indítása; képgenerálás (ChatGPT Images, Gemini, MeltFlex); rendelés vagy ajánlatkérés. A másik két versenyző V3.1-ágát és PR-jét nem olvastam.

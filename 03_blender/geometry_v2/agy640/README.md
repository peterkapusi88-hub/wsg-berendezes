# agy640 – master 05.1 ágytengely y 6,00 → 6,40 (v2b-1-k11b, 2026-10-25)

Riport: `03_blender/validator_report_2026-10-25_v2b1k11b_agy640.md`. Futtatva háttér-Blender 5.2.3 LTS-sel a Macen (`~/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/`); a szkriptekben ezért Mac-útvonalak vannak.

## Szkriptek, futtatási sorrendben

| Fájl | Mit csinál |
|---|---|
| `01_agy640_athelyezes.py` | **r2** – a 33 bútor- és stílusréteg-objektum eltolása a mesh-adatban (location 0 marad), mentés új fájlba (`copy=True`). Ellenőrzi a forrás sha256-ját, a szülő/kényszer/animáció hiányát, a mesh egyetlen használóját és az eltolás pontosságát (< 1 mm). |
| `02_validator_agy640.py` | Validator v2 – `ures` / `referencia` / `master_butor` mód. |
| `02b_validator_stil_master.py` | Validator v2 – `zenit_master` / `lakeforest_master`: csak az adott stílusréteg master-elemei láthatók. |
| `03_render_ellenorzes_agy640.py` | Cam_04, Cam_11 és 05.1 felülnézet jelölőkkel (EEVEE, 64 minta), mérések → `render_log_agy640_v2.json`. Nem ment. |
| `04_vizsgal.py` | Transzformáció-kivonat 5 objektumra – ezzel derült ki az r1 hibája. |
| `05_diag_lathatosag.py` → `05_diag.json` | Láthatósági diagnózis. Megfigyelés: Blender 5.2-ben a `Collection.all_objects`-en át írt `hide_render` nem maradt meg, a `Collection.objects`-en át igen – ezért a 02b az `objects`-et használja. |
| `06_leltar_05_1.py` → `06_leltar_r2.json` | A 05.1 bútor- és stílusréteg-leltára a `matrix_basis`-ből (nem a futásidejű `matrix_world`-ből). |
| `futtat2.sh` | r2 mentése, kivonat, validátor (3 mód), ellenőrzőképek. |
| `futtat3.sh` | A stílusrétegek előtte/utána validálása (régi és új fájl). |
| `futtat4.sh` | **Végső validáció a PR-lockkal** (v2b-1-k11b), 5 mód → `03_blender/validator_v2b1k11b_agy640_*.json`; sha256 → `futtat4_sha.txt`. |

## Naplók

- `01_agy640_naplo_r2.json` – objektumonként: típus, location/rotation/scale, módszer, befoglaló előtte és utána; a forrás és a kimenet sha256-ja.
- `04_vizsgal_r2.json` – az r2 fájl transzformációi (minden location 0, matrix_world = egységmátrix, ez konzisztens).
- `elotte_v2b1k11/` – bizonyítékok az előtte-állapotról:
  - a régi (v2b-1-k11) fájl validálása master bútor, Zenit és Lake Forest módban;
  - a régi fájl leltára és transzformációi;
  - `04_vizsgal_r1_HIBAS.json`: az r1 kísérletben a location 0,4 lett, a betöltött `matrix_world` viszont egységmátrix maradt.

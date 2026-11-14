# Validator-riport: A-902 v2b-1-k13 KAMERACSOMAG C (2026-10-25)

**Feladat:** Péter 2026-10-25 04:08 – C elrendezés, K1 Cam_03, a Cam_12 kompozíciós felülvizsgálata.
- **Változás:** csak a `Cam_03_Etkezo_konyha` és a `Cam_12_Nappali_Hero` kamera.
- **Változatlan:** fal, nyílás, padló, terasz, bútor- és stílusréteg, többi kamera, render-beállítás.

## Eredmény
Validator v2, lock v2b-1-k13 (sha256 `2ca93735…3d1b`) + `A902_villamos.json` (terv szerinti kiállások).

| Mód | Eredmény | JSON |
|---|---|---|
| üres | **PASS 0/0 – 12 kamera teljes paraméterrel** | `validator_v2b1k13_ures.json` |
| referencia (beépített szaniterek) | FAIL 6/3 – a régi 6 szaniter-ütközés, változatlan, nem e csomag tárgya | `validator_v2b1k13_referencia.json` |
| master bútor | PASS 0/0 | `validator_v2b1k13_master_butor.json` |
| C S01 + TV40 / C S02 + TV40 | **PASS 0 hiba / 7 figyelmeztetés** | `validator_v2b1k13_C_S0{1,2}_TV40.json` |
| C S01 + TV60M / C S02 + TV60M | **PASS 0 hiba / 12 figyelmeztetés** | `validator_v2b1k13_C_S0{1,2}_TV60M.json` |

**Figyelmeztetések:**
- D16, D17, G01–G04 és G08 a TV-alsószekrény mögött van, a hozzáférés ellenőrizendő: kivehető vagy szellőző hátfal.
- TV60M-ben ezen felül:
  - a D18 a déli, 60 cm-es szekrény mögött van → szervizkivágás kell;
  - a 75"-os képernyő 5 cm-re átfed az északi próbaszekrénnyel (próbatömb, a középső mező szélessége / TV-méret kérdése).

## Mi változott (v2b-1-k12 v2 → v2b-1-k13)
- **`03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`:** sha256 `66172d43…c9d3` → `e01170d315193f8785bbeee5f7d319ce3c8adec886375962cee83e0a3f70ddbd`.
  - A mentést a `geometry_v2/cam12_C/03_rogzites_C.py` végezte, másolatként.
  - A szkript ellenőrizte, hogy csak a két kamera mozdult.
  - Aktív kamera: Cam_04_Master.
- **`03_blender/geometry_lock_A902_v2b.json`:** a két kamera új paraméterei, a `javitasok` v2b-1-k13 bejegyzése a régi paraméterekkel.
- **`03_blender/geometry_v2/kamera_parameterlap_v2b.md`:** a Cam_03 és a Cam_12 sora.

## Futtatás
- Szkriptek: `03_blender/geometry_v2/cam12_C/futtat3.sh` (03_rogzites_C.py, majd 04_ellenorzes_C.py).
- A Mac élő Blenderéből indított háttérfolyamat, Blender 5.2.3.
- Az élő, nem mentett projektfájlt nem érintette; a forrás sha256-ja a futás előtt és után azonos (`naplok/futtat*_sha*.txt`).

# Validator-riport: A-902 v2b-1-k12 JAVASLAT v2 – Cam_12_Nappali_Hero (2026-10-25 02:50)

**Feladat:**
- Péter 01:39: második, látványközpontú nappali kamera.
- 01:58: sarokból, átlósan.
- 02:06: az ÉNy-i sarok a fő jelölt, összevetés a DNy-ivel.
- Egyetlen változás: a Cam_12 kamera. Fal, nyílás, padló, terasz, bútor- és stílusréteg, többi kamera és render-beállítás változatlan.

## Eredmény
Validator v2, lock v2b-1-k12 v2 (sha256 `54796a6eb3f4234b19709934dbd2f1f8d7b9b5c2c1b313dbe2a1e3eaa8ed2f46`) + `A902_villamos.json` (130 terv szerinti kiállás).

| Mód | v2b-1-k11b (main) | v2b-1-k12 v2 | JSON |
|---|---|---|---|
| üres | PASS 0/0 (11 kamera) | **PASS 0/0 – 12 kamera teljes paraméterrel** | `validator_v2b1k12_cam12_ures.json` |
| referencia (beépített szaniterek) | FAIL 6/3 | FAIL 6/3 – ugyanaz a 6 régi szaniter-ütközés, nem e PR tárgya | `…_referencia.json` |
| master bútor | PASS 0/0 | PASS 0/0 | `…_master_butor.json` |
| **S01 V3 tömb** (KI3-L/V/P, TV, Lennon L, Toni + 6 Eamy, KI3-A) | – | **PASS 0 hiba / 8 figyelmeztetés** | `…_tomeg_S01.json` |
| **S02 V3 tömb** (BN3-L/V/P, TV, JÄTTEBO U, Anouk + 6 Ciselia, BN3-A) | – | **PASS 0 hiba / 8 figyelmeztetés** | `…_tomeg_S02.json` |

Mindkét fájlban: LOCK 61 fal / 54 nyílás / 17 padló, 0 eltérés; terasz 43 elem, 0 változás; ajtó: 11 nyílás negyedkörrel vizsgálva.

**A 8 figyelmeztetés** (S01 és S02, azonos), mind „dugalj/aljzat a bútor előtt, hozzáférés ellenőrizendő”:

| Kiállás | Mi áll előtte | Teendő |
|---|---|---|
| D16, D17, G08 | az alsó TV-szekrény | A V3 kivehető, szellőző hátfalat ír elő: rendben |
| G01, G02, G03, G04 | az alsó TV-szekrény | A rajzi doboz-helyzet bizonytalan (x 3,91–4,03); helyszíni mérés, hátfal-kivágás |
| D18 (y 4,749) | a KI3-V torony, ill. a BN3-V szekrény | **Szervizkivágás kell** – a V3 nem írja elő; V3.1-ben a LED-tápegység helye is lehet |

## Mi változott (v2b-1-k11b → v2b-1-k12 v2)
- **`03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`:** sha256 `9875cd57…ed28` → `66172d43cedfa3b7ccc78bb5dea894c02acef80933940f5a0ea98c1bef61c9d3`.
  - Egyetlen új objektum a Cam_04_Master gyűjteményében: `Cam_12_Nappali_Hero` (PERSP).
  - Paraméterek: 22 mm, 36 × 24 AUTO, shift_y −0,08, clip 0,1–200, hely [3,95; 7,90; 1,45], Euler XYZ [π/2; 0; −3π/4].
  - Aktív kamera: Cam_04_Master (változatlan).
  - A mentést a `03_cam12_rogzites_v2.py` végezte a main k11b fájljából, másolatként.
- **`03_blender/geometry_lock_A902_v2b.json`:** új `cameras.Cam_12_Nappali_Hero` és `javitasok` → `v2b-1-k12` bejegyzés. sha256 `7aa85d70…154b` → `54796a6e…2f46`.
- **`03_blender/geometry_v2/kamera_parameterlap_v2b.md`:** új Cam_12 sor.

## Futtatás
- `03_blender/geometry_v2/cam12/`:
  - `01_sarok_jeloltek.py`: K1/K2/K3 és lencsevariánsok, ray cast;
  - `02_finomitas.py`: R1–R3;
  - `03_cam12_rogzites_v2.py` és `04_ellenorzes_v2.py`.
- A Mac élő Blenderéből indított háttérfolyamatok, Blender 5.2.3; az élő, nem mentett projektfájlt nem érintették.
- A 01:39-es tengelyes jelölt (H1) szkriptjei és naplói: `cam12/v1_H1_tengelyes_elvetve/`.

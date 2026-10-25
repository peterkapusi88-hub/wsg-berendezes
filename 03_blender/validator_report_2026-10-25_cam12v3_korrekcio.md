# Validator-riport: A-902 Cam_12 v3 KORREKCIÓ (2026-10-25)

**Feladat:** Péter – a ChatGPT Images Cam_12 próbák (S01, S02) GEOMETRIA FAIL-je után új, olvashatóbb semleges alapkép + S01/S02 tömbrender ugyanabból a kamerából. Nincs AI-képgenerálás.

**Forrás (nem módosult):**
- Blend: a v2b-1-k13 KAMERACSOMAG C blend MÁSOLATA, sha256 `e01170d315193f8785bbeee5f7d319ce3c8adec886375962cee83e0a3f70ddbd`. A repóban ez `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` a `kep004/kameracsomag-C-K1` (f190e5f), `competition/baseline-20261025-v3` (45632b5) és `competition/fable51-v3-1-20261025` (b445412) ágon. A Macen: `~/Downloads/WSG/KEP-004/_munka/blender_cam12C_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k13_KAMERACSOMAG_C.blend` (azonos sha).
- Másolat a futáshoz: `~/Downloads/WSG_CAM12_V3_KORREKCIO/forras/WSG_A902_v2b1k13_MASOLAT_cam12v3_korrekcio.blend`. Sha a futás előtt és után azonos, a szkript nem ment (`naplok/cam12v3_korr_log.json`: `mentve: false`).
- Lock: `geometry_lock_A902_v2b.json` v2b-1-k13, sha256 `2ca9373596b3445d984ad1fdbaaa9d12848c21b25908f6dc8d7fdfc3f9eb3d1b`. Nem írtam.
- Validátor: `03_blender/geometry_validator_v2.py`, sha256 `b7d7f6a678f3ccc6bf0dd06023073f879d85a1aab916c101ad097f08129e8d77`. Villamos: `A902_villamos.json` `f881dcceb5f8c99df098f11e5ac7e9fd06eee0f1f226e34cc94647445bb04c4c`.
- Futtatás: Blender 5.2.3 LTS, háttérfolyamat a Mac élő Blenderéből indítva. Az élő fájl (`~/Downloads/WSG/Blender_aktualis_2026-10-24/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend`) a futások előtt és után mentett állapotú volt (`is_dirty: false`), nem nyúltam hozzá.
- Szkriptek: `03_blender/geometry_v2/cam12_v3_korrekcio/` (`01_render_cam12v3.py`, `blokk_spec.py`).

## Eredmény
| Mód | Eredmény | JSON |
|---|---|---|
| üres (minden bútor rejtve) | **PASS – 0 hiba, 0 figyelmeztetés**: 61 fal, 54 nyílászáró, 17 padló, 43 teraszelem 0 eltérés, 12 kamera teljes paraméterrel | `naplok/validator_cam12v3korr_ures.json` |
| referencia (beépített szaniterek) | FAIL 6/3 – a régi, ismert 06.1/06.2 szaniterhibák, változatlanok (lásd `validator_nyilvantartas_A902_kameracsomag_C.md`) | `…_referencia.json` |
| S01 tömb | **FAIL – 5 hiba, 15 figyelmeztetés** | `…_S01.json` |
| S02 tömb | **FAIL – 10 hiba, 17 figyelmeztetés** | `…_S02.json` |

### Hibák értékelése
| Hiba | S01 | S02 | Valós? | Teendő |
|---|---|---|---|---|
| A hűtőoszlop (ET-01, y 5,05–5,65) takarja a K07–K09 kapcsolócsoportot (doboz y 5,65) | 3 | 3 | **VALÓS** – a kapcsolódoboz pont az oszlop északi élén van, a 0,40 m-es sáv nem elég | döntés kell (lásd a README 4. pontját) |
| S02 tükörsáv (ET-02, y 5,65–6,05) takarja a K07–K09-et | – | 3 | **VALÓS** | kivágás vagy keskenyebb/áthelyezett tükör |
| S08 érzékelő (x 3,569) a TV-fal elemei mögött | 1 | 1 | **téves riasztás** – a 05.1 háló oldalán van | – |
| S02 érzékelő, T04 termosztát, K20 kapcsoló (x 10,849) | 1 (ET-03) | 3 (ET-02) | **téves riasztás** – a 05.3 szoba oldalán vannak | – |

A validátor a falvastagságot nem nézi, csak ±12 cm-es körzetet. Ezért jelez a fal túloldali kiállásaira.

### Figyelmeztetések (lényeg)
- **TV ↔ konzol ütközés (S01, S02):** a 65"-os TV középmagassága 1,20 m, így az alsó éle 0,78 m-en van. A konzol teteje 0,95 m. A TV alsó 17 cm-e a konzol testébe érne. A TV középmagassága legalább 1,37 m kell legyen, vagy a konzolt kell lejjebb tenni. A Cam_12-ben ez nem látszik.
- Konyhai dugaljak (D02–D07, D10, D14) a szekrények mögött: szokásos, kivágás kell.
- D12, D13 a hűtőoszlop mögött; D16–D18 és G08 a TV-fal paneljei mögött: szervizkivágás kell.

### Ami a validátoron kívül esik (2D mérés: `02_utak_blokk.py` → `utak_blokk_S01_S02.json`)
| Mérés (cél) | S01 | S02 |
|---|---|---|
| fő utak betolt székkel (≥ 0,90): terasz / konyha / folyosó / **05.3 ajtó** | 0,90 / 1,00 / 1,00 / **0,85** | 0,90 / 0,95 / 0,90 / **0,85** |
| hűtőoszlop – étkező (szék) | 0,897 | 0,88 |
| székkihúzás függönnyel (≥ 0,90) | min. 0,93 | min. 0,93 |
| kanapé – TV-bútor (≥ 0,60) | 0,75 | 0,88 |
| dohányzóasztal – kanapé (0,45–0,50) | 0,45 az ülés elejéig; **0,115 a chaise oldaláig** (hely FELTEVÉS) | **0,075–0,10 – FAIL** |
| dohányzóasztal – TV-bútor (≥ 0,60) | 0,60 | 0,68 |
| konyhai pultköz | 0,86 (FELTÉTELES, ismert) | 0,86 |
| Cam_12 állóhely (x 4,30–4,50; y 7,75–8,05) szabad | igen | igen |

**Következtetés:** a semleges alap geometriailag PASS. A két Fable-terv tömbje a megadott méretekkel **nem PASS**: kapcsolótakarás, 0,85 m-es út a 05.3 ajtóhoz (a W03-a elé tett hűtőoszlop miatt), S02-ben a dohányzóasztal helye, mindkettőben a TV–konzol magasság. A Cam_12 képi összevetéshez a tömbök használhatók, de ezek nem kivitelezhető elrendezések.

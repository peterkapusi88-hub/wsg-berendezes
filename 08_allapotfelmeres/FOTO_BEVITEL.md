# Fotó- és dokumentumbevitel: helyiségenként visszakereshetően, Blender-kamerához kötve

## 1. Hol vannak a fájlok
| Mi | Hol | Miért |
|---|---|---|
| **Eredeti** fotók és videók (változatlanul) | Mac: `~/Downloads/WSG_helyszin/2026-10-27/<lakás>/<helyiség>/` | egy nap anyaga több GB is lehet; az eredetit soha nem írjuk felül |
| Kicsinyített munkapéldány (1600 px, JPG, kb. 300 KB) | repó: `08_allapotfelmeres/fotok/<lakás>/<helyiség>/` | Astra, Codex és Claude ezt látja, verziózva |
| Leltár | repó: `08_allapotfelmeres/fotok/LELTAR_2026-10-27.csv` | Claude készíti a II. szakasz 1. lépésében: fájlnév, eredeti név, idő, irány (EXIF), lakás, helyiség, kamera, státusz |

Ha Péter egyszerűen egy mappába dobja a képeket (pl. `~/Downloads/WSG_helyszin/2026-10-27/` ömlesztve), az is jó. A szétválogatást és az átnevezést Claude végzi, az eredeti nevet a leltárban megtartja.

## 2. Fájlnév
`<lakás>_<helyiségkód>_<ééééhhnn>_<sorszám>_<irány>.jpg`
Például: `A902_04_20261027_03_szemkozti-sarok.jpg`, `A902_12_20261027_01_domb-agyas.jpg`, `A811_05-23_20261027_02_gardrob.jpg`.

**Helyiségkódok** (a terv számozása szerint, a mappanevekkel azonosak):
- **A902:** 01 előtér · 02 konyha · 03 étkező · 04 nappali · 05-1 master · 05-2 · 05-3 · 06-1 · 06-2 · 07 közlekedő · 08 WC · 09 terasz greslap Ny · 10 terasz greslap K · 11 terasz WPC · 12 zöldtető · 13 erkély · 90 kilátás · 99 dokumentum
- **A811:** 01 · 02 · 03 · 04 · 05-1 · 05-23 (összevont) · 06-1 · 06-2 · 07 · 08 · 09 HTH · 10 erkély · 90 · 99
- **A812:** 01 · 02 · 03 · 04 · 05-1 · 05-2 · 05-3 · 06-1 HTH · 06-2 · 08-09 fürdő sarokkáddal · 07 · 10-2 és 10-3 gardrób · 11 erkély · 90 · 99

## 3. Kapcsolat a Blender-nézetekkel
- `FOTO_KAMERA_KAPCSOLAT.csv`: **255 tervezett felvétel** (`foto_id`). Minden felvételhez tartozik helyiség, irány, tartalom, Blender-kamera és prioritás. Hétfőn a `tenyleges_fajl` oszlopba kerül a valódi fájlnév.
- A-902 meglévő kamerái:
  - Cam_02: nappali → terasz;
  - Cam_03: étkező–konyha;
  - Cam_04: master;
  - Cam_07: greslap → nyugat;
  - Cam_08: madártávlat;
  - Cam_09: felülnézet.
  A Cam_05 (régi terasz) elavult.
  Az „ajtóból” felvétel ugyanabból a pontból és magasságból (1,5 m) készüljön, mint a kamera. Így közvetlen fotó–Blender összevetés lehetséges, és a Reality Card erre épül.
- A-811 és A-812: a kamerák `Cam_A811_<kód>` névvel **jönnek létre**, amikor elkészül a modell. Az „ajtóból” fotó határozza meg a kamera helyét.
- Videó: `<lakás>_<kód>_<dátum>_V<sorszám>.mov`. A kulcskockákat Claude vonja ki (2 s-onként) a repóba, a `02_referenciak/<lakás>_helyszin/` alá.

## 4. Dokumentumok
- **Műszaki** dokumentum (terv, statika, zöldtető-rendszer, villamos terv) → `fotok/<lakás>/99_dokumentum/`. Előtte a nevek és aláírások kitakarása kötelező (lásd `01_alaprajzok/terv_kivonat_2026-10-24/`).
- **Szerződés, személyes adat, garanciális levelezés: soha nem a repóba**, hanem a „Lakásátvétel és garanciák” projektbe.

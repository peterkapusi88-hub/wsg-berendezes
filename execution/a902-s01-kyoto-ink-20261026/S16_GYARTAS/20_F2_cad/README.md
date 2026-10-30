# S16 R15 médiafal – 2. fázis (a): 3D szerkezeti CAD-modell

Készült: 2026-10-30, Claude (Opus 5.5). Státusz: **TERVI MODELL – nem gyártási kiadás.** **Az AutoCAD-ben felépítve és visszaolvasva: 129/129 test egyezik** (2026-10-30 14:22, Péter Macje).

## Mi ez?

A `../10_F1_adatmodell/parts_v1.json` (R15, QA: 0 blokkoló / 0 hiba) 129 alkatrészéből **egy építési tervből** (`cad_terv.json`) három kimenet:

| Fájl | Mi | Státusz |
|---|---|---|
| `S16_R15_szerkezet.dwg` | **natív AutoCAD-modell** (AutoCAD 2018 formátum): 129 tömör test, mindegyik saját `$PART_` rétegen + `TECH_*` megmunkálás-testek | AutoCAD 2027-ben felépítve, **129/129 visszaolvasva** (`mac_futtatas/README_readback.md`) |
| `S16_R15_szerkezet_v2.dwg` | ugyanaz, **délnyugati axonometria + realisztikus nézet** és `S16_ATTEKINTES` rajzlap 4 nézettel (elöl/bal/felül/axo) – így nyílik meg | 2026-10-30 15:04, AcCoreConsole, 129 test |
| **`S16_R15_szerkezet_v3.dwg`** | **etalon-szintű változat:** rétegnév `$PART_<ID>˙0˙0¨<élkód>˙0¨#0¨<szám>` (mint a km.dwg), 299 `TECH_*` furattest, 205 `$ITEM_REF_*` vasalat (75 tipli, 120 polctartó, 5 pánt + talp), 4 pecsétes A4 rajzlap (áttekintés, torony, alsó sor, háttér/TV), 3 nézet laponként | AcCoreConsole 2026-10-30 15:33, **129/129 visszaolvasva** |
| `S16_R15_szerkezet.lsp` | AutoLISP (ActiveX nélkül) – interaktív AutoCAD-hez | generálva |
| `S16_R15_build.scr`, `S16_R15_smoke.scr` | ugyanaz AcCoreConsole-szkriptként (háttérben, képernyő nélkül fut) | ez futott |
| `S16_R15_elonezet.dxf` | ugyanaz MESH-ként, bárhol megnyitható előnézet | kész – nem gyártási modell (háló, nem tömör test) |
| `cad_ellenorzes.md` | a tervből újraépített testek ↔ QA-ellenőrzött geometria | **129/129 egyezik**, max. térfogat-eltérés 0,04 % |

Futtatás: `python3 f2_cad_export.py` (a F1 függőségei + `ezdxf`).

## Réteg- és testkonvenció

- Alkatrész-réteg: `$PART_<címke-ID>#<él-kód>`, pl. `$PART_S16_D2-L#VVV0` – az asztalos etalonjának szerkezetét követi (név + él-kód + azonosító), ASCII-ben. Az etalon pontos jelölése (`¨`, `˙0`, `#0`) az asztalos válasza után állítható át a `gyartasi_szabalyok_v1.json`-ban.
- Megmunkálás: kivonva az alkatrészből **és** külön testként `TECH_<művelet>_<címke-ID>` rétegen (mint az etalon `TECH_*` testei): átmenő kivágás, hátsó fényfalc (T-DOOR-L), fénycsatorna (TV-FIELD), kimetszés (T-B).
- Ívek: 16 kontúros alkatrész valódi ívvel (LWPOLYLINE bulge az R14 `curve_vertices`-ből; a kontúrtól ≤ 0,3 mm). Két kivétel sokszöggel, mert az R14 ív-adata hibás: T-DOOR-L-BACK (a textilbetét íve, 12 mm-rel eltér), TV-FIELD (csak részlet).

## FONTOS: koordináta-tükrözés

Az R14 helyi rendszere (X jobbra a szobából, Y a faltól a szoba felé, Z fel) **balkezes** – ezért kellett a Blenderben az X-tükröző szülő. Jobbkezes AutoCAD-ben ez a bútor tükörképét adná (torony jobb oldalt). A CAD-exportban ezért **egyetlen tükrözés: Y_CAD = −Y_helyi**. Eredmény: fal síkja Y=0, a front −Y felé néz, az **AutoCAD FRONT nézet = szobából nézett homlokzat, torony bal oldalt** (előnézettel ellenőrizve). Az adatmodell helyi koordinátái (A/B oldal, E1–E4) ettől nem változnak.

## Lefuttatás a Macen (megtörtént, megismételhető)

Az AutoCAD for Mac csomagban lévő **AcCoreConsole** (grafikus felület nélküli parancssori motor) futtatja a `.scr`-t háttérben – ugyanezt használta a ChatGPT is az R05-höz. Lépések (`mac_futtatas/`):

1. `S16_R15_*.scr` + `mac_futtatas/S16_*.command` → `~/CAD/S16_R15/`.
2. Finderben megnyitni: `S16_smoke.command` (3 test), majd `S16_build.command` (129 test, DWG-mentés). Billentyűzet-bemenet nélkül, időkorláttal futnak.
3. `python3 f2_readback.py <readback-mappa> [--smoke]` – minden test térfogata és befoglalója a tervhez.

Tanulságok (2026-10-30): (a) a `-help` kapcsoló interaktív parancssort nyit és beragad – nem használjuk; (b) az AcCoreConsole kb. 4 KB-nál levágja a szkriptsort → a pontlisták 40 pontos részletekben épülnek; (c) külső `.lsp` betöltését a motor biztonsági okból megtagadja, ezért minden a `.scr`-ben van; (d) a kényszerített leállítás Autodesk-hibaablakot nyit – ártalmatlan, bezárható.

## Ami még nincs benne (2. fázis b)

Gyári vasalat-geometria (Blum CLIP top pánt + talp, MOVENTO sín, TIP-ON, kötőelemek) és furatképek; fényprofilok. Ezek a Blum/Häfele gyári CAD-adatából jönnek, nem kitalálva.

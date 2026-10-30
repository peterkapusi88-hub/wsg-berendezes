# S16 R15 médiafal – 2. fázis (a): 3D szerkezeti CAD-modell

Készült: 2026-10-30, Claude (Opus 5.5). Státusz: **TERVI MODELL – nem gyártási kiadás.** Az AutoCAD-beli lefuttatás és visszaolvasás még hátravan.

## Mi ez?

A `../10_F1_adatmodell/parts_v1.json` (R15, QA: 0 blokkoló / 0 hiba) 129 alkatrészéből **egy építési tervből** (`cad_terv.json`) három kimenet:

| Fájl | Mi | Státusz |
|---|---|---|
| `S16_R15_szerkezet.lsp` | AutoLISP, ActiveX nélkül (Mac-en is fut): alkatrészenként 1 tömör test saját rétegen, valódi ívekkel, kivont megmunkálásokkal | generálva, **AutoCAD-ben még nem futott** |
| `S16_R15_elonezet.dxf` | ugyanaz MESH-ként, bárhol megnyitható előnézet | kész – nem gyártási modell (háló, nem tömör test) |
| `cad_ellenorzes.md` | a tervből újraépített testek ↔ QA-ellenőrzött geometria | **129/129 egyezik**, max. térfogat-eltérés 0,04 % |

Futtatás: `python3 f2_cad_export.py` (a F1 függőségei + `ezdxf`).

## Réteg- és testkonvenció

- Alkatrész-réteg: `$PART_<címke-ID>#<él-kód>`, pl. `$PART_S16_D2-L#VVV0` – az asztalos etalonjának szerkezetét követi (név + él-kód + azonosító), ASCII-ben. Az etalon pontos jelölése (`¨`, `˙0`, `#0`) az asztalos válasza után állítható át a `gyartasi_szabalyok_v1.json`-ban.
- Megmunkálás: kivonva az alkatrészből **és** külön testként `TECH_<művelet>_<címke-ID>` rétegen (mint az etalon `TECH_*` testei): átmenő kivágás, hátsó fényfalc (T-DOOR-L), fénycsatorna (TV-FIELD), kimetszés (T-B).
- Ívek: 16 kontúros alkatrész valódi ívvel (LWPOLYLINE bulge az R14 `curve_vertices`-ből; a kontúrtól ≤ 0,3 mm). Két kivétel sokszöggel, mert az R14 ív-adata hibás: T-DOOR-L-BACK (a textilbetét íve, 12 mm-rel eltér), TV-FIELD (csak részlet).

## FONTOS: koordináta-tükrözés

Az R14 helyi rendszere (X jobbra a szobából, Y a faltól a szoba felé, Z fel) **balkezes** – ezért kellett a Blenderben az X-tükröző szülő. Jobbkezes AutoCAD-ben ez a bútor tükörképét adná (torony jobb oldalt). A CAD-exportban ezért **egyetlen tükrözés: Y_CAD = −Y_helyi**. Eredmény: fal síkja Y=0, a front −Y felé néz, az **AutoCAD FRONT nézet = szobából nézett homlokzat, torony bal oldalt** (előnézettel ellenőrizve). Az adatmodell helyi koordinátái (A/B oldal, E1–E4) ettől nem változnak.

## Lefuttatás a Macen (még hátravan)

1. AutoCAD 2027 for Mac, új üres rajz (mm), `APPLOAD` → `S16_R15_szerkezet.lsp`.
2. Próba: `(s16-smoketest)` → `(s16-readback "/Users/<név>/CAD/s16_smoke")` → `python3 f2_readback.py <mappa> --smoke` (3 test: hasáb, íves kihúzás, kivonás).
3. Ha a próba OK: új rajz, `(s16-build)` → `(s16-readback "/Users/<név>/CAD/s16_readback")` → `python3 f2_readback.py <mappa>` – mind a 129 test térfogata (≤ 0,5 %) és befoglalója (≤ 0,05 mm) a tervhez.
4. Mentés: `S16_R15_szerkezet.dwg`.

A `ROTATE3D`, `EXTRUDE` és `MASSPROP` parancssori viselkedése a Mac-verzión élő próbán ellenőrizendő – ezért van előbb a smoketest.

## Ami még nincs benne (2. fázis b)

Gyári vasalat-geometria (Blum CLIP top pánt + talp, MOVENTO sín, TIP-ON, kötőelemek) és furatképek; fényprofilok. Ezek a Blum/Häfele gyári CAD-adatából jönnek, nem kitalálva.

# S16 F2b – vasalat- és furatterv (S16-R15C-GY-v1)

Generálva: 2026-10-30 · `f2b_vasalat.py` · státusz: TERVI

| Furat-funkció | db |
|---|---|
| FIOK_DOBOZ_CSAVAR_ATMENO | 84 |
| FIOK_DOBOZ_CSAVAR_ELOFURAS | 84 |
| MINIFIX_CSAP | 22 |
| MINIFIX_CSATORNA | 22 |
| MINIFIX_HAZ | 22 |
| MOVENTO_HOROG | 12 |
| MOVENTO_SIN_JELOLO | 36 |
| PANTKEHELY | 11 |
| PANTTALP | 22 |
| PANT_DUBEL | 22 |
| POLCTARTO | 120 |
| TIPLI_EL | 142 |
| TIPLI_LAP | 108 |

| Kötés | db |
|---|---|
| FIOKDOBOZ_CSAVAR | 36 |
| TIPLI | 25 |
| TIPLI+MINIFIX | 11 |
| TIPLI_EL_EL | 1 |
| TIPLI_EL_EL_KERETLEC | 14 |

**Problémák:** {}

| Súlyosság | Alkatrész | Megállapítás |
|---|---|---|

## Nem tiplis kapcsolatok (külön kötés kell)

| A | él | B | típus | ok |
|---|---|---|---|---|
| D1-L | E1 | CURVE-T-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D1-R | E1 | CURVE-T-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D1-R | E3 | T-R | TIPLI_EL_EL | él-él illesztés (egymásra ülő oldallapok): Ø8×35, 17,5/17,5 – Claude döntés |
| D6-R | E1 | CURVE-B-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D6-R | E3 | CURVE-B-TOP | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D6-B | E2 | CURVE-B-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D6-T | E2 | CURVE-B-TOP | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| T-L | E1 | CURVE-T-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| T-L | E3 | CURVE-T-TOP | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| T-R | E3 | CURVE-T-TOP | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| T-C | E3 | CURVE-T-TOP | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| FRAME-T-L | E1 | FRAME-T-BOT | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-T-L | E3 | FRAME-T-TOP | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-T-R | E1 | FRAME-T-MID | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-T-R | E3 | FRAME-T-TOP | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-T-MID | E2 | FRAME-B-HIGH-1 | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-LOW-1 | E2 | FRAME-B-LOW-2 | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-LOW-1 | E4 | FRAME-T-BOT | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-LOW-2 | E2 | FRAME-B-LOW-3 | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-LOW-3 | E2 | FRAME-B-BOT | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-HIGH-1 | E2 | FRAME-B-HIGH-2 | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-HIGH-2 | E2 | FRAME-B-HIGH-3 | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-HIGH-3 | E2 | FRAME-B-TOP | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-R | E1 | FRAME-B-BOT | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| FRAME-B-R | E3 | FRAME-B-TOP | TIPLI_EL_EL_KERETLEC | 18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés |
| T-LOW-DIV | E1 | CURVE-T-BOT | TIPLI+MINIFIX | íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés |
| D1-BOX-L |  | D1-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D1-BOX-R |  | D1-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D1-BOX-L |  | D1-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D1-BOX-R |  | D1-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D1-BOX-L |  | D1-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D1-BOX-R |  | D1-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-L |  | D2-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-R |  | D2-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-L |  | D2-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-R |  | D2-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-L |  | D2-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D2-BOX-R |  | D2-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-L |  | D3-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-R |  | D3-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-L |  | D3-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-R |  | D3-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-L |  | D3-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D3-BOX-R |  | D3-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-L |  | D4-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-R |  | D4-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-L |  | D4-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-R |  | D4-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-L |  | D4-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D4-BOX-R |  | D4-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-L |  | D5-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-R |  | D5-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-L |  | D5-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-R |  | D5-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-L |  | D5-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D5-BOX-R |  | D5-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-L |  | D6-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-R |  | D6-BOX-F | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-L |  | D6-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-R |  | D6-BOX-H | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-L |  | D6-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |
| D6-BOX-R |  | D6-BOX-B | FIOKDOBOZ_CSAVAR | oldalon át 4×35 csavar + ragasztás |

## Paraméterek és források

```json
{
 "tipli": {
  "d": 8.0,
  "el_melyseg": 25.0,
  "lap_melyseg": 13.0,
  "hossz": 35,
  "veg_tav": 32.0,
  "max_koz": 192.0,
  "min_el": 60.0,
  "forras": "etalon km.dwg CONNOBJ_DOWEL_D8_L35_13-24: Ø8, lapba 13, élbe 25 mm; 32-es rendszer"
 },
 "tipli_el_el": {
  "d": 8.0,
  "melyseg": 17.5,
  "hossz": 35,
  "forras": "él-él illesztés (egymásra ülő oldallapok): Ø8×35, 17,5/17,5 – Claude döntés"
 },
 "tipli_keret": {
  "d": 6.0,
  "melyseg": 15.0,
  "hossz": 30,
  "forras": "18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés"
 },
 "minifix": {
  "haz_d": 15.0,
  "haz_melyseg": 12.5,
  "B": 24.0,
  "csatorna_d": 8.0,
  "csap_d": 5.0,
  "csap_melyseg": 11.0,
  "forras": "Häfele Minifix 15 (262.26.174, az asztalos km.dwg/coo1.dwg CONNOBJ_MINIFIX_D15_AV18_L24 blokkja); B = 24 mm; furatmélységek Häfele adatlap szerint ellenőrizendők"
 },
 "movento": {
  "sin_jelolo_d": 2.5,
  "sin_jelolo_m": 3.0,
  "sin_furatok_eloltol": [
   37.0,
   165.0,
   261.0
  ],
  "sin_magassag_fiokoldal_alatt": 6.5,
  "horog_d": 6.0,
  "horog_m": 10.0,
  "horog_alulrol": 7.0,
  "horog_kulso_oldaltol": 11.0,
  "forras": "Blum MOVENTO szerelési útmutató (wwhardware.com movento-2016.pdf): hátsó horog Ø6×10, 7/11 mm; elülső hézag 3 mm; csavarpozíciók A/B NL300-hoz (763.3050M: 165/261) + 37 mm elülső rendszerfurat; zár (T51.7601) és TIP-ON sablonnal (T65.1000.02 / T65.1600.01)"
 },
 "polc": {
  "d": 5.0,
  "melyseg": 10.0,
  "elol": 37.0,
  "hatul": 37.0,
  "z_eltolas": -6.0,
  "lepes": [
   -32,
   0,
   32
  ],
  "forras": "becslés – a polctartó (etalon: de_11090) típusától függ"
 },
 "pant": {
  "kehely_d": 35.0,
  "kehely_melyseg": 13.0,
  "B": 3.0,
  "csavar_d": 8.0,
  "csavar_melyseg": 11.5,
  "csavar_koz": 45.0,
  "csavar_eltolas": 9.5,
  "talp_elol": 37.0,
  "talp_koz": 32.0,
  "talp_d": 5.0,
  "talp_melyseg": 12.0,
  "veg_tav": 100.0,
  "talp_magassag": 50.0,
  "talp_kiallas": 12.0,
  "cikkszam": "Blum CLIP top 110° rugó nélküli, inset, csavaros 70T3750",
  "talp_cikkszam": "Blum CLIP talplemez 0 mm 177H3100E",
  "forras": "Blum CLIP top: Ø35, B 3–6 mm, Ø8 45/9,5 (richelieu.com Blum adatlap); 13 mm mélység, 37/32 rendszer; 71T3750 = inset 110° csavaros (sfs.ch), 70T3750 = rugó nélküli (TIP-ON) változat; etalon km.dwg: 71T3750 + 177H3100E"
 },
 "min_maradek": 5.0
}
```

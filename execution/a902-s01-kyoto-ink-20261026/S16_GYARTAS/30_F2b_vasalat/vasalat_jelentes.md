# S16 F2b – vasalat- és furatterv (S16-R15B-GY-v1)

Generálva: 2026-10-30 · `f2b_vasalat.py` · státusz: TERVI

| Furat-funkció | db |
|---|---|
| PANTKEHELY | 11 |
| PANTTALP | 22 |
| PANT_DUBEL | 22 |
| POLCTARTO | 120 |
| TIPLI_EL | 75 |
| TIPLI_LAP | 75 |

| Kötés | db |
|---|---|
| EL_EL_ILLESZTES | 21 |
| NEM_TIPLIS | 11 |
| TIPLI | 25 |

**Problémák:** {}

| Súlyosság | Alkatrész | Megállapítás |
|---|---|---|

## Nem tiplis kapcsolatok (külön kötés kell)

| A | él | B | típus | ok |
|---|---|---|---|---|
| D1-L | E1 | CURVE-T-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| D1-R | E1 | CURVE-T-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| D1-R | E3 | T-R | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| D6-R | E1 | CURVE-B-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| D6-R | E3 | CURVE-B-TOP | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| D6-B | E2 | CURVE-B-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| D6-T | E2 | CURVE-B-TOP | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| T-L | E1 | CURVE-T-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| T-L | E3 | CURVE-T-TOP | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| T-R | E1 | D1-R | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| T-R | E3 | CURVE-T-TOP | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| T-C | E3 | CURVE-T-TOP | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |
| FRAME-T-L | E1 | FRAME-T-BOT | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-T-L | E3 | FRAME-T-TOP | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-T-R | E1 | FRAME-T-MID | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-T-R | E3 | FRAME-T-TOP | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-T-MID | E2 | FRAME-B-HIGH-1 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-1 | E2 | FRAME-B-LOW-2 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-1 | E4 | FRAME-T-BOT | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-2 | E2 | FRAME-B-LOW-3 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-2 | E4 | FRAME-B-LOW-1 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-3 | E2 | FRAME-B-BOT | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-LOW-3 | E4 | FRAME-B-LOW-2 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-1 | E2 | FRAME-B-HIGH-2 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-1 | E4 | FRAME-T-MID | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-2 | E2 | FRAME-B-HIGH-3 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-2 | E4 | FRAME-B-HIGH-1 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-3 | E2 | FRAME-B-TOP | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-HIGH-3 | E4 | FRAME-B-HIGH-2 | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-R | E1 | FRAME-B-BOT | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| FRAME-B-R | E3 | FRAME-B-TOP | EL_EL_ILLESZTES | két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem |
| T-LOW-DIV | E1 | CURVE-T-BOT | NEM_TIPLIS | B (IVES_SZERELVENY, M02) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés |

## Paraméterek és források

```json
{
 "tipli": {
  "d": 8.0,
  "el_melyseg": 25.0,
  "lap_melyseg": 12.0,
  "hossz": 35,
  "veg_tav": 32.0,
  "max_koz": 192.0,
  "min_el": 60.0,
  "forras": "etalon (km/coo1): Ø8×25/35 bordás tipli; 32-es rendszer"
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

# R16J F1 – QA-jelentés (R16-J-GY-v1)

Generálva: 2026-10-30 · `r16_qa.py` (a S16 qa_parts_v1.py ellenőrzéseivel) · forrás: `parts_v1.json` (106 alkatrész)

**Ítélet: NEM KIADHATÓ – HIBA javítandó**

| Súlyosság | db |
|---|---|
| BLOKKOLO | 0 |
| HIBA | 1 |
| FIGYELMEZTETES | 12 |
| INFO | 13 |

Geometria-forrás: {'R16_doboz': 99, 'R14_kontur_extrudalas': 7} · vizsgált ütköző pár (befoglaló-átfedéssel): 0

## HIBA (1)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q18_MENNYEZETI_RES | bútortest | legmagasabb pont Z=2880, rés a névleges 2900 mm-es mennyezetig 20 mm (helyszíni felmérés még nincs) |

## FIGYELMEZTETES (12)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-03 | R16 listázott [212, 48, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-04 | R16 listázott [212, 48, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-05 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-06 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-07 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-08 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-09 | R16 listázott [212, 408, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-10 | R16 listázott [212, 408, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-11 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI14-BAT-12 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI16-M6-BAT-06 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |
| Q05R_R16_LISTA_JAVITVA | KI16-M6-BAT-07 | R16 listázott [212, -222, 18] hibás → kész 18×212×18 a befoglalóból (javitasi_naplo.json) |

## INFO (13)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q13_FIOK_OK | D1 | LW 684, SKW 642, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q13_FIOK_OK | D2 | LW 414, SKW 372, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q13_FIOK_OK | D3 | LW 414, SKW 372, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q13_FIOK_OK | D4 | LW 1044, SKW 1002, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q13_FIOK_OK | D5 | LW 414, SKW 372, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q13_FIOK_OK | D6 | LW 414, SKW 372, oldal 290 (NL 300), fenék besüllyesztés 13 mm – MOVENTO szabályok szerint |
| Q14_FIOK_MOZGAS_OK | D1 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D2 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D3 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D4 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D5 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D6 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q21_SZERSZAM_NINCS | KIMETSZES | 14 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |

## Homlokzati rések mozgó elemek körül (front-sík, ≤ 10 mm)

| A | B | rés mm | átfedés mm² |
|---|---|---|---|
| KI12-TV01F-01 | KI12-TV01F-02 | 3.0 | 0.0 |
| KI12-TV01F-01 | KI12-TV02F1-01 | 3.0 | 0.0 |
| KI12-TV01F-02 | KI12-TV02F1-01 | 3.0 | 0.0 |
| KI12-TV02F1-01 | KI12-TV02F2-01 | 3.0 | 0.0 |
| KI12-TV02F2-01 | KI12-TV02F2-02 | 3.0 | 0.0 |
| KI12-TV02F2-02 | KI12-TV02F2-03 | 3.0 | 0.0 |
| KI12-TV02F2-03 | KI12-TV02F2-04 | 3.0 | 0.0 |
| KI12-TV02F2-04 | KI16-M6-FRONT-04 | 3.0 | 0.0 |

## Hatókör – amit ez a QA NEM bizonyít

- Valós pánt/sín kinematika, kábelpálya, LED-profilok, R16 hardware_geometry befoglalók ütközése (csak a 106 lapalkatrész).
- Ajtónyitás söpört térfogata (R16 pánt: Blum 70T3550.TL + 173H7100, gyári kinematika nélkül).
- Lapméret és élanyag: becsült értékek a `gyartasi_szabalyok_v1.json`-ból, termék nincs kiválasztva.
- Gépi ütköztetés, nullpont, él-kód sorrend: az asztalos konvenciójának megerősítéséig javaslat.
- Helyszíni felmérés nincs; a méretlánc tervi.

# S16 F1 – QA-jelentés (S16-R15B-GY-v1)

Generálva: 2026-10-30 · `qa_parts_v1.py` · forrás: `parts_v1.json` (129 alkatrész)

**Ítélet: adatmodell konzisztens (műhelyi megerősítés még kell)**

| Súlyosság | db |
|---|---|
| BLOKKOLO | 0 |
| HIBA | 0 |
| FIGYELMEZTETES | 2 |
| INFO | 44 |

Geometria-forrás: {'R14_zart_halo': 127, 'doboz_minusz_kimetszes': 1, 'R14_kontur_extrudalas': 1} · vizsgált ütköző pár (befoglaló-átfedéssel): 27

## FIGYELMEZTETES (2)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q16_HIVATKOZAS_TISZTAZANDO | BG-LOWER-HIDDEN-RETURN | nincs ilyen test; R15-ben tisztázandóként rögzítve (layout.r15_tisztazando) – Blender-ellenőrzés, kitalált geometria nélkül |
| Q16_HIVATKOZAS_TISZTAZANDO | BG-UPPER-HIDDEN-RETURN | nincs ilyen test; R15-ben tisztázandóként rögzítve (layout.r15_tisztazando) – Blender-ellenőrzés, kitalált geometria nélkül |

## INFO (44)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q03_SZANDEKOS_RAHAGYAS | BG-1 | nyers 841.0×2405 a szabály-szövegben rögzített ráhagyással egyezik |
| Q03_SZANDEKOS_RAHAGYAS | BG-FINISH | nyers 2887×2405 a szabály-szövegben rögzített ráhagyással egyezik |
| Q07_OSSZEALLITAS_NEM_LAP | CURVE-B-BOT | IVES_SZERELVENY – T=337 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q07_OSSZEALLITAS_NEM_LAP | CURVE-B-TOP | IVES_SZERELVENY – T=337 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q07_OSSZEALLITAS_NEM_LAP | CURVE-T-BOT | IVES_SZERELVENY – T=337 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q07_OSSZEALLITAS_NEM_LAP | CURVE-T-TOP | IVES_SZERELVENY – T=337 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q07_OSSZEALLITAS_NEM_LAP | TV-SPACER-1 | OSSZEALLITAS – T=69 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q07_OSSZEALLITAS_NEM_LAP | TV-SPACER-2 | OSSZEALLITAS – T=69 befoglaló, nem lapvastagság; nem írható ki egy lapként |
| Q14_FIOK_MOZGAS_OK | D1 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D2 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D3 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D4 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D5 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q14_FIOK_MOZGAS_OK | D6 | 300 mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne) |
| Q16_TERMEK_HELYFOGLALO | I-D1-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-D2-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-D3-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-D4-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-D5-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-D6-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-TL-DIFFUSER | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-TL-HOUSING | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-TL-LOW-0 | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-TR-DIFFUSER | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | I-TR-HOUSING | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | PSU-INTERNAL | VASAROLT_KESZULEK / HELYFOGLALO |
| Q16_TERMEK_HELYFOGLALO | TEXTILE-RECESSED-HOUSING | BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó) |
| Q16_TERMEK_HELYFOGLALO | TV-CONSOLE-ENVELOPE | VASAROLT_KESZULEK / HELYFOGLALO |
| Q16_TERMEK_HELYFOGLALO | TV-SCREEN | VASAROLT_KESZULEK / HELYFOGLALO |
| Q18_FENYRES_SZABAD | fénytakarók | a résben ülő felfelé világító szerelvény fölött 21.0 mm szabad (R14 szándék: 4 mm-t foglal, 21 mm marad; min. 20 mm) |
| Q18_MENNYEZETI_RES | bútortest | legmagasabb pont Z=2875, rés a névleges 2900 mm-es mennyezetig 25 mm (helyszíni felmérés még nincs) |
| Q20_FALC_MERES | T-DOOR-L | HATSO_FENYFALC: mélység 10.0 mm, maradék 8.0 mm, perem 8 mm |
| Q20_FALC_MERES | TV-FIELD | FENYCSATORNA_FALC: mélység 12.0 mm, maradék 6.0 mm |
| Q21_SZERSZAM_NINCS | ATMENO_KIVAGAS | 1 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | FENYCSATORNA_FALC | 1 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | FRONTRÖGZÍTÉS_FURAT | 6 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | HATSO_FENYFALC | 1 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | KIMETSZES | 1 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | KONTUR_MARAS | 18 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | PANTKEHELY | 2 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | PANTTALP_FURAT | 3 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | SIN_KAPCSOLAT_MEGMUNKALAS | 18 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | SIN_RÖGZÍTÉS_FURAT | 12 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |
| Q21_SZERSZAM_NINCS | SULLYESZTETT_KAZETTA_NYILAS | 1 művelet szerszám-hozzárendelés nélkül – MPR nem generálható |

## Homlokzati rések mozgó elemek körül (front-sík, ≤ 10 mm)

| A | B | rés mm | átfedés mm² |
|---|---|---|---|
| D1-FRONT | D2-FRONT | 3.0 | 0.0 |
| D1-FRONT | FRAME-T-BOT | 3.0 | 0.0 |
| D1-FRONT | FRAME-T-MID | 3.0 | 0.0 |
| D1-FRONT | T-DOOR-L | 3.0 | 0.0 |
| D2-FRONT | D3-FRONT | 3.0 | 0.0 |
| D2-FRONT | FRAME-B-HIGH-1 | 3.0 | 0.0 |
| D2-FRONT | FRAME-B-LOW-1 | 3.0 | 0.0 |
| D3-FRONT | D4-FRONT | 3.0 | 0.0 |
| D3-FRONT | FRAME-B-HIGH-1 | 3.0 | 0.0 |
| D3-FRONT | FRAME-B-LOW-1 | 3.0 | 0.0 |
| D4-FRONT | D5-FRONT | 3.0 | 0.0 |
| D4-FRONT | FRAME-B-HIGH-2 | 3.0 | 0.0 |
| D4-FRONT | FRAME-B-LOW-2 | 3.0 | 0.0 |
| D5-FRONT | D6-FRONT | 3.0 | 0.0 |
| D5-FRONT | FRAME-B-HIGH-3 | 3.0 | 0.0 |
| D5-FRONT | FRAME-B-LOW-3 | 3.0 | 0.0 |
| D6-FRONT | FRAME-B-HIGH-3 | 3.0 | 0.0 |
| D6-FRONT | FRAME-B-LOW-3 | 3.0 | 0.0 |
| D6-FRONT | FRAME-B-R | 3.0 | 0.0 |
| T-DOOR-L | FRAME-T-BOT | 3.0 | 0.0 |
| T-DOOR-L | FRAME-T-L | 3.0 | 0.0 |
| T-DOOR-L | FRAME-T-MID | 3.0 | 0.0 |
| T-DOOR-L | FRAME-T-TOP | 3.0 | 0.0 |
| T-DOOR-L | T-DOOR-R | 3.0 | 0.0 |
| T-DOOR-R | FRAME-T-MID | 3.0 | 0.0 |
| T-DOOR-R | FRAME-T-R | 3.0 | 0.0 |

## Hatókör – amit ez a QA NEM bizonyít

- Valós pánt/sín kinematika, kábelpálya, LED-profilok és a 32 segédobjektum ütközése (csak a 120 fő alkatrész tömör geometriája).
- Ajtónyitás (pánttípus és -oldal nincs véglegesítve) – 2. fázis gyári CLIP top geometriával.
- Lapméret és élanyag: becsült értékek a `gyartasi_szabalyok_v1.json`-ból, termék nincs kiválasztva.
- Gépi ütköztetés, nullpont, él-kód sorrend: az asztalos konvenciójának megerősítéséig javaslat.
- Helyszíni felmérés nincs; a méretlánc tervi.

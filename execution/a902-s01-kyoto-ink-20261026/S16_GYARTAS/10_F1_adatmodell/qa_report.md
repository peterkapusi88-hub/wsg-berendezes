# S16 F1 – QA-jelentés (S16-GY-F1-v1)

Generálva: 2026-10-30 · `qa_parts_v1.py` · forrás: `parts_v1.json` (120 alkatrész)

**Ítélet: BLOKKOLT – gyártási kiadás tilos**

| Súlyosság | db |
|---|---|
| BLOKKOLO | 2 |
| HIBA | 16 |
| FIGYELMEZTETES | 12 |
| INFO | 41 |

Geometria-forrás: {'R14_zart_halo': 117, 'doboz_minusz_kimetszes': 1, 'R14_kontur_extrudalas': 2} · vizsgált ütköző pár (befoglaló-átfedéssel): 27

## BLOKKOLO (2)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q02_NYERS_KISEBB_MINT_KESZ | BG-1 | nyers W=2315 < élzárás előtti 2405.0 (kész 2405) – a darab nem gyártható le ebből a szabásból · forrás: R14 explicit raw_L/raw_W (forrásból átvéve – QA ellenőrzi) |
| Q02_NYERS_KISEBB_MINT_KESZ | BG-FINISH | nyers W=2315 < élzárás előtti 2405.0 (kész 2405) – a darab nem gyártható le ebből a szabásból · forrás: R14 explicit raw_L/raw_W (forrásból átvéve – QA ellenőrzi) |

## HIBA (16)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q03_SZOVEG_ADAT_ELTERES | BG-1 | R14 raw_rule szövege kész L=801 mm-t ír, az adat L=811.0 mm; nyers a szövegben 831, adatban 831 |
| Q03_SZOVEG_ADAT_ELTERES | BG-FINISH | R14 raw_rule szövege kész L=801 mm-t ír, az adat L=2857 mm; nyers a szövegben 831, adatban 2877 |
| Q07_VASTAGSAG_ANYAG_ELTERES | BATTEN-1 | T=8 mm, de az anyag (M01 – 18 mm kétoldalt melaminos grafitszürke bútorlap) névleges vastagsága 18 mm |
| Q07_VASTAGSAG_ANYAG_ELTERES | BATTEN-2 | T=8 mm, de az anyag (M01 – 18 mm kétoldalt melaminos grafitszürke bútorlap) névleges vastagsága 18 mm |
| Q07_VASTAGSAG_ANYAG_ELTERES | BATTEN-3 | T=8 mm, de az anyag (M01 – 18 mm kétoldalt melaminos grafitszürke bútorlap) névleges vastagsága 18 mm |
| Q07_VASTAGSAG_ANYAG_ELTERES | BATTEN-4 | T=8 mm, de az anyag (M01 – 18 mm kétoldalt melaminos grafitszürke bútorlap) névleges vastagsága 18 mm |
| Q07_VASTAGSAG_ANYAG_ELTERES | BATTEN-5 | T=8 mm, de az anyag (M01 – 18 mm kétoldalt melaminos grafitszürke bútorlap) névleges vastagsága 18 mm |
| Q07_VASTAGSAG_ANYAG_ELTERES | T-DOOR-L-BACK | T=12 mm, de az anyag (M02 – Szatén sötét barnásgrafit keret) névleges vastagsága 18 mm |
| Q13_BLUM_FENEK_BESULLYESZTES | D1 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q13_BLUM_FENEK_BESULLYESZTES | D2 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q13_BLUM_FENEK_BESULLYESZTES | D3 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q13_BLUM_FENEK_BESULLYESZTES | D4 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q13_BLUM_FENEK_BESULLYESZTES | D5 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q13_BLUM_FENEK_BESULLYESZTES | D6 | fiókfenék alsó síkja az oldal alsó élétől 0.0 mm-re van; MOVENTO-hoz ≥ 12 mm (max 15 mm mély) besüllyesztés kell, hogy a sín takarva legyen · forrás: https://ea.blum.com/en/building-a-movento-drawer/ (lekérve 2026-10-30) |
| Q16_HIVATKOZOTT_ALKATRESZ_HIANYZIK | BG-LOWER-HIDDEN-RETURN | a layout.json R14 'primary_changed' listája hivatkozza, de sem a parts.json-ban, sem a zárt jelenetben nincs ilyen test |
| Q16_HIVATKOZOTT_ALKATRESZ_HIANYZIK | BG-UPPER-HIDDEN-RETURN | a layout.json R14 'primary_changed' listája hivatkozza, de sem a parts.json-ban, sem a zárt jelenetben nincs ilyen test |

## FIGYELMEZTETES (12)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
| Q03_NYERS_SZABALY_ELLENTMONDAS | BG-1 | R14 explicit nyers 831×2315 ≠ anyagszabály szerinti 811.0×2405.0 |
| Q03_NYERS_SZABALY_ELLENTMONDAS | BG-FINISH | R14 explicit nyers 2877×2315 ≠ anyagszabály szerinti 2857.0×2405.0 |
| Q03_NYERS_SZABALY_ELLENTMONDAS | T-DOOR-L-BACK | R14 explicit nyers 370×2525 ≠ anyagszabály szerinti 380.0×2535.0 |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | DECK-CONTINUOUS-BAFFLE | R14 jelenet-segédobjektum (befoglaló [870.0, 109.0, 579.0, 2628.0, 4.0, 17.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | DECK-CONTINUOUS-COVER | R14 jelenet-segédobjektum (befoglaló [870.0, 101.0, 592.0, 2628.0, 8.0, 4.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | LOW-INTERNAL-LIGHT-VISOR | R14 jelenet-segédobjektum (befoglaló [57.0, 359.0, 554.0, 306.0, 5.0, 16.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | TOP-WASH-BAFFLE | R14 jelenet-segédobjektum (befoglaló [740.0, 34.0, 2857.0, 2857.0, 4.0, 18.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | TOP-WASH-COVER | R14 jelenet-segédobjektum (befoglaló [740.0, 26.0, 2872.0, 2857.0, 8.0, 3.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | TOP-WASH-HIDDEN-END | R14 jelenet-segédobjektum (befoglaló [3595.0, 26.0, 2857.0, 2.0, 8.0, 15.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | UPLIGHT-FRONT-VISOR | R14 jelenet-segédobjektum (befoglaló [740.0, 25.0, 2876.0, 2845.0, 4.0, 3.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | UPLIGHT-REAR-VISOR | R14 jelenet-segédobjektum (befoglaló [740.0, 5.0, 2876.0, 2845.0, 3.0, 3.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |
| Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN | UPLIGHT-TRAY | R14 jelenet-segédobjektum (befoglaló [740.0, 5.0, 2875.0, 2845.0, 24.0, 1.0]) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő |

## INFO (41)

| Kód | Alkatrész | Megállapítás |
|---|---|---|
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
| Q18_MENNYEZETI_RES | * | legmagasabb pont Z=2875, rés a névleges 2900 mm-es mennyezetig 25 mm (helyszíni felmérés még nincs) |
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

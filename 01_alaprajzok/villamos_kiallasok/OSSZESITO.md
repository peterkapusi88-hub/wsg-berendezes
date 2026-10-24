# Villamos kiállások – lakásonkénti összesítő

> Generált fájl (`kinyeres/osszesito.py`). A teljes, tételes lista a `<LAKÁS>_villamos.csv` / `.json` fájlokban van.
> Minden adat **TERV SZERINT**; a helyszíni ellenőrzésig nem HELYSZÍNEN MÉRT. Koordináták méterben, lakásonkénti rendszerben (lásd README).

## A-811

Forrás: `WGR1_meretezett_alaprajzok.pdf` 5. oldal (dosszié 150), 1:50, M1 (érvényes; KORR-alaprajz nem készült).

Koordináta-origó: x=0: 04 nappali homlokzati (erkélyajtós, rajzon bal) belső falsíkja; y=0: 05.1 szoba rajzon alsó belső falsíkja. Helyi rendszer (Blender-modell még nincs).

| Típus | db |
|---|---|
| dugalj | 44 |
| kapcsolo | 21 |
| mennyezeti_lampakiallas | 16 |
| fali_lampakiallas | 6 |
| gyengearamu_aljzat | 6 |
| R_jelu_kiallas – motoros redőny (valószínű) | 5 |
| ventilator_kiallas | 3 |
| hangjelzo_vagy_erzekelo – mozgásérzékelő (valószínű) | 3 |
| termosztat | 3 |
| fix_bekotes | 1 |
| antenna_tv_aljzat | 1 |
| BK_doboz – riasztóközpont (valószínű) | 1 |
| lakaselosztó | 1 |
| kezelo_billentyuzet | 1 |
| bejarati_ajto_eszkoz | 1 |
| EPH_csatlakozo | 1 |
| kaputelefon_belteri | 1 |

### Mennyezeti lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y |
|---|---|---|---|---|
| A811-ML01 | 01 ELŐTÉR | a | 7,26 | 7,28 |
| A811-ML02 | 02 KONYHA | c | 6,91 | 10,05 |
| A811-ML03 | 03-04 ÉTKEZŐ-NAPPALI | e,f | 2,21 | 8,95 |
| A811-ML04 | 03-04 ÉTKEZŐ-NAPPALI | g | 5,27 | 8,95 |
| A811-ML05 | 05.1 SZOBA | n | 1,91 | 1,35 |
| A811-ML06 | 05.2-3 SZOBA | m | 1,61 | 5,20 |
| A811-ML07 | 05.2-3 SZOBA | m | 1,61 | 3,33 |
| A811-ML08 | 05.2-3 SZOBA | l | 4,17 | 3,33 |
| A811-ML09 | 05.2-3 SZOBA (gardrób) | l | 4,17 | 5,20 |
| A811-ML10 | 06.1 FÜRDŐ | s | 7,26 | 1,25 |
| A811-ML11 | 06.2 FÜRDŐ | u | 7,26 | 3,67 |
| A811-ML12 | 07 KÖZLEKEDŐ | h | 5,64 | 7,28 |
| A811-ML13 | 07 KÖZLEKEDŐ | h | 5,64 | 5,08 |
| A811-ML14 | 07 KÖZLEKEDŐ | h | 5,64 | 2,88 |
| A811-ML15 | 08 WC | b | 7,78 | 5,92 |
| A811-ML16 | 09 HTH | r | 5,64 | 0,75 |

### Fali lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y | Magasság |
|---|---|---|---|---|---|
| A811-FL01 | 02 KONYHA | d | 8,23 | 10,08 | nincs a rajzon |
| A811-FL02 | 03-04 ÉTKEZŐ-NAPPALI |  | 0,30 | 11,54 | 2,65 |
| A811-FL03 | 06.1 FÜRDŐ | t | 8,23 | 2,02 | nincs a rajzon |
| A811-FL04 | 06.2 FÜRDŐ | v | 6,81 | 4,66 | nincs a rajzon |
| A811-FL05 | 10 ERKÉLY | k | -0,47 | 8,62 | nincs a rajzon |
| A811-FL06 | 10 ERKÉLY | p | -0,47 | 2,85 | nincs a rajzon |

### Helyiségenként (darab)

| Helyiség | mennyezeti lámpa | fali lámpa | kapcsoló | dugalj | gyengeáram | TV/antenna | ventilátor | R (redőny?) | termosztát | egyéb |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 ELŐTÉR | 1 |  | 2 | 2 |  |  |  |  |  | bejarati_ajto_eszkoz, kezelo_billentyuzet, lakaselosztó |
| 02 KONYHA | 1 | 1 |  | 7 |  |  |  |  |  | fix_bekotes |
| 03-04 ÉTKEZŐ-NAPPALI | 2 | 1 | 6 | 8 | 4 | 1 |  | 3 | 1 | hangjelzo_vagy_erzekelo |
| 05.1 SZOBA | 1 |  | 2 | 8 | 1 |  |  | 1 | 1 | hangjelzo_vagy_erzekelo |
| 05.2-3 SZOBA | 3 |  | 3 | 5 | 1 |  |  | 1 |  | hangjelzo_vagy_erzekelo |
| 05.2-3 SZOBA (gardrób) | 1 |  | 2 | 3 |  |  |  |  | 1 | BK_doboz |
| 06.1 FÜRDŐ | 1 | 1 | 1 | 3 |  |  | 1 |  |  | EPH_csatlakozo |
| 06.2 FÜRDŐ | 1 | 1 |  | 3 |  |  | 1 |  |  |  |
| 07 KÖZLEKEDŐ | 3 |  | 4 | 1 |  |  |  |  |  | kaputelefon_belteri |
| 08 WC | 1 |  |  |  |  |  | 1 |  |  |  |
| 09 HTH | 1 |  | 1 | 3 |  |  |  |  |  |  |
| 10 ERKÉLY |  | 2 |  | 1 |  |  |  |  |  |  |

### Mennyezeti hűtő-fűtő mezők (ide nem fúrunk)

| Azonosító | Helyiség | x-tól | x-ig | y-tól | y-ig |
|---|---|---|---|---|---|
| A811-HF01 | 05.1 SZOBA | 0,00 | 4,42 | 0,00 | 2,70 |
| A811-HF02 | 05.2-3 SZOBA | 0,00 | 3,22 | 2,80 | 6,55 |
| A811-HF03 | 03-04 ÉTKEZŐ-NAPPALI | 0,13 | 6,60 | 7,92 | 11,55 |
| A811-HF04 | 05.2-3 SZOBA (gardrób) | 3,32 | 5,02 | 3,85 | 6,55 |
| A811-HF05 | 02 KONYHA | 6,27 | 7,58 | 8,55 | 10,82 |

### Mire készült – a rajzlap módosítási szövegéből

Forrás: 5. o. (alaprajz M1, dosszié 150) és 6. o. (parkoló, tároló, dosszié 151). Tömörítve; a hely a fenti táblákban és a CSV-ben van.

| Terület | Villamos módosítás |
|---|---|
| 02 KONYHA | A konyhatechnológia sorrendje megváltozik, az elektromos kiállások követik. +1 pultdugalj. Mikró m=1,30 m. |
| 03 ÉTKEZŐ | +1 „g” váltókapcsoló (a váltópárja a nappaliban). A „g” mennyezeti lámpakiállás helye módosul. |
| 04 NAPPALI | +1 oldalfali kiállás m=2,65 m. A konyhai pengefal megszűnése miatt a kapcsolók („g” és „c,d”), a termosztát és a **mozgásérzékelő** a nappali válaszfalának sarkára kerül. |
| 05.1 SZOBA | Az ágy két oldalán 1-1 többlet dugalj a meglévők mellé, m=65 cm. TV-blokk m=1,20 m. +2 dugalj. |
| 05.2-3 SZOBA | A két szoba összevonva. Az ágy két oldalán 1-1 többlet „m” váltókapcsoló a dugaljak mellé, m=65 cm. +2 mennyezeti lámpakiállás („m” és „l”); az „m” 3 helyről kapcsolható. A **biztonsági központ** áthelyezésre kerül. |
| 06.1 FÜRDŐ | A mosdó és a WC helycseréjét az elektromos kiállások követik; az elszívó ventilátor az ajtó mögül a mosdó fölé kerül. |
| 06.2 FÜRDŐ | Az elrendezés módosul, az elektromos kiállások követik. |
| 07 KÖZLEKEDŐ | A „h” mennyezeti lámpakiállás 3 helyről kapcsolható. |
| 09 HTH | +1 dugalj a szárítógépnek a mosógép-dugalj fölött; +1 dugalj a kapcsoló alatt. |

**Lakáson kívül:** AT8-03 szinti tároló: 2 dugalj. P-0-33 beálló: autótöltő. T-0-06 tároló és P-0-34 beálló: nincs módosítás.

**Álmennyezet:** Péter átvételi összesítője szerint gipszkarton álmennyezet csak az előtérben, a WC-ben és a fürdőben van, min. 2,40 m. A rajzon zöld „gk. álm.” felirat jelöli (imp. = impregnált, nor. = normál); a pontos kiterjedés helyszínen ellenőrizendő. Feliratok ezen a lapon: „imp.gk. álm.” – 08 WC (7,79; 5,90).

Átfedéskép: `A811_villamos_atfedes.png` · Tételes lista: `A811_villamos.csv`

## A-812

Forrás: `WGR1_meretezett_alaprajzok.pdf` 12. oldal (dosszié 179), 1:100, M1 KORR (2026.04.28.) – átnézeti lap 1:100, a teljes lakás (az 1:50-es 11. oldal csak részlet).

Koordináta-origó: x=0: 04 nappali homlokzati (erkélyajtós, rajzon bal) belső falsíkja; y=0: 04 nappali rajzon alsó belső falsíkja. Helyi rendszer (Blender-modell még nincs).

| Típus | db |
|---|---|
| dugalj | 50 |
| kapcsolo | 19 |
| mennyezeti_lampakiallas | 18 |
| gyengearamu_aljzat | 7 |
| R_jelu_kiallas – motoros redőny (valószínű) | 7 |
| fali_lampakiallas | 5 |
| termosztat | 4 |
| ventilator_kiallas | 3 |
| fix_bekotes | 1 |
| antenna_tv_aljzat | 1 |
| BK_doboz – riasztóközpont (valószínű) | 1 |
| hangjelzo_vagy_erzekelo – mozgásérzékelő (valószínű) | 1 |
| lakaselosztó | 1 |
| kezelo_billentyuzet | 1 |
| kaputelefon_belteri | 1 |
| bejarati_ajto_eszkoz | 1 |

### Mennyezeti lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y |
|---|---|---|---|---|
| A812-ML01 | 01 ELŐTÉR | a | 7,05 | 3,50 |
| A812-ML02 | 02 KONYHA | b | 6,95 | 1,43 |
| A812-ML03 | 03-04 ÉTKEZŐ-NAPPALI | j | 4,60 | 3,52 |
| A812-ML04 | 03-04 ÉTKEZŐ-NAPPALI | e,f | 1,61 | 2,80 |
| A812-ML05 | 03-04 ÉTKEZŐ-NAPPALI | d | 4,60 | 1,43 |
| A812-ML06 | 05.1 SZOBA | z | 4,42 | 6,34 |
| A812-ML07 | 05.2 SZOBA | v | 4,70 | 9,63 |
| A812-ML08 | 05.3 SZOBA | s | 4,87 | 14,78 |
| A812-ML09 | 06.1 FÜRDŐ (HTH) | n | 8,02 | 11,21 |
| A812-ML10 | 06.2 FÜRDŐ | t | 7,45 | 15,60 |
| A812-ML11 | 07 KÖZLEKEDŐ | h | 6,70 | 11,05 |
| A812-ML12 | 07 KÖZLEKEDŐ | h | 6,70 | 8,65 |
| A812-ML13 | 07 KÖZLEKEDŐ | h | 6,70 | 6,28 |
| A812-ML14 | 07 KÖZLEKEDŐ (gardrób rész) | k | 7,74 | 5,28 |
| A812-ML15 | 08/09 FÜRDŐ | m | 8,02 | 9,25 |
| A812-ML16 | 08/09 FÜRDŐ | m | 8,02 | 8,20 |
| A812-ML17 | 10.2 GARDRÓB | w | 4,39 | 11,73 |
| A812-ML18 | 10.3 GARDRÓB | r | 7,67 | 13,53 |

### Fali lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y | Magasság |
|---|---|---|---|---|---|
| A812-FL01 | 02 KONYHA | c | 6,70 | 2,79 | nincs a rajzon |
| A812-FL02 | 06.1 FÜRDŐ (HTH) | p | 8,63 | 11,01 | nincs a rajzon |
| A812-FL03 | 06.2 FÜRDŐ | u | 7,26 | 16,73 | nincs a rajzon |
| A812-FL04 | 08/09 FÜRDŐ | l | 8,64 | 8,35 | nincs a rajzon |
| A812-FL05 | 11 ERKÉLY | g | -0,47 | 2,75 | nincs a rajzon |

### Helyiségenként (darab)

| Helyiség | mennyezeti lámpa | fali lámpa | kapcsoló | dugalj | gyengeáram | TV/antenna | ventilátor | R (redőny?) | termosztát | egyéb |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 ELŐTÉR | 1 |  | 6 | 3 |  |  |  |  | 1 | bejarati_ajto_eszkoz, hangjelzo_vagy_erzekelo, kaputelefon_belteri, kezelo_billentyuzet, lakaselosztó |
| 02 KONYHA | 1 | 1 |  | 9 |  |  |  |  |  | fix_bekotes |
| 03-04 ÉTKEZŐ-NAPPALI | 3 |  | 2 | 7 | 4 | 1 |  | 2 |  |  |
| 05.1 SZOBA | 1 |  | 1 | 4 | 1 |  |  | 1 | 1 |  |
| 05.2 SZOBA | 1 |  | 1 | 6 | 1 |  |  | 2 | 1 |  |
| 05.3 SZOBA | 1 |  | 1 | 6 | 1 |  |  | 2 | 1 |  |
| 06.1 FÜRDŐ (HTH) | 1 | 1 |  | 4 |  |  | 1 |  |  |  |
| 06.2 FÜRDŐ | 1 | 1 |  | 3 |  |  | 1 |  |  |  |
| 07 KÖZLEKEDŐ | 3 |  | 6 | 1 |  |  |  |  |  |  |
| 07 KÖZLEKEDŐ (gardrób rész) | 1 |  |  | 1 |  |  |  |  |  | BK_doboz |
| 08/09 FÜRDŐ | 2 | 1 |  | 3 |  |  | 1 |  |  |  |
| 10.2 GARDRÓB | 1 |  | 1 | 1 |  |  |  |  |  |  |
| 10.3 GARDRÓB | 1 |  | 1 | 1 |  |  |  |  |  |  |
| 11 ERKÉLY |  | 1 |  | 1 |  |  |  |  |  |  |

### Mennyezeti hűtő-fűtő mezők (ide nem fúrunk)

| Azonosító | Helyiség | x-tól | x-ig | y-tól | y-ig |
|---|---|---|---|---|---|
| A812-HF01 | 03-04 ÉTKEZŐ-NAPPALI | 0,00 | 5,82 | -0,00 | 4,70 |
| A812-HF02 | 03-04 ÉTKEZŐ-NAPPALI | 0,96 | 5,74 | 0,78 | 4,63 |
| A812-HF03 | 05.1 SZOBA | 3,32 | 5,30 | 4,80 | 7,65 |
| A812-HF04 | 05.2 SZOBA | 3,32 | 6,00 | 7,99 | 11,14 |
| A812-HF05 | 10.2 GARDRÓB | 3,32 | 5,47 | 11,28 | 12,63 |
| A812-HF06 | 05.3 SZOBA | 3,32 | 6,42 | 12,73 | 16,82 |
| A812-HF07 | 05.1 SZOBA | 4,21 | 5,47 | 6,08 | 7,89 |
| A812-HF08 | 10.3 GARDRÓB | 6,29 | 8,59 | 12,74 | 14,27 |

### Mire készült – a rajzlap módosítási szövegéből

Forrás: 11. o. (alaprajz M1 KORR 2026.04.28., dosszié 178) és 13. o. (parkoló, tároló, dosszié 160). Tömörítve; a hely a fenti táblákban és a CSV-ben van.

| Terület | Villamos módosítás |
|---|---|
| 02 KONYHA | +2 pultdugalj. |
| 05.2 SZOBA | Az ágy két oldalán 1-1 többlet dugalj a meglévők mellé, m=65 cm. TV-blokk m=1,20 m. |
| 05.3 SZOBA | Az ágy melletti dugaljak m=65 cm-re kerülnek; +2 dugalj m=65 cm. |
| 06.1 HTH | +1 dugalj a szárítógépnek a mosógép-dugalj fölött. |
| 08/09 FÜRDŐ | A WC és a HTH fürdővé vonva össze. Az „m” és „l” lámpák egy csillárkapcsolóra kerülnek. Az elszívó ventilátor páraérzékelős típus lesz. |
| 07 KÖZLEKEDŐ | KORREKCIÓ 2026.04.28.: a közlekedői gardróbrészben nem kell gipszkarton álmennyezet. |

**Lakáson kívül:** AT8-02 szinti tároló: 2 dugalj. P-0-32 beálló: autótöltő. T-0-03 tároló és P-0-31 beálló: nincs módosítás.

**Álmennyezet:** Péter átvételi összesítője szerint gipszkarton álmennyezet csak az előtérben, a WC-ben és a fürdőben van, min. 2,40 m. A rajzon zöld „gk. álm.” felirat jelöli (imp. = impregnált, nor. = normál); a pontos kiterjedés helyszínen ellenőrizendő. Feliratok ezen a lapon: „gk. álm.” – 01 ELŐTÉR (7,89; 4,12); „nor. gk. álm.” – 02 KONYHA (7,84; 0,24).

Átfedéskép: `A812_villamos_atfedes.png` · Tételes lista: `A812_villamos.csv`

## A-902

Forrás: `WGR1_meretezett_alaprajzok.pdf` 18. oldal (dosszié 176), 1:50, M1 KORR 2 (rajz 2025.12.15., kiküldve 2025.12.18.; tartalmazza a 2025.10.13-i KORR-t).

Koordináta-origó: x=0: 05.1 szoba homlokzati (rajzon bal) belső falsíkja; y=0: 05.2 szoba rajzon alsó belső falsíkja. Azonos a Blender-modell (WSG_A902_*) koordinátáival.

| Típus | db |
|---|---|
| dugalj | 49 |
| kapcsolo | 29 |
| mennyezeti_lampakiallas | 12 |
| fali_lampakiallas | 7 |
| gyengearamu_aljzat | 7 |
| R_jelu_kiallas – motoros redőny (valószínű) | 6 |
| hangjelzo_vagy_erzekelo – mozgásérzékelő (valószínű) | 4 |
| termosztat | 4 |
| ventilator_kiallas | 3 |
| fix_bekotes | 1 |
| antenna_tv_aljzat | 1 |
| BK_doboz – riasztóközpont (valószínű) | 1 |
| lakaselosztó | 1 |
| kezelo_billentyuzet | 1 |
| kaputelefon_belteri | 1 |
| bejarati_ajto_eszkoz | 1 |
| EPH_csatlakozo | 1 |
| jakuzzi_aramkiallas | 1 |

### Mennyezeti lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y |
|---|---|---|---|---|
| A902-ML01 | 01 ELŐTÉR | a | 7,82 | 2,45 |
| A902-ML02 | 01 ELŐTÉR | a | 6,45 | 1,32 |
| A902-ML03 | 02 KONYHA | c | 9,50 | 2,70 |
| A902-ML04 | 03 ÉTKEZŐ | b | 8,55 | 6,27 |
| A902-ML05 | 04 NAPPALI | n,p | 5,62 | 6,27 |
| A902-ML06 | 05.1 SZOBA | t | 1,83 | 6,05 |
| A902-ML07 | 05.2 SZOBA | s | 1,82 | 1,32 |
| A902-ML08 | 05.3 SZOBA | e | 12,81 | 6,07 |
| A902-ML09 | 06.1 FÜRDŐ | k | 4,62 | 1,32 |
| A902-ML10 | 06.2 FÜRDŐ | f | 15,45 | 6,62 |
| A902-ML11 | 07 KÖZLEKEDŐ | r | 3,86 | 3,40 |
| A902-ML12 | 08 WC | m | 6,11 | 3,02 |

### Fali lámpakiállások

| Azonosító | Helyiség | Áramkör | x | y | Magasság |
|---|---|---|---|---|---|
| A902-FL01 | 02 KONYHA | d | 10,53 | 3,15 | nincs a rajzon |
| A902-FL02 | 04 NAPPALI |  | 3,68 | 7,85 | 2,85 |
| A902-FL03 | 06.1 FÜRDŐ | l | 5,48 | 1,32 | nincs a rajzon |
| A902-FL04 | 06.2 FÜRDŐ | g | 16,38 | 6,62 | nincs a rajzon |
| A902-FL05 | 09 TERASZ | v | 6,69 | 8,53 | nincs a rajzon |
| A902-FL06 | 10 TERASZ | h | 12,96 | 8,53 | nincs a rajzon |
| A902-FL07 | 13 ERKÉLY | u | -0,47 | 3,11 | nincs a rajzon |

### Helyiségenként (darab)

| Helyiség | mennyezeti lámpa | fali lámpa | kapcsoló | dugalj | gyengeáram | TV/antenna | ventilátor | R (redőny?) | termosztát | egyéb |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 ELŐTÉR | 2 |  | 1 | 1 |  |  |  |  |  | bejarati_ajto_eszkoz, kaputelefon_belteri, kezelo_billentyuzet, lakaselosztó |
| 02 KONYHA | 1 | 1 | 2 | 9 |  |  |  |  |  | fix_bekotes |
| 03 ÉTKEZŐ | 1 |  | 6 | 4 |  |  |  | 1 |  |  |
| 04 NAPPALI | 1 | 1 | 3 | 5 | 4 | 1 |  | 1 | 1 | hangjelzo_vagy_erzekelo |
| 05.1 SZOBA | 1 |  | 4 | 6 |  |  |  | 2 | 1 | BK_doboz, hangjelzo_vagy_erzekelo |
| 05.1 SZOBA (északi fülke) |  |  |  | 1 | 1 |  |  |  |  |  |
| 05.2 SZOBA | 1 |  | 2 | 3 |  |  |  | 1 | 1 | hangjelzo_vagy_erzekelo |
| 05.2 SZOBA (gardróbfülke) |  |  |  | 2 | 1 |  |  |  |  |  |
| 05.3 SZOBA | 1 |  | 4 | 8 | 1 |  |  | 1 | 1 | hangjelzo_vagy_erzekelo |
| 06.1 FÜRDŐ | 1 | 1 | 1 | 3 |  |  | 1 |  |  | EPH_csatlakozo |
| 06.2 FÜRDŐ | 1 | 1 | 1 | 3 |  |  | 1 |  |  |  |
| 07 KÖZLEKEDŐ | 1 |  | 4 | 1 |  |  |  |  |  |  |
| 08 WC | 1 |  | 1 |  |  |  | 1 |  |  |  |
| 09 TERASZ |  | 1 |  | 1 |  |  |  |  |  | jakuzzi_aramkiallas |
| 10 TERASZ |  | 1 |  | 1 |  |  |  |  |  |  |
| 13 ERKÉLY |  | 1 |  | 1 |  |  |  |  |  |  |

### Mennyezeti hűtő-fűtő mezők (ide nem fúrunk)

| Azonosító | Helyiség | x-tól | x-ig | y-tól | y-ig |
|---|---|---|---|---|---|
| A902-HF01 | 05.2 SZOBA | -0,00 | 3,65 | -0,00 | 2,65 |
| A902-HF02 | 05.1 SZOBA | -0,00 | 3,67 | 3,45 | 8,05 |
| A902-HF03 | 04 NAPPALI | 3,77 | 9,80 | 4,05 | 8,05 |
| A902-HF04 | 02 KONYHA | 9,05 | 9,95 | 2,40 | 4,05 |
| A902-HF05 | 05.3 SZOBA | 10,85 | 14,37 | 4,10 | 8,05 |

### Mire készült – a rajzlap módosítási szövegéből

Forrás: 19. o. (átnézeti M1 KORR 2, dosszié 177) és 20. o. (parkoló, tároló, dosszié 170). Tömörítve; a hely a fenti táblákban és a CSV-ben van.

| Terület | Villamos módosítás |
|---|---|
| 01 ELŐTÉR / 02 KONYHA | Az előtér és a konyha közötti pengefal megszűnik, a konyhai kapcsolóblokk követi a változást. |
| 02 KONYHA | Sütő m=1,10 m, mikró m=1,30 m (magasszekrény a folyosó felé eső falon). A mosogató feletti falikar-kiállás és a mosogatógép-dugalj követi az új helyet. A pultdugaljak helye megváltozik; +1 pultdugalj a meglévővel egy szerelvényben. |
| 02 KONYHA | KORR 2 (2025.12.15.): a „d” kapcsoló változik. |
| 03 ÉTKEZŐ | A „b” mennyezeti lámpakiállás eltolva. |
| 04 NAPPALI | +1 falikar-kiállás a 05.1 szoba felé eső válaszfalon, m=2,85 m. Az „n,p” mennyezeti lámpakiállás eltolva. |
| 05.1 SZOBA | A válaszfal a szoba felé tolódik. Az ágy két oldalán 1-1 dugalj + 1-1 váltókapcsoló egy szerelvényben, m=65 cm. **+1 dugalj szekrényvilágításhoz.** |
| 05.2 SZOBA | +1 dugalj a TV-blokk részeként. |
| 05.3 SZOBA | Az ágy két oldalán 1-1 dugalj + 1-1 váltókapcsoló egy szerelvényben, m=65 cm. **+2 dugalj szekrényvilágításhoz.** |
| 06.2 FÜRDŐ | A törölközőszárító (TSZ) a szoba felé eső válaszfalra kerül, a kiállása követi. |

**Lakáson kívül:** AT8-01 szinti tároló: 2 dugalj. P-0-65 beálló: autótöltő. T-0-26 tároló és P-0-64 beálló: nincs módosítás.

**Álmennyezet:** Péter átvételi összesítője szerint gipszkarton álmennyezet csak az előtérben, a WC-ben és a fürdőben van, min. 2,40 m. A rajzon zöld „gk. álm.” felirat jelöli (imp. = impregnált, nor. = normál); a pontos kiterjedés helyszínen ellenőrizendő. Feliratok ezen a lapon: „imp. gk. álm.” – 08 WC (5,45; 3,50); „imp. gk. álm.” – 08 WC (6,00; 3,88).

Átfedéskép: `A902_villamos_atfedes.png` · Tételes lista: `A902_villamos.csv`


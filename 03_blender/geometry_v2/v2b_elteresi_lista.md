# A-902 geometria v2b – eltéréslista (v2 → v2b), 2026-10-24

Alap: `WSG_A902_v2_terasz_ELOZETES_20261024.blend` (változatlan). Kimenet: `WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` (új fájl). Az élő `WSG_A902_stilusok.blend` érintetlen; a tetőkert (A902_Terasz_v2_ELOZETES, 43 elem) változatlan.

Forrás-hierarchia: (1) méretezett megvalósulási alaprajz M1 KORR 2 (PDF vektor, 18. o.), (2) műszaki ellenőri mérés, (3) fotó/videó, (4) Blender v1/v2, (5) becslés = ELŐZETES.
Bbox-formátum: [x0; y0; z0; x1; y1; z1] m, vakolatlan tervsíkok. A bútor nem mozdult – az új falakkal ütköző bútort a validátor-riport listázza.

**Státuszosztályok:** TERV SZERINT IGAZOLT · HELYSZÍNEN MÉRT · FOTÓVAL ALÁTÁMASZTOTT · ELŐZETES · MÉRENDŐ

| Státusz | db |
|---|---|
| TERV SZERINT IGAZOLT | 123 |
| TERV SZERINT IGAZOLT + HELYSZÍNEN MÉRT | 1 |
| ELŐZETES / MÉRENDŐ | 1 |

## Falak (48)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `Kulso_Ny_szemoldok1` | [-0,3; 0,05; 2,55; 0; 1,93; 2,9] | [-0,3; 0,06; 2,57; 0; 1,94; 2,9] | 2 cm | TERV SZERINT IGAZOLT | 05.2 erkélyajtó 1,88/2,57; tok y 0,059–1,939 |
| `Kulso_Ny_1` | [-0,3; 1,93; 0; 0; 4,25; 2,9] | [-0,3; 1,94; 0; 0; 4,28; 2,9] | 3 cm | TERV SZERINT IGAZOLT | nyílásvégek a tokvonalakhoz (1,939 / 4,274) |
| `Kulso_Ny_szemoldok2` | [-0,3; 4,25; 2,55; 0; 7,9; 2,9] | [-0,3; 4,28; 2,57; 0; 7,92; 2,9] | 3 cm | TERV SZERINT IGAZOLT | 05.1 üvegfal 3,65/2,57; tok y 4,274–7,924 |
| `Kulso_Ny_2` | [-0,3; 7,9; 0; 0; 8,95; 2,9] | [-0,3; 7,92; 0; 0; 8,95; 2,9] | 2 cm | TERV SZERINT IGAZOLT | tok y 7,924 |
| `Kulso_D_eloter_sarok_0` | [6,6; -0,3; 0; 6,9; 0,35; 2,9] | [6,7; -0,3; 0; 6,95; 0,6; 2,9] | 25 cm | TERV SZERINT IGAZOLT | V 6,699 / 6,949 (y −0,31…0,60) |
| `Kulso_D_eloter_0` | [6,6; 0,35; 0; 7,3; 0,65; 2,9] | [6,7; 0,6; 0; 7,3; 0,85; 2,9] | 25 cm | TERV SZERINT IGAZOLT | V 6,699 (…0,849); ajtótok 7,299 (y 0,599–0,849) |
| `Kulso_D_eloter_szemoldok1` | [7,3; 0,35; 2,1; 8,35; 0,65; 2,9] | [7,3; 0,6; 2,1; 8,35; 0,85; 2,9] | 25 cm | TERV SZERINT IGAZOLT | bejárati ajtó 1,05/2,10, tok 7,299–8,349 |
| `Kulso_D_eloter_1` | [8,35; 0,35; 0; 8,55; 0,65; 2,9] | [8,35; 0,6; 0; 8,6; 1,35; 2,9] | 70 cm | TERV SZERINT IGAZOLT | V 8,349 / 8,599 (y 0,60–1,35) |
| `Kulso_tomb_eloter_konyha` | [8,45; 0,35; 0; 9,1; 1,3; 2,9] | [8,6; 1,1; 0; 9,1; 1,35; 2,9] | 75 cm | TERV SZERINT IGAZOLT | a 65 cm-es „tömb” helyett a konyha D-i fala: H 1,099 / 1,349 |
| `Kulso_D_konyha_0` | [9,1; 1; 0; 10,9; 1,3; 2,9] | [9,1; 1,1; 0; 10,85; 1,35; 2,9] | 10 cm | TERV SZERINT IGAZOLT | H 1,099 / 1,349 (x 8,60–10,55) |
| `Beepitett_szekreny_eloter` | [8,45; 1,3; 0; 9; 2,3; 2,9] | [8,95; 1,35; 0; 9,05; 2,35; 2,9] | 50 cm | TERV SZERINT IGAZOLT | a tömör „szekrénytömb” helyett a fülke K-i fala: V 8,949 / 9,049; a fülke az előtér felé nyitott |
| `Fal_konyha_Ny_0` | [8,45; 2,3; 0; 8,55; 4,04; 2,9] | [8,35; 2,35; 0; 8,45; 4,05; 0,85] | 205 cm | TERV SZERINT IGAZOLT | V 8,348 / 8,448 (y 2,35–4,05); −10 cm; MAGASSÁG 0,85 m: a terven „pm.:85.0 cm”, a módosítás szerint „pengefal helyett 85 cm magas, erősített gipszkarton fal” (M1 KORR 2) |
| `Kulso_K_konyha_05_3_0` | [10,64; 1; 0; 10,9; 6,1; 2,9] | [10,55; 1,1; 0; 10,85; 4,1; 2,9] | 200 cm | TERV SZERINT IGAZOLT | konyha K-i fala: V 10,549 / 10,849; −9 cm a belső síkon |
| `Kulso_K_konyha_05_3_szemoldok1` | [10,64; 6,1; 2,1; 10,9; 7; 2,9] | [10,75; 6,05; 2,1; 10,85; 6,95; 2,9] | 11 cm | TERV SZERINT IGAZOLT | 05.3 ajtó 90/2,10, tok y 6,049–6,949 |
| `Kulso_K_konyha_05_3_1` | [10,64; 7; 0; 10,9; 7,1; 2,9] | [10,75; 6,95; 0; 10,85; 7,025; 2,9] | 11 cm | TERV SZERINT IGAZOLT | nappali|05.3 válaszfal 10 cm: V 10,749 / 10,849 |
| `Akna_etkezo_05_3` | [10; 7,1; 0; 11; 7,97; 2,9] | [9,8; 7,025; 0; 11,1; 8,05; 2,9] | 20 cm | TERV SZERINT IGAZOLT | akna: V 9,799 / 11,099, H 7,024; pillér 10,80–11,10 a 05.3 ÉNy-i sarkában |
| `Kulso_D_05_3_06_2_0` | [10,9; 3,74; 0; 16,8; 4,04; 2,9] | [10,85; 3,85; 0; 16,7; 4,1; 2,9] | 11 cm | TERV SZERINT IGAZOLT | H 3,849 / 4,099 (05.3 D-i belső sík +6 cm) |
| `Akna_06_2` | [14,6; 4,04; 0; 16,8; 5,13; 2,9] | [15; 4,1; 0; 16,4; 5,2; 2,9] | 40 cm | TERV SZERINT IGAZOLT | gépészeti tömb: V 14,999…16,399, H 4,099 / 5,199; a 14,37–15,00 sáv a 05.3 fülkéje |
| `Kulso_K_06_2_0` | [16,5; 5,13; 0; 16,8; 8,27; 2,9] | [16,4; 4,1; 0; 16,7; 8,35; 2,9] | 103 cm | TERV SZERINT IGAZOLT | V 16,399 / 16,699; −10 cm |
| `Fal_05_3_06_2_0` | [14,5; 4,04; 0; 14,6; 6,05; 2,9] | [14,375; 5,1; 0; 14,475; 6,3; 2,9] | 106 cm | TERV SZERINT IGAZOLT | V 14,374 / 14,474; −12,6 cm |
| `Fal_05_3_06_2_szemoldok1` | [14,5; 6,05; 2,1; 14,6; 6,8; 2,9] | [14,375; 6,3; 2,1; 14,475; 7,05; 2,9] | 25 cm | TERV SZERINT IGAZOLT | 06.2 ajtó 75/2,10, tok y 6,299–7,049 |
| `Fal_05_3_06_2_1` | [14,5; 6,8; 0; 14,6; 7,97; 2,9] | [14,375; 7,05; 0; 14,475; 8,05; 2,9] | 25 cm | TERV SZERINT IGAZOLT | V 14,374 / 14,474 |
| `Kulso_E_terasz_0` | [3,4; 7,97; 0; 4,5; 8,27; 2,9] | [3,32; 8,05; 0; 4,38; 8,35; 2,9] | 12 cm | TERV SZERINT IGAZOLT | H 8,049 / 8,349; nyílás falazott kávája 4,379 |
| `Kulso_E_terasz_szemoldok1` | [4,5; 7,97; 2,55; 9; 8,27; 2,9] | [4,38; 8,05; 2,53; 9; 8,35; 2,9] | 12 cm | TERV SZERINT IGAZOLT | nappali üvegfal 4,50/2,53; káva 4,379–8,999 |
| `Kulso_E_terasz_1` | [9; 7,97; 0; 12,2; 8,27; 2,9] | [9; 8,05; 0; 12; 8,35; 2,9] | 20 cm | TERV SZERINT IGAZOLT | H 8,049 / 8,349; káva 8,999 / 11,999 |
| `Kulso_E_terasz_szemoldok2` | [12,2; 7,97; 2,55; 14; 8,27; 2,9] | [12; 8,05; 2,53; 13,92; 8,35; 2,9] | 20 cm | TERV SZERINT IGAZOLT | 05.3 teraszajtó 1,80/2,53; káva 11,999–13,919 |
| `Kulso_E_terasz_2` | [14; 7,97; 0; 16,8; 8,27; 2,9] | [13,92; 8,05; 0; 16,7; 8,35; 2,9] | 10 cm | TERV SZERINT IGAZOLT | H 8,049 / 8,349 |
| `Pillér_05_1_EK` | [2,95; 7,97; 0; 3,4; 9,25; 2,9] | [3,02; 8,04; 0; 3,32; 9,25; 2,9] | 8 cm | TERV SZERINT IGAZOLT | V 3,019 / 3,319, H 8,039 |
| `Fal_05_1_nappali_0` | [3,62; 3,94; 0; 3,72; 7,97; 2,9] | [3,57; 4,05; 0; 3,67; 8,05; 2,9] | 11 cm | TERV SZERINT IGAZOLT + HELYSZÍNEN MÉRT | V 3,569 / 3,669; méretszám 3,57 és 7,08; Kémeri 05.1 = 3,548 (vakolt) |
| `Fal_eloszoba_E_05_1ajto_0` | [2,42; 3,94; 0; 2,63; 4,04; 2,9] | [2,42; 3,95; 0; 2,594; 4,05; 2,9] | 4 cm | TERV SZERINT IGAZOLT | 05.1 ajtótok 2,594 |
| `Fal_eloszoba_E_05_1ajto_szemoldok1` | [2,63; 3,94; 2,1; 3,53; 4,04; 2,9] | [2,594; 3,95; 2,1; 3,494; 4,05; 2,9] | 4 cm | TERV SZERINT IGAZOLT | 05.1 ajtó 90/2,10, tok x 2,594–3,494 |
| `Fal_eloszoba_E_05_1ajto_1` | [3,53; 3,94; 0; 3,72; 4,04; 2,9] | [3,494; 3,95; 0; 3,67; 4,05; 2,9] | 5 cm | TERV SZERINT IGAZOLT | tok 3,494 → válaszfal 3,669 |
| `Fal_eloszoba_Ny_0` | [2,42; 2,55; 0; 2,52; 3,94; 2,9] | [2,42; 2,65; 0; 2,52; 3,95; 2,9] | 10 cm | TERV SZERINT IGAZOLT | V 2,419 / 2,519 |
| `Fal_eloszoba_D_05_2ajto_0` | [2,42; 2,55; 0; 2,63; 2,65; 2,9] | [2,42; 2,65; 0; 2,674; 2,75; 2,9] | 10 cm | TERV SZERINT IGAZOLT | H 2,649 / 2,749 (+10 cm); 05.2 ajtótok 2,674 |
| `Fal_eloszoba_D_05_2ajto_szemoldok1` | [2,63; 2,55; 2,1; 3,53; 2,65; 2,9] | [2,674; 2,65; 2,1; 3,574; 2,75; 2,9] | 10 cm | TERV SZERINT IGAZOLT | 05.2 ajtó 90/2,10, tok x 2,674–3,574 |
| `Fal_eloszoba_D_05_2ajto_1` | [3,53; 2,55; 0; 3,72; 2,65; 2,9] | [3,574; 2,65; 0; 3,75; 2,75; 2,9] | 10 cm | TERV SZERINT IGAZOLT | tok 3,574 |
| `Fal_05_2_furdo_0` | [3,62; 0; 0; 3,72; 2,65; 2,9] | [3,65; 0; 0; 3,75; 2,65; 2,9] | 3 cm | TERV SZERINT IGAZOLT | V 3,649 / 3,749; méretszám 3,65 és 1,75 |
| `Fal_furdo_E_0` | [3,72; 2,55; 0; 3,95; 2,65; 2,9] | [3,75; 2,65; 0; 3,824; 2,75; 2,9] | 13 cm | TERV SZERINT IGAZOLT | 06.1 ajtótok 3,824 |
| `Fal_furdo_E_szemoldok1` | [3,95; 2,55; 2,1; 4,7; 2,65; 2,9] | [3,824; 2,65; 2,1; 4,574; 2,75; 2,9] | 13 cm | TERV SZERINT IGAZOLT | 06.1 ajtó 75/2,10, tok x 3,824–4,574 |
| `Fal_furdo_E_1` | [4,7; 2,55; 0; 5,55; 2,65; 2,9] | [4,574; 2,65; 0; 5,6; 2,75; 2,9] | 13 cm | TERV SZERINT IGAZOLT | H 2,649 / 2,749 (x 4,574–5,599) |
| `Fal_furdo_wc_K_0` | [5,45; 0; 0; 5,55; 4,04; 2,9] | [5,5; 0; 0; 5,6; 2,75; 2,9] | 129 cm | TERV SZERINT IGAZOLT | V 5,499 / 5,599 (y 0–2,75); +5 cm; északon nem folytatódik |
| `Pillér_kozlekedo` | [5; 2,9; 0; 5,45; 3,35; 2,9] | [5; 2,95; 0; 5,2; 3,45; 2,9] | 25 cm | TERV SZERINT IGAZOLT | H 2,949 / 3,449, V 4,999; a 30-as méretszám a pillér + fal |
| `Fal_wc_D_0` | [5,55; 1,95; 0; 5,7; 2,05; 2,9] | [5,6; 2; 0; 5,774; 2,1; 2,9] | 7 cm | TERV SZERINT IGAZOLT | H 1,999 / 2,099 (+5 cm); WC-ajtótok 5,774 |
| `Fal_wc_D_szemoldok1` | [5,7; 1,95; 2,1; 6,45; 2,05; 2,9] | [5,774; 2; 2,1; 6,524; 2,1; 2,9] | 7 cm | TERV SZERINT IGAZOLT | WC-ajtó 75/2,10, tok x 5,774–6,524 |
| `Fal_wc_D_1` | [6,45; 1,95; 0; 6,6; 2,05; 2,9] | [6,524; 2; 0; 6,6; 2,1; 2,9] | 7 cm | TERV SZERINT IGAZOLT | tok 6,524 → akna 6,599 |
| `Akna_WC_gepeszet` | [6,6; 1,95; 0; 7,4; 4,04; 2,9] | [6,6; 2; 0; 7,3; 3,95; 2,9] | 10 cm | TERV SZERINT IGAZOLT | V 6,599 / 7,299, H 1,999 / 3,949; K-i sík −10 cm (az átjáró 1,05 marad) |
| `Fal_wc_E_nappali_0` | [5,55; 3,94; 0; 6,6; 4,04; 2,9] | [5,2; 3,95; 0; 7,3; 4,05; 2,9] | 70 cm | TERV SZERINT IGAZOLT | H 3,949 / 4,049 (x 5,20–7,30) |
| `Szemoldok_atjaro_eloter_nappali` | [7,4; 3,94; 2,1; 8,55; 4,04; 2,9] | [7,3; 3,95; 2,1; 8,45; 4,05; 2,9] | 10 cm | ELŐZETES / MÉRENDŐ | átjáró x 7,30–8,35 a terv szerint; a 2,10-es szemöldök a v1 brosúrából – NEM igazolt |

## új fal (6)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `Fal_kozlekedo_wc_v2b` | – | [5,2; 2,75; 0; 5,3; 4,05; 2,9] | új | TERV SZERINT IGAZOLT | V 5,199 / 5,299 (y 2,75–4,05) – közlekedő|WC fal; a WC É-i része 1,30 széles (méretszám) |
| `Akna_WC_gepeszet_b_v2b` | – | [6,45; 3,25; 0; 6,6; 3,95; 2,9] | új | TERV SZERINT IGAZOLT | V 6,449, H 3,249 – a WC L-alakja (ÉK-i sarok) |
| `Fal_szekrenyfulke_E_v2b` | – | [8,35; 2,25; 0; 9,05; 2,35; 2,9] | új | TERV SZERINT IGAZOLT | H 2,249 / 2,349 (x 8,35–9,05) – az előtéri fülke É-i fala |
| `Fal_konyha_K_csonk_v2b` | – | [10,55; 4,1; 0; 10,85; 5,05; 2,9] | új | TERV SZERINT IGAZOLT | V 10,549 / 10,849, H 4,099 / 5,049 – gépészeti csonk + szerelt GK technikai fal (elszívó) |
| `Fal_nappali_05_3_v2b_0` | – | [10,75; 5,05; 0; 10,85; 6,05; 2,9] | új | TERV SZERINT IGAZOLT | V 10,749 / 10,849 (y 5,06–6,05) |
| `Fal_06_2_D_v2b` | – | [14,375; 5,1; 0; 15; 5,2; 2,9] | új | TERV SZERINT IGAZOLT | H 5,099 / 5,199 – 06.2 D-i fala = a 05.3 DK-i fülke É-i fala |

## ajtó (28)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `Ajto_05_1_tok_b` | [2,63; 3,94; 0; 2,66; 4,04; 2,1] | [2,594; 3,95; 0; 2,624; 4,05; 2,1] | 4 cm | TERV SZERINT IGAZOLT | tok x 2,594–3,494 (−3,6 cm) |
| `Ajto_05_1_tok_j` | [3,5; 3,94; 0; 3,53; 4,04; 2,1] | [3,464; 3,95; 0; 3,494; 4,05; 2,1] | 4 cm | TERV SZERINT IGAZOLT | tok x 2,594–3,494 (−3,6 cm) |
| `Ajto_05_1_tok_f` | [2,63; 3,94; 2,07; 3,53; 4,04; 2,1] | [2,594; 3,95; 2,07; 3,494; 4,05; 2,1] | 4 cm | TERV SZERINT IGAZOLT | tok x 2,594–3,494 (−3,6 cm) |
| `Ajto_05_1_lap` | [2,66; 3,97; 0; 3,5; 4,01; 2,08] | [2,624; 3,98; 0; 3,464; 4,02; 2,08] | 4 cm | TERV SZERINT IGAZOLT | tok x 2,594–3,494 (−3,6 cm) |
| `Ajto_05_2_tok_b` | [2,63; 2,55; 0; 2,66; 2,65; 2,1] | [2,674; 2,65; 0; 2,704; 2,75; 2,1] | 10 cm | TERV SZERINT IGAZOLT | tok x 2,674–3,574 (+4,4 cm), fal +10 cm |
| `Ajto_05_2_tok_j` | [3,5; 2,55; 0; 3,53; 2,65; 2,1] | [3,544; 2,65; 0; 3,574; 2,75; 2,1] | 10 cm | TERV SZERINT IGAZOLT | tok x 2,674–3,574 (+4,4 cm), fal +10 cm |
| `Ajto_05_2_tok_f` | [2,63; 2,55; 2,07; 3,53; 2,65; 2,1] | [2,674; 2,65; 2,07; 3,574; 2,75; 2,1] | 10 cm | TERV SZERINT IGAZOLT | tok x 2,674–3,574 (+4,4 cm), fal +10 cm |
| `Ajto_05_2_lap` | [2,66; 2,58; 0; 3,5; 2,62; 2,08] | [2,704; 2,68; 0; 3,544; 2,72; 2,08] | 10 cm | TERV SZERINT IGAZOLT | tok x 2,674–3,574 (+4,4 cm), fal +10 cm |
| `Ajto_furdo_06_1_tok_b` | [3,95; 2,55; 0; 3,98; 2,65; 2,1] | [3,824; 2,65; 0; 3,854; 2,75; 2,1] | 13 cm | TERV SZERINT IGAZOLT | tok x 3,824–4,574 (−12,6 cm) |
| `Ajto_furdo_06_1_tok_j` | [4,67; 2,55; 0; 4,7; 2,65; 2,1] | [4,544; 2,65; 0; 4,574; 2,75; 2,1] | 13 cm | TERV SZERINT IGAZOLT | tok x 3,824–4,574 (−12,6 cm) |
| `Ajto_furdo_06_1_tok_f` | [3,95; 2,55; 2,07; 4,7; 2,65; 2,1] | [3,824; 2,65; 2,07; 4,574; 2,75; 2,1] | 13 cm | TERV SZERINT IGAZOLT | tok x 3,824–4,574 (−12,6 cm) |
| `Ajto_furdo_06_1_lap` | [3,98; 2,58; 0; 4,67; 2,62; 2,08] | [3,854; 2,68; 0; 4,544; 2,72; 2,08] | 13 cm | TERV SZERINT IGAZOLT | tok x 3,824–4,574 (−12,6 cm) |
| `Ajto_WC_tok_b` | [5,7; 1,95; 0; 5,73; 2,05; 2,1] | [5,774; 2; 0; 5,804; 2,1; 2,1] | 7 cm | TERV SZERINT IGAZOLT | tok x 5,774–6,524 (+7,4 cm) |
| `Ajto_WC_tok_j` | [6,42; 1,95; 0; 6,45; 2,05; 2,1] | [6,494; 2; 0; 6,524; 2,1; 2,1] | 7 cm | TERV SZERINT IGAZOLT | tok x 5,774–6,524 (+7,4 cm) |
| `Ajto_WC_tok_f` | [5,7; 1,95; 2,07; 6,45; 2,05; 2,1] | [5,774; 2; 2,07; 6,524; 2,1; 2,1] | 7 cm | TERV SZERINT IGAZOLT | tok x 5,774–6,524 (+7,4 cm) |
| `Ajto_WC_lap` | [5,73; 1,98; 0; 6,42; 2,02; 2,08] | [5,804; 2,03; 0; 6,494; 2,07; 2,08] | 7 cm | TERV SZERINT IGAZOLT | tok x 5,774–6,524 (+7,4 cm) |
| `Ajto_bejarat_tok_b` | [7,3; 0,35; 0; 7,33; 0,65; 2,1] | [7,3; 0,6; 0; 7,33; 0,85; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok x 7,299–8,349 (egyezik), fal y 0,60–0,85 (+25 cm) |
| `Ajto_bejarat_tok_j` | [8,32; 0,35; 0; 8,35; 0,65; 2,1] | [8,32; 0,6; 0; 8,35; 0,85; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok x 7,299–8,349 (egyezik), fal y 0,60–0,85 (+25 cm) |
| `Ajto_bejarat_tok_f` | [7,3; 0,35; 2,07; 8,35; 0,65; 2,1] | [7,3; 0,6; 2,07; 8,35; 0,85; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok x 7,299–8,349 (egyezik), fal y 0,60–0,85 (+25 cm) |
| `Ajto_bejarat_lap` | [7,33; 0,48; 0; 8,32; 0,52; 2,08] | [7,33; 0,705; 0; 8,32; 0,745; 2,08] | 22 cm | TERV SZERINT IGAZOLT | tok x 7,299–8,349 (egyezik), fal y 0,60–0,85 (+25 cm) |
| `Ajto_05_3_tok_b` | [10,64; 6,1; 0; 10,9; 6,13; 2,1] | [10,75; 6,05; 0; 10,85; 6,08; 2,1] | 11 cm | TERV SZERINT IGAZOLT | tok y 6,049–6,949 (−5 cm), fal 10,75–10,85 |
| `Ajto_05_3_tok_j` | [10,64; 6,97; 0; 10,9; 7; 2,1] | [10,75; 6,92; 0; 10,85; 6,95; 2,1] | 11 cm | TERV SZERINT IGAZOLT | tok y 6,049–6,949 (−5 cm), fal 10,75–10,85 |
| `Ajto_05_3_tok_f` | [10,64; 6,1; 2,07; 10,9; 7; 2,1] | [10,75; 6,05; 2,07; 10,85; 6,95; 2,1] | 11 cm | TERV SZERINT IGAZOLT | tok y 6,049–6,949 (−5 cm), fal 10,75–10,85 |
| `Ajto_05_3_lap` | [10,75; 6,13; 0; 10,79; 6,97; 2,08] | [10,78; 6,08; 0; 10,82; 6,92; 2,08] | 5 cm | TERV SZERINT IGAZOLT | tok y 6,049–6,949 (−5 cm), fal 10,75–10,85 |
| `Ajto_06_2_tok_b` | [14,5; 6,05; 0; 14,6; 6,08; 2,1] | [14,375; 6,3; 0; 14,475; 6,33; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok y 6,299–7,049 (+25 cm) |
| `Ajto_06_2_tok_j` | [14,5; 6,77; 0; 14,6; 6,8; 2,1] | [14,375; 7,02; 0; 14,475; 7,05; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok y 6,299–7,049 (+25 cm) |
| `Ajto_06_2_tok_f` | [14,5; 6,05; 2,07; 14,6; 6,8; 2,1] | [14,375; 6,3; 2,07; 14,475; 7,05; 2,1] | 25 cm | TERV SZERINT IGAZOLT | tok y 6,299–7,049 (+25 cm) |
| `Ajto_06_2_lap` | [14,53; 6,08; 0; 14,57; 6,77; 2,08] | [14,405; 6,33; 0; 14,445; 7,02; 2,08] | 25 cm | TERV SZERINT IGAZOLT | tok y 6,299–7,049 (+25 cm) |

## üvegfal (24)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `Uvegfal_nappali_terasz_also` | [4,5; 8,09; 0; 9; 8,15; 0,05] | [4,44; 8,21; 0; 8,94; 8,33; 0,05] | 18 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_felso` | [4,5; 8,09; 2,5; 9; 8,15; 2,55] | [4,44; 8,21; 2,48; 8,94; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_uveg` | [4,5; 8,1; 0,02; 9; 8,14; 2,52] | [4,44; 8,25; 0,02; 8,94; 8,29; 2,5] | 15 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_profil0` | [4,47; 8,09; 0; 4,53; 8,15; 2,55] | [4,41; 8,21; 0; 4,47; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_profil3` | [8,97; 8,09; 0; 9,03; 8,15; 2,55] | [8,91; 8,21; 0; 8,97; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_profil1` | [5,97; 8,09; 0; 6,03; 8,15; 2,55] | [6,227; 8,21; 0; 6,287; 8,33; 2,53] | 26 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_nappali_terasz_profil2` | [7,47; 8,09; 0; 7,53; 8,15; 2,55] | [7,919; 8,21; 0; 7,979; 8,33; 2,53] | 45 cm | TERV SZERINT IGAZOLT | tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53 |
| `Uvegfal_05_3_terasz_also` | [12,2; 8,09; 0; 14; 8,15; 0,05] | [12,06; 8,21; 0; 13,86; 8,33; 0,05] | 18 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_3_terasz_felso` | [12,2; 8,09; 2,5; 14; 8,15; 2,55] | [12,06; 8,21; 2,48; 13,86; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_3_terasz_uveg` | [12,2; 8,1; 0,02; 14; 8,14; 2,52] | [12,06; 8,25; 0,02; 13,86; 8,29; 2,5] | 15 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_3_terasz_profil0` | [12,17; 8,09; 0; 12,23; 8,15; 2,55] | [12,03; 8,21; 0; 12,09; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_3_terasz_profil2` | [13,97; 8,09; 0; 14,03; 8,15; 2,55] | [13,83; 8,21; 0; 13,89; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_3_terasz_profil1` | [13,07; 8,09; 0; 13,13; 8,15; 2,55] | [12,905; 8,21; 0; 12,965; 8,33; 2,53] | 18 cm | TERV SZERINT IGAZOLT | tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53 |
| `Uvegfal_05_1_erkely_also` | [-0,18; 4,25; 0; -0,12; 7,9; 0,05] | [-0,28; 4,28; 0; -0,2; 7,92; 0,05] | 10 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Uvegfal_05_1_erkely_felso` | [-0,18; 4,25; 2,5; -0,12; 7,9; 2,55] | [-0,28; 4,28; 2,52; -0,2; 7,92; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Uvegfal_05_1_erkely_uveg` | [-0,17; 4,25; 0,02; -0,13; 7,9; 2,52] | [-0,254; 4,28; 0,02; -0,226; 7,92; 2,54] | 10 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Uvegfal_05_1_erkely_profil0` | [-0,18; 4,22; 0; -0,12; 4,28; 2,55] | [-0,28; 4,25; 0; -0,2; 4,31; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Uvegfal_05_1_erkely_profil2` | [-0,18; 7,87; 0; -0,12; 7,93; 2,55] | [-0,28; 7,89; 0; -0,2; 7,95; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Uvegfal_05_1_erkely_profil1` | [-0,18; 6,045; 0; -0,12; 6,105; 2,55] | [-0,28; 5,154; 0; -0,2; 5,214; 2,57] | 89 cm | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Erkelyajto_05_2_also` | [-0,18; 0,05; 0; -0,12; 1,93; 0,05] | [-0,28; 0,06; 0; -0,2; 1,94; 0,05] | 10 cm | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |
| `Erkelyajto_05_2_felso` | [-0,18; 0,05; 2,5; -0,12; 1,93; 2,55] | [-0,28; 0,06; 2,52; -0,2; 1,94; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |
| `Erkelyajto_05_2_uveg` | [-0,17; 0,05; 0,02; -0,13; 1,93; 2,52] | [-0,254; 0,06; 0,02; -0,226; 1,94; 2,54] | 10 cm | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |
| `Erkelyajto_05_2_profil0` | [-0,18; 0,02; 0; -0,12; 0,08; 2,55] | [-0,28; 0,03; 0; -0,2; 0,09; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |
| `Erkelyajto_05_2_profil1` | [-0,18; 1,9; 0; -0,12; 1,96; 2,55] | [-0,28; 1,91; 0; -0,2; 1,97; 2,57] | 10 cm | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |

## új osztó (2)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `Uvegfal_05_1_erkely_profil_v2b_5184` | – | [-0,28; 6,054; 0; -0,2; 6,114; 2,57] | új | TERV SZERINT IGAZOLT | tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57 |
| `Erkelyajto_05_2_profil_v2b_1029` | – | [-0,28; 0,999; 0; -0,2; 1,059; 2,57] | új | TERV SZERINT IGAZOLT | tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57 |

## padló (13)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `P_05_1` | [0; 3,45; -0,02; 3,62; 7,97; 0] | [0; 3,45; -0,02; 3,57; 8,05; 0] | 8 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_05_1_eszaki` | [0; 7,97; -0,02; 2,95; 8,95; 0] | [0; 8,05; -0,02; 3,02; 8,95; 0] | 8 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_05_2` | [0; 0; -0,02; 3,62; 2,55; 0] | [0; 0; -0,02; 3,65; 2,65; 0] | 10 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_05_2_gardrob` | [0; 2,55; -0,02; 2,42; 3,35; 0] | [0; 2,65; -0,02; 2,42; 3,35; 0] | 10 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_05_3` | [11; 4,04; -0,02; 14,5; 7,97; 0] | [10,85; 4,1; -0,02; 14,375; 8,05; 0] | 15 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_eloszoba_kozlekedo` | [2,52; 2,65; -0,02; 5,45; 4,04; 0] | [2,52; 2,75; -0,02; 5,2; 4,05; 0] | 25 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_eloter` | [5,55; 0; -0,02; 8,45; 1,95; 0] | [5,6; 0; -0,02; 6,7; 2; 0] | 175 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_eloter_atjaro` | [7,4; 1,95; -0,02; 8,45; 4,04; 0] | [7,3; 2; -0,02; 8,35; 4,05; 0] | 10 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_furdo_06_1` | [3,72; 0; -0,02; 5,45; 2,55; 0] | [3,75; 0; -0,02; 5,5; 2,65; 0] | 10 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_furdo_06_2` | [14,6; 5,13; -0,02; 16,5; 7,97; 0] | [14,475; 5,2; -0,02; 16,4; 8,05; 0] | 12 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_konyha` | [8,55; 1,3; -0,02; 10,64; 5,15; 0] | [8,45; 1,35; -0,02; 10,55; 4,05; 0] | 110 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_nappali_etkezo` | [3,72; 4,04; -0,02; 10,64; 7,97; 0] | [3,67; 4,05; -0,02; 10,75; 8,05; 0] | 11 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |
| `P_wc` | [5,55; 2,05; -0,02; 6,6; 3,94; 0] | [5,6; 2,1; -0,02; 6,6; 3,95; 0] | 5 cm | TERV SZERINT IGAZOLT | helyiség a tervi falsíkok között |

## új padló (4)

| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |
|---|---|---|---|---|---|
| `P_eloter_b_v2b` | – | [6,7; 0,85; -0,02; 8,35; 2; 0] | új | TERV SZERINT IGAZOLT | előtér K-i része (a bejárati fal mögött) |
| `P_eloter_fulke_v2b` | – | [8,35; 1,35; -0,02; 8,95; 2,25; 0] | új | TERV SZERINT IGAZOLT | előtéri fülke (a tömör „szekrénytömb” helyén; funkció ELŐZETES) |
| `P_05_3_fulke_v2b` | – | [14,375; 4,1; -0,02; 15; 5,1; 0] | új | TERV SZERINT IGAZOLT | 05.3 DK-i fülke |
| `P_wc_b_v2b` | – | [5,3; 2,75; -0,02; 5,6; 3,95; 0] | új | TERV SZERINT IGAZOLT | WC É-i része 1,30 széles (L-alak) |

## Anyagok (53 objektum) – FOTÓVAL ALÁTÁMASZTOTT

Belül fehér nyílászáró-profil, világosszürke beltéri ajtólap, szürke tok, fehér fal és mennyezet, szürkésbarna parkettatónus (deszkaminta nincs modellezve).

| Változás | db |
|---|---|
| belül fehér profil | 22 |
| szürke tok | 18 |
| világosszürke ajtólap | 6 |
| bejárati ajtó belül fehér | 4 |
| semleges fehér (régi (0.93, 0.92, 0.9)) | 1 |
| semleges fehér (régi (0.96, 0.96, 0.95)) | 1 |
| szürkésbarna tónus a ME-BAL-080 fotóhoz (deszkaminta NINCS modellezve) | 1 |

## Nem változott, MÉRENDŐ (hétfő)

- Terasz: a WPC-nyelv bejáratát keresztező betonszegély, a lépcső helye, a zöldtető +0,77 m-es szintje (Codex-audit 3.) – a modellben nem javítottuk, mert nincs bizonyíték.
- Teraszüvegezés osztása (ME-BAL-045 fotó vs terv) – a terv szerinti 4,50 m-es tolóajtó maradt.
- Vakolt falsíkok (a terv vakolatlan; kb. 1–2 cm-rel beljebb).


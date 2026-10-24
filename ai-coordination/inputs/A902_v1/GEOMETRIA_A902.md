# A-902 – rögzített geometria (Astra-input, v1 · 2026-10-24)

**Forrás:** `03_blender/geometry_lock_A902.json` (a Blender-modellből gépileg kiírva) – a modell a **brosúra-alaprajz** alapján készült, **helyszíni méréssel még nincs igazolva**. Koordináta: méter, origó a 05.2 szoba DNy-i sarka, x = kelet, y = észak. Fal belső síkok közti értékek.
**Szabály a tervezéshez:** falak, nyílászárók, pillérek, aknák, belmagasság **fixek** (nincs bontás, gipszkarton, áthelyezés). Bútor, lamella/panel/tapéta, asztalos tömeg, világítás szabadon tervezhető.

## Belmagasság
- Szerződéses: **2,90 m ± 3 cm** (A-902, 9. em.). A modell 2,90-nel számol. **A 2026-10-21-i két független mérés eredménye még nincs a projektben** → ha 2,87 alatt van valahol, a padlótól plafonig tömegek magasságát ahhoz kell igazítani.
- Mennyezeti fűtő-hűtő panelek: **fúrás csak panel nélküli zónába**. A panelek kiosztása nem ismert → függesztett lámpa, függönysín, mennyezeti rögzítés **csak a kiosztás ismeretében véglegesíthető**.

## Helyiségek (modell)
| Helyiség | x (m) | y (m) | méret (m) | m² |
|---|---|---|---|---|
| 05.2 háló | 0.00–3.62 | 0.00–2.55 | 3.62 × 2.55 | 9.2 |
| 05.2 gardróbfülke | 0.00–2.42 | 2.55–3.35 | 2.42 × 0.80 | 1.9 |
| 05.1 master | 0.00–3.62 | 3.45–7.97 | 3.62 × 4.52 | 16.4 |
| 05.1 északi nyúlvány | 0.00–2.95 | 7.97–8.95 | 2.95 × 0.98 | 2.9 |
| közlekedő | 2.52–5.45 | 2.65–4.04 | 2.93 × 1.39 | 4.1 |
| nappali + étkező | 3.72–10.64 | 4.04–7.97 | 6.92 × 3.93 | 27.2 |
| 05.3 háló/dolgozó | 11.00–14.50 | 4.04–7.97 | 3.50 × 3.93 | 13.8 |
| 06.1 fürdő (kád) | 3.72–5.45 | 0.00–2.55 | 1.73 × 2.55 | 4.4 |
| WC | 5.55–6.60 | 2.05–3.94 | 1.05 × 1.89 | 2.0 |
| előtér (bejárat) | 5.55–8.45 | 0.00–1.95 | 2.90 × 1.95 | 5.7 |
| átjáró előtér→nappali | 7.40–8.45 | 1.95–4.04 | 1.05 × 2.09 | 2.2 |
| konyha (nyitott, a nappaliba fut) | 8.55–10.64 | 1.30–5.15 | 2.09 × 3.85 | 8.0 |
| 06.2 en-suite (zuhany, 05.3-hoz) | 14.60–16.50 | 5.13–7.97 | 1.90 × 2.84 | 5.4 |

## Ajtók
| Ajtó | szélesség | magasság | hely |
|---|---|---|---|
| 05_1 | 90 cm (tokkal) | 210 cm | x 2.63–3.53, y≈3.99 |
| 05_2 | 90 cm (tokkal) | 210 cm | x 2.63–3.53, y≈2.60 |
| 05_3 | 90 cm (tokkal) | 210 cm | y 6.10–7.00, x≈10.77 |
| 06_2 | 75 cm (tokkal) | 210 cm | y 6.05–6.80, x≈14.55 |
| WC | 75 cm (tokkal) | 210 cm | x 5.70–6.45, y≈2.00 |
| bejarat | 105 cm (tokkal) | 210 cm | x 7.30–8.35, y≈0.50 |
| furdo_06_1 | 75 cm (tokkal) | 210 cm | x 3.95–4.70, y≈2.60 |

## Üvegfalak, erkélyajtó (padlótól, keskeny fekete profil)
| Elem | szélesség | magasság | osztás | hely |
|---|---|---|---|---|
| Erkelyajto_05_2 | 1.88 m | 2.55 m (parapet nélkül, padlótól) | 1 mező | y 0.05–1.93, x≈-0.17 |
| Uvegfal_05_1_erkely | 3.65 m | 2.55 m (parapet nélkül, padlótól) | 2 mező | y 4.25–7.90, x≈-0.17 |
| Uvegfal_05_3_terasz | 1.80 m | 2.55 m (parapet nélkül, padlótól) | 2 mező | x 12.20–14.00, y≈8.10 |
| Uvegfal_nappali_terasz | 4.50 m | 2.55 m (parapet nélkül, padlótól) | 3 mező | x 4.50–9.00, y≈8.10 |

## Fix szerkezeti elemek
- Pillér a 05.1 ÉK-i sarkánál (x 2,95–3,40, y 7,97–9,25), pillér a közlekedőben (x 5,00–5,45, y 2,90–3,35).
- Gépészeti aknák: WC mögött (x 6,60–7,40, y 1,95–4,04) – ez a „TV-fal" lehetséges hordozó fala a nappali felé; étkező ÉK-i sarka (x 10,00–11,00, y 7,10–7,97); 06.2 mellett (x 14,6–16,8, y 4,04–5,13).
- Szemöldök az előtér–nappali átjáró fölött 2,10 m-en (x 7,40–8,55).
- Beépített szekrény-tömb az előtérben (x 8,45–9,00, y 1,30–2,30) – a brosúra szerint, ellenőrizendő.

## Terasz és erkély (modell, padló-felületek)
| Felület | x | y | m² |
|---|---|---|---|
| T_09_greslap | 3.40–9.60 | 8.27–12.70 | 27.5 |
| T_11_fa | 9.60–11.50 | 8.27–14.50 | 11.8 |
| T_10_greslap | 11.50–16.80 | 8.27–12.70 | 23.5 |
| T_12_kert | 3.40–16.80 | 12.70–20.40 | 103.2 |
| T_12_kert_b | 11.50–16.80 | 12.70–14.50 | 9.5 |
| Erkely_13 | -2.30–-0.30 | 0.00–6.05 | 12.1 |
Szerződés szerint terasz **79,22 m²** (zöldterasszal); a brosúra 158 m²-t (ebből 84 m² tetőkert) ír → **a használható felület és a jakuzzi-előkészítés pontos helye helyszíni méréssel ellenőrizendő.** Jakuzzi: 9. emelet → szállítás/daru/terhelhetőség külön tisztázandó.

## Kamerák (rögzítve – minden stílus ugyanebből renderel, hogy összevethető legyen)
| Kamera | típus | pozíció (x, y, z m) | objektív |
|---|---|---|---|
| Cam_01_Felulnezet | ORTHO | (8.25, 10.0, 40.0) | 24.0 mm · ortho 23.0 m |
| Cam_02_Nappali_terasz | PERSP | (8.3, 4.4, 1.55) | 20.0 mm |
| Cam_03_Etkezo_konyha | PERSP | (4.7, 7.7, 1.5) | 20.0 mm |
| Cam_04_Master | PERSP | (0.35, 4.3, 1.5) | 20.0 mm |
| Cam_05_Terasz | PERSP | (11.5, 15.5, 1.7) | 24.0 mm |
| Cam_06_Alaprajz_lakas | ORTHO | (8.25, 4.5, 40.0) | 24.0 mm · ortho 18.0 m |
Nézetek: Cam_02 = nappali a terasz felé, Cam_03 = étkező–konyha, Cam_04 = master, Cam_05 = terasz kívülről, Cam_06 = alaprajz felülnézet.

## Ellenőrizendő méretek (helyszíni mérés 2026-10-27 és az átvételi jegyzőkönyv alapján)
1. Belmagasság helyiségenként (2,90 ± 3 cm).
2. Nappali hossza: modell 6,92 m, GOAL/brosúra 7,08 m; étkező mélysége 2,80 m.
3. 05.1 master: modell 3,62 × 4,52 + 2,95 × 0,98 északi nyúlvány; GOAL 3,57 × 5,50 (4,00 tiszta + gardróbfülke).
4. Konyhafal (keleti) hossza: modell 3,85 m, GOAL 3,90 m; konyhai víz-/szennyvíz-/elektromos kiállások helye (**nincs a modellben** – a konyha elrendezésének kulcsa).
5. Mosó-szárító helye (HTH / fürdő) – nem ismert.
6. Fűtő-hűtő mennyezeti panelek kiosztása; dugaljak, TV-kiállás, ágy melletti dugaljak (a brosúra/vevői módosítás szerint, nincs modellezve).
7. Terasz pontos kontúrja, jakuzzi-előkészítés helye, kültéri víz/áram.
8. Előtéri beépített tömb valós mérete.

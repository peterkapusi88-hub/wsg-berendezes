# A-902 – U/L kanapé a nappali-étkezőben (2026-10-24)

**Státusz:** `MÉRETPRÓBA` – nem stílusterv. Geometria: `03_blender/geometry_lock_A902_v2b.json` (main, terv szerinti), helyszínen nem mért. A nyitott PR #11 (lock v2b-1) a nappalit nem érinti.

**Kérdés:** Péter (18:23): „Nagyon fontos, hogy a 902-be is U, de minimum L alakú legyen a kanapé.” A többi lakásnál hozott döntései:
- az étkező a terv helyén, a lámpája alatt marad;
- a TV helye szabad, csak meglévő dugalj kell mögé;
- egy szűkebb mellékút elfogadható, ha máshol így sokkal jobb.

## Röviden
- **A U elfér: Péter rajza (18:36) szerint, de 0,45 m-rel északabbra, a teraszüveg felé tolva.**
  - A rajz helyén délen csak 0,44 m maradna, és ott megy a bejárattól a hálók folyosójához vezető fő út.
  - Feljebb tolva ott 0,90 m marad, az üveg előtt pedig 0,10–0,20 m.
- **Legjobb változat: U 3,00 × 2,20 (P902_22).**
  - A nyitott oldal a gyári TV-blokk (nyugati fal) felé néz, a háta az étkező felé.
  - A teraszhoz a U és az asztal között 1,00 m-es út vezet. A hálók folyosójához kb. 0,85–0,90 m, a konyhához 1,00 m marad.
  - Nézőtáv 2,70 m, a U és a TV-konzol között 0,65 m.
  - Ha a U a TV felé 2,40 m mély (P902), a teraszhoz 0,80 m-es út marad.
- **A kanapétól független kötöttség – a 05.3-as háló ajtaja:**
  - A terv asztalhelyénél az asztal és a konyhapult benyúló sarka (x 9,95; y 5,25) között csak kb. 0,6 m marad. Ez a fejlesztő bútorrajzán is így van.
  - Ha az asztal 0,30 m-rel nyugatra kerül, ott 0,90 m lesz, és az ML04 lámpa legfeljebb kb. 0,2 m-re esik az asztal közepétől. A teraszhoz vezető út viszont a U mellett 0,75 m-re szűkül (P902_22A).
- **A teraszajtó:** a U előtt az üvegig 10–20 cm marad. Hétfőn meg kell nézni, melyik szárny tolható.
  - Ha a nyíló szárny a U mögé esik, a U szélessége legfeljebb kb. 2,2 m lehet, hogy az üveg mentén is 0,9 m maradjon.
  - Ha a nyíló szárny a U és az asztal közé esik, a fenti változatok jók.
- **Péter ötlete (18:39):** félhold alakú, ívelt kanapé pufffal, amely L-ként vagy U-ként működik. Ugyanebbe a befoglalóba ugyanígy elfér; a stílusterv (Astra) változatként vizsgálja.

## Péter U-ja (18:36) az ellenőrzővel
Rajz: `terv_elrendezes_A902.png`; adatok: `terv_elrendezes_A902.json`. A táblázat értékei célonként a legszélesebb utat mutatják (m, 5 cm-es lépés). A TV-konzol 180 × 45, a gyári blokk előtt.

| Változat | U (x × y) | Terasz | Hálók folyosója | Konyha | 05.3 háló | Nézőtáv | U–TV | Déli sáv | Az üveg előtt | U–asztal |
|---|---|---|---|---|---|---|---|---|---|---|
| P902_rajz – Péter rajza szerint | 2,42 × 2,99 | 0,75 | 0,55 | 1,00 | 0,60 | 2,92 | 0,65 | 0,44 | 0,57 | 0,79 |
| P902 – Péter U-ja 0,46 m-rel északabbra | 2,40 × 3,00 | 0,80 | 0,85 | 1,00 | 0,60 | 2,90 | 0,65 | 0,90 | 0,10 | 0,81 |
| P902_29 – U 2,40 × 2,90, az üveg előtt 0,20 m | 2,40 × 2,90 | 0,80 | 0,85 | 1,00 | 0,60 | 2,90 | 0,65 | 0,90 | 0,20 | 0,81 |
| P902_22 – U 2,20 × 3,00 (a TV felé 20 cm-rel rövidebb) | 2,20 × 3,00 | 1,00 | 0,85 | 1,00 | 0,60 | 2,70 | 0,65 | 0,90 | 0,10 | 1,01 |
| P902_22A – U 2,20 × 3,00, az asztal 0,30 m-rel nyugatra | 2,20 × 3,00 | 0,75 | 0,85 | 1,00 | 0,90 | 2,70 | 0,65 | 0,90 | 0,10 | 0,71 |

## Szigorú próba (minden út 0,90 m, kerülő nélkül)
`kanape_meretproba_a902.py` → `kanape_meretproba_A902.png/.json`. A TV-falak:
- **nyugati:** a gyári blokk, mögötte a G08 antenna és a D16/D17 dugalj;
- **déli:** a D19 dugalj a konzol vége mellett; a kapcsolóoszlop (x 7,15) szabad marad.

| Étkező | Kanapé | TV-fal | Eredmény |
|---|---|---|---|
| terv (betolt székek) | Gala U 300 × 225 | nyugati | – |
| terv (betolt székek) | Gala U 300 × 225 | deli | – |
| terv (betolt székek) | U 320 × 250 (generikus) | nyugati | – |
| terv (betolt székek) | U 320 × 250 (generikus) | deli | – |
| terv (betolt székek) | Blok sarok L 290 × 230 | nyugati | – |
| terv (betolt székek) | Blok sarok L 290 × 230 | deli | – |
| terv, 0,30 m-rel nyugatra | Gala U 300 × 225 | nyugati | **elfér** · út ≥ 0,90 · nézőtáv 3,30 · kanapé [5.32, 5.05, 7.57, 8.05] |
| terv, 0,30 m-rel nyugatra | Gala U 300 × 225 | deli | – |
| terv, 0,30 m-rel nyugatra | U 320 × 250 (generikus) | nyugati | – |
| terv, 0,30 m-rel nyugatra | U 320 × 250 (generikus) | deli | – |
| terv, 0,30 m-rel nyugatra | Blok sarok L 290 × 230 | nyugati | **elfér** · út ≥ 1,00 · nézőtáv 3,35 · kanapé [5.32, 5.15, 7.62, 8.05] |
| terv, 0,30 m-rel nyugatra | Blok sarok L 290 × 230 | deli | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | Gala U 300 × 225 | nyugati | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | Gala U 300 × 225 | deli | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | U 320 × 250 (generikus) | nyugati | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | U 320 × 250 (generikus) | deli | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | Blok sarok L 290 × 230 | nyugati | – |
| 60 cm széktolás, 0,60 m-rel nyugatra | Blok sarok L 290 × 230 | deli | – |

**Eredmények:**
- **Az étkező a terv helyén:** a 05.3-as háló ajtajához vezető 0,6 m-es szűkület miatt semmi sem felel meg. Ez az étkező miatt van, nem a kanapé miatt.
- **Az asztal 0,30 m-rel nyugatra:** a Gala U 300 × 225 és a Blok L 290 × 230 elfér a nyugati TV-fallal szemben, az üveghez tolva. A U háta ekkor közvetlenül az asztal nyugati székei mögött van, ott a székeket nem lehet hátratolni.
- **60 cm-es széktolással mindkét oldalon, minden út 0,90 m-rel:** csak egy kis, 2,0 × 2,4-es U fér el (a déli TV-fallal). Ezért kell Péter elrendezésénél a mellékutakat elfogadni, ahogy az A-811-ben és az A-812-ben is.

## Nyitott – Péter döntése kell
1. **A U nyitott oldala:** Péter rajzán kelet, az étkező felé néz; a számítás a TV (nyugat) felé nyitottal készült. Ha az étkező felé nyitjuk, a TV-t máshova kell tenni.
2. **A 05.3-as háló ajtaja és a terasz:**
   - (a) az asztal a terv helyén: a 05.3-as ajtóhoz 0,6 m, a teraszhoz 1,0 m;
   - (b) az asztal 0,30 m-rel nyugatra: a 05.3-as ajtóhoz 0,9 m, a teraszhoz 0,75 m.
3. **A U mélysége:** 2,20 m (a teraszhoz 1,0 m marad) vagy 2,40 m (0,8 m marad).
4. **Hétfőn:** a teraszajtó tolható szárnyának helye; a konyhapult benyúló végének (y 5,25) valós helye.

## Korlátok
- A geometria terv szerinti, helyszínen nem mértük. Péter rajzát a képről mértük, ±5 cm.
- A U ülőrészei (0,95 m) jelzésértékűek. A valós termék méretét Astra termékkeresése adja, ehhez a fenti befoglalók a korlát.
- A konyhapult a terv konyhabútor-rétege szerint szerepel. A pultsor y 5,25-ig benyúlik az étkezőbe.
- A lámpa- és dugaljhelyek TERV SZERINTiek (`01_alaprajzok/villamos_kiallasok/A902_villamos.json`). A nappali mennyezete hűtő-fűtő mező (HF03).

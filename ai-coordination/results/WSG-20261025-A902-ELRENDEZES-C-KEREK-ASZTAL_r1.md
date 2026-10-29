# A-902 · C alapelrendezés – kerek étkezőasztal méretpróbája (r1, Claude, 2026-10-25 05:55 CET)

- **Megbízás:** Péter 04:28 CET – a versenyzők téglalap, ovális, kerek és bővíthető asztalt is javasolhassanak; a C a jóváhagyott alapelrendezés, de nem kötelező asztalforma vagy változtathatatlan székrend; kerek asztalnál a hat szék körben; a korábban linkelt kerek Kave Home asztal (Nealy Ø150) és más, hat személyes Kave Home modell ellenőrzése; **az új variánsok külön méretpróbája, a C megfelelősége nem vihető át automatikusan kerek asztalra.**
- **Frissítés 05:10 CET:** a PR #20 r2 Blender-méretpróbája (`03_blender/geometry_v2/elrendezes_C/c_kerek*.py`, validátor PASS, függönysávval) **felülírja** ezt a 2D-próbát és ugyanerre jut: Ø150 csak sík (≤ 4 cm) TV-fallal és a kanapé legnyugatibb helyén (ML04 0,31–0,41 m oldalt), Ø130 40 cm-es TV-bútorral U-val, Ø150 40–60 cm-es szekrénnyel nem fér el. A versenyzőknek a `GEOMETRIA_C_KAMERACSOMAG_v2.md` 2. pontja a mérvadó.
- **Státusz:** `MÉRETPRÓBA (2D, felülírva a PR #20 Blender-próbával)` – ugyanazzal a motorral, szabályokkal és tűrésekkel, mint a PR #18 A/B/C változatai (`03_blender/geometry_v2/elrendezes_alt/elrendezes_alt_a902.py`; geometria `geometry_lock_A902_v2b.json`, terv szerinti; kiállások `A902_villamos.csv`; konyhapult a terv bútorrétege). **Blender-tömbkép még nincs** – a kameracsomag (Cam_03 K1 + Cam_12) validálása után készül, a lock nem változott. Nem stílusterv, nem kivitelezési terv.
- **Szkript és eredmény:** `03_blender/geometry_v2/elrendezes_alt/opt_kerek2.py`, `opt_kerek2.json`, `opt_kerek2.log` (futásidő 8 perc).

## 1. Módszer
- Kanapé: S01 Westwing Lennon L 238 × 180 (jobbos) · S02 IKEA JÄTTEBO U 285 × 160, a C szerint nyugatabbra tolva (XB keresés 6,20–7,05).
- Asztal: kerek, Ø150 / Ø140 / Ø130 / Ø120, középpont keresés x 7,60–9,20, y 5,80–6,80; **hat szék körben**, két szögállásban (30°-tól és 0°-tól 60°-onként); székméret Eamy (S01) / Ciselia (S02).
- TV-fal-bútorsáv a kanapé előtt: **40 cm** és **60 cm**.
- Kötelező méretek (PR #18 §2): fő utak ≥ 0,90 m betolt székekkel (terasz-tolóajtó, konyha, hálók folyosója, 05.3 ajtó); székkihúzás ≥ 0,90 m; kanapé–TV-bútor ≥ 0,60 m; nézőtáv ≥ 2,0 m; a hűtő előtti 60 cm szabad. Tájékoztató: ülő vendégekkel (0,60 m-es sáv) a legszűkebb út, és az ML04 függeszték távolsága az asztal közepétől.

## 2. Eredmény – a legjobb megoldás átmérőnként (ML04-távolság szerint)
| TV-sáv | Ø | S01 Lennon L | S02 JÄTTEBO U |
|---|---|---|---|
| 40 cm | **150** (Nealy) | **nincs megoldás** | 12–13 megoldás; ML04 **0,53–0,58 m** félre; ülő utak 0,65–0,80 |
| 40 cm | 140 | 5–6 megoldás; ML04 0,46–0,50; ülő szék–kanapé **0,34–0,35** | 71–77; ML04 0,24–0,26; ülő utak 0,65–1,00 |
| 40 cm | **130** | 27–42; **ML04 0,25** (0°-os szögállás); ülő szék–kanapé 0,70; ülő utak 0,65 (terasz) – 1,00 | 228–238; **ML04 0,20–0,21**; ülő utak 0,65 (05.3) – 1,00 |
| 40 cm | 120 | 136–154; ML04 **0,13–0,15**; ülő utak 0,60 (05.3) – 1,00 | 525–559; ML04 0,15–0,17; ülő utak 0,65 (05.3) – 1,00 |
| 60 cm | 150 | nincs | nincs |
| 60 cm | 140 | nincs | 2–4; ML04 0,46–0,53; ülő szék–kanapé 0,29–0,35 |
| 60 cm | 130 | nincs | 26–30; ML04 0,25 (0°) |
| 60 cm | 120 | 7–12; ML04 0,28–0,42; ülő szék–kanapé 0,32–0,65 | 115–118; ML04 0,15–0,17 |

Viszonyítás – a PR #18 téglalap/ovális C (2+2+1+1): ML04 **0,10 m**, 60 cm-es TV-szekrény **mindkét** kanapéval, ülő utak 0,70–0,85.

## 3. Következtetés (szabály a versenyzőknek)
1. **Kerek asztal megengedett**, de a C megfelelősége nem vihető át: **Ø120–Ø130 működik mindkét kanapéval** a kötelező méretekkel, **ha a TV-fal-bútor a kanapé előtt legfeljebb 40 cm mély**; az ML04 0,13–0,25 m-re kerül az asztal közepétől (a téglalap-C 0,10-e helyett).
2. **60 cm mély TV-szekrénnyel kerek asztal csak a 160 cm mély U-kanapéval** (Ø120–Ø130) működik; a 180 cm mély L-kanapéval 60 cm-es szekrény + kerek asztal **nem** fér el. Vagyis a kerek asztal az L-kanapés stílusban **a TV-fal mélységét veszi el**.
3. **Ø140 csak U-kanapéval** ajánlható (40 cm-es TV-sávval); L-lel az ülő vendég háta 0,34 m-re kerül a kanapétól – ez a 36 cm-es hiba visszatérése.
4. **Ø150 (Kave Home Nealy / Argo Ø150) a C alapelrendezésben nem ajánlott:** L-kanapéval egyáltalán nem, U-kanapéval csak 40 cm-es TV-sávval és a függesztéktől 0,53 m-re – ekkor az ML04 nem az asztal fölött lóg.
5. Hat személyre a Ø120 szűk (63 cm/fő a kerületen), a Ø130 elfogadható (68 cm/fő), a Ø140 kényelmes; a versenyző mutassa ki az ülőhely-szélességet is.
6. **Bővíthető asztal:** zárt állapotban a fenti szabályok, nyitott állapotban csak alkalmi használat – a kihúzott állapot útjait a versenyző jelezze, Claude méretpróbával ellenőrzi.

## 4. Kave Home kerek asztalok – ellenőrzés (2026-10-25)
| Modell | Méret (gyártói oldal) | Ülőhely | Ár | Elérhetőség | Megítélés a C-ben |
|---|---|---|---|---|---|
| **Nealy Ø150** ekrü lakk MDF (T0300050LL05) / dió furnér / tölgy furnér | Ø150 × 75 cm, lábmagasság 70, lap 44 mm, 103,5 kg, 2 csomag 165 × 165 × 12 – **ellenőrzött** (kavehome.com, 2026-10-25) | spec. 6 (leírás: max. 8) | 1 349 € ekrü / 1 465 € dió – kavehome.com/hu, **2026-10-24** (KOLTSEG_ELOSZURES_4STILUS); ≈ 0,52 / 0,56 M Ft ×367 +5 % | HU-szállítás és mai ár Chrome-ról ellenőrizendő | **nem ajánlott** (2. pont 4.) |
| Argo Ø150 üveg | Ø150 × 74 – forgalmazói adat (galaxus), gyártói oldal ellenőrizendő | 6 | ellenőrizendő | ellenőrizendő | mint a Nealy Ø150 |
| Argo Ø119 üveg, fekete acél | Ø119 × 76 – a PR #8 árkönyvtárban (379 €, 2026-10-24) | 4–5 kényelmes, 6 szűk | ≈ 0,15 M | ellenőrizendő | Ø120 kategória – geometriailag jó, ülőhely szűk |
| Vashti Ø120 | Ø120 × 76 – forgalmazói adat | 4–6 | ellenőrizendő | ellenőrizendő | Ø120 kategória |
| **Ø130-as Kave Home modell** | – | 6 | – | **keresendő** (Chrome, kavehome.com/hu, szűrő Ø125–135) | a méretpróba szerint a legjobb kompromisszum |

A HU-webshop árait és készletét a Claude-munkamenetből 2026-10-25 hajnalban nem lehetett lekérdezni; a Nealy méretei a gyártói termékoldalról igazoltak, az árak a repó egy napos rekordjai.

## 5. Nyitott
- Blender-tömbkép a Ø130-as változatról (S01 és S02) a kameracsomag után; a Cam_12 előterét a kerek asztal másképp tölti ki.
- Egy valós Ø125–135-ös, hat személyes Kave Home / Westwing modell cikkszámmal, árral.
- A terasz-tolóajtó keleti, tényleg tolható része helyszínen (hétfő).

# A-902 nappali–étkező – elrendezési alternatívák és új, konyhaorientált Cam_03 (r1)

- **Task ID:** WSG-20261025-A902-ELRENDEZES-ALT · **Készítette:** Claude, 2026-10-25 (CET)
- **Megbízás:** Péter 02:33 és 02:52 CET.
  - Készüljön 2–3 valóban használható elrendezési alternatíva, hat étkezőhellyel, a székkihúzás és a közlekedés valós méreteivel.
  - A 36–38 cm-es közlekedő nem elfogadható, a +15 cm önmagában kevés.
  - Kiindulópont: Lennon L és JÄTTEBO U.
  - Készüljön új, konyhaorientált Cam_03, amely érdemben különbözik a Cam_12-től.
- **Státusz:** `MÉRETPRÓBA` – nem stílusterv, nem kivitelezési terv.
  - **Geometria:** `03_blender/geometry_lock_A902_v2b.json`, terv szerinti, helyszínen nem mért.
  - **Kiállások:** `01_alaprajzok/villamos_kiallasok/A902_villamos.csv`.
  - **Konyhapult:** a terv bútorrétege (WGR1, 18. o.), mint a korábbi méretpróbában.
- **Nem engedélyez:** képgenerálást, merge-et, az alaprajzi döntés önálló módosítását. **A végleges elrendezést Péter választja.**

## 1. Miért volt 0,36–0,38 m?
- A P902_24A egy **2,40 × 3,00 m-es U-befoglaló** volt.
- A V3-tömbben a valós termékek ennek a keleti élére kerültek: a kanapé háta x 7,17-en maradt. A valódi termékek kisebbek a befoglalónál:
  - a Lennon L 1,80 m mély;
  - a JÄTTEBO U 1,60 m mély.
- Ezért a kanapé indokolatlanul közel állt az étkezőhöz.
- **Mindhárom alternatíva közös lépése:** a kanapé a termék valós mélységéhez igazítva nyugatabbra kerül.
- ~~**Feltétele:** a TV-fal bútora a kanapé előtti szakaszon (y 5,0–7,7) legfeljebb **40 cm mély** (a V3 KI3-L/BN3-L is 40 cm).~~ **Pontosítva 03:56 CET, lásd §3.1:** a számok 40 cm mély TV-bútorral készültek. A C-ben a brief 60 cm-es szekrénye is elfér mindkét kanapéval; az A-ban az L előtt legfeljebb 45 cm, a B-ben az U előtt legfeljebb 50 cm. Ez az Astra V3.1-integrációnál kötelező ellenőrzési pont.

**A második szűk pont:** a 05.3-as háló ajtajához vezető út, az étkező délkeleti széke és a hűtőoszlop sarka (x 9,95; y 5,25, D13) között. A hűtőoszlop helyét a D13 hűtődugalj rögzíti. Ezért nem lehet a hosszanti asztalt 3+3 székkel pontosan az ML04 lámpa alá tenni.

## 2. Szabályok
Forrás: a promptsablon v3.1 §1 és Péter.
- **Fő út:** legalább 0,90 m, betolt székekkel. Célok: terasz-tolóajtó, konyha, hálók folyosója, 05.3 háló ajtaja.
- **Mellékút:** 0,75 m csak az asztal terasz felőli oldalán.
- **Székkihúzás:** legalább 0,90 m az asztal élétől.
- **Kanapé–TV-bútor:** legalább 0,60 m.
- **Nézőtáv:** 2,0–3,4 m.

**Ülő vendéggel:** a szék az asztal élétől 0,60 m-es sávot foglal. Ezt tájékoztató adatként mérjük.

**Terasz:** cél a tolóajtó keleti része (Péter, 2026-10-24 18:43). Hétfőn ellenőrizendő.

## 3. Az alternatívák

**Ábrák:**
- `04_renderek/A902_elrendezes_alt_v1/A902_elrendezes_alt_v1_alaprajzok.png` – alaprajzok méretekkel;
- `…/A902_elrendezes_alt_v1_tomeg_S01.jpg` és `…_S02.jpg` – szürke tömb a Cam_12, az új Cam_03, a Cam_02 és a felülnézet szemszögéből.
- Felső sor: S01 Lennon L. Alsó sor: S02 JÄTTEBO U.
- Oszlopok: R = mostani, majd A, B, C.

**Számok:** `…/elrendezes_alt_A902_v1.json`. A paraméterek keresése: `opt_alt2.py`, `opt_b2.py`, `opt_c2.py`, `opt_c160.py`, `xb_max.py`.

| | **R – mostani** | **A – hosszanti asztal 3+3** | **B – keresztbe fordított asztal 3+3** | **C – hosszanti asztal 2+2+1+1 az ML04 alatt** |
|---|---|---|---|---|
| **Mit változtat** | – | A kanapé nyugatabbra (S01 −0,67 m, S02 −0,77 m), az asztal 0,10 m-rel nyugatabbra a P902_24A-nál | Az asztal keresztbe fordul (hossza kelet–nyugati), 3 szék északon, 3 délen | Az asztalnál 2–2 szék a hosszoldalon és 1–1 a két végén, közvetlenül az ML04 alatt; a kanapé nyugatabbra (−0,57 m) |
| **Termékcsere** | – | nincs | S02: nincs (Anouk 180). S01: 180 × 90-es asztal kell a Toni 200 helyett | S02: nincs (Anouk 180). S01: **Toni 160 × 90** a Toni 200 helyett |
| **Kötelező méretek, betolt székkel** | **NEM**: terasz 0,60–0,65, 05.3 0,75–0,80, székkihúzás 0,73 | **mind teljesül** | **mind teljesül** | **mind teljesül** |
| **Szék–kanapé** (S01 / S02) | 0,38 / 0,36 | 0,95 / 1,03 | 0,62* / 0,99 | 1,05 / 1,03 |
| **Székkihúzás, minimum** | 0,73 | 1,10 | 1,35 | 0,90 |
| **Ülő vendégekkel a legszűkebb út** (S01 / S02) | nincs terasz-út / 0,55 | 0,65 / 0,65 (05.3) | 0,75 / 0,85 | 0,75 / 0,70 |
| **ML04-lámpa az asztal közepétől** | 0,20 | **0,30 keresztben** (az asztal szélére esik) | S01 0,55 / S02 0,35 **hosszában** | **0,10** – gyakorlatilag középen |
| **Kanapé–TV-bútor / nézőtáv** (S01; S02) | 1,30 / 2,90; 1,50 / 2,90 | 0,63 / 2,23; 0,73 / 2,13 | 0,63 / 2,23; 0,68 / 2,08 | 0,73 / 2,33; 0,93 / 2,33 |
| **Költségkülönbség** | – | 0 Ft | S02: 0 Ft. S01: a 180-as asztal ára kutatandó | S02: 0 Ft. S01: **−90 010 Ft** (Toni 160: 259 990 Ft a Westwingen 2026-10-25-én, a Toni 200 rekordja 350 000 Ft, 2026-10-24) |

\* S01 B-nél a kanapé háta és az asztal nyugati vége között 0,62 m-es zsák marad. Ez nem út, a terasz felé az asztal északi oldalán lehet menni, de nem elegáns.

### Röviden
- **A – a legkisebb változás.** Nincs termékcsere, minden kötelező méret teljesül.
  - Ára: az ML04-függeszték 0,30 m-rel félre, az asztal hossztengelyére merőlegesen lóg. A Cam_12-n ez látszani fog.
  - Ülő vendégek mögött a 05.3 felé 0,65 m marad.
  - Az S01-nél a kanapé a TV-bútortól csak 0,63 m-re van.
- **B – a legjobb közlekedés U-kanapéval** (S02): ülő vendégekkel is 0,85–0,90 m.
  - A függeszték 0,35 m-rel félre esik, de az asztal hossza mentén, ez kevésbé zavaró.
  - Az asztal keresztben választja el a nappalit a konyhától.
  - **L-kanapéval (S01) gyenge:** a függeszték 0,55 m-re esik, 0,62 m-es zsák marad, és 180-as asztal kell.
- **C – a függeszték középen** (0,10 m), minden kötelező méret teljesül mindkét kanapéval. Az S01-en még olcsóbb is.
  - Ára: két szék az asztalvégeken. Az északi székkihúzás az üvegig pontosan 0,90 m.
  - Ülő vendégekkel a konyha és a 05.3 felé 0,70 m (S02, Anouk 180), illetve 0,85 és 0,80 m (S01, Toni 160).
  - S02-nél 160-as üvegasztallal ezek 0,85 és 0,80 m-re javulnának, de ehhez termékkeresés kell.

**Claude javaslata:** C.
- A függeszték az asztal fölött középen lóg, ez a hero képen is látszik.
- Mindkét kanapétípussal teljesül minden kötelező méret.
- *(Kiegészítés 03:56 CET, §3.1)* Csak a C-ben fér el mindkét kanapéval a brief szerinti 60 cm-es TV-fal-szekrény. Így Astra TV-fal-koncepcióit nem kell visszafogni.
- Ha a végeken ülés nem tetszik: A, ha nincs termékcsere; B, ha U-kanapés stílus a cél.

### Közös következmények
- **TV-fal:** ~~a kanapé előtti szakaszon legfeljebb 40 cm mély bútor. Magasabb vagy mélyebb elem csak a két szélén,~~ a megengedett mélység az alternatívától függ (§3.1). A közlekedő felé (y < 5,0) bármilyen elem csak a folyosóút ellenőrzése után kerülhet.
- **Dohányzóasztal:**
  - S01 L: a fő ülőrész előtt kb. 1,4 m szabad hely marad a TV-ig. Ebben 45–50 cm-es távolsággal elfér egy alacsony asztal.
  - S02 U: a U belseje kb. 0,95 × 0,65 m. Puff vagy tálca fér el, nagy dohányzóasztal nem.
- **Toni 200 elérhetősége:** a Westwing termékoldalán 2026-10-25-én csak a 160 × 90-es Toni látszik (259 990 Ft, 9–11 munkanap). A 200-as újraellenőrzendő; ez az A változat S01-es asztalát is érinti.
- **A Cam_12 kivágását** a választott elrendezéssel újra kell ellenőrizni (a PR #17 beolvasztásának feltétele).

### 3.1 Kiegészítés (2026-10-25 03:56 CET) – mélyebb TV-fal-bútor
**Miért:** a fenti számok 40 cm mély TV-bútorsávval készültek (x 3,67–4,07; y 4,25–7,65). Az Astra V3.1-brief (r2, §11.4) a W01-en legfeljebb 60 cm mély, mennyezetig érő zárt szekrénytestet is megenged.

**Módszer:**
- ugyanaz a motor és ugyanazok a kötelező méretek;
- a bútorsáv mélysége 40, 45, 50, 55 és 60 cm, a kanapé teljes hossza előtt (a legrosszabb eset);
- a kanapé legfeljebb 30 cm-rel keletebbre mehet, a kanapé–TV ≥ 0,60 m-hez szükséges mértékben;
- az asztal és a székek helye változatlan.

Szkript: `03_blender/geometry_v2/elrendezes_alt/tv_melyseg.py`, eredmény: `tv_melyseg.json`.

| A kanapé előtt megengedett legnagyobb TV-bútor-mélység | S01 Lennon L | S02 JÄTTEBO U |
|---|---|---|
| **A** – hosszanti 3+3 | **45 cm** (a kanapé +2 cm keletre); 50 cm-től nincs megoldás | 60 cm (a kanapé +7 cm; szék–kanapé 0,96 m) |
| **B** – keresztbe 3+3 | 60 cm, de a kanapé és a legnyugatibb székek közötti zsák 0,46 m-re szűkül (a kanapé +17 cm) | **50 cm** (a kanapé +2 cm); 55 cm-től nincs megoldás |
| **C** – 2+2+1+1 | **60 cm** (a kanapé +7 cm; szék–kanapé 0,98 m; minden út ≥ 0,90 m) | **60 cm**, változtatás nélkül (kanapé–TV 0,73 m) |

**Következmény:**
- **C-vel a brief 60 cm-es felső határa mindkét kanapéval érvényes.** Az Astra-futáson nem kell változtatni.
- **A-val az L előtt legfeljebb 45 cm, B-vel az U előtt legfeljebb 50 cm.** Ha Péter ezek egyikét választja, ezt az Astra-integrációnál kötelező feltételként kell kezelni.
- **Mindegyik változat feltétele:** maga a TV a falsíkon vagy a fülkében marad (a képernyő x ≈ 3,77; nézőtáv C-ben 2,33–2,40 m).
  - Ha a TV egy 60 cm-es szekrény elejére kerülne, a nézőtáv 2,0 m alá csökkenne.

## 4. Korlátok
- Terv szerinti geometria, helyszínen nem mért; a konyhapult a fejlesztő bútorrajza szerint.
- A székek modellje egyszerűsített:
  - betolt szék: az asztal alá 18 cm, a szék mélysége 53–55 cm;
  - ülő vendég: az asztal élétől 0,60 m.
- Az ovális Toni asztallapot téglalappal számoltam, ez a biztonság felé téved.
- Az utak szélessége 5 cm-es lépésben, körrel mért (`ut_szelesseg`, mint a korábbi méretpróbában). A „0,90” jelentése: legalább 0,90, de 0,95-nél kevesebb.

## 5. Új, konyhaorientált Cam_03 – javaslat (Péter 02:33 és 02:52)
**Vizsgálat:** öt jelölt kamera, valamint összevetésként a régi Cam_03 és a Cam_12.
- **Alap:** v2b-1-k12 v2 (PR #17), sha `66172d43…` – a futás előtt és után azonos.
- **Konyhatömb:** generikus, a terv szerinti sorokkal (alsó sor 0,90 m, hűtőoszlop és magas elemek 2,20 m).
- **Képek és log:** `04_renderek/A902_cam03_konyha_javaslat/`.

**Két mérés:**
- **Konyha a képben:** a képpontok hány százaléka esik konyhaelemre.
- **Átfedés a Cam_12-vel:** a jelölt látható falai, tömbjei és felületei közül mennyit lát a Cam_12 is. Sugárvetés 120 × 75 pontrácson; padló és mennyezet nélkül; 20 cm-es cellák.

| Kamera | Hely [x; y; z], irány, optika | Konyha a képben | Átfedés a Cam_12-vel | Megítélés |
|---|---|---|---|---|
| régi Cam_03 | [4,70; 7,70; 1,50], KDK felé, 20 mm | 5 % | **70 %** | szinte ugyanaz, mint a Cam_12 → elvetve |
| **K1 – JAVASLAT** | **[9,45; 7,55; 1,50], dél felé, a konyha tengelyében, vízszintes, 20 mm, shift_y −0,08** | **22 %** | **42 %** | A konyha a kép tárgya: a két pultsor, a hűtőoszlop és a hátsó, sütős magas elemfal. Előtérben az étkező széle és az ML04-függeszték. A teraszt és a TV-falat nem mutatja. |
| K1 18 mm | ugyanaz, 18 mm | 18 % | 45 % | több étkező, kisebb konyha |
| K2 | [8,95; 7,70; 1,50], 78°-kal délkelet felé, 20 mm | 19 % | 49 % | a 05.3 ajtó tokja a bal szélen; kevésbé tiszta |
| K3 | [7,20; 7,20; 1,50], 55°-kal délkelet felé, 22 mm | 19 % | 62 % | túl közel a Cam_12-höz → elvetve |
| **K4 – alternatíva** | **[9,50; 2,20; 1,50], a konyhából észak felé, 18 mm** | **28 %** | **18 %** | Előtérben a két pultsor, középen az étkező, a háttérben a teraszüveg és a valódi panoráma. Nagyon eltér a Cam_12-től, de inkább a konyhából kifelé mutat. A terasz a Cam_02-n már nappal szerepel. |

**Javaslat: K1 mint új Cam_03** (konyha–étkező, nappal).
- Ha a „konyhából a terasz felé” kép jobban tetszik: K4.

**A lockba csak a választás után kerül:**
- a régi Cam_03 paraméterei a `javitasok` mezőben megmaradnak;
- a 66-os regiszter Cam_03-azonosítói változatlanok.
- Ezt a Cam_12-vel együtt egy kamera-PR-ben javaslom: a választott elrendezés után a Cam_12 kivágását újraellenőrzöm, utána validátor és Render Reality Gate, merge csak Péter külön engedélyével.

## 6. Megfigyelés a tömbképekből: a Cam_12 előtere
- Mindhárom alternatívában 0,57–0,77 m-rel közelebb kerül a kanapé a hero kamerához.
- A Cam_12 előterének nagyobb részét a kanapé háta és karfája tölti ki; ez a tömbképeken jól látszik.
- **A választott elrendezéssel a Cam_12-t újra kell vizsgálni:** kissé magasabb nézőpont, kis elforgatás vagy 1–2 mm-rel hosszabb lencse. A sarok és az irány marad. Ez a kamera-PR része lesz.

## 7. Döntés (Péter)
1. Elrendezés: **A / B / C**. Claude javaslata: C.
2. Cam_03: **K1** (rá a konyhára) vagy **K4** (a konyhából a terasz felé). Claude javaslata: K1.

A választás után: a Cam_12 kivágásának újraellenőrzése, a lock frissítése (Cam_03, Cam_12), validátor, Render Reality Gate, majd egy kamera-PR. Merge csak Péter külön engedélyével.

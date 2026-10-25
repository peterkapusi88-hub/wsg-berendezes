# Helyszíni fotók és a Blender-modell (Cam_12 környezet) – Claude, 2026-10-25

**Bemenet:**
- Helyszíni fotók, 2026-10-21, 1600 × 1200 (`08_allapotfelmeres/fotok/A902/`):
  - `04_nappali/…ME-BAL-046_nappali_eloter_fele.jpg` (sha `d1f35e57…5b95b`);
  - `04_nappali/…ME-BAL-045_nappali_terasz_fele.jpg` (sha `06981c28…67715`);
  - `02_konyha/…ME-BAL-056_konyhafal_kiallasok.jpg` (sha `cb316cd7…1cc667`).
- Modell: lock v2b-1-k13 és a Cam_12 v3 KORR semleges render.

**Módszer:**
- Elemenként, minőségileg vetettem össze: van-e, hol van, milyen sorrendben, milyen a kapcsolata a szomszédos elemekkel.
- A fotók nagylátószögűek, torzítanak, és nem a Cam_12 helyéről készültek. A 046 ÉK felől délnyugatra néz, a 045 az előtér-átjáróból északkeletre, az 056 a konyha északi végéből délre.
- **A más fotóállás önmagában nem geometriai hiba**, és a Blender-kamerát nem igazítottam a fotóhoz.
- A fotó nem méretforrás. Számszerű eltérést csak mérés igazolhat (hétfő, 2026-10-26).

| Elem (lock) | Mit mutat a fotó | Modell | Értékelés |
|---|---|---|---|
| **W02** (x 5,20–7,30, y 4,05) a kapcsolóoszloppal | 046: tömör, mennyezetig érő falmező. A keleti szélén fent a termosztát, alatta 3-as kapcsoló, lent dugalj. A tömb keleti oldallapja mély (az akna). | W02 2,10 × 2,90; T01, K10–K12, D19 x 7,149-en; az Akna_WC_gepeszet a W02 mögött | **EGYEZIK** |
| **W07 / közlekedő torka** (x 3,67–5,20) | 046: a W02 és a TV-fal között nyílás, a végén szürke ajtótok, mögötte ablakos szoba | közlekedő a W02 nyugati végétől délre; a 05.2/06.1 ajtók a déli falon | **EGYEZIK** (a szélesség nem mérhető) |
| **előtér-átjáró** (x 7,30–8,35) szemöldökkel (z 2,10) | 046: az átjáró fölött alacsonyabb mennyezet vagy szemöldök, a végén a bejárati ajtó. 056: a mellvéden túl az előtér és a bejárati ajtó. | Szemoldok_atjaro_eloter_nappali; bejárati ajtó y 0,60–0,85 | **EGYEZIK** |
| **mellvéd** (x 8,35–8,45; y 2,35–4,05; ~0,85 m) | 046, 045, 056: alacsony, szabadon végződő fal a konyha nyugati oldalán, déli végén teljes magasságú pillérrel | Fal_konyha_Ny_0, Fal_szekrenyfulke_E_v2b | **EGYEZIK** (a magasság nem mért) |
| **konyha keleti fala** (K-pultfal + K-csonk, x 10,55) | 056: hosszú fal vízkiállásokkal és dugaljakkal, a déli fal dugaljakkal. 045: ugyanez a fal a kiállásokkal. | x 10,55 felület y 1,35–5,05; D02–D07, D10, D14, FL01 | **EGYEZIK** |
| **W03-a visszaugrás** (x 10,55 → 10,75 az y 5,05-nél) | 045: a falsíkban és a mennyezetvonalban függőleges törés a kapcsolók és a konyhafal között | 0,20 m-es lépcső | **EGYEZIK** (a 0,20 m nem mért) |
| **05.3 ajtó** (y 6,05–6,95) és K07–K09 | 045: sötétebb szürke tok, nyitott ajtólap; a kapcsolóoszlop közvetlenül a tok déli oldalán | Ajto_05_3; K07–K09 y 5,65 (0,40 m-re a toktól) | **EGYEZIK** |
| **akna az ajtótól északra** (x 9,80–11,10; y 7,025–8,05) | 045: az ajtótól balra (északra) kiugró falsarok két lappal, mögötte az üvegfal | Akna_etkezo_05_3 | **EGYEZIK** (a mélység nem mért) |
| TV-fal W01 (x 3,67) a G/D-aljzatokkal | 046: szemből, középen dugaljsor és kábelek | D16, D17, G08 y 6,1–6,4 | **EGYEZIK** (a Cam_12-ben nem látszik) |
| **mennyezeti csőcsonk kék kupakkal** a konyha nyugati részén, a mellvéd–pillér közelében | 046, 045 és 056: kb. Ø15 cm-es fehér cső a mennyezetből, kék kupakkal (valószínűleg páraelszívó-csatlakozás) | **a lockban, a modellben és a kiállás-listában nincs** | **MODEL SOURCE ERROR – hiányzó elem.** Becsült hely: x ≈ 8,5–8,8, y ≈ 2,4–2,7 (fotóról, nem mért). Számítás szerint a Cam_12-ből a 2,10-es átjáró-szemöldök takarja, a Cam_03-ban viszont látszhat. Hétfőn mérendő, majd a lockba felveendő (külön PR). |
| szegélyléc (~6 cm, szürke) | 046, 045, 056: minden fal alján, a mellvéden is | a modellben nincs | **modell-egyszerűsítés**, nem geometriai hiba; a promptok „6 cm matching skirting”-ot írnak |
| ajtótok színe | 045/046: középszürke–sötétszürke tok, világosszürke lap | lap 0,50, tok 0,42 albedó (a renderben 0,47 / 0,30) | megfelel (szín nem mért) |

## Eredmény
- **Fal, ajtó, közlekedő, konyha:** a vizsgált fotókon nincs olyan eltérés, amely a lock fal- vagy nyílásgeometriáját cáfolná.
- **MODEL SOURCE ERROR: 1 db** – a konyhai mennyezeti csőcsonk hiányzik a modellből. A Cam_12-re számítás szerint nincs hatása.
- **Nem ellenőrizhető fotóból** (hétfőn mérendő):
  - a mellvéd magassága;
  - a W03-a visszaugrás mélysége;
  - az akna mélysége;
  - a közlekedő szélessége;
  - a 05.3 ajtó szélessége;
  - a konyha 2,10 m-es belső szélessége, amelyen a 86 cm-es pultköz múlik.
- **A ChatGPT által kitalált elemek:** a hátsó falas konyha szigettel, a W02 áthelyezése, a 05.3 ajtó elhagyása és a kitalált közlekedőnyílás egyik fotóval sem igazolható. Ezek a képgenerálás hibái, nem a modellé.

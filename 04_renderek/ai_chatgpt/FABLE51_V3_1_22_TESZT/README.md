# FABLE51 V3.1 – ChatGPT Images koncepcióteszt (2026-10-25)

**Minden kép státusza: KONCEPCIÓ – NEM VALIDÁLT.** Egyik kép sem kivitelezhető látványterv, és egyik sem igazolja a padlót, a termékeket vagy a költséget.

- **Forrás:** `competition/fable51-v3-1-20261025` @ `b44541205cdd79e3d1f33ee8074c2bc280beb7a7`, `05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/`. A manifestben 22 COMPLETE sor szerepelt, ezt generálás előtt újraellenőriztem.
- **Eszköz:** ChatGPT Images (chatgpt.com, „Kép létrehozása” eszköz), Péter Plus-fiókja, a Claude in Chrome bővítményen át. Képenként külön beszélgetés, egyszerre egy generálás, képenként egy generálás, újragenerálás nem volt. Fizetős API-t és extra kreditet nem használtam.
- **Küldött szöveg:** `uzenetek/NN_<kep_id>.txt`. Előbb egy fejléc jön (képazonosító, `FABLE51-V3.1`, a referenciák szerepe, „pontosan EGY kép”, megőrzendő elemek), utána a Fable eredeti angol promptja **szó szerint**, a BEGIN/END jelölők között. Beküldés előtt a szerkesztőmező tartalmát a fájlhoz hasonlítottam: mind a 17 esetben teljes egyezés.
- **Referenciák:** az első kép mindig a kamera semleges Blender-alapképe. A többit kameránként a manifest `referenciak_sorrendben` oszlopa sorolja fel: padló ME-080; terasz 045/004/074/003; master üvegfal 077; konyha 056; fürdő 064/066.
  - **Eltérés:** a 18-as képnél (S02 Cam_04) a 077-es ablakfotót szándékosan kihagytam, mert a 14-es képen ez felerősítette a hibát.
- **Eredeti fájlok:** a ChatGPT eredeti PNG-i változtatás nélkül: 1586×992; 02 és 17: 1536×1024; 03: 1672×941; 16: 1448×1086. Mac-másolat: `~/Downloads/WSG_FABLE51_V3_1_RENDEREK/`.
- **Összevetés:** `_gate/<kep_id>__gate.jpg` négy mezőben: alapkép | render | 50%-os áttűnés | élkép (piros = alapkép, zöld = render). A render a 16:10-es alapképre van nyújtva, ezért a képarány-eltérésnél torzít.

## Eredmény
| | db |
|---|---|
| Elkészült (DONE) | **17 / 22** |
| BLOCKED – Cam_12 hero, Péter 07:46-os döntése: visszatartva a javított referenciáig | 5 (06, 08, 10, 12, 22) |
| FAILED | 0 |
| Geometria: PASS – feltételes | 1 (15 – S01 master Cam_11) |
| Geometria: feltételes, kisebb eltérés / tervközeli | 3 (16, 20 – fürdők; 17 – S02 konyha, Péter 08:19: elfogadva) |
| Geometria: FAIL | 13 |

A Cam_12 hero képek közül a 02 és a 04 még Péter megállítása előtt elkészült. **Mindkettő súlyos GEOMETRY FAIL.**

## Ismétlődő geometriai hibák (képazonosítóval)
1. **Cam_02, minden kép (01, 03, 05, 07, 09, 11, 21).** A kamera kb. 30–45°-kal balra fordul, és a W01 TV-falat szemből mutatja ahelyett, hogy ferdén a bal harmadban lenne. A falsarok, a padló–fal vonal és az üvegfal osztása nem fedi az alapképet. A terasz (WPC-dobogó, korlát, zöldtető, panoráma) viszont mindig felismerhető.
2. **Cam_12 (02, 04).** A konyha hátsó falas sorrá alakul, kitalált szigettel/pultvéggel. A W02 faltest, a K-csonk és a 05.3 ajtó elmozdul, és megjelenik egy kitalált folyosónyílás.
3. **Cam_04 (14, 18).** A szoba teljesen átrendeződik: az üvegfal a bal oldalra kerül, az ágy a szemközti falra, a gardrób a hátsó falra. **Forrásütközés:** a Fable Cam_04 prompt üvegfalat ír a bal szélre, az alapkép ezt nem mutatja. A 077-es fotó nélkül is ugyanez történt (18).
4. **Cam_03.** 13: a két pultsor fel van cserélve, és a jobb sor a pillér és a mellvéd zónáját tölti ki. 17: a tervhez közeli (déli fal, pillér, mellvéd, nyílás egy vonalban), de U-alakú, mert pult fordul a déli falra; Péter elfogadta (08:19).
5. **Képarány:** négy kép nem 16:10 (02, 03, 16, 17).
6. **Padló:** a képek többségén melegebb, világosabb vagy barnább a tölgy, mint a meglévő hűvös szürke Treviso. Ez nem igazolt; legközelebb a 07, 15 és 19 jár.

## Tulajdonosi kreatív visszajelzés (Péter 08:13) – fürdők (16, 20)
„Nincs üveg, igénytelen a bútor, alig van pakolófelület.” A ChatGPT itt a promptot követte. A Fable mindkét fürdőpromptja tiltja az üveg zuhanyfalat („no glass screen”), és csak minimális tárolót ad: S01-ben egy 60×45×30 cm-es szekrényt és egy polcot, S02-ben egy 40×90 cm-es faliszekrényt és egy polcot. **Ez a versenyzői terv gyengesége.** A Fable promptjait nem írtam át.

## S07 Wolke
A 21-es kép Wolke-szerű L kanapéja koncepcióteszt. A promptban szereplő 258 × 167 cm-es konfigurációt termékadat nem igazolja, a pontos méret kivitelezhetősége nem állítható.

## Érintetlen maradt
PR #23, PR #22, a közös baseline és a `main`. Merge nem történt.

## Kiegészítés 08:30 – 13 v2 újragenerálás (Péter kérésére)
`A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A__FABLE51_V3_1__v2.png`: azonos bemenet, új beszélgetés (https://chatgpt.com/c/6addae83-62ac-83eb-9243-ed4af1190dd6). A v1 megmaradt. A v2 **GEOMETRY FELTÉTELES – tervközeli**, a sorozat legjobb konyha-geometriája:
- a keleti sor a helyes oldalon van;
- a pillér, a mellvéd és a déli fal az alapkép szerinti helyen áll.

Eltérések: rövid L-visszafordulás a déli falon, és a padló melegebb a meglévőnél. Részletek a `KAPU_ERTEKELES.csv`-ben.

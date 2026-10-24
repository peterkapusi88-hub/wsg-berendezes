# A-902 – négyhelyiséges renderprompt-sablon a tízstílusos képfázishoz (v3, 2026-10-24 21:10) – KEP-004, NEM INDÍTOTT

**Kiterjeszti** a `A902_STYLE10_Cam02_prompt_sablon_v2.md`-t négy helyiségre; a v2 (Cam_02, Astra eredeti §10-promptjai + Claude kiegészítései) **változatlanul megmarad** mint a nappali-alap és történeti referencia (Péter 21:08: az eredeti Astra-promptokat és a v2 sablont nem írjuk felül). **A stílusblokkokat ebben a sablonban a V2 Medium-feladat megerősített, négyhelyiséges koncepciói töltik ki** – külön, verziózott fájlban (`A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md`); az A fázis eredeti stíluspromptjai a kiindulás, de változatlanul nem futtathatók (Péter 21:04). Használja: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004.md`. Minden kép státusza a Gate-auditig: **KONCEPCIÓ – NEM VALIDÁLT**.

## 0. Helyiségek és kamerák (lock `geometry_lock_A902_v2b.json` → v2b-1; `03_blender/geometry_v2/kamera_parameterlap_v2b.md`)

| Helyiség | Kamera | Hely [x; y; z] m | Forgatás [rad, XYZ] | Objektív | Alapkép (bútor nélkül) | Státusz |
|---|---|---|---|---|---|---|
| 1 · Nappali–terasz | **Cam_02_Nappali_terasz** | [8,30; 4,40; 1,55] | [1,479; 0; 0,858] | 20 mm, 36×24, 1600×1000 | `04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png` | kész (v2b) – **v2b-1-ből újrarender/ellenőrzés kell** (audit H7) |
| 2 · Konyha–étkező | **Cam_03_Etkezo_konyha** | [4,70; 7,70; 1,50] | [1,493; 0; −2,111] | 20 mm | `…/A902_Alap-v2b_blender_03_etkezo-konyha.png` | kész (v2b); konyhabútor nincs a lakásban – a képen IKEA METOD-váz + stílusfront, K1 (85–86 cm köz) FELTÉTELES |
| 3 · Master háló (05.1) | **Cam_04_Master** | [0,35; 4,30; 1,50] | [1,434; 0; −0,745] | 20 mm | `…/A902_Alap-v2b_blender_04_master.png` | kész (v2b-1 javítás a 05.1 fülkét érinti → újrarender kell) |
| 4 · Fürdő **06.2** (walk-in zuhany) – **javaslat** | **Cam_10_Furdo_06_2 (ÚJ, javasolt)** | [14,75; 5,45; 1,55] (DNy-i belső sarok) | [1,48; 0; −0,456] (ÉK felé, a hosszanti tengely mentén) | 20 mm (ha szűk: 18 mm, rögzítve) | **nincs** – Claude rendereli a v2b-1 .blend-ből, Péter „mehet”-jével; a lockba új kameraként kerül | **ELŐFELTÉTEL a képfázishoz**; alternatíva: 06.1 (kád 170×70, 1,75×2,65 m) – Péter dönt |

Fürdő 06.2 adatai (lock): belső befoglaló x 14,475–16,40 (1,925 m), y 5,20–8,05 (2,85 m); ajtó a nyugati falon y 6,33–7,02 (a közlekedő felől); épített walk-in zuhany 182×85; belmagasság 2,90. A kamera javaslat: az ajtó melletti DNy-i sarokból a zuhany és a mosdó felé; véglegesítés Blenderben a szaniterek tényleges helyével.

## 1. KÖZÖS FIXED BLOKK (minden helyiség, szó szerint)

> **CONCEPT ONLY – NOT VALIDATED. Do not generate before the KEP-004 gate is open for this batch.** Create a photorealistic interior image of the A-902 apartment, room "{ROOM}", style "{STYLE_NAME}", as one of four coordinated rooms of the same style, for a ten-way comparison.
>
> **Geometry and camera (image 1 is authoritative).** Use image 1 strictly for room geometry, openings and camera. Keep the exact framing, wall contours, the 2.90 m white ceiling, door and window positions and the real exterior view. Do not widen the room, do not add or move walls, columns, niches, bulkheads, coves or ceiling fixtures; the ceiling carries heating/cooling panels – nothing is attached to it except the existing light points.
>
> **Existing surfaces – must not change.** Floors in living, dining, kitchen, corridor and bedrooms: the existing Egger Grey Treviso Oak EL2184 laminate as in image 2 – medium grey-brown oak with strong grain and knots, 6 cm matching skirting; not light oak, not cool grey, not concrete. Walls and ceilings: painted white, smooth, no colour cast. Window and door frames white inside, anthracite outside in a dark brick reveal; interior doors light grey with black handles; switches, thermostat, sensors and consumer units stay visible and free. Bathroom and WC: the existing large-format light warm-grey stone-effect tiles on floor and walls, the built-in walk-in shower with linear drain, black rain head, black tap, black towel radiator and black flush plate stay exactly as built; nothing is re-tiled, demolished or moved.
>
> **Furniture and products.** Only the products and envelopes named in the style block, at their exact real dimensions and handedness; no enlarging, no shrinking to fit. Circulation: minimum 90 cm main routes (accepted 75 cm side route on the terrace side of the dining table only), 45–50 cm sofa–table, 90 cm chair pull-out, 60 cm beside beds, door swings free. Powered items only at the existing point IDs named in the style block. Laminate reads as laminate, fabric as the named fabric; real metal, glass, ceramics and stone only where a verified product says so; no faux stone, faux travertine or fake marble surfaces.
>
> **Light and grading – comparison rules.** Series A (first): neutral overcast daylight, no sun, identical exposure and white balance across all images of the batch and the calibration images; no warm grading, haze or bloom. Series B (finalists only, later): identical evening scene with the existing points lit. Luxury must come from silhouette, material depth, proportion, layering and negative space – not from warmer light, larger imaginary furniture, a wider lens or a fictional view.
>
> **Coherence rule.** The four rooms of one style share one material and colour DNA and the same signature gesture family, but each room has its own composition and at least one room-specific signature element; the bedroom and bathroom must not simply repeat the living-room colours.
>
> **Style block for this room follows. Unresolved fields are blockers, not creative freedom.**

## 2. HELYISÉG-SPECIFIKUS FIXED KIEGÉSZÍTÉS (a közös blokk után, szó szerint)

**Cam_02 · nappali–terasz:**
> Camera Cam_02: position (8.30, 4.40, 1.55), Euler (1.479, 0, 0.858), 20 mm, 1600×1000. Terrace levels: ceramic tiles −0.15 m, raised ribbed WPC deck +0.62 m, green roof, anthracite railing, real Buda hillside and city roofs. Dining table centre 0.30 m west of the plan position (P902_24A). U-shaped sofas only with the TV on the west factory block (points D16/D17, antenna G08); with a south-wall TV (point D19, console ending before the switch column at x ≈ 7.15) only L-shaped sofas. Pendant only at point ML05 (living) and ML04 (dining).

**Cam_03 · konyha–étkező:**
> Camera Cam_03: position (4.70, 7.70, 1.50), Euler (1.493, 0, −2.111), 20 mm, 1600×1000. There is no kitchen furniture in the apartment: show an IKEA METOD carcass kitchen with the style's fronts and worktop on the plan layout (two runs, 62 cm deep; the clear width between the runs is only 85–86 cm, below the 90 cm target – CONDITIONAL K1; a 45 cm shallow dry run opposite the appliance run is the fallback), the existing ~85 cm high west parapet wall kept as is (no island, no full-height wall), appliances in the budgeted line, pendant at ML04 over the dining table, worktop light only at the existing point FL01 and ceiling point ML03, no new ceiling lights. Dining table and six chairs exactly as in the living-room image of the same style.

**Cam_04 · master háló 05.1:**
> Camera Cam_04: position (0.35, 4.30, 1.50), Euler (1.434, 0, −0.745), 20 mm, 1600×1000. Room 3.57 × 5.50 m incl. the wardrobe niche; bed 180×200 with its real outer frame dimensions, at least 60 cm beside the bed, wardrobe doors and the terrace door swing free; the headboard composition must keep the existing points D20–D23 accessible; reading lights only at D20/21 and D22/23, ceiling point ML06, niche light D26; no wall drilling into the ceiling panels; the terrace glazing (3.65 m) and the white frames unchanged.

**Cam_10 · fürdő 06.2 (javasolt kamera – a lockba rögzítés után):**
> Camera Cam_10_Furdo_06_2: position (14.75, 5.45, 1.55), Euler (1.48, 0, −0.456), 20 mm (18 mm if fixed so in the lock), 1600×1000. Room 1.925 × 2.85 m, door on the west wall (y 6.33–7.02). Everything built stays: light warm-grey large-format stone-effect tiles on floor and walls, walk-in shower 182×85 with linear drain, black rain head, taps, towel radiator and flush plate, the existing basin and WC. The style may add only: one mirror composition (safety-backed, fixed to the tiled wall), light at the existing basin point, one freestanding or wall-hung storage piece in the free zone, textiles, accessories, plants; no re-tiling, no new niches, no new plumbing, no floor change.

## 3. KALIBRÁCIÓS PÁR (először; közös + helyiség-blokk + ez)

**C1 – Zenit (eredeti koncepció):** `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` Zenit-verziója az adott helyiségre: greige kárpit, füstös tölgy-hatású laminált (Egger H1180/H3710 család) padlón álló tömegek, beton-hatású laminált akcent, fekete fém, bronzos tükör, mustár/olíva akcent csak textilben; őszinte anyagok, nincs valódi kő, nincs vakolat, nincs mennyezeti munka. Ez a kreatív minimum referenciája, nem versenyző.

**C2 – Lake Forest (eredeti koncepció):** krém texturált kárpit, világos tölgy-hatású laminált tároló ívelt véggel, travertin-hatás csak egyértelműen jelzett nyomtatott/laminált panelként, pezsgőarany fém kis valódi darabokban, fehér márvány-hatás csak kis valódi asztallapon; őszinte anyagok. Ez a kreatív minimum referenciája, nem versenyző.

Kalibrációs képek az 1. ütemben: C1 és C2 **Cam_02 és Cam_04** (nappali + master) – 4 kép; a Cam_03/Cam_10 kalibráció csak akkor, ha a 2. ütem előtt Péter kéri.

## 4. STÍLUSBLOKK-SÉMA (a V2 eredménye tölti ki, stílusonként 4 blokk)

```
### Sxx — <Név> · <helyiség> (Cam_xx)
Style DNA (common to the four rooms): <1 mondat: anyag- és színvilág, gesztuscsalád>
Room composition: <2–4 mondat: tömegek, arányok, negatív tér, mi a helyiség saját szignatúra-eleme>
Products (verified records): <kanapé/asztal/ágy/front… gyártó, modell, konfiguráció/sarokirány, külső méret, szín/anyag, forrás dátummal, státusz>
Custom pieces: <méret, korpusz, front/dekorkód, él, rögzítés, hozzáférés; költségsor és sáv>
Light: <pontazonosítók (ML/FL/D), lámpatest típus, nincs új kiállás>
Avoid: <stílus-specifikus giccs és a többi stílussal való összecsúszás tiltása>
Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_Sxx_<Stílus>_<n>_<helyiség>_Cam0x_A.png (+ .prompt.txt)
```
A V2-ben Astra minden stílushoz ezt a négy blokkot angolul adja meg (`### Sxx — … · nappali–terasz (Cam_02)`, `· konyha–étkező (Cam_03)`, `· master (Cam_04)`, `· fürdő 06.2 (Cam_10)`), a differenciálási mátrix hármasaival egyezően. Claude a KEP-004 indítása előtt csak a termékrekordok, a geometriai korlátok és a pontazonosítók egyezését ellenőrzi; a kreatív szöveg Astráé.

## 5. Ütemezés és kiértékelés (kreditvédelem)

| Ütem | Képek | Feltétel |
|---|---|---|
| **1. ütem – kalibráció + próba** | C1, C2 × (Cam_02, Cam_04) = 4; **két karakteresen eltérő stílus** × 4 helyiség = 8 → **12 kép**, A sorozat | KEP-004 kapu; Péter „mehet” az 1. ütemre |
| Gate-ellenőrzés | thumbnail-sziluett (400 px), szürkeárnyalat, geometriahűség (Reality Card helyiségenként), kalibrációs összevetés | csak sikeres ellenőrzés után tovább |
| **2. ütem – fennmaradó 8 stílus** | 8 × 4 = 32 kép, **két adagban** (4–4 stílus, 16–16 kép), adagok között Gate | Péter „mehet” adagonként |
| **B sorozat (este)** | csak a döntősökre (3 × 4 = 12 kép) a döntés után | külön engedély |

Teljes A sorozat: 44 kép (4 kalibráció + 40 stílus). Sikertelen kép újragenerálása legfeljebb 1×, a promptváltozás rögzítve a `.prompt.txt`-ben. Két egyformán olvasható sziluett → vissza Astrának **sziluett-**, nem színmódosításra.

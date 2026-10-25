# A-902 – fotóval igazolt prompt-elvek (kötelező minden új kép-/videóprompthoz)

**Verzió:** v1 · 2026-10-25 · Claude.
**Forrás:**
- profi fotók: `08_allapotfelmeres/fotok_profi_20261025/A902/` (33 db; `main` @ 1d59243);
- összevetés: Mac `~/Downloads/WSG_ASTRA_V3_1_RENDEREK/qa/30_FOTO_OSSZEVETES.md`.

**Jóváhagyta:** Péter, 2026-10-25 20:30–20:34 – „a padló valahol a kettő közt legyen, 10–15%, de a legjobb a profi fotók alapján”.

**Hogyan használd:**
- Ezt a fájlt minden új promptcsomag (Astra, Claude, Gemini/Flow, MeltFlex) a GEOMETRY LOCK / RUN NOTES része előtt idézze vagy hivatkozza.
- Az Astra design-szövegét nem írjuk át. Ezek a technikai valóságrögzítő szabályok a design-brief fölött állnak, ahogy a geometriai lock is.
- A fotók bizonyítékok anyagra, színre, nyílásra és kilátásra, de méretforrásnak nem számítanak (retusáltak, EXIF nélkül). A méretet a méretezett terv és a Blender-lock adja.

---

## 1. Padló (minden lakószoba és az étkező)
- **Valóság:** hűvös, világos–középszürke tölgyhatású laminált parketta, hosszú pallókkal. Finom, egyenes erezetű, kevés és apró göcs, alacsony kontraszt. Terv szerint Egger Grey Treviso Oak EL2184; a pontos dekor nem igazolt.
- **Cél (Péter):** a profi fotók tónusa a mérvadó, legfeljebb enyhén melegebb – „a kettő közt”.
  - Mérőszám: a padló HSV-telítettsége **10–15%**. A profi fotók ~5–8%, a ME-080 ~10%, az eddigi renderek 16–60%.
  - Lab-ban: C* kb. 5–12, b* kb. 0…+8.
- **Képszerep-referencia:**
  - új referencia (image 2): **profi fotós padlókivágás**, `padlo_profi_3695.jpg` (KZS_3695 alsó sáv, lábazattal);
  - a ME-080 legfeljebb kiegészítő referencia lehet: a nagy, sötét göcse félrevisz.
- **Szerepszöveg (angol, promptba):**
  > real professional photo of the EXISTING floor in this apartment – a cool light-to-mid grey oak-effect laminate, long planks, fine straight grain, only few small knots, low contrast, matching grey-taupe skirting. This exact floor stays; under warm evening light it may look only slightly warmer (a hint of taupe), but it must never read as honey, golden, orange-brown, reddish or dark-stained oak, and never as rustic/heavily knotted oak.
- **QA:**
  - padlókivágás telítettsége 10–15% körül;
  - ha a nappali fényes képen 20% fölött van, vagy barnának hat: FLOOR_MATERIAL_DRIFT, újragenerálás.

## 2. Lábazat
- Szürkésbarna (taupe), a padlóval egyező, kb. 6 cm magas laminált lábazat. Ne legyen fehér, ne legyen sötét fa.

## 3. Falak és mennyezet
- A falak tiszta fehérek, a mennyezet sík fehér, 2,90 m magas.
- A valóságban nincs mennyezeti spot, kávás/rejtett LED vagy álmennyezet.
- Fény csak a meglévő kiállásokról és a brief által nevesített bútor-/falpanel-LED-ből jöhet.
- A brief szerinti tapéta vagy panel megengedett, de a mennyezet érintetlen marad.

## 4. Nappali–étkező teraszüvegfala (x 4,44–8,94; Cam_02 / Cam_05 / fotók 3659, 3708, 3726)
- Emelő-toló (HST) egység fehér belső kerettel, a toló szárny belső éle sötét (fekete tömítés/profil).
- A kiosztás (terv): kb. 1,79 + 1,69 + 0,99 m.
- **Belső lépcső / dobogó (fotóból becsülve, nem mért):**
  - az üvegfal előtt belül végig egy padlóburkolattal (ugyanaz a laminált dekor) borított lépcső fut;
  - **magassága kb. 15 cm (becslés 13–17 cm)**, mélysége kb. 25 cm (a falsík előtt kb. 10 cm-rel túlnyúlik);
  - x ≈ 3,67-től (Ny-i fal sarka) ≈ 9,25-ig, vagyis mindkét végén túlnyúlik a nyíláson;
  - az üveg és a keret erre a lépcsőre ül, a terasz greslapja kívül alacsonyabb;
  - Blender-jelölés: `FOTO_ELTERES_lepcso_nappali_uvegfal` (a k13 MÁSOLATON, a lock nem változott); Cam_02 alapkép: `A902_Alap-v2b1k13_blender_02_nappali-terasz_KORR_LEPCSO15_semleges.png`.
  - Promptszöveg:
    > along the full length of the living-room terrace glazing there is a continuous low interior step about 15 cm high, clad in the same grey oak-effect floor; the glass frames sit on it. Keep it; do not remove it, do not turn it into a bench.
- A bútor és a szőnyeg ne takarja el teljesen, és ne kerüljön rá.

## 5. Master 05.1 üvegfal (Cam_04 / Cam_11c / fotók 3741, 3753, 3771)
- Pontosan három fehér keretes mező: déli szélén a nyíló szárny, középső mező, a legszélesebb fix mező (terv: 0,90 + 0,90 + 1,84 m).
- A keret a padlószinten ül, **nincs lépcső**.
- Kívül: erkély világosszürke greslappal, fekete függőleges pálcás korláttal; a jobb (É) végén kívül téglaburkolatú homlokzat-visszafordulás.
- Az üveg fölött kb. 33 cm fehér falsáv van, a függönysín ide kerül.

## 6. Ajtók, szerelvények
- Beltéri ajtó: középszürke lap, sötétebb szürke tok, fekete kilincs; mérete és helye nem változik.
- Kapcsolók és dugaljak: antracit/fekete keret, a meglévő kiállásokon.
- Az előszobai/bejárati panelek a valós helyükön vannak.

## 7. Fürdő 06.2 (Cam_10 / fotó 3598, ME-064)
- Meglévő burkolat: **semleges hűvös szürke** nagylapos kőhatású csempe, finom erezettel (Geostone Grigio). Meleg fényben is szürkének kell látszania, nem bézsnek vagy krémnek. Telítettség a csempén kb. 10% alatt.
- A zuhany hátfala (bal/É) **hatszöges 3D relief** (Esagonetta). Nem négyzetrácsos mozaik, nem sima csempe.
- Fekete Grohe szerelvények: négyzetes fejzuhany karon, falsík alatti keverő, kézizuhany.
- A meglévő kis fehér fali mosdó a helyén marad (ha a brief pultot tesz alá, abba illeszkedik); lineáris folyóka a hátfal mentén.
- Ma nincs üvegfal; a brief szerinti fix üveg a meglévő padkavonalon áll.
- Ablak és kilátás nincs.

## 8. Terasz és zöldtető (Cam_02 / Cam_07; fotók 3488, 3498, 3539, 3726)
- Világosszürke nagylapos greslap.
- Magasabb WPC-dobogó lépcsőkkel; a ládák és szegélyek meleg szürkésbarna WPC-burkolatúak.
- Zöldtető évelőkkel; antracit/fekete függőleges pálcás korlát.
- A homlokzat világos–középszürke tégla.
- A fotókon látszó daruk ideiglenesek: nem kerülnek a képre.

## 9. Kilátás
- Pesti háztetők, mögöttük a budai hegyek; templomtorony is látszik.
- A városkép valós (a fotók és a 077/045/panoráma szerint). Nincs Duna, nincs Parlament, nincsenek felhőkarcolók, nincs tenger.

## 10. Ismert AI-hajlamok és előre beépítendő ellenszerek
| Kamera | Hajlam | Ellenszer |
|---|---|---|
| Cam_02 | 6–10%-kal a TV-fal felé fordul, az üvegfal keskenyebb lesz | lock-mondat: „no rotation towards the TV wall; glazing starts at 52%”; NEAR elfogadott (Péter) |
| Cam_03 | a padló–fal vonal feljebb kerül, a kép kissé közelebbi | tűrés, nem hiba |
| Cam_04 | az ágy nagyobb/közelebbi | tűrés |
| Cam_11c | az üvegfal összeszűkülhet, és kitalált fal jelenhet meg mellette | v2-blokk: „glass 32–92%, only the narrow pier 92–100%” |
| Cam_10 | a pult szélesebb, a relief fal mozaikká válik, a csempe bézs lesz | 7. pont mondatai |
| minden | meleg fényben a padló barnára, a falak bézsre csúsznak | 1–3. pont; a materials-first mondat: „light may warm the image, not change the materials” |

## 11. Folyamat
1. A promptfejlécben a képszerepek rögzítettek:
   - image 1 = Blender-alap (kötelező geometria);
   - image 2 = profi fotós padlókivágás (anyag);
   - továbbiak: helyszíni/profi fotók (csak anyag és kilátás) és termékfotó (csak identitás).
2. A kész képet kapuképpel (Blender-vetítés) és padlótelítettség-méréssel ellenőrizzük. Státusz: KONCEPCIÓ – NEM VALIDÁLT, amíg nincs tételes ár és ajánlat.
3. Fotókamerás (Cam_F_<KZS>) munkánál a maszkon kívül semmi nem változhat (lásd `FOTOKAMERA_LATVANYTERV.md`).

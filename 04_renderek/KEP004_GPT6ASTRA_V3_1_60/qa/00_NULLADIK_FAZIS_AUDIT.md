# A-902 · GPT-6 Astra V3.1 · 0. fázis – hatkamerás előellenőrzés (képgenerálás nélkül)

Claude, 2026-10-25 ~17:30 (Budapest). Státusz: **KONCEPCIÓ – NEM VALIDÁLT**. Képet ebben a fázisban nem generáltam.

## 1. Forrásellenőrzés (7.1)
- Astra-ág `competition/gpt6astra-v3-1-20261025` távoli SHA = **2bef09ae6081b5bafb86bc876ef8410be44bb567** (egyezik a rögzítettel).
- Fable-renderág `renders/fable51-v3-1-22-tests` = e511439…, integrátorág `integrator/cam12-v3-korrekcio-20261025` = f5977fc… (mindkettő egyezik).
- Manifest: 66 sor = 60 COMPLETE (01–60) + 6 KOZOS (61–66, kihagyva). Mind a 60 promptfájl létezik, a név = IMAGE_ID, saját BEGIN/END jelölő, a karakterszám egyezik (±1 a záró sortörés). 10 stílus × 6 kamera (Cam_02/03/04/10/11/12) – PASS.
- `renders/gpt6astra-v3-1-60-tests` ág **még nem létezik**; a munkamenetnek csak olvasási GitHub-hozzáférése van (push-jogot a rendszer megtagadta) → a mentés egyelőre csak a Macen.
- Hat helyszíni fotó + a terasz-panoráma v0/v0b a repóban megvan, SHA naplózva. A Cam_11 a 077-es master fotót kapja, NEM a tetőterasz-panorámát; a Cam_02 a terasz-panorámát kapja.

## 2. Kamerakép-ellenőrzés (7.2) – mind a hat alapot megnyitottam
A vetítést a lock (v2b-1-k13, `cameras`) paramétereiből saját szkripttel számoltam; a Cam_02 KORR naplójában szereplő Blender-vetítéssel pixelre egyezik (760,3 / 648,6 px).

| Kamera | Használt image 1 | Forrás / SHA256 (rövid) | Azonosság igazolása | Olvashatóság |
|---|---|---|---|---|
| Cam_02 | `A902_Alap-v2b1k13_blender_02_nappali-terasz_KORR_semleges.png` | Mac `~/Downloads/WSG_CAM02_KORREKCIO/vegleges/` · 75ec3c85… (Claude-integrátor, 2026-10-25 13:42; blend-másolat sha e01170d3… = k13; validátor üres PASS 0/0) | élkép-távolság a hivatalos `A902_alap_v2b1/…_02_nappali-terasz.png`-hez (cb60ec8e…): medián **0 px**; kamera loc/rot/lens = lock | jobb (W01 és északi fal tónusa elválik) |
| Cam_12 | `A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png` | integrátorág f5977fc · 8ffd40c0… | PNG-metaadat kamera `Cam_12_Nappali_Hero`; élkép-távolság az eredeti v3-hoz (66a9c6af…) medián 2 px, 80% ≤ 5 px (csak árnyékél); integrátori jelentés: kamera- és geometriaváltozás nincs | jó |
| Cam_03 K1 | `A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_KORR_semleges.png` | integrátorág f5977fc · 92f9ebed… | metaadat `Cam_03_Etkezo_konyha`, ugyanaz a k13 blend-másolat; élkép-távolság az eredeti K1-hez (5ba6c359…) medián 2 px, 80% ≤ 6 px | jó (a BiBo-tömbrendert NEM használom) |
| Cam_04 | `A902_Alap-v2b1_blender_04_master.png` (hivatalos) | ee9cdf86… | metaadat `Cam_04_Master`, k10 blend; lock-paraméter egyezik | **gyenge** (fehér-a-fehéren) – javított változat nincs → kockázat |
| Cam_11 | `A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png` | 66fa4efb… | metaadat `Cam_11_Master_Panorama`; 3 üvegmező a vetítés szerint 21–35 / 35–50 / 50–79 % | jó |
| Cam_10 | `A902_Alap-v2b1_blender_10_furdo-06-2.png` | 25c818fd… | metaadat `Cam_10_Furdo_06_2`; akna, mosdó, padka a vetítéssel egyezik | jó |

## 3. Prompt–Blender konfliktusok (7.3) és a futtatási megoldás
| Kamera | Konfliktus az Astra S01 promptban | Kezelés a futtatási bevezetőben (a prompt szó szerint marad) | Állapot |
|---|---|---|---|
| Cam_02 | „The television wall is the visual protagonist” → a Fable-nél ez okozta a szembe fordulást; a WALL CONTINUITY bekezdés W02/W03/W07/05.3 ajtót ír, ezek nem látszanak; a Somar (ML04) a vetítés szerint képen kívül (x 146 %, y −91 %) | W01 ferde, 0–47 %; sarok 47–48 %; üveg 52 %-tól, osztó ~70 %; ML05 44 % a felső szélen; étkező csak a jobb alsó sarokban (86 %/85 %-tól); W02-csoport és Somar kifejezetten tiltva | READY |
| Cam_12 | nincs érdemi; a konyhaelrendezés Astránál csak elvi | fix elemek balról jobbra (integrátori vetítés, újraszámolva); hűtőoszlop a W03-a előtt (D13), fő sor a keleti falon felsőkkel, alacsony sor a mellvédnél, sziget tilos | READY |
| Cam_03 | a FURNITURE/PLAN bekezdés kanapét, szőnyeget is felsorol (nem látszik); a főzőlap/mosogató oldala Astránál nincs megadva | sorok a villamos terv szerint: keleti fali sor mosogatóval + felsőkkel (D04 mosogatógép), nyugati alacsony sor a mellvédnél főzőlappal (X01), déli magas fal, D13 hűtőoszlop bal elöl; W02 csak 84–100 % | READY (a főzőlap-oldal integrátori értelmezés, Astra-megerősítés kell) |
| Cam_04 | a déli gardrób „actual visibility at the edge” – a vetítés szerint **egyáltalán nem látszik**; a függönysín az üvegfal fölött – az üvegfal a kamera mögött van (−11 %) → a Fable-nél pont ebből lett kitalált bal oldali üvegfal | „NINCS ablak, üveg, erkély, ajtó a képen”; északi gardrób 0–43 %; pillér 43–46 %; sarok 48 %; ágy fejvége a keleti falon 54–78 %; ágytengely y 6,40 (Péter 2026-10-25 00:05, k11b – a lockba még nincs beolvasztva) | READY, de magas kockázat (gyenge alap) |
| Cam_11 | nincs | üvegmezők %-ban, fejvég mögötte, 077-es fotó a valós kilátáshoz | READY |
| Cam_10 | a közös REALITY bekezdés „grey-oak floor és actual external view”-t ír – fürdőben téves | futtatási megjegyzés: padló = meglévő Geostone, nincs ablak/kilátás; üveg a padkavonalon a távoli faltól (38 %) a kamera felé; mosdóbútor 38–68 %, mosdó a helyén (50 %) | READY |

BLOCKED kamera nincs. A Fable/Opus kreatív tartalmát nem vettem át; a Fable-től csak a bevált módszer (fix elemek balról jobbra, képszerepek) jött.

## 4. Csatolmányok (sorrend = image-szám)
- Cam_02: Cam_02 KORR · ME-BAL-080 parketta · ME-BAL-045 · terasz-panoráma v0
- Cam_12: Cam_12 v3 KORR · 080 · 046 · Somar L00148FA05 termékfotó-kivágás (Astra saját 60_TERMEK_BIZONYITEKOK képéből)
- Cam_03: Cam_03 K1 KORR · 080 · 056 · Somar-kivágás
- Cam_04: Cam_04 · 080 (igazolt master-fotó a fejvégfalról nincs; a 077-et szándékosan nem csatolom)
- Cam_11: Cam_11 · 080 · 077
- Cam_10: Cam_10 · 064 (a 066-ot nem: WC-t húzhatna a képbe)

Teljes SHA-lista: `attachments_log/pilot_S01_csatolmanyok.json`. A küldendő üzenetek: `prompts_sent/0N_<IMAGE_ID>__ASTRA_V3_1__v1.txt`.

## 5. Ismert, feltételes pontok (nem a kép tárgya, de naplózva)
- Hűtőoszlop a W03-a előtt takarja a K07–K09 kapcsolókat és szűkíti a 05.3 ajtóhoz vezető utat (integrátori jelzés, Fable-nél is) – Astra-terv FELTÉTELES.
- Somar: Ø76 vs Ø75 variáns-ellentmondás; Hue-izzó beférése nem igazolt.
- A Lennon L kanapé (238 × 180) a CLAUDE.md „min. L, inkább U” szabályának megfelel; az elfogadott P902_24A U-méretpróbától eltér – Péter döntése.
- Fürdő: üvegméret, mosdóbeépítés (Smyle gyári jóváhagyás), nedves zónás Hue-táp – szakági ellenőrzés kell.

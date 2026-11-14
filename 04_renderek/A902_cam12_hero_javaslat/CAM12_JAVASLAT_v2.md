# A-902 · Cam_12_Nappali_Hero – sarokból, átlósan (JAVASLAT v2, 2026-10-25)

**Kérés:**
- Péter 01:39: második, látványközpontú nappali főnézet.
- 01:58: sarokból, átlósan, a TV-fal felőli sarok közeléből; nem extrém nagylátószög; 2–3 valós állás vizsgálata.
- 02:06: az ÉNy-i sarok a fő jelölt, a DNy-i sarokkal össze kell vetni; a Cam_02 külön, változatlan kontrollnézet marad.

**Állapot:** a kamera a v2b-1-k12 fájlban és a lockban van (draft PR). A main-be csak Péter „mehet”-je után kerül. Képgenerálás ehhez a nézethez nem indult.

## A választott állás
| Paraméter | Érték |
|---|---|
| Hely | [3,95; 7,90; 1,45] – az ÉNy-i sarokban, a TV-faltól (x 3,67) 0,28 m-re, az északi falsíktól (y 8,05) 0,15 m-re, szemmagasságban |
| Irány | délkelet (θ = −45°), vízszintes kamera: Euler [π/2; 0; −3π/4] → a függőlegesek egyenesek |
| Optika | **22 mm** (vízszintes látószög 78,6°). Nem extrém nagylátószög; a Cam_02/03/04 20 mm-es. |
| Kivágás | shift_y −0,08: kevesebb mennyezet, több bútor; 1600 × 1000 |
| Alapkép | `A902_Alap-v2b1k12_blender_12_nappali-hero_JAVASLAT.png` (az 1. képi alap ehhez a nézethez) |
| Tömbképek | `A902_Cam12_tomeg_S01_V3_v2.png`, `…_S02_V3_v2.png`, `…_P902_24A_generikus_v2.png` |

**Mit mutat** (balról jobbra, képtéri u-érték: 0 = bal, 1 = jobb szél):

| Elem | u | Megjegyzés |
|---|---|---|
| 05.3 szürke ajtó (W03) | 0,05–0,15 | teljes ajtólap, szemöldökkel |
| W03 keleti fal, y 5,05–6,05 | 0,15–0,25 | K07–K09 kapcsoló és D12 dugalj (y 5,65), D13 hűtődugalj (lent, az asztal takarja) |
| Étkezőasztal + 6 szék | 0,03–0,40 | a kanapé mögött; az **ML04 függesztékpont látszik** (0,21; 0,05) |
| Konyhacsonk + konyha pultfala (x 10,55) | 0,26–0,50 | a pultfal (D02–D07, FL01) – itt a konyhabútor lesz a látványelem |
| Előtér-átjáró | ≈0,50 | élben |
| **W02 déli tömör fal** (x 5,20–7,30) | 0,54–0,81 | teljes felület, szemben; a kapcsolóoszlop (K10–K12, T01, S01, D19) a bal szélén, u 0,56 |
| **Hálószobai közlekedő torka** | 0,82–0,99 | x 5,20 visszafordulás (K25–K27 + D46, y 3,90), pillér, a közlekedő déli fala a 06.1 ajtó tokjáig |
| Kanapé eleje | 0–0,69 (előtér) | S01: az L ülései és a chaise; S02: a U belseje |

**Nem látszik:** a TV-fal (a kamera mögött jobbra), az üvegfal és a terasz, az ML05.

## Vizsgált állások
Bizonyítékok: `jeloltek/`. Mérések (ray cast, vetítés): `03_blender/geometry_v2/cam12/cam12v2_jeloltek_log.json` és `cam12v2_ellenorzes_log.json`.

| Jelölt | Hely, irány, optika | Pro | Kontra | Döntés |
|---|---|---|---|---|
| **K1 – ÉNy-i sarok** | [3,95; 7,90; 1,45], θ −45…−47°, 20/22/24 mm | Péter minden kért eleme látszik: kanapé eleje, étkező, konyha pultfala, W03 + 05.3 ajtó, jobbra a W02 és a közlekedő torka | A W02 nagy, sík fala uralja a kép jobb közepét → erős falkezelés kell. A terasz nem látszik. | **választott**, finomítva: 22 mm, shift −0,08 |
| K2 – ÉNy, 0,6 m-rel beljebb | [4,50; 7,65; 1,45], θ −52°, 20 mm | közelebbi, intimebb kanapé | az ajtó 05.3 a bal szélre szorul (u 0,01), a kanapé túl nagy az előtérben | elvetve |
| K3 – DNy-i sarok | [4,25; 4,35; 1,45], θ +30°, 20 mm | panoráma és terasz balra, a W03 és az akna szemből, a kanapé U-belseje | nincs konyha (csak a csonk) és nincs összekötő fal (a kamera mögött van); a U déli karjának háta van előtérben | elvetve – de **ez a legszebb „panorámás” átló**, ha később kell |
| H1 – tengelyes (01:39) | [4,25; 6,35; 1,50], kelet felé, 20 mm | szimmetrikus | Péter 01:58-kor sarokállást kért helyette | elvetve, dokumentálva (`jeloltek/cam12v1_…`) |
| Finomítás R1 / R2 / R3 | 20 mm θ −46° / **22 mm θ −45°** / 22 mm 1,35 m | R2: kevesebb mennyezet, természetesebb perspektíva, az ajtó és a közlekedő torka is benne | R1 tágabb, torzabb; R3-ban a kanapéhát többet takar az étkezőből | **R2** |

## Fontos a döntéshez
- **Átfedés a Cam_03-mal** (konyha–étkező, [4,70; 7,70], θ −31°, 20 mm). A két kamera ugyanabból a sarokból néz, 14°-kal elforgatva. Közös tartalmuk: az étkező, a konyha, a 05.3 ajtó és a W02.
  - A Cam_12 a kanapé–W02–közlekedő tengelyt, a Cam_03 az étkező–konyha–akna tengelyt hangsúlyozza.
  - **Javaslat (Péter dönt):** maradjon mindkettő. Vagy a 66 képes sorozat előtt a Cam_03-at irányítsuk át a konyhára, például az étkező északi végéből dél felé. Ez a v1-csomag két Cam_03 promptját érintené.
- **A kamera helye:** a sarokba (x < 4,40; y > 7,70) ne kerüljön magas szekrény. Ha mégis kerül, a kamera ~0,3 m-rel beljebb megy.
- **Rejtett LED (V3.1):** a nézetben a W02, a W03, a konyha pultfala és a közlekedő torka látszik. Ezek tápellátását és a kiállásokat lásd `ai-coordination/requests/WSG-20261025-ASTRA-V3_1_INPUT_Cam12_falak_vilagitas.md`.

## Ellenőrzés
- Validátor v2, lock v2b-1-k12 v2 (sha256 `54796a6e…2f46`), blend sha256 `66172d43…c9d3`:
  - üres: PASS 0/0, 12 kamera teljes paraméterrel;
  - S01 és S02 V3 tömb: PASS 0 hiba / 8 figyelmeztetés;
  - referencia: FAIL 6/3 (a régi szaniterhibák, nem e PR tárgya).
- Riport: `03_blender/validator_report_2026-10-25_v2b1k12_cam12.md`.

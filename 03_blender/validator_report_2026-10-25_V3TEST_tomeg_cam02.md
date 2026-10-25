# Validator-riport: A-902 v2b-1-k11b – Cam_02 V3TEST-tömbök (S01 Kyoto Ink, S02 BiBo Nocturne), 2026-10-25

**Feladat:**
- Péter 01:55-kor kérte, hogy a V3 TV-szekrényeinek és magas tárolóinak eltérő méreteit a tömbképen és a promptban ellenőrizzem.
- 02:22-kor a két javított tömbképet és a PASS validátort jelölte meg kiindulásnak.
- A tömbök csak a V3_TEST 1b képéhez készültek. A modellt nem módosítják.

## Eredmény

Validator v2 (`geometry_validator_v2.py`, `b7d7f6a6…`), lock v2b-1-k11b (`7aa85d70…154b`), `A902_villamos.json` (`f881dcce…`, 130 terv szerinti kiállás).

| Mód | Eredmény | Figyelmeztetések |
|---|---|---|
| üres (a tömbök nélkül) | **PASS 0/0** | – |
| S01 tömbök (`Stil_TOMEG_S01_V3TEST`) | **PASS 0/8** | **A KI3-L előtt:** D16, D17, G01–G04 és G08. A V3 kivehető, szellőző szervizhátfalat ír elő.<br>**A KI3-V előtt:** D18. A legalsó rekesz hátfalán át érhető el |
| S02 tömbök (`Stil_TOMEG_S02_V3TEST`) | **PASS 0/9** | **A BN3-L előtt:** D16, D17, G01–G04, G08 (szervizhátfal).<br>**D18:** a BN3-V ajtós oszlopa és szervizlapja is a 0,3 m-es sávba esik. Az elérés a tükör alatti zárt szervizlap mögül történik (y 4,70 ≤ 4,749 ≤ 5,15; z 0,30 < 0,40) |

**Minden módban:**
- LOCK: 61 fal, 54 nyílás, 17 padló – 0 eltérés.
- Terasz: 43 elem – 0 változás. 11 kamera – a paraméterek egyeznek.
- Ütközés bútor és fal/nyílászáró között: 0. Bútor–bútor átfedés: 0. Ajtólendület: 11 nyílás – 0 ütközés.
- Takart kapcsoló: 0. Az ML04 alatt az étkezőasztal áll – ez terv szerinti.

## Mérések (`geometry_v2/tomeg_cam02_v3test/tomeg_cam02_V3TEST_log_v1.json`)

| | S01 | S02 |
|---|---|---|
| Az alsó szekrény eleje és a kanapé nyugati vége | 1,30 m | 1,50 m |
| Ajtólendület (x) | KI3-V 60 cm → 4,57; KI3-L 60 cm → 4,67 | BN3-V 45 cm → 4,44; BN3-L 60 cm → 4,67 |
| A magas és az alsó szekrény közti rés | 0,20 m | 0,10 m |
| A magas szekrény és a DNy-i átjáró síkja | 0,30 m | 0,20 m |
| FL02 és a TV-háttér (vízszintesen / függőlegesen) | 0,199 / 0,40 m | 0,199 / 0,40 m |
| TV-tengely / kanapétengely | y 6,35 / 6,40 | y 6,35 / 6,40 |
| Nézőtáv (TV – az ülés közepe) | 2,93 m | 2,93 m |
| A kanapé északi vége és az üveg | 0,46 m | **0,225 m** |
| Kanapéhát – nyugati széktámla | **0,38 m** | **0,36 m** |

**Nyitott (Péter dönt):**
- **Kanapé–szék távolság, 0,36–0,38 m:**
  - ez a P902_24A elfogadott tűrése;
  - kihúzott széknek kevés;
  - ha az étkező 0,15 m-rel keletre kerül, 0,51–0,53 m lesz.
- **S02 – a U északi vége 0,225 m-re van az üvegtől:** a teraszra a nyugati sávon és az asztal északi végénél lehet kijutni. A függöny és a V3.1 függönyfénye itt szűk helyre kerülne.

## Futtatás
- Szkript: `geometry_v2/tomeg_cam02_v3test/01_tomeg_cam02_v3test.py` + `tomeg_lib.py`; indító: `futtat.sh`; napló: `01_tomeg_v3test.log`.
- A szkript a .blend másolatán fut, háttérben, mentés nélkül. Előtte és utána ellenőriztem a sha-t (`futtat_sha_elotte.txt`, `futtat_sha_utana.txt`): `9875cd57…`, változatlan.
- Az élő Blender-jelenethez és a Macen megnyitott fájlhoz nem nyúlt.
- A validátor JSON-kimenetei: `validator_v2b1k11b_V3TEST_{ures,tomeg_S01,tomeg_S02}.json`.

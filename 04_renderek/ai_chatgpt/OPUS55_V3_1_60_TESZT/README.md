# OPUS55 V3.1 – ChatGPT Images koncepcióteszt, 60 sor (2026-10-25)

**Minden kép státusza: KONCEPCIÓ – NEM VALIDÁLT.** Egyik kép sem kivitelezhető látványterv, és egyik sem igazolja a padlót, a termékeket vagy a költséget. Az auditban nyitott tételek (K-02 S03–S10, K-03 S04, K-04, K-05, K-06, K-08 … K-19) képenként a `GENERALASI_NAPLO.csv` `nyitott_audit_tetelek` oszlopában.

## Eredmény
| Státusz | db |
|---|---|
| DONE | **52** |
| FAILED | 0 (egy technikai hiba volt – 18-as –, egy újrapróbával DONE) |
| BLOCKED | **8** (a Cam_02 sorai: 13, 19, 25, 31, 37, 43, 49, 55) |
| SKIPPED_LIMIT | 0 |
| **Összesen** | **60** |

Futás: 08:57–10:17, egy ChatGPT-fiók (Plus), Claude in Chrome, saját lap. Képenként új beszélgetés, egy kép. A Fable-lapokat és -beszélgetéseket nem érintettem.

## Kameránként (geometria a Blender-alapra vetítve, `_gate/`)
| Kamera | Eredmény | Jellemző hiba |
|---|---|---|
| Cam_10 fürdő | 10/10 **PASS** (feltételes) | a beépített elemek pontosan fednek; a mosdó néha 3–5 %-kal lejjebb, a kézizuhany 3 képen hiányzik |
| Cam_11 master panoráma | 8 PASS, 1 feltételes (35), 1 FAIL (17) | a padló–fal vonal ~5 %-kal magasabban; a 17-esen a kamera 10–15°-kal jobbra fordult |
| Cam_03 konyha K1 | 10/10 feltételes – tervközeli | a sorok mindig a helyes oldalon (a Fable-féle csere nem jött elő); a kamera közelebbi/szűkebb; 27, 39: íves végelem a mellvéd elé nyúlik |
| Cam_12 hero v3 | 10/10 feltételes – tervközeli | a térváz mindig felismerhető, sziget nincs; a kamera rendszeresen hátrébb/balra (W02 bal éle ~45 % az 55 % helyett) |
| Cam_04 master | 10/10 feltételes – közepes | a Fable-féle kitalált üvegfal egyszer sem jött elő, az ágy mindig a jobb oldali fejvégfalon; a bal falszakasz/fülke átrendeződik (a gardrób szemből látszik) |
| Cam_02 nappali–terasz | 2/2 **GEOMETRY_FAIL**, 8 BLOCKED | a kamera a TV-fal felé fordul; a 045/004/003 fotókkal (07) enyhébb, az üveg és a terasz stimmel, de a TV-fal még mindig szemből |

**Legjobban tartó kamerák:** Cam_10 > Cam_11 > Cam_03 > Cam_12 > Cam_04 >> Cam_02.

## Stílusonként
Minden stílusból 5 kép készült (S01, S02: 6 – ezeknél a Cam_02 is lefutott, FAIL). Minden stílusnál Cam_10 és (a 17-es és 35-ös kivételével) Cam_11 PASS; Cam_12/03/04 feltételes.

## Módszer
- **Források:** `competition/opus55-v3-1-20261025` @ `7d3c67f823c646d9daef06b294826e89c1c61467` (56 prompt) és `integrator/opus55-v3-1-audit-20261025` @ `94f80688dff460dd1c726e3bca2338d603f047c6` (S01/S02 Cam_02 + Cam_12 v1.2; sha256 a patch-README szerint egyezik). A manifest 61–66. sorát nem generáltam.
- **Üzenet** (`uzenetek/NN_<kep_id>.txt`): fejléc (azonosító, csatolmányszerepek, kameránkénti GEOMETRY LOCK %-os elemsorrenddel, „pontosan EGY kép”), utána az Opus-prompt **szó szerint**, BEGIN/END jelölőkkel. Beküldés előtt a szerkesztő tartalmát és a csatolmány-sorrendet minden képnél szkript ellenőrizte (52/52 + 1 újrapróba egyezés).
- **Csatolmányok** (mindig az 1. a Blender-alap):
  - Cam_02 `A902_alap_v2b1/…02_nappali-terasz.png`; Cam_03 `A902_kameracsomag_C/…03_konyha-etkezo_K1_JAVASLAT.png`; Cam_04 `A902_alap_v2b1/…04_master.png`; Cam_11 `A902_cam11_javaslat_v1/…11_master-panorama_JAVASLAT.png`; Cam_10 `A902_alap_v2b1/…10_furdo-06-2.png`.
  - **Cam_12:** `A902_cam12_v3_korrekcio/…v3_KORR_semleges.png` (@09c2762, sha `8ffd40c0…`). Ugyanaz a v3 kamera, mint a `JAVASLAT_v3` (sha `66a9c6af…`), csak megvilágítva; a brief engedi a bizonyítottan azonos, jobban megvilágított alapot.
  - 2. kép: ME-BAL-080 padlófotó (fürdőnél ME-BAL-064).
  - 3+. helyszíni fotók csak anyag/környezet szereppel: Cam_02: 045, 004, 003; Cam_12: 046; Cam_03: 056; Cam_11: 077; Cam_10: 066; Cam_04: nincs fotó. **Kivétel:** a 01-es kép csak 1+2 csatolmánnyal ment, a többi fotót Péter 08:57-es kérdése után adtam hozzá.
- **Letöltés:** az eredeti PNG (1586 × 992) változatlanul, JS-blob → `~/Downloads` → `~/Downloads/WSG_OPUS55_V3_1_RENDEREK/`; méret és sha256 a naplóban.

## Újragenerálandó / javítandó
1. **Cam_02, mind a 10** – előbb olvasható, megvilágított Cam_02 semleges alap kell (a Cam_12 v3 KORR mintájára, Blender + validátor). Utána a 8 BLOCKED sor és a 01/07 újra.
2. **17** (S03 Cam_11) – kamerafordulás.
3. **14, 20** – olajfa a W02 előtt (K-03; az S03-ban is előjön, nem csak az S04-ben).
4. Opcionális: **27** (S05 konyha, íves végelem a mellvéd előtt), **50** (kitalált ablak az előszobában?), **52** (kitalált komód).
5. **Fürdők (mind):** gyenge pakolófelület – ez az Opus-promptok hibája, nem a generálásé (Péter Fable-kritikája itt is áll).

## Folytatás
`plan.json` + `uzenetek/` + `GENERALASI_NAPLO.csv`: a BLOCKED sorok (13, 19, 25, 31, 37, 43, 49, 55) újraindíthatók; a kész képeket nem írom felül (új verzió: `__v2`).

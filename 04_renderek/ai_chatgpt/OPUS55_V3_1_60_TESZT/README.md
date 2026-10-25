# OPUS55 V3.1 – ChatGPT Images koncepcióteszt, 60 sor (2026-10-25)

**Minden kép státusza: KONCEPCIÓ – NEM VALIDÁLT.** Egyik kép sem kivitelezhető látványterv, és egyik sem igazolja a padlót, a termékeket vagy a költséget. Az auditban nyitott tételek (K-02 … K-19) képenként a `GENERALASI_NAPLO.csv` `nyitott_audit_tetelek` oszlopában.

## Eredmény (a javítókör után)
| Státusz | db |
|---|---|
| DONE | **60** |
| FAILED | 0 (egy technikai hiba volt – 18-as –, egy újrapróbával DONE) |
| BLOCKED | 0 (az első körben 8 Cam_02-sor volt BLOCKED, a javítókörben elkészültek) |
| SKIPPED_LIMIT | 0 |
| **Összesen** | **60 sor, 69 PNG** (60 × v1 + 9 × v2; a v1-eket nem írtam felül) |

- 1. kör: 08:57–10:17, 52 DONE + 8 BLOCKED.
- Javítókör: 14:53–15:14 (Péter: „oldd meg az összes rosszat”). 17 generálás: 8 BLOCKED Cam_02-sor v1-ként, 9 v2 (01, 07, 13, 14, 17, 20, 27, 50, 52). Napló: `GENERALASI_NAPLO_v2.csv`, üzenetek: `uzenetek_v2/`, terv: `plan_v2.json`.
- Egy ChatGPT-fiók (Plus), Claude in Chrome, saját lap, képenként új beszélgetés, egy kép. A Fable-lapokat és -beszélgetéseket nem érintettem.

## Kameránként (a legfrissebb változat geometriája, Blender-alapra vetítve, `_gate/`)
| Kamera | Eredmény | Jellemző eltérés |
|---|---|---|
| Cam_10 fürdő | 10/10 **PASS** (feltételes) | a beépített elemek pontosan fednek; a mosdó néha 3–5 %-kal lejjebb, a kézizuhany 3 képen hiányzik |
| Cam_11 master panoráma | 8 PASS, 2 feltételes (35; 17 v2) | a 17-es v2-n a kamera már nem fordul el, de az üvegfal jobb szakasza keskenyebb, és kitalált téglapillér jelenik meg |
| Cam_03 konyha K1 | 10/10 feltételes – tervközeli | a sorok a helyes oldalon vannak. **27 v2: az íves végelem továbbra is a mellvéd elé nyúlik**, a lock-sor nem hatott. 39 ugyanilyen. |
| Cam_12 hero v3 | 10/10 feltételes – tervközeli | 14/20/50 v2: a W02 élei (~45 % / ~87 %) a lockkal egyeznek, a W02 előtt nincs fa, és az 50-esen nincs kitalált ablak. A többi v1-en a kamera hátrébb/balra áll. |
| Cam_04 master | 10/10 feltételes – közepes | az ágy mindig a jobb oldali fejvégfalon van; a bal fal/gardrób szemből látszik. 52 v2: a kitalált komód eltűnt. |
| Cam_02 nappali–terasz | 7 feltételes – közepes, 3 feltételes – gyenge, **0 FAIL** | az üvegfal, osztó, terasz, dobogó és korlát mindig a helyén van. A kamera hátrébb áll, a belső sarok ~53–55 %-nál van a ~47 % helyett, a W01 rövidülése laposabb. **Gyenge** (31, 43, 07 v2): a TV-fal majdnem szemből látszik. |

**Legjobban tartó kamerák:** Cam_10 > Cam_11 > Cam_12 (v2 csomaggal) ≈ Cam_03 > Cam_04 > Cam_02.

## A javítókör módszere
1. **Cam_02 – új, megvilágított semleges alap.** Lásd `_cam02_korrekcio/`.
   - A `v2b1k13` blend **másolatából** készült, a lock szerinti kamerával: [8.3, 4.4, 1.55], rot [1.4791, 0, 0.8577], 20 mm.
   - Bútorok és lámpák rejtve; EEVEE; három area-fény: északi ablak, DK-i derítő, mennyezeti derítő.
   - Élátfedés a régi alappal: 99,1 %.
   - Geometry Validator, „üres” mód: **PASS 0/0**. A „referencia” mód FAIL 6-ot ad; ezek a fürdő régi, már meglévő ütközései, nem a Cam_02 hibái.
   - Képek: `vegleges/…KORR_semleges.png` (sha256 `75ec3c85…`) és `…KORR_1b_TVfal_zona.png` (sha256 `3f247d98…`). Utóbbi a W01 TV-fal zónáját sötét blokkal jelöli (x 3,67–4,07; y 4,05–8,05).
   - Az élő Blender-fájlhoz nem nyúltam; a másolat sha256-ja a futás után változatlan.
2. **Cam_02 csatolmánycsomag:** 1. KORR alap, 2. 1b TV-fal-zóna, 3. ME-BAL-080 padló.
   - A helyszíni fotókat (045/004/003) **kivettem**. A 13-as első javított próbája 6 csatolmánnyal 38 %-os sarkot adott, vagyis a fotók rontották a kameratartást.
   - Az üzenet elejére bekerült a „0. METHOD: IMAGE-TO-IMAGE EDIT of image 1” szabály.
3. **Integrátori v1.3 promptmásolatok** (`_patch_v1_3/`, 10 fájl + `patch_v1_3_naplo.json`). A naplóban hivatkozott `05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_3_7d3c67f/` útvonal tartalma ez a mappa; a 05_promptok-ba nem írtam.
   - **K-02** (S03–S10 Cam_02): az ML04 függeszték a képen kívül van, a jobb szélen nem rajzolható. A 31-es és a 49-es ezt megszegte, a függeszték a jobb felső sarokban látszik.
   - **K-03** (S03/S04 Cam_12): az olajfa kikerült, és tiltott lett bármilyen tárgy a W02 előtt. Ez a 14-es és a 20-as v2-n működött.
4. **Fejléc-kiegészítések:**
   - 27: az íves végelem a mellvéden belül marad. **Nem hatott.**
   - 50: nincs ablak az előszobában. **Hatott.**
   - 52: a bal előtér üres marad. **Hatott.**

## Stílusonként
Minden stílusból 6 kép van, 10 × 6 = 60. A vizuális sorrendem szerint a top 3: **S10 Desert Modern 70, S02 BiBo Nocturne, S06 Zenit Atelier**. Ez ízlésítélet, nem költség- és nem kivitelezhetőségi rangsor.

## Fájlok
- `<IMAGE_ID>__OPUS55_V3_1__v1.png` / `__v2.png` – az eredeti, letöltött 1586 × 992-es PNG; méret és sha256 a naplókban.
- `A902_OPUS55_V3_1_kontaktlap_v2.jpg` – mind a 60 sor, a legfrissebb változattal; a kék felirat a javítókörben készült képeket jelöli. A régi `…_kontaktlap.jpg` az 1. kör állapota.
- `_gate/<kep_id>__gate.jpg`, `…__v2__gate.jpg` – alap | render | 50 % keverék | élkép. A Cam_02 sorai a KORR alapra vetítve.
- `_munka/` – a generáló, a kapukép- és a naplószkriptek (`build_v2.py`, `claim_v2.py`, `gate2.py`, `kontakt_v2.py`).

## Nyitott / következő lépés
1. **Cam_02:** még mindig hátrébb álló kamera, ~7–8 %-os sarokeltolódás. Nem javasolok vakon további ChatGPT-regenerálást. Ha kell, előbb a döntős stílusokra érdemes kis kép-a-képben maszkos szerkesztést vagy Blender-tömegmodellt adni.
2. **27 (és 39) Cam_03:** a mellvédvonalat Blenderben kell jelölni az alapon (1b-típusú jelölőkép), csak utána érdemes újrafuttatni.
3. **Cam_12 v1-sorok** (02, 08, 26, 32, 38, 44, 56): a v2-csomag (K-03 tiltólista) tartja a kamerát. A döntősöknél érdemes ezzel újrafuttatni.
4. **Fürdők (mind):** gyenge a pakolófelület. Ez az Opus-promptok hibája, nem a generálásé.
5. A részletes Blender-validáció és a költségellenőrzés a döntős koncepciókra jön, Péter döntése után.

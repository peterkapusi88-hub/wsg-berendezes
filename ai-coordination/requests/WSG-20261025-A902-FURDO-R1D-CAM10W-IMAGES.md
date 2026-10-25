# WSG-20261025-A902-FURDO-R1D-CAM10W-IMAGES – 10 fürdőkép, ellenirány, fantáziadúsabb változat (r1d), ChatGPT Images, a versenyen kívül

**Felváltja a r1c-futást (Péter 17:16: „meh”).** Ha a r1c-futás még megy, állítsd le; a kész r1c-képek maradnak, de nem folytatjuk. A r1d-ben:
- a WC-szekrény formázott, megvilágított nyitott fülkéket kap (stílusonként más);
- a jobb fal a zuhany vége, pontosan a zuhany szélességében, a padkától a belső sarokig, fogassal egybeépítve, néhol trompe-l’oeil „poénnal”;
- a WC-szekrény fényének forrása (V02 ventilátor-táp, a szekrény tetejében) a promptban is ki van mondva.

**Kérte:** Péter, 2026-10-25 16:52 és 16:56.
- A fürdőt a Kémeri-fotó (ME-BAL-066) szögéből is kéri.
- A WC fölé, a Geberit-falra egysíkú beépített szekrény kerüljön, rejtett fénnyel.
- A jobb oldali falra vízálló dekor kerüljön, ha nem sok.
- **Minden fénynek legyen valós áramforrása.**

**Előkészítette:** Claude (Opus 5.5) · **Indítás:** Péter, külön munkamenetben · **Státusz:** KONCEPCIÓ – NEM VALIDÁLT. A DC2026-versenynek nem része.

## 1. Forrás (csak olvasni)
- Ág: `wsg/a902-furdo-r1b-20261025`. A commitot a futás elején rögzítsd.
- Promptok (10 db, szó szerint, változtatás nélkül): `05_promptok/A902_furdo_r1b_20261025/promptok_Cam10W_r1d/<kep_id>.prompt.md (kép-ID végződés: `_Cam_10W_B`)`.
- Háttér: a stílusspecifikációk 4. pontja, „r1c” rész (`05_promptok/KEP004_OPUS55_V3_1_r1/10_STILUS_SPEC/`); az elemlista F10–F12 sora.

## 2. Képek sorrendje (minden képnél)
1. **Image 1 – a kamera és a geometria (kötelező):** `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg`. Ennek a nézetnek nincs Blender-alapja, a valódi fotó a mérvadó.
2. **Image 2 – anyagreferencia:** `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg`.
3. **Image 3 – a stílus folytonossága:** az azonos stílus elfogadott Cam_10 képe a `renders/a902-furdo-r1b-10` ágról: `04_renderek/ai_chatgpt/OPUS55_FURDO_R1B/<A902_Sxx_…_4_furdo-06-2_Cam_10_A>__FURDO_R1B__v1.png`. A fájlnevet a prompt IMAGES bekezdése megadja.

## 3. Üzenetfejléc
Rövid fejléc a prompt elé:
- a kép-ID;
- **„0. METHOD: IMAGE-TO-IMAGE EDIT of image 1”** – a 60-as futás Cam_02-javítókörében ez tartotta a kamerát;
- pontosan 1 kép, fekvő, az 1. kép kivágásával, felirat nélkül.

A 60-as futás GEOMETRY LOCK-ját itt ne használd, mert az a Blender Cam_10-re szól. A prompt a REALITY RULES-ban maga mondja ki a kötöttségeket.

## 4. Futtatási szabály
- Egy fiók, saját lap, **képenként új beszélgetés**, pontosan 1 kép, ugyanaz a képes modell.
- **Az S01-gyel kezdj.** Akkor folytasd, ha az S01-en ez mind rendben van:
  - a kameraállás egyezik a fotóval;
  - a szekrény egy síkban van a perem homlokával, és a stílus formázott fülkéje felismerhető;
  - a megvilágított nyitott rész a hatszög-dekort mutatja;
  - a zuhany-végfal pontosan a zuhany szélességében van, a fogasokkal együtt;
  - a nyomólap szabad;
  - a WC és a törölközőszárító a helyén van.
- Ha az S01 nem jó, állj meg, és írd meg a hibát. A promptot ne írd át.
- Hibás kép legfeljebb 1× generálható újra, `__v2` néven, a fejléc-változtatást naplózva.
- CAPTCHA-t és limitet ne kerülj meg; limit esetén `SKIPPED_LIMIT`.

## 5. Kimenet
- Ág: a meglévő `renders/a902-furdo-r1b-10`, új mappa: `04_renderek/ai_chatgpt/OPUS55_FURDO_R1D_CAM10W/`.
  - `<kep_id>__FURDO_R1D__v1.png`
  - `GENERALASI_NAPLO.csv`
  - `uzenetek/`
  - `_gate/` – fotó | render | 50 % keverék | élkép
  - kontaktlap
  - `README.md`
- A `main`-be és a `competition/*` ágakba nem írsz. PR-t nem nyitsz.
- Képenkénti ellenőrzés a README-be:
  - kamera = fotó;
  - burkolat és hatszög-dekor változatlan;
  - a szekrény egy síkban van, nem lóg ki, a ventilátor alatt végződik;
  - a nyitott sáv megvilágított, a hatszögek árnyékot vetnek;
  - a nyomólap és a WC a helyén van;
  - a törölközőszárító kábele rendezett;
  - a zuhany-végfal a padkától a belső sarokig ér, 2,40 m magas, fogasokkal; a trompe-l’oeil lapos kép, nem ablak;
  - a pult vége és a mosdó a bal alsó sarokban egyezik az image 3-mal;
  - ablak nincs;
  - a LED folyamatos vonal.

## 6. Tilos
Blender módosítása, rendelés, ajánlatkérés, külső kommunikáció, PR-merge, más ágak írása, a prompt szövegének átírása.

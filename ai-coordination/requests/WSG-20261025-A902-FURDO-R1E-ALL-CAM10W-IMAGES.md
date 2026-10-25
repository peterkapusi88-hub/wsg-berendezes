# WSG-20261025-A902-FURDO-R1E-ALL-CAM10W-IMAGES – 9 + 1 kép: letisztult Cam_10W, S02–S10 (+ S01 kábeljavítás), ChatGPT Images, a versenyen kívül

**Kérte:** Péter, 2026-10-25 18:21 („sokkal jobb lett a letisztult verzió, a bútor is, a kép is – így csináld meg S02–S10”).
**Előkészítette:** Claude · **Indítás:** Péter · **Státusz:** KONCEPCIÓ – NEM VALIDÁLT.

## 1. Forrás
- Ág: `wsg/a902-furdo-r1b-20261025`.
- Promptok (szó szerint, változtatás nélkül): `05_promptok/A902_furdo_r1b_20261025/promptok_Cam10W_r1e/A902_Sxx_…_4_furdo-06-2-wc_Cam_10W_C.prompt.md`.
- Az S01 promptja a kábeles mondattal kiegészült: „a kábel feszesen a dugaljba megy, semmi nem lóg”.

## 2. Képek, minden képnél ebben a sorrendben
1. `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg` – kamera, image-to-image szerkesztés.
2. `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg` – anyagok.
3. `renders/a902-furdo-r1b-10`: `04_renderek/ai_chatgpt/OPUS55_FURDO_R1B/<A902_Sxx_…_Cam_10_A>__FURDO_R1B__v1.png`.
4. `renders/a902-furdo-r1b-10`: `04_renderek/ai_chatgpt/OPUS55_FURDO_R1D_CAM10W/<A902_Sxx_…_Cam_10W_B>__FURDO_R1D__v1.png`.

## 3. Futás
- A fejléc a r1e-é: kép-ID, „0. METHOD: IMAGE-TO-IMAGE EDIT of image 1”, pontosan 1 kép, fekvő, felirat nélkül.
- Képenként új beszélgetés. Sorrend: S02, S03 … S10, végül az **S01 `__v2`**, amely csak a kábel miatt fut.
- Hibás kép legfeljebb 1 újrapróbát kap (`__v2`), naplózva.
- Ellenőrzés képenként:
  - a kamera azonos a fotóval;
  - a szekrény a mennyezetig ér, egy síkban van, a ventilátor nem látszik;
  - csak egy nyílás és benne legfeljebb egy tárgy;
  - a végfal egy darab a padkától a sarokig és a csempe tetejéig, egyetlen motívummal, ≥ ⅔ üres felülettel (az S04/S06/S07 anyagfelület, nem kép);
  - festett ablak nincs (S03, S09);
  - fény csak megnevezett forrásból;
  - a kábel nem lóg;
  - csupasz izzó nincs.

## 4. Kimenet
- Ág és mappa: `renders/a902-furdo-r1b-10`, `04_renderek/ai_chatgpt/OPUS55_FURDO_R1E_ALL/`.
- Tartalom: `<kep_id>__FURDO_R1E__v1.png` (az S01-nél `__v2`), napló, üzenetek, kapuképek, kontaktlap mind a 10 r1e képpel (az S01 a jobbik változattal), README.
- A main-be és a competition/* ágakba nem írsz, PR-t nem nyitsz.

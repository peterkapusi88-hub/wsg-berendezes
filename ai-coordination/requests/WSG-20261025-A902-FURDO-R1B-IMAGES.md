# WSG-20261025-A902-FURDO-R1B-IMAGES – 10 fürdőkép (Cam_10), ChatGPT Images, a versenyen kívül

**Kérte:** Péter, 2026-10-25 16:00, 16:04 és 16:17–16:20 – új fürdő: 100 cm-es üveg a zuhany szélén; az üvegtől a falig érő mosdóbútor, amelybe a mosdó belesüllyed; fali tároló; 1–2 stílustárgy; több látványos rejtett fény. Az egyedi üvegeket jóváhagyta. **Nem része a DC2026-versenynek:** a versenyben az eredeti marad (`competition/opus55-v3-1-20261025`, tartalma = CP14).
**Előkészítette:** Claude (Opus 5.5) · **Indítás:** Péter, ebben a fájlban hivatkozott külön munkamenetben.
**Státusz minden képre:** KONCEPCIÓ – NEM VALIDÁLT.

## 1. Forrás (csak olvasni)
- Ág: `wsg/a902-furdo-r1b-20261025` – a commitot a futás elején rögzítsd a naplóban.
- Promptok (10 db, szó szerint, változtatás nélkül): `05_promptok/A902_furdo_r1b_20261025/promptok/<kep_id>.prompt.md`. A BEGIN/END jelölők közötti szöveg a kreatív brief.
- Áttekintő és ellenőrzőlista: `05_promptok/A902_furdo_r1b_20261025/A902_furdo_r1b_10_prompt_Cam10.md`.
- Háttér: a stílusspecifikációk 4. pontja (`05_promptok/KEP004_OPUS55_V3_1_r1/10_STILUS_SPEC/` ezen az ágon), az elemlista F01–F09 sorai.

## 2. Képek sorrendje (minden képnél ugyanaz, mint a 60-as futás Cam_10-soraiban)
1. **Image 1:** `04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png` – kötelező kamera/geometria.
2. **Image 2:** `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg` – burkolat, dekorfal, szerelvények, mosdó (csak anyag).
3. **Image 3:** `08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg` – WC-fülke, törölközőszárító, ajtó (csak anyag).

## 3. Üzenetfejléc – a 60-as futás Cam_10-fejléce, két módosítással
A `renders/opus55-v3-1-60-tests` ág `04_renderek/ai_chatgpt/OPUS55_V3_1_60_TESZT/uzenetek/06_…Cam_10_A.txt` fejlécét használd (GEOMETRY LOCK). Ott a Cam_10 10/10 PASS lett. Két módosítás kell:
- **A 3. pont (Forbidden) ezt kapja:** *„Exception for this run: the creative brief ADDS three new built elements – a fixed 100 × 200 cm glass panel standing on the shower kerb from the far wall towards the camera (no door, open entry at the near end), a floating vanity on the far wall from the right-hand shaft-block corner to the glass (the existing basin stays exactly in place and is set into the counter, asymmetrically: narrow towel slot left, drawer block right), and a slim wall cabinet in the right-hand corner. Add them; everything already built stays exactly as in image 1.”*
- **A 2. pont kiegészítése (képarányok a 60-as lock alapján):** a vanity a jobb oldali aknasaroktól (≈ 68 %) a zuhanypadka vonaláig (≈ 35–37 %) ér; a mosdó a helyén marad (≈ 41–58 %). Az üveg a padka vonalán a távoli faltól (≈ 30–37 %) a kép bal széle felé tart. Az üveg 200 cm magas, a teteje a csempe felső széle (2,85 m) alatt van.
- A „glass shower screen” tilalom a régi fejlécben és a régi promptokban volt; **ebben a futásban nem érvényes.**

## 4. Futtatási szabály
- Egy ChatGPT-fiók, saját lap, **képenként új beszélgetés**, pontosan 1 kép, ugyanaz a képes modell. A modell nevét a naplóba írd.
- Sorrend: **S01 először.** Ha az S01-en az üveg, a pult, a belesüllyesztett mosdó és a geometria rendben van, mehet a többi kilenc (S02 … S10). Ha nem, állj meg, és írd meg a hibát; promptot ne írj át.
- Sikertelen kép legfeljebb 1× generálható újra; a második próba `__v2` néven fut, és a fejléc-változtatást naplózd.
- Ne kerülj meg CAPTCHA-t vagy limitet; limitnél `SKIPPED_LIMIT`, a többi kép marad.

## 5. Kimenet
- Ág: **`renders/a902-furdo-r1b-10`** (új ág a `wsg/a902-furdo-r1b-20261025`-ből). A `main`-be, a `competition/*` és a `renders/opus55-v3-1-60-tests` ágba nem írsz. PR-t nem nyitsz.
- Mappa: `04_renderek/ai_chatgpt/OPUS55_FURDO_R1B/`
  - `<kep_id>__FURDO_R1B__v1.png` – az eredeti letöltött PNG, átnevezve, nem újratömörítve;
  - `GENERALASI_NAPLO.csv` – a 60-as napló oszlopaival (nr, kep_id, kamera, verzió, státusz, prompt-forrás + commit, csatolmányok, üzenet + sha256, chat-URL, időpont, fájl, méret, sha256, geometria, megjegyzés);
  - `uzenetek/` – a ténylegesen elküldött üzenetek;
  - `_gate/` – alapkép | render | 50 % keverék | élkép, mint a 60-as futásban;
  - kontaktlap a 10 képről;
  - `README.md` – eredménytábla.
- Képenkénti ellenőrzés a README-be:
  - a burkolat és a dekorfal változatlan;
  - a mosdó ugyanaz a fehér szögletes Geberit, beleülve a pultba, balra kb. 19 cm-es réssel;
  - a pult az aknától az üvegig ér, és alatta látszik a padló;
  - egyetlen fix üveg van a padkán, ajtó nélkül, nyitott belépővel;
  - a fali oszlop a jobb sarokban van, és a dugaljak szabadok;
  - nincs ablak;
  - a LED folyamatos vonal;
  - a stílustárgy(ak) látszanak.

## 6. Tilos
Blender módosítása, rendelés, ajánlatkérés, külső kommunikáció, PR-merge, más versenyző ágának vagy PR-jének írása, a prompt szövegének átírása.

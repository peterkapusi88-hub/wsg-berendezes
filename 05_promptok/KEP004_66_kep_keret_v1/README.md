# KEP-004 · 66 képes keret – regiszter, futtatási sorrend, átvétel/archiválás, ellenőrzőlista (v1, 2026-10-25)

**Forrás:** Péter 01:39 (66 képes célstruktúra, kis adagok), 01:49 (rejtett LED, V3.1), 01:58 (hero kamera, összekötő fal), 02:06 (két V3 próbakép).

**Generálási engedély:**
- Ez a keret **nem ad** generálási engedélyt. Minden adaghoz külön „mehet” kell; Péter ezt képszámra és képenként egy generálásra adja.
- Astra-futtatás, extra kredit, fizetős API csak Péter külön engedélyével.

## 1. Szerkezet
**66 kép = 10 stílus × 6 nézet + 6 kalibráció.** Regiszter: `KEP004_66_kep_regiszter.csv` (kép-ID, kamera, alapkép, promptforrás, adag, állapot, engedély).

| # | Nézet | Kamera | Alapkép (1. kép) | Megjegyzés |
|---|---|---|---|---|
| 1 | nappali–terasz | Cam_02 | `04_renderek/A902_alap_v2b1/…_02_nappali-terasz.png` | geometriai kontrollnézet; 1b: stílus-tömbkép |
| 2 | nappali hero | **Cam_12** (JAVASLAT, PR #17) | `04_renderek/A902_cam12_hero_javaslat/A902_Alap-v2b1k12_blender_12_nappali-hero_JAVASLAT.png` | ÉNy-i sarok, 22 mm; a W02 + W07 összekötő fal és a konyha pultfala látszik |
| 3 | konyha–étkező | Cam_03 | `…/A902_Alap-v2b1_blender_03_etkezo-konyha.png` (régi) | **Péter 02:33 CET: konyhaorientált új kamerajavaslat** (Claude), hogy ne fedjen át a Cam_12-vel |
| 4 | master | Cam_04 | `…/A902_Alap-v2b1_blender_04_master.png` | ágy 180 × 200, tengely y 6,40 |
| 5 | master panoráma | Cam_11 | `04_renderek/A902_cam11_javaslat_v1/…` | a PR #15-tel a main-en |
| 6 | fürdő 06.2 | Cam_10 | `…/A902_Alap-v2b1_blender_10_furdo-06-2.png` | csak műfény; a meglévő burkolat marad |
| K | kalibráció | C1 Zenit, C2 Lake Forest × Cam_02/Cam_04/Cam_11 | mint fent | a v1 benchmarkok kontrollált újratervezése (geometria v2, falkezelés) |

**Kép-ID:** `A902_<stílus>_<StílusNév>_<helyiségszám>_<helyiség>_<kamera>_A`. A hero ID-ja `…_1_nappali-hero_Cam_12_A`.
- **Ismétlésnél nem írunk felül:** új utótag kell – `_V3_r1`, `_V3_r2`… vagy `_v2`.
- A v1 16 ID-ja változatlanul benne van a regiszterben.

## 2. Futtatási sorrend (adagok és kapuk)
| Adag | Tartalom | Előfeltétel | Állapot |
|---|---|---|---|
| **A0 – geometriajavító próba** | 1 kép: S01 Cam_02, szerkesztő módban. A 1b tömbkép vagy az alapkép a szerkesztett forráskép, a termékfotók másodlagosak. | Péter „mehet” | **javasolt** – a V3-teszt geometriai hibája miatt (10–13,5 %). A V3_TEST (r2) után: az S02 héja ±1 %-on belül, az S01-ben ~+8 % belmagasság, mindkettőn túlméretes falbútor → S01-re továbbra is indokolt (`WSG-20261025-KEP-004_V3_TEST_gate.md`, 8. pont). **Péter 02:33 CET: most nem – előbb a V3.1 kreatív újratervezés.** |
| **A1** | S01 + S02 Cam_02 V3 | V3.1 (világítás, függöny); az A0 módszere, ha bevált | V3-teszt kész (V3_r1 02:18/02:23; V3_TEST r2 02:35/02:38 – Péter 02:22-es tesztpárja), végleges vár |
| **A2** | S01 + S02 Cam_12 hero | PR #17 „mehet”; V3.1, benne W02/W07 és konyhafront | vár |
| **B** | S01 + S02 Cam_03, Cam_04, Cam_11 | A1/A2 Gate PASS-közeli (geometria tűrésen belül) | vár |
| **C1/C2** | 1–2 további, karakteresen eltérő stílus (javaslat: S04 LA Horizon, S08 Milano Radical) Cam_02, majd Cam_12 | Astra V3 r2: részletes blokk ezekhez (a V3 r1 §5 csak falstratégiát ad) | vár |
| **D** | a többi stílus nagyobb adagokban (master, konyha) | C Gate | vár |
| **E** | fürdők (Cam_10) | utolsóként | vár |
| **K** | kalibráció (C1/C2 × 3) | a stílusképekkel azonos kapukkal, újratervezett promptokkal | vár |

**Stop-szabály:**
- Ha egy adagban két egymás utáni kép geometriája FAIL, a következő adag nem indul. Előbb a módszert javítjuk.
- Hero- és masternézetet csak jó első kör után skálázunk (Péter, 01:39).

## 3. Promptcsomag-verziók
| Mappa | Mi | Állapot |
|---|---|---|
| `05_promptok/KEP004_ChatGPT_Images_v1/` | 16 prompt (V2 stílusblokk), 2026-10-24 | megőrizve, nem írjuk át |
| `05_promptok/KEP004_ChatGPT_Images_v2_geometria/` | Cam_02 FRAME LAYOUT blokk (P902_24A) | megőrizve |
| `05_promptok/KEP004_ChatGPT_Images_V3_teszt/` | S01/S02 Cam_02 V3 próbakép, futtatva | megőrizve |
| `05_promptok/KEP004_ChatGPT_Images_V3_TEST/` | S01/S02 Cam_02 V3_TEST (r2: javított 1b tömbkép, fizikailag lehetséges tükörkép, pad nélkül, nyílászáró/padló-sor), futtatva | megőrizve |
| következő: `KEP004_ChatGPT_Images_V3_1/` | V3.1 (LED, függöny, összekötő fal, konyha) + az A0 módszere + Cam_12 FRAME LAYOUT | V3.1 után |

**2026-10-25 02:50 CET – végleges V3.1-brief, r2:** `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md` (az r1 felülírva).
- Astra mind a 66 kreatív promptot egy Work-futásban adja, checkpointolva.
- Helye: `05_promptok/KEP004_ASTRA_V3_1_r1/`, a manifestben `statusz` + `validalas` mezővel.
- A `COMPLETE` kreatív promptot jelent, nem futtatható csomagot. Futtatható csomag csak Claude auditja után készül.

A B része szerint változik a csomagépítés:
- teljes berendezés a „Nothing else stands in the room” tiltás helyett;
- nézetenkénti fény;
- új tömbképek a V3.1 elemlistából;
- rövidebb prompt, legfeljebb kb. 10–11 ezer karakter.

**Összefűzés:**
1. fejléc;
2. közös FIXED (a V3 felületkivétellel);
3. helyiség-FIXED;
4. Hue blokk;
5. FRAME LAYOUT (stílusonként, Blenderből vetítve);
6. stílusblokk (Astra, szó szerint, a dokumentált cserékkel);
7. RUN NOTES.

Minden csomaghoz: `_eszkozok/epito_*.py` + ellenőrzés (szó szerinti egyezés, sha256, csatolmánylista).

## 4. Átvétel és archiválás (v2)
1. **Mac csomag:** `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/<forduló>/<NN_kép-ID>/` – csatolmányok sorszámozva + `PROMPT_<kép-ID>.prompt.txt`.
2. **Futtatás** (Claude in Chrome):
   - új chat, „Kép létrehozása”, csatolás a sorrendben;
   - a prompt **fájlból** a lapba, sha256-ellenőrzéssel;
   - beillesztés, majd „Megjelenítés a szövegmezőben”;
   - **DOM-ellenőrzés** a küldés előtt; egy küldés.
   - Ha a ChatGPT a mezőbe helyezéskor maga küld (V3-teszt S02), a beküldött szöveget és a csatolmányokat utólag ellenőrizni és naplózni kell.
3. **Letöltés** natív felbontásban (1586 × 992), majd áthelyezés: `04_chatgpt_images_atvetel/<forduló>/<NN_kép-ID>/`, átnevezés nélkül.
4. **Repó:**
   - `04_renderek/ai_chatgpt/STYLE10_KEP004/<almappa>/<kép-ID>.png` + a futtatott `.prompt.txt`;
   - `archiv_manifest_<forduló>.json` (sha256, átvételi név, idő, chat-link);
   - `ATVETELI_NAPLO.csv`: a Mac-napló repó-másolata, ugyanaz a tartalom.
5. **Gate-audit:** `ai-coordination/results/WSG-…_<forduló>.md`; bizonyítékok: `_gate_<forduló>/`. A státusz a naplóba is bekerül.

## 5. Ellenőrzőlista képenként (Render Reality Gate)
**Előtte:**
- [ ] Péter „mehet” (képszám, adag)
- [ ] alapkép + tömbkép a helyes kamerából
- [ ] a V3/V3.1 befoglalók a Blenderben validálva (fal, ajtólendület, kiállás, közlekedő)
- [ ] a prompt sha256-ja egyezik
- [ ] csatolmánysorrend
- [ ] nincs hibás korábbi kép csatolva

**Utána:**
- **Geometria:**
  - [ ] vetített referenciapontok: falsarok, nyílászáró-profilok, padló- és mennyezetvonal; tűrés ±3 % (±30 px)
  - [ ] bútorhelyek a tömbkép szerint (±5 %)
- **Felületek:**
  - [ ] padló (EL2184, nem igazolt)
  - [ ] falak: tapéta, panel vagy fehér a terv szerint; kőhatású panel nem jelenhet meg valódi kőként
  - [ ] nyílászárók: fehér keret, sötét téglakáva
  - [ ] ajtók: világosszürke, fekete kilincs
  - [ ] kapcsolók szabadon
- **Termékek:** [ ] valós termék, konfiguráció, darabszám, szín
- **Fény:**
  - [ ] csak a meglévő pontok
  - [ ] Hue-kompatibilis lámpa
  - [ ] LED csak a jóváhagyott V3.1-terv szerint
- **Tükör, üveg:** [ ] fizikailag lehetséges tükörkép
- **Költség:** [ ] a látható anyag a jóváhagyott költségváltozat (fő vagy gazdaságos)
- **Státusz:** [ ] `KONCEPCIÓ` / `ELŐSZŰRT` / `PASS` / `FAIL`, eltéréslistával

## 6. Költségfegyelem
- Astra V3 r1 §5.1 stílusonkénti nappali-csomag: fő változat 0,68–1,20 M Ft, gazdaságos 0,51–0,86 M Ft (Astra-becslés).
- A V3.1 LED-csomagja nagyságrendben 0,5–1,0 M Ft a lakásra (Claude-becslés, nem ellenőrzött).
- A 18 M nem nő, a 2 M tartalék érintetlen; minden többletnél meg kell mutatni, mi esik ki.
- A képek a jóváhagyott költségváltozatot mutatják. A gazdaságos változat nem jelenhet meg prémium anyaggal.

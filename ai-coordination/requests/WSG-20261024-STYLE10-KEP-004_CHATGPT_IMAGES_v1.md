# WSG-20261024-STYLE10-KEP-004 · ChatGPT Images végrehajtási terv v1 (2026-10-24 23:10) – 40 kép, fokozatosan

**Viszony az eredeti briefhez:** az eredeti `WSG-20261024-STYLE10-KEP-004.md` változatlanul megmarad (Astra MEDIUM-ra írt, kétrészes terv). Ez a verziózott dokumentum Péter 2026-10-24 22:13-as utasítását hajtja végre.
- A képek **normál ChatGPT-chatben** készülnek, nem új Astra Work-feladatban.
- **10 stílus × 4 helyiség = 40 kép.** A fürdő nincs halasztva; a korábbi 30 képes, fürdő nélküli terv tárgytalan.
- Képgenerálás **nem indult**. Minden lépéshez Péter külön „mehet”-je kell. Astra Work nem indul.

**Státusz minden képre a Gate-auditig:** `KONCEPCIÓ – NEM VALIDÁLT`.

## 1. Bemenetek (ellenőrzött)

- **Kreatív forrás:** Astra V2 – `05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md` (`72f6401`), 40 stílusblokk. **Sablon:** v3.1 §1 közös FIXED + §2 helyiség-FIXED (`05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md`). Egyik sincs módosítva.
- **Kameraalapok** (PR #14, `be15c61`, `04_renderek/A902_alap_v2b1/`): Cam_02, Cam_03, Cam_04, Cam_10.
  - A Cam_10 rögzített blokkja (`05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`) a v3.1 ideiglenes Cam_10-blokkját váltja.
- **Új, dokumentált kiegészítések** (az összefűzött promptban szó szerint):
  - `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`: Philips Hue, minden helyiség (Péter, 22:57);
  - `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md`: gardróbfal az északi fülkében, master (Péter, 22:37–22:40).
- **Cam_11 master-panoráma:** JAVASLAT, draft PR #15. A Cam_04/Cam_11 döntésig a master-képek blokkoltak. Összevetés: `04_renderek/A902_cam11_javaslat_v1/CAM11_JAVASLAT_es_OSSZEVETES_v1.md` (a PR ágon).

## 2. Ütemezés – 40 stíluskép + 4 kalibráció

| Lépés | Képek | Tartalom | Kapu (mind kell) |
|---|---|---|---|
| **1a** | 6 | C1 Zenit + C2 Lake Forest kalibráció **Cam_02**; S01 Kyoto Ink + S02 BiBo Nocturne **Cam_02 és Cam_03** | csomag kész ✔ · 6 Kave Home-termékkép ✔ (Péter képernyőképeiből kivágva, 23:25) · K8 ✔: Eamy 55 × 53 × 75 és Ciselia 52,5 × 55 × 75 · **Péter „mehet”** |
| **1b** | 2 | S01 + S02 **fürdő 06.2 (Cam_10)**, rögzített kamerablokk + valódi 06.2-fotók | 1a Gate · Péter „mehet” |
| **1c** | 4 | C1 + C2 kalibráció és S01 + S02 **master 05.1** | **Cam_04/Cam_11 döntés** (Cam_11 esetén újra-összefűzés a Cam_11 blokkal) · ágy-y döntés · olvasólámpa- és fülkefény-termék Hue-foglalattal (Astra „pre-image gate”) · Péter „mehet” |
| Gate 1 | – | Claude-audit: thumbnail-sziluett (400 px), szürkeárnyalat, C1/C2 összevetés helyiségenként, Reality Card képenként, Hue- és termékegyezés | sikeres audit |
| **2** | 16 | S03 Alelí Casa · S04 LA Horizon · S05 Miami Streamline · S06 Zenit Atelier × 4 helyiség | Gate 1 · Kave-fotók és K8 · Hue-ellenőrzés · Péter „mehet” |
| Gate 2 | – | mint fent | |
| **3** | 16 | S07 Lake Forest Couture · S08 Milano Radical · S09 Paris Collector · S10 Desert Modern 70 × 4 | Gate 2 · Péter „mehet” |
| Döntés | – | 3 döntős a **teljes 10 × 4** összevetés után (Péter) | – |
| B sorozat | 3 × 4 | döntősök, esti jelenet | külön engedély |

- Stílusképek összesen: 8 + 16 + 16 = **40**.
- Kalibráció: 4 kép (Cam_02 + master). Cam_03/Cam_10 kalibráció csak Péter kérésére; fürdőhöz nincs eredeti Zenit/LF referencia.
- **Teljes 40 automatikusan nem indul.**
- Sikertelen kép legfeljebb 1× generálható újra, a promptváltozás új, `_v2` fájlban. Variánsokat Péter kérése nélkül nem futtatunk.

## 3. Futtatási szabály ChatGPT-ben

1. **Képenként új chat** (ne keveredjen a stílusok kontextusa), mindig ugyanazzal a képes modellel. A modell nevét a naplóba írjuk.
2. Csatolás a csomag `01_…`, `02_…` sorrendjében (a fájlnév adja a sorrendet). Csomagonként legfeljebb 9 kép.
3. A teljes `PROMPT_<kép-ID>.prompt.txt` szöveg bemásolva. A futtatási fejléc kimondja, hogy a küldés = Péter jóváhagyása.
4. Kimenet: fekvő kép az 1. kép kivágásával. 16:10, ha nincs, a legközelebbi fekvő formátum. A Gate-auditban normalizáljuk.
5. A kép letöltve az átvételi mappába, átnevezés nélkül. Claude archiválja.

## 4. Képenkénti csomag (próbakör 1 – 12 csomag)

Hely: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/probakor1_v1_2026-10-24/`. A promptok a repóban: `05_promptok/KEP004_ChatGPT_Images_v1/`.

| # | Kép-ID | Lépés | Csatolmány | Hiányzik |
|---|---|---|---|---|
| 01 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | 1a | 5 | – |
| 02 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | 1a | 5 | – |
| 03 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | 1a | 9 | – (3 Kave-kép pótolva) |
| 04 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | 1a | 9 | – (3 Kave-kép pótolva) |
| 05 | `A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A` | 1a | 8 | – (2 Kave-kép pótolva) |
| 06 | `A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A` | 1a | 8 | – (2 Kave-kép + Ciselia-méret pótolva) |
| 07 | `A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A` | 1b | 3 | – |
| 08 | `A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A` | 1b | 3 | – |
| 09–12 | C1, C2, S01, S02 `…_3_master_Cam_04_A` | 1c | 4 | kameradöntés |

**Képbemenetek sorrendje** (v3.1 §0/a):
1. Blender-alapkép;
2. valós helyszíni fotók: a padló a 2. kép, a fürdőnél a 06.2-fotó;
3. eredeti Zenit/LF-kép – csak kalibrációnál;
4. termékfotók: IKEA/Westwing letöltve; Kave Home kivágva Péter képernyőképeiből (csökkentett felbontás, csak alak, arány, szín és anyag).

**Tudatos eltérések az Astra-blokkok „Inputs” sorától** (a prompt végén, a „RUN NOTES” részben dokumentálva):
- v2b-1 alapkép a régi v2b-útvonal helyett.
- Az annotált ellenőrző rajzot nem csatoljuk (felirat, sraffozás).
- Stílusképhez nem csatolunk Zenit/LF-képet (stíluskeveredés).
- Master: a ME-BAL-060/069/063 a 05.3-at mutatja, helyette a ME-BAL-077 (05.1).
- Fürdő: az 1. kép már létezik, a ME-BAL-064/066 igazoltan a 06.2.
- Jelölve, nem validált: a modell régi szaniter-ütközései (2–10 cm) és a közelítő hatszög-dekor.

## 5. Ellenőrzések (2026-10-24 23:12) – `05_promptok/KEP004_ChatGPT_Images_v1/README.md`

- A 12 prompt mindegyikében szó szerint egyezik: a közös FIXED, a helyiség-FIXED (Cam_10-nél a rögzített blokk), a Hue-blokk, a mastereknél a gardróbblokk és a frontsor, valamint az Astra-stílusblokk vagy a §3 kalibráció + koncepció-cella.
- A kép-ID egyezik Astra „Output” sorával. Nem maradt helyőrző. A csatolmánylista hossza egyezik a fájlokéval.
- **Termékek:**
  - Lennon 800 000 Ft és Anouk 320 000 Ft (egyezik);
  - **Toni 200×90: most 350 000 Ft, Astra rekordjában 320 000 Ft (+30 000 Ft, Westwing 2026-10-24)**;
  - JÄTTEBO 928 000 Ft, NORDLI 189 900 Ft (180×202×30, ellenőrzött), EKBACKEN 24 990 Ft.
- **Hue:**
  - Somar: függeszték, „Hanging method: Wire” (Kave-specifikáció, Péter képernyőképe 23:02). E27, 40 W: megfelel. A kábelhossz nincs rögzítve.
  - Brisia: E27, de a gömbnyílás Ø49 mm, ezért Hue Lustre E14 + E27→E14 adapter kell. A Hue Lustre E14 mérete Ø45 × 77 mm, 2200–6500 K (Philips Hue termékoldal, 2026-10-24, ellenőrzött). Feltételesen megfelel, Péter dönt.
  - **Brisia rögzítése:** a Kave méretrajza szerint (Péter képernyőképe, 23:06) **mennyezeti lámpa, nem függeszték**: Ø80 × 26 cm, rozetta Ø16, 4 db Ø15-ös gömb. Az ML04-en a mennyezeten ül, a legalsó pontja kb. 2,64 m-en van (belmagasság 2,90). Astra S02-blokkja „pendant / suspended object”-ként írja; a RUN NOTES ezt felülírja, a kép nem rajzolhat zsinóron lógó lámpát.
  - A típus-előírt lámpák (ML03, FL01, FL04, ML10, olvasólámpák, D26 fülkefény) csak Hue-kompatibilis foglalattal vagy Hue-lámpatestként választhatók.
  - A meglévő kültéri FL05–07 foglalata ismeretlen (hétfő).
  - **Visszaellenőrzés mind a 12 promptra (23:28):**
    - a Hue-blokk mindenhol szó szerint szerepel;
    - G9/G4 vagy nem Hue-s integrált LED sehol (a kalibráció LED-elemeit a RUN NOTES Hue-ra fordítja);
    - lámpánkénti tábla: `05_promptok/KEP004_ChatGPT_Images_v1/README.md`.

## 6. Átvétel és archiválás

- **Mac:** `~/Downloads/WSG/KEP-004/04_chatgpt_images_atvetel/probakor1/<NN_kép-ID>/` (mappánként 1 kép, átnevezés nélkül) + `ATVETELI_NAPLO.csv` (chat-link, modell, időpont, megjegyzés).
- **Claude archiválja** a `archivalas_elokeszito.py` szkripttel (csak másol, nem töröl, nem ír felül):
  - kanonikus név: `A902_<Sxx>_<Stílus>_<n>_<helyiség>_<Cam>_A.png`, ismétlésnél `_A_v2`;
  - mellé a futtatott `.prompt.txt` kerül;
  - a sha256 a naplóba kerül.
- **GitHub:** `04_renderek/ai_chatgpt/STYLE10_KEP004/` (README + napló), commit lépésenként. Eredményfájl: `ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md` (1a–1c), `_r2a.md`, `_r2b.md`.

## 7. Nyitott kérdések / döntések (Péter)

1. **Master-kamera:** Cam_04 vagy Cam_11 (javaslat: Cam_11; PR #15).
2. **Ágy y-tengelye:** a Blender-modellben 6,00, a tervrajz és a kiállások szerint 6,40. A modell helyén a fejvég a D22/D23 dugaljat és a K14 kapcsolót takarja. A prompt a terv szerinti helyet írja, a modell nem változott.
3. **Brisia (S02, és Astra S08-blokkjában is):**
   - elfogadható-e a Hue-adapter;
   - mennyezeti lámpaként az asztallap fölött kb. 1,9 m-re ül, így nem ad az asztal fölé lógó, meghitt fényt.
   - Javaslat: a próbakörben a valós, mennyezeti Brisia fut (őszinte kép). Ha a Gate 1-nél gyenge, Astra az ML04-re valódi függesztéket választ Hue-kompatibilis foglalattal.
4. **Kave Home – kész (23:25):**
   - mind a 20 tétel termékképe és 10 méretrajz Péter képernyőképeiből kivágva (6 próbaköri + 14 a 2–3. adaghoz);
   - a forrás-képernyőképek a Macen vannak, csak a Kave-oldal részével.
   - A 2–3. adaghoz kell még: az Ardali, a Drava, a Madali és a Novae „Specifications” paneljének képernyőképe (foglalat).
5. **Kanapé:** a 10 stílusból csak az S06 és az S10 Kave-kanapés. A 2–3. adag előtt cserélhetünk Kave-re (Gala U, Martina íves + Neom puff, Vera, Blok).
6. **Hétfői mérés:**
   - az erkély északi vége (a fotón téglafal, a modellben korlát);
   - az üvegfal-osztás (modell 0,90/0,90/1,84 m);
   - a kültéri lámpák foglalata;
   - a 06.2 szaniter-render-réteg javítása (külön feladat).
7. **A 2–3. adaghoz:**
   - stílusonkénti gardróbfront (S03–S10);
   - Hue-ellenőrzés (Ardali, Drava, Novae, Madali);
   - K8: Eamy barna, Ciselia bézs, Corvena méretei. A méretrajzok kivágva megvannak, a leolvasás az adag építésekor jön.
8. **Master-lámpák (1c-kapu):** Astra V2 a master olvasólámpáinak (D20–D23) és fülkefényének (D26) termékét és rögzítését „pre-image gate”-nek jelöli. Az 1c előtt tehát kell egy Hue-kompatibilis termék és befoglaló, vagy Péter kifejezett engedélye, hogy típusleírással fusson.

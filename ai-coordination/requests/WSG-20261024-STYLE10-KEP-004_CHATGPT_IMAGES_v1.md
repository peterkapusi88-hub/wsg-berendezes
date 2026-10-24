# WSG-20261024-STYLE10-KEP-004 · ChatGPT Images végrehajtási terv v1 (2026-10-24 23:10, frissítve 2026-10-25 00:05) – 50 stíluskép, fokozatosan

**Viszony az eredeti briefhez:** az eredeti `WSG-20261024-STYLE10-KEP-004.md` változatlanul megmarad (Astra MEDIUM-ra írt, kétrészes terv). Ez a verziózott dokumentum Péter 2026-10-24 22:13-as utasítását hajtja végre.
- A képek **normál ChatGPT-chatben** készülnek, nem új Astra Work-feladatban.
- **10 stílus × 4 helyiség = 40 kép** (Péter, 22:13). A fürdő nincs halasztva; a korábbi 30 képes, fürdő nélküli terv tárgytalan.
- **23:33, Péter: a master mindkét kamerával** (Cam_04 + Cam_11) → stílusonként 5 kép, **összesen 50 stíluskép + 6 kalibráció = 56**.
- Képgenerálás **nem indult**. Minden lépéshez Péter külön „mehet”-je kell. Astra Work nem indul.

**Státusz minden képre a Gate-auditig:** `KONCEPCIÓ – NEM VALIDÁLT`.

## 1. Bemenetek (ellenőrzött)

- **Kreatív forrás:** Astra V2 – `05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md` (`72f6401`), 40 stílusblokk. **Sablon:** v3.1 §1 közös FIXED + §2 helyiség-FIXED (`05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md`). Egyik sincs módosítva.
- **Kameraalapok** (PR #14, `be15c61`, `04_renderek/A902_alap_v2b1/`): Cam_02, Cam_03, Cam_04, Cam_10.
  - A Cam_10 rögzített blokkja (`05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`) a v3.1 ideiglenes Cam_10-blokkját váltja.
- **Új, dokumentált kiegészítések** (az összefűzött promptban szó szerint):
  - `05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md`: Philips Hue, minden helyiség (Péter, 22:57);
  - `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md`: gardróbfal az északi fülkében, master (Péter, 22:37–22:40).
- **Cam_11 master-panoráma:** draft PR #15; Péter 23:33-kor a Cam_04 **mellé** kérte, nem helyette. A 13–16. csomag futtatásához a PR beolvasztása („mehet”) kell. Összevetés: `04_renderek/A902_cam11_javaslat_v1/CAM11_JAVASLAT_es_OSSZEVETES_v1.md` (a PR ágon).

## 2. Ütemezés – 50 stíluskép + 6 kalibráció

| Lépés | Képek | Tartalom | Kapu (mind kell) |
|---|---|---|---|
| **1a** | 6 | C1 Zenit + C2 Lake Forest kalibráció **Cam_02**; S01 Kyoto Ink + S02 BiBo Nocturne **Cam_02 és Cam_03** | csomag kész ✔ · 6 Kave Home-termékkép ✔ (Péter képernyőképeiből kivágva, 23:25) · K8 ✔: Eamy 55 × 53 × 75 és Ciselia 52,5 × 55 × 75 · **Péter „mehet”** |
| **1b** | 2 | S01 + S02 **fürdő 06.2 (Cam_10)**, rögzített kamerablokk + valódi 06.2-fotók | 1a Gate · Péter „mehet” |
| **1c** | 8 | C1 + C2 kalibráció és S01 + S02 **master 05.1, Cam_04 és Cam_11** (párban, ugyanabban a chatben: előbb a Cam_04, utána a Cam_11) | ágy ✔ (terv szerint, 23:35) · olvasólámpa ✔ (Raze, Aleyla – Hue) · **PR #15 „mehet”** (Cam_11) · 1a/1b Gate · Péter „mehet” |
| Gate 1 | – | Claude-audit: thumbnail-sziluett (400 px), szürkeárnyalat, C1/C2 összevetés helyiségenként, Reality Card képenként, Hue- és termékegyezés | sikeres audit |
| **2** | 20 | S03 Alelí Casa · S04 LA Horizon · S05 Miami Streamline · S06 Zenit Atelier × 5 kép (master 2 kamerával) | Gate 1 · Kave-fotók és K8 ✔ · Hue-ellenőrzés (Novae ✗) · gardróbfrontok · Péter „mehet” |
| Gate 2 | – | mint fent | |
| **3** | 20 | S07 Lake Forest Couture · S08 Milano Radical · S09 Paris Collector · S10 Desert Modern 70 × 5 | Gate 2 · Péter „mehet” |
| Döntés | – | 3 döntős a **teljes 10 stílus** összevetése után (Péter) | – |
| B sorozat | 3 × 4 | döntősök, esti jelenet | külön engedély |

- Stílusképek összesen: 10 + 20 + 20 = **50**.
- Kalibráció: 6 kép (Cam_02, master Cam_04, master Cam_11). Cam_03/Cam_10 kalibráció csak Péter kérésére; fürdőhöz nincs eredeti Zenit/LF referencia.
- **Az 50 kép automatikusan nem indul.**
- Sikertelen kép legfeljebb 1× generálható újra, a promptváltozás új, `_v2` fájlban. Variánsokat Péter kérése nélkül nem futtatunk.

## 3. Futtatási szabály ChatGPT-ben

1. **Képenként új chat** (ne keveredjen a stílusok kontextusa), mindig ugyanazzal a képes modellel. A modell nevét a naplóba írjuk.
   - **Kivétel:** a master Cam_11-képét ugyanabban a chatben kell futtatni, közvetlenül az azonos stílusú Cam_04-kép után, hogy a bútorok és anyagok egyezzenek. A prompt kimondja, hogy új képet kér, nem a régit szerkeszti.
2. Csatolás a csomag `01_…`, `02_…` sorrendjében (a fájlnév adja a sorrendet). Csomagonként legfeljebb 9 kép.
3. A teljes `PROMPT_<kép-ID>.prompt.txt` szöveg bemásolva. A futtatási fejléc kimondja, hogy a küldés = Péter jóváhagyása.
4. Kimenet: fekvő kép az 1. kép kivágásával. 16:10, ha nincs, a legközelebbi fekvő formátum. A Gate-auditban normalizáljuk.
5. A kép letöltve az átvételi mappába, átnevezés nélkül. Claude archiválja.

## 4. Képenkénti csomag (próbakör 1 – 16 csomag)

Hely: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/probakor1_v1_2026-10-24/`. A promptok a repóban: `05_promptok/KEP004_ChatGPT_Images_v1/`.

| # | Kép-ID | Lépés | Csatolmány | Hiányzik |
|---|---|---|---|---|
| 01 | `A902_C1_Zenit_1_nappali-terasz_Cam_02_A` | 1a | 5 | – |
| 02 | `A902_C2_LakeForest_1_nappali-terasz_Cam_02_A` | 1a | 5 | – |
| 03 | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | 1a | 9 | – (3 Kave-kép pótolva) |
| 04 | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | 1a | 9 | – (Kave-képek pótolva; Brisia → Brisia függeszték Ø50) |
| 05 | `A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A` | 1a | 8 | – (2 Kave-kép pótolva) |
| 06 | `A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A` | 1a | 8 | – (Kave-képek + Ciselia-méret pótolva; Brisia → Brisia függeszték Ø50) |
| 07 | `A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A` | 1b | 3 | – |
| 08 | `A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A` | 1b | 3 | – |
| 09–10 | C1, C2 `…_3_master_Cam_04_A` | 1c | 4 | – |
| 11–12 | S01, S02 `…_3_master_Cam_04_A` | 1c | 5 | – (+ olvasólámpa: Raze, illetve Aleyla) |
| 13–16 | C1, C2, S01, S02 `…_3_master_Cam_11_A` | 1c | 4 | PR #15 „mehet” |

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
  - **Visszaellenőrzés mind a 16 promptra (2026-10-25 00:00):**
    - a Hue-blokk mindenhol szó szerint szerepel;
    - a megnevezett lámpák mind Hue-kompatibilisek: Somar E27; Brisia függeszték E27, Ø97 mm-es nyílás; Raze E27; Aleyla E14;
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

**Lezárva 2026-10-24 23:33–23:39 (Péter):**
- **Master-kamera:** mindkettő. A Cam_04 a fejvéget és az északi gardróbfalat mutatja, a Cam_11 a panorámát.
- **Ágy:** a terv szerinti helyen, y 6,40-en, a két éjjeli dugaljcsoport között („ahogy szerinted jó”). A promptok így írják. A Blender-modell bútorrétegében még 6,00 van, ezt a draft PR #15-ben javítom; a lockot nem érinti, mert a bútor nincs benne.
- **Brisia:** választhattam helyette. A Brisia család függesztett változata lett: 1 gömb Ø50, drótos, E27, Ø97 mm-es nyílás, Kave L00152CR05, 287,10 € (akciós). Az ML04-ről lóg, az asztalközéptől kb. 0,20 m-re.
- **Olvasólámpák:** designosak legyenek, és férjen beléjük Hue-izzó.
  - S01: Kave Raze (bézs márvány + vászonbúra, H54, E27, 89,99 €);
  - S02: Kave Aleyla, bordó (gombalámpa, H33, E14, 79,99 €).
  - Mindkettő elfér a 30 × 30-as éjjeliszekrényen, és dugasszal a D20–D23-ba csatlakozik.
- **Kave-adatok:** Péter kérésére (23:39) a Kave-oldalt a böngészőben olvastam. A 4 lámpa foglalata és a 3 új termékkép innen van.

**Nyitva:**
1. **PR #15 beolvasztása** („mehet”): kell a 13–16. csomaghoz (Cam_11).
2. **Kanapé:** a 10 stílusból csak az S06 és az S10 Kave-kanapés. A 2–3. adag előtt cserélhetünk Kave-re (Gala U, Martina íves + Neom puff, Vera, Blok).
3. **Hétfői mérés:**
   - az erkély északi vége (a fotón téglafal, a modellben korlát);
   - az üvegfal-osztás (modell 0,90/0,90/1,84 m);
   - a kültéri lámpák foglalata;
   - a 06.2 szaniter-render-réteg javítása (külön feladat).
4. **A 2–3. adaghoz:**
   - stílusonkénti gardróbfront (S03–S10);
   - stílusonkénti olvasólámpa, Hue-kompatibilis;
   - a **Novae** (S05, S08) beépített LED-es, ezért cserélni kell Hue-kompatibilis fürdőlámpára. Az Ardali, a Madali és a Drava rendben van (Drava: E14).
   - K8: Eamy barna, Ciselia bézs, Corvena méretei. A méretrajzok megvannak.

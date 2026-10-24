# Gemini / Flow image-to-video benchmark – A902 Lake Forest nappali

> **KONCEPCIÓ ALAPÚ VIDEÓTESZT – NEM KIVITELEZÉSI BIZONYÍTÉK** (`ai-coordination/RENDER_REALITY_GATE.md` E. pont). Modell-összehasonlító benchmark nem validált ChatGPT-renderből. A videók nem mutatnak igazolt anyagot, terméket vagy geometriát.

- **Dátum:** 2026-10-24, 04:30–04:42 (Budapest)
- **Végezte:** Claude (Chrome-on át, Google Flow felület), Péter jóváhagyásával
- **Fiók:** peter.kapusi88@gmail.com, Google AI **PLUS** (a felület szerint napi +50 Flow-kredit)
- **Flow-projekt:** „okt. 24 – 04:30” (flow.google.com, /u/1/)
- **Forráskép:** `04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png` (1586×992 px, 2 965 052 bájt; a GitHub-változat és a helyi tükör mérete egyezik)
- **Prompt:** `05_promptok/A902_LakeForest_1_nappali_video_prompt_v1.md`. Mindhárom futásnál szó szerint ugyanaz, egy bekezdésbe fűzve.
- **Mód:** Flow → Videó → **Képkockák** (a forráskép mint *Kezdet* képkocka), Ügynök kikapcsolva, 16:9, ×1 generálás
- **Render státusza:** koncepció. A videó nem költségelt és nem kivitelezhetőségi bizonyíték.
- **Veo 3.1 Quality:** NEM futott (Péter utasítása).

## 1. Kreditfogyasztás (ellenőrzött, a Flow fiókpaneljéről leolvasva)

| # | Modell (Flow-név) | Előtte | Felület szerinti költség | Utána | Tényleges levonás | Hossz | Felbontás |
|---|---|---:|---:|---:|---:|---|---|
| 1 | Omni 1.1 Flash (Gemini Omni Flash) | 250 | 10 | 240 | **10** | 6 mp (6,016 s) | 1280×720 |
| 2 | Veo 3.1 – Lite | 240 | 10 | 230 | **10** | **8 mp** (fix) | 1280×720 |
| 3 | Veo 3.1 – Fast | 230 | 20 | 210 | **20** | **8 mp** (fix) | 1280×720 |
| | **Összesen** | **250** | | **210** | **40** | | |

Bizonyítékok: `04_renderek/ai_video_tests/A902_LakeForest_1_nappali_videoteszt_kredit_elotte_250.png` és `…_kredit_utana_210.png`.

**Eltérések a kért tesztelrendezéstől**
- A Flow-ban a **Veo 3.1 Lite és Fast nem kínál hossz- és felbontásválasztót**: fixen 8 mp és 720p. 6 mp csak az Omni Flash-nél választható (4/6/8/10 mp, 360p/720p). A Veo-videókat ezért 8 mp-ként kaptuk. A pontozás a teljes 8 mp-et és külön az első 6 mp-et is nézte. A Lite első 6 mp-e geometriában valamivel tisztább, mert a kitalált lamellás fal 7 mp után jelenik meg. A Fast már 3–4 mp-nél eltér, ott a 6 mp-es vágás nem segít.
- A forráskép **16:10** arányú (1586×992), nem 16:9. A Flow középre vágta: fent és lent kb. 50–50 px veszett el (≈10% magasság). Az első képkocka mindhárom modellnél a középre vágott forráshoz illeszkedik a legjobban (átlagos abszolút eltérés 8,9–9,7 / 255). Ez tónus- és részletbeli eltérés (újragenerált első kocka, tömörítés), a geometria az első kockán azonos.
- **Veo Quality ára:** a táblázatban szereplő 100 kreditet a felületen **nem ellenőriztem**, mert nem választottam ki a modellt.
- **Modell-azonosítás:** a Flow szerkesztőnézete nem írja ki a generáló modellt. Az Omni egyértelmű, mert csak az 6 mp-es. A Lite és a Fast az indítási sorrendből azonosítható: a Lite elkészült, amikor a Fast még kb. 15%-on állt.

## 2. Mentett fájlok

| Fájl | Méret | Hely |
|---|---:|---|
| `A902_LakeForest_1_nappali_omniflash_6s_720p.mp4` | 3 941 315 B | `04_renderek/ai_video_tests/` |
| `A902_LakeForest_1_nappali_veo31lite_8s_720p.mp4` | 5 893 584 B | `04_renderek/ai_video_tests/` |
| `A902_LakeForest_1_nappali_veo31fast_8s_720p.mp4` | 8 757 915 B | `04_renderek/ai_video_tests/` |
| `A902_LakeForest_1_nappali_videoteszt_attekintes.jpg` | 257 KB | mind a 3 modell 0/2/4/6/8 mp-nél, a forrással |
| `…_videoteszt_{omniflash,veo31lite,veo31fast}_kockak.jpg` | ~0,5 MB/db | modellenként 8 képkocka + forrás |
| `…_videoteszt_{omniflash,veo31lite,veo31fast}_reszlet.jpg` | ~0,5 MB/db | nagyított forrás ↔ 3 képkocka |
| `…_videoteszt_kredit_elotte_250.png`, `…_kredit_utana_210.png` | kicsi | a Flow fiókpaneljének kivágása (kreditbizonyíték) |

Mindegyik a `04_renderek/ai_video_tests/` mappában van, a GitHubon és a helyi tükörben (`~/Downloads/wsg-berendezes/`) is. Kivétel a két kredit-PNG: ezek csak a helyi tükörben vannak, mert a webes feltöltő ezeket nem érte el. A Flow-ból letöltött eredeti MP4-ek a Mac `~/Downloads/` mappájában is megvannak (Chrome alapértelmezett letöltési helye). Minden fájl GitHub-kompatibilis méretű (< 25 MB).

## 3. Vizsgálati módszer

1. Mindhárom MP4 visszajátszva és **12 kép/mp-es mintavétellel** végigléptetve, a forrásrenderrel egy rácsban összevetve (0–8 mp).
2. **Első kocka ↔ forrás:** átlagos abszolút szürkeárnyalat-eltérés 160×90 px-en, a legjobb vágás kereséssel.
3. **Mozgásfolytonosság:** egymást követő kockák eltérése (átlag / max). Ugrásra, vágásra, villogásra utaló kiugrást kerestem.
4. **Kameramozgás becslése:** a t. kocka és a 0. kocka közötti nagyítás és eltolás (>1 = előre/zoom, <1 = hátra/kitágul). Parallaxis miatt csak tájékoztató érték.
5. Geometriai elemenkénti vizuális ellenőrzés: falak, ablakok/teraszajtók, mennyezet, kanapé, fotel, dohányzóasztal, TV-fal, csillár, függönyök, terasz és kilátás.

| Modell | Első kocka MAE | Kockaváltás átlag / max | Becsült nagyítás a végén | Mozgás iránya |
|---|---:|---|---:|---|
| Omni 1.1 Flash | 9,7 | 4,2 / 6,6 | ≈1,12 (6 mp) | lassú **előre**, enyhe oldalra |
| Veo 3.1 Lite | 9,2 | 4,9 / 7,3 | ≈0,93–0,96 (6 mp) | **balra pásztázás + enyhe hátrálás** |
| Veo 3.1 Fast | 8,9 | 8,7 / 13,6 | ≈0,69 (8 mp) | **nagy jobbra kocsizás / fordulás** az ablak felé |

Egyik videóban sincs vágás, ugrókocka vagy villogás. A Fast nagyobb kockaváltási értéke a gyors, nagy kameramozgásból adódik, nem hibából.

## 4. Geometriai eltérések (forrásrenderhez képest)

### Omni 1.1 Flash (6 mp)
- **Jobb oldali áttetsző függöny:** kb. 1,5 mp-től széles, lebbenő függönylappá nő, és eltakarja a jobb szélső üvegmezőt, valamint a fekete ablakkeret jobb szélét. A forrásban csak keskeny sáv. *Közepes eltérés.*
- **TV-fal:** a forrás bal szélén éppen látszó sötét TV-felület a 16:9 vágás miatt már az első kockán kiesik, és később sem jelenik meg. Ez nem átalakítás, de **a TV-fal nem látszik a videóban.**
- Kanapé (forma, párnák száma), fotel, márvány-sárgaréz dohányzóasztal, csillár, festmény, állólámpa, ablakosztás, terasz-jakuzzi, olajfa, budai/parlamenti kilátás: **változatlan.** A dohányzóasztal a végén a perspektíva miatt oválisabbnak látszik, ez nem formaváltozás.
- Új tárgy, ember, szöveg: nincs.

### Veo 3.1 Lite (8 mp)
- **Kameraút ellentétes a prompttal:** előre helyett balra pásztáz és kissé hátrál, ezért a forráson kívüli részeket talál ki.
- **TV-fal:** feltárja a bal falat. Fekete, fali TV és világos tölgy alacsony szekrény LED-csíkkal jelenik meg; ez összhangban van a forrás bal szélével. 7–8 mp-nél azonban a TV mögött **függőleges világos tölgy lamellás/panelburkolat** jelenik meg, ami a forrásban nem látszik. *Kitalált, nem ellenőrizhető elem.*
- **Csillár:** 5–8 mp között az ágak és gömbök elrendezése enyhén átrendeződik, kis morfolódás. *Kis–közepes eltérés.*
- **Mennyezet:** a bal falnál rejtett világítású mennyezeti sáv/árnyékvonal tűnik fel. *Kis eltérés.*
- **Jobb oldali függöny:** az Omnihoz hasonlóan kiszélesedik.
- **Kilátás:** a Duna-sáv a végére szélesebb lesz. *Kis eltérés.*
- Kanapé, fotel, dohányzóasztal, festmény, állólámpa, terasz-jakuzzi: **változatlan.**

### Veo 3.1 Fast (8 mp)
- **Kameraút:** több méteres jobbra kocsizás és fordulás az ablak felé. Ez messze több a kért ~40 cm-nél, és a 3. mp-től nagyrészt **kitalált tér**.
- **Új fal- és padlószakasz** az ablaktól jobbra, valamint **nehéz, padlóig érő taupe sötétítőfüggöny**, amely a forrásban nincs.
- **Ablakosztás:** további tolóajtó-keretek és osztások jelennek meg, az üvegfal ritmusa megváltozik.
- **Terasz:** a jakuzzi elé **fa lépcső/dobogó** kerül, ami a forrásban nincs.
- **Kanapé:** a chaise longue vége lekerekített sarokelemmé alakul, a párnák átrendeződnek.
- **Eltűnő tárgyak:** a dohányzóasztal, a fotel, a puff és a csillár kimegy a képből. A szekrény és a TV-fal nem látszik.
- **Mennyezet:** a belmagasság-hatás alacsonyabbnak tűnik.
- Önmagában szép, filmszerű felvétel, de **nem az A-902 nappali**.

### 4.1 Render Reality Gate – videó-eltéréslista (C. pont)

A forrás maga sem validált: ChatGPT-koncepció, reality card nélkül. Ezért a lenti „döntés” oszlop csak azt mondja meg, hogy a videó **a forrásképhez képest** hű-e. A valós lakáshoz való megfelelést nem állítja.

| Elem | Forrás / azonosító | Tervezett valós felület | Képen látott (videó) | Eltérés | Ft-kockázat | Bizonyíték | Döntés |
|---|---|---|---|---|---|---|---|
| Padló | ChatGPT-render | meglévő Egger szürke tölgy (SKU nem igazolt) | világos/meleg tölgy már a forrásban, mindhárom videóban azonos | a forrás eltér a valóstól; a videók nem rontják | nem árazott (cserét nem tervezünk) | `_kockak.jpg` | FAIL a valósághoz, videótesztként elfogadott |
| Falak | ChatGPT-render | meglévő fehér | krém/greige a forrásban és mindhárom videóban | fény- vagy festéshatás, nem igazolt | ha valódi festés: nem árazott tétel | `_kockak.jpg` | nem igazolt |
| Ablakok, teraszajtók, keret | brosúra / forrásrender | meglévő fekete keretes üvegfal | Omni, Lite: azonos osztás; **Fast: új tolóajtókeretek, osztásváltás** | Fast: kitalált geometria | – | `veo31fast_kockak.jpg` 4–8 mp | Fast: FAIL |
| Mennyezet, belmagasság | forrásrender | meglévő | Lite: rejtett világítási sáv tűnik fel; Fast: alacsonyabbnak hat | kis (Lite) / közepes (Fast) | süllyesztett mennyezet a gate szerint tiltott | `_reszlet.jpg` | Lite: figyelmeztetés; Fast: FAIL |
| TV-fal | forrás bal széle | ismeretlen (nincs reality card) | Omni: nem látszik; Lite: TV + tölgy szekrény, **7 mp után lamellás tölgy falburkolat** | Lite: kitalált falburkolat | ha megtartanánk: nem árazott asztalos-/burkolattétel | `veo31lite_reszlet.jpg` 7,95 mp | nem igazolt |
| Kanapé | AI-render, termék nincs | nincs kiválasztva | Omni, Lite: azonos; **Fast: a chaise vége lekerekített modullá alakul** | Fast: objektummorfing | – | `veo31fast_kockak.jpg` | Fast: FAIL |
| Csillár | AI-render, termék nincs | nincs kiválasztva | Omni: azonos; **Lite: ágak/gömbök enyhén átrendeződnek** | Lite: kis morfing | – | `veo31lite_reszlet.jpg` | figyelmeztetés |
| Függönyök | AI-render | nincs kiválasztva | Omni, Lite: a jobb oldali voile kiszélesedik; **Fast: új, padlóig érő taupe sötétítő** | Fast: új tárgy | nem árazott | `_kockak.jpg` | Omni, Lite: figyelmeztetés; Fast: FAIL |
| Terasz, kilátás | forrásrender | valós panoráma (nem igazolt) | Lite: szélesebb Duna-sáv; **Fast: fa lépcső/dobogó a jakuzzi előtt, kitalált kilátásrészlet** | Fast: kitalált geometria | – | `veo31fast_kockak.jpg` | Fast: FAIL |
| Kameramozgás | prompt: ~40 cm előre | – | Omni: előre (OK); Lite: balra és hátra; Fast: több méteres jobbra kocsizás | Lite, Fast: promptsértés | – | 3. pont táblázata | – |

**Videóstátusz:** Omni → `KONCEPCIÓ – NEM VALIDÁLT` (a forráshoz hű). Lite → `KONCEPCIÓ – NEM VALIDÁLT`, figyelmeztetésekkel. Fast → `FAIL / ÚJRATERVEZÉS` (kitalált geometria).

## 5. Pontozás (1–10; „Videóhibák”: 10 = nincs hiba)

| Modell | Hossz | Kredit | Geometria hűsége | Luxushatás | Mozgás minősége | Videóhibák | Összbenyomás |
|---|---|---:|---:|---:|---:|---:|---:|
| **Omni 1.1 Flash 720p** | 6 mp | 10 | **8** | 7 | **7** | **7** | **7,5** |
| Veo 3.1 Lite | 8 mp (fix) | 10 | 7 | **8** | 5 | 7 | 7 |
| Veo 3.1 Fast | 8 mp (fix) | 20 | 3 | **8** | 4 | 4 | 4 |
| Veo 3.1 Quality | 8 mp | 100 (nem ellenőrzött) | – | – | – | – | nem futott |

**Pontozási indoklás röviden**
- **Omni:** az egyetlen, amelyik a kért irányban (előre) és nagyságrendben mozog, a bútorzat és az architektúra végig megmarad. Gyengeségei: a függöny túlmozog, és a mozgás inkább zoomszerű, kevés a parallaxis.
- **Lite:** a leggazdagabb térélmény (TV-fal, szekrény, mélység), egyenletes mozgás. Rossz viszont az irány, és kitalált falburkolat jelenik meg, ami geometriai kockázat.
- **Fast:** a legfilmszerűbb, de a geometria-megőrzés a projekt fő szabálya, és ezt sérti: új fal, függöny, terasz-lépcső jelenik meg, és megváltozik a kanapéforma.

## 6. Ár/érték: összbenyomás-pont / 10 kredit

| Modell | Összbenyomás | Kredit | Pont / 10 kredit |
|---|---:|---:|---:|
| **Omni 1.1 Flash** | 7,5 | 10 | **7,5** |
| Veo 3.1 Lite | 7 | 10 | 7,0 |
| Veo 3.1 Fast | 4 | 20 | 2,0 |

**Eredmény:** az **Omni 1.1 Flash 720p** adja a legjobb minőséget a felhasznált kreditekhez képest, és abszolút értékben is ez a leghűbb a geometriához. A Veo Lite második, és csak akkor érdemes rá, ha a lakás egy rejtett részének „feltárása” kifejezetten kell; ilyenkor az eredményt geometriailag külön ellenőrizni kell. A Veo Fast ehhez a feladathoz nem alkalmas.

**Korlát:** modellenként egyetlen generálás (n = 1). A modellek sztochasztikusak, ezért ez irányadó, nem statisztikailag igazolt sorrend. A valós idejű visszajátszás élményét Péternek érdemes saját szemmel is megnéznie.

## 7. Javaslat a következő lépésre (nem indítva, Péter dönt)

1. **Veo 3.1 Quality (≈100 kredit, nem ellenőrzött ár):** csak akkor indítanám, ha a Lite/Fast mintázata (kitalált tér, nem követett kameraút) a Quality-nél is megmarad, mert akkor sem lesz a jelenlegi szabályok szerint használható. 100 kredit = 10 Omni-futás. **Javaslatom: most ne.** Előbb 2–3 további Omni-futás (20–30 kredit) a szórás méréséhez.
2. **Promptjavítás Omnihoz:** a függönymozgást korlátozni („curtains: barely perceptible movement, keep right sheer panel at its original width”), és a TV-falat a képkivágásban tartani, vagy előre 16:9-re vágni úgy, hogy a bal szél megmaradjon.
3. **Végkép (Vége) képkocka:** a Flow engedi a kezdő és a záró képkocka megadását. Ha Blenderből előre kiszámolt, ~40 cm-rel beljebb álló kamera végképét adjuk meg, a modell nem tud tetszőleges teret kitalálni. Ez a geometriahűség legerősebb kontrollja.

## 8. Átadás / státusz

- Felület: **Google Flow** (flow.google.com). Ugyanaz a Google AI-előfizetés és kreditkeret van mögötte, mint a Gemininek, de itt modellenként választható a beállítás, és látszik a kreditköltség.
- Semmilyen extra kredit vagy előfizetés nem lett vásárolva. A Flow első használatakor Péter elfogadta az adatvédelmi tájékoztatót; a feltöltéskor megjelent „kép használatára vonatkozó jogok” megerősítést Claude fogadta el a forrásrender feltöltéséhez.

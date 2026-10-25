# KEP-004 · V3_TEST – integrációs napló (r2-csomag, S01 és S02 Cam_02)

**Készítette:** Claude, 2026-10-25. A két `_V3_TEST` prompt fejléce erre a fájlra hivatkozik.

**Jóváhagyás (Péter):**
- **01:55 CEST:** V3 azonnali képteszt két képpel.
- **02:22 CEST:** „1. opció” – ez a munkamenet az egyetlen felelős; „MEHET pontosan két ChatGPT Images-generálás … egy-egy kép”.

**Eredmény:** két kép, képenként egy generálás. Gate-audit: `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`.

## 1. Források

| Forrás | Hely | Azonosító |
|---|---|---|
| Astra Creative Upgrade V3 r1 – S01/S02 Cam_02 kreatív blokk, falkezelés, költségmodell | draft PR #16, ág `astra/creative-upgrade-v3-r1-20261025`; `05_promptok/A902_S01_S02_Cam02_CREATIVE_UPGRADE_V3_r1.md`, `ai-coordination/results/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_r1.md` | commit `be6b1f3` (nincs beolvasztva) |
| Geometria v2 – FRAME LAYOUT, P902_24A | `05_promptok/KEP004_ChatGPT_Images_v2_geometria/Cam02_GEOMETRIA_v2.md` | `main` |
| A másik munkamenet r1-csomagja (a kiindulás) | `05_promptok/KEP004_ChatGPT_Images_V3_teszt/` | S01 r1 `8a26bfad…45ce` (18 957 kar.), S02 r1 `03966065…785f` (19 275 kar.) |
| Javított V3-tömbkép (1b) | `04_renderek/A902_cam02_tomeg_V3TEST/` | S01 `ed70d29e…`, S02 `b78dd073…` |
| Blender-modell és lock | v2b-1-k11b, a `main` másolata | .blend `9875cd57…` (változatlan), lock `7aa85d70…` |
| Kiállások, validátor | `A902_villamos.json` (130 kiállás), `geometry_validator_v2.py` | `f881dcce…`, `b7d7f6a6…` |

## 2. A generálás előtti ellenőrzés

### 2.1 A V3 kreatív blokkok
- Mindkét stílusblokk szó szerint került a promptba. Kivétel a „Light” bekezdés tesztváltozata, és az alábbi, műszakilag indokolt sorok (3. pont).
- **Falfelület-kivétel:** csak a kijelölt W01–W04 kaphat tapétát, felületi panelt és bútorfrontot.
  - A mennyezet, a fehér keretek, a káva, a szervizfedlapok, a padló és a terasz változatlan.
  - Ellentmondó mondat nem maradt: a régi „painted white, smooth” és „keep the upper wall mostly empty” tiltólistán van, egyik prompt sem tartalmazza.
- **Világítás (Péter, 02:22):** a V3.1 rejtett LED-jét nem kell megvárni. A teszt LED nélkül készül; ez nem tilalom, és a hiánya kreatív hibának sem számít.
  - Mindkét promptban azonos a nappali fény mondata.

### 2.2 TV-szekrény és magas tároló – V3-méretek a régi tömbök helyett
A régi Cam_02-tömbkép (`04_renderek/A902_cam02_tomeg_v1/A902_Cam02_tomeg_P902_24A_v1.png`) 180 × 45-ös konzolt és 65″-os TV-t mutatott. A V3 más méretű szekrényeket ír elő, ezeket új tömbként építettem be.

| Elem | V3 r1 (Astra) | Tömb (x × y × z, m) | Megjegyzés |
|---|---|---|---|
| KI3-L alsó szekrény | 240×48×40 | 3,67–4,07 × 5,15–7,55 × 0–0,48 | 4 × 60-as front; kivehető szervizhátfal (D16/D17/G08) |
| KI3-V magas szekrény | 60×220×30 | 3,67–3,97 × 4,35–4,95 × 0–2,20 | a D18 a legalsó rekesz hátfalán át érhető el |
| KI3-P TV-háttér | két sík, összesen 260×190, ≤ 4 cm | 3,67–3,71 × 5,05–7,65 × 0,55–2,45 | **egy befoglalóként.** A régi V3-tömbkép (`…_tomeg_S01_V3_v1.png`) a két sík osztását a TV közepe mögé tette; ezt kivettem. Az osztás helyét a stílusblokk adja |
| BN3-L alsó szekrény | 240×50×40 | 3,67–4,07 × 5,25–7,65 × 0–0,50 | 4 × 60-as front, kivehető hátfal |
| BN3-V magas szekrény | 90×220×32 | ajtós oszlop: y 4,25–4,70; tükörmező: y 4,70–5,15, z 0,40–2,20; szervizlap alatta z 0–0,40 | **A tükör a TV-panel felőli oszlopba került.** A D18 (y 4,749; z 0,30) így a szervizlap mögé esik, és onnan elérhető |
| BN3-P TV-háttér | 240×190 | 3,67–3,71 × 5,25–7,65 × 0,55–2,45 | – |
| TV | 65″ | 5,625–7,075 × 0,85–1,68 | tengely y 6,35, a D16/D17 előtt |

### 2.3 Tömbkép, validátor, távolságok
- Szkript: `03_blender/geometry_v2/tomeg_cam02_v3test/01_tomeg_cam02_v3test.py` (+ `tomeg_lib.py`).
  - A .blend egy másolatán futott, mentés nélkül. Az élő Blender-jelenethez nem nyúlt.
- **Validátor:** üres PASS 0/0 · S01 PASS 0/8 · S02 PASS 0/9.
  - Ütközés bútor és fal/nyílászáró/ajtólendület között: 0. Bútor–bútor átfedés: 0. Kapcsolót semmi nem takar.
  - Részletek: `03_blender/validator_report_2026-10-25_V3TEST_tomeg_cam02.md`.
- **Távolságok** (`tomeg_cam02_V3TEST_log_v1.json`):
  - TV-tengely 6,35, kanapétengely 6,40; nézőtáv 2,93 m;
  - az S01 L-kanapé 0,46 m-re, az S02 U 0,225 m-re van az üvegtől;
  - kanapéhát – nyugati széktámla: **0,38 m (S01) / 0,36 m (S02)** – ez a P902_24A elfogadott tűrése, nyitott döntés.

### 2.4 A tükörkép levezetése (S02)
- Helyzet:
  - a tükör síkja x = 3,99 (a BN3-V előlapja); a tükörmező y 4,70–5,15, z 0,40–2,20;
  - a kamera: [8,30; 4,40; 1,55].
- A kamera tükörképe [−0,32; 4,40; 1,55]. A tükörbe érkező sugarak visszavert ága kelet felé, kissé északra halad: x = 8,30-nál y ≈ 5,0–5,9, a keleti részen y ≈ 5,1–6,2.
- **A tükörben tehát belső tér látszik:** a U déli karja, az étkezőszékek, az üveglap éle, a keleti fal, a mennyezet és egy világosszürke belső ajtó éle.
- **Kilátás, ablak, égbolt vagy maga a kamera nem látszhat.** A prompt mondata így szól: „…only what it can physically reflect … never the exterior view, the skyline, a window or the camera.”

### 2.5 A kültéri pad
- A KI-O és a BN-O padnak nincs ellenőrzött helye, ezért nem jelenik meg.
- Mindkét promptban szerepel: „No terrace furniture is shown in this test image.” Az S02 karfatálcája (25 × 35) marad.

### 2.6 A referenciafájlok azonossága
Ellenőrző szkript: `tisztit.py`, eredménye a munkamenet bemenet-ellenőrzésében. A sha-k: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/archiv_manifest_V3_TEST.json`.

- **Mind a 18 csatolmány** (2 × 9) pixelre azonos a forrásával.
- **C2PA-bélyeg:**
  - A munkamenet fájlátvitele automatikusan C2PA-bélyeget tesz a fájlokra (JPEG APP11, 5769 B). A pixeleken ez nem változtat.
  - A csomagból leválasztottam, így a ChatGPT a forrásfájllal bájtra azonos képet kapott.
  - Érintett fájlok: helyszíni lap, Lennon, Toni, JÄTTEBO, Anouk, Eamy, Nifelia, Ciselia, Marely.
- **A v1-nyilvántartás (`KEP004_ChatGPT_Images_v1/_eszkozok/csomag_nyilvantartas.json`) sha-jával egyezik:**
  - alapkép, padló (ME-BAL-080), helyszíni lap, panoráma;
  - Lennon, Toni, JÄTTEBO, Anouk.
- **Eltér a v1 kivágásától a négy Kave-fotó** (Eamy, Nifelia, Ciselia, Marely):
  - ezek az r1-csomagban már új kivágásként szerepeltek;
  - a terméket szemrevételezéssel azonosítottam: Eamy kőris héj + világosszürke ülés + fekete láb; Nifelia bézs, barna végcsíkkal; Ciselia bézs zsenília + fekete láb; Marely fehér gyapjú.
- **Tömbképek:** az 1b képek ezek a javított V3TEST-tömbképek (S01 `ed70d29e…`, S02 `b78dd073…`), nem a régi V3-tömbképek.
- **Egyezés a futtatott prompttal:** a ChatGPT-mezőbe került szöveg küldés előtt karakterre egyezett a prompt-fájllal (a záró sortörés nélkül). A 9 csatolmány a fájlnév szerinti sorrendben (01 → 09) került fel.

## 3. r1 → r2 változtatások
Eszköz: `_eszkozok/epito_r2.py`. Napló: `epites_r2_naplo.json`. Diff: `*_r1_r2.diff`.

| # | Mi | r1 | r2 | Ok |
|---|---|---|---|---|
| 1 | Kép-ID, verzió | `_V3_r1`, KEP004-CGI-V3TEST-r1 | `_V3_TEST`, KEP004-CGI-V3TEST-r2; hivatkozás erre a fájlra | új, felülírásmentes azonosító (Péter: „új mappába, régi képeket ne írj felül”) |
| 2 | Jóváhagyás | 02:06, egy kép | 02:22, pontosan két kép (S01 + S02), képenként egy | Péter 02:22 |
| 3 | Nyílászáró, padló, terasz | – | új sorok: üvegezés pontosan az 1. kép szerint, a padló a 2. kép szerint, 6 cm-es szegőléc; a terasz pontosan az 1. és a 2b kép szerint, terasz-bútor nélkül | Péter 02:22: „az eredeti geometriát, nyílászárókat és padlót őrizd meg” |
| 4 | Helyek | „javasolt, Claude ellenőrizze” | „ellenőrizve – v2b-1-k11b, validátor PASS, 1b”; a D18 hozzáférése | a 2.2–2.3 pont szerint ellenőrizve |
| 5 | S02: a BN3-V két oszlopa | egy mondat | az ajtós oszlop a kép 0–10 %-án, a tükör 10–17 %-án (magasságban 25–71 %); alatta zárt szervizlap | a tömbkép és a D18 szerint |
| 6 | S02: tükör | „…real visible architecture and the actual exterior view” | csak a fizikailag lehetséges belső tér; soha nem a kilátás, az égbolt, ablak vagy a kamera | Péter 02:22; a 2.4 pont levezetése. Az r1-kép tükre lehetetlen teraszképet mutatott |
| 7 | Kültéri pad (KI-O / BN-O) | „az elfogadott helyén” | nem jelenik meg (nincs ellenőrzött hely); a karfatálca marad | Péter 02:22 |
| 8 | Bemenetek | „Claude to assemble… selected V3 samples” | pontosan a csatolt 9 kép; anyagmintakép nincs, az anyagok szövegből | a valóban csatolt fájlok; minta még nincs kiválasztva |
| 9 | Kimenet | `CREATIVE_UPGRADE_V3/…_V3_r1.png` | `V3_TEST/…_V3_TEST.png` | felülírás kizárva |
| 10 | 1b jegyzet | – | S01: a KI3-P egy befoglaló. S02: a világos mező a tükör, a sötét az ajtós oszlop, alatta a szervizlap | a tömbkép olvasása |
| 11 | Nappali fény | stílusonként eltérő mondat | azonos mondat mindkét promptban: semleges, borult nappali fény, közvetlen nap és belső világítás nélkül | Péter 01:55: azonos nappali fény |

**Ellenőrzés:**
- tiltott kifejezés 0 találat: 17 elem, köztük „02:06”, „approved position”, „Claude must verify”, „_V3_r1”, „actual exterior view”, „painted white, smooth”;
- kötelező elem mind megvan (S01: 10, S02: 12).
- Az Astra stílusblokkjának többi része szó szerinti.

## 4. Fájlok
- **Promptok, ahogy futottak:**
  - `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_TEST.prompt.txt` – `eb4f1908…970c`, 20 238 karakter;
  - `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_TEST.prompt.txt` – `aea9d602…7f16`, 21 327 karakter.
  - A kép mellett is megvannak: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/`.
- **Építés:** `_eszkozok/epito_r2.py`, `epites_r2_naplo.json`, `*_r1_r2.diff`.
- **Gate-eszközök:** `_eszkozok/gate_atfedes.py`, `osszevetes_lapok.py`, `reszlet_lap.py`, `kontrollpont_lapok.py`.
- **A csatolandó képcsomagok** csak a Macen vannak: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/V3_TEST_r2_2026-10-25/`. A termékfotók miatt nem kerülnek a repóba.

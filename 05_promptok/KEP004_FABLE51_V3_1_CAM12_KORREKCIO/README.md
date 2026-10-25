# Cam_12 v3 korrekció – Fable 5.1 S01/S02 (Claude integrátor, 2026-10-25)

**Kiváltó ok:** a Fable 5.1 S01 és S02 Cam_12 promptjaira a ChatGPT Images **GEOMETRIA FAIL**-t adott.
- Hátsó falas konyhát talált ki szigettel, és elmozdította a W02 falat.
- Elhagyta a 05.3 szürke ajtót, és kitalált egy közlekedőnyílást.

**Státusz:** a semleges alap geometriailag **PASS**; a tömbök és a csomag **KONCEPCIÓ – NEM VALIDÁLT**.
- Képet nem generáltam. A ChatGPT-hez és a Chrome-hoz nem nyúltam.
- A versenyzők ágait, promptfájljait, a `main`-t és a PR #22/#23-at nem módosítottam.

## 1. Mi volt valójában az „image 1” – ellenőrizve
| | Érték |
|---|---|
| fájl | `04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png`, 1600 × 1000, RGBA |
| SHA256 | `66a9c6af6992721226174fcc62563de0f34160263ad19dde82bc2d4bc3a1d87e` – **egyezik** a megadottal (a repóban és a Macen is) |
| készítő ág | `kep004/kameracsomag-C-K1` (draft PR #20, f190e5f), innen került a `competition/baseline-20261025-v3` (45632b5), a `fable51` és a többi versenyág alá |
| forrás-blend (PNG-metaadat) | `/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12C_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k13_KAMERACSOMAG_C.blend`, scene `WSG_A902`, kamera `Cam_12_Nappali_Hero`, 2026-10-25 04:23:53 |
| blend sha | `e01170d315193f8785bbeee5f7d319ce3c8adec886375962cee83e0a3f70ddbd` – azonos a repó `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` fájljával a fenti ágakon. **A `main` blendje ettől eltér** (régebbi, k13 előtti). |
| lock | `geometry_lock_A902_v2b.json` v2b-1-k13, sha `2ca93735…3d1b` |
| szkript, riport | `03_blender/geometry_v2/cam12_C/04_ellenorzes_C.py`; `03_blender/validator_report_2026-10-25_v2b1k13_kameracsomag_C.md` |
| render | EEVEE, 128 minta; **lámpák kikapcsolva**, csak egyenletes világ-háttérfény (0,86/0,88/0,92), expozíció 0,75 |

**Megjegyzés:** a `kep004/cam12-nappali-hero-javaslat` (e16ee77) a **v2** Cam_12-t tartalmazza ([3,95; 7,90; 1,45], θ −45°, shift −0,08). Az nem a v3, nem azt küldtük.

**Miért hagyta figyelmen kívül a modell:** egyenletes, irány nélküli fénynél minden fehér fal szinte azonos tónusú. A falélek, a mellvéd, a szemöldök és a mennyezetvonal alig válik el. A képmodell így „üres fehér dobozt” kap, és a szöveg alapján újrarajzolja a teret.

## 2. A v3 kamera ellenőrzése a `GEOMETRIA_C_KAMERACSOMAG_v2.md` ellen
A méréshez a blend másolatát nyitottam meg (Blender 5.2.3): `naplok/probe_masolat_blend.json`, `naplok/cam12v3_korr_log.json`.

| Paraméter | v2 dokumentum | lock k13 | blend (mért) | Eredmény |
|---|---|---|---|---|
| hely | [4,40; 7,88; 1,60] | [4,4; 7,88; 1,6] | [4,4; 7,88; 1,6] | ✔ |
| irány | θ −48° | rot [90°; 0; −138°] | előre-vektor (0,669; −0,743; 0) → −48,0° | ✔ (a rot_z −138° = θ − 90°) |
| dőlés | vízszintes | rot_x 90° | pitch 0,0° | ✔ |
| optika | 22 mm | 22 | 22,0; szenzor 36 × 24 AUTO → vízszintes látószög 78,6° | ✔ |
| shift_y | −0,05 | −0,05 | −0,05 | ✔ |
| felbontás | – | 1600 × 1000 | 1600 × 1000 | ✔ |

**Eltérés nincs.**
- Formai megjegyzés: a blend aktív kamerája `Cam_04_Master`, ezért a szkript renderkor a Cam_12-re vált.
- A validátor mind a 12 kamerát a lock szerint, 0 eltéréssel találta.

## 3. Új semleges alapkép és tömbrenderek
`04_renderek/A902_cam12_v3_korrekcio/`

| Kép | Fájl | SHA256 |
|---|---|---|
| semleges v3 KORR | `A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png` | `8ffd40c0…d231d` |
| S01 tömb | `A902_S01_Cam12v3_KORR_tombrender.png` | `03068ad6…3e8b` |
| S02 tömb | `A902_S02_Cam12v3_KORR_tombrender.png` | `9ee45aa5…c826` |
| dokumentációs képek | `…_JELOLT.jpg` (jelölt), `…_tomb_felulnezet.png` (felülnézet + utak), `A902_Cam12v3_KORR_osszevetes_regi_uj.jpg` | – |

**Mitől olvashatóbb (geometria- és kameraváltozás nincs):**
- **Fény:** EEVEE raytracing GI-vel. Nagy, 4,50 × 2,35 m-es nappali „ablakfény” az északi üvegfal belső síkján (220 W, a kamera mögött), gyenge mennyezeti derítés és 0,25-ös égbolt-háttér. Így a különböző irányú falsíkok eltérő tónust kapnak: a falélek, a szemöldökök, a mellvéd, a W02/W07 és a mennyezetvonal elválik.
- **Tónusok:** a falak fehérek maradtak (0,78). A mennyezet kissé világosabb (0,84). Az ajtólap világosszürke (0,47), a tok sötétebb (0,30), így a 05.3 nyílás kerete olvasható. A padló a modell parkettaanyaga.
- **A Cyclest elvetettem:** a lock egymásba lógó falhasábjai (pl. a W02 nyugati vége × a W07 10 cm-en) Cyclesben fekete csíkot adtak. Ez modell-higiéniai jelzés, nem méreteltérés.
- **Konyha a semleges képen nincs, mert a valóságban sincs** (056 fotó). A konyhai pultsor helyét az 1b tömbrender mutatja. A semleges kép a meglévő héj: a K-csonk, a K-pultfal, a mellvéd és a szemöldök.

**Validátor:** `03_blender/validator_report_2026-10-25_cam12v3_korrekcio.md`
- üres: **PASS 0/0**;
- S01 tömb: FAIL 5/15 – ebből 3 valós (kapcsolótakarás), 2 téves riasztás;
- S02 tömb: FAIL 10/17 – ebből 6 valós, 4 téves riasztás.

**Tételes tömblista és közlekedés:** `10_BLOKK_VALIDALAS.md`.

## 4. Fő találatok – ezekhez tulajdonosi vagy versenyzői döntés kell
1. **Hűtőoszlop a W03-a előtt (Fable S01/S02-ET-01):**
   - Takarja a K07–K09 étkezőkapcsolókat (y 5,65) és a D12-t.
   - A 05.3 ajtóhoz vezető utat 0,85 m-re szűkíti (cél 0,90).
   - Lehetőségek:
     - (a) a hűtő a konyhasorban marad, ahogy a korábbi C-próbában (a D13 hűtődugalj áthelyezése villanyszerelői munka);
     - (b) 45–50 cm-es oszlop, amely a kapcsolókat és az utat is szabadon hagyja, de hűtőtermék kell hozzá;
     - (c) a kapcsolók áthelyezése (bontás, villanyszerelő – a „nincs építés” szabály miatt Péter döntése).
2. **S02 tükörsáv (ET-02)** ugyanazokat a kapcsolókat fedi: kivágás vagy áthelyezés kell.
3. **TV és konzol magassága (S01, S02):**
   - 17 cm ütközés: a TV közepe ≥ 1,37 m-en legyen, vagy a konzol lejjebb.
   - A Cam_02-ben látszik, a Cam_12-ben nem.
4. **S02 Sheffield Ø80:** a JÄTTEBO U-ban nincs szabályos helye. Kisebb asztal kell.
5. **Kisebb pontatlanságok:**
   - S01 lintel: 1,10 vs 1,30 m;
   - S02 borda: 7 cm-rel a nyomat elé lóg;
   - nyugati pult: 5 cm-rel a mellvéd fölé lép;
   - S01 dohányzóasztal: a helye nincs megadva.
6. **Az elemlista:** a feladatban említett `40_ELEMLISTA_V3_1.csv` a Fable-ágon nincs, csak az Opus 5.5-én. A Fable saját spec-tábláiból dolgoztam.
7. **MODEL SOURCE ERROR (1 db):** a konyhai mennyezeti csőcsonk (kék kupak) hiányzik a modellből. A Cam_12-ből a szemöldök takarja. Lásd `20_FOTO_VS_MODELL.md`.

## 5. Fotó és modell összevetése
`20_FOTO_VS_MODELL.md`
- A falak, ajtók, a közlekedő és a konyha a 045, 046 és 056 fotón minőségileg egyezik a lockkal.
- Méretet a fotó nem igazol.
- A hiányzó csőcsonkon kívül nincs modellhiba.

## 6. A javított S01 tesztcsomag
`csomag_S01/` – fájllista, SHA-k és források: `csomag_S01/CSOMAG_LISTA.md`.
- **image 1:** új semleges render (kötelező geometria).
- **image 1b:** S01 tömbrender.
- **image 2:** parkettafotó (csak anyag).
- **image 3:** 046 helyszíni fotó (csak felületek, nem kamera).
- **Üzenet:** `csomag_S01/UZENET_S01_Cam12_v3_KORR.txt`.
  - Elöl: képszerepek, GEOMETRY LOCK, a fix elemek balról jobbra képszázalékkal (a Blender-vetítésből), tiltások, „pontosan egy kép”.
  - Utána a Fable-prompt szó szerint, bájtra azonosan.

## 7. Őszinte vélemény: tartja-e a ChatGPT Images a geometriát?
**Röviden: a javított referenciával valószínűleg jobb lesz, de megbízhatóan nem fogja tartani. A döntéshez és a végső fotórealisztikus képhez Blender-alapú út kell.**

Amit láttam és tudok:
- **A hiba egyik oka a referenciakép volt.** Az új kép élei, síkjai és nyílásai olvashatók, és ott van mellette a tömbkép is. Ez a durva elrendezést (merre van a konyha, hol az ajtó, hol a W02) várhatóan rendbe teszi.
- **A másik ok a modell működése, ezen a csomag nem segít.**
  - A ChatGPT Images a csatolt képet laza mintaként kezeli, nem kötött élvázként (nincs mélység- vagy élkényszer).
  - Egy 1600 × 1000-es, 22 mm-es nagylátószögű nézetnél 5–15 %-os elcsúszás várható: a W02 szélessége, a mellvéd magassága, az ajtó helye, a fal-padló vonal.
  - A 16:10-es arányt sem tudja pontosan.
  - A hosszú Fable-prompt („No kitchen exists… show an IKEA METOD kitchen”, sok anyagleírás) ráadásul a szöveg felé húzza a képet.
- **A tömbök maguk is mutatnak tervhibát** (hűtőoszlop, TV-konzol, Sheffield), ezért a „szép kép” itt egyébként sem lehet validált látványterv.

**Javaslat:**
1. **ChatGPT Images** csak hangulat- és anyagkutatásra, KONCEPCIÓ címkével. Ezt az egy csomagot érdemes lefuttatni tesztnek. Az eredményt élfedéssel kell összevetni az image 1-gyel (W02 élek, ajtótok, mellvéd, mennyezetvonal), és a 2 %-os képszélességnél nagyobb eltérés FAIL.
2. **Összehasonlító és végső kép: Blender.** Valós termékméretű proxyk és anyagok, Cycles/EEVEE render, opcionálisan **szerkezettartó image-to-image restyle** (mélység- vagy élvezérelt, alacsony erősséggel), majd ugyanez az élfedéses kapu.
   - Ez lassabb, de a geometria benne marad, és a Render Reality Gate-en átmehet.
   - Megjegyzés: ehhez a falhasábok átfedését Cycles előtt rendezni kell (render-másolatban, a lock változatlanul hagyásával).

## 8. Verziók
- Bázis: `main` @ `114988f`.
- Bemenetek:
  - `competition/fable51-v3-1-20261025` @ `b44541205cdd79e3d1f33ee8074c2bc280beb7a7`;
  - `kep004/kameracsomag-C-K1` @ `f190e5f`;
  - `competition/baseline-20261025-v3` @ `45632b5`.
- Blender 5.2.3 LTS (e13b728c6880); validátor v2 `b7d7f6a6…`; lock k13 `2ca93735…`.
- Mac munkamappa: `~/Downloads/WSG_CAM12_V3_KORREKCIO/`.
  - `forras/`: a blend másolata, a lock, a validátor és a villamos adat másolata.
  - `vegleges/`: a renderek és a naplók.
  - `csomag_S01/`: a tesztcsomag.

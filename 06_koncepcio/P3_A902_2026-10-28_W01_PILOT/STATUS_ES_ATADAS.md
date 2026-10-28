# WSG A-902 · P3 hatnézetes W01 pilot – forráshű állapotmentés

**Eredményazonosító:** \`A902-P3-WORK-W01-SIXVIEW-20261028-v1\`  
**Rögzítés dátuma:** 2026-10-28  
**Tulajdonosi visszajelzés:** „Nem rossz, de még mindig hiányolok használhatóságot és fantáziát. **A képek formátuma és külalakja kiváló!**”  
**Döntési státusz:** **VIZUÁLIS MEGJELENÍTÉS RÉSZLEGESEN ELFOGADVA · FUNKCIONALITÁS/KREATÍV TÉRRENDEZÉS NEM ELFOGADVA · KONCEPCIÓ – NEM VALIDÁLT**. Nem P3-sorozatindítás, nem Render Reality PASS és nem kivitelezési jóváhagyás.

## 1. Mit rögzítünk?

Az A-902 penthouse teraszának \`WORK-W01 – Wellness-udvar és távoli baldachin\` koncepciójára **hat konkrét képfájl** készült egy összetartozó Blender-alapú vizuális pilot részeként:

| Kód | Fájlnév a felhasználói ZIP-ben | Méret | Tartalom |
|---|---|---|---|
| V01 | \`images/WORK-W01_01_PREMIUM_2D.png\` | 1386 × 1135 | Prémium ortografikus látványalaprajz |
| V02 | \`images/WORK-W01_02_MUSZAKI_2D.png\` | 2200 × 1800 | Méretezési jelöléseket tartalmazó műszaki 2D PNG |
| V03 | \`images/WORK-W01_03_3D_A_NAPPAL.png\` | 1448 × 1086 | Építészeti/festői axonometria, nappal |
| V04 | \`images/WORK-W01_04_3D_B_NAPPAL.png\` | 1448 × 1086 | Fotórealisztikus axonometria, nappal |
| V05 | \`images/WORK-W01_05_3D_A_ESTE.png\` | 1448 × 1086 | V03 kamera esti nézete |
| V06 | \`images/WORK-W01_06_3D_B_ESTE.png\` | 1448 × 1086 | V04 kamera esti nézete |

**Vizuális minőség:** a felhasználó pozitívan fogadta a közös ábrázolási formát, a 2D/3D grafikai stílust és az esti hangulatokat. **Ez a képformátum a következő tervek kiinduló vizuális etalonja**, de nem bizonyítja az összes tárgy, szint vagy kilátás pontos helyét. A natív Blender-képek és az utólagosan stílusfinomított képek megkülönböztetendők.

**Valós bemenetek:** \`06_koncepcio/P0_A902_2026-10-27_v1/P0_TENYCSOMAG.md\`, részletes geometriai és fotóleltár, eredeti 1:50 terv, a rögzített T09-jakuzzihely és a 2026-10-27-i tulajdonosi pontosítások. W01 nem azonos a későbbi közös, végleges \`C01–C10\` elrendezéslistával.

## 2. A kapott ZIP ellenőrzött tartalomjegyzéke és épsége

**Felhasználótól kapott eredeti archívum**: \`WSG_A902_P3_SIXVIEW_W01_2026-10-28.zip\`  
**Méret:** 37 051 602 bájt (kb. 37,1 MB decimálisan).  
**SHA-256 (teljes ZIP):** \`67af81684580d8a2886fce93aca61a0f62a31f11e5aab1869ecd38f4759b84f1\`  
**Belső állományok száma:** 25; közös archívummappa: \`a902-terasz-p3-sixview-w01-20261028/\`.

**Ellenőrizhető kiemelt belső állományok:**
- \`index.html\` – helyi, képes bemutató; SHA-256: \`20db7ddca679a1e74c24c3648193f68af76e5e43bb3dabf1ae9304c74d645d10\`.
- \`source/P3_WORK_W01_pilot.blend\` – önálló pilot Blender-fájl; SHA-256: \`4ea80a221a7c8331ce52fcf8884d97a8b8cd2ca22fd17105818d18af8a048151\`. **Nem a WSG Blender-master cseréje vagy validált helyszíni modell.**
- \`source/build_and_render.py\` – renderépítő forrás; SHA-256: \`80535ed9584079ba733d41ead2fe8fd3b51225050b163588b5bea2294abb5217\`.
- \`source/repair_technical.py\` – technikai lap javító script.
- \`source/native_renders/\` – 5 natív Blender-kocka a képi stilizálás előtti referenciaállapotról.
- \`source/IMAGEGEN_PROMPTS.md\` – a képi finomításban használt promptok.
- \`audit/scene.json\`, \`audit/qa.json\`, \`audit/postprocess.json\`, \`audit/reality_gate.json\`, \`audit/budget.json\` – jelenet, belső QA, képi feldolgozás, feltételes realitás és becsült költség.
- \`source/reference_2d.jpeg\`, \`source/reference_4es.png\`, \`source/reference_6os.png\` – **külső eredetű inspirációs képek**; ezek a felhasználói ZIP részei, **nem a WSG meglévő vagy megvalósult teraszáról készültek**.

**A hat kész kép SHA-256-ja, sorrendben:**
- V01: \`2a058a54369dee2c43719e8fac722dcae286b4bd5f6117c23a1e83296aa58e4c\`
- V02: \`a47a718ba3a0987ff7c099ed5b334fb3d8ef06c837a85b901a25ec5056935068\`
- V03: \`9de30b94f982a0cf1162a0b4d2896eac146c2bf6bab1457197c86eb433f41580\`
- V04: \`0d4b2816bf3c233b75a002316a623dc65ca3f322970a86a360423a1d6baf6f9e\`
- V05: \`6a544aae082ec8200c1c049a762021df2ffe54e8fe83ea8e86b96d9cd842163b\`
- V06: \`22cd21042401fef425103601574ec7913284d4e90c8bb1ca9ea6795914cc7654\`

**GitHub-tárolási korlát ennél az állapotmentésnél:** ez az állapotlap és az ellenőrzőösszegek **felkerültek a GitHubra; az eredeti bináris ZIP, a hat PNG, a .blend és a külső referenciafotók viszont nincsenek a repóba átmásolva**. A ZIP továbbra is a 2026-10-28-i ChatGPT-beszélgetés felhasználói csatolmánya. Ennek oka, hogy a csatlakoztatott GitHub-írási művelet szövegfájlokra alkalmas, továbbá a repo a mentéskor **nyilvános**, miközben az archívum harmadik féltől származó mintaképeket és személyes gépen keletkezett fájlelérési útvonalakat is tartalmaz. **NEM állítjuk azt, hogy a teljes pilot GitHubon visszatölthető.** A későbbi teljes archívmentés előtt tisztázni kell a publikálás és a bináris Git/Git LFS feltételeit; a régi csomag változatlanul megőrzendő.

## 3. P3 pilot – saját bizonyítékok és nyitott korlátok

A pilot \`audit/qa.json\` szerint hat elkészült kép van, a két 3D kamera nappali–esti párja megegyezik. Ez **a csomag belső QA-állítása**, nem független, helyszíni milliméteres egyezésbizonyíték.

A \`audit/reality_gate.json\` szerint a következők **NEM IGAZOLTAK / FELTÉTELESEK**:
1. **WPC-szintváltás:** a képen szereplő +12 cm-es többletemelés **képi helyettesítő**, nem mért adat. Az R2 kutyarámpa +30 cm-es szintáthidalása modellpróba; R0–R3 teljes útvonal, fordulók, megfelelő rámpalejtés és a beltéri kapcsolódás mérendő.
2. **Valós térkontúr:** a teljes kertkontúr, a külön T13 oldalerkély és a jövőbeli szomszédtömeg nincs méretre pontosan a pilotban. A fotórealisztikus képek nem igazolnak valódi panorámát.
3. **Szauna és spa:** a kabin alapja, ajtója, tényleges kályha/szellőzőrendszere, 400 V ellátása, teher- és szélvédelme nincs műszakilag jóváhagyva. A jakuzzi teljes telepítése/szerviztere is méretpróbát kíván.
4. **Zuhany:** víz-, szennyvíz-, lefolyó- és téliesíthetőségi alapja nincs igazolva; ezért opció.
5. **Új kültéri elemek:** baldachin, növénydézsák, belátást csökkentő lamellák, többfokozatú világítás pontterhei, rögzítése és a 9. emeleti szélbiztonsága nyitott.
6. **2D műszaki lap:** jelenleg \`2200×1800\` **raster PNG**, a korábbi prezentációs szabványban megkívánt szerkeszthető/vektoros műszaki PDF még nincs igazoltan átadva.
7. **Képi finomítás:** V01, V03–V06 natív Blender-eredetű kockák képgeneratív stilizálásai; a feljavított növény, anyag és fény **nem mérési bizonyíték**.

A korábbi P0 \`geometry.json\` és a mellékelt P3 pilot \`scene.json\` nem azonos az új tárgyak független, fizikailag igazolt helyszíni méretellenőrzésével.

## 4. Költséghelyzet: konkrét, reprodukálható előzetes számok

Az eredeti \`audit/budget.json\` szerint a **képeken szereplő W01 teljes kreatív csomagja** (nem vásárlási ajánlat):
- direkt tételek: **7,93022 M Ft**;
- elkülönített 10% tartalék: **0,881136 M Ft**;
- bruttó mindösszesen: **8,811356 M Ft**;
- teljes kültéri tulajdonosi tervezési cél: **6,0–6,5 M Ft**;
- **eltérés a 6,5 M Ft-os felső célhoz: +2,311356 M Ft**.

Ebből a \`budget.json\` az alábbiakat **OPCIÓ** címkével jelöli: \`BA01\` baldachin 0,55 M, \`Z01\` zuhany 0,42 M, \`T01\` lamellás takarás 0,12 M, \`P01\` új növénycsoport 0,14 M. Még ha e négy tételt kivennénk és a kapcsolódó 10%-ot arányosan csökkentenénk, minden más változatlansága mellett kb. **7,46 M Ft** maradna – **még ez sem fér a 6,5 M Ft-os célba**. Az „opciók” törlését nem tekintjük automatikusan jóváhagyott designcsökkentésnek, hiszen éppen a kreatív térélmény fő elemei szerepelnek köztük.

- A jakuzzi készülékár és a szauna/kályha termékára csak **forrásolt árhorgony**, az egyedi helyszíni logisztika, statika, szerelés és bekötés több sora **tervezői becslés**.
- A tulajdonosi 2 M jakuzzi + 1,5 M szauna cél **nem garantált telepített ár**.
- A teljes **A-902 lakás bruttó 20 M Ft-os plafonja és 2 M Ft-os közös tartaléka továbbra is irányadó**; 6–6,5 M kültér a korábbi kb. 4 M-nál nagyobb, még teljes-lakás szinten egyeztetendő forgatókönyv. A tartalékot nem számoljuk kétszer.
- **Nincs tételesen validált, a képekkel azonos, 6–6,5 M Ft-os W01 kivitelezési alternatíva.**

## 5. Felhasználói értékelés és következő javítási prioritások

**Megőrzendő és követendő vizuális színvonal:** a hatnézetes formátum, prémium 2D, két eltérő axonometrikus kamera és esti pár, azonos térösszetétel, kellemes növény- és anyagmegjelenítés, érthető HTML-galéria.

**Nem elfogadott – tartalmi/működési kapu:**
- A jelenlegi W01 kültéri étkezője **csak 2 főre** szól; vizsgálni kell, hogy a tulajdonos által kért baráti összejövetelekhez milyen **4–6 fős** étkező/társalgó és italos kapcsolat teremthető.
- A lounge és a szabadon használható, elnyúlós, napos/árnyékos ülésrendszer kreatív ereje és napi praktikuma elmarad az eredeti, jelentős vendégélményre épülő víziótól.
- A szauna–jacuzzi–kültéri zuhany kapcsolata legyen valódi, biztonságosan közlekedhető **wellness-útvonal**, ne csak három külön lerakott készülék.
- A kutyarámpa legyen **fizikai, minden szinten végigellenőrzött út**, nem csak vizuális szürke csík.
- Belátásvédelem: a leendő szomszéd lakott teraszairól fennálló szemvonalakat **ülő/fekvő/álló/jakuzzi-használati magasságban** is vizsgálni kell; új növényeknek tényleges takarási és téli szerepük legyen, a Ny/ÉNy panoráma ne sérüljön.
- A kültéri bár/italhűtés, hordozható mozi, diszkrét hang, Hue-jelenetek és eső/téli tárolás **napi használati** szempontjai ne maradjanak utólagos szöveges ígéretek; koncepciónként tudatosan integrálandók vagy hiányként jelölendők.
- A szauna villamos betáplálása, szellőzésének tényleges kivezetése és telepíthetősége **kötelező műszaki gate**, nem kikerülendő vizuális korlát.
- **Kreatív változatosság:** a további \`C01–C10\` tervek ne pusztán W01 átöltöztetései legyenek; eltérő térélmények (baldachin, integrált bár+lounge, privát spa, napozó, kutyás kert stb.) maradjanak.

**Javasolt következő átadás:** új, kifejezetten **használhatósági és térélmény-revíziós W01** az érvényes P0 alapján, a hatnézetes képi sablon **megtartásával**, szerkezeti/villamos/költségkritikus feladatlista és 6–6,5 M Ft-os valós alternatíva kidolgozásával. **Ne indítsunk automatikusan 10×6 vagy 30×4 sorozatot.** A \`C01–C10\` végleges közös lista sem lezárt, amíg a Work- és Pro-koncepciók átfedését nem ellenőriztük.

## 6. Bizonyítási és feladatátadási státusz

| Szakasz | Állapot |
|---|---|
| P0 ténycsomag | Létrejött, P1-re alkalmas, de helyszíni méretek és belátás még nyitott |
| P1 két független kreatív kör | Elkészült, eltérő forráscsomagok; a két modell előzményeit ne írjuk át |
| P1.5 v1 első vizualizáció | Tulajdonosi elutasítás; túl sok hasonló, pusztán átrendezett bútor |
| P1.6 térkompozíciók | 15 WORK-SVG új irány; karakteresebb kreatív alap, de nem validált és nem lezárt közös top 10 |
| **P3 WORK-W01 6-képes pilot** | **6 kép ténylegesen elkészült, a vizuális formátum jóváhagyó visszajelzést kapott; a térhasználat, kreativitás és a keret még nem fogadott el** |
| P3 teljes 10×6 | **NEM INDULT** |
| P4 30×4 stílusverseny | **NEM INDULT** |
| P5 párosítás | **NEM INDULT** |
| P6 fotókamerás döntősök | **NEM INDULT** |

**Tilos:** \`GOAL.md\`, P0, P1-v1/P1.5-v1/P1.6, Blender-master vagy a korábbi 30 stíluskatalógus csendes módosítása, hamis PASS, felhasználói döntés nélküli nagy renderbatch.

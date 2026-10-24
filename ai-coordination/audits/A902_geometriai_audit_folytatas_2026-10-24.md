# WSG A-902 – a geometriai audit célzott folytatása

Dátum: 2026-10-24. Státusz: **geometriai megfelelés nem igazolt; RENDER REALITY PASS nem adható.**

Ez a meglévő audit folytatása, a korábbi validátorjelentések és a v2-es tervkinyerés felhasználásával. Csak ezt a jelentést hoztam létre. Nem indítottam Blendert vagy Blender MCP-kapcsolatot; nem módosítottam jelenetet, szkriptet, lockot vagy projektutasítást. Az alábbi új számítások JSON- és Python-forrásból készültek, nem az élő jelenet újraméréséből.

## Bizonyítékalap és jelölések

- **KÓDBÓL/ADATBÓL IGAZOLT:** a vizsgált verzióból számszerűen levezethető. Nem jelent helyszíni igazolást vagy azonosságot Claude aktuális, nem mentett jelenetével.
- **TERV / KORÁBBI JELENTÉS:** dokumentumban vagy korábbi mérési riportban szerepel; ebben a körben nem mértem újra Blenderben.
- **BIZONYTALAN:** hiányzó, ellentmondó vagy csak becsült adat; lezáráshoz szükséges bizonyítékot külön megadom.

Elolvastam a kért négy dokumentum aktuális GitHub-változatát: `GOAL.md`, `AGENTS.md`, `ai-coordination/RENDER_REALITY_GATE.md`, `ai-coordination/inputs/A902_v1/GEOMETRIA_A902.md`. Rögzített forrásverzió: [f307765edd2a812498287edea5645596289eafa3](https://github.com/peterkapusi88-hub/wsg-berendezes/commit/f307765edd2a812498287edea5645596289eafa3). Elolvastam az OPENAI-instrukciókat, a kötelező stíluslabor-skillt, a v1.1 kiegészítést és a műszaki ellenőri kivonatot is.

A helyi olvasási forrás `/Users/peterkapusi/Downloads/wsg-berendezes`. 23 kiválasztott forrásfájlt Git blob SHA-val összevetettem a fenti committal: 22 egyezett, a helyi skill régebbi volt, ezért annak aktuális GitHub-változatát is teljesen elolvastam. A vizsgált Blender-kód, JSON, korábbi riportok és két A902 tervkivágat egyezett. A `.blend` fájlokat nem nyitottam meg és nem hasonlítottam össze az élő memóriával.

Vizuálisan ellenőriztem a méretezett alaprajzot, a megvalósulási terv kivágatát, a semleges modell alaprajzi nézetét és a v2 terasz felülnézeti renderét. A render csak alátámasztó kép; a méreteket a forrásadatokból számoltam.

## 1. Konyha – a 89 cm nem a legszűkebb használati keresztmetszet

**Megállapítás: a Lake Forest forráskód szerint a párhuzamos munkalapélek között 85 cm marad. Ez 5 cm-rel kevesebb a GOAL 90 cm-es közlekedési alsó célértékénél.** Ez projektkritérium, nem jogszabályi megfelelőségi állítás.

Forrás: [stil_lakeforest_layer.py, 89–95. sor környezete](/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/stil_lakeforest_layer.py:89).

| Vizsgált elemek | Számítás | Hézag |
|---|---|---:|
| Keleti és nyugati alsószekrény-test | 10,04 − 9,15 | 89 cm |
| Keleti és nyugati munkalap | 10,02 − 9,17 | **85 cm** |
| Déli magasszekrény és keleti munkalap helyi keresztmetszete | 10,02 − 9,70 | **32 cm** |

A 85 cm-es sáv y=2,40–4,04 között, 1,64 m hosszon áll fenn. A 32 cm-es rés y=1,30–1,90 között a déli végszakasz helyi hézaga; nem állítom, hogy a teljes konyhába ezen kell belépni. A magasszekrény frontiránya és használati helyigénye nincs igazolva, ezért ez külön hozzáférési kockázat.

A v2 tervi konyhaszélesség 10,55−8,45=2,10 m, a v1-é 2,09 m. Ha mindkét oldalon 62 cm mély munkalap marad, a tervi nyers szélességből is csak **86 cm** adódik, még a kész felületek hatásának tisztázása előtt. A falak terv szerinti átvezetése önmagában tehát nem oldja meg a szűkületet. Ugyanezen keresztmetszetben 90 cm-hez legfeljebb 120 cm összes munkalapmélység férne a nyers 210 cm-be; ez vizsgálati korlát, nem jóváhagyott bútoráttervezés.

**BIZONYTALAN:** az aktív Zenit/Lake Forest jelenet aktuális munkalapjai, kész falak közötti tényleges távolság, gépajtók és fiókok nyitott helyigénye. Egy feltételezett 60 cm-es benyíló gépajtó a 85 cm-ből 25 cm-t hagyna; ez érzékenységi példa, nem termékadat. A gépészeti kiállások és a valós termékkonfiguráció nélkül a konyha használhatósága nem zárható le.

**Lezárási feltétel:** kész falsík–falsík mérés; aktív bútorok világkoordinátás kontúrja munkalappal és fogantyúval; gép-/fióknyitási burkolók; a bejárást és használatot igazoló alaprajzi nézet.

## 2. 05.2 háló – a jelenlegi elrendezés hibás, az általános bútorozhatatlanság nem bizonyított

A [korábbi validátorjelentés](/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/validator_report_2026-10-24.md) szerint a 160×200-as ágy és az északi éjjeliszekrény 22–30 cm-rel érintette a szobaajtó vizsgált előterét. A későbbi terasz-v2 riport ugyanezeket a belső hibákat továbbra is nyitottnak írja. Ez **korábbi jelentéssel alátámasztott, ebben a körben újra nem mért hiba**.

| Geometria | Fő térrész | Gardróbfülke |
|---|---|---|
| v1 lock | 3,62×2,55 m | 2,42×0,80 m |
| v2 tervkinyerés | 3,65×2,65 m | 2,42×0,70 m |
| Műszaki ellenőri kivonat | 3,548 m szélesség; kb. 3,33 m teljes mélység | A mérési szakasz értelmezése ellenőrizendő |

A 3,65×3,35 m-es teljes befoglaló **nem teljes téglalap alakú szabad szoba**. A fülke és a belépő kialakítása külön kezelendő. A v2 két téglalapjának összege 11,3665 m², míg a terv helyiségfelirata 11,66 m²: a dobozos közelítés nem pontos helyiségpoligon.

Az elhelyezési irány döntő:

- Ha a 160 cm-es ágyszélesség a 2,65 m-es fő mélységből fogy, kétoldalt összesen 105 cm marad, azaz középre helyezve 52,5–52,5 cm. Ez a kétoldali 60 cm-es projektcélt már elméleti, keret nélküli számítással sem teljesíti. V1-ben ugyanez 47,5–47,5 cm.
- Ha az ágy 200 cm-es hossza észak–dél irányú, a 3,65 m-es szélességből 205 cm marad az ágy két oldalára. A fülkében feltételezett 60 cm mély gardrób előtt a teljes 3,35 m mélységből 75 cm maradhat az ágy végén. Ez **vizsgálható alternatíva**, nem elférési igazolás: ajtóívek, tényleges ágykeret, fülke széle és gardróbnyitás még korlátozzák.
- A 140 cm-es szélesség a 2,65 m-es fő térrészben elméletileg 62,5–62,5 cm-t engedne, de a külső ágykeret és a kész falméret ezt csökkenti. Önmagában a „140-es ágy” megnevezés nem megoldási bizonyíték.

**Fontos korrekció a korábbi audithoz:** a validátor téglalap alakú megközelítési sávot tesztel, nem valódi ajtóforgást. Az „ajtó csak ~60 cm-re nyílik” állítás ebből nem vezethető le. A nyugati `Erkelyajto_05_2_*` elemek ráadásul nem `Ajto_*_lap` nevűek, így a jelenlegi ajtó-előtér ciklus kihagyja őket. Az alaprajzon látható nyitásívet külön kell összevetni a bútorral.

**BIZONYTALAN:** a 3,548 m-es kézírásos méret pontos mérési szakasza; a jelenlegi ágy külső kontúrja; ajtópánt és nyitásirány, nyitható erkélyajtószárny, gardrób frontja. **Lezárási feltétel:** ezekkel együtt két méretezett alternatíva összevetése, mindkét ajtó és a gardrób működtethetőségével. Az audit nem választ új bútort.

## 3. Terasz – a v2 lényegi javulás, de a járhatósági és területi geometria nincs lezárva

A megvalósulási terven a gres szintje +28,40, a WPC-é +29,02: **a 62 cm különbség tervből igazolt**. A v2 relatív z=−0,15 / +0,47 értékei ezt helyesen reprodukálják. A belső padlóhoz viszonyított pontos küszöb- és csatlakozóprofil helyszíni ellenőrzése továbbra is szükséges; a méretezett terv 15 cm-es fellépést és korrekciót jelöl.

A v1 sík terasza, üvegkorlátja és régi Cam_05 nézete elavult. A v2 riport szerint ezeket elrejtették, a belső falakat viszont nem vezették át a v2-re. A fájlnévben szereplő „v2” ezért nem jelent teljes lakásgeometriai v2-t.

**Kódból igazolt eltérések** – [build_terasz_v2.py](/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/geometry_v2/build_terasz_v2.py:64):

1. **A WPC-nyelv bejáratát szegély keresztezi.** A `v2_Szegely_beton_D` x=3,44–16,27 és y=13,41–13,53 között folytonos. A nyelv x=9,29–11,39 között ugyanitt indul. A szegély z=0,47–0,82, vagyis 35 cm-rel emelkedik a WPC fölé, és 12 cm mélyen teljes szélességében keresztezi a bejáratot. A kód nem hagy nyílást. Ez a forrásból felépülő geometriában tényleges akadály; a helyszíni szegély helyes kialakítását és a mentett `.blend` esetleges későbbi javítását külön kell ellenőrizni.
2. **A lépcsőadat és a létrehozott geometria eltér.** A JSON mindkét lépcsőt y=12,10–12,40 közé, 30 cm mély dobozba teszi; a kód y=11,50-től épít három 30 cm-es fokot. A teljes vetület így 90 cm, 60 cm-rel délebbre kezdődik. A 62 cm-t négy, egyenként 15,5 cm-es emelkedésre osztja: három köztes fok és a felső dobogó. Ez belsőleg következetes számítás, de nem mért lépcsőgeometria.
3. **Nincs igazolt folyamatos út az északi pihenőhöz.** A nyelv y=14,46-nál véget ér, az északi WPC-pihenő y=18,95-nél kezdődik. Közöttük 4,49 m hosszon nincs összekötő WPC a kódban. A videó alapján említett perem menti járósávot a projekt tudatosan nem modellezte. Ez hiányzó modellkapcsolat, nem bizonyíték arra, hogy a valós helyen nincs járható út.
4. **A zöldtető +0,77 m szintje és +25 cm-es dombja becslés.** A szegély a kódban 35 cm-rel áll a WPC fölé. A korlát teteje a kert mentén 0,47+1,10=1,57 m; a feltételezett 0,77 m-es zöldfelülethez képest csak 80 cm. Ez referenciaszint-eltérés, nem helyszíni korlátminősítés; a valóban járható felület szintjét kell hozzárendelni.

**Területi ellenőrzés** – vízszintes vetület, a megadott dobozokból:

| Zóna | Terv | Kód/adat szerinti vetület | Eltérés / értelmezés |
|---|---:|---:|---|
| Nyugati greszóna | 23,62 m² | 22,815 m² | −0,805 m²; a terv felirata „terasz és lépcső” |
| Keleti greszóna | 19,34 m² | 19,032 m² | −0,308 m²; eltérő területfogalom is közrejátszhat |
| Négy WPC-téglalap | 25,00 m² | **26,5453 m²** | +1,5453 m², +6,18%; a lépcsőkkel nem növeltem |
| Zöldtető külső befoglaló | 71,18 m² | 78,7887 m² | Befoglaló, nem nettó zöldfelület |
| Kódbeli fű- és ágyásfoltok, domb vetületével | 71,18 m² | 72,2953 m² | +1,1153 m² a szegélyek takarásának levonása előtt |

Ezek a különbségek **kontúr- és területfogalom-egyeztetést** igényelnek. Nem szabad a teljes v2 dobozterületet igazolt használható területként közölni vagy burkolatkiíráshoz felhasználni. Az erkély 11,26 m² külön tétel; a 79,22 m² teraszösszeg ezt már tartalmazza, a 71,18 m² zöldtető azon felül van, összesen 150,40 m² kültér.

**BIZONYTALAN / DOKUMENTUMKONFLIKTUS:** a v1.1 egyszer könnyű bútort megenged a zöldtetőn, később csak gresre/WPC-re engedi; a GOAL igazolt terhelhetőséget követel. Ebből a jelentésből nem adható zöldtető-bútorozási jóváhagyás. A jakuzzi 2×2 m-es téglalapja jelölő: a mélység feltételezett, nem igazolt előkészítési méret.

**Lezárási feltétel:** felmért zónapoligonok, küszöbprofil, összes járószint, lépcsőszélesség/fokmélység/emelkedés, szegélymegszakítások, perem menti út és a jakuzzi tényleges előkészítési kontúrja. A terasz új elemeit külön v2 lockkal kellene ellenőrizni; ez a kör nem módosította a lockot.

## 4. Falak, nyílások és kamerák a méretezett tervhez képest

Forrás: [v1–v2 eltéréslista](/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/geometry_v2/A902_eltereslista_v1_v2.md), a méretezett terv vizuális ellenőrzésével.

| Elem | v1 → v2 tervadat | Következmény |
|---|---|---|
| Nappali hossza | 6,92 → 7,08 m | +16 cm teljes hossz; két falsík együtt változik |
| 05.2 keleti / északi határ | +3 / +10 cm | Bútorozást újra kell számolni, a fülke mélysége csökken |
| 05.1 keleti falsík | 3,62 → 3,57 m | A falra szerelt tömegek 5 cm-rel eltérnek a tervtől |
| 05.3 nyugati / keleti határ | −15 / −13 cm | Nem csupán szobaméret, hanem helyzet változik |
| Konyha nyugati / keleti határ | −10 / −9 cm | Szélesség csak 1 cm-rel nő; a bútor helyét is át kellene vezetni |
| Közlekedő keleti határ | −15 cm | A korábbi szabad szélességek nem vihetők át ellenőrzés nélkül |

A konyhazóna északi −110 cm-es különbsége zónadefiníció-váltás, nem 1,10 m-rel elmozdult fal. A helyiségdobozok nem helyettesítik a falkontúrt: a kivágások, ajtózsebek, pillérek és aknák miatt a „±15 cm-en belül” nem elégséges használhatósági bizonyíték egy 85–90 cm-es közlekedőnél.

**Nyílások:** a terv és a lock fő névleges szélességei összhangban vannak: nappali 4,50 m, 05.3 1,80 m, nyugati nyílások 3,65 és 1,88 m. A terv a terasznyílásoknál 2,53 m, a nyugatiaknál 2,57 m magasságot jelöl; a v1 modell egységesen 2,55 m-rel dolgozik. Ez ±2 cm névleges eltérés, eltérő mérési referenciák lehetőségével. A 90 cm-es beltéri tokhoz a lock 84 cm-es ajtólapot tárol; a tokméret nem azonos az igazolt szabad átjáróval. A nyitásirány, a nyitható mezők és a küszöb részletes geometriája nincs validálva. A 05.3 terasznyílásnál a terv nyitásíve miatt a minden teraszfalra általánosított „tolóajtó” leírás sem fogadható el részletes ellenőrzés nélkül.

**Kamerák:**

- A Cam_02–04 pozíciója a v2 helyiségbefoglalókon belül marad; ez csak durva pozícióellenőrzés, nem bútorütközés- vagy láthatóságvizsgálat.
- Cam_02–04 a lockban **20 mm**, miközben az OPENAI-instrukció 24 mm-t kér. Azonos szenzor esetén a 20 mm szélesebb látómezőt ad; a kameraazonosító önmagában nem biztosít összevethető perspektívát.
- A validátor csak pozíciót és Euler-forgatást ellenőriz. Nem ellenőrzi az objektívet, kameratípust, ortho-skálát, szenzort, shiftet, képarányt, clippinget vagy a ténylegesen aktív renderkamerát. A „kamerák OK” így nem teljes kamerazár.
- Cam_05 elavult, ráadásul a v2 adatai szerint növényágyás fölé esik. Új helyszínhű terasznézethez nem használható igazolt járható kameraként.
- Az új Cam_07 16 mm-es, z=1,45 m, vagyis 1,60 m-rel a gres fölött. Cam_08 madártávlati, Cam_09 ortografikus ellenőrző nézet. Egyik sincs a v1 hatkamerás lockban; külön rögzítésük nélkül nem ellenőrzött az összevethetőség. A madártávlat ellenőrző ábra, nem szemmagasságú helyszíni kamera.

A belmagasságra a frissebb műszaki ellenőri kivonat 2,903–2,925 m-es méréseket ad. A v1 input „mérés még nincs” mondata elavult. A 2,90 m-es modell ehhez közeli referencia, de padlótól plafonig bútorhoz helyiségenkénti mérés szükséges. A fekete belső ablakkeret v1-leírását szintén felülírja a frissebb fotókivonat „kívül antracit, belül fehér” adata; a pontos termékazonosság ettől még nem igazolt.

## 5. Mit bizonyít és mit nem a meglévő validátor?

A [geometry_validator.py](/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/geometry_validator.py) a v1 lockhoz való visszaegyezést ellenőrzi, nem a valós tervhez való megfelelést. A régi, elrejtett padlókat is összehasonlítja, miközben az új `A902_Terasz_v2_ELOZETES` geometriát a fix gyűjteménylistái kihagyják. Ezért a v2 terasz riportjában szereplő 54 fal / 52 nyílás / 19 padló / 6 kamera „OK” nem terasz-v2 validáció.

További releváns korlátok: nincs általános bútor–bútor ütközésvizsgálat, konyhai munkalap-hézagteszt, ajtónyitási ív, járható útvonal vagy helyi teraszszintekhez kötött bútorvizsgálat. A helyiségbefoglalás csak a négy bbox-sarkot vizsgálja, ezért nem igazolja, hogy az egész tárgy a megengedett poligonon belül van. A 05.2 erkélyajtaját a névszűrés kihagyja. Az `ok` listába a kód hibák mellett is beír ellenőrzésenkénti sorokat; ezeket nem lehet önálló PASS-jelzésként értelmezni.

## 6. Auditdöntés és szükséges bizonyítékok

| Terület | Döntés ebben a körben | Következő lezáró bizonyíték |
|---|---|---|
| Konyha | **A vizsgált LF-kód 85 cm-es sávja nem teljesíti a 90 cm-es projektcélt** | Kész méretek és aktuális bútor-/gépnyitási kontúrok |
| 05.2 | **A korábbi elrendezés hibája nyitott; általános bútorozhatatlanság nem igazolt** | Külső bútorméretek, pontos szobapoligon, mindkét ajtó működése |
| Terasz | **ELŐZETES; szegélyakadály, útvonal- és területeltérések** | Szint- és kontúrfelmérés, lépcsők, szegélymegszakítások, pihenő megközelítése |
| Falak / nyílások | **v1 lock-egyezés nem valóságigazolás** | Tervhez és kész méretekhez illesztett kontúrok, nyitási és küszöbadatok |
| Kamerák | **Részlegesen zároltak, a perspektíva nem teljesen ellenőrzött** | Teljes kamera-paraméterlap és renderenkénti forrásverzió |

Az előző audit eredményeit ezek a megállapítások pontosítják, nem nullázzák. Az élő jelenet megfelelőségéről új állítást nem teszek. A meglévő koncepcióképek továbbra is **KONCEPCIÓ – NEM VALIDÁLT** besorolásúak; a v2 terasz képei **ELŐZETES GEOMETRIA-ELLENŐRZŐ NÉZETEK**. Anyag-, termék- és költségaudit nélkül geometriai javítás után sem következne automatikusan teljes Render Reality PASS.

# WSG A-902 – teljes P0 forrás- és geometriai audit

**P0-v1 · 2026.10.27. · Jóváhagyásra átadott eredmény**

Forrásállapot: `peterkapusi88-hub/wsg-berendezes`, commit `4959bfe143833617d220b1613bd58908ee4ec5b7`. Készítő: a jelen Work/Codex munkamenet; egyetlen elemző folyamat, másik AI vagy független ellenőr indítása nélkül. Új látványkép: **0**. Blender-módosítás: **0**. P1 kreatív elrendezés: **0**. Az auditábrák meglévő adottságokat és bizonytalanságokat mutatnak, nem berendezési terveket.

## 1. Az audit eredménye

A forrásokból összeállítható a két későbbi AI számára azonos, használható kiindulási ténycsomag. A rendelkezésre álló modell azonban **nem tekinthető minden részletében helyszínhű geometriának**. A legfontosabb korrekció a WPC-n belüli további szintváltás és a tájolás: az 1:50-es tervvel egyeztetett műholdkép szerint a fő kijárattól egyenesen kifelé nagyjából ÉK felé nézünk. A régi rajzi x/y tengelynevek nem földrajzi kelet/észak. [PLAN3, PLAN18, U07, P08–P11, T02; azonosítók a forrásjegyzékben és fotókatalógusban]

**A teljes saját kültér használható, a jakuzzi helye kötött.** Ez tulajdonosi alapadat, nem újra megnyitott általános használhatósági kérdés. Konkrét készülék mérete, tele tömege, víz- és áramigénye, szerelési hozzáférése ettől még külön, jelenleg hiányos műszaki adat. A régi zöldtető-tiltást és `butorozhato:false` mezőt a későbbi AI-k nem vihetik tovább érvényes általános tilalomként. [U01]

Az új szomszéd hatását irányonként kell kezelni. Az ÉNy-i panoráma, az É/ÉK felé megmaradó lehetséges rések és a DK felé lehetséges távoli kilátás nem vonható össze „eltűnő panorámává”. A K/DK belátás és a szemközti új teraszok belátása kötelező tervezési bemenet. A jelentős új árnyék hiánya tulajdonosi várakozás; sem jelentős árnyék, sem egész éves árnyékmentesség nem igazolt. [U03–U07]

## 2. Forráslefedettség és módszer

| Forráscsoport | Elvégzett ellenőrzés | Határ |
|---|---|---|
| Kötelező projektutasítások | Master, GOAL, AGENTS, projekt-SKILL, OPENAI_instructions, Render Reality Gate, átadási protokoll, részletes brief és háromrétegű prezentációs szabvány elolvasva. | A friss tulajdonosi utasítás az ütköző régi feltételezéseket felülírja. |
| Tervek | Eredeti 27 oldalas PDF 3. és 18. lapja képi és szöveges ellenőrzéssel; repo-kivonatok egyeztetve. | A 3. lap megvalósulási 1:125; a 18. lap módosított vevői 1:50, nem azonos státusz. A teljes kert nincs a 18. lapon. |
| Profi A902 | **33/33 eredeti fájl**, minden kép külön vizsgálva; három vágott pár jelölve. | Nézőképek 1800 px, kritikus részek eredeti képből kivágva; nincs fotogrammetriai kalibráció. |
| Külső profi képek | **19/19 kontaktlapos szűrés**, 9 releváns kép külön megvizsgálva, 10 lobby/garázs kép irrelevánsként nyilvántartva. | Közös kert és homlokzat nem az A902 saját terasza. |
| Műszaki fotók | 8 célzott terasz/kert/kiállás közeli kép részletes feldolgozása. | A meglévő teljes műszaki fotóarchívum nem a 33-as profi leltár része. |
| Blender | v2 és v2b másolat csak olvasva; 43 teraszelem összevetve a lockkal. | A geometriai egyezés nem helyszíni méret- vagy műszaki alkalmasságigazolás. |
| Műholdkép | Tulajdonosi piros jelölés és észak-felfelé tájolás; utcák és épülettömegek egyeztetése. | Felvételi dátum, geodéziai tetőpontok és pontos magasságok hiányoznak. |
| Környezeti webforrás | Beruházói Park West Rise és Westside Grand adatok; Puskás Aréna hivatalos helyszínadat. | Nem helyettesít szomszéd építészeti metszetet vagy közvetlen látóvonal-ellenőrzést. |

**237 letöltött/másolt repófájl bájtszintű azonossága** ellenőrzött a rögzített GitHub-fa megfelelő blobjaival. Ez forrásazonosság, nem 237 tétel minden részletének tartalmi validálása. Az ellenőrzőösszegek a [forrásmanifestben](evidence/source_manifest.json) vannak. A forrás-commit időpontját követő egyéb repóváltozások nem részei ennek az auditnak.

A régi videóelemzés és kinyert képkockák kiegészítő anyagként rendelkezésre állnak; az eredeti videók nem kerültek új, teljes körű feldolgozásra. A torzított panoráma-összefűzés nem méretforrás. Az eredeti repó-kontaktlap helyett a teljes, ellenőrzött profi fájlkészletből készült helyi leltár szolgált a hiánytalanság ellenőrzésére. A P3–P6 vizuális minőségreferenciák nem szolgáltak A902-geometriaként. [V, M]

## 3. Terület, határok és anyagok

A tervi saját kültér összesen **150,40 m²**: T09 gres és lépcső 23,62; T10 gres és lépcső 19,34; WPC 25,00; zöldtető 71,18; oldalerkély 11,26 m². A 79,22 m² burkolt terasz/erkély és a 71,18 m² zöldtető összege nem ugyanennyi sík, nettó berendezhető terület. A kontúrok, lépcsők, szegélyek, ajtók, fedlapok és közlekedés helyet foglalnak. A zöldtető egészének használhatóságát U01 rögzíti. [PLAN3, U01]

T09 a széles nappali üvegfal előtt, T10 a 05.3 szoba előtt fekszik. Közöttük magas WPC-dobogó, a kert felé harántsáv és kiugró nyelv kapcsolódik. Két oldalán gyepes zóna, középen kiemelt vegyes növényágyás látszik. A kert távoli végén további kis WPC-felület szerepel a forrásmodellben. A fő tetőterasz és a 05.1/05.2 előtti L-erkély kapcsolatai külön kezelendők. [PLAN3, PLAN18, P03–P15, P26–P30, G]

Meglévő anyagok: világosszürke gres, sötét szürkésbarna bordázott WPC, világos betonszegélyek, antracit függőleges pálcás fémkorlát, foltos világos téglahomlokzat és sötétebb nyíláskávák, antracit külső nyílászárók. A szín fotófüggő; gyártó, dekor, csúszásállósági osztály és pontos burkolatméret nem igazolt. A későbbi render ezeket nem cserélheti önkényesen új építészeti anyagra. [P03–P11, T01–T08]

Meglévő növényzeti leltár: gyep; csomós fűjellegű növények; szélesebb levelű évelők/talajtakarók; vékony szárú rózsaszín és világos virágok; vegyes ágyás; mulcs/kavics; felszíni fekete öntözőcsövek és szerelvényfedlapok. Faj, darabszám, téli tömeg, kutyára gyakorolt hatás és gyökérmélység nincs hitelesítve. A modell 70 zöld és 28 virággömbje nem növényfelmérés. [P05–P13, T05–T08, G]

## 4. Terv–fotó–Blender eltérésjegyzék

| ID | Terv / egyéb forrás | Fotó | Blender / adatfájl | P0-következtetés |
|---|---|---|---|---|
| D01 | Gres +28,40; WPC +29,02; 62 cm különbség. | A harántsáv felett még külön emelkedik a középső platform. | Minden WPC teteje +0,47. | A modell több tényleges szintet egy síkra egyszerűsít. A plusz fellépés cm-ben ismeretlen. |
| D02 | T09 23,62 m². | Nem kalibrált. | Téglalap 22,815 m². | −0,805 m², kb. −3,41%; eltérő határértelmezés lehetséges, nem „kijavított” tervterület. |
| D03 | T10 19,34 m². | Nem kalibrált. | Téglalap 19,032 m². | −0,308 m², kb. −1,59%. |
| D04 | WPC 25,00 m². | Több részfelület és magasság. | Négy téglalap 26,5453 m². | +1,5453 m², +6,18%; további kontúrellenőrzés szükséges. |
| D05 | Zöldtető 71,18 m². | Tagolt ágyás, gyep, domb. | Befoglaló 78,7887 m²; becsült magasság. | Befoglaló nem nettó zöldtető. Nem vezethető le valódi térfogat vagy földvastagság. |
| D06 | Erkély 11,26 m². | Keskeny, részben belátható. | L-poligon 11,8841 m²; rejtett régi téglalap is jelen van. | +0,6241 m², +5,54%; csak aktív L-kontúr használható előzetesen. |
| D07 | Két lépcső. | Három köztes járófelület után további WPC-szintváltás olvasható. | 4 ×15,5 cm modell-emelkedés; régi JSON rövid doboza nem teljes futás. | Modellméret nem helyszíni lépcsőfelmérés. |
| D08 | WPC-nyelv kertkapcsolata. | A nyelv megközelíthető. | Folytonos betonszegély a bejáratán keresztül. | Fiktív elzárást nem szabad tervezési adottságnak tekinteni. |
| D09 | Kert körvonala és burkolatjelölés. | Nem minden külső útvonal követhető végig. | Távoli pihenő kapcsolata hiányos; külső WPC-sáv nincs teljesen modellezve. | Folytonos körbejárás nem bizonyított. |
| D10 | 18. lap északjele ≈52,8°, 3. lap helyszínvázlatáé ≈12,5°. | Kameraazimut nincs kalibrálva. | Régi x=K/y=É megnevezések. | U07 a 18. lap szerinti munkatájorientációt támogatja. +y≈53° ÉK. |
| D11 | Jakuzzi áramjel új kinyerésében y≈9,29. | Nagyobb doboz és kisebb fedeles szerelvény látható. | Marker y≈9,69; 2×2 m helyőrző. | Kb. 40 cm pozícióeltérés; pontos kiállást és valódi készülékhelyet nem ad a marker. |
| D12 | Zöldtető használata U01 szerint teljes. | Saját tetőkert látható. | Régi „nem bútorozható” mező. | Tulajdonosi közlés elsőbbséget élvez; egyedi terhek/bekötések külön adatként maradnak. |
| D13 | Régi brief kb. 6 emeletes szomszéd. | Építkezési állapot, nyitott horizont. | Nincs hiteles jövőbeli szomszédtömeg. | U03 és W1 alapján 9 emeletes teraszos épülettel számolunk; magasság/távolság ismeretlen. |

Részletes koordináták és reprodukálható modell-összevetés: [tér- és geometriai adatlap](TER_ES_GEOMETRIA.md), [geometry.json](geometry.json), [43 elem összehasonlítása](evidence/terrace_lock_comparison.json). A fenti D01 és D08 a jelenlegi modell fotóval kimutatható korlátai; a többi tételnél az eltérő dokumentumstátuszt és definíciót is meg kell őrizni.

## 5. Tájolás, környezet és kilátási/belátási szektorok

A [műholdképkivágaton](plans/U07_google_maps_terasz_kivagat.png) a piros nyíl a WSG I Szabolcs utcai, északkeleti végéhez közeli tetőteraszra mutat. Az észak-felfelé képen a Szabolcs utca DNy–ÉK tengelyű; a vasúti sáv az épülettől DK felé húzódik. A 3. lap épülettömegének és a 18. lap északjelének összeolvasása alapján a rajzi fő kijárati irány ÉK. A kb. 53°-os érték használható munkairány, nem bemért azimut. Az URL koordinátája térképnézet-közép. [U07, PLAN3, PLAN18]

Az új, szemközti beruházás valószínű azonosítása **Park West Rise, Szabolcs utca 15**. A beruházó kilencemeletes, penthouse-okat és teraszokat is tartalmazó projektet közöl. A cím és a műholdképi építkezési hely összhangban van a tulajdonosi leírással; a pontos telekhatár, szintmagasság, A902-től mért távolság és takarási kontúr nincs geodéziailag ellenőrizve. A WSG II ettől külön szomszédsági elem; nem szabad automatikusan ugyanennek a szemközti háznak nevezni. [U03, U07, W1, W2]

| Szektor | Jelenlegi / várható kilátás | Belátás | Tervezésbe továbbadandó tény |
|---|---|---|---|
| Ny–ÉNy, a kijárattól balra | Városi tetők és távoli hegyes horizont több fotón; fontos panoráma. | Közeli tetőteraszok/ablakok részleges belátása lehetséges. | A panoráma érték; teljes intimitás nem bizonyított. |
| É–ÉK | Tulajdonos szerint maradhat panoráma; a nyitott építkezési állapot változik. | A szemközti új felső teraszok kötelezően figyelembe veendők. | Csak az új ház saját látószögében várható takarás; a széleken megmaradó rések mérete ismeretlen. |
| K–DK, részben jobbra | Közeli épületek; DK felé távoli kilátás lehetséges. | Tulajdonos által jelzett saját és új épületi ablakok/teraszok. | Egyszerre belátási és lehetséges panorámaszektor; teljes lezárás nem következik az auditból. |
| DK, Puskás Aréna lehetősége | A tulajdonos felvetése; a fotókon nem biztosan azonosított. | A közelebbi lakóteraszok ettől függetlenek. | Az Aréna láthatóságát későbbi helyszíni irányfotó igazolhatja; nem garantált panorámapont. |
| D–DNy, lakás felé | Saját épülettömeg, homlokzat és visszaforduló oldalerkély-kapcsolat. | Saját épületszárnyakból irányfüggő lehetőség. | Nem szabad 360° akadálymentes körpanorámát feltételezni. |

A Puskás Aréna hivatalos címe Istvánmezei út 3–5.; ez az objektum azonosítását segíti, **nem igazolja**, hogy az A902-ről látható. A fotó kivágása, látószöge és megjelenítési mérete megnehezítheti a távoli részletek észlelését; ebből nem következik, hogy a stadion biztosan ott van a képen. [W3, U06]

Az [iránytérkép](NORTH_NEIGHBOURS_VIEW_PRIVACY_SUN.svg) az égtájakat helyesen rendeli a rajzi tengelyekhez. A kilátási szektorok szemléltető irányok, **nem kimért láthatósági sokszögek**. A szomszédok nincsenek ismeretlen távolságon méretarányos tömegként elhelyezve. Ülő, álló, fekvő és jakuzziban ülő szemmagasságokra nem készült sugárkövetés; a védendő helyek magassága és a szomszéd teraszok pontos helye még nincs meg.

## 6. Napfény és mikroklíma

A profi képeken a gres, WPC, falak és növények napos és árnyékos felületei is látszanak. Ez egy felvételi állapotot dokumentál. A mappa dátuma és a nyers EXIF nem helyettesít hiteles, időzónával egyeztetett felvételi időt. Ezért P0-ban nincs zónánkénti „napi 6–8 óra napsütés” vagy garantált nyári/téli árnyékállítás. [P03–P13]

A tájolás korrigálása után az ÉK-i új épület hatását elsősorban az adott napállás és a felső tömeg tényleges magassága dönti el. A hasonló teraszszint önmagában nem bizonyít árnyékmentességet: tetőfelépítmény és visszalépő felső szint is számít. Ugyanakkor nincs bizonyíték arra sem, hogy ez jelentős teraszárnyékot okoz. **Péter várakozását – nem lesz számottevő új árnyék – megtartjuk feltételezésként.** Az audit nem indokol kötelező új árnyékolót vagy napfényvesztési százalékot. [U05, U07]

Szélcsatorna-hatás, tetőkerti szélerősség, öntözési vízigény, nyári felülethőmérséklet és téli növénymegmaradás nincs helyszíni adatsorral igazolva. Új árnyékoló, növényedény, hangszóró vagy világítás kiválasztása P0-ban nem történt. Későbbi szerkezetnél a szélrögzítés konkrét műszaki feltétel, nem indok a teljes kültér használatának megkérdőjelezésére.

## 7. Víz, áram, jakuzzi, zuhany és kutyarámpa

**Víz:** T09-en meglévő kültéri csap látszik; a terv fagymentes csapot jelöl. A fagymentes jelölés nem igazol minden csatlakoztatott berendezés téli használhatóságát. Vízhozam, nyomás, elzáró helye és melegvíz nincs ellenőrizve. Az öntözőcsövek és fedlapok ténylegesen láthatók. A műszaki kivonat szelepaknát/vízórát és vezérlőcsatlakozást említ; a hivatkozott 027/028 képek e célzott csomagban nem önállóan vizsgált bizonyítékok. [PLAN18, P07, T01, T05–T08, MŰ]

**Áram:** D47 és D48 a két teraszdugalj tervi jelölése. Két szerelvény nem jelent két külön áramkört. A nagyobb doboz fotós megjelenése önmagában nem bizonyítja a jakuzzihoz megfelelő fázisszámot, teljesítményt vagy üzemkész bekötést. Biztosító, vezeték, védelmi eszközök, kapcsolás és egyidejű terhelhetőség nincs auditálva. A tervi FL05/06/07 lámpapont nem jelent már meglévő Hue-rendszert. [EL, P07, T01]

**Jakuzzi:** a helye kötött a T09 előkészítési zónájában; az áthelyezés nem megengedett elrendezési változó. A modell 2×2 m-es doboza illusztratív marker, a tervi szaggatott befoglaló mélysége nem teljesen olvasható. Készülék nincs a vizsgált fotókon telepítve. Készülékméret, szervizoldal, fedélnyitás, belépés, szállítási mód, telített terhelés, feltöltés/ürítés módja hiányzik. A rögzített hely elfogadása mellett ezeket konkrét termékhez kell egyeztetni. [U01, PLAN18, G, EL]

**Kültéri zuhany:** funkcionális igény; meglévő kültéri zuhany és hozzá tartozó szennyvízkiállás nem bizonyított. A csap vagy öntözőkör nem automatikusan alkalmas zuhanyellátás. Hideg/meleg víz, használati mód, fagymentesítés és vízelvezetés külön kérdés. A tető esővíz-elvezetését nem lehet bizonyíték nélkül zuhany-szennyvízcsatlakozásként átadni. A beltéri fürdőfotók ehhez nem igazolások. [B, P16, P25, T01]

**Kutyarámpa:** a teljes beltér→ajtó-fellépő→gres→lépcső→haránt WPC→magasabb közép→gyep útvonalat kell majd megoldani. Nem elég a tervi 62 cm-rel számolni. A brief 1:12-es szemléltető aránya 62 cm emelkedésnél 7,44 m vízszintes hosszt jelent; ez nem kiválasztott nyomvonal, nem kutyaszabvány és nem tartalmazza a fordulókat vagy a további fellépéseket. Kutyaméret és egyedi mozgásképesség, valós szintkülönbségek és szabad sávok nélkül végleges rámpa nem méretezhető. [B, PLAN18, P17–P20, T02]

## 8. Nyitott adatok, amelyekre nem szabad választ kitalálni

| Prioritás | Hiányzó adat | Feloldás módja | Mire hat? |
|---|---|---|---|
| Első | Haránt WPC és középső dobogó pontos szintje; minden útvonali fellépés | Szintező/mérőszalagos helyszíni adat, fotóval megjelölt mérési pontok | Rámpa, lépcső, közlekedés, helyszínhű modell |
| Első | Jakuzzi készülék és fix zóna valós befoglalója/szerviztere | Konkrét termékadatlap és a hely kijelölt határainak mérése | Berendezhetőség és bejutás |
| Első | Dugaljak és jakuzzi kiállás tényleges áramköri adatai | Megvalósult villamos dokumentáció / szakági ellenőrzés | Jakuzzi, konyha, hűtő, fűtés egyidejű használata |
| Első | Zuhany betápja és szabályos vízelvezetése | Gépészeti megvalósulási adat és helyszíni azonosítás | Zuhany megvalósíthatósága |
| Következő | Új ház felső szintek kontúrja, magassága, teraszai, távolsága | Szomszéd terv/metszet és térbeli egyeztetés | Belátási sugarak, tényleges takarás és árnyék |
| Következő | Korlátmagasság, résméret, ajtók szabad szélessége, fedlap-hozzáférés | Helyszíni mérés | Kutyás használat és szabad közlekedés |
| Következő | Zöldtető rétegrendje és konkrét új pontterhek feltétele | Meglévő szakági adat konkrét választott tárgyakhoz | Nagy edények, szerkezetek és készülékek |
| Kiegészítő | É/ÉK réskilátás és Puskás Aréna azonosítása | Ismert irányú helyszíni sorozat, távoli részletfotó | Panorámapontok megőrzése |
| Kiegészítő | Meglévő növényfajok, öntözési körök, szezonális állapot | Kertészeti ültetési terv / helyszíni leltár | Kutyás növényválasztás és fenntartás |

Ezek **az audit nyitott eredményei**, nem a teljes saját terület használati tilalmai. A későbbi kreatív ötlet feltételesen kezelheti őket; a végleges méretvalidálás és kivitelezhetőség azonban nem állítható a hiányzó bizonyíték nélkül.

## 9. Egységes átadás és jóváhagyási kapu

A két későbbi AI ugyanazt a [P0_TENYCSOMAG.md](P0_TENYCSOMAG.md), [geometriai adatlapot](TER_ES_GEOMETRIA.md), [iránytérképet](NORTH_NEIGHBOURS_VIEW_PRIVACY_SUN.svg) és teljes [fotókatalógust](FOTOKATALOGUS.md) kapja. A ténycsomag tartalmazza a funkcionális programot, a 4 M Ft bruttó alapkeretet és az 5 M Ft feltételes alternatívát, a tartalék elvét és a meglévő anyagokat. Nincs benne új elrendezési koncepció vagy kreatív rangsor.

A P0 lezárása nem Render Reality PASS, nem kiviteli terv és nem automatikus P1-indítás. **Péter jóváhagyása szükséges a P1 megkezdéséhez.** Az auditanyag publikálási engedélye ettől külön: kizárólag új, verziózott eredményfájlokra szól, a meglévő projektfájlok és Blender-geometria felülírása nélkül.

[Forrásjegyzék és bizonyítéki státuszok](FORRASJEGYZEK.md) · [Tulajdonosi pontosítások](TULAJDONOSI_PONTOSITASOK.md) · [Böngészhető csomag](index.html)

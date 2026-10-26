# WSG A-902 · Work/Sol Chrome render operátor

Állapot: **ELŐKÉSZÍTVE; ÚJ KÉP NINCS GENERÁLVA. Chrome közvetlen füles kapcsolatára vár.**

A felhasználó új rendelkezése szerint a hosszú operátori megbízás előtti három próba kimarad ebből a sorozatból: nem pilot, nem elfogadott kép és nem blokkoló QA-előfeltétel. Az új futás kizárólag az `operator_request_original.txt` teljes szakmai leírását követi, Claude helyett Work/Sol vezérléssel. Astra marad az egyedüli kreatív tervező.

## Ténylegesen ellenőrzött állapot

- V3.1/V3.2/V3.3 források és archívumok GitHub-auditja a `sources/archive_source_audit.json` fájlban. V3.1: 130 PNG; V3.2: 104 PNG, a 94 első és 10 javító változat mind szerepel a távoli naplóban. A V3.3 átadás régi 58-as archívumszáma elavult.
- V3.3 végleges átadás: `4d2b7e857f034a7080bd62bd249e84a0a8e310e3`, 147 új prompt.
- Chrome natív alkalmazásként olvasható volt, a külön ChatGPT-ablakban High látszott. Közvetlenül címezhető Chrome-fülek ebben a chatben még nem jelentek meg; az elérhető böngészők között csak a beépített böngésző és MCP Apps szerepelt.
- A natív Chrome-vezérlés többször megszakadt ablak-/fókuszváltozáskor; az automatikus ellenőrzés az ezutáni általános olvasást elutasította, mert nem garantálható, hogy a feladat ChatGPT-ablakára irányul. Nem folytattuk más magántartalom olvasásával.
- A kilenc referenciafájl helyben összeállt. A Toni160 pontos SKU-ja, mérete és világos tölgy megjelenése a Westwing hivatalos termékoldalán feloldva; a gyári kép letöltve és megtekintve. A teljes prompt beküldésre előkészítve, **még nem elküldve**.

## Futási rend a Chrome bekötése után

1. Egy új S01 C Cam12 pilot; Image1 az eredeti, változatlan Blender-kép, utána a három manifest szerinti profi helyiségfotó, majd az öt pontos termékfotó a referenciajegyzékben megadott sorrendben. Minden csatolmány készre töltését és a teljes szövegegyezést ellenőrizni kell. High minden beküldés előtt ellenőrizendő.
2. Egy kérés pontosan egy képet készít. Eredeti PNG-letöltés, hash, QA és távoli checkpoint után kap kész státuszt. A műszaki/katalógus/szakági feltételek külön maradnak; KONCEPCIÓ – NEM VALIDÁLT.
3. Sikeres új pilot után két, majd legfeljebb három saját Chrome-fül: egyetlen operátor sorban tölti fel és indítja őket, a generálások várakozási ideje átfedhet. Egyszerre nem vezérli ugyanazt a Chrome-ot Claude vagy másik Computer Use feladat. Fülenként egy aktív képkérés; ne legyen egy kérésben több képes batch.
4. A soron következő kész referencia-csomagú tételt kell kiosztani. Stíluson belül a manifest és az Astra átadási sorrendje az irányadó. A termék-/kamerahiányos sor HOLD, más kész sorral lehet haladni. S16/S17 esetén a tulajdonosi autófotók tényleges bemenetek az Astra szerepkiosztása szerint; nem építészeti és nem kamerareferenciák.
5. Nincs kreatív átírás, rövidítés, bútorcsere. Képszám/sorrend, kép1-kamera, falak/nyílások, bútorazonosság, eredeti anyagok, világítás és hozzáférés ellenőrzése képenként; takart elem NEM ELLENŐRIZHETŐ. Célzott v2/v3 külön fájl, az eredeti megmarad.
6. A teljes ellenőrzött képtár után indul a négy lookbook. Keretelfogyáskor pontos checkpoint és megállás; nincs kerülőút.

## A korábbi Claude QA alkalmazása

A történeti S01-jelentés kiegészítése rögzíti a tulajdonos akkori Cam12-v1 „tervközeli” elfogadását és a későbbi döntést: a teljes képes bútorazonosság-referenciát már nem használják. Ezt a módszert követjük: az archív teljes rendert nem csatoljuk automatikusan kamera- vagy bútorreferenciaként. Az új kép kameráját az Image1 adja, a bútorét a konkrét termékfotók. A tervközeli képstátusz különbözik a numerikusan igazolt kamera-/Render Reality PASS-tól; egyiket sem állítjuk mérés nélkül. A korábban elfogadott koncepciószintű tűrést nem helyettesítjük önkényesen pixelpontos sikerfeltétellel.

## Következő kapcsolati lépés

A hivatalos útmutató: https://learn.chatgpt.com/docs/chrome-extension . Beállítások → Computer Use → Chrome: Manage és bekapcsolt elérhetőség; majd @Chrome vagy a megfelelő Chrome-fül csatolása ehhez a chathez. A helyi feltöltéshez az útmutató szerint szükség lehet az extension „Allow access to file URLs” engedélyére, amit a tulajdonos állít be. Az alkalmazás saját beállításait a natív eszköz biztonsági szabálya nem engedi nekünk megnyitni.

Az `images/` és `prompts_sent/` az új futásban üres. A `prompts_prepared/` tervezet, nem sikeres beküldés. API, extra kredit és vásárlás nem történt.

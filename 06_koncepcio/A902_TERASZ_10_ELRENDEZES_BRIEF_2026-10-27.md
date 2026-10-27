# WSG A-902 – 10 különböző tetőterasz-elrendezés: kreatív és műszaki feladatbrief

**Azonosító:** `A902-TERASZ-10-ELRENDEZES-V1`  
**Dátum:** 2026-10-27.  
**Státusz:** Feladatindításra **előkészített brief**, render/HTML/Blender-módosítás nincs elindítva.  
**Hely:** WSG A-902 penthouse, Budapest.  
**Kapcsolódó, kötelező prezentációs szabvány:** [Háromrétegű teraszprezentáció, 4 + 2 képes verzió](WSG_ALAPRAJZI_PREZENTACIO_3_RETEG_2026-10-27.md).

## 0. A feladat egy mondatban

Tervezd meg a **valódi, többszintű, 150,4 m² nyilvántartott kültéri területre** az A-902 tetőterasz **10 lényegileg eltérő, funkcionálisan használható, költségre előszűrt elrendezését**; mindegyiknek készíts magyarázó 2D/műszaki alaprajzot, pro-kontra és keretkockázat-elemzést, majd az elfogadott geometria és koncepció birtokában összesen négy nappali nézetet. Későbbi opcionális kiegészítésként koncepciónként két esti 3D nézet is készülhet, összesen hatra bővítve a sorozatot. A tíz változat egyazon vizuális sablonban, **összehasonlítható HTML-katalógusban** szerepeljen.

**Elsőbbség most: elrendezés, használhatóság, valós geometria, költséghatár.** A Tulum/Bali/Ibiza/Marbella/Japán/stb. stílusvilág később választható rá a nyertes elrendezés(ek)re; a tíz opció nem lehet pusztán tíz eltérő színpaletta.

## 1. Kötelező források és forrásrang

Indításkor frissen olvasd el, és jegyezd fel a forrásverziót:

1. `GOAL.md`; `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`; `OPENAI_instructions.md`.
2. `ai-coordination/RENDER_REALITY_GATE.md`; `ai-coordination/HANDOFF_PROTOCOL.md`; adott esetben `ai-coordination/ROUTER.md`.
3. Valódi, méretezett terv: `01_alaprajzok/` és a megvalósulási/kiosztási terv releváns PDF/vektoros mellékletei; **méretet nem fotóból találunk ki**.
4. A terasz előzetes Blender-forrása `03_blender/WSG_A902_v2_terasz_ELOZETES_20261024.blend`, illetve a legfrissebb **ténylegesen érvényes és ellenőrzött** geometria/lock (nem szabad automatikusan régi változatra visszaállni). A fő lakásmodell `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` önmagában nem bizonyít minden teraszszintet.
5. **Profi fotóarchívum:** `08_allapotfelmeres/fotok_profi_20261025/A902/` (33 fotó) + `README.md`, `LELTAR_profi_20261025.csv` és `FOTOKAMERA_LATVANYTERV.md`. Különösen KZS 3488 (greslap), KZS 3498 (zöldtető–homlokzat) és KZS 3483 (iránybesorolása bizonytalan). A képek teljes felbontású, de **retusált/vágott, EXIF nélküli fotók**; alkalmasak a látvány, anyag, szint, kilátás és nyílások vizsgálatára, de önmagukban nem hiteles méret- vagy égtájforrások.
6. Az alábbi, e beszélgetéshez csatolt **három képfájlt** külön csatold az Astra/Work indítófeladatához. **Nem a WSG valós adottságai, kizárólag ábrázolási etalonok:** `2d.jpeg` (fotóéles felülnézet), `4es design.png` (festői/építészeti 3D axonometria), `6os design.png` (fotórealisztikus 3D axonometria). Ezek a fájlok **nem kerültek be automatikusan a GitHub-repóba**, a futtatásnál kézzel kell csatolni őket.

Minden bemenet: `IGAZOLT / TERV SZERINT / BECSLÉS / HIÁNYZIK` státusszal; ütközést külön döntési listába, semmi csendes modellátírás.

## 2. A terasz valós, kiinduló adottságai – nem designjavaslat

A `GOAL.md` jelenlegi rögzítése szerint:

- Gres szakaszok **23,62 m² és 19,34 m²**, emelt WPC **25,00 m²**, erkély **11,26 m²** → összes terasz/erkély **79,22 m²**;
- további zöldtető **71,18 m²**, összes kültér **150,40 m²**;
- a WPC-felület kiemelése tervi adatként körülbelül **+62 cm**, pontos fellépők és valódi szabad méretek ellenőrizendők;
- több síkú zöldtető, gyepes peremek és évelőágyás, meglevő betonperem, korlát, homlokzat és nyílászárók;
- a nyugati gresfelületen **jakuzzi-előkészítés**. Ez önmagában **nem** igazolt teherbírás, bekötési kapacitás vagy engedély.

Minden fix sík, burkolat, szintkülönbség, bejárat, víz/elektromos kiállás, korlát és tetőszigetelés változatlan marad, hacsak az átalakítás ténylegesen engedélyezett, tételesen beárazott és jóváhagyott. A zöldtető nem automatikusan szabadon járható vagy a kutyának kijelölhető rész.

## 3. Pénzügyi keret – a nehézséget ne rejtsd el

- A WSG A-902 **teljes lakására 20,0 M Ft bruttó** a rögzített plafon, minimum **10% projekt-tartalékkal**. A `GOAL.md` a kültérre jelenleg kb. **4,0 M Ft-ot** irányoz elő.
- Péter a teraszvizsgálatban **4–5 M Ft teljes kültéri keretet** mérlegel. A **4 M Ft-os eset a hivatalos alap**, az **5 M Ft-os külön, feltételes forgatókönyv**, amelyet nem lehet csendben hozzáadni a lakás húszmilliós keretéhez; csak a teljes kereten belüli, ellenőrzött átcsoportosítással vagy külön felhasználói döntéssel tárgyalható.
- A jakuzzira kb. **2 M Ft bruttó célszám** hangzott el: **előzetes felhasználói feltevés, nem beszerzési/telepítési ajánlat**. Bruttó teljes bekerülésében számolj gép, fedés, emelés/szállítás, alátámasztás, villany/víz/lefolyó, üzembe helyezés, téli kezelés, szervizhozzáférés és kiegészítő burkolat elemeivel. Ha a 2 M nem fedezi ezeket, a különbözetet mutasd ki.
- Ezzel a 4–5 M Ft-os teraszcsomagból nominálisan **2–3 M Ft marad minden másra** a jakuzzi feltételezett 2 M Ft-ja után (nem feltétlenül szabadon elkölthető, még lehetnek rejtett költségek). Nincs ingyenes kültéri konyha, öntöző-/villamos-átalakítás vagy korlát.
- Minden koncepciónál kötelező: kategóriánkénti bruttó **alacsony / várható / konzervatív magas sáv**, forrás és dátum vagy „becslés”, a teljes bekerülés a **4,0 M alap** és **5,0 M feltételes** esethez, maradvány, tartalék, és `NEM FÉR / FELTÉTELES / ELŐSZŰRT` jelzés. A funkciók prioritása és halaszthatósága legyen látható.
- A külső berendezés hatásának töredék költségen történő elérését preferáld. Ne ábrázolj 10–15 M Ft-os színvonalú, tétel nélküli beépítéseket 4 M Ft-os reális opcióként. A stílusos, egyszerű és visszabontható kész termék gyakran jobb, mint a költséges egyedi építés.

## 4. Funkcionális program — mindegyiket mérlegeld, de ne erőltesd mindet minden tervbe

### A. Spa / fürdés / privát pihenés
- Jakuzzi elsősorban a meglévő előkészítés logikus környezetében; alternatív hely csak **szerkezeti és gépészeti feltételek feltüntetésével**. Vizsgálj költséghatékony, hozzáférhető, szervizelhető **részleges körbeburkolást** is, de ne rejtsd el a karbantartó oldalt.
- **Kültéri zuhany** a jakuzzi közelében, trópusi spa-hangulattal, a vízkiállás esetleges szabályos megosztásával. **Csak akkor fizikai javaslat, ha** a víznyomás, hideg/meleg víz, szabályos lefolyás, megfelelő visszafolyásvédelem, csőfagyás elleni leürítés és társasházi jóváhagyhatóság tisztázott. A „kettéosztjuk a csövet” **nem** automatikus kiviteli megoldás.
- Privát, akár meztelen napozásra is alkalmas intimitás a valós szomszédos kilátások figyelembevételével, **nem** a szép render által sugallt hamis takarás.

### B. Kutyás zóna – francia bulldog
- Külön, valóban elérhető, biztonságos kutyajátszó-, pihenő- és potenciális illemhely; a zöldtető megközelíthetősége, terhelhetősége, higiéniai/öntözési/szigetelési következményei **ellenőrizendők**. Ha a meglévő gyep nem használható így, javasolj külön, engedélyezhető és takarítható alternatívát.
- Lehetőleg WPC-hez vizuálisan illő **csúszásmentes, mérsékelt hajlású rámpa**, ne kötelező lépcsőzés. A 62 cm-es szintkülönbségnél a *példa* 1:12 vízszintes rámpaszakasz ~7,44 m, ehhez forduló/pihenő hely is kell; ez **nem előírt univerzális kutyarámpa-méret**, hanem a geometriai helyigény nagyságrendjének érzékeltetése. Változtatható megközelítés, lépcsőt megkerülő út vagy rövidebb rámpás alternatívák valós helyigénnyel vizsgálandók.
- Árnyékos visszavonuló hely, hőségnek kitett WPC/padlófelületek és csúszásveszély vizsgálata, kültéri növények kutyabiztossága.
- Kedves, visszafogott **francia bulldog motívum** opcionálisan cserélhető tárgyon, párnán, kerámián vagy diszkrét táblán; nem giccses fix építészeti elem.

### C. Különféle pihenőfunkciók
- **Napozózóna**: napágyak és/vagy baldachinos/függönyös ágy csak ha szél- és rögzítési feltételei valósak; egyes változatokban több napozás, másokban több árnyék.
- **Lounge**: kényelmes elnyúlás (L-kanapé / fotelek / kültéri daybed / függőágy valós rögzítéssel). Legyen társasági, italos, hosszabb időre hívogató, de ne akadályozza az átjárást.
- **Étkezés**: kültéri asztal használható székekkel, az ajtóhoz/konyhához való praktikus távolság és a kihúzott székek szabad helyigénye figyelembevételével.
- **Dolgozóhely / naplementenézés**: kényelmes, stabil munkafelület, árnyékolt képernyő, megfelelő energia/Wi-Fi, **északi–nyugati / északnyugati panoráma** a tényleges tájolás és fotók igazolása alapján; évszakfüggő napállással.
- **Mozizós/sportközvetítés**: lehetőleg a lounge többfunkciós használata; kivihető projektor/összecsukható vászon, a napfény és vetítési távolság reális korlátaival, kültéri időjárásbiztos tárolással. Nappali tévénézési ígéret ellenőrizetlenül tilos.
- **Mini kültéri konyha / drink station**: mobil vagy kis modul, italhűtő/kiszolgálópult. Valódi víz/áram/évszakos tárolás/szél/környezetvédelem alapján; külön alternatíva **víz nélküli, hordozható bár**.

### D. Hang, fény és növényzet
- Kompakt, jó minőségű, lehetőleg diszkrét kültéri hangszórók, több zónában opcionálisan. **A nyitott tetőterasz hangja nem tehető hangszigeteltté pusztán növénnyel**: elhelyezés, irányítottság, hangerő, mélyhang, rezgéscsillapítás és házirend szerinti használat legyen a valódi megoldási csomag. A kemény visszaverő panel akár ronthatja is a szomszéd felé terjedést; ilyet csak szakvéleménnyel tervezz.
- **Philips Hue-kompatibilis hangulatvilágítás**: lépcső-, lounge-, jakuzzi-, étkező-, növény-akcentfény külön, este meleg és alkalomszerűen színes jelenetek. Valós kültéri IP/elektromos megfelelés, áramellátás, szerelés, kábelezés, Wi-Fi/bridge és bruttó ár. A terasz két ismert dugalja és az öntözőrendszer áramkiállása csak **helyszíni / villamos biztonsági ellenőrzés után** használható; ne tervezz automatikusan új vezetéket, vésést vagy túlterhelést.
- **Plusz növényzet**: Budapest tetőteraszára és téli klímájára alkalmas, viszonylag alacsony fenntartásigényű fajok, szél, nyári hő, szigetelés, konténer- és talajsúly, öntözés és vízelvezetés ellenőrzésével. A pálmák kreatív opciók, **külön téliesítési / edényfagyási / gondozási kockázattal**; ne nevezd őket bizonyíték nélkül egész évben gondozásmentesnek. Ne nehezítsd el a tetőt nem igazolt teherbírással.

## 5. Égtáj, benapozottság, szomszédok és a valódi panoráma – kötelező külön audit

**Péter leírása mint vizsgálati kiindulás, NEM igazolt helyszíni láthatósági mérés:**

- Nappaliból kilépve az előrenéző **délkeleti**, illetve a jobb kéz felőli **keleti/délkeleti** oldalon szomszédos épületek, köztük előre egy kb. hatszintes ház. Belátás zavarhatja a napozást, jacuzzit és privát együttlétet.
- Balra és átlósan előre-balra a kilátás/panoráma nagyobb érték; **nem** szabad automatikusan eltakarni.
- Északnyugat / nyugat felé fontos a naplemente és az ott ülve, laptopon dolgozva átélhető kilátás.

**Szükséges kimenet (szemléletes és ellenőrizhető):**
1. Hiteles **É-jel / tájolás** + azonosított szomszédos épületek (látószög és lehetőleg épületmagasság) + tényleges, fotóhoz kötött panorámaszektorok térképe; kétes látóirány „FELTÉTELES”.
2. Zónánként **belátási mátrix**: mit lát a szomszéd lakásból magasabb/alacsonyabb szögből? Ülve/fekve/jakuzziban hogyan változik? Növény csak akkor biztos takarás, ha a **szemvonalat ténylegesen metszi**; emeleti belátásnál vízszintes/oldalsó pergolás árnyékoló is külön vizsgálandó, szél- és szerkezeti korláttal.
3. **Benapozási tanulmány** külön évszakokra és napszakokra (nyári/téli napforduló és napéjegyenlőség, kora délelőtt, dél, délután, naplemente közelében) a valós épületsziluettel/teraszgeometriával; ne a render véletlen árnyékából következtess.
4. **Intimitás vs panoráma kompromisszum:** csak a valós belátási irányban emelj növényt/mobil takarást; nyugati–északnyugati panoráma lehetőség szerint maradjon nyitott. Vizsgáld az árnyékolás, zaj, fenntartás és szélterhelés hatását.
5. Minden 3D nézetben azonos, helyes **É / DK / ÉNy** jelölések, és ha kell külön bemutató lap `VIEW / NEIGHBOUR / SUN` rétegek. Nem szabad a takarást kedvezőbb kameraállásból „bizonyítani”, mint a valós szomszéd látószögéből.

## 6. Valós megvalósíthatósági előszűrés – a tervezés előfeltételei

**Helyszíni, műszaki és jogosultsági ellenőrzés kell, mielőtt az adott funkció reálisként kerül a költségtáblába:**

- tetőszerkezet teherbírása **vízzel, emberekkel és kiegészítő szerkezettel terhelt jacuzzira**, dinamikus terhelés, rezgés, terheléselosztás;
- vízszigetelés, tetődrén és lefolyók, karbantarthatóság, talajterhelés, pangó víz; új áttörés nem feltételezhető;
- zuhany vízellátásának/lefolyásának jogszerűsége, fagymentesítés, villamos–vizes zónák biztonsága;
- kültéri elektromos körök, dugaljak, meglévő vezetékezés, kioldásvédelem, teljesítmény, Hue/elektromos termékek kültéri alkalmassága;
- a terasz szélviszonyai, pergola/baldachin/árnyékoló rögzítése, társasházi házirend és esetleges engedély;
- kutyás gyep használhatósága, hozzáférés, öntözés/ürítés, tisztítható burkolat, a tetőkert kezelésének korlátai;
- tetőre emelendő nehéz elemek logisztikája, elférés/fordulók/nyílásméretek, hozzáférés a jakuzzi szervizoldalához;
- visszaverődő hang/áthallatszás kockázata; ne állíts zajszigetelési garanciát nyitott teraszra.

Minden `BLOCKER` mellé: ok, szükséges ellenőrzés, milyen egyszerűbb, olcsóbb és technikailag megvalósítható `B` terv van.

## 7. Tíz, ténylegesen eltérő térszervezési változat

A tíz terv különbsége **a funkciók helye és kapcsolata**, nem csak a bútorok színe. Ötletindító, nem kötelező, geometria előtt nem validált irányok:

1. **Sunset Lounge:** a legjobb kilátásra és munkasarokra optimalizált lounge; külön rejtett spa.
2. **Spa Sanctuary:** jakuzzi + zuhany + intimitás a fő élmény; társasági zóna másodlagos.
3. **Social Dining First:** nagy étkező és mobil italbár dominál; kisebb privát pihenő.
4. **Resort Sun Deck:** napozó és baldachin árnyék/napsütés-tengely mentén, könnyű átrendezhetőség.
5. **Dog Garden Loop:** kutyának biztonságos, folyamatos út/rampakoncepció és elérhető, tisztítható zöldzóna a fő szervezőelem.
6. **Rooftop Cinema Club:** lounge + árnyék + esti projektoros nézőirány és diszkrét hang.
7. **Two Islands:** külön beszélgetős és csendes/nappali pihenőzóna, minimális kereszteződés.
8. **Garden Privacy:** belátást szűrő növényszigetek, meghagyott panoráma-kilátással.
9. **Flexible Minimal Luxe:** kevés, sokfunkciós, mozgatható bútor, jobb ár és nagyobb szabad terület.
10. **Outdoor Living + Compact Kitchen:** kompakt kültéri kiszolgálás és étkezés, jól használható lounge.

Mindegyiknél kötelező ugyanazoknak a programigényeknek az elbírálása: `megvalósul / kompromisszummal / nem fér be / nem igazolt`, konkrét fizikai okkal és árhatással. Indokolt esetben egy-egy irány elvethető és helyettesíthető **egy valóban más szervezésű, megvalósítható** változattal.

## 8. Összehasonlítható kimenet minden koncepcióhoz

`C01`…`C10` azonosítók, mindegyikhez:

- 1 mondatos térélmény, alapzónák (jakuzzi, zuhany, lounge, étkező, napozó, kutya, munka, mozi, mini konyha, növény), tájolás és közlekedési logika;
- méretezett, valós koordinátákra épülő **zónatérkép** és berendezési blokkok valódi befoglalói; minimális / legszűkebb szabad közlekedőket színnel és mérettel mutassa;
- zónánkénti nap/árnyék, belátás, panoráma és esti hangulat lehetősége, a valós tájolási tanulmány alapján;
- **legalább 3 pro és 3 kontra**, benne külön pénzügyi, fenntartási és kivitelezési probléma;
- kategóriás, dátumos **bruttó 4 M / 5 M összevetés**, 10%-os teljes projekt tartalékszabály figyelembevételével, dupla tartalék levonása nélkül; költségazonosítóval;
- külön `BLOKKOLÓ / ELLENŐRIZENDŐ / ELŐSZŰRT` státusz és szükséges műszaki bizonyíték;
- áttekintő rangsor szubjektív szempontokkal (WOW, privát szféra, panoráma, kutyás kényelem, vendéglátás, rugalmasság, fenntartás, keretbiztonság) **nem összekeverve tényekkel**;
- opcionális kültéri stíluscímke (pl. Japán, Bali, Miami, Los Angeles, Tulum, Mykonos, Ibiza, Provence, Portofino, Marbella, skandináv vagy új trend), de a bútorkiosztás nem stilizálás útján legyen eltérő.

## 9. 4 + 2 képes megjelenítési séma – pontosan ugyanazon tervállapotról

**Alapsorozat: 10 koncepció × 4 = 40 kép.** Opcionális teljes sorozat: **10 × 6 = 60 kép**, esti bővítés külön engedéllyel.

| Nézetkód | Kép | Feladat / referencia |
|---|---|---|
| **01** | Nagyon éles, prémium **2D felülnézet** | `2d.jpeg`. Fotórealisztikus anyagok, precíz teraszburkolat, élő növénytextúrák, esztétikus, nem technikai |
| **02** | **Méretezett műszaki 2D** | nettó terasz-szélesség × hosszúság, m², WPC-szint, lépcső, közlekedő legszűkebb pontja, funkciók és kerítések |
| **03** | **3D axonometria A – NAPPAL** | `4es design.png` építészeti/vízfesték-szerű stílus; rögzített `CAM_A`, amely a kilátás és a szintek érthetőségét szolgálja |
| **04** | **3D axonometria B – NAPPAL** | `6os design.png` fotórealisztikus, textúragazdag stílus; **eltérő**, rögzített `CAM_B`, amely a szomszédságot és zónákat kiegészítő irányból mutatja |
| **05** | **3D axonometria A – KÉKÓRA/ESTE** | ugyanazon `CAM_A` + ugyanazon építészeti/funkcionális tartalom és 03-as stílus, valódi világítás; **opcionális** |
| **06** | **3D axonometria B – KÉKÓRA/ESTE** | ugyanazon `CAM_B` + ugyanazon építészeti/funkcionális tartalom és 04-es stílus, valóságos Hue-jelenet; **opcionális** |

**Kiemelten fontos:** `CAM_A` és `CAM_B` helyzete, vetülete, kivágása és méretaránya **mind a tíz koncepcióban rögzített és dokumentált**. A látványtáblák azonos layouttal, elnevezéssel, felirattal, világítási alapbeállítással és felbontással készüljenek. A műszaki 2D lapot ne render „rajzolja”; tényleges tervi méretadatból **vektorosan** készítsd. Minden nézeten mutasd meg a valós É/DK/ÉNy, `KILÁTÁS` és `SZOMSZÉD / BELÁTÁS` jelzéseket a nézethez illő módszerrel: a képen visszafogott overlay, a HTML-ben kapcsolható rétegek.

A három beküldött kép **minimum vizuális részletességi és élességi cél**, nem jogcím az eredeti épület-, növény- vagy tárgyelrendezés átvételére. A tényleges render minőségét és pontosságát külön elfogadási teszttel kell megítélni, **nem megígérni**.

## 10. Kért HTML-prezentáció

Készüljön **ténylegesen működő**, az átadott képekhez kötött `index.html` / szükséges lokális assetek (vagy önálló HTML, ha a képmennyiség mellett fenntartható) **azonos vizuális sablonnal**. A képek ne legyenek CSS-ben kitalált tervek.

Minimum funkciók:
- 10 koncepció kártya és azonos tipográfia; az alapképek 01–04, az esti 05–06 csak ha léteznek;
- képváltó és nagyítás, 2–3 koncepció egymás melletti összehasonlítása;
- `panoráma / szomszéd / belátás / napfény / közlekedő-szélesség / akadály / költség` szemléletes jelmagyarázat vagy kapcsolható overlay (ha ténylegesen alátámasztott);
- 4 és 5 M Ft-os sávváltás és kategóriákra bontott, forrásmegjelöléses költségsor, pro/kontra és blocker;
- minden lap mellett **forrás-, modell-, kamera-, koncepció-, verzió-, dátum- és státuszjelzés**, mobilon/asztalon is működő navigáció;
- az eredeti, nagy felbontású képek és a vektoros méretezett terv letölthetők legyenek; ne csak beágyazott, kisfelbontású preview legyen;
- a HTML működését ellenőrizd böngészőben; nem elegendő csak HTML-szöveget vagy egy nem működő gombokkal teli mockupot leadni.

## 11. Ajánlott végrehajtási munkaszakaszok

Az összes kép azonnali generálása helyett **ellenőrzött lépcsőzetes gyártás** — a végső cél ettől még a 10×4, opcionálisan 10×6:

1. **P0 – Valóság-térkép:** méretezett teraszszintek, geometriaváltozatok, fotó- és kilátásirány-audit; panoráma/szomszéd belátás, csatlakozók, szerkezeti/engedély-kockázatok; bizonytalanságlista.
2. **P1 – Elrendezési verseny:** 10 ténylegesen eltérő, még anyag- és stílussemleges layout, méretezett, bejelölt használati blokkokkal; pro-kontra, 4/5 M sávok. Az első döntési kapu az elrendezés: ne a drága látvány győzzön a működő terv helyett.
3. **P2 – Mintalap:** egy (legfeljebb két) fontos koncepción 01–04 nézetet készíts, szigorú geometriagáttal és vizuális minőségvizsgálattal; szükség szerint javítsd a gyártási sablont.
4. **P3 – Teljes 10×4:** minden validált koncepció ugyanazzal a sablonnal, a felületi/textúra ellenőrzéssel, 40 nappali képpel és működő HTML-összehasonlítóval.
5. **P4 – Esti 05–06:** csak **külön megrendeléssel**, amikor a konkrét Hue/elektromos/árnyékolási és egyéb elemek már valós vagy beárazható specifikációval megvannak. A döntős koncepciókra részleges, vagy külön utasítással mind a tízre teljes esti sorozat.

Az első geometriagáttól **nem szabad átugrani** a 40–60 képes fázisra. Bármelyik fotó-hallucináció, teraszszint-/rámpa-/szomszéd-/területdrift, kívülről be nem árazott funkció vagy a szabad áthaladás romlása `FAIL / JAVÍTÁS` listára kerül.

## 12. Minőségellenőrzés és szerepek

**Claude**: aktuális, hiteles méretezés / Blender geometriamodell és teraszszintek, fotók beazonosítása, tervek műszaki/engedély-előszűrése, **független** költségkontroll és repó koordináció.  
**ChatGPT Work/Astra**: kreatív, fizikailag értelmes térszervezés, 10 koncepció versenyeztetése, vizuális rendszer és HTML, termék/ár kontroll.  
**Codex**: független geometriai/objektum-/közlekedő-/kamera-ellenőrzés; a Claude által használt élő Blender MCP-t ne vegye át párhuzamosan.  
**Péter**: keretváltoztatás, végső elrendezés, indítások és kivitelezés jóváhagyása.

**Átadás minimum:** `SOURCE_STATUS.md` (forráslista/eltérések), `LAYOUTS_C01-C10.md` vagy CSV (zónapozíciók/bútorbefoglalók), `COSTS` (bruttó két forgatókönyv), `VIEW_MATRIX`, működő `index.html` képekkel, `GATE_AUDIT` (valós geometriához és érvényes terméklistához mért eltérések), végső ajánlás több győztes iránnyal, **nem** a felhasználó helyett egyetlen végső választással.

## 13. Felhasználói rövid indító mondat

**A nagy kreatív feladathoz** kérlek használd a `A902-TERASZ-10-ELRENDEZES-V1` briefet itt:  
`06_koncepcio/A902_TERASZ_10_ELRENDEZES_BRIEF_2026-10-27.md`, továbbá a  
`06_koncepcio/WSG_ALAPRAJZI_PREZENTACIO_3_RETEG_2026-10-27.md` megjelenítési szabványt. Olvasd be a kötelező GitHub-fájlokat és az A-902 profi fotóit. Mellékelem a három valódi referenciaképet: `2d.jpeg`, `4es design.png`, `6os design.png`. Először P0/P1: tíz különböző térszervezés, műszaki/zónás rajzok, pro-kontra, valós 4/5 M Ft-os keretsáv. **Ne indítsd a 40–60 képet P0/P1 jóváhagyása előtt.** Később négy nappali nézet/koncepció, az esti kettő csak külön jóváhagyással.

**Ez az MD létrehozása önmagában nem indít Astra Worköt, nem nyit PR-t, nem ír át Blender-modellt, nem rendel terméket, nem küld külső megkeresést.**

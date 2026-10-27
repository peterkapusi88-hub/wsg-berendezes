# WSG A-902 – egységes P0-ténycsomag

**Verzió:** P0-v1, 2026-10-27. **Állapot:** jóváhagyásra átadott forrásaudit; a P1 nem indult el. **Forrás-commit:** `4959bfe143833617d220b1613bd58908ee4ec5b7`. Azonos tartalmú példányt kell adni mindkét későbbi kreatív AI-nak. Ez a fájl önállóan tartalmazza a döntő bemeneteket; a mellékelt jelentés, geometriai adatlap és fotók a részletes bizonyítékok.

## Elsőbbséget élvező tulajdonosi pontosítások

**A teljes saját kültér használható. A jakuzzi helye fix, máshova nem helyezhető.** A régi fájlok zöldtetőre vonatkozó általános tiltó mezőit nem kell alkalmazni. A konkrét eszköz mérete, terhe, szerelhetősége és bekötése külön műszaki adat, amelyet nem szabad kitalálni. [U01](TULAJDONOSI_PONTOSITASOK.md)

A nappaliból kilépve **szemben épülő, Péter közlése szerint 9 emeletes házzal**, várhatóan hasonló magasságú penthouse-/teraszszinttel kell számolni. Kötelező belátási irányok: a szemközti új teraszok, továbbá saját és új házak **K/DK** ablakai és teraszai. A korábbi kb. hatszintes ház feltételezése elavult. A valószínű érintett beruházás a Park West Rise (Szabolcs utca 15); a beruházó kilencemeletes, teraszos/penthouse-os épületet közöl. A pontos szomszédkontúr és az azonos teraszmagasság ettől még nem igazolt. [W1 a forrásjegyzékben](FORRASJEGYZEK.md) A jelenlegi nyitott építkezési háttér nem tekinthető véglegesnek. Az új épület a saját látószögében takarhat; nem szünteti meg automatikusan a többi panorámaszektort. [U03–U05](TULAJDONOSI_PONTOSITASOK.md)

**Ny/ÉNy panoráma megőrzése fontos; É/ÉK felé is lehetséges kilátás, DK felé esetleg Puskás Aréna.** Az utóbbi két irány tulajdonosi lehetőség, az Aréna képi azonosítása nem biztos. DK felé a belátást és a távoli kilátást egyszerre kell kezelni. Péter nem vár jelentős új árnyékot; ez nem igazolt benapozási számítás. [U05–U06](TULAJDONOSI_PONTOSITASOK.md)

## Bizonyítékok és koordináták

- **TERV:** eredeti PDF 3. lap = 2026.07.08-i, 1:125-ös megvalósulási szintalaprajz; 18. lap = 1:50-es A902 vevői módosított terv, M1 KORR2, 2025-ös korrekciókkal. Nem ugyanaz a dokumentumstátusz. A teljes kert a 18. lapon nincs rajta.
- **FOTÓ:** mind a 33 A902 profi fotó átnézve. Három `x` változat vágott pár, nem három új helyszíni nézet. A 19 külső kép közül 9 környezeti kiegészítés; egyik közös kert sem az A902 tetőkertje. A fotó anyagot/formát igazol, centimétert, teherbírást vagy abszolút irányt nem.
- **MODELL:** a v2b fájl 43 teraszeleme a lockhoz 0,5 mm-en belül illeszkedik. Ez belső adatkonzisztencia, nem helyszíni megfelelőség. A képekkel több eltérés van.
- **Rajzi koordináták:** méter, x jobbra, y felfelé; a lakás a fő terasz alatt. A régi „x kelet, y észak” címkét ne tekintsd igazolt földrajzi tájolásnak. A két terv északjele kb. 40°-kal eltér; a szintalaprajzi jel helyszínvázlatban szerepel. A tulajdonos észak-felfelé műholdképe és az 1:50-es terv együtt a +y ≈53° (ÉK), +x ≈143° (DK) munkatájorientációt támogatja. A nappaliból egyenesen kifelé ÉK, balra ÉNy, jobbra DK. Ez térképi következtetés, nem geodéziai mérés. [U07; TER_ES_GEOMETRIA.md]
- **Modell z=0:** belső padló referencia; a valós kültéri magasságoknál a terv abszolút szintjét és a fotós eltérést is tartsd meg.

## Területek és térkapcsolatok

| Terület | Tervi adat | Kapcsolat / jelenlegi modell befoglalója |
|---|---:|---|
| T09 gres + lépcső | 23,62 m² | Nappali széles üvegfala előtt; x 3,44–9,29; y 8,50–12,40. Itt a jakuzzi kötött előkészítési helye. |
| T10 gres + lépcső | 19,34 m² | 05.3 szoba előtt; x 11,39–16,27; y 8,50–12,40. |
| T11 WPC összesen | 25,00 m² | Középső sáv, harántsáv, kertbe nyúló platform és távoli kis pihenő. Nem kezelhető egyetlen igazolt vízszintes síkként. |
| T12 zöldtető | 71,18 m² | Két oldalsó gyepes rész, középen dombos vegyes ágyás, csövek és szerelvényfedlapok. Teljes terület használható U01 szerint. |
| T13 oldalerkély | 11,26 m² | 05.1 és 05.2 előtt, L alak; nem a nagy tetőterasz részeinek egybefüggő folytatása. |
| Összes saját kültér | **150,40 m²** | 79,22 m² terasz/erkély + 71,18 m² zöldtető. Nem ugyanennyi sík, akadálymentes vagy nettó bútorhely. |

A modell T09 és T10 téglalapjai 22,815 és 19,032 m²; a négy WPC-téglalap 26,545 m²; az erkélypoligon 11,884 m². Ezek **nem** helyettesítik a tervi területeket, és nem igazolt nettó méretek. A részletes koordináták a [geometriai adatlapban](TER_ES_GEOMETRIA.md), géppel olvashatóan a `geometry.json` fájlban vannak.

## Kötelező szint- és geometriai korrekciók a gondolkodásban

1. A terv gres **+28,40**, WPC **+29,02** értéke közötti különbség **0,62 m**. Ez nem bizonyítja, hogy minden WPC-rész azonos magasságú.
2. A fotók és különösen a **ME-BAL-102** közeli kép egyértelműen mutatják: a középső dobogó/nyelv magasabb az oldalsó harántsávnál. A többletlépcső magassága ismeretlen. A jelenlegi modell ezt elmossa: minden WPC-teteje +0,47.
3. Két WPC-lépcső vezet a gresöblökből felfelé. A modell három köztes fokkal, 15,5 cm emelkedésekkel és 30 cm belépőkkel számol, de ezek nem helyszíni mérések.
4. A két fő teraszajtó előtt belül is van fellépő. A terv 15 cm-t ír; a fotók a fellépő létét igazolják. A kutya útvonalán ezt is számításba kell venni.
5. A modell folytonos betonszegélye elzárja a WPC-nyelv bejáratát. Ezt a képek nem támasztják alá; ne tervezz köré fiktív akadályt.
6. A távoli WPC-pihenő megközelítése és egy régi videóelemzésben szereplő külső WPC-sáv teljes nyomvonala nincs hitelesen rögzítve. Ne találj ki körbefutó járdát.
7. A zöldtető modellmagassága (+0,77), a domb +25 cm-es kiemelése, a növényhatárok és az 1,10 m-es korlátmagasság becslések. A növénygömbök helye/darabszáma illusztráció.

## Meglévő anyagok, növényzet és közművek

Meglévő világosszürke kőhatású gres; sötét szürkésbarna bordázott WPC járófelület, lépcső és homloklap; világos betonszegély; antracit függőleges pálcás fémkorlát; foltos világosszürke téglahomlokzat, sötétebb kávák, kívül antracit nyílászárók. Pontos gyártó, dekor, felületosztály és méret nem igazolt. Ezeket a későbbi képekben nem lehet önkényesen új anyaggá alakítani.

Meglévő gyep, csomós fűjellegű növények, leveles évelők/talajtakarók, vékony szárú rózsaszín és világos virágok, mulcs/kavics, felszíni fekete öntözőcsövek és fedlapok látszanak. Fajlista, darabszám, őshonosság és kutyabiztosság **ismeretlen**; a régi fajhasonlatok nem azonosítások.

| Közmű / funkció | Biztosan átadható adat | Hiányzó adat |
|---|---|---|
| Kültéri csap | Terv és T09 közeli fotó igazolja; a terv fagymentes csapot nevez meg. | Nyomás, vízhozam, elzárás, téli üzem, melegvíz és zuhanykapacitás. |
| Két teraszdugalj | Villamos terv: D47 a T09-nél, D48 a T10-nél. Fotón fedeles szerelvények. | Két dugalj nem jelent két külön áramkört; kábel, biztosító, védelem, terhelhetőség és működés nincs auditálva. |
| Jakuzzi-előkészítés | T09, kötött hely U01 szerint; tervi áramkiállás és szaggatott befoglaló. | A modell 2×2 m-es jelölője csak helyőrző; a mélység nem látszik teljesen a terven. Termék, szerelési tér és készülékspecifikus követelmény nincs rögzítve. |
| Öntözés | Csövek és fedlapok fotón; a korábbi kivonat szelepaknát/vízórát és vezérlőcsatlakozást említ. | Vezérlő, körök, kapacitás és más fogyasztóra felhasználhatóság nem igazolt. |
| Kültéri zuhany | Tulajdonosi funkcionális igény, nem igazolt meglévő berendezés. | Betáp, hideg/meleg víz, szennyvízelvezetés, visszafolyás- és fagyvédelem, elhelyezési méret. |
| Kutyarámpa | Szükséges tervezési funkció; teljes útvonal a beltértől a gyepig vizsgálandó. | Mért összes emelkedés, rámpaszélesség, pihenő/forduló, a kutya mérete és számára megfelelő hajlás. |

A brief 1:12-es példája 62 cm-re **7,44 m vízszintes hosszt** ad; ez kizárólag szemléltető geometria, nem kiválasztott rámpa, nem kötelező kutyaszabvány, és nem számolja bele az összes további fellépőt.

## Funkcionális program és pénzügyi keret

Később mindegyik elrendezés értékelje: fix helyű jakuzzi; lehetséges közeli zuhany; kutyás játszó/pihenő/illemhely és rámpa; napozás és privát együttlét; napos/árnyékos lounge; étkezés; panorámás laptopos munka; sport/mozi projektorral; mini konyha vagy mobil bár/hűtő; diszkrét hang; Hue-kompatibilis fény; meglévő és új növényzet. A funkciók prioritása változhat, elhagyásukat/halasztásukat nyíltan jelezni kell. Új áttörés, burkolatcsere vagy szerkezeti átalakítás nem automatikusan engedélyezett. [M, B a forrásjegyzékben](FORRASJEGYZEK.md)

Kültéri alapcél **4 M Ft bruttó**, **5 M Ft csak feltételes alternatíva**, a teljes lakás **20 M Ft-os** keretén belül. A 10%-os tartalékszabályt külön soron kell megtartani. A jakuzzi kb. 2 M Ft-ja becslési feltevés, nem ellenőrzött telepített ár. P0-ban nem történt termékválasztás vagy új árkutatás.

## Kilátás, belátás, napfény

A jelenlegi fotók városi tetőket, közeli lakott tetőteraszokat/ablakokat, távoli hegyeket és darukat mutatnak. Egyetlen nyitott panorámaképből sem következik teljes intimitás. A jövőbeli házat ne rajzold méretezett tömegként ismeretlen magassággal/távolsággal; ugyanakkor a belátását se hagyd ki. A pálcás korlát önmagában nem takarófelület. A meglévő alacsony növényzet nem bizonyít egész éves vagy azonos emeleti takarást.

Az [irány- és környezeti auditlap](NORTH_NEIGHBOURS_VIEW_PRIVACY_SUN.svg) külön jelöli a rajzi irányokat, a tulajdonosi égtájakat és a műholdképpel egyeztetett, közelítő északirányt. A fotókon van napos és árnyékos gres/WPC; hiteles felvételi idő, pontos szomszédmagasságok és takarási geometria nélkül nyári/téli zónás napóraszám **nem állítható**. Jelentős új árnyék nincs bizonyítva, és Péter nem vár ilyet. A későbbi árnyékszámítás az új ház tényleges kontúrjával végezhető el.

## Átadás két független AI-nak

Mindkettő ugyanazt a csomagverziót kapja. A másik AI ötleteit, rangsorát és első eredményét egyik sem láthatja saját anyagának lezárása előtt. Ez a csomag nem ad kész elrendezési ötleteket és nem jelöl ki győztes stílust. A régi brief példakoncepciói nem kötelező megoldások.

P1 csak Péter külön jóváhagyása után indulhat. A bizonytalan méretekre épülő javaslatot feltételesként kell megjelölni; nem nevezhető méretvalidált vagy kivitelezhető végleges tervnek. A jakuzzi áthelyezésével járó változat ellentétes U01-gyel. A nyitott kérdések az audit eredményei; nem jogosítanak kitalált válaszra vagy a teljes kültér használatának általános tiltására.

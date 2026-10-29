# Asztalos-, alkatrész- és műhelyi átadás

## Az átadható terv tartalma

Bútoronként: helyszíni elhelyezés, befoglaló, frontosztás, belső kiosztás, használható méretek, nyitott állapot, homlokzat/oldal/metszet, kritikus csomópont, rögzítés, kábel/szellőzés, szerelési sorrend és szerviz. Legyen anyagos/színes nézet, de a jelmagyarázat különböztesse meg a műszaki színt a tényleges felülettől.

Rajzlapon: elemkód, lapazonosító, dátum, revízió, egység, skála, méretforrás és státusz. Nem kell hamis gyártási méretet kiadni azért, hogy a lap részletesnek látszódjon. A felmérésre váró méret legyen megkülönböztethető a gyári adattól.

## Alkatrész-adatmodell

Egy alkatrész egyértelmű azonosítót kapjon, azonos geometriánál is követhető példányokkal:

| Adatcsoport | Kötelező tartalom a műhelyi használathoz |
|---|---|
| Azonosítás | projekt, bútor, modul, alkatrész, példány/darabszám, revízió |
| Méret | készméret és külön nyers szabásméret, vastagság, egység; levonások és ráhagyások szabálya |
| Anyag | gyártó/kód, lapvastagság, felület mindkét oldalon, szál/erezetirány |
| Tájolás | helyi XYZ, nullpont, A/B lapoldal, élek E1-E4 térképe, látszó és csatlakozó él |
| Bázis | ütköztetett él és lapoldal, befogási orientáció, fordítás utáni transzformáció |
| Élzárás | élenként anyag, szín, vastagság, készméretre gyakorolt hatás |
| Művelet | furat/marás azonosító, koordináta, átmérő, mélység, oldal, tűrés és vasalathivatkozás |
| Kapcsolat | másik alkatrész és illeszkedő kötés, rajz és 3D objektum, költségsor |
| Program | fájlnév, programazonosító, revízió/hash, státusz és ellenőrzés |

A hossz/szélesség értelmezése, az erezet és a gép X/Y iránya ne legyen hallgatólagosan azonos. Különítsd el az összeépítési elülső élt a gépi ütköztetési éltől. A betűjel (például „C”) csak a konkrét műhely kódtáblájával értelmezhető; ne találj ki élvastagságot hozzá.

## Vasalat és furat

Pontos rendszer/variáns kell: sín és hossz, terhelési osztály, kapocs, kampó, stabilizátor/szinkron, nyomásra nyitó és csillapító egység, pánt/talp, emelő vagy függesztő. Gyári szerelési rajz alapján ellenőrizd az oldalt, bázist, minimum anyagvastagságot, csavarbesüllyedést és hozzáférést. Ár és beszerezhetőség külön bizonyíték.

A kötés két oldalát együtt ellenőrizd: tengelyegyezés, tényleges furatmélység, maradó anyag és csavarhossz. Különítsd el a szerkezeti furatot a vasalat gyári megmunkálásától. Ha hiányzik a gyári sablon, kutasd fel a pontos modellhez tartozó elsődleges dokumentációt; ne hagyd indokolatlanul a teljes rendszert tervezetlenül. Ha továbbra sem bizonyítható, az érintett művelet maradjon nyitott, ne találj ki koordinátát.

## MPR / woodWOP és más CNC

Csak akkor készíts gépi programot, ha a feladat kéri. Ismerd meg a gép pontos azonosítását, vezérlést, szoftververziót, posztprocesszort, tengely- és oldalkonvenciót, makrókat és befogást. Az elírásgyanús géptípust ellenőrizd adattábláról vagy gépkönyvből. Új bútorhoz ne örökítsd automatikusan az előző gépét.

Működő mintaprogram előnyös, de hiányában dokumentált formátumból is készülhet **egyértelműen jelölt tervezet**. Ennek státusza nem lehet „gépre kész”, amíg a műhelyben nem ellenőrizték.

Szerszámonként szükséges: valós gépi azonosító, típus, átmérő/rádiusz, hasznos hossz, forgásirány, megengedett anyag és fordulatszám/előtolás, korrekció és gépi mérési adat. A be- és kilépés, rámpa/ív, fogásmélység, sorrend és kiszakadás elleni megoldás függjön a konkrét szerszámtól és anyagtól. Ne találj ki T-számot vagy univerzális forgácsolási értéket.

A befogásnál: ütközők, vákuumtappancs/szorító, szabad szerszámút, szerszámtartó és gép mozgástere; nemcsak a maró középvonalát kell nézni. Fordított darab koordinátáit és a címke tájolását is ellenőrizd.

Ellenőrzési lépcsők, külön eredménnyel:
1. Adatmodell ↔ rajz ↔ alkatrészlista egyezése.
2. Programformátum és műveletek visszaolvasása; koordináták és anyaghatárok ellenőrzése.
3. Megnyitás a tényleges műhelyi verzióban és releváns szimuláció.
4. Gép/befogás/szerszám ellenőrzése a gépkezelő által, műhelyi szabályok szerinti próba.
5. Első darab mérése és próba-összeállítás, terhelési/működési ellenőrzés, utána sorozatengedély.

Ne indíts fizikai megmunkálást dokumentációs feladatból. Az AI által lefuttatott parser nem a 3-5. lépcső bizonyítéka.

## Címke és adatbázis

A címke olvashatóan tartalmazza az alkatrészazonosítót és revíziót, anyagot/vastagságot, méretfajtával jelölt méreteket, élzárást és egyértelmű tájolást. Vonalkód/QR esetén ugyanazt az azonosítót vagy ellenőrzött hivatkozást kódolja, amelyet a műhely ténylegesen használ. A mintacímke külalakja ne fedjen el eltérő jelentést.

A címkét nyomtatva is próbáld. A helyi Excel/SQLite kereső még nem a woodWOP adatbázisába való integráció. Igazolt műhelyi import/lekérdezés nélkül „előkészített megfeleltetés” a helyes státusz. Elavult revízió ne nyisson meg észrevétlenül új vagy más alkatrészt. Az átadott program neve, címkéje és visszakeresése ugyanarra a példányra mutasson.

## Élő CAD-híd és megosztott munkamenet

Ha van helyi AutoCAD-híd, előbb státusz és pontos célrajz-útvonal. Az eredeti referenciarajzot ne módosítsd a saját munkamásolat helyett. Kötégelt lekérdezések/módosítások után olvasd vissza a méreteket és a mentést. Bizonytalan kimenetelű módosítást vagy időtúllépést ne ismételj automatikusan; előbb állapítsd meg, megtörtént-e. Egyeztesd a kézi szerkesztéssel, és add vissza a kezelést, ha a híd lefoglalja a parancssort.

## Átadás ellenőrzése

Külön jegyzékben: mi tekinthető ajánlatkérési dokumentumnak, mely fájl csak programtervezet, melyik érvénytelen/archív. Az aktív átadás ne tartalmazzon jelöletlen régi méretet. A megnyitható DWG/DXF, PDF, Excel, képek és kért gépi fájlok ténylegesen legyenek a csomagban, az alkalmazott verzióval és szükséges külső függőségekkel.

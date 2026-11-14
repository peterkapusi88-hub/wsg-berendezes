WSG-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3
Szerző-AI: ChatGPT / Codex, Péter által kért Astra kreatív kontroll
Modell: pontos futtatási modellverzió nem igazolt
Bázis-commit: fee7123f877bba3c2e2604ca021f5598c7e18b0d
Dátum: 2026-10-25, Europe/Budapest
Verzió: V3 r1
Státusz: KREATÍV ÁTADÁS · KONCEPCIÓ – NEM VALIDÁLT · Claude integrációjára vár

# A-902 · Creative Upgrade V3 · egész térre kiterjedő minőség + emlékezetes karakter

**Döntés:** a V2 tárgyközpontú kompozícióját felület- és tárolórendszerré kell továbbépíteni. Minden látható tömör falfelület tudatos szerepet kap; ehhez kapcsolódik egy erős, helyiségspecifikus WOW-elem. Az új rendszer tíz eltérő stílusra készült stratégiai szinten. Részletes frissítés most csak **S01 Kyoto Ink és S02 BiBo Nocturne, Cam_02**. A két angol kreatív csereblokk: [promptfájl](../../05_promptok/A902_S01_S02_Cam02_CREATIVE_UPGRADE_V3_r1.md).

Nem készült kép, új Blender-jelenet vagy futtatható képcsomag. A V2 dokumentumok, a KEP-004 képek és előkészített csomagok változatlanok. A külön ágon lévő két új V3 fájlt Claude geometriai ellenőrzés és prompt-összefűzés után integrálhatja. Nincs automatikus Claude-indítás vagy tömeges képgenerálás.

## 1. Forrásrend és az új tulajdonosi utasítás

Olvasott alap: friss GOAL; Render Reality Gate; értékalapú stíluslabor-skill; Astra V2 40 stílusblokkja; KEP-004 ChatGPT Images végrehajtási terve; az első S01 kép r1 Gate-auditja; a két tényleges Cam_02 csomag; aktuális geometrialock és villamos összesítő. A csatolt 1586×992 Kyoto-képet vizuálisan értékeltem. A kép nem alaprajzi bizonyíték.

**Elsőbbség:** Péter mostani utasítása engedélyezi a kijelölt tapétákat, felületi paneleket és akár festett MDF-et. Ezzel a régi „minden fal fehér” és „nincs festett front” kreatív tilalom a **külön megnevezett, méretezett és költségelt új elemekre** módosul. Ez nem engedély új falra, bontásra, mennyezetre, nyílászáró- vagy gépészeti változásra. A régi fixed blokk változatlan bemásolása és egy ellentmondó színesfal-prompt egymás mellé tétele hibás lenne: Claude új verzióban vezesse át a §8 szerinti pontos felületkivételt.

A friss main már tartalmazza Cam_10 véglegesítését és a master Cam_11 kiegészítését. Ezeket nem nyitom újra; jelen scope Cam_02. A végrehajtási terv elején maradt „nem indult” állításnál frissebb az r1 audit: **egy S01 kép elkészült, FAIL / ÚJRATERVEZÉS**.


**Mentés előtti frissítés:** munka közben main-re került a `fee7123f877bba3c2e2604ca021f5598c7e18b0d` commit. A friss [Cam_02 geometriai v2 blokk](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/05_promptok/KEP004_ChatGPT_Images_v2_geometria/Cam02_GEOMETRIA_v2.md) és a [szürke tömegvázlat](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/04_renderek/A902_cam02_tomeg_v1/README.md) elolvasva és figyelembe véve. Az étkezőből a nyugati hosszoldal és három nyugati szék háta látszik, nem egy önálló bal előtéri étkező. A vázlat 180×45 cm-es TV-konzolja helyett itt 240×40 cm és egy új keskeny torony szerepel: **Claude-nak ezért a bútortömböket és vetített képtéri határokat frissítenie kell az új, ellenőrzött befoglalókra**, az építészeti alap és kamera változtatása nélkül. Az eredeti képszázalékok nem írhatják felül az új, valós bútorméretet. A kanapé és étkező elrendezéscsaládja változatlan.

## 2. Kyoto Ink első képének kritikus kreatív értékelése

**A kép kellemes, összehangolt bútorozást mutat, de nem teljesíti a kért, egész térre kiterjedő tervezői luxusminőséget.** Ez saját kreatív értékelés, a tulajdonosi visszajelzéssel összhangban.

| Képen látható jelenség | Kreatív következmény | V3 válasz |
|---|---|---|
| A TV körül és felett nagy sima, fehér mező marad | A TV és a hosszú komód két lerakott tárgy; nincs falnyi kompozíció vagy integrált tárolási hierarchia | Zárt tároló + két léptékű, sík panelmező + texturált háttér egy rendszerben |
| A magas textilpanel az étkező mögött elszigetelt dekor | Nem szervezi a TV-zónát; léces szegélye általános japandi jel | A textil/grafika a frontokba és egy önálló, nagy műbe kerül, ismétlődő lécek nélkül |
| A bézs, taupe és világos fa hasonló hangsúlyt kap | Kyoto „Ink” karakteréből a tintakontraszt gyenge; inkább kellemes katalógusszoba | Grafit nagy mező, füstszürke papírtextúra, világos szövött ellenpont; a bútorok színe marad |
| A homlokzat fölötti és melletti tömör részek sima háttérként maradnak | A kompozíció megszakad a TV-zónán kívül | Halk, egységes tapétamező a tényleges belső tömör felületeken; a fehér keretek és kávák tudatos, keskeny átmenetek |
| A kép dísztárgyakból, növényből és meleg fényből próbál rétegezni | A karakter a stylingtól függ; nappali semleges fényben gyenge | A mélységet illesztés, frontosztás, valódi textúra és árnyék adja, új tárgyak nélkül |
| A jó alapbútorok között elegendő nyugalom látszik | Ezt érdemes megtartani, nem zsúfolással „javítani” | Megmarad a Lennon, Toni, Eamy és a szabad középtér |

**Önkritika a V2-höz:** a „keep the upper wall mostly empty”, a különálló 100×180-as panel és a szerény alacsony tároló együtt túl visszafogott utasítás volt. A generálás a geometriában hibázott, de a kreatív hiányt nem lehet kizárólag az eszközre fogni. A tudatos negatív tér továbbra is fontos: V3-ban ez anyaggal megdolgozott, csendes mezőt jelent, nem véletlenül befejezetlen falat.

**Külön műszaki lista – Claude auditjából, nem újramérve:** a tér mélyítése/szélesítése, az étkező bal előtérbe helyezése, az ML04-től eltérő függeszték, a terasz korlátszakaszának változása; a listán kívüli dohányzóasztal és gömblámpa; a KI-T engedély nélküli háttérfénye; szőnyeg- és padlóeltérés. A V3 egyik eltérést sem őrzi meg. A kép geometriája nem lesz új referencia, és a képen látszó tárgyak nem kerülnek automatikusan a költségvetésbe.

## 3. Folytonos falrendszer – az egész lakásra érvényes stratégia

Minden tömör falfelület kap **azonosítót, szerepet, tényleges felületet és lezárási részletet**. A főfal tárolást és karaktert hordoz; a kísérőfalak halkabb textúrát; a nyílások körüli keskeny sávok és kávák tiszta átmenetet. A fehér ablakkeret, mennyezet, belső ajtólap és a meglévő fürdőburkolat szándékosan megőrzött elem. Ezek nem „üres foltok”, és nem festhetők át pusztán a kompozíció kedvéért.

A nappali–étkező–konyha nyitott térrendszerének felületei közös tónuscsaládot kapnak, de a munkapult mögött csak tisztítható, a meglévő konyhatervvel egyeztetett anyag alkalmazható. A masternek saját, világosabb anyagsűrűsége van; a két másik szoba és az előtér ugyanennek egyszerűbb változatát kapja a meglévő tárolófrontokon. A fürdők és WC megmaradó lapja teljes értékű, tudatos háttér: tükör, egy tároló és textil formálja tovább; nincs száraz tapéta a zuhanyban.

**Nem elég egy Cam_02 kép:** a teszt után a valós faljegyzéken végig kell menni a bejáratból, a kanapéról, az étkezőből és a fordított nézetből is. A most nem látható fal is kiosztott felületet kap, de a prompt nem mozdíthatja el a kamerát azért, hogy mindent megmutasson.

A kis költségű réteg is maradjon mindenütt: ha spórolni kell, először a fényes fényezés, ív, reliefmélység és dekor-LED egyszerűsödik. **Nem** a teljes kísérőfal-kezelést töröljük, hogy egyetlen drága TV-fal maradjon három csupasz fal mellett.

### 3.1 Valós falszakaszok – S01 és S02 közös Cam_02 felületjegyzéke

A koordináták a main lockból olvasott, **terv szerinti** belső síkok, nem helyszíni mérés. A jelen felületkiosztás javaslat; Claude határozza meg a végső láthatóságot és nettó mennyiséget.

| ID | Tényleges felület | Feladat és új réteg | Megtartás / megszakítás |
|---|---|---|---|
| W01 | Nyugati 10 cm-es fal, nappali oldala x=3,67; y=4,05–8,05; H=2,90 | Fő tároló–TV-kompozíció + a fennmaradó felület tapétája. Javasolt bútor/panelmező y=4,25–7,75 | Nem nő a falvastagság szerkezetként; a burkolat külön, max. 4 cm. FL02 y=7,85, z=2,85 és D16/D17/G08 hozzáférhető |
| W02 | Déli tömör szakasz x=5,20–7,30; nappali oldala y=4,05 | Kísérőtapéta + egyetlen nagy mű vagy grafikai mező | D19 és kapcsoló/szenzor környezet szabad; nincs 40 cm mély új bútor |
| W03 | Keleti/étkező felőli valóban tömör csonkok: konyha-K csonk, 05.3 fal, akna nappali oldala | Ugyanazon kísérőtapéta a száraz nappali oldalon, sarkonként következetes lezárással | Ajtók, nyitott átjárók, akna és kiállások változatlanok; nyílást nem rajzolunk be falnak |
| W04 | Északi homlokzat belső tömör mezői, szemöldök a y=8,05 síkon; üveg x=4,38–9,00 | Halk kísérőtapéta a hozzáférhető sík belső mezőkön, nem külön hangsúlyfal | Keret, redőnytok/szerelőfedél, tömítések és sötét külső téglakáva megmarad; tokot nem tapétázunk át |
| W05 | Nyíláskávák és a délnyugati nyitott átjáró | Meglévő fehér, tiszta élű összekötő részlet; a tapéta a fal élén zárul | Nincs új ajtókeret, burkolati „portál”, álboltív vagy fal a nyitott sarokban |
| W06 | Mennyezet és kültéri falak/terasz | Meglévő, tudatosan változatlan építészeti keret | Nincs álmennyezet, mennyezeti panelragasztás/fúrás, kültéri beltéri tapéta |

**Mennyiségmodell a költséghez:** W01 látható háttere a bútorral együtt az A csomag része; W02–W04 kísérőfelületére 14–18 m² előirányzat, nem mért mennyiség. W05 megtartás, új anyagköltsége 0; az élképzés/védelem a B csomagban. A teljes tapétamennyiség csak a nyílások, beépítések és tekercsvágás után végleges. Ha a felmért felület több, a mennyiséget és költséget kell javítani, nem a renderen elhagyni egy falat.

## 4. Költségmodell és ellenőrizhető árhorgonyok

Minden összeg **bruttó Ft**, a táblákban **ezer Ft**. A kész csomagok saját, 2026-10-25-i **tervezői becslések, ajánlatkötelesek**; a webshopárak csak alapanyag-/résztermék-horgonyok. Az ismeretlen ár nem nulla. Egyedi grafika, fényezési szín, tükörforma és a falrögzítés végleges ára kizárólag műszaki tartalomra adott beszállítói ajánlattal igazolható.

| Árforrás, ellenőrzés 2026-10-25 | Forrásadat | Mire használható / mire nem |
|---|---|---|
| [IKEA BESTÅ 002.458.42](https://www.ikea.com/hu/hu/p/besta-vaz-feher-00245842/) | 60×40×192 cm váz, 22 000 Ft áfával | Csupasz váz, nem komplett bútor; front/pánt/polc/láb/rögzítés külön. A 40 cm váz nem 40 cm kész bútor |
| [IKEA BESTÅ 602.459.19](https://www.ikea.com/hu/hu/p/besta-vaz-feher-60245919/) | 60×20×64 cm váz, 12 000 Ft áfával | Sekély modul, nem ellenőrzés nélkül toronnyá halmozható rendszer |
| [Lapszabó U961 ST7](https://www.lapszabo.hu/butorlap/egger/U961-st7-18-grafitszurke) | 2800×2070×18 mm, szabott táblaár 42 875 Ft, áfával | Grafit laminált alapanyag; vasalat, ABS, beépítés nem ebből következik |
| [HK Group festett MDF](https://hkgroup.hu/) | Egyoldalas 26 900 Ft/m² nettó; kétoldalas 44 400; magasfényű egyoldalas 40 900. Anyag, szabás és fényezés a forrás szerint benne | 27%-kal számított bruttó: 34 163 / 56 388 / 51 943 Ft/m²; egyedi szín/forma ajánlatos. Nem komplett bútor |
| [Rasch TB100997](https://tapetabarlang.hu/beton-hatasu-szurke-bezs-szinu-tapeta) | Vlies, 10,05×0,53 m, 16 790 Ft/tekercs; szállítás 3499 Ft, 0 cm illesztés | Középsávú anyagár-horgony, nem automatikusan mind a tíz stílus kiválasztott tapétája |
| [OBI Rasch 608960](https://www.obi.hu/dekorativ-tapetak/rasch-fatyoltapeta-tapetenwechsel-ii-608960-csikos-krem-szuerke-10-05-m-x-0-53-m/p/4925913) | 8349 Ft/tekercs, 10,05×0,53 m, áfával + szállítás | Gazdaságos árszint; széles blokkcsíkos, ezért nem S01 papírtextúra-SKU-ként választott |
| [Fancy textilhatású vlies](https://fancytapeta.hu/TEXTIL-HATASU-CSIKOS-FINOM-TEXTURAJU-VLIES-TAPETAT) | 32 560 Ft/tekercs, 0,52×10,05 m | Magasabb anyagsáv; a teljes lakásra nem elsődleges választás |
| [Ádám a festő](https://adamafesto.hu/tapetazas-arak/) | Középnehéz tapéta ragasztása 3500–4500 Ft/m², anyag nélkül; adókezelés nem egyértelmű | Nem címkézem bruttó ajánlatnak; a saját becslésben óvatosabb, előkészítéssel és adóval növelt sáv |
| [Gulyás Üveges](https://gulyasuveges.hu/arlista/tukor-arak/) | 4 mm ezüst tükör 18 000 Ft/m² bruttó; gépi élcsiszolás 1700 Ft/fm; színes tükör 40 000 Ft/m² | Beépítés, háttérbiztosítás, keret és forma külön. A V3 nem óriási bronztükröt árazzal ezüstáron |
| [Képmánia](https://kepmania.eu/arlista) | Kétpaneles 200×100 cm vászon, normál bruttó 92 735 Ft, 2 cm vakrámával; akciót nem feltételezek | Monumentális nyomat gyártási árhorgonya, nem egyedi alkotói díj vagy minden méret ára |
| [Apollo Design](https://apollodesign.hu/vaszonkep) | 120×100 cm vakrámás vászon 38 000 Ft, AAM/bruttó értelmű, szállítás nélkül | Gazdaságos nyomat-alap; szerzői grafika, nagyobb méret, szerelés külön |

**Tapétavágás:** 2,90 m falnál egy 10,05 m-es tekercs jellemzően három teljes magasságú csíkot ad; a névleges 5,33 m² nem azonos hasznos falterülettel. 0,53 m szélességgel kb. 4,61 m² hasznos felület, további mintaismétlés és vágási veszteség előtt. Nettó 14–18 m² kísérőfelületre ezért előzetesen 4–5 tekercs, nem egyszerűen terület/5,33; pontos kiosztás a felmérés után.

### 4.1 Mi van benne a csomagárban?

A = TV-tároló és a W01 integrált felület, korpusz, front, panel, élzárás, vasalat, kábelajtó, alap rögzítés, szállítás, szerelés és arányos részletrajz. B = W02–W04 kísérőtapéta 14–18 m², előkészítés, ragasztó, sarok/élképzés, munkadíj és védelem. C = egy nagy mű/grafikai betét vagy stíluskarakter-elem, gyártási előkészítéssel, kerettel és rögzítéssel; S02 tükrét az A tartalmazza, nem C-ben ismétlődik.

S01 A 520–680 eFt becslésének felosztása: korpusz 90–120; front/panel 120–150; szabás/ABS 35–45; vasalat 40–55; rögzítés/kábelhozzáférés 30–40; W01 tapéta 35–45; műhely és szerelés 115–150; logisztika/részletrajz 55–75. Összeg 520–680. S02 A 650–820: korpusz 100–130; front/fényezés 150–190; szabás/él 35–45; vasalat 45–60; tükör/keret/biztosítás 70–95; rögzítés/kábel 35–45; W01 háttér 30–40; műhely/szerelés 130–150; logisztika/részletrajz 55–65. Összeg 650–820. Ezek **nem beszállítói sorárak**, hanem a csomagbecslés átlátható felosztásai.

Nincs új villamos hálózat vagy dekor-LED az S01/S02 alapcsomagban; ez a sor 0 **mert nincs ilyen scope**, nem ismeretlen termék ára. A meglévő TV bekötése/hátlaphozzáférés benne. Súlyos faljavítás, rejtett műszaki hiba vagy a 14–18 m²-nél nagyobb felület külön felmérendő. Teljes lakás tervezési díját nem számítjuk újra; a részletrajz A-n belüli összege a meglévő tervezői szerződés tartalmával egyeztetendő, kétszerezés nélkül.


## 5. A tíz stílus különböző fal- és tárolóstratégiája

Az alábbi csomagok **alternatív lakásstílusok**, nem tíz egyszerre megvásárolandó rendszer. A–C költség most a nappali–étkező összefüggő falkezelési mintacsomagjára szól. A többi helyiség szövege stratégia; az ottani kivitelezés nincs elrejtve ebben az árban, §5.2 külön keretet ad hozzá.

### S01 · Kyoto Ink — Tintával szerkesztett textilarchitektúra

**Karakter / gesztus:** A. Füstszürke, finom papírrost-hatású vlies összefüggő mezők; grafit síkok és egy nagy, eredeti tusjel-nyomat. A luxus a mély és vékony síkok arányából jön, nem lécezésből.

**Integrált tároló:** Nyugati TV-fal: 240 cm-es alacsony zárt tároló + 60 cm-es keskeny torony, közös, eltolt panelritmus. A torony két vagy három ajtaján végigfutó matt nyomat külön ajtólapokra bontva, valódi fugákkal.

**Folytonosság a lakásban:** Étkező: füstszürke papírtextúra és egy 100×180 cm-es textilmű a tényleges tömör falszakaszon. Master: gyöngyszürke szövethatás és eltolt textilfejvég; gardróbfront grafit vonalakkal tagolt világos sík. Előtér/másik két szoba: ugyanennek világosabb, kisebb mintasűrűségű változata, meglévő tárolófrontokhoz kötve. Fürdő: a meglévő lap saját textúrája a csendes mező; keskeny fekete tükörkeret és egy grafit tároló.

**WOW:** Egyetlen grafit horizontba kapcsolt, függőlegesen felemelkedő nyomtatott tárolófront és árnyékot vető TV-panel.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 520–680 eFt; B kísérőfelületek 160–260 eFt; C mű/karakterelem 60–100 eFt. Teljes nappali mintacsomag **740–1040 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 535–740 eFt:** Sík U961 ST7 laminált front, 20 cm mély standard felső/tárolóváz csak alkalmas helyen; a mű egyetlen feszített nyomat. Olcsóbb, finom textúrájú tapéta az összes kísérőfalon; a falkezelés nem marad el. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** shoji-utánzat, bambusz, rendszeres lamella, bézs len minden felületen. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S02 · BiBo Nocturne — Kék lakk-kabinet és ezüst ellenfény

**Karakter / gesztus:** B. Tintakék sík MDF-front a TV körül, a többi tömör falon ezüstszürke, finoman fényváltó szövethatású vlies. Egyetlen rögzített tükörsáv, puha kontúrral, valódi visszaverődéssel.

**Integrált tároló:** 90 cm széles, részben zárt kabinet fix tükörmezővel + 240 cm alacsony médiatároló. A kék mezők 600–900 mm-esek, nem lamellák; a fényes hatás csak a kabinet két frontján. Tükör nem mozgó, túlterhelt szekrényajtó.

**Folytonosság a lakásban:** Étkező: halk ezüstszürke fal és a kabinet frontjára komponált, nagy kék-szilva grafikai átmenet. Master: tompa szilva textilfal és sima világos gardróbfront; előtér: kék ajtómező és fix tükör egy meglévő tárolóegységen. 05.2/05.3: világos szövött háttér, legfeljebb egy sötét frontmező/szoba. Fürdő: eredeti lap, aszimmetrikus ezüst tükör és grafit textil, új falburkolat nélkül.

**WOW:** Aszimmetrikus kék kabinetfal a valós teret metszetszerűen visszaadó, keskeny tükörrel.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 650–820 eFt; B kísérőfelületek 160–260 eFt; C mű/karakterelem 45–80 eFt. Teljes nappali mintacsomag **855–1160 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 650–860 eFt:** Kész mélykék laminált mintára váltott front; tükör egyenes, csiszolt téglalap lekerekített kontúrkeret mögött. Grafika egy sík betétre, nem minden frontra. A visszaverődés valós marad, a magasfényű MDF elhagyható. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** teljes tükrös fal, arany hoteldekor, virágos étteremmásolat, minden él mögé LED. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S03 · Alelí Casa — Agyag tónusú, kézműves szalon

**Karakter / gesztus:** F. Meleg világosszürke, vakolatszemcsét idéző vlies az összes száraz háttérfalon; a déli TV-zónában nagyméretű, matt terrakotta festett MDF-mező. A kézműves karaktert egy valódi, sekély textil–agyag kompozíció hordja.

**Integrált tároló:** A meglévő déli 210 cm-es tároló helyén dióhatású zárt front; a panellel közös széles mezők, egyetlen 60 cm-es kerámia/textil betét. Nincs új falszerkezeti boltív.

**Folytonosság a lakásban:** Étkező: a körasztal hátterében folytonos halvány agyagszín, széles mezők. Master: kakaó–nyerslen textilfejvég és vászonhatású kísérőfal. Előtér és mellékszobák: világos ásványi tónus, dióhatású tárolófront; fürdő: eredeti lap + kör bronzperemű tükör, agyagszín textil. Kerámia csak két hangsúlyos tárgy, nem falnyi nehéz csempe.

**WOW:** Nagy, egymásba metsző terrakotta és dió felületek a körasztal tömegével.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 480–650 eFt; B kísérőfelületek 160–260 eFt; C mű/karakterelem 80–140 eFt. Teljes nappali mintacsomag **720–1050 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 540–730 eFt:** Sík agyagszínű laminált az MDF-festés helyett; valódi kerámia relief helyett festett rétegeltlemez–len kompozíció, kerámiának nem ábrázolva. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** rusztikus álboltív, műkő mediterrán díszlet, apró cseréptárgyak sora. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S04 · LA Horizon — Folyamatos dióhorizont, ezüst felső mező

**Karakter / gesztus:** E. Déli falon hosszú, széles dióhatású lapsáv és alatta összefogott alacsony tároló; a többi száraz falon finom, vízszintes szálirányú szürke vlies. A felső fal textúrája csendes, de nem csupasz.

**Integrált tároló:** Két eltolt, padlón támaszkodó tárolótest a V2 befoglalóján belül; vízszintes frontfugák, valódi zsanéros rekeszek. Falpanel legfeljebb 30 mm kiállású, nem polcként kitalált lebegő kőtábla.

**Folytonosság a lakásban:** Étkező: dohányszínű üvegasztal mögött hűvös ezüstszürke mező. Master: gyöngyszürke textil és folyamatos alacsony fejvégsáv, a gardrób széles vízszintes osztással. Előtér/mellékszobák: egy alacsony dióhatású frontvonal a helyi bútoron, fölötte halk szürke textúra. Fürdő: tájformátumú tükör, megmaradó lap.

**WOW:** A panorámával párbeszédben álló, több falnézeten folytatott vízszintes felületrendszer.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 500–660 eFt; B kísérőfelületek 150–240 eFt; C mű/karakterelem 50–90 eFt. Teljes nappali mintacsomag **700–990 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 530–740 eFt:** Egger faerezetű laminált a valódi furnér helyett; vízszintes nagy fotónyomat alumíniumkeret nélkül, egyszerű vakrámán. A laminált erezete a bütüknél sem válik tömör fává. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** S10 lépcsőző terrakotta tömegei, pálmás fotótapéta, luxusvillát utánzó új üvegfal. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S05 · Miami Streamline — Széles, lépcsőző Deco-kontúrok

**Karakter / gesztus:** G. Krémszürke, halvány selyemhatású vlies; a TV-falon három nagy, eltérő szélességű, kétlépcsős festett MDF-kontúr. A V2 bordázat helyett kevés, nagy görbület, grafit élvonal.

**Integrált tároló:** Sík, pezsgőszínű frontok standard kiosztáson; a kerekítés csak a fix oldalzárón, nem minden ajtón. A rózsaszín kanapé előtt a tároló nem kap második fő akcentust.

**Folytonosság a lakásban:** Étkező: kréta alap és egy tompa türkiz sík a meglévő szekrényfronton. Master: pezsgő kárpit és grafit kontúr; gardróbfront két széles, lekerekített keretmintával. Előtér/mellékszobák: sima háttér tapéta és egy lépcsős nyomat, nem minden falon Deco-minta. Fürdő: meglévő lap + lépcsős tükör, nedvességálló sima tároló.

**WOW:** Nagyvonalú, ritka kontúrokból formált beépített hatás, rózsaszín ülőtömeggel.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 550–750 eFt; B kísérőfelületek 150–250 eFt; C mű/karakterelem 60–110 eFt. Teljes nappali mintacsomag **760–1110 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 550–760 eFt:** Sík MDF-re nyomott/festett kontúr, CNC mélymarás nélkül; csak két lekerekített fix sarok. A halvány selyemhatás alacsony fényű vliesből készül. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** ismétlődő bordázat, arany csík minden fugában, harsány retróhotel. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S06 · Zenit Atelier — Sötét atlasz, egyetlen fénymetszés

**Karakter / gesztus:** D. Füstös dióhatású nagy panel és matt grafit mező a TV körül, a többi száraz falon sötétebb gyöngyszürke szövethatás. Az anyagváltás két-három széles sávra korlátozott.

**Integrált tároló:** V2 alacsony tároló és egy oldaltorony összekomponálva; a toronyba visszahúzott, valóban épített rés, egy később igazolandó Hue fényvonallal. Nem falba vájt fülke.

**Folytonosság a lakásban:** Étkező: világosabb textúrájú fal ad kontrasztot a diófrontokhoz. Master: három széles világos textilmező, sötét oldalzáróval; gardróbfront ugyanebből a dióhatású dekorból. Előtér/mellékszobák: grafit lábazati bútorsáv és visszafogott szövethatás. Fürdő: mély fekete tükörkeret, meglévő lap szabadon.

**WOW:** A széles, zárt diótömegen átvágó egyetlen keskeny, mély rés.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 580–780 eFt; B kísérőfelületek 150–250 eFt; C mű/karakterelem 60–100 eFt. Teljes nappali mintacsomag **790–1130 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 590–800 eFt:** A torony és a bemetszés marad, dekorfény nélkül; sík faerezetű laminált, sötét fóliás polchát. Az A nappali sorozatban a fizikai árnyék viszi a gesztust. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** LED-szalag minden peremen, teljes fekete fal, Kyoto áttetsző textilsíkja. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S07 · Lake Forest Couture — Gyöngyszürke dombormű és puha panelmezők

**Karakter / gesztus:** F. Világos gyöngyszürke szövethatású vlies az összes száraz háttérfalon, a TV-zónában két nagy, alacsony domborulatú festett MDF-betét. A relief nem kőnek álcázott lap.

**Integrált tároló:** Világos laminált zárt tároló, egy íves fix véggel; sima ajtólapokra felrakott könnyű textilbetétek csak a megengedett pántterhelésig. A teljes felület aránya finomabb, nem az S02 tükörjátéka.

**Folytonosság a lakásban:** Étkező: szürkés gyöngyfényű, nem csillámos tapéta; master: konvex textilfejvég és sík gyöngyszürke tárolófront. Előtér/mellékszobák: világos tapéta nagy léptékű, sekély reliefnyomattal. Fürdő: eredeti lap és ovális tükör, puha textil, csempefestés nélkül.

**WOW:** Nagy, puha árnyékot vető relief a Wolke ívével egy kompozícióban.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 570–780 eFt; B kísérőfelületek 180–280 eFt; C mű/karakterelem 80–140 eFt. Teljes nappali mintacsomag **830–1200 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 590–800 eFt:** A valódi 3D relief két kivágott, festett rétegeltlemez-lapra egyszerűsül; az íves véget két lekerekített sarok váltja. A kísérőtapéta továbbra is végigfut. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** travertinnek látszó MDF, bézs minden felületen, fodros hoteltextilek. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S08 · Milano Radical — Szerkesztett színmezők és tárológeometria

**Karakter / gesztus:** B. Krétafehér, finoman matt texturált vlies mint tudatos alap; egy széles sárga laminált mező, grafit és dió ellenponttal. A többi falon a frontokhoz igazított nagy, vékony grafikai vonalak.

**Integrált tároló:** A V2 három testét két zárt tároló és egy valóban megtámasztott összekötő sík szervezi. Színmező mindig teljes valódi ajtót vagy panelt fed; álajtók nélkül.

**Folytonosság a lakásban:** Étkező: körasztal mögött egyetlen 120×160 cm-es geometrikus nyomat. Master: kréta textil és grafit keret, sárga csak kis jel. Előtér/mellékszobák: egymásra válaszoló fekete–fehér mezők a meglévő frontokon. Fürdő: eredeti lap, eltolt fekete tükörkeret.

**WOW:** A frontok és a fali kép egyetlen nagy, szabálytalan geometrikus kompozícióvá állnak össze.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 480–650 eFt; B kísérőfelületek 140–230 eFt; C mű/karakterelem 60–110 eFt. Teljes nappali mintacsomag **680–990 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 510–700 eFt:** Három sík laminált dekor és egy matt nyomat; nincsen egyedi hajlítás vagy magasfényű fényezés. A ritmusból nem veszünk el, csak a felületi technikából. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** Memphis-díszlet, sok apró színes tárgy, S02-féle tükörfal. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S09 · Paris Collector — Monumentális mű és halk szövetfal

**Karakter / gesztus:** H. Füstös világosszürke szövethatású vlies a teljes száraz háttérrendszerben; PC-A01 mű 140×180 cm, eredeti szilva–kréta grafika, nagy matt vászonként. A mű nem egy fehér falra felakasztott magányos plakát.

**Integrált tároló:** Dióhatású zárt alsó tároló egy könyvrekesszel; a fölötte futó széles sötét panel a mű keretezését folytatja, nem teljes könyvespolcfal. A mű helyét a valós TV és Corvena befoglalója mellett kell véglegesíteni.

**Folytonosság a lakásban:** Étkező: finom szövethatású mező, második monumentális kép nélkül. Master: szilva textil és halvány kísérőtapéta, gardróbfront keskeny sötét peremmel. Előtér/mellékszobák: egy-egy kisebb, azonos sorozatú nyomat meglévő frontmezővel összerendezve. Fürdő: nedvességálló passe-partout hatású tükör, meglévő lap.

**WOW:** Egyetlen monumentális kép, valódi tároló és fotel egymást erősítő együttese.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 480–650 eFt; B kísérőfelületek 160–260 eFt; C mű/karakterelem 100–180 eFt. Teljes nappali mintacsomag **740–1090 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 570–770 eFt:** PC-A01 két 70×180 cm-es vászonból, egyszerű vakrámával; művészi felületfestés helyett jó minőségű nyomat. Valós textúra csak az alapon, nem digitálisan hamisított impasto. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** műtárgymásolat, zsúfolt galériafal, kisméretű olcsó poszter nagy falon. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### S10 · Desert Modern 70 — Réteges földszínű síkok és tetőkerti kapcsolat

**Karakter / gesztus:** I. Világos, tompa agyagszürke vlies a kísérőfalakon; a déli TV-falon három széles, eltérő magasságú, okker–kakaó MDF/lapmező. A szintezés kizárólag bútor és panel, a padló változatlan.

**Integrált tároló:** A V2 220 cm-es tároló két magasságú, ténylegesen zárt dobozból; egy lapos felső panel árnyékával kötődik a háttérhez. A terasz valós szintjeire utal, nem épít új dobogót.

**Folytonosság a lakásban:** Étkező: dió körasztal és halk, vízszintes rostú kísérőfal. Master: kakaó–len fejvég, világos agyagszürke tapéta; előtér/mellékszobák: két szintű grafika vagy frontmező. Fürdő: lépcsős tükörkörvonal a meglévő lap előtt. Kültéren csak a már tervezett pad textilje kapcsolódik hozzá.

**WOW:** Nagy, lépcsőző bútor–fal kompozíció, amely a meglévő tetőkert valós szintjeire felel.

**Megvalósítás és bruttó becslés:** A integrált TV/tárolófal 480–650 eFt; B kísérőfelületek 150–240 eFt; C mű/karakterelem 70–120 eFt. Teljes nappali mintacsomag **700–1010 eFt**, minden eleme ajánlatköteles. A méretek az S01/S02-nél §6–7; S03–S10-nél a V2 tároló befoglalója marad, panelmélység legfeljebb 30 mm, a mű legfeljebb 140×180 cm; pontos falhossz és mennyiség következő fázis.

**Gazdaságos alternatíva, teljes csomag 520–720 eFt:** Festett sík MDF helyett kész földszínű laminált; a relief két laprétegből, nem tömör tömbből. Megmarad a lépcsős ritmus, elmarad az egyedi felületvakolás. A jelzett kompromisszum anyagban/mélységben látszódjon a későbbi képen is. A teljes felületi folytonosság megmarad.

**Elhatárolás / kerülendő:** LA egyetlen dióhorizontja, műsivatagi panoráma, új emelvény. A korábbi főbútor és L2/L3 elrendezés nem változik; ha a V2 termékhez nyitott méret/árfeltétel tartozik, az továbbra sem feloldott.

### 5.1 Bruttó többlet és a 18 M Ft-os keret védelme

**A nettó többlet nem az új csomag teljes ára.** Az új TV-fal a régi 03a csomagot kiváltja. Az alábbi összevetés a V2-ben hivatkozott **03a tervezési plafonhoz**, nem ténylegesen megrendelt bútor visszatérítéséhez viszonyít. A régi KI-L/KI-T, BN-L/BN-R és megfelelő stílusú tároló/relief nem marad pluszban. Más régi mű/textil keretet nem vonok le újra. Ha a régi 03a ténykeret kisebb, a tényleges többlet nagyobb.

| Stílus | Régi 03a plafon | V3 A+B+C | V3 eltérés a plafonhoz | Gazdaságos teljes csomag | Gazdaságos eltérés |
|---|---:|---:|---:|---:|---:|
| S01 | 800 | 740–1040 | -60 … +240 | 535–740 | -265 … -60 |
| S02 | 900 | 855–1160 | -45 … +260 | 650–860 | -250 … -40 |
| S03 | 750 | 720–1050 | -30 … +300 | 540–730 | -210 … -20 |
| S04 | 800 | 700–990 | -100 … +190 | 530–740 | -270 … -60 |
| S05 | 800 | 760–1110 | -40 … +310 | 550–760 | -250 … -40 |
| S06 | 900 | 790–1130 | -110 … +230 | 590–800 | -310 … -100 |
| S07 | 850 | 830–1200 | -20 … +350 | 590–800 | -260 … -50 |
| S08 | 750 | 680–990 | -70 … +240 | 510–700 | -240 … -50 |
| S09 | 800 | 740–1090 | -60 … +290 | 570–770 | -230 … -30 |
| S10 | 750 | 700–1010 | -50 … +260 | 520–720 | -230 … -30 |

**Alapértelmezett költségdöntés:** a gazdaságos változat a keretvédő kivitelezési kiindulás; az erősebb felületű csomag csak a 18 M-on belül igazolt átrendezéssel választható. A két részletes kreatív prompt az erősebb, fent külön beárazott anyagváltozatot írja le, **nem a gazdaságos áron mutatja azt**. A fájlban külön megvan a gazdaságos anyagcsere, így Claude a jóváhagyott költségváltozatot fordíthatja a végleges képbe. Mindkét változatban azonos falrendszer és kompozíció marad.

### 5.2 Későbbi egész-lakás kiterjesztés – külön költség, még nem megrendelt scope

A Cam_02-n túli elv ugyanaz, a konkrét szín/felület a §5 stílusleírásából jön. Minden alábbi sor **új/kiváltó munkacsomag bruttó becslése**, nem része az A–C összegnek:

| Kiterjesztési csomag | Előzetes mennyiség és kivitel | Becsült bekerülés | Gazdaságos megoldás | Keretsor / kettős számolás elkerülése |
|---|---|---:|---|---|
| Master kísérőfalak | 12–18 m² mintázatában halk vlies, előkészítéssel, ragasztással | 120–220 eFt | 80–140 eFt, kedvezőbb vlies, azonos teljes felület | Új felületcsomag; a V2 fejvég 04b megmarad, nem újra vásárolt |
| Master gardróbfrontok | Csak a mért PAX-frontok stílusváltása, tervezési példa 4–6 m² | 100–220 eFt többlet a sík alapfront fölött | 50–100 eFt, csak két hangsúlymező + sík, koherens többi ajtó | 04d alapfront kiváltása; mennyiség nem PAX-darabszám-jóváhagyás |
| Előtér + 05.2/05.3 kísérőfalak | Összesen 25–35 m² nyugodt vlies + 2 kisebb 60×90 nyomat | 250–430 eFt | 170–280 eFt, azonos felület olcsóbb vliesből, egyszerű nyomat | Előtér/hálók eredeti dekor/tároló soraihoz kapcsolódik; ismeretlen jóváírást nem vonok le |
| Konyha még nem kezelt száraz fal / végpanel | 4–6 m² tisztítható felület, a konyhatervvel egyeztetve | 60–120 eFt | 40–75 eFt, a választott konyhalaminált folytatása | 02a; a nappali B-ben már kezelt falrész nem ismétlődik |
| Fürdők + WC | Meglévő burkolat teljes megtartása; V2 tükör/tároló formálja a hátteret | 0 új falburkolati többlet | Ugyanez | 07 V2 alapcsomagja nem nulla és nem törölhető; V3-ban nincs új burkolat |
| Terasz | Meglévő felületek, V2 pad/textil megtartva | 0 új falburkolati többlet | Ugyanez | 13; a kültéri bútor alapára továbbra is a V2-ben |

A kiterjesztés előirányzata **530–990 eFt**, gazdaságos változat **340–595 eFt**; ez a fenti négy nem nulla sor összege, nem lakásonként mért ajánlat. A stílusok többségénél a gazdaságos felületi alap ajánlott. A nagy egyedi relief, festett teljes gardrób vagy plusz tükör külön opció marad; nem szabad ugyanezt az összeget prémium kivitelre idézni.

**Keretképlet Claude-nak:** új teljes lakás = aktuálisan igazolt teljes alap − ténylegesen kiváltott, még le nem kötött csomagok + jóváhagyott V3 csomagok + a korábban hiányzó szerelés/szállítás. Követelmény: **≤18 000 000 Ft; a külön 2 000 000 Ft tartalék változatlan.** A V2 régi maradványa nem új rendelkezésre álló pénz; a frissebb Toni-ár és a korábbi szék/premium eltérések rendezése is kell.

Nem állítom, hogy az egész-lakás V3 most igazoltan belefér. A tíz stratégia közül egyikre sem indokolt automatikus +0,5–1 M költés. Először a meglévő tároló/front/fejvég/dekor keretet szervezzük át; ha ez nem elég, egyszerűbb felület, kevesebb egyedi ív és egy közös nyomatsorozat következik. A teljes falkezelési elv marad, a drága technika csökken. A 18 M feletti változat **nem alapjavaslat, hanem elutasítandó vagy újratervezendő**.


### 5.3 Gazdaságos kivitel tételenként

Az A/B/C tartalom a §4.1 szerint értendő. Az alábbi összegek külön-külön is **bruttó becslések, ajánlatkötelesek**. B minden stílusban 100–160 eFt: kedvezőbb, saját stílushoz választott vlies + teljes felrakás; nem minden stílus ugyanazt a tapétát kapja. C a kisebb gyártási költségű, §5-ben leírt anyagváltozat, nem a drágább mű az olcsó áron.

| Stílus | A gazdaságos tároló/főfal | B gazdaságos kísérőfelület | C gazdaságos mű/karakterelem | Összesen |
|---|---:|---:|---:|---:|
| S01 | 400–520 | 100–160 | 35–60 | 535–740 |
| S02 | 520–650 | 100–160 | 30–50 | 650–860 |
| S03 | 405–510 | 100–160 | 35–60 | 540–730 |
| S04 | 395–520 | 100–160 | 35–60 | 530–740 |
| S05 | 415–540 | 100–160 | 35–60 | 550–760 |
| S06 | 455–580 | 100–160 | 35–60 | 590–800 |
| S07 | 455–580 | 100–160 | 35–60 | 590–800 |
| S08 | 375–480 | 100–160 | 35–60 | 510–700 |
| S09 | 410–510 | 100–160 | 60–100 | 570–770 |
| S10 | 385–500 | 100–160 | 35–60 | 520–720 |

## 6. S01 Kyoto Ink · részletes Cam_02 fal- és tárolókoncepció

**Egyetlen felismerhető kép:** hosszú grafit „tintavonal” előtt/alatt zárt tárolás, mellette keskeny, magas nyomtatott textilfront; mindezt füstszürke papírrostos felület veszi körül. Nem bézs japandi, nem shoji és nem lamellafal. A fehér mennyezet és ablakprofil éles, világos keret marad.

| ID / funkció | Tervezett méret, Sz×M×Mé | Anyag / gyártás | Beépítés és hozzáférés |
|---|---|---|---|
| KI3-L médiatároló | 240×48×40 cm **teljes külső** | Fehér 18 mm lapkorpusz, grafit U961 ST7 jelölt front, 2 mm ABS; 4 valódi, 60 cm-es frontmodul, egyenként nyíló | Padlón álló visszahúzott lábazat; 36 cm korpusz + kb. 2 cm front + 2 cm szerelőhézag = 40 cm. D16/D17/G08-nál levehető, szellőző hátlap |
| KI3-V függőleges zárt tároló | 60×220×30 cm teljes külső | Fehér korpusz, 3 külön nyíló front; 60×192 cm összefüggő grafika három 64 cm-es mezőre bontva, matt nyomtatott vlies-betéttel sík MDF-en, élvisszahajtás helyett lezárt betétkeret | Padlóra támaszkodik, falhoz borulásgátló; a grafika valódi ajtórésekkel szakad. Nem egy 220 cm magas, nehéz tapétás ajtó |
| KI3-P TV-háttér | 260×190×max.4 cm; alsó él z=0,55, felső z=2,45 | Két széles, egymáshoz képest 15 mm-rel eltolt grafit és füstszürke laminált sík; mögötte saját fehér falsík, nincs kivésett mélyedés | Rejtett, ellenőrzött fali sín/cleat, kábelek és TV-szerviz hozzáférhető. A TV rögzítése nem a dekorlap teherbírásán múlik |
| KI3-W kísérőfal | W02–W04, 14–18 m² becslés | Matt, apró papírrost-hatású füstszürke vlies; fizikai minta még kiválasztandó. Nem valódi japán kézműves papírnak nevezett olcsó nyomat | Sarkoknál zárás, szegőléc fölött tiszta él; fedlapok szabadok |
| KI3-A mű | 100×180×3 cm, W02-n javasolt, nem a TV előtt | Egy eredeti absztrakt grafika: halvány szürkés alapon egy széles, megszakított grafit tusmező és egy vékony függőleges szál. Matt vászon vakrámán, nem másolt mű | Mechanikus kétpontos falrögzítés a kapcsoló/szenzor szabadon hagyásával; nincs hátfény |

**Falhoz rendelés, nem Blender-módosítás:** W01-en a KI3-V javasolt y=4,35–4,95; KI3-L y=5,15–7,55, x=3,67–4,07. A KI3-P y=5,05–7,65; TV a meglévő D16/D17 környezetében. A 20 cm köztes rés szándékos, tapétás árnyékmező. A panel és a bútor külön mélységű; ettől építészeti, nem attól, hogy megnöveljük a falat. A teljes W01 megmaradó része ugyanazt a papírrostos felületet kapja. A W02 mű helye javasolt, pontos koordinátája a kapcsolók alapján véglegesítendő. Ha a vizsgált Cam_02-ben W02 nem látszik, nem kerül át a TV-falra a kép kedvéért.

A felület alacsony kontrasztú apró textúrája távolról csendes, közelről gazdag. A szekrényfront-nyomat **más**: nagy léptékű, alig két-három vonal. Ezek nem konkurálnak egymással. A tér többi felületének sötétsége nem érheti el a fő grafit tömegét.

**Költség:** KI3-L/V/P + W01 alap = A 520–680 eFt; KI3-W = B 160–260; KI3-A = C 60–100; összesen **740–1040 eFt**, régi 03a 800-hoz képest −60…+240 eFt. Gazdaságos változat A 400–520 + B 100–160 + C 35–60 = **535–740 eFt**. Ez a V2 csomag helyére kerül, nem mellé. A fő verzió ajánlatköteles; a gazdaságosnál a frontnyomat egyszerűbb, a panel eltolt mélysége 15 helyett 8 mm, a teljes kísérőfelület marad.

**Standard váz lehetősége:** BESTÅ 60×40-es vázat nem nevezünk 40 cm teljes kész mélységű bútornak. Ha Claude 44 cm-t igazol, standard váz + front + szerelőhézag válthatja a 36 cm mély egyedi korpuszt. A 20 cm-es standard váz is lehetséges kisebb tárolóhoz, de kevésbé használható médiamélységet ad. Egyik váltás sem automatikus, a kép a kiválasztott mélységet mutatja.

**Megmarad V2-ből:** P14 Lennon jobbos L 238×180×68; P09 Toni 200×90×75; 6 Eamy LG 55×53×75; Nifelia 200×300; Somar Ø76 csak ML04; KI-O kültéri pad csak a jóváhagyott helyen. A frissebb csomag Toni-ára 350 000 Ft, nem a V2 320 000-e. A Cam_02-ben az étkezőnek csak a terv szerinti részlete látszik. A korábbi külön KI-T panel megszűnik, a textilkarakter az új rendszer része.

## 7. S02 BiBo Nocturne · részletes Cam_02 fal- és tárolókoncepció

**Egyetlen felismerhető kép:** mélykék kabinetként megformált fal, amelyben az alacsony és magas zárt tömeg között egy keskeny, valódi ezüsttükör vág fényt. A környező falak ezüstszürke szövethatása csendes, következetes burkot alkot. Nem kék Kyoto: itt a felületi fényváltás, a puha sarok és a reflexió a nyelv; nincs tusgrafika vagy shoji.

| ID / funkció | Tervezett méret, Sz×M×Mé | Anyag / gyártás | Beépítés és hozzáférés |
|---|---|---|---|
| BN3-L alacsony tároló | 240×50×40 cm teljes külső | Fehér korpusz, matt mélykék laminált front, 4×60 cm-es valódi ajtó, ABS élek | Padlón álló lábazat, szerelőhézag a 40 cm-en belül, TV-blokk hátul hozzáférhető |
| BN3-V magas kabinet | 90×220×32 cm teljes külső | Egy 45 cm-es, magasságban megosztott ajtóoszlop + egy 45 cm-es fix tükrös szerelőmező; az ajtó külső síkján festett MDF, 20–30 gloss mintához kötött, nem tükörfényű zongoralakk. Fix felső sarok R6 cm; a belső korpusz derékszögű | Padlótámasz és falhoz borulásgátló. Nehéz front/pánt ellenőrzendő; az ív csak egyszerű fix záróelem |
| BN3-P háttér és felső zárómező | 240×190×max.4 cm, alsó él z=0,55 | Nagy, matt tintakék laminált mezők, valódi modulhézagok; nem épített fülke | Külön szerelt háttér, TV saját teherhordó megoldással, szellőzés és kábelajtó |
| BN3-R fix reflexiós betét | 45×180 cm, max.3 cm teljes kiállás | 4–6 mm ezüsttükör, biztonsági hátfóliával és mechanikus biztosítással; egyik felső sarok finom íve. Nem bronz üveg és nem tükrös tapéta | A kabinet egyik **fix**, nyílástól független oldalsó panelmezőjén, z=0,40–2,20; nem mozgó ajtó. Tartó és ragasztó az üveges rendszere szerint |
| BN3-W kísérőfal | W02–W04, 14–18 m² becslés | Világos ezüstszürke szövethatású vlies, finom keresztirányú fényváltással; nem csillámos, nem fémlemez | Tiszta sarokzárás, keret és szerelőfedél változatlan |
| BN3-A grafikai mező | 120×160 cm W02-n, max.2 cm | Saját absztrakt kék–szilva–ezüstszürke kétmezős grafika matt nyomaton, sík MDF-betéten; nem restaurant-mű másolata | Kétpontos falrögzítés; nincs önálló szobor vagy plusz bútor |

**Falhoz rendelés:** BN3-V javasolt y=4,25–5,15; BN3-L y=5,25–7,65; BN3-P az alacsony bútor fölött. BN3-R a magas kabinet fix homlokzati oldalsávján van, a 90 cm-es összszélességen belül: **egy 45 cm-es nyitható oszlop + egy 45 cm-es fix tükrös, sekély szerelőmező**. Ez nem két teljes értékű tárolóoszlop; a belső kapacitás szándékosan kisebb. A tükörmező mögé nem ígérek rejtett szekrényt. A nyíló frontok pontos kiosztása és a tükör tartószerkezete asztalos-/üvegesrajzon véglegesítendő.

A TV-közép a D16/D17 zónában marad, nem kell a teljes kompozíció közepére húzni. A tükör a valós üvegfal/panoráma részletét veri vissza, nem ad második ablakot vagy nagyobb szobát. BN3-R az A költségében benne van, külön BN-R V2 tükör nem marad. A W01 fennmaradó része a BN3-W azonos szövethatású háttérrel zárul.

**Költség:** A 650–820 + B 160–260 + C 45–80 = **855–1160 eFt**, régi 03a 900-hoz képest −45…+260. Gazdaságos A 520–650 + B 100–160 + C 30–50 = **650–860 eFt**. Sík kész laminált front, négyszögletes tükör vékony lekerekített kerettel, egyszerű nyomat; a reflexió és az összefüggő felület megmarad. Nem kell hozzá teljes magasfényű bútorfal vagy új világítás.

**Megmarad V2-ből, frissebb csomaggal:** P04 mélykék JÄTTEBO U 285×160×71, nyitott oldala a nyugati TV felé; P08 átlátszó Anouk 180×90×75; 6 Ciselia fekete lábbal 52,5×55×75; MarelyW szőnyeg a V2 termékrekord szerint. Brisia már **L00152CR05, egy Ø50 gömbös függeszték**, E27, csak ML04-en; nem a régi négygömbös mennyezeti változat. A BN-O kültéri pad és a 25×35 cm karfatálca megmaradhat a jóváhagyott helyén. A U belsejébe nem kerül kőasztal.

## 8. Claude-nak átadott integrációs és ellenőrzési pontok

1. **Új verzióban összeállítani:** aktuális common fixed + Cam_02 fixed + Hue fixed + Claude javított FRAME LAYOUT + a V3 **csereblokk**, nem a V2 mögé hozzáfűzött kiegészítés. A két promptfájlban lévő régi render-indítási engedélyszöveg nem terjed ki erre az új képre.
2. **Felületkivétel:** a common fixed „Walls and ceilings: painted white, smooth” mondata új csomagban úgy módosuljon, hogy a mennyezet, keretek, ajtók és nem kijelölt felületek maradnak; kizárólag a V3 W01–W04 és KI3/BN3 térképen megnevezett, költségelt tapéta/panel/front engedett. Nem globális „minden falat színezz át”.
3. **Geometria:** ellenőrizni a 40 cm teljes média-mélységet, 30/32 cm toronymélységet, az új nyitott ajtók mozgását, a TV látási tengelyt, a 90 cm utakat és a teraszbejáratot. Új torony miatt a régi kanapé-befoglaló PASS önmagában kevés. A fal menti koordináták tervezési javaslatok, nem módosított lock-adatok.
4. **Rögzítés és szerviz:** 10 cm-es falba rögzítés csak vezetékkeresés és falazat-/terhelésellenőrzés után; magas szekrény padlótámaszos. Nincs mennyezeti teher vagy padlóba csavarozott lábazat. A meglévő laminált padló mozgási hézaga szabad, szegőléc nem tűnik el varázslattal: bútor hátul takarás/kivágás. TV, kábel, ventiláció és FL02 hozzáférhető.
5. **Anyagminták:** a tapéta és a laminált szürkéje a valódi EL2184 mellett ellenőrizendő; festett MDF-nél jóváhagyott szín és gloss. Fronttapéta sík, stabil hordozón, lezárt szélekkel; előtte 30×30 cm tapadási/tisztíthatósági próba. Nem akusztikai vagy tűzállósági minősítés állítása.
6. **Költségkapu:** gazdaságos vagy fő anyagcsomag egyértelmű kiválasztása, két-három azonos tartalmú ajánlat később, külön tulajdonosi engedéllyel. Kereten belüliség csak a teljes lakás új egyeztetése után; a 2 M tartalékhoz nem nyúlunk.
7. **Képbemenet:** hiteles Cam_02 alap és Claude elrendezési segédképe az első geometriai bizonyíték; a bukott render csak kritikai referencia, nem geometry/style seed. Új anyagminták külön, pontos címkékkel. Referenciasorrendet és képszámot Claude írja a végleges csomagba.
8. **Két független kapu:** Claude műszaki/termék/felület Gate és Péter kreatív döntése. Egy jó geometriájú, de csupasz kép kreatív FAIL; egy lenyűgöző, de széthúzott tér műszaki FAIL. Egyik sem váltja ki a másikat.

### Kreatív elfogadás a próbakör után

- A TV-zóna képen építészeti együttesnek olvasható; a TV nincs magányosan egy komód fölött.
- Minden látható tömör falfelület visszavezethető W-ID-re és anyagra; nincs véletlen fehér falfolt. A tudatosan megtartott fehér káva/keret nem hiba.
- Szürkeárnyalatban is különbözik S01 réteg–grafika rendszere és S02 tömeg–reflexió rendszere.
- A WOW a semleges nappali fényben is működik; nincs a specifikáción túli meleg LED vagy extra lámpa.
- A nyomtatott anyag és laminált becsületesen látszik; nincs papír helyett valódi selyem, laminált helyett márvány vagy digitálisan eltüntetett ajtófuga.
- A két próba után először a kapcsolódó Cam_03 nézet és a fordított térnézet konzisztenciája ellenőrzendő, majd a többi helyiség/stílus részletesítéséről Péter dönt. A 40 V2 promptot most nem írjuk át.

## 9. Változásjegyzék V2 → Creative Upgrade V3 r1

- Megmarad mind a tíz stílus neve, fő karaktere és az elfogadott főbútorok/elrendezések; S01/S02 pontosítja a frissebb KEP-termékadatokat.
- A V2 nagy üres felső falra vonatkozó utasítását felváltja a teljes száraz falfelületi rendszer.
- KI-L/KI-T és BN-L/BN-R helyett integrált, tételazonosított tároló–fal csomag; régit és újat nem vásároljuk meg egyszerre.
- Festett MDF megengedett, de nem kötelező és nem alapból drága; minden fő megoldásnak van egyszerűbb, teljes falrendszert megtartó változata.
- A költségmodell különválasztja a résztermékárat, a komplett gyártási becslést, a V2 plafonhoz viszonyított többletet és a későbbi lakáskiterjesztést.
- Csak két Cam_02 kreatív blokk frissül. A V2 és a KEP-004 eredeti fájljai változatlanok, main-re közvetlen integráció nincs.

## 10. Forrásjegyzék és zárás

- [GOAL.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/GOAL.md)
- [07_skill/wsg-ertekalapu-stiluslabor/SKILL.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/07_skill/wsg-ertekalapu-stiluslabor/SKILL.md)
- [ai-coordination/RENDER_REALITY_GATE.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/ai-coordination/RENDER_REALITY_GATE.md)
- [05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md)
- [ai-coordination/results/WSG-20261024-ASTRA-KREATIV-V2.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/ai-coordination/results/WSG-20261024-ASTRA-KREATIV-V2.md)
- [ai-coordination/requests/WSG-20261024-STYLE10-KEP-004_CHATGPT_IMAGES_v1.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/ai-coordination/requests/WSG-20261024-STYLE10-KEP-004_CHATGPT_IMAGES_v1.md)
- [ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md)
- [03_blender/geometry_lock_A902_v2b.json](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/03_blender/geometry_lock_A902_v2b.json)
- [01_alaprajzok/villamos_kiallasok/OSSZESITO.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/01_alaprajzok/villamos_kiallasok/OSSZESITO.md)
- [05_promptok/KEP004_ChatGPT_Images_v1/README.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/fee7123f877bba3c2e2604ca021f5598c7e18b0d/05_promptok/KEP004_ChatGPT_Images_v1/README.md)

Költségforrások a §4 táblában, 2026-10-25-i hozzáféréssel. A mellékelt Kyoto-kép vizuális forrás, a main-ben archivált példány az r1 auditban azonosított. **Státusz: kreatív V3 átadva; geometriával, mintával, teljes költségvetéssel és ajánlatokkal még nem validált.** Következő lépés Claude integrációs ellenőrzése, majd Péter külön képfázis-döntése. Kép nem készült, Blender nem módosult, külső ajánlatkérés nem ment ki.

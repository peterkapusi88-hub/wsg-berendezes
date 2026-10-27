## R04 — legújabb rajzi és tárolási felülvizsgálat (2026-10-27)

Az új kiadás belépőpontja: [R04/OLVASD_EL_R04.txt](R04/OLVASD_EL_R04.txt). Ötlapos tulajdonosi használati útmutató, 93 A3 rajz-/specifikációs lap, szerkeszthető SVG-k és külön Blender-munkamásolat. **Feltételes felülvizsgálat, nem lezárt megvalósítás vagy gyártási jóváhagyás.** Az élő Excel CP3 főösszege változatlan; az R04 költsége külön, még ki nem választott forgatókönyv.

<!-- CP3_CURRENT -->
## Aktuális CP3-R03 — 2026-10-27

A legfrissebb tárolási és világítási csomag belépője: [CP3/README_CP3.txt](CP3/README_CP3.txt). Az élő Excel fő előirányzata **23 253 840 Ft**, a tartalék külön marad. A CP3 ajánlati/felmérési állapot; a régebbi fejezetek összegei történeti adatok.

# A-902 Kyoto Ink S01 – R02 megvalósítási munkacsomag

2026-10-26. Státusz: **érdemi ajánlati és egyeztetési csomag; a teljes megvalósítás még nincs lezárva**. Nincs gyártási engedély, végleges render-PASS, megrendelés vagy elküldött ajánlatkérés.

Az eredeti CP0 és CP1a megmaradt. CP0: `884788f70bdcade7d603f5e90d2f4085c99b939c`; CP1a: `5c855e968b5005e0cac58d2befb64f8f421733d5`; V3.3 célátvétel: `af9906a5039e0fe7198ca8ae8397d53e49352ead`. A munka ugyanazon engedélyezett execution ágon folytatódik. A main és a kreatív ágak változatlanok.

## Kézzelfogható átadás

- [Ötlapos tulajdonosi bemutató](outputs/A902_Kyoto_Ink_tulajdonosi_bemutato_5oldal.pdf): közérthető projektbemutató, költségmagyarázat, idő és kockázat, használati érték, tulajdonosi cselekvési terv. A korábbi egyoldalas PDF történeti példányként megmarad.
- [Élő Excel](outputs/A902_Kyoto_Ink_elo_regiszter.xlsx):159 sor, fő/gazdaságos számítás, források, lefedettség, ütemterv, eltérések,208 soros előzetes szabásjegyzék és külön05.2 alternatíva.
- [78 oldalas rajzcsomag](outputs/A902_R02_rajzcsomag.pdf):33 szerkezet saját lapja/specifikációja, alaprajzok, gardróbbelsők, TV/konyha/üveg részletek, ALT-052. Egyedi PDF-ek és szerkeszthető SVG-k a `drawings/` mappában.
- [17 oldalas szakági csomag](outputs/A902_R02_szakagi_egyezteto.pdf):világítás, víz/gép, felületek, textilek, kültér, ütemezés, nyitott kapuk.
- [39 oldalas teljes tételjegyzék](outputs/A902_R02_teljes_teteljegyzek.pdf) és [vizuális eltérések](outputs/A902_R02_vizualis_elteresek.pdf).
- [Tényleges Blender-munkafájl](blender/A902_Kyoto_Ink_R02.blend):elmentve és újranyitva;28 semleges kontrollkép, vizsgálati szkriptek és naplók. Méretmodellek, részben egyszerűsített formák; nem teljes gyári termékmodellek.
- [Renderoperátori indítóprompt](render_handoff/00_RENDEROPERATOR_INDITOPROMPT.txt),26 önálló angol prompt és [pontos manifest](render_handoff/manifest_R02.json). Végleges futtatásuk a dokumentált kapuk miatt blokkolt; generatív sorozat nem indult.
- `rfq/`:öt szakági ajánlatkérési tervezet, nincs elküldve.
- `targets/`:hat kiválasztott célkép tényleges PNG-je. Cam02/12 pontos V3.3, többi a korábbi kiválasztás. Régi nappali képek az `archive/renders/` alatt.

## Költség és bizonyíték

Fő előrejelzés **20 554 190 Ft**, takarékos javaslat **19 899 690 Ft**. A18M keret feletti előirányzati eltérés2 554 190, illetve1 899 690Ft. Külön2M tartalék érintetlen. Fő indikatív sáv17 740 028–27 132 689Ft, nem statisztikai vagy beszállítói garancia. Ellenőrzött webshop-termékár1 757 130Ft; írásos ajánlat0Ft; többi18 797 060Ft becslés. A megtakarítások részben becsült egyedi műszaki cserék, nem lekötött ajánlatok. Jakuzzi1,7M +emelés/bekötés0,3M megmaradt.

## Mi használható és mi maradt nyitva?

A fő anyag- és méretjavaslat, költségregiszter és rajzlapok **előzetes összehasonlító ajánlatkérésre/felmérésre** használhatók a nyitott feltételek feltüntetésével. Nem minden lap végleges gyártmányterv: teljes CNC/furatlista, vasalat SKU, minden késztermék, részletes gyári modell és szakági jóváhagyás hiányzik.

A konyhai folyosó840mm, a900mm célt nem teljesíti. Nyitott mosogatógép mellett nincs átjárás. A05.2 fő elrendezés íróasztala/széke ütközik az erkélyajtóval; külön ALT-052 integrált munkahely készült, korlátozott vizsgálatban0jelzéssel. Az alternatíva1380mm teljes magas gardróbot hagy2380mm helyett, +80000Ft±40000 becsült különbséggel; nincs elfogadva és nincs a főösszegben.

További lényeges nyitott tételek: pontos elszívó/mosogató/csap és kültéri főcsalád; teljes Hue/LED SKU és hozzáférés; textilek és minták; minden fiók és gépajtó használata; gyártói bútorazonosság; helyszíni szintek/küszöb/nyílások; elektromos, vizes, üveges és teraszstatikai feltételek. Végleges renderelés előtt a gyári termékfotókat/mesh-eket be kell csomagolni és a modellbe egyeztetni.

A korábbi12termékes korlátozás megszűnt. A folytatás a teljes lakásra vonatkozik; az R02 nem új CP0 és nem késznek nyilvánítás.

## Tulajdonosi bemutató bővítése - 2026-10-26

A megrendelő kérésére a tulajdonosi összefoglaló most pontosan öt A4-oldal. A dokumentum a fő kérdésekre válaszol: miért kerül ennyibe, miért tart eddig, mi jöhet közbe, mitől különleges, megéri-e, és hogyan gyorsítható. A 15 hetes gyorsított változat feltételes szervezési javaslat; a 17 hetes alapütem, az élő költségvetés és a műszaki jóváhagyási állapot nem változott. A renderpromptokon másik munkamenet dolgozik; ez a módosítás nem írja át őket.

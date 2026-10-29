AKTUÁLIS ÁLLAPOT / 2026-10-29
Az R16 ismert alkatrészméret-hibákat tartalmaz; a javítás/újragenerálás tulajdonosi döntéssel leállítva. Nem gyártási kiadás. A külső fény Philips Hue követelménye még nincs átvezetve a régi műszaki és költségexportokba. Részletes állapot és Claude-folytatás: CLAUDE_ATADAS/00_KEZDD_ITT.txt (a projekt gyökeréhez képest).

--- KORÁBBI DOKUMENTUM, TÖRTÉNETI ÁLLAPOT ---

## R16 – médiafal: bronzbetét, tusgrafika és magas fiókok (2026-10-29)

Aktuális médiafalcsomag: `R16_feluletek_fiokok/00_OLVASD_EL.txt`. Hat magas fiók, ajtós torony,200mm matt bronzbarna betétsáv oldalsó LED-del,8nyitásérzékelős belső fény. R16felváltja azR15alsó ajtós kiosztását. Az élő Excel öt érintett sora frissítve; becsült főösszeg26 212 190Ft. R16CAD/PDF/Blender/grafika/címke/MPR-tervezet ténylegesen átadva. Felmérés, gyári vasalati sablonművelet, anyag/nyomatminta, gépi és szakági próba nyitott. Asztal200mm eltolás: külön javaslat.

# Legutóbbi részfeladat: R15 – hat műhelyi továbbfejlesztés / 2026-10-29

Aktuális átadás: `R15_muhely/OLVASD_EL.txt`; `A902_TV_R15_hat_fejlesztes.zip`. 75 megmunkált faalkatrész,826 furat,12 kivágás,113 vasalati helyfoglalás;103 oldalas rajzkönyv,12 lapos Excel,73 aktív fúrási MPR-tervezet. Külön10darabos/84furatos/11MPR elsődarab-csomag. A korábbi revíziókat ne állítsd vissza.

Camar/MF375/TV-fali teherút kidolgozva, de fal és gyártói alkalmazás nyitott. A/B front–asztal alternatíva nem kiválasztott. Konkrét háromágú24V fényrendszer és szerviztálca. Címke/CSV/SQLite kapcsolatok tesztelve; valódi műhelyi import, woodWOP5 és gépi elsődarab nem tesztelt. Felmérés/anyagminták nem lezártak. Minden R15 ár becslés. A főregiszter24 673 390Ft; feltételes R15-egyeztetéssel25 161 190Ft, további átfedés vizsgálandó. A18M célkeret nem teljesült;2M tartalék érintetlen.

Az alábbiak történeti előzmények.

# Legutóbbi részfeladat: R14 TV-modul / 2026-10-28

Aktuális forrás: `R14_muhely/OLVASD_EL.txt`, az R14 adat- és rajzcsomag. 75 alkatrész,579 natív furat,69 aktív MPR,87 PDF-oldal,75 címke. R13-ra ne állíts vissza. A hátsó lécek/merevítők és TIP-ON adapterfuratok már kidolgozottak; a hátlapokat1mm kerületi hézaggal terveztük át. Az R13 kézi Excel-mezői megőrizve. Saját ellenőrzés: natív térfogat egyezik,0 CAD-adatbázishiba,0 Excel-képlethiba, minden címke visszakereshető, hibás hash és régi revízió elutasítva.

Még nyitott: fal- és panelrögzítés teljes teherútja; alsó3–4.front/asztal konfliktus (S10 továbbra is külön alternatíva); teljes konkrét fényrendszer és hőtechnika; felmérés/anyagminták; tényleges woodWOP5/műhelyi befogás/szerszám és elsődarab. A 126946Ft várható rejtett szerkezeti növekmény becslés, nem automatikusan a teljes projekthez hozzáadott költség. A helyi címkekereső nem telepített Livewood-integráció. Az aktív makrókat ne tiltsd le a felhasználó korábbi kifejezett kérése ellenére; az aktiválást ne keverd a gépi jóváhagyással.

Az alábbi R13 és R02 bejegyzések történeti előzmények.

# Korábbi részfeladat: R13 TV-modul / 2026-10-28

Aktuális műhelyi forrás: `R13_muhely/OLVASD_EL.txt`, `data/parts.json`, `data/holes.json`, `data/programs.json`. A három R13 DWG tartalmazza a293 valódi furatkivonást; R12-re ne állítsd vissza. A34 MPR-tervezet aktív a felhasználó kifejezett kérésére, de nincs woodWOP5 vagy gépi futtatási jóváhagyás. A SQLite/címkekereső helyi prototípus, nem igazolt Livewood-import.

Következő valódi műszaki lépések: a3-4. alsó front nyitásmódjának lezárása (S10 alternatíva, más korpusz/fogás/alsó mechanika), teljes fal- és hátlaprögzítés, LED-szerelvények és nyitók rögzítőfuratai, helyszíni hézagok/minták, műhelyi szerszám- és befogásadatok, woodWOP-megnyitás és próba. A teljes négy eredeti hiányterület még nincs lezárva. Az élő teljes projektköltség-Excel változatlan, új fix ár nincs.

Az alábbi R02 átadás történeti előzmény, nem a jelenlegi TV-modul állapota.

# Folytatási állapot – R02, teljes lakás

A korábbi csak12termékes szakasz lezárult; régi átadó az archive/CP1a alatt. Induláskor a tényleges távoli ágat és az aktuális Excelt kell visszaolvasni. Ne futtasd a CP0 build_data.py/build_workbook.mjs generátorokat a frissített állományokra.

Az R02 tényleges fájljait a README sorolja. A design_R02.json a jelen méretezett javaslat közös adatforrása. A teljes költséghez az élő Excel az elsődleges; elemek.json/CSV dokumentált pillanatkép. Bármely módosítás előtt cellánként olvasd vissza és őrizd meg a kézi változásokat. Ne importálj újra régi JSON-t az Excelre ellenőrzés nélkül.

Következő ellenőrzési pont: CP3 – pontos beszerzési és gyártói adatlezárás. Első kapuk:05.2 főelrendezés vagy ALT-052 döntés; konyha840mm és elszívóút; külterek konkrét SKU és jakuzzi feltételei; Hue/LED teljes rendszer; minden lámpa/árnyékolás/textil tényleges modellje. Ezek után közös rajz–Excel–Blender revízió, teljes nyitási vizsgálat és gyári termékazonossági kontroll. Rendelési engedély ettől külön szükséges, jelenleg nincs.

A műszaki/költségkutatás továbbra is végezhető; semmi nem jogosít rendelésre, ajánlatkérések elküldésére vagy keretemelés elfogadására. A látványveszteséggel járó anyag-, lámpa- és tárolóváltozások tulajdonosi döntésre várnak. Nem indítható tömeges új generatív renderelés.

Blender: a korlátozott indítás Metal/GPU-detektálásnál összeomlott. Külön jóváhagyott háttérfolyamat működött. Csak a saját execution munkamásolat módosítható; élő felhasználói Blender-session és eredeti forrás nem.

Reprodukálás: a scripts/blender_validate.py a forrásból új R02 főmodellt készít; UTÁNA az alternative_052.py adja hozzá a rejtett alternatívát. A reopen_validate.py a mentett állományt ellenőrzi. A detail_drawings.py alap77oldalt készít; az alternative_052_drawing.py egyszer fűzi hozzá az ALT-052lapot, a végső csomag78oldal. Ezeket érvényes eredményen ne futtasd feleslegesen újra. A render_handoff.py manifestje az aktuális.blend SHA256-ját tartalmazza.

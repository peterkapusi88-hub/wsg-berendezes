# Folytatási állapot – R02, teljes lakás

A korábbi csak12termékes szakasz lezárult; régi átadó az archive/CP1a alatt. Induláskor a tényleges távoli ágat és az aktuális Excelt kell visszaolvasni. Ne futtasd a CP0 build_data.py/build_workbook.mjs generátorokat a frissített állományokra.

Az R02 tényleges fájljait a README sorolja. A design_R02.json a jelen méretezett javaslat közös adatforrása. A teljes költséghez az élő Excel az elsődleges; elemek.json/CSV dokumentált pillanatkép. Bármely módosítás előtt cellánként olvasd vissza és őrizd meg a kézi változásokat. Ne importálj újra régi JSON-t az Excelre ellenőrzés nélkül.

Következő ellenőrzési pont: CP3 – pontos beszerzési és gyártói adatlezárás. Első kapuk:05.2 főelrendezés vagy ALT-052 döntés; konyha840mm és elszívóút; külterek konkrét SKU és jakuzzi feltételei; Hue/LED teljes rendszer; minden lámpa/árnyékolás/textil tényleges modellje. Ezek után közös rajz–Excel–Blender revízió, teljes nyitási vizsgálat és gyári termékazonossági kontroll. Rendelési engedély ettől külön szükséges, jelenleg nincs.

A műszaki/költségkutatás továbbra is végezhető; semmi nem jogosít rendelésre, ajánlatkérések elküldésére vagy keretemelés elfogadására. A látványveszteséggel járó anyag-, lámpa- és tárolóváltozások tulajdonosi döntésre várnak. Nem indítható tömeges új generatív renderelés.

Blender: a korlátozott indítás Metal/GPU-detektálásnál összeomlott. Külön jóváhagyott háttérfolyamat működött. Csak a saját execution munkamásolat módosítható; élő felhasználói Blender-session és eredeti forrás nem.

Reprodukálás: a scripts/blender_validate.py a forrásból új R02 főmodellt készít; UTÁNA az alternative_052.py adja hozzá a rejtett alternatívát. A reopen_validate.py a mentett állományt ellenőrzi. A detail_drawings.py alap77oldalt készít; az alternative_052_drawing.py egyszer fűzi hozzá az ALT-052lapot, a végső csomag78oldal. Ezeket érvényes eredményen ne futtasd feleslegesen újra. A render_handoff.py manifestje az aktuális.blend SHA256-ját tartalmazza.

# Legutóbbi részfeladat: R13 TV-modul / 2026-10-28

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

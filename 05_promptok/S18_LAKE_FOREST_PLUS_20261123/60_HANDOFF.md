# S18 – önálló folytatási csomag

## Következő lépés

A szövegek elkészültek. **Ne generáld újra a promptokat.** A `30_ALL_PROMPTS.json` az `image_id`, `variant`, `prompt_sha256`, kamera, eredeti LF-referencia és helyszíni forrás alapján azonosít minden munkát. Az új lakásképek állapota `NOT_GENERATED`; a korábbi feladat szerint a tényleges generálás a későbbi Claude Browser munkameneté.

1. Állítsd össze az inputot a prompt megadott sorrendjében. Az első kép a lakás saját geometriája/kamerája. Utána az adott A vagy B változat eredeti LF-képei; a hozzárendelt KZS-fotók csak a meglévő felületekhez és panorámához adnak bizonyítékot.
2. A811/A812: 31 kontroll másolata a `controls/` alatt. Az R9 forrás geometriai tanúsítása hiányos; ne állíts helyszíni méretvalidációt. A fehér Blender-szanitertömb nem bizonyítja a valódi termék formáját.
3. A902: a manifestben megnevezett hat kamera inputját össze kell állítani. Cam_02 és Cam_04 semleges forrása a main repóban megvan; Cam_12 v3, Cam_03 K1 és Cam_11c pontos képi inputja külön feloldandó. Cam_10-nél a rögzített kamerablokk létezik, de az elfogadott semleges képet nem helyettesítheti az ideiglenes WC-ben álló kamera. A konkrét képösszeállítás előtt nincs generálás.
4. Ahol nincs helyiséghez rendelt helyszíni anyagfotó (a QA listázza), pótold ezt az inputot. Ne használd a villa padlóját vagy a Blender ideiglenes shaderét.
5. Első kör: a három nappali A/B, összesen 6 összehasonlító kép. Második: konyha és master A/B. Ezután a többi kamera és funkcionális részlet. Egy véglegesített anyagkészlet menjen tovább minden nézetbe.
6. Egymás mellé téve ellenőrizd az eredeti referenciát és a lakásrendet: TV-mező, faerezet, pult, kárpit, gardróbmotívum, fejvég; külön a fix építészet és fényforrások. Ugyanaz a hibás felület nem válik elfogadhatóvá attól, hogy több kamerán következetes.

## Eredeti anyagok beérkezésekor

A konszignáció és eredeti textúra/gyártói anyagminták kerüljenek az M01–M10 referenciaazonosítókhoz, az A/B felületkiosztást megtartva. A képről nem állítható valódi anyagazonosság; a render csak vizuális egyezést céloz. A mozaik művészeti mező eredeti forrását és kivitelezési módját külön azonosítani kell. A kész bútorok modelljét nem lehet pusztán képi hasonlóság alapján megnevezni.

## Nyitott műszaki és költségkapuk

Teljes lakáskeret: A811 9+1 M, A812 9+1 M, A902 18+2 M Ft. A keretfelosztás nem ajánlat és nem igazolt végösszeg. Az eredeti kő/fém/kárpit nem olcsósítható csendben. Kültérben azonos vizuális karakterhez kültéri minősített anyag kell. A konyha, ruhalift, mosdó integrálhatósága, 100 cm zuhanyüveg, bekötés és fűtő-hűtő mennyezet korlátai továbbra is ellenőrizendők.

## Mentés és újraindítás

Az ág: `competition/s18-lake-forest-plus-20261123`. Mindig annak aktuális manifestjéből folytasd; a CP0 és az A811 CP1 már külön ellenőrzött mentés. A `80_FILE_INTEGRITY.json` a végleges csomag fájljainak SHA256-ját tartalmazza (saját magát és a később kiállított mentési nyugtát kivéve). A helyi átadási ZIP azonos tartalmat őriz. GitHub-írási hiba esetén a kész anyag innen folytatható, nem kell újraalkotni.

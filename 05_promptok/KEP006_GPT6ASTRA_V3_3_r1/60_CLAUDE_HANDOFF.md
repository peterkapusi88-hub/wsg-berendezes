# Claude átadás · Astra V3.3 / CP2.5 / CP3

## Mit kapott meg a csomag?

17önálló stílus identitylapja; S01–S10teljes lakásrész-szintű kreatív felzárkóztatás; S01–S15integrált művészeti revízió; S16sajátG63DNS és S17modellcsalád-szobaprogram;147teljes angol renderprompt; termék-,anyag-,elemlista és teljes lakáskeret;17világítási ellenőrzőlap. A megvalósítás KONCEPCIÓ / FELTÉTELES, a szövegek COMPLETE. Nem készült új render, nincs élőBlender-módosítás.

## Első teendő

Nyisd meg a30_GENERATION_MANIFEST.json fájlt ezen az ágon. A promptfájlokhoz tartozó SHA256-ot ellenőrizd. Olvasd a15_LIGHTING_LUXURY_CHECKLIST és53_NYITOTT_MUSZAKI_KAPUK fájlt. A történeti A/Bképeket a forráscommitokról töltsd be; a kész részeket ne generáld újra. A GOAL aktuális tulajdonosi döntéseivel egyeztesd az új lockot, a briefet és a valódi fotókat; egy későbbi explicit döntés felülírhatja a csomagot, de ezt változásnaplózd.

## Indítási sorrend

1. Kamera- és képforráscsomag: Cam12/02/03/04/11c/10 azonosító és helyiség;ne nevezz át más fotót. Cam11c ésCam10 pontos semleges fájlja először oldandó fel. Bath06.2hiányzó második fotó legyen jelzett, ne másik lakásból pótolt.
2. S01 ésS02 C Cam12+Cam02: az új főmű és a stíluskülönbség gyors összevetése. S11S12S13ugyanezen képei a célzott javítások ellenőrzésére. S16/S17Cam12,02,04először, hogy a két új DNS különbsége látszódjon. A karaktert ne tervezd újra a technikai integráció közben.
3. Minden stílus fennmaradó négy alapkamera;stílusonkéntazonos bútortranszform és termékvariáns. A/B/C nem három véletlen új lakás:azonos tervezett bútor/art, eltérő igazolt referenciamódszer.
4. A33_EXTRA_PRIORITAS szerint extra fürdő/terasz/master/konyha;nem helyettesíti az alaphatot. A javasolt fürdőkamera előbb Blenderben épül és ellenőrizendő.

## C-generálás referenciafegyelme

A manifest soronként megadja a promptot, kameraállapotot, elsődleges fotót és kontextusfotókat, termékazonosságot, korábbi kreatív referenciát, kimeneti nevet és QA-t. Image1 a pontos semleges kamera;fotókamerás extra esetén maga a pontos profi fotó. A többi profi fotó anyag/geometriai kontextus, nem nézőpontcsere. Termékfotó a konkrét szín/modul/láb/oldal;egyedi bútorhoz saját anyag és terv, nem kitalált katalóguskép. Ha nincs megfelelő forrás, a sortHOLD-on hagyd, közben másik kész sorral haladj. Általános inspirációt ne kezelj helyszíni bizonyítékként.

## Render utáni QA

Képenként: eredeti padló,fehér mennyezet,fehér belső keretek,szürke ajtók,fixfalak és valós kilátás;bútorSKU,modul,oldal és méret;azonosTV-fal/gardrób/art;1méteres üveg,folytonosmosdóbútor és használható tároló;LEDforrás/profil/szerviz fizikája;nem túlmelegítettfehér;árazatlan új elem. A takart részt NEMELLENŐRIZHETŐnek nevezd. Külön kép/eltéréslista és gépi fit-kimenet szükséges; a szöveges preflight nem renderPASS.

A képhibát külön v2fájl javítsa;eredetit őrizd meg. Jegyezd az inputSHAkat,modell/futtatási időt,csatolt valós képfájlokat és tényleges promptot. Jóváhagyás csak megfelelő részstátuszokkal:szöveg,termék,méret,ár,kamera,render külön.

## Mentés és folytatás

Branch: `competition/gpt6astra-v3-3-creative-revision-s16-s17-20261026`. A00_CHECKPOINT_NAPLO stílusonkénti commitjai megőrzik a részeredményt. Az új futások is ugyanitt vagy kifejezetten kijelölt renderágon folytatódjanak, a manifest image_id mezőjét használva. Sikeres,kész részt ne generálj újra. A már korábban létrejöttV3.1/V3.2A/Bállományok érintetlenek. A mostani csomag csak a17C alapot, kétújstílusA/B-jét és21extrát adja.

A történetiV3.2renderág58képfájlt jelez (47alapv1+11javítás), nem94elkészültképet. A hiányzó történeti képeket ne jelöld késznek. A stílusok A/Bkártyái létező archívumra mutatnak; a tényleges teljes51változatos képtár későbbi feladat.

Záró GOAL/skill ellenőrzés: main@d04a107f9890abbb6414ea496b77f3643833b2ce. A használhatósági elvek átvezetése és külön tételallokációja:55_HASZNALHATOSAG_ES_KOLTSEGFELOSZTAS.md.

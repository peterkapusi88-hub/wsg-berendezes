# CP V33 - célképek és költségelőrejelzés

2026-10-26. Előzmény: CP1a `5c855e968b5005e0cac58d2befb64f8f421733d5`; újabb távoli execution mentés az átvételkor nem volt.

A két pontos új célkép ténylegesen megnyitva: A902_S01_KyotoInk_Cam_02__V33_C_v1.png és A902_S01_KyotoInk_Cam_12__V33_C_v1.png. Eredeti PNG-k a targets mappában, SHA256 és eredeti elérés a data/render_manifest.json fájlban. A korábbi két kép az archive/renders mappába került. A többi négy korábban választott kép marad érvényes. Az üzenethez csatolt Cam03/04 V3.3 fájlokat nem tekintjük automatikus célcserének.

A két kreatív prompt a `4d2b7e857f034a7080bd62bd249e84a0a8e310e3` commitból visszaolvasva; helyi forrásmásolat a sources alatt. Ez promptforrás, a PNG-k generálásának commitját nem igazolja.

## Tartalmi változások és költséghíd
|Elem|CP1a Ft|V3.3 Ft|Tartalom|
|---|---:|---:|---|
|KI-030|310000|450000|Folytonos TV-panel/torony grafika és nagyobb panelmező|
|KI-031|210000|260000|Folytonos alsó tároló, előzetesen 3300 mm|
|KI-037|150000|105000|700×450×350 mm egyedi grafit laminált asztal|
|KI-038|70000|55000|300×300×450 mm egyedi grafit kocka|
|KI-123|60000|0|Kiváltva KI-132 textilpanellel; nem elhagyott munka|
|KI-132|80000|185000|2100×2880 mm levehető textilpanel, felmérendő|
|KI-133|60000|95000|Panelhordozó és rejtett rögzítés a képkeret helyett|

CP1a 20 083 350 Ft → V3.3 20 293 350 Ft. Kerethiány 2 293 350 Ft. A 2 000 000 Ft tartalék érintetlen. A változások tervezői becslések, nem beszállítói ajánlatok. A jakuzzi 1,7 M és beemelés/bekötés 0,3 M változatlanul szerepel. Gazdaságos változat ekkor még nem kész.

## Vizuális és műszaki egyeztetés
- W01: grafikus torony és TV-panel közös tusmotívummal; teherhordó TV-konzol a falon, levehető szerelőhát; felső, függőleges és alsó fény külön útvonal.
- W02: keret nélküli, teljes magasságú textilpanel; a kapcsoló/termosztát sávja szabadon marad. A render nem falméret-bizonyíték.
- Konyha: kréta magas/felső front, grafit alsó front és oldallap, F274 család betonhatású munkalap/hátfal. A régi Cam03 anyagkezelését ehhez egyeztetjük; a galéria méretét, géptornyot és FL01 pontját a hiteles alaprajz szerint javítjuk. Nem rendelünk új konyhát a torzított képméretek alapján.
- Lennon/Toni/Eamy/Nifelia azonos cikkszám minden nézetben. Somar az ML04 ponton. A Cam02 hengeres mennyezeti búrája és Enrave lapos teste látható eltérés; termékválasztási döntés szükséges.
- Függöny a belső szemöldökre, redőnyszerviz szabadon; küszöb/fellépés helyszíni mérete nyitott.
- A W02-re áthelyezett TV és nagy L/U kanapé kizárt alternatíva ebben a csomagban.

A munkafüzet importált példányát módosítottuk, nem futtattuk rá az eredeti generátort. Az átvételi munkafüzet és minden cella visszaolvasása archivált. A nyitott Excel zárolófájl miatt az export előtt fájlváltozás-ellenőrzés történt; későbbi mentéskor ezt ismételni kell.

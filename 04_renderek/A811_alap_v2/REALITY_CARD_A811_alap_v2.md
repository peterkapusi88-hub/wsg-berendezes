# A-811 – bútor nélküli alapképek az alaprajzi modellből · Render Reality Card v2 (2026-10-24)

**Azonosító:** `A811-ALAP-V2-20261024` · **Cél:** az Astra-féle B fázis (azonos kamerás stílusképek) geometriai alapja az A-811-hez. Nem látványterv. A v1 képeket ez a készlet váltja; a v1 nem került a `main`-be.

**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Nem PASS, mert:
- a padló dekorja nem igazolt;
- a falsík a hétfői helyszíni mérésig terv szerinti;
- az erkély szintje, a korlát és az osztó magassága feltételezés;
- a PDF ellentmondásos a konyha és az előtér burkolatában: az 5. oldalon kerámia, a 7. oldali burkolatkiosztási terven parketta. A modell a 7. oldalt követi.

## Javítás a v1-hez képest
A független tervhűségi ellenőrzés (2026-10-24) alapján, a PDF CAD-rétegeivel összevetve. A teljes lista: `03_blender/geometry_A811_A812/README.md`, „v2” szakasz.

| Hiba a v1-ben | v2 | Látszik |
|---|---|---|
| 5 mm-es, teljes magasságú rés a 05.1 külső falában | lezárva | Cam_05: a bal falon nincs sötét csík |
| 4 cm-es lyuk a 05.2-3 ajtó mellett | lezárva | – |
| A beltéri ajtók falnyílása 4 cm-rel szűkebb volt (5 ajtó), a tok 3 cm | terv szerinti falnyílás, 4 cm-es tok, a tiszta nyílás a tervvel egyezik | – |
| Hiányzott az EL4 lakáselosztó 12,5 cm-es GK előtétfala az előtérben (x 7,25–8,25) | modellezve | – |
| Erkélyosztó: falazott, fehér tömb | fém (antracit), 1,445 × 0,08 m, a terv szerint | Cam_02: az erkély jobb végén |
| A korlát tengelye 2,5 cm-rel eltolva, pálcatávolság 12 cm | terv szerinti tengely, ≈ 11 cm-es pálcatávolság | Cam_02, 04, 05 |
| Fölösleges falblokk a közlekedő végén; 1 cm-es rés a 05.1 \| 05.2-3 válaszfalnál; padlórés a HTH-ban | javítva | – |
| A homlokzati hőszigetelés egy sávja hiányzott | modellezve | csak az erkélyről |
| A WC álmennyezete (+2,40) hiányzott | modellezve | – |

Ellenőrzés: a validátor v2 PASS (0/0), réskeresés 5 magasságban 0 rés. A validátor PASS csak azt igazolja, hogy a modell egyezik a saját lock-fájljával; a tervhűséget a független ellenőrzés és a réskeresés adja.

## Bemenet és beállítás
| | |
|---|---|
| Modell | `03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend`, geometria v2. Forrás: a méretezett terv (5. old., 1:50, M1) vektoros rajza és CAD-rétegei. Lock: `geometry_lock_A811.json`. Leírás: `03_blender/geometry_A811_A812/README.md`. |
| Szkript | `03_blender/geometry_A811_A812/render_alapkepek_a8.py`. Csak a betöltött példányon módosít, nem ment. Utómunka (metaadat törlése, felülnézeti feliratok): `alapkep_utomunka_a8.py`. |
| Render | Blender 5.2.3, EEVEE sugárkövetéssel, 1600 × 1000, AgX + Medium High Contrast, expozíció +0,75. Ugyanaz a „semleges” beállítás, mint az A-902 v2b alapképein. Háttér-Blender a Macen; az élő `WSG_A902_stilusok.blend`-hez nem nyúlt. |
| Fény | Egyenletes, szórt nappali fény: egyszínű égbolt, 0,86/0,88/0,92, erősség 1,0. Nincs nap, mert az iránya nem igazolt; a rajz É-jele szerint az üvegfal ≈ ÉNy felé néz. Belső lámpa nincs. |
| Rejtve | A kiállás-réteg. Bútor, konyha és szaniter nincs a modellben. |
| Kamerák | 20 mm, z 1,5 m, változatlanok:<br>• Cam_02_Nappali_erkely (nappali → erkélyüveg);<br>• Cam_03_Etkezo_konyha (ablak felől → étkező, konyha);<br>• Cam_04_Haloszoba (05.2-3: ágyfal + üvegfal);<br>• Cam_05_Haloszoba_05_1. |

## Felületek – kamera szerint
A padló tónusa a kép alsó közepén mérve; ugyanott mérve a v1 és a v2 azonos. A v1-hez képest a képpontok 0,6–2,2%-a változott, csak a javított elemeknél (korlát, osztó, rés). A falértékek a v1 mérései.

| Felület | Cam_02 nappali → erkély | Cam_03 étkező → konyha | Cam_04 háló 05.2-3 | Cam_05 háló 05.1 | Státusz |
|---|---|---|---|---|---|
| Padló | meleg szürke sík tónus, sRGB ~152/150/147 | ~151/149/146 | ~150/147/145 | ~151/148/146 | Egger Grey Soria Oak EL2065 a 7. oldali burkolatkiosztási terv szerint. **Deszkaminta nincs modellezve, a tónus BECSLÉS** (nincs helyszíni fotó). A konyha és az előtér burkolata ellentmondásos a PDF-ben: hétfőn dönteni kell. |
| Falak | fehér, ~211/212/213 | ~210/211/212 | ~212/213/214 | ~212/213/214 | MEGLÉVŐ fehér festés |
| Mennyezet | fehér | fehér | fehér | fehér | MEGLÉVŐ. A hűtő-fűtő mező nem látszik (a kiállás-rétegben van). A WC álmennyezete (2,40) nem látszik. |
| Homlokzati üvegfal | 3,65 × 2,57 m:<br>• egyszárnyú erkélyajtó;<br>• beton oszlop;<br>• fix mező;<br>• kétszárnyú erkélyajtó.<br>Belül fehér profil. | – | 3,65 m-es elem, a 05.2-3 része, erkélyajtóval | 05.1: erkélyajtó + fix mező | TERV SZERINT (rajz). A profil színe a GOAL szerint IGAZOLT-F (belül fehér). A 2,57 m névleges nyílászáró-méret; hogy a kész padlótól mérendő-e, hétfőn derül ki. |
| Beltéri ajtó | – | bejárati ajtó a háttérben, belül fehér | – | – | TERV SZERINT, 4 cm-es tok. A beltéri ajtók színe az A-902 fotója alapján feltételezett. |
| Konyha | – | **nincs konyhabútor** (átadás konyha nélkül); a pengefal megszűnt, a konyha nyitott | – | – | TERV SZERINT (M1 vevői módosítás) |
| Erkély | lemez, pálcás korlát, a jobb végén fém osztó | – | korlát látszik | korlát látszik | **ELŐZETES.** A kontúr, a korlát helye és pálcás típusa a terv szerinti. A szint (−0,15), a korlátmagasság (1,10) és az osztó magassága NEM IGAZOLT. |
| Kilátás | **nincs modellezve** – egyszínű világos égbolt | – | ua. | ua. | A valós kilátás csak helyszíni fotóból jöhet; generikus skyline tilos. |

## Képek
- `A811_Alap-v2_blender_02_nappali-erkely.png`
- `A811_Alap-v2_blender_03_etkezo-konyha.png`
- `A811_Alap-v2_blender_04_haloszoba.png`
- `A811_Alap-v2_blender_05_haloszoba-2.png`
- `A811_Alap-v2_blender_06_alaprajz-kiallasok.png`: **ellenőrző felülnézet, nem Astrának szól.** Workbench, 1 m-es rács, rajta a 115 kiállás és az 5 hűtő-fűtő mező. Az x/y koordináták megegyeznek a `01_alaprajzok/villamos_kiallasok/A811_villamos.csv` értékeivel.
- `render_log_A811.json`: a futás pontos beállításai.

## Astrának – a B fázis promptjában kötelező
- Őrizze meg:
  - a falakat, az üvegfal osztását és a nyílásokat;
  - a kamera nézetét;
  - a padló meleg szürke tónusát. A padló meglévő szürke tölgy parketta (Egger Grey Soria Oak), nem beton és nem mikrocement.
- Új elem csak a reality card és a tételes lista szerint kerülhet a képre. Lámpa csak a mennyezeti kiállás helyére, kiállás-azonosítóval.
- A konyha üres. Konyhabútor csak a stílusterv tételeként jelenhet meg, méretezve.
- Az erkély korlátja pálcás, az osztó fém. Ha a stílusképen fontos, maradjanak semlegesek. Ne találjon ki üveg- vagy kőkorlátot, és ne falazott mellvédet.
- A kilátás valós forrásból jöjjön, ne kitalált.

## Észrevétel a kiállás-rétegből – tervezést érinti
**Hűtő-fűtő mezőn belül van** a konyha, a nappali, mindkét háló és a gardrób mennyezeti lámpakiállása: **ML02–ML07 és ML09**. A lámpa rögzítése előtt hőkamerával, fűtési üzemben ellenőrizendő, mint az A-902-ben. **Hétfőn ellenőrizendő.**

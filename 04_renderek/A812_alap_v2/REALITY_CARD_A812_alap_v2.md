# A-812 – bútor nélküli alapképek az alaprajzi modellből · Render Reality Card v2 (2026-10-24)

**Azonosító:** `A812-ALAP-V2-20261024` · **Cél:** az Astra-féle B fázis (azonos kamerás stílusképek) geometriai alapja az A-812-höz. Nem látványterv. A v1 képeket ez a készlet váltja; a v1 nem került a `main`-be.

**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Nem PASS, mert:
- a padló dekorja nem igazolt;
- a falsík a hétfői helyszíni mérésig terv szerinti;
- az erkély szintje és korlátmagassága, valamint a francia erkély korlátjának típusa és magassága nem igazolt.

## Javítás a v1-hez képest
A független tervhűségi ellenőrzés (2026-10-24) alapján, a PDF CAD-rétegeivel összevetve. A teljes lista: `03_blender/geometry_A811_A812/README.md`, „v2” szakasz.

| Hiba a v1-ben | v2 | Látszik |
|---|---|---|
| **Hiányzott a hálók francia erkély korlátja**, pedig a terven szerepel (Lakatos Külső réteg, x 2,915–2,935, 6 szakasz). A v1 README tévesen írta, hogy a rajzon nincs. | modellezve a terv szerinti helyen. Típus és magasság a terven nincs: semleges pálcás, 1,00 m, NEM IGAZOLT | Cam_04, Cam_05 |
| Hiányzott az EL4 lakáselosztó 12,5 cm-es GK előtétfala az előtérben (y 4,575–4,70) | modellezve | – |
| Hiányzott az álmennyezet: előtér +2,50, konyhasarok +2,45 (x 7,30–8,25, y 0–0,30) | modellezve | Cam_03: az előtér fölött és a konyha jobb hátsó sarkában |
| Padlóhiány a közlekedő → gardrób átjáróban | lezárva | – |
| A beltéri ajtók falnyílása 4 cm-rel szűkebb volt (4 ajtó), a tok 3 cm | terv szerinti falnyílás, 4 cm-es tok | – |
| A 05.1 és 05.2 ablaka közti pillér 27 cm széles, teljes mélységű volt | a terv szerint 16 cm-es vasbeton oszlop + kapcsolóprofil a tok síkjában | egyik kamerában sem |
| Erkélyosztó: falazott, fehér tömb | fém (antracit), 1,445 × 0,08 m, a terv szerint | Cam_02 |
| A homlokzati hőszigetelés és a fülke külső sarka hiányzott; rés a 05.3 sarkánál | modellezve, lezárva | csak kívülről |

Ellenőrzés: a validátor v2 PASS (0/0), réskeresés 5 magasságban 0 rés. A validátor PASS csak azt igazolja, hogy a modell egyezik a saját lock-fájljával; a tervhűséget a független ellenőrzés és a réskeresés adja.

## Bemenet és beállítás
| | |
|---|---|
| Modell | `03_blender/WSG_A812_alaprajz_ELOZETES_20261024.blend`, geometria v2. Forrás: a méretezett terv (12. old., 1:100, M1 KORR 2026.04.28.; a 11. old. 1:50-es lapja azonos vektorokkal) vektoros rajza és CAD-rétegei. Lock: `geometry_lock_A812.json`. Leírás: `03_blender/geometry_A811_A812/README.md`. |
| Szkript | `03_blender/geometry_A811_A812/render_alapkepek_a8.py`. Csak a betöltött példányon módosít, nem ment. Utómunka: `alapkep_utomunka_a8.py`. |
| Render | Blender 5.2.3, EEVEE sugárkövetéssel, 1600 × 1000, AgX + Medium High Contrast, expozíció +0,75. Azonos az A-902 és az A-811 alapképeivel. Háttér-Blender a Macen; az élő fájlhoz nem nyúlt. |
| Fény | Egyenletes, szórt nappali fény: egyszínű égbolt, 0,86/0,88/0,92, erősség 1,0. Nincs nap; a homlokzat a rajz É-jele szerint ≈ ÉNy-i. Belső lámpa nincs. |
| Rejtve | A kiállás-réteg. Bútor, konyha és szaniter nincs a modellben; az egyedi sarokkád be van építve (Péter), de nincs modellezve. |
| Kamerák | 20 mm, z 1,5 m, változatlanok:<br>• Cam_02_Nappali_erkely (nappali → erkélyüveg);<br>• Cam_03_Etkezo_konyha (ablak felől → étkező, konyha, előtér);<br>• Cam_04_Haloszoba (05.3 háló: ágyfal + ablakfal);<br>• Cam_05_Haloszoba_05_2. |

## Felületek – kamera szerint
A padló tónusa a kép alsó közepén mérve; ugyanott mérve a v1 és a v2 azonos. A v1-hez képest a képpontok 0,4–3,9%-a változott, csak a javított elemeknél. A falértékek a v1 mérései.

| Felület | Cam_02 nappali → erkély | Cam_03 étkező → konyha | Cam_04 háló 05.3 | Cam_05 háló 05.2 | Státusz |
|---|---|---|---|---|---|
| Padló | meleg szürke sík tónus, sRGB ~152/150/147 | ~151/148/146 | ~151/149/146 | ~151/149/146 | Egger Grey Soria Oak EL2065 a burkolatkiosztási terv szerint (a konyhában és az előtérben is parketta). **Deszkaminta nincs, a tónus BECSLÉS.** |
| Falak | fehér, ~210/211/212 | ~211/212/213 | ~211/212/214 | ~212/213/214 | MEGLÉVŐ fehér festés |
| Mennyezet | fehér | fehér; az előtérben **2,50 m-es álmennyezet**, a konyhasarokban **2,45 m** | fehér | fehér | MEGLÉVŐ. Az álmennyezet a terv szerint (Álmennyezet Lakás réteg), a kiterjedése helyszínen ellenőrizendő. |
| Homlokzati üvegfal / ablak | 3,65 × 2,57: kétszárnyú erkélyajtó + fix mező; belül fehér profil | – | 2,80 × 2,57, padlóig érő, 3 nyíló szárny | 2,87 × 2,57, padlóig érő, 4 nyíló szárny | TERV SZERINT. A hálók nyíló szárnyai a rajzon 45°-os ablakjellel. A 2,57 m névleges méret; a viszonyítási szintje hétfőn derül ki. |
| Beltéri ajtó | – | bejárati ajtó a háttérben | – | – | TERV SZERINT; a szín az A-902 fotója alapján feltételezett |
| Konyha | – | **nincs konyhabútor**; a konyha nyitott | – | – | TERV SZERINT. A felsőszekrény a sarokban legfeljebb 2,45 m-ig érhet. |
| Erkély / korlát | erkélylemez, pálcás korlát (lépcsős kontúr), a végén fém osztó | – | **francia erkély korlát** a padlóig érő ablakok előtt | ua. | **ELŐZETES.** Az erkélykontúr (a bal széle a 11. és 12. oldalon is kirajzolt) és a korlát helye terv szerinti. A szint (−0,15) és a korlátmagasság (1,10) NEM IGAZOLT. A francia erkély korlátjának helye terv szerinti; típusa és magassága (1,00) NEM IGAZOLT. |
| Kilátás | **nincs modellezve** – egyszínű világos égbolt | – | ua. | ua. | A valós kilátás csak helyszíni fotóból jöhet; generikus skyline tilos. |

## Képek
- `A812_Alap-v2_blender_02_nappali-erkely.png`
- `A812_Alap-v2_blender_03_etkezo-konyha.png`
- `A812_Alap-v2_blender_04_haloszoba.png`
- `A812_Alap-v2_blender_05_haloszoba-2.png`
- `A812_Alap-v2_blender_06_alaprajz-kiallasok.png`: **ellenőrző felülnézet, nem Astrának szól.** Rajta a 121 kiállás és a 8 hűtő-fűtő mező, a `A812_villamos.csv` koordinátáival.
- `render_log_A812.json`

## Astrának – a B fázis promptjában kötelező
- Őrizze meg:
  - a falakat, az ablakok és az üvegfal osztását;
  - a kamera nézetét;
  - a padló meleg szürke tónusát (meglévő szürke tölgy parketta).
- A hálók padlóig érő ablaka előtt **francia erkély korlát van** a terven. Ne vegye ki, és ne cserélje kitalált üveg- vagy kovácsoltvas korlátra; a típus hétfőn derül ki.
- Az előtérben 2,50 m-es álmennyezet van, a konyhasarokban 2,45 m-es. Ide nem kerülhet magasabb szekrény vagy rejtett világítás kiállás nélkül.
- A konyha üres. Konyhabútor csak a stílusterv tételeként, méretezve.
- Lámpa csak a mennyezeti kiállás helyére, kiállás-azonosítóval.
- A kilátás valós forrásból.

## Észrevétel a kiállás-rétegből – tervezést érinti
**Hűtő-fűtő mezőn belül van** a nappali-étkező, mindhárom háló és mindkét gardrób mennyezeti lámpakiállása: **ML03–ML08, ML17, ML18**. A lámparögzítés előtt hőkamerás ellenőrzés kell. **Hétfőn ellenőrizendő.**

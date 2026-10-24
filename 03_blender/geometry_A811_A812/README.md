# A-811 és A-812 – Blender-alapmodell (geometria v2, ELŐZETES) – 2026-10-24

**Státusz:** `TERV SZERINT – ELŐZETES`. A vektoros méretezett alaprajzból és a PDF CAD-rétegeiből készült, **helyszínen nem mért**. A falsíkok vakolatlan tervsíkok, a kész falsík oldalanként ~1–2 cm-rel beljebb lehet. A végleges változat a hétfői (2026-10-27) helyszíni mérés és fotók után, Péter jóváhagyásával készül.

| | A-811 | A-812 |
|---|---|---|
| Modell | `03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend` | `03_blender/WSG_A812_alaprajz_ELOZETES_20261024.blend` |
| Lock (validátor v2) | `03_blender/geometry_lock_A811.json` | `03_blender/geometry_lock_A812.json` |
| Geometria-adat | `A811_geometria_ELOZETES.json` | `A812_geometria_ELOZETES.json` |
| Ellenőrző kép (terv + modell) | `A811_geometria_ellenorzes.png` | `A812_geometria_ellenorzes.png` |
| Forrásrajz | 5. old., 1:50, M1 (KORR nem készült) | 12. old., 1:100, M1 KORR (2026.04.28.); a 11. old. 1:50-es lapja azonos vektorokkal |
| Belmagasság a modellben | 2,70 m (Kémeri: 2,69–2,72) | 2,70 m (Kémeri: 2,69–2,73) |
| Validátor v2 | PASS – LOCK 0, ERKÉLY 0, kamera rendben | PASS – ua. |
| Tervhűség | független ellenőrzés javítva (lásd „v2”), réskeresés 0 | ua. |
| Alapképek | `04_renderek/A811_alap_v2/` | `04_renderek/A812_alap_v2/` |
| Kamera-paraméterlap | `kamera_parameterlap_A811_A812.md` | ua. |
| Kanapé-méretpróba (U/L + TV + étkező) | `meretproba/MERETPROBA_KANAPE_A811_A812.md`; a terv bútorrajza és az L + szekrénysor változat: `meretproba/terv_elrendezes_A811.png` | `meretproba/MERETPROBA_KANAPE_A811_A812.md` |

**Fontos:** a validátor v2 PASS csak azt igazolja, hogy a .blend egyezik a saját lock-fájljával (nem változott semmi), azt nem, hogy a modell egyezik a tervvel. A tervhűséget a független ellenőrzés, a geometria-szkript réskeresése (`resek_6cm_alatt`: 0) és az 5 magasságban futtatott réskeresés (0 rés) adja.

## v2 – a független tervhűségi ellenőrzés javításai (2026-10-24)
Egy független ellenőrző a PDF CAD-rétegeit (Homlokzati fal, Válaszfal, T_Oszlop, Előtétfal (GK), Szerelő fal, Lakatos Külső, Álmennyezet, T_Gerenda, KÁVA) poligonokká alakította, és a modellhez hasonlította. A repóhoz nem nyúlt. 5 HIBA-t és 11 FIGYELEM-et talált; a HIBA-kat és a FIGYELEM-eket a PDF-en újraellenőriztem, és az alábbiak szerint javítottam.

| # | Megállapítás | Javítás a v2-ben |
|---|---|---|
| H1 | Hiányzott az EL4 lakáselosztó 12,5 cm-es GK előtétfala az előtérben. A-811: x 7,25–8,25, y 8,325–8,45 (méretszám 1,62⁵); A-812: x 7,32–8,25, y 4,575–4,70 (1,67⁵). | `Elotetfal_GK_EL4` mindkét lakásban; az előtér helyiségpoligonja ennyivel kisebb. A 2. oldali m² nem vonja le, ezért helyszínen igazolandó. |
| H2 | A-812: a hálók francia erkély korlátja **szerepel** a terven (Lakatos Külső, x 2,915–2,935; y 6,98–7,955 · 7,985–9,50 · 9,53–10,93 · 13,06–13,91 · 13,94–14,805 · 14,835–15,76). A v1 README tévesen írta, hogy nincs. | `Francia_erkely_korlat_1…6` a terv szerinti helyen. Típus és magasság a terven nincs: semleges pálcás, 1,00 m, NEM IGAZOLT. |
| H3 | A-811 05.1 külső fal: 5 mm-es, teljes magasságú rés (x 3,015–3,02). | lezárva (a pillér 3,015-től) |
| H4 | A-811 05.2-3 ajtó: 4 cm-es, teljes magasságú lyuk (y 3,736–3,776). | lezárva (a falcsonk a terv szerinti 3,775-től) |
| H5 | A-812: padlóhiány a közlekedő → gardrób átjáróban (x 7,22–7,32, y 4,80–5,60). | az átjáró a `kozlekedo_gardrob` helyiséghez került |
| F6 | 9 beltéri ajtónál a modell a terv 4 cm-es tokját falnak vette, és ezen belül még egy 3 cm-es tokot tett: a tiszta átjáró 2–6 cm-rel kisebb lett. | A `nyilas` a terv falnyílása (pl. A-811 05.1: y 1,70–2,60); a tok vastagsága a falnyílás és a tiszta szárnyszélesség különbségéből (beltéri ajtóknál 4 cm). Mind a 12 beltéri ajtó falnyílásának két végén a terven ott a lezáró falvonal. |
| F7 | A-811: fölösleges falblokk a közlekedő végén (x 5,135–5,31, y 1,60–1,70). | eltávolítva (`kivon`); a falsíkig érő padlóval |
| F8 | A-812: a 05.1 és 05.2 ablaka közti pillér túl széles volt (y 7,835–8,105, teljes mélységben). | a terv szerint 16 cm-es vasbeton oszlop (x 3,12–3,32, y 7,89–8,05) + kapcsolóprofil a tok síkjában (x 3,04–3,12); az oszlop melletti mélyedésben padló és szemöldök |
| F9 | Kisebb rések: A-811 x 0–0,01 (a 05.1 \| 05.2-3 válaszfal az üvegfalnál), A-812 a 05.3 sarka (y 16,808–16,82), A-811 HTH padlórés (y 1,486–1,50). | lezárva |
| F10 | Homlokzat kívül: hiányzó hőszigetelés (A-812 x −0,465…−0,305, y −1,03…0,925), szigetelés-sávok (A-812 y 4,52–4,695, A-811 y 0,90–1,08) és falsarok (A-812 x −0,975…−0,67, y 4,695–5,00). | modellezve |
| F11 | Az erkélyosztó a terven fém (Lakatos), 1,445 × 0,08 m (x −1,955…−0,51); a modellben 1,57 m-es, fehér, falazottnak látszó tömb volt. | fém (antracit) osztó a terv szerinti méretben; magassága a terven nincs (1,10 m feltételezve) |
| F12 | Erkélyszint (−0,15) és korlátmagasság (1,10): a terven nincs. A korlát pálcás, kb. 11 cm-es osztással; a helye egyezik (terv x −2,055…−2,005). | a korlát tengelye −2,03-ra, a pálcatávolság 11 cm-re igazítva; szint és magasság továbbra is NEM IGAZOLT |
| F13 | Hiányzott az álmennyezet: A-811 WC (x 7,30–8,25, y 4,85–6,60, +2,40), A-812 előtér (x 7,22–8,25, y 2,90–4,575, +2,50), A-812 konyhasarok (x 7,30–8,25, y 0–0,30, +2,45 – a felsőszekrény magasságát korlátozza). | modellezve (`Almennyezet_*`), a rajzi felirat szerinti magassággal |
| F14 | A vizes helyiségek szerelő- és előtétfalai, padkái nincsenek a modellben (szándékos). Az A-811 06.1 +0,18 m²-es eltérését a kádmagasságú padka (0,185 m²) okozza, nem a WC előtétfala. | szándékosan nincs modellezve; a lábjegyzet javítva |
| F15 | Az A-811 konyha és előtér burkolata ellentmondásos: az 5. oldalon „kerámia”, a 7. oldali burkolatkiosztási terven „lam. parketta”. | a modell a 7. oldalt követi; helyszínen dönteni kell |
| F16 | A 2,57-es ablakmagasság névleges nyílászáró-méret; nem dönthető el, hogy a kész padlótól mérendő-e. | helyszínen mérendő |

További kis javítás: a homlokzati üvegfalak tokjánál a geometria-szkript ablaknyílás-kivágása 1 cm-rel a belső falsíkon túl is vágott; ezt a válaszfal csatlakozásánál a `hozzaad_utana` pótolja.

**Ami rendben volt** (az ellenőrzés szerint): minden más falsík ±2 cm-en belül; az aknák és a vasbeton oszlopok; az üvegfalak kiváltói, fesztávjai; mind a 15 nyíló szárny és mind a 14 ajtó zsanéroldala, iránya és sugara; a méretszámok (legfeljebb 1,1 cm eltérés); a lakó- és hálóhelyiségek területe ±0,03 m²-en belül; az erkélykontúr ±1 cm-en belül (az A-812 bal széle x −2,035 a 11. és a 12. oldalon is kirajzolt, a v1 feltételezése tehát igazolt); a magasságok; a villamos JSON koordináta-rendszere.

## Mi van a modellben
- **Falak, pillérek, aknák** (`<lakás>_Falak`): 45 és 45 falelem, 2 és 5 gépészeti akna (tömör tömb). A homlokzati pilléreken az erkély felé a hőszigetelés is.
- **Előtétfal:** az EL4 lakáselosztó 12,5 cm-es GK előtétfala az előtérben (`Elotetfal_GK_EL4`).
- **Álmennyezet** a rajz szerint (`Almennyezet_*`): A-811 WC 2,40 m; A-812 előtér 2,50 m, konyhasarok 2,45 m.
- **Szemöldök** minden ajtó (2,10 m) és üvegfal (2,57 m) fölött; mennyezet 2,70-en (`Plafon_*`).
- **Beltéri ajtók** (`<lakás>_Nyilaszarok`): a terv szerinti falnyílásban 4 cm-es tok és csukott lap. A szín az A-902 fotója alapján feltételezett: világosszürke lap, szürke tok, belül fehér bejárati ajtó.
- **Homlokzati üvegfalak és ablakok:**
  - alsó és felső tok, a profilok (tömör sávok az üvegtáblák között), üvegtáblák a rajzi tokvonalakból;
  - A-812: a 05.1 és 05.2 ablaka között kapcsolóprofil;
  - a nyíló szárnyak nyitási negyedköre a lockban (`openings_meta`);
  - anyag: belül fehér profil, az A-902-ével azonos.
- **Padló helyiségenként** (`<lakás>_Padlo`):
  - parketta: Egger Grey Soria Oak EL2065 (7. és 14. oldali burkolatkiosztási terv); a tónus BECSLÉS, meleg szürke;
  - kerámia a fürdőkben, a WC-ben és a HTH-ban: Glitch Salt 60×60;
  - padló az ajtónyílásokban (küszöb) és az ablakmélyedésben is.
- **Erkély** (`<lakás>_Erkely_ELOZETES`):
  - lemez a rajzi erkélykontúrból;
  - feltételezett −0,15 m-es szint;
  - 1,10 m-es pálcás korlát, ≈ 11 cm-es osztással (a típus a terv szerinti);
  - a szomszéd erkély felé fém osztó (1,445 × 0,08 m);
  - A-812: francia erkély korlát a hálók padlóig érő ablakai előtt, 1,00 m.
  - **Szint, korlát- és osztómagasság, a francia erkély korlátjának típusa NEM IGAZOLT.**
- **Kamerák:** Cam_02 nappali → erkélyüveg, Cam_03 ablak felől → étkező/konyha, Cam_04 fő háló, Cam_05 második háló. Mind 20 mm, z 1,5 m, mint az A-902-ben. Felülnézet: Cam_01, Cam_06. A kamerák a v1-hez képest nem változtak.
- **Kiállás-réteg** (`<lakás>_Villamos_TERV`, renderben rejtve):
  - minden kiállás azonosítóval, a `01_alaprajzok/villamos_kiallasok/<lakás>_villamos.json` szerint;
  - a hűtő-fűtő mezők kerettel és átlóval;
  - a doboz nélküli jelek a legközelebbi falsíkra illesztve (az álmennyezet nem számít falnak), az eredeti pont a jelölő `x_terv`/`y_terv` tulajdonságában.
  - Ellenőrzés: `<lakás>_kiallas_reteg_ellenorzes.json`.
- **Render-beállítás:** semleges, mint az A-902 alapképein. EEVEE sugárkövetéssel, AgX Medium High Contrast, +0,75 expozíció, egyszínű égbolt, nap és lámpa nélkül.

**Nincs a modellben:** bútor, konyha (a lakások konyhabútor nélkül kerültek átadásra), szaniter (kád, zuhany, WC, mosdó), a vizes helyiségek szerelő- és előtétfalai és padkái, az A-811 06.2 fürdő mennyezeti dobozolása (a rajzon szaggatott vonal, kiterjedése bizonytalan), redőnytok, a kilátás és a felettük lévő szerkezet (az erkély fölött égbolt).

## Ellenőrzés a tervvel
**Helyiség-területek** a 8. emeleti megvalósulási terv (2. old., 1:125, 2026.05.20.) m²-ével. A 2. oldalt vonal-korrelációval illesztettük a lakáslapokhoz, a két lakás x-e közös, és y_A812 = y_A811 − 11,85: az A-811 felső fala az A-812 alsó fala. A terv a homlokzati szobák területébe az üvegfal tokjáig tartó ~20 cm-es ablakmélyedést is beszámítja, ezért a modell is így számol.

| A-811 | terv m² | modell m² | + ablakmélyedés | eltérés |
|---|---|---|---|---|
| Nappali+étkező | 30,93 | 30,23 | 30,96 | +0,03 |
| Konyha | 5,80 | 5,82 | 5,82 | +0,02 |
| Előtér | 4,04 | 3,93 | 3,93 | −0,11 ** |
| Közlekedő | 5,30 | 5,29 | 5,29 | −0,01 |
| Szoba 05.2-3 (gardróbbal) | 18,74 | 18,38 | 18,75 | +0,01 |
| Szoba 05.1 | 13,33 | 12,98 | 13,32 | −0,01 |
| Fürdő 06.2 | 3,82 | 4,26 | 4,26 | +0,44 * |
| Fürdő 06.1 | 4,77 | 4,95 | 4,95 | +0,18 * |
| HTH 09 | 2,48 | 2,46 | 2,46 | −0,02 |
| WC 08 | 1,47 | 1,65 | 1,65 | +0,18 * |

| A-812 | terv m² | modell m² | + ablakmélyedés | eltérés |
|---|---|---|---|---|
| Nappali+étkező | 33,85 | 33,12 | 33,85 | 0,00 |
| Konyha | 6,35 | 6,35 | 6,35 | 0,00 |
| Előtér | 1,78 | 1,68 | 1,68 | −0,10 ** |
| Közlekedő | 8,63 | 8,63 | 8,63 | 0,00 |
| Közlekedő gardrób része | 1,48 | 1,48 | 1,48 | 0,00 |
| Szoba 05.1 | 8,15 | 7,96 | 8,15 | 0,00 |
| Szoba 05.2 | 9,50 | 8,91 | 9,50 | 0,00 |
| Gardrób 10.2 | 3,21 | 3,21 | 3,21 | 0,00 |
| Szoba 05.3 (+10.3 gardrób) | 16,97 | 16,42 | 16,98 | +0,01 |
| Fürdő 06.2 | 4,31 | 4,77 | 4,77 | +0,46 * |
| HTH 06.1 | 3,45 | 3,62 | 3,62 | +0,17 * |
| Fürdő 08/09 | 4,37 | 4,62 | 4,62 | +0,25 * |

\* A fürdők terve a szerelő- és előtétfalakat, padkákat levonja; a modellben ezek nincsenek benne (az A-811 WC a levonás után pontosan 1,47 m²; az A-811 06.1 eltérése a kádmagasságú padka). A lakó- és hálóhelyiségek ±0,03 m²-en belül egyeznek.
\** Az EL4 előtétfal (0,125 / 0,116 m²): a 2. oldali m² nem vonja le, a modell igen. Helyszínen igazolandó, hogy megépült-e.

**Méretszámok a rajzról** (a modell falsíkjai között mérve):
- **A-811:**
  - nappali 6,17 × 4,90 ✓;
  - konyha 2,08 × 3,00 ✓;
  - 05.2-3: 3,22 + 1,70 (gardrób), 5,02, mélysége 2,70 ✓;
  - 05.1 4,42 × 2,70, fülke 0,67 ✓;
  - közlekedő 1,05 ✓;
  - 06.2 1,98 × 2,15 ✓, 06.1 1,98 × 2,50 ✓;
  - HTH 1,65 × 1,49 (rajz: 1,50), WC 0,95 × 1,74 (rajz: 1,75);
  - üvegfalak 3,65 / 3,65 ✓;
  - előtér 1,62⁵ az EL4 előtétfalig ✓ (v2).
- **A-812:**
  - nappali 3,89 / 7,22 / 5,60 / 4,70 / 5,80 ✓;
  - konyha 2,45 × 2,80 ✓;
  - 05.1 2,75 × 3,09 ✓, 05.2 2,75 × 3,24 ✓;
  - 10.2 2,75 × 1,30 ✓;
  - 05.3 3,10 × 4,09 ✓;
  - közlekedő 1,05 × 7,93 ✓;
  - 06.1 1,40 × 2,83 ✓, 08/09 1,40 × 3,30 ✓;
  - 06.2 2,20 ✓; a 2,29⁵ a 6–7 cm-es gipszkarton előtétfalig mér;
  - előtér 1,67⁵ az EL4 előtétfalig ✓ (v2);
  - ablakok 3,65 / 0,905 / 2,875 / 2,80 ✓.

## Feltételezések és nyitott pontok (hétfőn ellenőrizendő)
1. **Falsíkok, nyílások, belmagasság:** helyszíni mérés (lézer), legalább a nappali, a háló és az üvegfalak. A 2,57-es nyílászáró-magasság viszonyítási szintje (kész padló?).
2. **Erkély:** a padló szintje az előszobapadlóhoz képest, a korlát magassága, a fém osztó magassága, a lemez széle.
3. **A-812 francia erkély:** a korlát a terven szerepel; a típusa és a magassága helyszínen.
4. **EL4 előtétfal (12,5 cm) mindkét előtérben:** megépült-e, és milyen mély. Az előtérszekrény ennyivel sekélyebb.
5. **Mennyezeti lámpakiállás a hűtő-fűtő mezőben:** a lámparögzítés előtt hőkamerával, fűtési üzemben ellenőrizendő, mint az A-902-ben.
   - A-811: ML02–ML07 és ML09 (konyha, nappali, mindkét háló, gardrób).
   - A-812: ML03–ML08, ML17, ML18 (nappali-étkező, mindhárom háló, gardróbok).
6. **Álmennyezet:**
   - A-811: a WC-ben 2,40 m (rajz, modellezve); Péter összesítője szerint az előtérben és a fürdőkben is van (min. 2,40), ezek kiterjedése a rajzon nincs, nincsenek modellezve.
   - A-812: az előtérben 2,50 m, a konyhasarokban 2,45 m (rajz, modellezve). A konyhasarok a felsőszekrény magasságát korlátozza.
   - A kiállás-réteg ezeken a helyeken a lámpajelölőt álmennyezet-magasságba teszi.
7. **A-811 konyha és előtér burkolata:** az 5. oldalon kerámia, a 7. oldalon parketta – melyik épült meg.
8. **Tájolás** (a rajz É-jele alapján, tájékoztató): a homlokzati üvegfal (−x) ≈ ÉNy felé néz, a rajz +y iránya ≈ ÉK.
9. **Parketta-tónus:** BECSLÉS (Egger: „meleg szürke”), helyszíni fotóval pontosítandó.

## Újrafuttatás
```
python3 a8_geometria.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf     # geometria-JSON + réskeresés (a PDF nincs a repóban)
python3 a8_ellenorzo_kep.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf # ellenőrző kép
WSG_KEZI_FUTTATAS=1 WSG_LAKAS=A811 python3 -c "import sys,bpy; sys.argv=['x','<repo>']; exec(open('build_a8_modell.py').read())"
WSG_LOCK=03_blender/geometry_lock_A811.json WSG_VILLAMOS=01_alaprajzok/villamos_kiallasok/A811_villamos.json python3 -c "import bpy,runpy; bpy.ops.wm.open_mainfile(filepath='03_blender/WSG_A811_alaprajz_ELOZETES_20261024.blend'); runpy.run_path('03_blender/geometry_validator_v2.py')"
WSG_KEZI_FUTTATAS=1 <Blender> -b WSG_A811_alaprajz_ELOZETES_20261024.blend --python render_alapkepek_a8.py -- <kimenet>
python3 alapkep_utomunka_a8.py <render-kimenet> <repo>
```
`pdf_kinyeres/ivek.py`: az ajtó-nyitásívek kinyerése, a zsanért és a sugarat adja. A PDF rajzelemei CAD-réteg nevet hordoznak (PyMuPDF `get_drawings()` → `layer`); a v2 javításai ezekre a rétegekre épülnek.

**A validátor v2 bővítése:**
- A lock `gyujtemeny_elotag` kulcsa választja ki a lakást.
- Az A-811/A-812-ben a tetőkert helyett az erkélyt ellenőrzi.
- A nyíló ablakszárnynál csak a nyitási negyedkört vizsgálja.
- A konyha- és a 05.2-ágyvizsgálat csak az A-902-ben fut.
- Az A-902 eredménye változatlan, regressziós próbával ellenőrizve: FAIL 89 / 82, a hibalista azonos.

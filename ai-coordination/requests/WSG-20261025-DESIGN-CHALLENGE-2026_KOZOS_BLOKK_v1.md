# WSG DESIGN CHALLENGE 2026 – közös versenyblokk (§0 v3.1 = „VB”) és a 11 célzott szövegcsere – VÉGLEGES (2026-10-25)

**Állapot:** végleges. A blokk szó szerint, bájtra azonosan be van építve a három indítópromptba:
- `ai-coordination/requests/DC2026_inditas/A_GPT6_Astra_Medium_ChatGPT_Work.md`
- `ai-coordination/requests/DC2026_inditas/B_Claude_Fable51_High.md`
- `ai-coordination/requests/DC2026_inditas/C_Claude_Opus55_High.md`

Indítási útmutató: `ai-coordination/requests/DC2026_inditas/00_INDITASI_UTMUTATO.md`.

**Közös forrásállapot:** ág `competition/baseline-20261025-v3`, commit `45632b5ad5586e1f3f884a8f723c1cc13cda6da3` = main `5ebc7d7` + PR #20 r2 (`f190e5f`, kameracsomag C) + PR #19 (`cf3b523`, közös bemenetek). A PR-ek nincsenek beolvasztva.

**Források:** a ChatGPT által összeállított három indítóprompt és a preflight-kérés (Péter, 2026-10-25 03:13); Péter döntései 03:32–05:00 (66 képes készlet, 60 saját + 6 közös kalibráció; ő a döntőbíró; hero-nézetek először; C1/C2 egyszer, Claude; költség-keresztellenőrzés; közös baseline; C elrendezés és K1; asztalforma szabad, külön méretpróbával; fénycsere Cam_02 ↔ Cam_12; a Cam_12 nem kreatív korlát; a fix alap versenyfeltételezés); a PR #20 r2 átadása (04:50).

**Miért „VB.x” a számozás:** az r2 briefnek saját 0. fejezete van (WOW-diagnózis), és az önellenőrző listája „§0.2”-re hivatkozik; a „§0.x” kettős jelentésű lett volna.

---

## 1. VB – KÖZÖS VERSENYBLOKK (§0 v3.1, végleges, 2026-10-25) – mindhárom versenyzőnek szó szerint azonos

**Elsőbbség:** ez a blokk felülírja az indítószöveg, az r2 brief, a GOAL.md, a házirendek és a repó minden más dokumentumának ellentmondó mondatát. A „VB.x” hivatkozás erre a blokkra, az „r2 §x” hivatkozás az r2 briefre utal (az r2 saját 0. fejezete a WOW-diagnózis, nem ez a blokk).

**VB.1 Forrásállapot, ágak, elavult anyagok**
- Közös, rögzített verseny-baseline (v3): ág `competition/baseline-20261025-v3`, commit `45632b5ad5586e1f3f884a8f723c1cc13cda6da3`. Tartalma: a main `5ebc7d7` + a PR #20 kameracsomag C végső állapota (`f190e5f`; benne a PR #17 és #18) + a PR #19 közös versenybemenetei (`cf3b523`). A PR-ek a mainbe nincsenek beolvasztva; a Cam_12 v3 és a Cam_03 K1 Péter által elfogadott kamerajavaslat. Az élő Blender-fájl Péter gépén érintetlen.
- Kizárólag ebből a commitból dolgozol. A saját ágadat (lásd a fejlécet) pontosan ebből a commitból hozod létre – nem a mainből, nem más ágból, nem újabb commitból; a draft PR-ed célága `competition/baseline-20261025-v3`. A main-t és a GOAL.md újabb változatát a verseny alatt nem olvasod: mindhárom versenyző ugyanazt az információt kapja; a verseny közben születő új tulajdonosi döntéseket Claude az integrációnál érvényesíti.
- Nem módosítod: a baseline-ágat, a main-t, a GOAL.md-t, a közös fájlokat, a másik két versenyző ágát és PR-jét. PR-t nem merge-elsz és nem zársz le.
- Közös, csak olvasható versenyfájlok a baseline-commitban:
  - `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md` – geometria, étkezőváltozatok, kamerák, fény;
  - `ai-coordination/inputs/A902_verseny/KOZOS_FIX_ALAP_v1.csv` és `.md` – közös költségalap;
  - `ai-coordination/inputs/A902_verseny/HUE_ALAPCSOMAG_v1.md` – Hue-rendszerelv és fajlagos árak;
  - `05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/` – a hat közös kalibrációs prompt;
  - `05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv` – a 66 soros képregiszter (kep_id);
  - `03_blender/validator_nyilvantartas_A902_kameracsomag_C.md` – a külön hibanyilvántartás;
  - `ai-coordination/results/WSG-20261025-A902-KAMERACSOMAG-C_r1.md` és `…_r2_ATADAS.md` – a kameracsomag bizonyítékai.
- **ELAVULT, nem használható** (a baseline-ban történeti okból benne maradt): `GEOMETRIA_C_KAMERACSOMAG_v1.md` (→ v2); a V3.1 brief r1 változata (→ r2); a `05_promptok/KEP004_ChatGPT_Images_v1/` C1/C2 promptjai (→ közös V3.1 kalibráció); a 2D kerek-asztal próba (`ai-coordination/results/WSG-20261025-A902-ELRENDEZES-C-KEREK-ASZTAL_r1.md` → GEOMETRIA v2 2. pont); a P902_24A elrendezés és a PR #18 A és B változata (→ C); a Cam_12 v2 (→ v3); a régi Cam_03 [4,70; 7,70] (→ K1); a GOAL.md 7. pontjának 2026-10-25 04:40 előtti fény-, Cam_03-, elrendezés-, étkező- és kalibrációs szabályai; a repóban lévő `WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` korábbi szövege (→ ez a blokk); a `competition/baseline-20261025` és `-v2` ág, valamint a GOAL.md-ben szereplő korábbi baseline-SHA-k (`32ba7bd`, `a8ab8d3`, `ce06496`); a korábbi `45d1e4d` forráscommit.
- Az r2 briefből ez a blokk kifejezetten felülírja: a képszámot és a kalibrációt mint versenyzői kimenetet (r2 fejléc, §8, §10, §11.0 „Prompt-kimenet”, §11.7, §11.9, §11.12 → VB.5); a §11.12 és a C rész ág-, mappa-, PR-jelölő- és folytatási szövegét (→ fejléc és VB.10); a §11.6 fénytábláját és a §11.11 Cam_03- és Cam_12-leírását (→ VB.3); a §11.2 „x < 4,40 és y > 7,70 között ne legyen magas szekrény” kamerakorlátját (→ VB.3); a §11.5 „az S02 U északi vége 0,225 m-re van az üvegtől” mondatát és a §11.8 elrendezési szövegét (→ VB.2); a §11.1 S01 Toni 200-as és S02 Anouk asztalát (→ VB.2); a §9 és §11.10 „teljes lakásszintű” költségkérését (→ VB.6); a B részt (Claude feladatai) – az nem a te feladatod. Minden más r2-előírás érvényes: kreatív cél, WOW-diagnózis és -mérce, rejtett LED, Hue-elv, teljes faltervezés, Péter hat eszköze, teljesebb berendezés, méretezett elemlista, prompt-forma, önellenőrzés.

**VB.2 Geometria – a C alapelrendezés** (GEOMETRIA_C_KAMERACSOMAG_v2.md 1., 2. és 4. pont; terv szerinti geometria, helyszínen nem mért)
- **Közlekedés:** fő utak ≥ 0,90 m betolt székkel (terasz-tolóajtó, konyha, hálók folyosója, 05.3 ajtó); székkihúzás ≥ 0,90 m; a kanapé legközelebbi pontja és a TV-fal bútora között ≥ 0,60 m; kanapé–dohányzóasztal 45–50 cm; az ágy mellett ≥ 60 cm; az ajtók szabadon nyílnak.
- **Kanapé:** minimum L, inkább U (Péter: „nagyon fontos”); íves vagy félhold kanapé csak puffal, amellyel L/U-ként működik. A háttámla keletre, az étkező felé néz; a hosszú ülés észak–déli, nyitott a nyugati TV-fal felé; az északi vége szabadon hagyja az üveget. A háttámla legkeletebbi helye x 6,67 (L) / x 6,60 (U). Blender-próbával igazolt: Westwing Lennon L 238 × 180 (S01), IKEA JÄTTEBO U 285 × 160 (S02); 2D-próbával: Westwing Wolke L 258 × 167. Mélyebb kanapé (pl. Kave Home Gala U 300 × 225) a C-ben 40 cm-es TV-bútorral nem fér el; minden más kanapé külön méretpróbát kap.
- **TV-fal (W01, x 3,67; y 4,05–8,05):** zárt szekrénytest legfeljebb 60 cm mély – lehetőség, nem kötelező mélység; a mennyezetig érő szekrénytest teteje és a hűtő-fűtő mező (HF03, x 3,77-től) kapcsolata FELTÉTELES – CLAUDE AUDIT SZÜKSÉGES; ≤ 4 cm-es panel árnyékfugával a mennyezetig mehet. A TV a falsíkon vagy a fülke hátfalán, saját teherhordó tartón (képernyő x ≈ 3,77); egy 60 cm-es szekrény elejére téve a nézőtáv 2,0 m alá esne – kerülendő. A TV-csatlakozók (G01–G04, D16, D17, G08) y 6,11–6,44 között, a D18 y 4,75-nél, az FL02 fali kiállás y 7,85 / z 2,85-nél: a TV és a középső mező ehhez igazodjon; előttük kivehető vagy szellőző hátfal, a D18-hoz szervizkivágás. A kameracsomag próbatömbjében (két szimmetrikus magas szekrény, y 4,25–5,05 és 6,85–7,65) a 75"-os képernyő 5 cm-rel belelógott az északi szekrénybe: ilyen elrendezésnél legfeljebb 65–70"-os TV vagy szélesebb középső mező kell.
- **Konyha:** konyhabútor nincs. IKEA METOD-váz, két sor 62 cm mélyen, a sorok között 85–86 cm (FELTÉTELES); a kb. 85 cm magas nyugati mellvéd marad – nincs sziget, nincs mennyezetig érő fal; a hűtőoszlop helyét a D13 rögzíti; front, munkalap és hátfal stílusonként.
- **Mennyezet és áram:** a mennyezeti hűtő-fűtő mezőkbe nem fúrunk; fény és áram csak meglévő kiállásról – nappali: ML04, ML05, FL01, FL02, D-pontok; master: ML06, D20–D23, D26; fürdő: a mennyezeti és a mosdó feletti pont. Az ML05 lámpatestjének rögzítése vizsgálandó, nem automatikus engedély. Bútor és TV rögzítéséhez fúrni szabad (vezetékkeresővel). Kapcsoló, termosztát, érzékelő, kaputelefon nem takarható. Függönysín falra szerelve, a szemöldök belső síkján vagy a kávában (nappali: y 8,05, z 2,53–2,90; master: a 0,33 m-es falsáv az üveg fölött; a káva mélysége hétfőn mérendő); a redőny-szervizfedél szabad.
- **Étkező – jóváhagyott alapváltozat:** hosszanti asztal 160 × 90-es befoglalóval (x 8,00–8,90; y 5,40–7,00) az ML04 alatt, hat hely 2+2+1+1 (oldalszékek tengelye y 6,10 és 6,70), az ML04 0,12 m-re a középtől; mindkét kanapétípussal és 40–60 cm-es TV-fallal minden kötelező méret teljesül, a kihúzás behúzott függönnyel is ≥ 0,93 m. Igazolt asztal: Westwing Toni ovális 160 × 90 (259 990 Ft, 2026-10-25). A Toni 200 és – ebben a 2+2+1+1 alapváltozatban – az Anouk 180 × 90 nem elfogadott (függönnyel 0,78 m-es kihúzás). További 160 × 90-es jelöltek (magyar ár és szállítás ellenőrizendő): Kave Home Kesia 160 (220) × 90 bővíthető, Kave Home Argo 160 × 90, Westwing/KARE Artistico 160 × 90.
- **Más asztalforma** – kerek, ovális, bővíthető vagy egyéb – kreatív alternatívaként javasolható, de minden eltérő forma és méret külön Blender-méretpróbát kap Claude-tól; a C megfelelősége nem vihető át; igazolásig a státusz „elrendezésben ellenőrizendő”. A kerek asztal (hat szék körben) Blender-próbája (validátor PASS, függönysávval): Ø150 (pl. Kave Home Nealy) csak sík, ≤ 4 cm-es TV-fallal és a kanapé legnyugatibb helyén (háttámla L x 6,11 / U x 5,91), az ML04 0,31–0,41 m-re oldalt; Ø140 ugyanígy; Ø130 40 cm-es TV-bútorral és U-kanapéval (háttámla x 6,27; ML04 0,21); 40 vagy 60 cm-es TV-bútorral a Ø150 nem fér el. A kerek asztal tehát megköti a TV-fal mélységét és a kanapé helyét, a függeszték nem kerül középre (az ML04 fix), a nyugatabbra tolt kanapé a Cam_12 előterébe kerül – ezt a kompromisszumot a tervben ki kell mondani.
- **Teraszajtó – FELTÉTELES:** a hétfői (2026-10-26) helyszíni ellenőrzésig a hat állandó ülőhely és a terasz egyidejű elérése nem igazolt. Ha a középső szárny nyílik, az alapváltozat rendben (0,95–1,00 m). Ha csak a legkeletibb, 0,93 m-es szárny, egyik hatszemélyes változat sem tartja meg egyszerre a terasz elérését és minden fő utat (96 vizsgált eset); a lehetőségek jelölt kompromisszumok, nem elfogadott végállapotok: 5+1 (az északi végszék alkalmi pótszék), 3+3 180 × 90-es asztallal (a 05.3 felé 0,65–0,70 m), bővíthető asztal alaphelyzetben öt hellyel. Írd le, melyik esettel számolsz.
- **Koordinátát nem találsz ki:** falazonosítóval és szavakkal megadott, méretezett elhelyezési szándékot adsz; a koordinátát Claude rendeli hozzá.

**VB.3 Kamerák és fény** (GEOMETRIA v2 3. pont; Péter 2026-10-25 04:40/04:49)
- **Cam_02 nappali–terasz** – [8,30; 4,40; 1,55], északnyugat felé, 20 mm – **KÉK ÓRA / KORA ESTE, prémium rétegzett Philips Hue, 2200–2700 K, RGB nélkül.** A TV-fal a kép fő WOW-eleme: a rejtett LED-ek és a textúrák itt érvényesülnek. Balra a W01 TV-fal, középen az ülőcsoport, jobbra az üvegfal, a terasz és a valódi panoráma, a jobb alsó sarokban az étkező nyugati hosszoldala, a felső szélen az ML05. Közepes expozíció, nem sötét és nem kontrasztos: nincs bebukó fekete és kiégett fény; a falélek, a nyílások, a padló–fal vonal, a teraszburkolat, a korlát és a zöldtető olvasható marad, így a nézet geometriai kontrollként is működik; a LED profilból, egyenletesen világít (nem pontsoros); fény csak a megnevezett lámpatestekből jön.
- **Cam_12 nappali hero v3** – [4,40; 7,88; 1,60], θ −48° (délkelet felé), vízszintes, 22 mm, shift_y −0,05 – **NAPPAL, természetes, világos luxusenteriőr-fotó** (a Hue visszafogott vagy kikapcsolt). Előtérben a kanapé eleje (a kép kb. 16–23 %-a), az étkező az ML04 függesztékkel, a konyha, a W03 a 05.3 szürke ajtóval, a W02 mint fő felület, a W07 a jobb szélen; a TV-fal és a terasz nem látszik. Ez a közös hero- és összehasonlító nézet.
- **Cam_03 K1 konyha–étkező** – [9,45; 7,55; 1,50], dél felé, vízszintes, 20 mm, shift_y −0,08 – **NAPPAL.** A konyha a kép tárgya: a két pultsor frontja, munkalapja és hátfala, a hűtőoszlop (D13), a déli magas elemfal; jobb előtérben az étkező és az ML04 lámpateste; a terasz és a TV-fal nem látszik.
- **Cam_04 master** – [0,35; 4,30; 1,50], északkelet felé, 20 mm – **ESTE, Hue-jelenet** (fejvégfény, olvasólámpák). A keleti fejvégfal az ággyal (180 × 200, tengely y 6,40), az északi fülke teljes, mennyezetig érő gardróbfala (3,00 × 0,90 × 2,90 m, a front a pillér síkjában; kötelező), az éjjelik; a déli 2,42 m-es gardróbsáv ugyanabban a frontcsaládban.
- **Cam_11 master panoráma** – [3,20; 6,10; 1,20], nyugat felé, 20 mm, ülő szemmagasság az ágyon – **NAPPAL.** A 3,64 m-es nyugati üvegfal három fehér keretes mezővel, az erkély és a valódi kilátás (városi tetők, templomtorony, budai hegyek); az ágy lábvége, jobb szélen az északi gardróbfal, bal szélen a déli gardróbsáv; a fejvég a kamera mögött van.
- **Cam_10 fürdő 06.2** – [14,50; 6,62; 1,50], kelet felé, 16 mm – **CSAK MŰFÉNY** (ablaktalan), a meglévő pontokról. A beépített burkolat (Geostone Grigio, Esagonetta dekor a zuhany hátfalán), a walk-in zuhany üvegfal nélkül, a fekete Grohe szerelvények, a Geberit mosdó és WC maradnak; csak tükör-, tároló-, lámpatest-, textil- és kiegészítő-réteg adható hozzá.
- A kamerák geometriája és a kep_id-k változatlanok; a semleges Blender-alapképek a geometriai kontroll; a végleges FRAME LAYOUT-ot Claude adja – a kompozíciót a látható elemek hierarchiájaként írd le, kameraértéket ne találj ki.
- **A Cam_12 v3 nem kreatív korlát:** x 4,40-en áll, a TV-falat (x ≤ 4,27) egyáltalán nem látja, ezért a TV-fal – az északi vége is – szabadon tervezhető, mennyezetig érő szekrénnyel is. Csak a kamera állóhelyét (x 4,30–4,50; y 7,75–8,05) hagyd szabadon. Ha a terved más nézőpontot kíván (pl. kerek asztal miatt nyugatabbra tolt kanapé, magas elem a kép előterében), írd le: Claude második hero kamerát vizsgál, és megmutatja a kompromisszumot – az enteriőrt a kép kedvéért nem butítjuk le, ilyenkor a kamerát vizsgáljuk újra.
- **Nézetek közötti azonosság:** a Cam_02, a Cam_12 és a Cam_03 ugyanazt az egyetlen nappali–étkező–konyha tervet mutatja – azonos bútorral, anyaggal, falkezeléssel és lámpatesttel, csak a fény más; a Cam_04 és a Cam_11 ugyanazt a master hálót. Ugyanaz a termék minden nézetben ugyanazzal a névvel, mérettel és színnel szerepel.
- A hat közös kalibráció ugyanezt a fényt követi (Cam_02 kék óra, Cam_04 este, Cam_11 nappal).

**VB.4 Beszerzési források és anyagszabály** (GOAL §4–5, CLAUDE.md)
- **Látszó darabok** (kanapé, asztal, szék, ágy, fotel, tükör, lámpa): Kave Home vagy Westwing; más márka csak ellenőrizhető magyar árral, szállítással és termékoldallal. **Vázak** (PAX, METOD, BESTÅ): IKEA. **Forma-darab** (lakásonként 1–3): gazdaságos egyedi asztalosmunka az anyagszabály szerint – matt vagy strukturált laminált bútorlap (Egger H1180 / H3710 / F274 család), bordázott MDF, ívekhez hajlított MDF; furnér legfeljebb egy felületen; nincs tömörfa, kő és festett front (festett MDF csak külön indoklással és Péter jóváhagyásával; BiBo: navy laminált az alap); a belső mindig fehér.
- **Dekoranyag** (kőfurnér, kőhatású panel, textúrás tapéta, kárpitpanel, nyomott grafika) őszintén megnevezve: a kőhatású panel nem „travertin”, a laminált nem „márvány”.
- **Nincs építés:** a falak fehérek maradnak, ahol nincs kijelölt, beárazott felületkezelés; nincs bontás, gipszkarton, álmennyezet, új burkolat.
- **Minden látható termékhez:** gyártó, terméknév/cikkszám, méret, bruttó ár, forrás (link), dátum, státusz (ellenőrzött / becslés). Bútorméret csak valós termékadatból; ismeretlen méret = ismeretlen, nem találod ki.

**VB.5 Képszám és kalibráció** (Péter 04:03 és 04:27)
- Versenyzőnként **60 SAJÁT kreatív prompt** (10 stílus × 6 kamera) **+ 6 KÖZÖS kalibrációs prompt = 66 képes készlet.** A három versenyző összesen 180 saját promptot készít.
- A hat kalibrációt (C1 Zenit, C2 Lake Forest × Cam_02/Cam_04/Cam_11; regiszter 61–66. sor) Claude egyszer elkészítette (`05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/`): nem te írod, nem módosítod, C1/C2 stílusspecifikációt sem készítesz; mindhárom versenyző ugyanazt a mércét kapja.
- A 66 soros manifested teljes marad: az 1–60. sor a saját promptod (PENDING / DRAFT / COMPLETE); a 61–66. sor `statusz` = KOZOS, `fajl` = a közös promptfájl útvonala, `validalas` = NEEDS_CLAUDE_VALIDATION, `megjegyzes` = „közös kalibráció, nem a versenyző munkája”.
- Az S06 Zenit Atelier és az S07 Lake Forest Couture ettől függetlenül teljes, önálló stílus.

**VB.6 Költség – közös alap és kapu** (KOZOS_FIX_ALAP_v1)
- **18,00 M Ft bruttó tervezhető = 8,40 M közös fix + 9,60 M stílusfüggő.** A 2,00 M tartalék érintetlen. A kb. 1 M Ft-os minőségi többlet legfeljebb külön, feltételes információként mutatható; a versenyben a ≤ 18,00 M-os változat számít.
- **A 8,40 M közös fix** (tervezés 0,40; konyhagépek 1,10; mosogató és bekötés 0,30; 05.2 háló 0,80; 05.3 háló 0,80; előtér és közlekedő 0,50; mosó-szárító 0,45; terasz 3,60; szállítás és szerelés 0,45) **versenyfeltételezés, nem igazolt kivitelezési ár:** a tervben egy sorban, változatlanul átveszed; a végső költségkapun ezt is ellenőrizzük, különösen a teraszt, a szállítást/szerelést és a tervezést.
- **A 9,60 M stílusfüggő keretet** tervezed és árazod tételesen, a KOZOS_FIX_ALAP_v1 soraiban: 02a konyhabútor; 03a TV-fal és kísérőfalak panelei; 03b kanapé; 03c fotel, asztalok, puff; 03d étkező; 03e szőnyeg; 03f függöny és sín; 04a ágy és matrac; 04b fejvégfal; 04c gardróbfal; 04d éjjelik, olvasólámpák, függöny, textil; 07 fürdő-kiegészítők; 10 világítás (Hue); 11 falfelületek; 12 textil, dekor, művészet, styling. A célértékek tájékoztatók, a sorok között szabadon átcsoportosíthatsz; a 9,60 M plafon nem. Fő és gazdaságos változat; a kiváltott korábbi tételek levonása.
- **A saját becslésed tájékoztató.** A 18,00 M-os beférésről a független keresztellenőrzés dönt: A (GPT-6 Astra) tervét Claude, B (Claude Fable 5.1) tervét GPT-6 Chat, C (Claude Opus 5.5) tervét Astra vagy GPT-6 ellenőrzi – azonos módszerrel, azonos fix alappal, dátumozott árakkal. Hiányzó vagy árazatlan szükséges tételt az ellenőrző konzervatív benchmark-árral pótol és jelöl: ez korrekció, nem kizárás – az alulárazás tehát nem előny, a teljesség igen.
- **A kapu:** a győztes teljes, keresztellenőrzött bruttó bekerülése (fix + stílusfüggő) legfeljebb 18,00 M, a tartalék érintetlen. Ha a beférés érdekében gazdaságosabb változat kell, annak a látványát értékeljük.

**VB.7 Hue** (HUE_ALAPCSOMAG_v1)
- Minden általános és dekoratív fény Philips Hue-jelenetben működik; kivétel a szekrénybelső, tisztán funkcionális fény. Lámpatest csak E27 / E14 / GU10 foglalattal, amelybe a Hue-izzó fizikailag befér, vagy Hue-gyári lámpatest, vagy Hue-szalag; G9, G4 és integrált nem-Hue LED nem. Ne tekints automatikusan minden 24 V-os szalagot Hue-kompatibilisnek.
- Rejtett vonalfény: Hue Lightstrip Plus (vagy Gradient, ahol a színátmenet látványelem; a jelenetekben RGB nélkül), alumínium profilban, opál fedéllel; a szalag és a LED-pont nem látszik. Táp meglévő dugaljról (D-azonosítóval); ahol nem igazolt: „FELTÉTELES – CLAUDE VILLAMOS AUDIT SZÜKSÉGES”.
- Minden fényvonalhoz és lámpatesthez: hely (fal-/elem-ID), hossz vagy darab, Hue-termék, táp- és kiállás-azonosító, profil és diffúzor, rögzítés (asztalos horony vagy felületi), kábelút, anyag + szerelés bruttó; a Bridge és a vezérlők a 10-es sorban. Enélkül a világítás tétele „nem igazolt”, és az ellenőrző a HUE_ALAPCSOMAG tájékoztató sávjának felső értékével pótolja.

**VB.8 Validátor-státusz**
- A lakás nem teljes egészében validált. A kameracsomag validátora PASS, de a régi 6 szaniterhiba (06.1/06.2) és a TV-fal elektromos figyelmeztetései (D16, D17, D18, G01–G04, G08) a külön hibanyilvántartásban élnek. A TV-csatlakozók tényleges helye, a parketta pontos dekorja (NEM IGAZOLT), a káva mélysége, a teraszajtó nyíló szárnya és a fürdő szanitereinek mérete hétfőn (2026-10-26) a helyszínen ellenőrizendő. Ezeket a terved kockázatként jelöli, nem igazoltként.

**VB.9 Képek és bírálat**
- A kész promptokból a koncepcióképeket Claude egyesével, Chrome-ból, ChatGPT Images-szel készíti, a kamera semleges Blender-alapképével és a helyszíni referenciákkal, „KONCEPCIÓ – NEM VALIDÁLT” státusszal: előbb minden stílus Cam_12-je (nappal), majd Cam_02-je (kék óra), utána a többi nézet. Te képet nem generálsz.
- A kapuk kizáró feltételek, nem kompenzálható pontszámok: (1) geometria és használhatóság valós Blender-geometriában; (2) műszaki kivitelezhetőség – rögzítés, villamos kiállás, Hue, mennyezeti hűtő-fűtő, anyagok; (3) keresztellenőrzött teljes bekerülés ≤ 18,00 M, tartalék érintetlen; (4) renderhűség – az összehasonlító képek a jóváhagyott, mérethű tervet ábrázolják. A végső összehasonlító képek csak a kapukon átjutó terveknél készülnek újra, azonos képgenerátorral, Blender-kamerákkal és helyszíni referenciákkal. Ha az audit a koncepciót érdemben módosítja, a módosított változatot ellenőrizzük és értékeljük újra.
- A megfelelt tervek közül Péter választ, a látvány alapján: a legjobb összhatás, enteriőrminőség és WOW-élmény nyer – nem a prompt hossza, nem a modell neve. Az integrációtól kezdve a csomagok kódnevet kapnak (X/Y/Z).
- Ne értékeld magadat győztesnek, ne írj a másik két versenyzőről. Az ő V3.1-munkájukat nem olvasod, nem használod, nem módosítod; a draft PR-ek a repóban láthatók – a tilalom önkéntes fegyelem, a bírálat kódneves.

**VB.10 Mentés, megszakítás, folytatás**
- Mentésnek csak a távoli GitHubon visszaolvasott commit számít; minden checkpoint után írd be a commit SHA-t és a visszaolvasás eredményét a `00_CHECKPOINT_NAPLO.md`-be.
- Ha a push vagy a GitHub-írás akad, azonnal jelezd, és ne folytass hosszú, mentés nélküli munkát. Végső tartalék: a kész fájlokat egyetlen csomagban, fájlonként a teljes útvonallal átadod a chatben, és Claude Péter jóváhagyásával változtatás nélkül committálja a saját ágadra.
- Ha induláskor a saját ágad már létezik: ne írd felül és ne töröld. Olvasd vissza a `00_CHECKPOINT_NAPLO.md`-t és a `01_MANIFEST_66.csv`-t; ha az egyértelműen a te korábbi futásod ugyanebből a baseline-commitból, folytasd; ha nem egyértelmű, állj meg és jelezd.
- Megszakadt futás után (kontextus, keret, GitHub-hiba) új munkamenetben ugyanazon az ágon, ugyanebből a baseline-ból folytatod: a PENDING és DRAFT tételeket készíted el, a COMPLETE tételeket nem írod újra; a saját ágadat nem hozod létre újra, és nem rebase-eled újabb commitra.

---

## 2. A 11 célzott szövegcsere – hol van alkalmazva
A három eredeti prompt (Péter csatolmánya, 03:13) kreatív szövege megmaradt; az alábbi cseréket a törzsszövegben ténylegesen végrehajtottam (nem csak a VB blokk írja felül).

| # | Csere | A – Astra | B – Fable | C – Opus |
|---|---|---|---|---|
| 1 | forráscommit `45d1e4d` → `45632b5…`; saját ág ebből; a draft PR célága a baseline-ág | fejléc, VB.1, 11. | fejléc, VB.1, Szerep (git), 9. | fejléc, VB.1, Szerep (git), 9. |
| 2 | kalibráció → 60 saját + 6 közös = 66 képes készlet; manifest 61–66 = KOZOS | VB.5, 1., 7., 10., 11., 12. | VB.5, 2., 6., 9., 10. | VB.5, 2., 6., 9., 10., 11. |
| 3 | „a végleges kamera még készül” → Cam_03 K1 | VB.3, 7. | VB.3, 6. | VB.3, 6. |
| 4 | „Claude 2–3 alternatívát készít” → a C alapelrendezés (GEOMETRIA v2), más asztalforma külön méretpróbával | VB.2, 5. | VB.2, 4. | VB.2, 4. |
| 5 | „teljes lakásszintű költségvetés” → 9,60 M stílusfüggő tételesen + 8,40 M fix sor | VB.6, 8. | VB.6, 2., 7. | VB.6, 2., 7. |
| 6 | „árazatlan tétel → nem igazolt” → benchmark-pótlás; a fix alap is ellenőrzött; teljes ≤ 18,00 M | VB.6, 8., 9. | VB.6, 5., 7. | VB.6, 5., 7. |
| 7 | fény: Cam_02 kék óra / Hue TV-fal, Cam_12 nappal, Cam_03 nappal, Cam_04 este, Cam_11 nappal, Cam_10 műfény | VB.3, 7. | VB.3, 6. | VB.3, 6. |
| 8 | „a rögzített közös commitból indíts” → a baseline-ág rögzített commitjából, PR-célág a baseline-ág | 11. | 9. | 9. |
| 9 | A §2 Work-keret + „ha elfogy, folytatjuk” | 2., VB.10 | – | – |
| 10 | A §11 ágnév | fejléc, házirend-eltérések, 11. – **új név:** `competition/gpt6astra-v3-1-20261025` (lásd lent) | – | – |
| 11 | „a draft PR-ek láthatók; önkéntes fegyelem; kódneves bírálat” | 1. (a szimmetria miatt A-ban is), VB.9 | 1., VB.9 | 1., VB.9 |

**A 10. csere eltér az eredeti javaslattól:** az eredeti A-ág (`astra/creative-upgrade-v3-1-r1-20261025`), mappa (`05_promptok/KEP004_ASTRA_V3_1_r1/`) és PR-jelölő (`WSG-ASTRA-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1`) megegyezik a 2026-10-25 02:52-kor indított, nem verseny Astra V3.1 feladatéval és az r2 C részének folytató üzenetével. Hogy egy esetleg még élő Work-futással ne keveredjen, a versenyző A a B/C mintájára kapott nevet: ág `competition/gpt6astra-v3-1-20261025`, mappa `05_promptok/KEP004_GPT6ASTRA_V3_1_r1/`, összefoglaló `ai-coordination/results/WSG-20261025-GPT6ASTRA-CREATIVE-UPGRADE-V3_1_r1.md`, jelölő `WSG-COMPETITION-RESULT: GPT6ASTRA-V3_1`. A „brief r2, kimenet r1” megjegyzés a README első sorában megmaradt.

**További, mindhárom promptban azonos kiegészítések** (az eredeti promptokból hiányoztak, a preflight és Péter döntései alapján):
- házirend-felülírás: Astránál az `OPENAI_instructions.md`/`HANDOFF_PROTOCOL.md` „friss main / main-re írás / PR nélkül / P902_24A” szabálya, Fable-nél és Opusnál a `CLAUDE.md` „operatív vezető, Blender, main-re írás” szerepe erre a feladatra nem érvényes;
- a kanapé L/U szabálya, a Kave Home/Westwing/IKEA/asztalos források és az anyagszabály (VB.2, VB.4);
- az elavult anyagok listája és az r2 felülírt fejezetei (VB.1);
- a validátor-státusz (VB.8);
- az összefoglaló kötelező fejléce (bázis-commit, státusz) és a stílusonkénti asztal-/teraszajtó-eset megadása.

## 3. Keresztellenőrzés beosztása (Péter, 04:03)
| Versenyző | Saját költség | Keresztellenőrző | Módszer |
|---|---|---|---|
| A – GPT-6 Astra | tájékoztató | **Claude** | azonos fix alap, dátumozott webshop-árak, benchmark-pótlás |
| B – Claude Fable 5.1 | tájékoztató | **GPT-6 Chat** | ua. |
| C – Claude Opus 5.5 | tájékoztató | **Astra vagy GPT-6** (nem Claude) | ua. |

A geometriai kaput mindhárom tervnél Claude futtatja (validátor + Render Reality Gate), kódnevekkel, szkripttel; az eredmény fájlban. A 8,40 M fix alap a végső kapun ugyanúgy ellenőrzött tétel (terasz 3,60, szállítás/szerelés 0,45, tervezés 0,40, gépek 1,10).

## 4. Mi nem változott
A három prompt szerkezete és kreatív tartalma, a 10 stílus, az S01/S02 három TV-fal-koncepciója, a 66 soros regiszter, a §11.12 fájlszerkezet (saját névtérben), a checkpoint-rend, a tiltások (nincs kép, Blender, merge, rendelés).

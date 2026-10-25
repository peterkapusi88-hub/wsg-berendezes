# WSG DESIGN CHALLENGE 2026
## CONTESTANT B — CLAUDE FABLE 5.1 · HIGH
### INDEPENDENT LUXURY INTERIOR DESIGN · 10 CONCEPTS · 60 OWN FULL PROMPTS + 6 COMMON CALIBRATIONS = 66-IMAGE SET

- **Repository:** `peterkapusi88-hub/wsg-berendezes`
- **Közös, rögzített versenykiindulás (baseline v3):** ág `competition/baseline-20261025-v3`, commit `45632b5ad5586e1f3f884a8f723c1cc13cda6da3`
- **Saját kimeneti ág (ebből a commitból):** `competition/fable51-v3-1-20261025`
- **Draft PR célága:** `competition/baseline-20261025-v3`
- **Saját eredménykönyvtár:** `05_promptok/KEP004_FABLE51_V3_1_r1/`
- **Saját összefoglaló:** `ai-coordination/results/WSG-20261025-FABLE51-CREATIVE-UPGRADE-V3_1_r1.md`
- **PR-jelölő:** `WSG-COMPETITION-RESULT: FABLE51-V3_1`
- **Elsődleges szakmai dokumentum:** `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md` – ahol eltér, az alábbi VB blokk érvényes.
- **Üzemmód:** Claude Fable 5.1, High effort – új, önálló Claude-munkamenet.

---

## VB – KÖZÖS VERSENYBLOKK (§0 v3.1, végleges, 2026-10-25) – mindhárom versenyzőnek szó szerint azonos

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

## SZEREPED EBBEN A MUNKAMENETBEN
Ebben a munkamenetben kizárólag a B versenyző kreatív belsőépítészi szerepét töltöd be, Péter kifejezett utasítására. A `CLAUDE.md`, a `MUNKAMENET.md` és a Claude Project-instrukciók szerepleírása – operatív projektvezető, Blender-/MCP-vezérlő, integrátor, független költségauditor, „a kreatív feladatot átadja Astrának”, döntésfrissítés közvetlenül a main-re, „minden munka előtt a friss main” – erre a munkamenetre nem vonatkozik.

Ebben a munkamenetben:
- Blendert és a Blender-MCP-t nem használod;
- a main-re, a GOAL.md-be és a közös fájlokba nem írsz;
- más PR-t nem kezelsz, más AI-t nem indítasz;
- képet nem generálsz (ChatGPT Images, Gemini, MeltFlex sem).

Péter belsőépítészeti skilljeit (westside-berendezes, wsg-ertekalapu-stiluslabor, interior-design-expert, interior-design, product-research, color-palette-generator, ffe-spec-book, product-cut-sheet) szöveges tervezésre és termékkutatásra használhatod; a képet vagy videót készítő meltflex- és portfolio-skilleket nem futtatod.

**Git-indítás (Claude-munkamenet):**
```
git fetch origin competition/baseline-20261025-v3
git ls-remote --heads origin competition/fable51-v3-1-20261025      # üres kell legyen – ha nem: VB.10
git checkout -b competition/fable51-v3-1-20261025 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
git rev-parse HEAD                                                  # = 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
# … CP0-fájlok, commit …
git push -u origin competition/fable51-v3-1-20261025
git ls-remote --heads origin competition/fable51-v3-1-20261025      # távoli visszaolvasás
```
A draft PR-t a GitHub REST API-val nyisd (`POST repos/peterkapusi88-hub/wsg-berendezes/pulls`, `base=competition/baseline-20261025-v3`, `draft=true`); a GraphQL ebből a környezetből nem érhető el. A saját ágadat nem rebase-eled és nem merge-eled másra.

## 1. FÜGGETLEN KREATÍV VERSENY
Te vagy a B versenyző. A GPT-6 Astra (A) és a Claude Opus 5.5 (C) ugyanebből a rögzített baseline-ból külön terveket készít.

Ne olvasd a másik két versenyző új V3.1 terveit, promptjait, manifestjeit vagy draft PR-jeit. Ne módosítsd a fájljaikat. A draft PR-ek a repóban láthatók: a tilalom önkéntes fegyelem, a bírálat kódneves (VB.9).

A verseny előtti közös Astra V2/V3 tervek, a PR #16, a baseline-ba beemelt PR #20 kameracsomag (benne a PR #17 és #18 tartalma), a valós lakás geometriája és a Zenit/Lake Forest benchmarkok viszont mindhárom versenyző számára közös kiindulási anyagok.

Olvasd célzottan (a baseline-commitban): a VB.1 közös fájljait – különösen a `GEOMETRIA_C_KAMERACSOMAG_v2.md`-t, a `KOZOS_FIX_ALAP_v1`-et és a `HUE_ALAPCSOMAG_v1`-et –, a végleges r2 briefet, a 66 képes regisztert, a releváns V2/V3 stílusalapot (a PR #16 ága: `astra/creative-upgrade-v3-r1-20261025`, csak olvasásra), a V3.1 Cam_12/fal/világítási bemenetet (a falazonosítók, a W02+W07 összekötő fal és a kiállás-mátrix érvényes; a kamera- és fényadatokat a VB.3 felülírja), a Cam_10/Cam_11 kamerablokkokat és a GOAL.md releváns tulajdonosi javításait, a VB.1 elavult-listája szerint. Csak konkrét szükség esetén nyiss további nagy dokumentumokat.

Elsőbbségi sorrend: (1) a VB blokk; (2) ez az indítószöveg; (3) az r2 brief – azon belül a 11.0, majd a 11. és a 0. fejezete (WOW-diagnózis) a brief többi része előtt; (4) a GOAL.md és a repó többi dokumentuma. A brief eredetileg GPT-6 Astrának készült: a hárommodelles versenyben az összes kreatív, geometriai, pénzügyi, Hue-, kamera-, kimeneti és checkpoint-követelményt önálló tervezőként neked kell teljesítened. A korábbi r1 változat elavult.

A győztes kiválasztásának elve: az a koncepció nyer, amelyik a legjobban néz ki, miközben igazoltan belefér a valódi lakásba és a teljes bruttó 18 M Ft-os keretbe. Az irreális látvány vagy a keresztellenőrzésen elbukó ár nem elfogadható versenyeredmény.

## 2. KÖTELEZŐ TELJES KIMENET
Készíts egyetlen összefüggő munkában:
1. Tíz teljes, önálló, karakteresen eltérő luxus-belsőépítészeti stílustervet: S01 Kyoto Ink, S02 BiBo Nocturne, S03 Alelí Casa, S04 LA Horizon, S05 Miami Streamline, S06 Zenit Atelier, S07 Lake Forest Couture, S08 Milano Radical, S09 Paris Collector, S10 Desert Modern 70.
2. S01 és S02 számára három-három valóban eltérő, kidolgozott TV-fal-koncepciót, egy-egy javasolt főváltozattal (a promptok a főváltozatot mutatják); S03–S10-hez stílusonként egy kidolgozott TV-fal-koncepciót.
3. Pontosan 60 önálló angol kreatív renderpromptot: tíz stílus × hat kamera. A C1 Zenit és C2 Lake Forest hat kalibrációs promptja közös, Claude készítette – azt nem te írod. 60 saját + 6 közös = 66 képes készlet (VB.5).
4. A nappali–étkező–konyha, master és fürdő teljes, helyiségenként egységes tervét.
5. Méretezett, falazonosítós elemlistát, anyag- és termékjavaslatokkal (gyártó, cikkszám, ár, forrás, dátum), rögzítéssel, elektromos feltételekkel.
6. Philips Hue-kompatibilis világítási koncepciót, táp-, kábel-, vezérlési és költségfeltételekkel (VB.7).
7. Fő és gazdaságos gyártási alternatívát, a 9,60 M-os stílusfüggő keret tételes költségvetését a 8,40 M közös fix sorral és a lakásszintű végösszeggel (VB.6), a kiváltott régi tételeket.
8. A későbbi független Blender-ellenőrzéshez és képgeneráláshoz pontos átadási dokumentációt.

Mind a 60 prompt a közös regiszter kep_id mezőjét betű szerint használja (a regiszter 1–60. sora). Legyen minden prompt különálló, teljes angol szöveg, önálló stílus-, helyiség-, kamera-, bútor-, anyag-, fal-, a VB.3 szerinti világítási és reality-leírással. Nem elfogadható a „same as above”, „see previous”, TBD vagy a hiányos sablon.

A négy kiemelt S01/S02 Cam_02/Cam_12 prompt különösen részletes legyen (irányérték: kb. 5–7 ezer karakter); a többi 56 szintén teljes értékű (kb. 3–5 ezer karakter). A minőség fontosabb a mechanikus karakterszámnál. Pozitív, leíró nyelv; képenként legfeljebb kb. 8 tiltás, a bizonyított hibákra (r2 §11.9).

## 3. WOW-MINŐSÉG ÉS TELJES ENTERIŐR
A cél a korábbi Zenit és Lake Forest képekhez mérhető vagy azokat meghaladó luxusérzet, a tényleges A-902 geometriájában.

Ne csak a TV mögé tervezz dekorációt. A teljes enteriőr legyen tudatosan megalkotott luxus-belsőépítészeti rendszer.

Kiemelt tervezési felületek:
- W01 teljes TV- és tárolófal;
- W02/W07 összekötő fal, egyetlen átfogó kompozícióként;
- az étkező fala, a konyha és a 05.3 szürke ajtó környezete;
- a nappali homlokzati tömör mezők;
- master fejvégfal, északi gardróbfal és déli gardróbsáv;
- fürdő 06.2 meglévő burkolatával összeegyeztethető kiegészítők, tükör és fények.

Minden jelentős látható tömör falnak legyen a képen is értelmezhető terve. Nem kell minden falat végigburkolni, de az esetleg nyugodtabb fal is tervezett felület legyen, ne véletlenül üres fehér háttér.

Tervezhetsz aszimmetrikus, monumentális, rétegzett, teljes magasságú, gazdaságosan gyártható TV-falakat és tárolófrontokat; különleges tapétát, dekor MDF-et, grafikát, vásznat, textileket és indirekt fényeket.

A tíz stílusnak legyen saját formavilága, művészeti karaktere, bútorlogikája és fénykompozíciója. Ne legyen tíz ugyanolyan lamellás vagy téglalap alakú TV-háttér eltérő színekkel.

A teljes, elegáns styling a terv része, amennyiben elfér: függöny, szőnyeg, párna, pléd, álló- vagy asztali lámpa, dohányzóasztal/puff, kiegészítők, nagy művészeti elemek.

## 4. BLENDER – A VALÓS ÉPÍTÉSZET RÖGZÍTETT, A BERENDEZÉS KREATÍVAN SZABAD
Változatlan:
- valós falak és nyílások;
- 2,90 m-es modellezett belmagasság;
- meglévő padló és fehér mennyezet;
- szürke belső ajtók, fehér belső ablakkeretek;
- terasz WPC- és burkolati adottságai, növényzete, korlátja, valódi panorámája;
- meglévő és csak terv szerint azonosított villamos pontok;
- mennyezeti hűtő-fűtő rendszer;
- fürdő 06.2 rögzített beépített állapota.

A mennyezeti hűtő-fűtő mezőbe nem fúrunk. Új nyílás, fiktív lámpakiállás, hamis panoráma, álmennyezet vagy irreális térnövelés nem megengedett.

A régi V3 Blender-bútortömbök nem kötött formák. A bútor-, panel-, tároló- és falrendszert újratervezheted.

Minden új elemhez adj (r2 §11.7):
- stabil ID és fal/helyiség-azonosító;
- elhelyezési szándék;
- szélesség × magasság × mélység;
- termék (gyártó, cikkszám, link, dátum) vagy anyag, gyártás, szerelés;
- rögzítés és szükséges villamos betáplálás (melyik meglévő pontról);
- fő/gazdaságos bruttó bekerülés;
- becsült vagy ellenőrzött státusz.

Az alaprajzi alap a jóváhagyott C elrendezés (VB.2): a kanapé minimum L, inkább U, háttal keletre, az étkező felé, nyitott a TV-fal felé; az étkező alapváltozata a 160 × 90-es hosszanti asztal az ML04 alatt, hat hellyel. Kerek, ovális vagy bővíthető asztalt kreatív alternatívaként javasolhatsz, külön Blender-méretpróbára. A TV-falon legfeljebb 60 cm mély zárt szekrénytest lehetséges, nem kötelező; a Cam_12 kamera nem korlátozza a TV-falat (VB.3). Adj kreatív, méretezett szándékot, de ne találj ki ellenőrizetlen Blender-koordinátát.

## 5. KÖTELEZŐ FÜGGETLEN BLENDER-UTÓELLENŐRZÉS
A kreatív munka csak akkor kerülhet a győztesjelöltek közé, ha a későbbi Render Reality Gate ellenőrzéseken megfelel.

A munkád elkészülte után a külön Claude műszaki integrátor:
1. A terveid alapján valós Blender-koordinátákat és új, mérethű bútortömböket készít.
2. Ellenőrzi a valódi geometriát, közlekedést, székmozgatást, ajtónyitást, konyhai és master-használhatóságot.
3. Vizsgálja a falpanelek, szekrények, világítások és rögzítések valós elférését.
4. Ellenőrzi a villamos pontokat és a mennyezeti hűtő-fűtő rendszer sértetlenségét.
5. A műszaki tételeket (szerelés, Hue, asztalos-előkészítés) a költségtervhez rendeli; a teljes bruttó bekerülést a független keresztellenőrzés igazolja – a B tervét GPT-6 Chat ellenőrzi (VB.6).
6. Az eltéréseket dokumentálja.
7. Szükség esetén azonos látványértékű, méretezett módosításokat javasol; ha az ötletet a kamera nem mutatja jól, a kamerát vizsgálja újra (VB.3).
8. Csak a geometriailag és költségileg megfelelő változatból készít végleges ChatGPT Images-csomagot; a koncepcióképek ettől függetlenül a kész promptjaidból készülnek (VB.9).

Az integrátor nem butíthatja vissza automatikusan a kreatív koncepciót a korábbi V3 bútortömbökre. Ha az eredeti ötlet nem fér el, a lehető legközelebbi látványértékű, használható megoldást kell keresnie. Jelentős vizuális kompromisszumot tulajdonosi döntés nélkül nem fogadhat el.

A később elkészült képek geometriáját is ellenőrizni kell a Blender-kontrollképek ellenében.

Jelen feladatodban ne módosíts Blendert és ne generálj képeket. Most a méretezett, auditálható kreatív terveket és a 60 saját promptot készítsd el.

## 6. EGYSÉGES KAMERÁK ÉS FÉNYEK
Pontos adatok és kompozíció: VB.3.
- **Cam_02:** nappali, TV-fal, terasz; kék óra / kora este, prémium rétegzett Hue, 2200–2700 K, RGB nélkül; a TV-fal a fő WOW-elem; közepes expozíció, a terasz és a geometria olvasható marad (kontrollnézet).
- **Cam_12 v3:** nappali hero, étkező, konyha, W02/W07, a W03 a 05.3 ajtóval; nappali, természetes, világos luxusenteriőr-fény.
- **Cam_03 K1:** konyhaorientált konyha–étkező, nappali fény.
- **Cam_04:** master, esti Hue-hangulat.
- **Cam_11:** ugyanaz a master, nappali panorámás geometriai kontroll.
- **Cam_10:** fürdő 06.2, csak műfény.

A közös C1/C2 kalibrációk (Cam_02, Cam_04, Cam_11; nem a te feladatod) ugyanezt a fényrendszert követik.

A kapcsolódó kamerák egyetlen közös helyiségtervet mutassanak, ugyanazzal a bútorral, anyaggal, falszerkezettel és fényforrással.

Az általános és dekoratív világítás Hue-rendszerben működjön; a szekrények tisztán funkcionális belső fénye kivétel. A Hue-kompatibilitáshoz konkrét rendszer, profil, vezérlés, tápegység, kábelút és költség kell, nem általános kijelentés (VB.7).

## 7. KÖLTSÉG – KÖTELEZŐ GYŐZTES-FELTÉTEL
A teljes A-902 elkölthető berendezési kerete 18 000 000 Ft bruttó. A további 2 000 000 Ft tartalék érintetlen.

A teljes lakás, konyhabútor, gépek, tárolók, világítás, kiegészítők, falak, textilek, fürdő, terasz, szállítás, szerelés és szükséges járulékos költségek mind beleszámítanak.

A közös költségalap (VB.6, `KOZOS_FIX_ALAP_v1`): a 8,40 M közös fix részt egy sorban, változatlanul átveszed; a 9,60 M stílusfüggő keretet tételesen tervezed és árazod.

Stílusonként add meg: a stílusfüggő rész tételes fő és gazdaságos változatát; a lakásszintű végösszeget (fix + stílusfüggő); a korábbi tervből kiváltott tételeket; a LED/Hue teljes szerelési költségét a `HUE_ALAPCSOMAG_v1` szerint; a nem ellenőrzött árakat és kivitelezési feltételeket külön jelölve; a túllépési kockázatot.

Győztes nem lehet olyan terv, amelynek független keresztellenőrzés után – a B tervét GPT-6 Chat ellenőrzi – az összes szükséges bruttó költsége (fix + stílusfüggő) meghaladja a 18 M Ft-ot. Árazatlan szükséges tételt a keresztellenőrző konzervatív benchmark-árral pótol és jelöl; törekedj a teljességre, mert a pótlás konzervatív. A 8,40 M fix alap versenyfeltételezés; a végső kapun ezt is ellenőrizzük.

Ha gazdaságos alternatívával lesz megfelelő a terv, az alternatíva tényleges látványát kell a versenyben értékelni, nem az eredeti, drágább és nem kivitelezhető változatot.

## 8. A VERSENY DÖNTÉSI PROTOKOLLJA
A három kreatív terv egyforma független műszaki, költség- és Blender-ellenőrzésen megy át. A kapuk (VB.9) kizáró feltételek, nem kompenzálható pontszámok.

A kész promptokból koncepcióképek már a kapuk előtt készülnek (VB.9). A jóváhagyott összehasonlító renderképek csak a teljesített műszaki és pénzügyi feltételek után készülnek, azonos kamerával, forrásreferenciákkal és képgeneráló eszközzel, kódnévvel.

A képi versenyben a legszebb, legkarakteresebb, legjobban megtervezett, ténylegesen megvalósítható belsőépítészeti változat nyerhet; a megfelelt tervek közül Péter választ.

Ne értékeld önmagadat győztesnek, és ne írj versenytársakról feltételezéseket. Az önértékelésed kizárólag a saját terved erősségeire és nyitott kockázataira terjedjen ki.

## 9. SAJÁT GITHUB-ÁG, FÁJLOK, CHECKPOINTOK
Az ágat kizárólag a baseline-ág rögzített commitjából készítsd:

`45632b5ad5586e1f3f884a8f723c1cc13cda6da3` (ág: `competition/baseline-20261025-v3`) → `competition/fable51-v3-1-20261025`

A draft PR célága `competition/baseline-20261025-v3`. Ha az ág már létezik: VB.10.

- Saját eredménykönyvtár: `05_promptok/KEP004_FABLE51_V3_1_r1/`
- Saját összefoglaló: `ai-coordination/results/WSG-20261025-FABLE51-CREATIVE-UPGRADE-V3_1_r1.md`

A brief §11.12 fájlszerkezetét használd saját névtér alatt, a 60+6 szabállyal:
```
05_promptok/KEP004_FABLE51_V3_1_r1/
  00_README.md                    – tartalom, bázis-commit (45632b5…), források; első sorában: „a brief verziója r2, ez a kimenet r1”
  00_CHECKPOINT_NAPLO.md          – checkpointonként: sorszám, idő, tartalom, commit SHA, a távoli ellenőrzés eredménye
  01_MANIFEST_66.csv              – nr;kep_id;stilus;kamera;fajl;statusz;validalas;checkpoint;karakterszam;mintaprompt;megjegyzes
                                    66 sor: 1–60 saját, 61–66 KOZOS
  02_KOZOS_REALITY_FIXED_elvek.md – közös elvek angolul (lásd lent)
  03_KAMERA_KOMPOZICIOK.md        – a hat kamera kompozíciós leírása (VB.3)
  10_STILUS_SPEC/S01_KyotoInk.md … S10_DesertModern70.md – tíz egységes specifikáció (C1/C2 nem kell)
  20_PROMPTOK/<kep_id>.prompt.md  – pontosan 60 fájl, mindegyikben:
                                    === BEGIN PROMPT <kep_id> ===
                                    … a teljes angol prompt …
                                    === END PROMPT <kep_id> ===
  30_TV_FAL_KONCEPCIOK_S01_S02.md – hat S01/S02 TV-falalternatíva
  40_ELEMLISTA_V3_1.csv           – méretezett elemlista (r2 §11.7)
  50_KOLTSEG_ES_KOCKAZAT.md       – fix + stílusfüggő, fő/gazdaságos, kiváltott tételek, LED/Hue műszaki-költség kockázati tábla
ai-coordination/results/WSG-20261025-FABLE51-CREATIVE-UPGRADE-V3_1_r1.md – összefoglaló és integrációs átadás
```
A `02_KOZOS_REALITY_FIXED_elvek.md`-be a promptsablon v3.1 §1-éből átveendő a geometria és kamera, a meglévő felületek, az őszinte anyagnevek és a közlekedési méretek; nem átveendő a „Walls and ceilings: painted white” mondat (helyette a stílus falterve, a mennyezet fehér marad) és a „Series A neutral overcast” fényszabály (helyette a VB.3).

Kötelező mentések:

**CP0:** saját ág a baseline-commitból → README, checkpointnapló, 66 soros manifest (1–60 PENDING, 61–66 KOZOS) → commit/push → távoli ellenőrzés → saját draft PR a `competition/baseline-20261025-v3` ágra.

**CP1:** tíz részletes stílusterv, a TV-falak és közös elvek, a kamera-kompozíciók; közben legalább két stílusonként commit, push és távoli visszaolvasás.

**CP2:** az S01/S02 négy prioritásos Cam_02/Cam_12 promptja (külön commitban), majd a további nyolc nézetük (Cam_03, Cam_04, Cam_11, Cam_10) és az S01/S02 elemlistája.

**CP3+:** S03–S10 stílusonként hat prompt, legfeljebb 6–10 új promptonként commit, push és távoli ellenőrzés.

**Záró CP:** 60/60 saját azonosító, fájl, BEGIN/END jelölő, tartalmi teljesség és stílusonkénti következetesség, a 6 KOZOS sor; költség-, műszaki és integrációs dokumentáció. Ha a futás nem ér végig, a PR-ben pontosan sorold fel a nem COMPLETE tételeket.

A manifestben a `statusz`: PENDING, DRAFT, COMPLETE, illetve a 61–66. sorban KOZOS; a `validalas` minden DRAFT, COMPLETE és KOZOS sornál NEEDS_CLAUDE_VALIDATION. A COMPLETE kreatív teljesítést jelent, nem Blender-validálást.

A kész részek minden megszakítás esetén megmaradjanak. Mentés csak ellenőrzött távoli GitHub-commit (VB.10). Hibás GitHub-írásnál azonnal jelezz. Ne ments mindent egyetlen záró commitban, és ne jelölj vázlatot késznek.

A main ágat, a baseline-ágat, a másik két versenyző ágát és a közös eredeti dokumentumokat ne módosítsd.

A draft PR címe: „WSG DC2026 · B · Claude Fable 5.1 – 10 stílus + 60 saját prompt (checkpointolt)”; a leírás első sora:

`WSG-COMPETITION-RESULT: FABLE51-V3_1`

## 10. VÉGSŐ ÁTADÁS
Az összefoglaló első sorai:
```
WSG-COMPETITION-RESULT: FABLE51-V3_1
Versenyző: B – Claude Fable 5.1
Modell és gondolkodási szint: <ahogy a munkamenet igazolja> | nem igazolt
Bázis-commit: 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
Utolsó ellenőrzött commit: <sha>
Státusz: TELJES | RÉSZLEGES | BLOKKOLT
```

Add meg:
- saját draft PR-link;
- ellenőrzött commit;
- a tényleges állapot: 60/60 saját COMPLETE + 6 KOZOS (vagy a hiányzók listája);
- a tíz stílus, a hat S01/S02 TV-falkoncepció és az S03–S10 TV-falai;
- teljes elemlista és bruttó költségbecslés (fix + stílusfüggő);
- kritikus műszaki és pénzügyi kockázatok;
- stílusonként: melyik asztalváltozattal és melyik teraszajtó-esettel számoltál, hol kérsz külön méretpróbát vagy második hero kamerát;
- konkrét Claude Blender-integrációs instrukciók;
- saját koncepciód rövid, tárgyszerű önértékelése.

Ne generálj képeket, ne módosíts Blendert, ne merge-elj PR-t, ne rendelj terméket.

Cél: a lehető legszebb, legegyedibb luxusenteriőr, amely a későbbi független Blender- és költségellenőrzést sikeresen teljesíti, és a 18 M Ft-os valódi, teljes keretben kivitelezhető.

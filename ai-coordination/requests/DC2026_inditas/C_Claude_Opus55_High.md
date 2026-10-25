# WSG DESIGN CHALLENGE 2026
## CONTESTANT C — CLAUDE OPUS 5.5 · HIGH
### INDEPENDENT LUXURY INTERIOR DESIGN · 10 CONCEPTS · 60 OWN COMPLETE PROMPTS + 6 COMMON CALIBRATIONS = 66-IMAGE SET

- **Repository:** `peterkapusi88-hub/wsg-berendezes`
- **Közös, rögzített versenykiindulás (baseline v3):** ág `competition/baseline-20261025-v3`, commit `45632b5ad5586e1f3f884a8f723c1cc13cda6da3`
- **Saját kimeneti ág (ebből a commitból):** `competition/opus55-v3-1-20261025`
- **Draft PR célága:** `competition/baseline-20261025-v3`
- **Saját eredménygyökér:** `05_promptok/KEP004_OPUS55_V3_1_r1/`
- **Saját összefoglaló:** `ai-coordination/results/WSG-20261025-OPUS55-CREATIVE-UPGRADE-V3_1_r1.md`
- **PR-jelölő:** `WSG-COMPETITION-RESULT: OPUS55-V3_1`
- **Végleges szakmai brief:** `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md` – ahol eltér, az alábbi VB blokk érvényes.
- **Üzemmód:** Claude Opus 5.5, High effort – új, önálló Claude-munkamenet.

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
Ebben a munkamenetben kizárólag a C versenyző kreatív belsőépítészi szerepét töltöd be, Péter kifejezett utasítására. A `CLAUDE.md`, a `MUNKAMENET.md` és a Claude Project-instrukciók szerepleírása – operatív projektvezető, Blender-/MCP-vezérlő, integrátor, független költségauditor, „a kreatív feladatot átadja Astrának”, döntésfrissítés közvetlenül a main-re, „minden munka előtt a friss main” – erre a munkamenetre nem vonatkozik.

Ebben a munkamenetben:
- Blendert és a Blender-MCP-t nem használod;
- a main-re, a GOAL.md-be és a közös fájlokba nem írsz;
- más PR-t nem kezelsz, más AI-t nem indítasz;
- képet nem generálsz (ChatGPT Images, Gemini, MeltFlex sem).

Péter belsőépítészeti skilljeit (westside-berendezes, wsg-ertekalapu-stiluslabor, interior-design-expert, interior-design, product-research, color-palette-generator, ffe-spec-book, product-cut-sheet) szöveges tervezésre és termékkutatásra használhatod; a képet vagy videót készítő meltflex- és portfolio-skilleket nem futtatod.

**Git-indítás (Claude-munkamenet):**
```
git fetch origin competition/baseline-20261025-v3
git ls-remote --heads origin competition/opus55-v3-1-20261025       # üres kell legyen – ha nem: VB.10
git checkout -b competition/opus55-v3-1-20261025 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
git rev-parse HEAD                                                  # = 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
# … CP0-fájlok, commit …
git push -u origin competition/opus55-v3-1-20261025
git ls-remote --heads origin competition/opus55-v3-1-20261025       # távoli visszaolvasás
```
A draft PR-t a GitHub REST API-val nyisd (`POST repos/peterkapusi88-hub/wsg-berendezes/pulls`, `base=competition/baseline-20261025-v3`, `draft=true`); a GraphQL ebből a környezetből nem érhető el. A saját ágadat nem rebase-eled és nem merge-eled másra.

## 1. HÁROMMODELL-VERSENY – AZONOS FELTÉTELEK
Te vagy a C versenyző. A GPT-6 Astra (A) és a Claude Fable 5.1 (B) külön versenymunkát készít, ugyanebből a rögzített baseline-ból.

A brief eredetileg GPT-6 Astrának készült, de ebben a feladatban te vagy a teljes jogú, független kreatív vezető. Minden kreatív, műszaki, költség-, kamera-, Hue-, prompt- és checkpoint-követelmény rád is érvényes.

Függetlenül tervezz. Ne olvasd, ne másold és ne módosítsd a másik két versenyző új V3.1 promptjait, stílusleírásait, draft PR-jeit vagy kreatív eredményeit. A draft PR-ek a repóban láthatók: a tilalom önkéntes fegyelem, a bírálat kódneves (VB.9).

A közös, korábbi V2/V3 stílusalap, a PR #16 (ág: `astra/creative-upgrade-v3-r1-20261025`, csak olvasásra) és a baseline-ba beemelt PR #20 kameracsomag (benne a PR #17 és #18 tartalma) minden résztvevőnek rendelkezésre áll. A munka a fenti rögzített commitból induljon, nem a közben változó main ágból.

Célzottan olvasd: a VB.1 közös fájljait – különösen a `GEOMETRIA_C_KAMERACSOMAG_v2.md`-t, a `KOZOS_FIX_ALAP_v1`-et és a `HUE_ALAPCSOMAG_v1`-et –, a végleges r2 briefet, a 66 képes regisztert, a V2/V3 stílus-DNS-t, a V3.1 Cam_12/fal/világítási bemenetet (a falazonosítók, a W02+W07 összekötő fal és a kiállás-mátrix érvényes; a kamera- és fényadatokat a VB.3 felülírja), a Cam_10/Cam_11 kamerablokkokat és a GOAL.md releváns tulajdonosi döntéseit, a VB.1 elavult-listája szerint.

Elsőbbségi sorrend: (1) a VB blokk; (2) ez az indítószöveg; (3) az r2 brief – azon belül a 11.0, majd a 11. és a 0. fejezete (WOW-diagnózis) a brief többi része előtt; (4) a GOAL.md és a repó többi dokumentuma. A korábbi r1 változat elavult.

A verseny lényege: melyik modell hozza létre a legszebb luxusenteriőrt úgy, hogy annak végső megjelenített változata Blenderben fizikailag helyes és a teljes bruttó 18 M Ft-os költségkeretbe ténylegesen belefér?

A puszta látványosság, ha nem megvalósítható, nem elegendő.

## 2. A KÖTELEZŐ TELJES KREATÍV KIMENET
Készíts:
1. Tíz részletes, önálló luxus-belsőépítészeti koncepciót:
   - S01 Kyoto Ink
   - S02 BiBo Nocturne
   - S03 Alelí Casa
   - S04 LA Horizon
   - S05 Miami Streamline
   - S06 Zenit Atelier
   - S07 Lake Forest Couture
   - S08 Milano Radical
   - S09 Paris Collector
   - S10 Desert Modern 70
2. Az S01 és S02 stílushoz három-három valóban különböző, méretezhető TV-fal-koncepciót, egy-egy ajánlott főváltozattal (a promptok a főváltozatot mutatják); S03–S10-hez stílusonként egy kidolgozott TV-fal-koncepciót.
3. Pontosan 60 saját kreatív renderpromptot: minden stílushoz Cam_02, Cam_12, Cam_03, Cam_04, Cam_11 és Cam_10.
4. A hat kalibrációs promptot (C1 Zenit és C2 Lake Forest × Cam_02, Cam_04, Cam_11) NEM te készíted: közös, Claude egyszer megírta; a 60 saját + 6 közös = 66 képes készlet (VB.5).
5. Helyiségenként egységes nappali–étkező–konyha, master és fürdő belsőépítészeti specifikációt.
6. Falazonosítós, méretezett bútor-, panel-, szekrény-, műalkotás-, anyag-, textil-, Hue- és styling-elemlistát.
7. Gazdaságos és fő anyag-/gyártási változatot, a 9,60 M-os stílusfüggő keret tételes bruttó költségvetését a 8,40 M közös fix sorral és a lakásszintű végösszeggel (VB.6), kiváltott tételeket és kockázatokat.
8. Pontos átadást a külön Claude műszaki integrátornak.

Mind a 60 saját promptot a közös regiszter kep_id mezője szerint, betűhíven azonosítsd (a regiszter 1–60. sora).

Minden prompt teljes, önálló angol szöveg legyen: stílus-DNS, helyiségterv, kamera, konkrét bútorok, falak, anyagok, styling, a VB.3 szerinti fény, Hue-fények, rövid reality-szabályok.

Nem elég a nézetek közötti hivatkozás, a hiányos sablon vagy 60 alig eltérő általános szöveg.

A négy kiemelt S01/S02 Cam_02/Cam_12 prompt különösen részletes legyen; irányértéke a brief szerint kb. 5–7 ezer karakter. A többi 56 szintén teljes, irányértéke kb. 3–5 ezer karakter. A minőség fontosabb a mechanikus karakterszámnál. Pozitív, leíró nyelv; képenként legfeljebb kb. 8 tiltás, a bizonyított hibákra (r2 §11.9).

## 3. A WOW-KONCEPCIÓ KÖVETELMÉNYE
A korábbi Zenit és Lake Forest képek nemzetközi luxushangulata a kiindulási vizuális mérce. Az új terv ennél lehet bátrabb, különlegesebb és személyesebb, de nem támaszkodhat fiktív építészetre vagy nem létező luxusanyagokra.

A V3 tesztek hiányosságai:
- túl egyszerű TV-fal és tároló;
- alig érzékelhető kísérőfal-kezelések;
- hiányzó integrált, rétegzett fény;
- hiányos berendezés, szőnyeg, függöny és styling;
- nem elegendő karakteres, emlékezetes építészeti gesztus.

Ezeket valódi belsőépítészeti újratervezéssel oldd meg.

Minden jelentős, látható tömör fal kapjon tudatos, a képeken is érzékelhető tervet. Nem kötelező minden négyzetcentimétert burkolni, de a nagy, jelentős falfelületek nem maradhatnak véletlenül csupasz, fehér háttérként.

Kiemelten tervezendők:
- W01 TV-fal, teljes integrált médiatároló és panelkompozíció;
- W02 és W07 mint egységes, a hálókhoz vezető falszakasz;
- W03/W03-a, a szürke 05.3 ajtó környezete;
- konyhafront, hátfal és hűtőoszlop;
- a nappali üvegezés melletti tömör falszakaszok;
- master fejvégfal, északi gardrób és déli gardróbsáv;
- a rögzített fürdőhöz illeszkedő tükör-, tároló- és világítási kompozíciók.

Alkalmazz eredeti formavilágot, gazdaságosan készíthető egyedi frontokat, texturált tapétát, dekor MDF-et, nyomott grafikát, monumentális műalkotást, karakteres bútort, rétegzett szöveteket, szőnyegeket és rejtett Hue-világítást.

Mind a tíz stílus legyen önálló karakter, ne ugyanannak a lamellás TV-falnak a tíz variációja.

## 4. RÖGZÍTETT ÉPÍTÉSZET, SZABADABB BERENDEZÉS
A lakás valós építészetét szigorúan őrizd meg:
- meglévő falak és nyílások;
- 2,90 m-es modellezett belmagasság;
- eredeti padló, fehér mennyezet;
- fehér belső ablakkeretek és szürke belső ajtók;
- tényleges tetőterasz, WPC, zöldtető, korlát és Buda-panoráma;
- meglévő vagy ellenőrzés alatt álló villamos kiállások;
- mennyezeti hűtő-fűtő mezők;
- fürdő 06.2 már beépített burkolatai, szaniterei és szerelvényei.

Tilos fiktív nyílás, plusz mennyezeti kiállás, álmennyezet, hamis kilátás, mennyezeti hűtő-fűtő mezőbe fúrás vagy térnövelés.

A korábbi Blender-bútortömbök nem kötelező designformák. A TV-falakat, tárolókat, paneleket, bútorelhelyezési szándékokat, textíliákat és világítási megoldásokat újratervezheted.

Az ülőcsoport és az étkező alapja a jóváhagyott C elrendezés (VB.2): a kanapé minimum L, inkább U, háttal keletre, az étkező felé, nyitott a TV-fal felé; az étkező alapváltozata a 160 × 90-es hosszanti asztal az ML04 alatt, hat hellyel, valós használhatósággal. Kerek, ovális vagy bővíthető asztalt kreatív alternatívaként javasolhatsz, külön Blender-méretpróbára. A TV-falon legfeljebb 60 cm mély zárt szekrénytest lehetséges, nem kötelező; a Cam_12 kamera nem korlátozza a TV-falat (VB.3). Saját ötleteidet méretezett elhelyezési szándékként add meg; koordinátát ne találj ki.

Minden új vagy módosított elemhez add meg (r2 §11.7):
- ID, fal/helyiség;
- elhelyezési szándék;
- szélesség × magasság × mélység;
- anyag és/vagy konkrét termék (gyártó, cikkszám, link, dátum);
- rögzítés, gyártás, villamos betáplálás (melyik meglévő pontról);
- fő és gazdaságos bruttó ár;
- igazolt vagy becsült státusz.

Így a terveid később valóban Blenderrel ellenőrizhetők lesznek.

## 5. KÖTELEZŐ BLENDER- ÉS KÖLTSÉGAUDIT A KREATÍV MUNKA UTÁN
A kreatív eredmény még nem véglegesen megvalósítható terv.

A külön Claude műszaki integrátor a te kimeneted alapján:
1. Új, mérethű Blender-bútortömböket és térbeli kompozíciókat hoz létre.
2. A meglévő héjba helyezi a javasolt bútorokat, tárolókat, paneleket és falkezeléseket.
3. Ellenőrzi a valódi elférést, székmozgatást, közlekedési szélességeket, ajtólendületeket, konyhai és hálószobai használhatóságot.
4. Ellenőrzi a valós elektromos kiállásokat, a Hue-megoldások betáplálását, vezérlését, szerelését és a mennyezeti hűtő-fűtő rendszer sértetlenségét.
5. A műszaki tételeket (szerelés, Hue, asztalos-előkészítés) a költségtervhez rendeli; a teljes lakásszintű bekerülést a független keresztellenőrzés számolja újra – a C tervét Astra vagy GPT-6 ellenőrzi (VB.6).
6. Dokumentálja az összes geometriai, műszaki és költségkonfliktust.
7. Ha módosítani kell a koncepciót, azonos vagy közel azonos látványértékű, kivitelezhető megoldást keres; ha az ötletet a kamera nem mutatja jól, a kamerát vizsgálja újra (VB.3).
8. Jelentős kreatív változtatást tulajdonosi jóváhagyásra terjeszt.
9. Csak az ellenőrzött változatból állít össze végleges Blender/FIXED/FRAME LAYOUT alapú ChatGPT Images-csomagot; a koncepcióképek ettől függetlenül a kész promptjaidból készülnek (VB.9).
10. A generált képeket ismét geometriailag ellenőrzi.

Az integrátor nem egyszerűsítheti vissza indokolatlanul a kreatív munkádat a régi V3-as formákra. A versenyben ugyanakkor nem szerepelhet megvalósíthatatlan, pusztán szép fantáziakép.

A jelenlegi Opus-futásban Blendert ne módosíts, és képgenerálást ne indíts. A feladatod az ellenőrzésre előkészített kreatív csomag.

## 6. EGYSÉGES KAMERA- ÉS FÉNYRENDSZER
A 60 saját prompt minden stílusban ugyanazokat a nézeteket és fényforgatókönyveket használja (pontos adatok és kompozíció: VB.3):
- **Cam_02:** nappali, TV-fal, terasz; kék óra / kora este, prémium rétegzett Hue, 2200–2700 K, RGB nélkül; a TV-fal a fő WOW-elem; közepes expozíció, a terasz és a geometria olvasható marad (kontrollnézet).
- **Cam_12 v3:** nappali hero, étkező, konyha és W02/W07, a W03 a 05.3 ajtóval; nappali, természetes, világos luxusenteriőr-fény.
- **Cam_03 K1:** konyha–étkező, konyhaorientált kompozíció, nappali fény; a FRAME LAYOUT-ot Claude integrátor adja, koordinátát ne találj ki.
- **Cam_04:** master, esti Hue-hangulat.
- **Cam_11:** ugyanaz a master, nappali panorámás kontroll.
- **Cam_10:** fürdő 06.2, műfény.

A közös C1 Zenit és C2 Lake Forest kalibrációk (Cam_02, Cam_04, Cam_11; nem a te feladatod) ugyanezt a fényt követik.

Az azonos helyiségek különböző nézetei ugyanazt a bútorozást, anyagot, frontot és világítási rendszert mutassák.

Minden általános és dekoratív fény legyen igazoltan Hue-kompatibilis; szekrénybelső funkcionális világítás lehet kivétel. Adj meg tényleges vagy ellenőrzendő tápforrást, vezérlőt, LED-profilt, diffúzort, kábelutat, szerelést és teljes bruttó bekerülést (VB.7).

## 7. A BRUTTÓ 18 M FT KIZÁRÓ KÖLTSÉGHATÁR
A teljes A-902 lakásra 18 000 000 Ft bruttó tervezhető keret van. A külön 2 000 000 Ft tartalékhoz nem nyúlunk.

A keret mindent tartalmaz: nappali, étkező, konyhabútor és gépek, tárolók, master, szükséges további berendezés, falak, textíliák, dekoráció, Hue-világítás, fürdő-kiegészítők, terasz, szállítás, szerelés és járulékos díjak.

A közös költségalap (VB.6, `KOZOS_FIX_ALAP_v1`): a 8,40 M közös fix részt egy sorban, változatlanul átveszed; a 9,60 M stílusfüggő keretet tételesen tervezed és árazod.

Készíts minden stílushoz:
- a 9,60 M-os stílusfüggő keret tételes fő és gazdaságos költségtervét a `KOZOS_FIX_ALAP_v1` soraiban, a 8,40 M fix sorral és a lakásszintű végösszeggel (fix + stílusfüggő);
- tételes bútor-, anyag-, világítási és gyártási költségeket;
- kiváltott régi elemeket és nettó változást;
- forrásolt termékárakat, dátummal;
- ellenőrizendő árajánlatok és szükséges szerelések listáját;
- költségkockázati összesítést.

Az árazás ellenőrizetlen részét ne jelöld bizonyítottnak. Árazatlan szükséges tételt a keresztellenőrző konzervatív benchmark-árral pótol és jelöl; törekedj a teljességre, mert a pótlás konzervatív. A 8,40 M fix alap versenyfeltételezés; a végső kapun ezt is ellenőrizzük.

Győztes csak olyan koncepció lehet, amelynek a végső, ténylegesen megépítendő változata független keresztellenőrzés alapján (a C tervét Astra vagy GPT-6 ellenőrzi) – fix + stílusfüggő együtt – legfeljebb 18 M Ft bruttóba kerül.

Ha egy drága, fantasztikus főváltozatot olcsóbb, hasonló látványértékű megoldásra cserélünk, már az új változatot kell képen összehasonlítani.

## 8. A VERSENY ELBÍRÁLÁSA
A három versenyzőt azonos elvek alapján külön vizsgáljuk (VB.9):

Első kapu: Blender-geometria és tényleges használhatóság.

Második kapu: elektromos, asztalos és világítástechnikai kivitelezhetőség.

Harmadik kapu: független, keresztellenőrzött teljes bruttó költségigazolás a 18 M Ft-on belül.

Negyedik kapu: jóváhagyott, azonos referenciákon és képgenerátoron alapuló renderképek geometriai egyezése.

A kész promptokból koncepcióképek már a kapuk előtt készülnek (VB.9); a végső összehasonlító képek csak a kapuk után.

Döntés: a kapukon megfelelt tervek közül a legjobb kinézetű, legerősebb, legkülönlegesebb belsőépítészeti eredmény nyer; Péter választ, kódnevekkel.

A látvány, amely nem fér el vagy túl drága, nem kompenzálható kreatív pontszámmal. Ne jelents ki győzelmet magadról vagy vereséget a másik két modellről.

## 9. SAJÁT GITHUB-ÁG ÉS KIMENETEK
Kizárólag a baseline-ág rögzített commitjából indulj:

`45632b5ad5586e1f3f884a8f723c1cc13cda6da3` (ág: `competition/baseline-20261025-v3`) → `competition/opus55-v3-1-20261025`

A draft PR célága `competition/baseline-20261025-v3`. Ha az ág már létezik: VB.10.

- Saját eredménygyökér: `05_promptok/KEP004_OPUS55_V3_1_r1/`
- Saját összefoglaló: `ai-coordination/results/WSG-20261025-OPUS55-CREATIVE-UPGRADE-V3_1_r1.md`

A brief §11.12 szerkezetét használd, a 60+6 szabállyal:
- `00_README.md` – tartalom, bázis-commit (45632b5…), források; első sorában: „a brief verziója r2, ez a kimenet r1”;
- `00_CHECKPOINT_NAPLO.md` – checkpointonként: sorszám, idő, tartalom, commit SHA, a távoli ellenőrzés eredménye;
- `01_MANIFEST_66.csv` – `nr;kep_id;stilus;kamera;fajl;statusz;validalas;checkpoint;karakterszam;mintaprompt;megjegyzes`; 66 sor: 1–60 saját, 61–66 KOZOS;
- `02_KOZOS_REALITY_FIXED_elvek.md` – közös elvek angolul: a promptsablon v3.1 §1-éből átveendő a geometria és kamera, a meglévő felületek, az őszinte anyagnevek és a közlekedési méretek; nem átveendő a „Walls and ceilings: painted white” mondat (helyette a stílus falterve, a mennyezet fehér marad) és a „Series A neutral overcast” fényszabály (helyette a VB.3);
- `03_KAMERA_KOMPOZICIOK.md` – a hat kamera (VB.3);
- `10_STILUS_SPEC/` – S01–S10 (C1/C2 nem kell);
- `20_PROMPTOK/<kep_id>.prompt.md` – pontosan 60 fájl;
- `30_TV_FAL_KONCEPCIOK_S01_S02.md`;
- `40_ELEMLISTA_V3_1.csv` – méretezett elemlista (r2 §11.7);
- `50_KOLTSEG_ES_KOCKAZAT.md` – fix + stílusfüggő, fő/gazdaságos, kiváltott tételek, LED/Hue műszaki-költség kockázati tábla;
- külön integrációs összefoglaló: a fenti results-fájl.

A promptfájlok `=== BEGIN PROMPT <kep_id> ===` / `=== END PROMPT <kep_id> ===` jelölőiben a tényleges, betű szerinti kep_id szerepeljen.

Csak a saját névterületedben dolgozz. Ne írj a main ágba, a baseline-ágba, közös forrásfájlba, Astra- vagy Fable-ágba. Nyiss saját draft PR-t a baseline-ágra.

## 10. KÖTELEZŐ GITHUB-CHECKPOINTOK
**CP0:** saját ág a baseline-commitból → README, 66 azonosítós manifest (1–60 PENDING, 61–66 KOZOS) és checkpointnapló → commit, push, távoli visszaolvasás → draft PR a `competition/baseline-20261025-v3` ágra.

**CP1:** tíz részletes stílus- és helyiségspecifikáció, az S01/S02 TV-falalternatívák, közös reality-elvek és kamerakompozíciók. Legalább két stílusonként külön ellenőrzött mentés.

**CP2:** a négy kiemelt S01/S02 Cam_02/Cam_12 prompt (külön commitban), majd az S01/S02 további nyolc kameranézete és elemlistája.

**CP3–CPn:** S03–S10 teljes promptjai, stílusonként hat, legfeljebb 6–10 új promptonként mentve.

**Záró CP:** mind a 60 saját fájl, azonosító és BEGIN/END ellenőrzése, a 6 KOZOS sor; önállósági és tartalmi ellenőrzés; elemlista; költség- és műszaki kockázati összesítés; átadás. Ha a futás nem ér végig, a PR-ben pontosan sorold fel a nem COMPLETE tételeket.

Manifeststátuszok: PENDING, DRAFT, COMPLETE, illetve a 61–66. sorban KOZOS; a `validalas` minden DRAFT, COMPLETE és KOZOS sornál NEEDS_CLAUDE_VALIDATION.

A COMPLETE kizárólag kreatív promptteljesség, nem Blender- vagy költségjóváhagyás.

Csak ellenőrzött, távoli GitHub-commit számít mentésnek (VB.10). Megszakítás esetén az elkészült fájlokat és a checkpointnaplót meg kell őrizni. GitHub-hozzáférési akadálynál azonnal jelezz. Ne ments mindent egyetlen záró commitban, és ne jelölj vázlatot késznek.

Draft PR: cím „WSG DC2026 · C · Claude Opus 5.5 – 10 stílus + 60 saját prompt (checkpointolt)”; a leírás első sora:

`WSG-COMPETITION-RESULT: OPUS55-V3_1`

## 11. LEZÁRÁS ÉS TILALMAK
Az összefoglaló első sorai:
```
WSG-COMPETITION-RESULT: OPUS55-V3_1
Versenyző: C – Claude Opus 5.5
Modell és gondolkodási szint: <ahogy a munkamenet igazolja> | nem igazolt
Bázis-commit: 45632b5ad5586e1f3f884a8f723c1cc13cda6da3
Utolsó ellenőrzött commit: <sha>
Státusz: TELJES | RÉSZLEGES | BLOKKOLT
```

Adj át:
- draft PR-linket és utolsó ellenőrzött commitot;
- valós manifestállapotot: 60/60 saját COMPLETE + 6 KOZOS (vagy a hiányzók listája);
- tíz stílust, az S01/S02 TV-falváltozatokat és az S03–S10 TV-falait;
- méretezett elemlistát;
- lakásszintű bruttó költségterveket (fix + stílusfüggő) és nyitott árazási kockázatokat;
- stílusonként: melyik asztalváltozattal és melyik teraszajtó-esettel számoltál, hol kérsz külön méretpróbát vagy második hero kamerát;
- konkrét Blender-validálási és ChatGPT Images-integrációs instrukciókat;
- rövid önértékelést a saját koncepciód erősségeiről és bizonytalanságairól.

Ne generálj képeket, ne módosíts Blendert, ne merge-elj PR-t, ne rendelj terméket.

A kreatív tervednek nem csupán szépnek kell lennie, hanem alkalmasnak kell lennie arra, hogy egy független műszaki csapat a valós A-902 lakásban, a teljes 18 milliós bruttó kereten belül megépítse. A végső győztest az ellenőrzött, valóban kivitelezhető terv látványminősége dönti el.

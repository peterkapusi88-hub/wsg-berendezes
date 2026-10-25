# WSG A-902 – ASTRA CREATIVE UPGRADE V3.1 (kiegészített kérés)
## Integrált építészeti világítás, teljes lakásminőség, WOW-korrekció, 66 képes végrehajtási terv

- **Task ID:** WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1
- **Cél AI:** ASTRA_WORK (kreatív vezető)
- **Típus:** STYLE_CONCEPT + RENDER_PROMPT + előzetes költség- és műszaki kockázat
- **Lakás, helyiségek:** A-902.
  - Részletesen: nappali–étkező–konyha (Cam_02, Cam_12).
  - Stratégiai szinten: a teljes lakás, mind a tíz stílus.
- **Stílus:** S01 Kyoto Ink, S02 BiBo Nocturne részletesen; S03–S10 stratégiai szinten.
- **Prioritás:** high
- **Gondolkodási szint:** az érvényes kreditszabály szerint Medium (Péter, 2026-10-24 19:34).
  - High csak Péter külön engedélyével. Claude ehhez a feladathoz a High-ot javasolja, mert itt a kreatív minőség a cél.
  - Ultra/Max nem.
- **Automatikus Work-indítás:** nem. Péter indítja kézzel (C rész); a GitHub nem feladatindító.
- **Keret:** A-902 bruttó 18 000 000 Ft költés + 2 000 000 Ft elkülönített tartalék, amelyhez nem nyúlunk.
  - A Zenit/Lake Forest-minőség miatti kb. 1 M Ft-os többlet csak külön, feltételes forgatókönyvként mutatható (CLAUDE.md).
- **Állapot:** TERVEZET – Péter jóváhagyására. Ha Péter elindítja, ezzel a §0 és a §11 módosításait is jóváhagyja, köztük a §11.6 fényszabályt.
- **Készítette:** Claude, 2026-10-25 02:30 CET.
  - Az időpontok innentől CET szerintiek; a téli időszámítás 03:00 CEST-kor (= 02:00 CET) kezdődött.
- **Források:**
  - Péter 02:05 CET-es visszajelzése és ötletlistája;
  - a V3.1-kérés Péter által bemásolt szövege (lent §1–10, szó szerint);
  - `ai-coordination/requests/WSG-20261025-ASTRA-V3_1_INPUT_Cam12_falak_vilagitas.md`;
  - `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md` és `…_V3_TEST_gate.md`;
  - Astra V3 r1 (PR #16, `be6b1f3`).

**Elsőbbség:** a §0 és a §11 megelőzi a §1–10-et; ütközésnél a §11 érvényes. A §1–10 Péter szövege, változtatás nélkül.

## 0. Miért kell a kiegészítés – tulajdonosi visszajelzés a V3-tesztképekre (Péter, 2026-10-25 02:05 CET)

**Javult:**
- a geometria sokkal rendezettebb;
- a terasz valósághűbb (fű, szép barna WPC);
- maga a render szép;
- a kanapék rendben vannak.

**Nem jó:**
- nincs WOW-hatás;
- a fal nem ötletes és nem exkluzív;
- a TV mögötti szekrény továbbra is ingerszegény;
- a panelek nem érnek a mennyezetig, és nem is egyforma magasak;
- a korábban adott ötletekből semmi igazán új nem lett;
- a „minden fal burkolt” elvet sem látja jónak, főleg a nagy, egybefüggő falakon;
- az első Zenit/Lake Forest képek még mindig a legjobbak, csak ott semmiről nem tudjuk, mi az és mennyibe kerül;
- kérdése: nem korlátozza-e túl a Blender a formavilágot?

**A képek** (mind a négy ugyanazt az Astra V3 r1 tartalmat mutatja):
- **`_V3_r1` (Claude, Péter 02:06 CEST):** `04_renderek/ai_chatgpt/STYLE10_KEP004/CREATIVE_UPGRADE_V3/`. Audit: `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md` – a terasz felőli padlósík 10–13,5 %-kal eltér, FAIL.
- **`_V3_TEST` (a második Claude-munkamenet, Péter 02:22 CEST, r2-csomag javított tömbképpel):** `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/`. Audit: `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`.
  - S02: a héj ±1 %-on belül, `ELŐSZŰRT – FELTÉTELES`.
  - S01: a belmagasság kb. +8 %, FAIL.
  - Mindkettőn a specifikáltnál magasabb falbútor (magas szekrény ≈2,45 m, alsó ≈0,65 m), és keletebbre csúszott étkező.

### 0.1 Claude diagnózisa: mi fékezte a képeket
Forrás: a ténylegesen futtatott V3-teszt promptok, `05_promptok/KEP004_ChatGPT_Images_V3_teszt/`.

A Blender három dolgot rögzített: a héjat, a kamerát, valamint a kanapé és az étkező helyét. A többi féket a saját szabályaink okozták:

| # | Fék | Bizonyíték | Mi változik a V3.1-ben |
|---|---|---|---|
| F1 | **Fény** | „neutral overcast daylight, no sun … no warm grading, haze or bloom … Luxury must come … not from warmer light” (KEP-004 promptsablon, `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` §1). Hozzá a teszt saját fénybekezdése: csak meglévő pontok, nincs LED. | §11.6: nézetenkénti fényforgatókönyv, nappal és este |
| F2 | **Üres szoba** | „Nothing else stands in the room: no coffee table, side table, floor or table lamp, sideboard or extra seating” (Claude FRAME LAYOUT). „Keep the middle of the room free; do not add a coffee table” (V3 r1). „the living point ML05 … carries no fixture”. A függöny, a díszpárna és a pléd egyszer sem szerepelt. | §11.5: teljes berendezés és styling |
| F3 | **Arányok** | S01: KI3-L 48 cm magas; KI3-V 220 cm; KI3-P z 0,55–2,45. S02: BN3-P z 0,55–2,45; BN3-R z 0,40–2,20. A belmagasság 2,90 m: három különböző felső vonal, egyik sem ér a mennyezetig. | §11.2: mennyezetig vagy egyetlen közös vonalig |
| F4 | **Mindenhol ugyanaz a halk fal** | „The wallpaper is a low-contrast fine texture”, a W01–W04-en, 14–18 m²-en | §11.3: falhierarchia |
| F5 | **Kicsi gesztus** | A mű 100×180 (S01) és 120×160 cm (S02); a TV-fal egyetlen sík panel | §11.4: Péter hat eszköze, nagyobb lépték |
| F6 | **A prompt formája** | Kb. 19 000 karakter, kb. 77–79 tiltó kifejezés (no, not, never, without…). A szürke tömbkép (1b) a V3 r1 rövid dobozait mutatta, a képgenerátor ezeket másolta. | §11.7–11.9 és a B rész |

**Következtetés:**
- **A geometria már kezelhető:** az S02 `_V3_TEST` héja ±1 %-on belül van, a WOW mégis hiányzik. A szűk keresztmetszet tehát a specifikáció, a berendezés és a fény.
- A Blendert nem kell elengedni. Nélküle a v1-hez hasonlóan nem létező lakás jönne vissza: kitalált panoráma és nyílások, mennyezeti fénycsík, kiállás nélküli csillár, valódi kőnek mutatott burkolat.
- **A sorrendet fordítjuk meg:**
  1. előbb a terv, szabadon, a rögzített héjon belül (§11.8);
  2. utána Claude méretez Blenderben, ellenőriz és áraz;
  3. végül a render.
- A V3 r1 tömbjei nem kötelező befoglalók.

### 0.2 A WOW-mérce: a v1 Zenit és Lake Forest
**Fájlok:**
- `04_renderek/ai_chatgpt/A902_Zenit_1_nappali_chatgpt.png`, `…_2_etkezo_konyha_chatgpt.png`, `…_3_master_chatgpt.png`;
- `04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png`, `…_2_…`, `…_3_…`.
- Státuszuk `KONCEPCIÓ – NEM VALIDÁLT`, a geometriájuk nem a lakásé.

**Ezt vedd át (az érzetet):**
1. **Rétegzett, meleg fény:** alkonyat vagy kék óra belső fényekkel (Zenit); lágy, világos nappal, átsütő áttetsző függönnyel (Lake Forest).
2. **Padlótól mennyezetig futó függőleges elemek:** függöny; bordázott, LED-del súrolt TV-fal (Zenit).
3. **Teljes textil és styling:** nagy szőnyeg, párnák, pléd, dohányzóasztal, kisasztal, álló- és asztali lámpa, nagy növény, tárgycsoportok.
4. **Egy nagy, karakteres mű:** nagy texturált relief (Lake Forest), vagy egységes képsor (Zenit).
5. **Erős anyagkontraszt:** meleg fa, bouclé és szövet, fém; matt és selyemfényű felületek.
6. **Látványos lámpatest a nappali mennyezeti pontján:** Zenitnél gyűrű, Lake Forestnél gömbcsillár. Nálunk ez az ML05 meglévő kiállás (§11.5).

**Ezt ne vedd át:**
- kitalált panoráma (Parlament) és nyílások;
- mennyezeti fénycsík, álmennyezet;
- lámpa kiállás nélkül;
- valódinak mutatott kő;
- nem létező fülke.

**Kötelező:** stílusonként írd le, melyik összetevőt hogyan valósítod meg, valós termékkel, mérettel és bruttó árral.

---

## A korábban megbeszélt V3.1-kérés – Péter bemásolt szövege (2026-10-25 02:05 CET), szó szerint
A cím a fájl címe. Ellenőrzés: 272 sor, 14 289 karakter, sha256 `577ee52f009964c296e01bb91ed8f5169711c45cb39303f3ec45d1d97b92c1c1` (a bemásolt üzenet 126–397. sora).

**Repository:** `peterkapusi88-hub/wsg-berendezes`

**Kiindulási állapot:** A Creative Upgrade V3 már elkészült a PR #16-ban, commit `be6b1f333cf2923790e4577c9b716f5fcb3bb417`. A Claude-féle Cam_02 geometriai javítás szintén elkészült. A második nappali hero kamera Blender-előkészítése folyamatban van.

**FONTOS: Ez nem újrakezdés.** A meglévő Astra V2 és Creative Upgrade V3 kreatív eredményeket tovább kell fejleszteni, nem lecserélni. Az eredeti fájlok megőrzendők. Képet ne generálj, Blendert ne módosíts.

## 1. Végső kreatív cél

A teljes A-902 lakás egyszerre rendelkezzen két tulajdonsággal:

**A. KÖVETKEZETES, MAGAS SZÍNVONALÚ BELSŐÉPÍTÉSZETI MINŐSÉG**

Az egész lakás minden látószögből egy nemzetközi színvonalú, részleteiben megtervezett luxusenteriőrnek hasson.

Ne legyenek véletlenszerűen csupasz, nagy fehér falfelületek. A falak, az integrált szekrények, a burkolatok, a művészeti elemek, a világítás és a bútorok alkossanak egységes építészeti rendszert.

**B. KARAKTERES, EMLÉKEZETES WOW-ELEMEK**

Az általános minőségérzet mellett minden fontos helyiségben legyen egy vagy több különleges, vizuálisan erős megoldás.

Ez lehet integrált TV- és tárolófal, monumentális egyedi vászonkép, különleges burkolat, nagyméretű szoborszerű front, egyedi falgrafika vagy kifejezetten izgalmas rejtett világítás.

Egy karakterelem nem helyettesítheti a teljes tér megtervezettségét, és a teljes tér igényes kidolgozottsága sem helyettesítheti a karakteres, emlékezetes gesztust.

## 2. ÚJ KIEMELT TULAJDONOSI PRIORITÁS: REJTETT LED-VILÁGÍTÁS

A rejtett, integrált LED-hangulatvilágítás a tulajdonos egyik legfontosabb vizuális és funkcionális elvárása.

A V3-ban szereplő általános LED-tiltások túlságosan korlátozóak voltak. Az új szabály:

**ALLOW AND ACTIVELY DESIGN INTEGRATED INDIRECT LIGHTING WHERE PHYSICALLY AND ELECTRICALLY FEASIBLE.**

A cél nem egyszerűen fényes LED-csíkok hozzáadása, hanem luxusminőségű, részletgazdag, rétegzett fénykompozíció.

Vizsgáld különösen:

- TV-fal és médiatároló mögötti közvetett megvilágítás.
- Falpanel és burkolat mögötti árnyékfény.
- Szekrények mögötti, fölötti és alatti rejtett világítás.
- Lábazati, alacsonyan futó fényvonalak.
- Integrált polc- és bemutatófülke-világítás.
- Texturált tapéták és dekorfelületek súrolófénye.
- Függönyök mögötti vagy előtti indirekt fény, illetve falra szerelt takarólécbe vagy karnisburkolatba rejtett világítás.
- A mennyezet–fal találkozásánál kialakított, falról megtámasztott indirekt fény, ahol ez a meglévő mennyezeti hűtő-fűtő rendszer megbolygatása nélkül megvalósítható.
- Master hálószobai fejvégfalak, éjjeliszekrények és gardróbfrontok fénykompozíciója.
- Konyhai bútorvilágítás, amennyiben megfelel a meglévő konyha és villamos kialakításának.
- Fürdőszobában a megfelelő védettségű, műszakilag szabályos tükör-, tároló- és indirekt világítás.

**Világítási minőség:**

A fényforrás lehetőleg ne legyen közvetlenül látható. Megfelelő profil, diffúzor, egyenletes fényeloszlás és valósághű fényhatás szükséges.

Kerüld:
- a látható LED-pontokat;
- a túlzott RGB-színes hatást;
- az összes szekrényél világítását;
- az irreális, mindenhol lebegő fényvonalakat;
- a takarás, kábelvezetés vagy tápegység nélküli megoldásokat;
- a nappali jelenetek irreálisan erős dekorfényét.

A nappali renderben a világítás legyen visszafogott, az esti jelenetben viszont valóban mutassa meg a prémium hangulatot.

## 3. PHILIPS HUE – KÖTELEZŐ RENDSZERELV

A lakás általános és dekoratív világítását Philips Hue-rendszerben szeretném működtetni.

Ez vonatkozik az új, látható építészeti hangulatvilágításra és a korábban meghatározott Hue-kötött világítótestekre is.

**Kivétel:** a szekrények belső, tisztán funkcionális világítása lehet nem Hue-kompatibilis. Például ajtónyitásra kapcsolódó gardróbfény vagy belső polcmegvilágítás.

A tervezett fényvonalaknál mindig különböztesd meg:
1. valódi Philips Hue LED-rendszer;
2. bizonyítottan Hue-rendszerbe integrálható, ellenőrzött harmadik féltől származó vezérlés;
3. nem Hue-s szekrénybelső funkcionális világítás.

Ne tekints automatikusan minden 24 V-os LED-szalagot Hue-kompatibilisnek.

A kompatibilitás, a fényerő-szabályozás, a színhőmérséklet-vezérlés, a tápegység és az esetleges vezérlő költsége is ellenőrzendő.

## 4. MŰSZAKI REALITÁS – A VILÁGÍTÁS LEGYEN MEGVALÓSÍTHATÓ

A meglévő falak, nyílászárók, szürke belső ajtók, parketta, terasz, elektromos kiállások és mennyezeti hűtő-fűtő rendszer változatlanok.

A rejtett világítás lehet bútorhoz, falpanelhez, takaróléchez vagy más, utólag felszerelhető elemhez integrálva.

Nem engedélyezett:
- új, fiktív mennyezeti lámpakiállás;
- a mennyezeti hűtő-fűtő rendszerbe fúrás;
- új álmennyezet automatikus feltételezése;
- elektromos kiállások eltüntetése;
- nem létező falfülke létrehozása;
- a parketta rögzítéssel vagy burkolással történő károsítása;
- nem hozzáférhető tápegység vagy vezérlő;
- a fürdőszobai villamos biztonsági követelmények figyelmen kívül hagyása.

Ahol a kábelezés vagy az áramellátás még nem igazolt, jelöld: **FELTÉTELES – CLAUDE VILLAMOS AUDIT SZÜKSÉGES**.

Ne tilts ki emiatt kreatív lehetőségeket: dolgozz ki olyan utólagos megoldásokat is, amelyek szekrényben, bútor hátoldalában vagy szerelt panel mögött vezethetők.

## 5. TELJES FAL-, BURKOLAT- ÉS TÁROLÓRENDSZER

A Creative Upgrade V3-ban kidolgozott falstratégiákat meg kell tartani.

Különösen fontos:
- teljesen megtervezett TV-fal;
- integrált médiatároló és szükség esetén magas szekrény;
- étkezőasztal mögötti fal;
- a meglévő szürke ajtók környezetének igényes kialakítása;
- falsíkba komponált tapéta, textil, dekor MDF, laminált és festett panel;
- egyedi, gazdaságosan gyártható vászonkép és falgrafika;
- különleges, de valóban kivitelezhető gardróbfrontok;
- a falfelületek és a rejtett világítás összhangja.

Ahol szekrényfrontot tapétával, textillel vagy grafikával kombinálsz, legyen valódi szerkezeti és gyártási megoldás.

Ne legyenek mind a tíz stílusban azonos lamellák vagy azonos LED-keretek.

A szürke belső ajtók színe és helye maradjon. A környezetükbe tervezhető falburkolat, tapéta, dekorpanel és fényhatás, de az ajtók nem változhatnak meg.

## 6. S01 KYOTO INK ÉS S02 BIBO NOCTURNE – A V3 MEGTARTÁSA

A PR #16-ban elkészült két koncepció kreatív alapja megőrzendő.

**S01 Kyoto Ink:**
- grafitszürke integrált TV-tároló;
- 240 cm-es alacsony médiatároló;
- keskeny magas szekrény;
- rétegzett grafit és füstszürke panelek;
- finom papírrost-hatású tapéta;
- monumentális egyedi grafika;
- meglévő L alakú Lennon kanapé és a jóváhagyott bútorok.

Ehhez tervezz finom, japános, precíz, rejtett fénykompozíciót. Például a TV-panel mögötti egyetlen finom árnyékfény, a magas szekrény oldalán rejtett fény vagy a függöny menti indirekt világítás.

**S02 BiBo Nocturne:**
- mélykék integrált tárolófal;
- magas kabinet és keskeny valódi tükörsáv;
- ezüstszürke textilhatású tapéta;
- a meglévő mélykék U alakú JÄTTEBO;
- a jóváhagyott étkezőbútorok;
- karakteresebb, drámai, mégis elegáns kompozíció.

Ehhez a Kyoto Inktől jól megkülönböztethető rejtett fénykompozíciót tervezz: szekrénytestek mögötti indirekt fény, finom fal-súrolófény vagy tükör körüli, fizikailag megvalósítható részlet.

**A meglévő V3-as LED-tiltásokat célzottan módosítsd**, de a V3 fal-, bútor- és tárolókoncepcióját ne cseréld le.

Új kép vagy képgenerálás most nem szükséges.

## 7. ÜLŐBÚTOROK ÉS TÉRKOMPOZÍCIÓ

A tíz stílus között lehet U alakú, L alakú vagy más, tudatosan megtervezett ülőbútor.

Ne erőltesd ugyanazt a kanapékialakítást minden koncepcióra.

Minden stílushoz rögzítsd, hogy:
- milyen a kanapé formája;
- miért illik a stílushoz;
- milyen térélményt ad;
- hogyan kapcsolódik a TV-falhoz, az étkezőhöz és az integrált világításhoz;
- fizikailag elfér-e a tényleges lakásban.

Az AI-képgenerátor nem rendezheti át önkényesen a teret.

## 8. A 66 KÉPES VÉGREHAJTÁSI TERV

A projekt teljes célja 66 kép, fokozatos generálással.

**60 új stíluskép: 10 stílus × 6 kameranézet**

1. Cam_02 – nappali–terasz, geometriai kontrollnézet.
2. Új nappali hero kamera – a TV-fal felől.
3. Cam_03 – konyha–étkező.
4. Cam_04 – master hálószoba belsőépítészeti nézete.
5. Cam_11 – ugyanaz a master hálószoba, panoráma felé.
6. Cam_10 – fürdőszoba 06.2.

**További 6 Zenit/Lake Forest kalibrációs kép.**

Az új nappali hero kamerából lehetőleg látszódjon:
- a kanapé eleje;
- az étkezőasztal;
- a konyha egy része;
- az étkező mögötti fal;
- a meglévő szürke belső ajtók és a környezetükben kialakított falburkolatok.

A végleges képkivágást Claude valódi Blender-kameravizsgálata határozza meg. Nem szabad a valós geometriát azért megváltoztatni, hogy minden egyszerre látszódjon.

A két nappali kép ugyanazt a szobát, ugyanazokat a bútorokat, falakat és világítási megoldásokat mutassa.

A Cam_04 és Cam_11 ugyanazt az egyetlen master hálószobát mutassa. Az ágy 180 × 200 cm, tengelye y = 6,40 m.

A fürdőben az eredeti burkolatok, szaniterek és gépészeti adottságok megmaradnak. Csak azokkal összeegyeztethető tároló-, tükör-, kiegészítő- és világítási megoldások tervezhetők.

A 66 képet nem indítjuk egyszerre. Kisebb adagokban, műszaki és kreatív jóváhagyással készülnek.

## 9. KÖLTSÉGKONTROLL – VÁLTOZATLANUL KÖTELEZŐ

**A-902 bruttó célkeret: 18 000 000 Ft. Tartalék: további 2 000 000 Ft, amelyhez a normál tervezés nem nyúlhat.**

A falburkolat, a szekrény, a művészeti elem és a LED-világítás nem automatikus pluszköltség az eredeti tervek felett. A korábbi csomagokból kiváltott elemek árát le kell vonni, és az új kombináció tényleges teljes bekerülését kell számolni.

Minden új LED-megoldásra adj:
- becsült teljes bruttó bekerülési árat;
- LED-szalag vagy lámpatest;
- profil és diffúzor;
- Hue-vezérlés vagy kompatibilis rendszer;
- tápegység;
- kábelezés;
- szerelés;
- szükséges bútorasztalos előkészítés;
- olcsóbb, közel azonos vizuális hatású alternatíva.

A legjobb vizuális hatás / teljes bekerülési költség arányt keresd.

Ne tételezz fel nulla forintos szerelést, korlátlan ingyenes kábelezést vagy automatikusan rendelkezésre álló elektromos csatlakozást.

A túl költséges fénymegoldásokat egyszerűsítsd:
- kevesebb, de jobban elhelyezett fényvonal;
- rövidebb profilos szakasz;
- standard bútorhoz integrált fény;
- egyszerűbb front- és panelrészlet;
- kisebb számú külön vezérelt zóna.

A cél a prémium fényhatás megőrzése, nem a maximális LED-mennyiség.

Minden ár jelenleg becslés, amíg konkrét termékkel vagy beszállítói ajánlattal nincs alátámasztva.

## 10. KONKRÉT KIMENET

1. Vizsgáld felül a Creative Upgrade V3 tíz stílusát az új világítási elvárások alapján.
2. Mind a tíz stílushoz készíts megkülönböztethető integrált világítási stratégiát, helyiségenkénti bontásban.
3. Az S01 Kyoto Ink és S02 BiBo Nocturne esetén dolgozz ki pontos, kreatív V3.1 világítási módosítást a meglévő Cam_02 promptokhoz, valamint alkalmazási elvet az új hero kamerához.
4. A többi nyolc stílusnál egyelőre stratégiai szinten dolgozz, hogy ne készítsünk fölöslegesen 66 új részletes promptot az első teszt előtt.
5. Tüntesd fel a szükséges elektromos kiállásokat vagy lehetséges tápforrásokat, de ezeket jelöld ellenőrizendőnek, ne feltételezd a létezésüket.
6. Különítsd el a Hue-kötött hangulatvilágítást és a nem Hue-s szekrénybelső funkcionális világítást.
7. Készíts költség- és műszaki kockázati táblát, valamint gazdaságos világítási alternatívákat.
8. Az eredmény új, verziózott V3.1 fájlokba kerüljön GitHubon. A V3 r1 maradjon érintetlenül.
9. A meglévő kreatív alapot, eredeti bútorokat és falrendszereket őrizd meg. Ne módosíts Blender-geometriát.
10. A végén add meg a fájlokat, a commitot, a nyitott műszaki feltételeket és a Claude-nak szóló integrációs instrukciót.

**VÉGSŐ ELVÁRÁS**

A teljes lakás legyen részleteiben megtervezett, magas minőségérzetű, karakteres, nem csupasz, látványos és hangulatos.

A falak, a bútorok, az egyedi művészeti elemek és a rejtett világítás együtt alkossanak különleges, mégis valóban kivitelezhető luxusenteriőrt.

A WOW-hatás legyen erős, de a 18 milliós bruttó célkeret és a geometriai realitás maradjon kötelező.

A feladat nem teljesül pusztán stratégiával, világítási javaslatokkal vagy rövid promptkiegészítésekkel.
Készíts négy TELJES, részletes, angol nyelvű V3.1 kreatív renderpromptot:
1. S01 Kyoto Ink – nappali–terasz, Cam_02.
2. S02 BiBo Nocturne – nappali–terasz, Cam_02.
3. S01 Kyoto Ink – második nappali hero kamera, a TV-fal irányából.
4. S02 BiBo Nocturne – második nappali hero kamera, a TV-fal irányából.
Mind a négy prompt egységesen tartalmazza:
- a korábbi Astra V2-ből megtartott, pontosan azonosított bútorokat;
- a Creative Upgrade V3-ban kialakított teljes fal-, burkolat- és integrált tárolókoncepciót;
- a karakteres, emlékezetes WOW-elemeket;
- az új, kiemelt rejtett LED- és Hue-világítási koncepciót;
- a megfelelő kanapétípust (Kyoto: L, BiBo: U);
- a tényleges kameranézetből látható kompozíciót;
- a valós geometriára, villamos kiállásokra és meglévő felületekre vonatkozó korlátokat;
- a listán kívüli bútorok és kitalált fényforrások tiltását;
- a választott fő anyagváltozatot, valamint külön gazdaságos alternatívát.
Ne pusztán LED-sorokat fűzz a V3 végére. A kreatív utasításokat teljes egészükben szerkeszd újra, hogy ne legyen köztük ellentmondás.
A Cam_02-höz már elkészült Claude geometriai v2 blokkja. Ezt használd kreatív referenciaként.
Az új hero kamera pontos Blender-pozícióját Claude véglegesíti. A hozzá készülő promptok legyenek teljes kreatív tartalmúak, de a még nem igazolt kamerageometriát jelöld integrálásra váró adatként; ne találj ki kameraértékeket.
Kimeneti követelmény: a négy új kreatív prompt külön-külön legyen átadható Claude-nak, aki a végleges FIXED blokkokkal, referenciákkal és ellenőrzött geometriával teljes, futtatható ChatGPT Images-csomagot készít belőlük.
A további nyolc stílushoz most csak a tízstílusos V3.1 világítási és anyagstratégiát készítsd el. A teljes 66 képes sorozat további promptjait az első sikeres képteszt után dolgozzuk ki.
Az A-902 18 millió Ft-os bruttó berendezési célkerete és a 2 millió Ft-os tartalék változatlan. A V3.1-ben szereplő világítás és falkezelés költségét is számold.
Az eredeti V2 és V3 fájlokat ne írd felül. Az új promptok külön V3.1 fájlokba kerüljenek GitHubon.
Ne indíts képgenerálást vagy Blender-módosítást.

---

## 11. KIEGÉSZÍTÉS – Péter 02:05 CET-es visszajelzése és Claude javaslata (kötelező, elsőbbséget élvez)

### 11.1 S01 és S02: mi marad és mi változik a V3-hoz képest
**Marad – a stílus identitása:**
- **S01:** grafit „tintavonal”, papírrost-hatás, monumentális tusgrafika. Lennon L (P14), Toni (P09), 6 db Eamy, Nifelia szőnyeg, Somar Ø76 az ML04-en.
- **S02:** mélykék tárolófal, keskeny valódi tükörsáv, ezüstszürke textilhatás. JÄTTEBO U (P04), Anouk (P08), 6 db Ciselia, Brisia Ø50 az ML04-en.

**Újratervezendő, a §6 „megtartás” ellenére:**
- a TV-fal elemeinek magassága, kiterjedése és léptéke (§11.2);
- a falkezelés eloszlása (§11.3);
- a mű mérete (§11.4);
- a berendezés és a styling (§11.5);
- a fény (§11.6).

A koncepció neve és karaktere marad, az arányai nem.

### 11.2 TV-fal és magas elemek: mennyezetig, vagy egyetlen közös vonalig
**Tények (TERV SZERINT):**
- **W01, a nappali felőli sík:** x 3,67; y 4,05–8,05 (4,00 m hosszú).
- **Belmagasság:** 2,90 m a modellben; mért 2,90–2,93 m (Kémeri, 2026-10-21).
- **Kiállások a W01-en:**
  - D16/D17 (y 6,45 / 6,25);
  - G01–G04 (y 6,03–6,52), G08 (y 6,05);
  - D18 (y 4,75);
  - FL02 fali lámpakiállás (y 7,85; z 2,85).
- **Mennyezet:** a hűtő-fűtő HF03 mező x 3,77-nél kezdődik, kb. 10 cm-re a falsíktól.

**A két megengedett megoldás:**
- **(a) Padlótól mennyezetig (0–2,90 m) futó kompozíció:**
  - panel, burkolat vagy front, a mennyezet alatt 10–20 mm-es árnyékfugával;
  - falra rögzítve; a mennyezethez semmit nem rögzítünk.
- **(b) Egyetlen közös felső vonal minden elemen:**
  - javasolt magasság az üvegfal szemöldökének alsó éle, z ≈ 2,53 m;
  - a fölötte maradó sáv tudatosan tervezett: fehér marad, vagy az FL02-ről táplált felső súrolófényt kap.

**Tilos:**
- három különböző felső vonal;
- a TV körül lebegő kisebb panel nagy, kezeletlen fehér mezővel.

**TV-tároló – ne egyetlen 48 cm-es doboz legyen.** Péter 2. ötlete szerint:
- alacsony, lebegő vagy lábazatos konzol, két oldalt keskeny, magas zárt elem, fölötte panel vagy tapéta;
- vagy aszimmetrikus, lebegő zárt–nyitott kombináció;
- gazdaságos út: standard alsó bútor + nagyon erős háttérfal + 1–2 egyedi felső vagy oldalsó elem.

**Mennyezetig érő zárt szekrénytest:**
- legfeljebb 60 cm mély;
- a teteje és a HF-mező kapcsolata: **FELTÉTELES – CLAUDE AUDIT SZÜKSÉGES** (szellőzés, páralecsapódás, a mező hatásfoka, hozzáférés);
- a legfeljebb 4 cm-es panel és burkolat árnyékfugával felmehet a mennyezetig: a teteje még a HF-mező előtt van (x 3,67–3,71), a 60 cm-es szekrény teteje viszont már alatta (x 3,67–4,27).

**Szerviz:**
- D16/D17 és a G-pontok hozzáférhetők: levehető hátlap vagy szervizajtó;
- a D18-hoz szervizkivágás kell;
- a TV saját, teherhordó tartón áll.

**A sarok szabadon marad:** x < 4,40 és y > 7,70 között ne legyen magas szekrény, mert ott áll a Cam_12.

### 11.3 Falhierarchia: nem minden fal burkolt
Péter: nem kell minden nagy, egybefüggő falat burkolni.

**Nézetenként:**
- **1 fő fal**, erős kezeléssel: a Cam_02-n a W01 TV-fal, a Cam_12-n a W02 + W07 összekötő fal;
- **1–2 másodlagos elem:** nagy mű, függöny, konyhafront, lámpatest;
- **a többi nyugodt keret:** a meglévő fehér fal, rajta legfeljebb mű és fény.

A „nem csupasz” nem jelenti azt, hogy „burkolt”: egy nagy fehér falat egy nagy mű, súrolófény vagy bútor is megtervezetté tesz.

**A V3 r1 B csomagja nem automatikus:**
- a W02–W04 kísérőtapéta (14–18 m², S01-nél 160–260 eFt) csak ott kell, ahol a kompozíció kéri;
- a megtakarítás a fő falra, a műre, a fényre és a textilre megy.

**W02 + W07 egy gondolatot kap** (V3.1-bemenet §3):
- a közlekedőben legfeljebb 2–3 cm-es kezelés;
- a kapcsolóoszlop (x 7,149) körül 10–15 cm szabadon marad;
- a K25–K27 + D46 a közlekedő sarkában szabad.

### 11.4 Péter hat eszköze – kötelezően vizsgálandó
A költségek Péter 02:05 CET-es üzenetéből valók: forrás nélküli becslések. Astra saját forrással árazza, Claude függetlenül ellenőrzi.

| # | Eszköz | Változatok | Becsült bruttó ár | Mit ad |
|---|---|---|---|---|
| 1 | **Teljes TV-fal tapéta vagy dekorpanel** | textilhatású prémium tapéta; japán- vagy lenvászonhatású falburkolat; finoman bordázott vagy paneles MDF/melamin; nagy mintás, de nyugodt falpanel | tapéta + felrakás 80–250 eFt/fal; egyszerű dekorpanel, lamella vagy bútorlap 150–400 eFt/fal; egyedi asztalos TV-fal 350–900 eFt+ | azonnal karaktert ad; a TV kevésbé „fekete lyuk”; nem zsúfolja túl a szobát |
| 2 | **TV-tároló kompozíció** | alacsony konzol + két oldalt keskeny, magas zárt elem + fölötte panel/tapéta; vagy aszimmetrikus, lebegő polcos–zárt kombináció | egyszerűbb asztalos vagy standard rendszer 250–600 eFt; komolyabb egyedi 0,7–1,5 M Ft | „standard alsó bútor + nagyon erős háttérfal + 1–2 egyedi elem”: sokkal olcsóbb, de majdnem ugyanúgy néz ki |
| 3 | **Nagy, karakteres egyedi print vagy vászon** | absztrakt; japános vagy tusfestéses; textilre nyomott; semleges, de nagyvonalú | nagy print/vászon 40–180 eFt; prémium keretezéssel 100–300 eFt | a drága érzetet gyakran jobban emeli, mint egy rosszul választott drága bútor |
| 4 | **Szélesebb, teljesebb, texturált kárpitozott panel** | a TV-falon vagy egy másik fal nagyobb részén; a hálóban is | egyszerű kárpitozott panel 100–300 eFt; nagyobb egyedi rendszer 300–700 eFt | luxusérzet; a V3 keskeny panelgondolata jó, csak kevés |
| 5 | **„Titkos fegyver”** | jó minőségű melamin, dekor MDF, nyomott panel, tapétázott bútorfront | 120–350 eFt/falrész | képen és élőben is jól néz ki; látványban gyakran többet ad, mint amennyibe kerül |
| 6 | **Grafikus vagy mintás tárolófrontok** | semleges textilhatás, finom japános grafika, festményszerű front, matt, puha tónusú minta | a 2. és 5. sorral együtt árazandó | sok tároló „gardróbszekrény-érzet” nélkül |

**Követelmény:**
- Az S01 és az S02 a nappaliban (Cam_02 + Cam_12) **legalább hármat** használjon közülük, láthatóan.
- Minden használt vagy elvetett eszközről egy sor indoklás.
- S03–S10: stratégiai hozzárendelés.

### 11.5 Teljes berendezés és styling: az üres szoba nem luxus
**Visszavonva:** a §0.1 F2 sorában idézett szabályok.

**Stílusonként kötelező, valós termékkel** (elsőként Westwing vagy Kave Home; dátum, ár, méret):
- **Dohányzóasztal vagy ottomán/puff.**
  - Az S02 U belseje szűk: ott kisebb puff vagy tálca is lehet.
  - Az ülőéltől 40–45 cm, a közlekedő legalább 80 cm. Claude Blenderben ellenőrzi.
- **Szőnyeg:** a kanapé első lábai rajta álljanak.
- **1–2 kisasztal.**
- **Álló- és/vagy asztali lámpa:** Hue-izzóval vagy igazoltan Hue-kompatibilis, a meglévő dugaljak közelében.
- **Lámpatest az ML05 nappali kiálláson** (x 5,62; y 6,27; meglévő mennyezeti kiállás, TERV SZERINT):
  - stílusonként egy karakteres, Hue-kompatibilis darab;
  - csak a meglévő dobozra; más mennyezeti fúrás nincs (HF-mező);
  - ha nem esik az ülőcsoport közepére, indokold a megoldást: mennyezeti lámpatest vagy tudatos aszimmetria.
- **Függöny az üvegfalon, a mennyezet alól a padlóig:**
  - áttetsző, igény szerint sötétítő réteggel;
  - sín vagy karnis a szemöldök belső síkján (y 8,05; z 2,53–2,90); az R01/R02 redőny szervizfedele szabad marad;
  - az S02-nél a U északi vége 0,225 m-re van az üvegtől: ott vékony függöny, vagy csak a nyugati szakaszon. A U eltolásáról Péter dönt.
- **Díszpárnák, pléd, 1–2 nagy növény, könyv- és tárgycsoportok:** felületenként 3–5 darab, nem zsúfoltan.
- **Étkező:** asztali dísz; az ML04 függesztéke már megvan.

Listán kívüli nagy bútor továbbra sem kerülhet a képre, ezért a lista legyen teljes.

### 11.6 Fény – nézetenkénti forgatókönyv
**Claude javaslata.** Péter jóváhagyásával felváltja a KEP-004 „semleges, borult” összevetési szabályát (a KEP-004 sablon v3 §1-ét).

- **Cam_02 – nappal:**
  - A terv szerint a nappali üvegfala az északi homlokzaton van.
  - Világos, lágy északi fény; tiszta vagy enyhén felhős ég; a belső térben nincs napfolt.
  - Természetes fehéregyensúly, nem fakó expozíció.
  - A tervezett rejtett LED-ek és a lámpák visszafogottan, alacsony fokozaton égnek.
- **Cam_12 – hero, este:**
  - Kék óra, kora este; a Cam_12-n az üvegfal nem látszik.
  - Hue „Esti” jelenet, 2200–2700 K, RGB nélkül: az ML04 és az ML05 tompítva, a lámpák égnek, és a V3.1-ben megvalósíthatónak jelölt rejtett LED-ek is.
  - A fényforrás nem látszik.
- **Mind a tíz stílus ugyanazt a forgatókönyvet kapja,** így az összevetés tisztességes marad.
- **Cam_03/04/11/10:** a V3.1 javasoljon. Alapjavaslat:
  - Cam_03 nappal;
  - Cam_04 este (fejvégfény);
  - Cam_11 nappal (panoráma);
  - Cam_10 műfény.

### 11.7 Méretezett elemlista – hogy a Blender a TE tervedet mutassa
Minden új vagy megváltozott elemhez egy sor (CSV-kompatibilis). Mezők:
- ID;
- fal vagy hely;
- x/y-tól–ig modellkoordinátában (m);
- z-tól–ig;
- mélység;
- anyag vagy termék (cikkszám, link, dátum);
- rögzítés;
- táp (D, FL vagy ML pont, vagy nincs);
- fő bruttó ár;
- gazdaságos bruttó ár;
- státusz (becslés vagy ellenőrzött).

**Beletartozik:**
- a TV-fal elemei;
- a W02/W07 kezelése;
- a konyha: front, munkalap, hátfal és hűtőoszlop a W03-a előtt;
- függöny, szőnyeg, dohányzóasztal, lámpák, az ML05 lámpatest;
- LED-szakaszok: hossz, profil, táp.

**Claude ebből:**
- új Blender-tömböt (1b) készít a Cam_02-re és a Cam_12-re;
- validátort futtat;
- ellenőrzi a kiállásokat, a közlekedőt, az ajtólendületet és az árakat;
- az eltéréseket a generálás előtt jelzi.

### 11.8 A rögzített héj – csak ez kötött
**Változatlan:**
- falak, nyílások, üvegfal és szemöldök; belmagasság 2,90 m;
- a meglévő szürke tölgy padló (pontos dekorja NEM IGAZOLT);
- fehér mennyezet a HF-mezővel (x 3,77–9,80; y 4,05–8,05), ahova nem fúrunk;
- a szürke belső ajtók: szín, hely, fekete kilincs;
- a nyílászárók belül fehérek, a téglakáva sötét;
- a villamos kiállások (TERV SZERINT);
- a terasz: burkolat, WPC, zöldtető, korlát, a valódi panoráma.

**Kamera:**
- a Cam_02 a lock szerint;
- a Cam_12 a PR #17 szerinti JAVASLAT, amíg Péter be nem olvasztja.

**Ülőcsoport és étkező helye:**
- P902_24A;
- S01 Lennon L, S02 JÄTTEBO U;
- más stílusnál L vagy U (CLAUDE.md: minimum L, inkább U), ha a P902_24A befoglalójába fér.

**Minden más szabad,** a kereten belül és megvalósíthatóan: asztalos elemek, panelek, tapéta, mű, függöny, textil, lámpák, styling, LED.

**A tömbképek nem kötelezők:** a V3 r1 tömbképei (`04_renderek/A902_cam02_tomeg_v1/…_V3_v1.png`, `04_renderek/A902_cam02_tomeg_V3TEST/` és a Cam_12 V3-tömbje a PR #17-ben) a régi méreteket mutatják.

### 11.9 A négy prompt formája
**Képenként a kreatív rész:**
- legfeljebb kb. 5000–6000 karakter, pozitív, leíró nyelven;
- ebben a sorrendben:
  1. a kép egymondatos WOW-gondolata;
  2. a fő elemek mérettel, anyaggal és színnel, az elemlista ID-ivel;
  3. a fényjelenet;
  4. a berendezés és a styling teljes listája;
  5. paletta és anyagkontrasztok;
  6. legfeljebb 8 tiltás, csak a bizonyított hibákra.

**A V3-tesztben bizonyított hibák** (ezekre tiltás vagy pozitív előírás kell):
- fizikailag lehetetlen tükörkép (S02);
- világos téglakáva a valódi sötét helyett;
- a valósnál világosabb padló;
- eltérő frontszám (S01: 4 helyett 3);
- padlóig érő tükör;
- a specifikáltnál magasabb falbútor és elcsúszott étkező (`_V3_TEST`): a magasságot és a helyet számmal kell megadni, nem a generátorra hagyni.

**A többit Claude teszi hozzá:**
- a terasz felőli padlósík és az üvegél magasságát a FIXED-blokk kezeli;
- a FIXED-blokkokat (héj, kamera, kiállások, padló) tömörítve;
- a teljes futtatott prompt célja legfeljebb 10–11 ezer karakter.

### 11.10 Költség
**A §9 érvényes.** Stílusonként add meg a nappali–étkező csomagot, fő és gazdaságos változatban. Tartalma:
- fő fal, mű, LED, függöny;
- textil és styling;
- az ML05 lámpatest;
- a konyhafront, mert a Cam_12-n látszik.

Mindkét változatnál mutasd meg:
- mit vált ki (V3 r1 A/B/C, V2 03a);
- mi esik ki a 18 M-ból.

**Viszonyítás – V3 r1 nappali-csomag (Astra-becslés):**
- S01: 740–1040 eFt, gazdaságos 535–740 eFt;
- S02: 855–1160 eFt, gazdaságos 650–860 eFt.

**Konyha:**
- A 18 M „mindennel” értendő, a konyhagépekkel együtt (GOAL §3).
- Konyhabútor nincs, ezért stílusonként külön sor kell: IKEA METOD-váz + front és munkalap; a gépek külön sorban.

A §11.4 becslései nem ellenőrzöttek.

### 11.11 Cam_12 – a hero nézet tényei (PR #17, JAVASLAT)
**Paraméterek:**
- hely [3,95; 7,90; 1,45], 22 mm, shift_y −0,08, vízszintes.
- képek a `kep004/cam12-nappali-hero-javaslat` ágon: alapkép, V3-tömbök, `CAM12_JAVASLAT_v2.md`.
- Más kameraértéket ne találj ki (§10).

**A TV-fal a Cam_12-n nem látszik,** az üvegfal és a terasz sem. A hero WOW-ját ezek adják:
- **W02 + W07:** a W02 a kép jobb közepén, szinte szemből (u 0,54–0,81), a W07 a jobb szélén (u 0,82–0,99);
- **a konyha:** front, munkalap, hátfal, hűtőoszlop a W03-a előtt;
- **a 05.3 ajtó környezete:** az ajtó változatlan, a szemöldöksáv (z 2,10–2,90) kezelhető;
- **az étkező:** az ML04 függesztéke látszik (u 0,21; v 0,05);
- **a kanapé eleje,** dohányzóasztallal és szőnyeggel;
- **az esti fény.**

Az ML05 lámpatest függesztékként a kép felső szélén látszhat; ezt Claude Blenderben vetíti.

**Részletek:** a V3.1-bemenet §1–2 (látható falszakaszok), §4 (LED-mátrix) és §5 (képtéri befoglalók).

### 11.12 A kész munka és a visszaadás
**Új fájlok** (a V2 és a V3 r1 érintetlen):
1. `ai-coordination/results/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r1.md` – a §10 1–10. pontja és a §11 válaszai: WOW-összetevők, a hat eszköz, falhierarchia, fényforgatókönyv, költség- és kockázati tábla, integrációs instrukció Claude-nak.
2. `05_promptok/A902_S01_S02_Cam02_Cam12_CREATIVE_UPGRADE_V3_1_r1.md` – a négy teljes prompt, külön blokkban.
3. `05_promptok/A902_V3_1_elemlista_S01_S02_r1.csv` – a §11.7 szerinti elemlista.

**Átadás:**
- új ág és draft PR;
- a PR-be: `WSG-ASTRA-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1`;
- ha nincs írási jog: az eredmény a Workben marad, `handoff blocked` jelzéssel.

**Önellenőrzés átadás előtt:**
- [ ] A négy kép mindegyike mutatja-e a §0.2 hat összetevője közül legalább az ötöt?
- [ ] Van-e mennyezetig érő vagy közös vonalú fő fal?
- [ ] Teljes-e a berendezési lista?
- [ ] Minden elemnek van-e mérete, forrása és ára?
- [ ] Kiderül-e, mi esik ki a 18 M-ból?

### 11.13 Mi NEM feladat
- képgenerálás;
- Blender-módosítás;
- a V2/V3 r1 fájlok felülírása;
- rendelés, ajánlatkérés;
- a végleges stílus kiválasztása Péter helyett.

---

## B rész – Claude-oldali változtatások (a csomagépítésben, a V3.1 után)
1. **FRAME LAYOUT:** a „Nothing else stands in the room…” mondat helyére a teljes, listázott berendezés kerül; csak a listán kívüli nagy bútor tilos.
2. **Új tömbképek (1b)** a V3.1 elemlistából, a Cam_02-re és a Cam_12-re: mennyezetig érő vagy közös vonalú elemek, függöny, dohányzóasztal, szőnyeg, lámpák, az ML05 lámpatest. Kiindulás a `_V3_TEST` r2-módszere (`03_blender/geometry_v2/tomeg_cam02_v3test/`), amellyel az S02 héja ±1 %-on belül maradt.
3. **Fényblokk nézetenként** (§11.6), ha Péter jóváhagyja.
4. **Rövidebb prompt:** tömörített FIXED, a tiltások a bizonyított hibákra; a cél legfeljebb 10–11 ezer karakter.
5. **Geometria:** az S01-nél (belmagasság kb. +8 % a `_V3_TEST`-ben, a padlósík 10–13,5 % a `_V3_r1`-ben) a végleges futtatás előtt az A0, szerkesztő módú próbakép; Péter „mehet”-jével.
6. **Független ellenőrzés a generálás előtt:** validátor, kiállások, közlekedő, ajtók, termékárak dátummal; eltéréslista.
7. **Gate + WOW-ellenőrzés** a §0.2 hat összetevőjével; a végső ítélet Péteré.
8. **Diagnosztikai lehetőség:** a 66 képes keret K-adagjának első képe – C1 Zenit a Cam_02-n, a valódi héjban, a v1 berendezésével, esti fénnyel – megmutatja, hogy a héj vagy a specifikáció fékez. Csak Péter „mehet”-jével.

## C rész – Péter indító üzenete Astrának (Work, kézzel beillesztve)
> WSG A-902 – Astra Creative Upgrade V3.1. Olvasd el és hajtsd végre a `peterkapusi88-hub/wsg-berendezes` repó `main` ágán: `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1.md`. A §0 és a §11 elsőbbséget élvez a §1–10-zel szemben. Képet ne generálj, Blendert ne módosíts, a V2 és a V3 r1 fájlokat ne írd felül. Az eredmény új ágon, draft PR-ben legyen; a PR-be írd: `WSG-ASTRA-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1`.

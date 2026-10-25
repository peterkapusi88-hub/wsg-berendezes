# WSG A-902 – ASTRA CREATIVE UPGRADE V3.1 – végleges brief (r2)
## Teljes lakásminőség, WOW-korrekció, integrált Hue-világítás és mind a 66 kreatív renderprompt

- **Task ID:** WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1 · **brief-verzió: r2**
- **Érvényes változat:** ez a fájl.
  - Az r1 (`ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1.md`, commit `3d4d0b4`) felülírva, csak visszakövetésre.
- **Cél AI:** ASTRA_WORK (kreatív vezető). **Egyetlen Work-feladat** (Péter, 02:35 CET).
- **Típus:** STYLE_CONCEPT + RENDER_PROMPT (66) + előzetes költség- és műszaki kockázat
- **Lakás, helyiségek:** A-902.
  - Nappali–étkező–konyha: Cam_02, Cam_12, Cam_03.
  - Master 05.1: Cam_04, Cam_11.
  - Fürdő 06.2: Cam_10.
- **Stílusok:** S01–S10, mind teljes részletességgel, valamint a C1 Zenit és a C2 Lake Forest kalibráció.
- **Prioritás:** high
- **Gondolkodási szint:** Medium (kreditszabály, Péter 2026-10-24 19:34).
  - High csak Péter külön engedélyével; Claude javasolja.
  - Ultra/Max nem.
- **Automatikus Work-indítás:** nem. Péter indítja kézzel (C rész).
- **Keret:** A-902 bruttó 18 000 000 Ft tervezhető összeg + 2 000 000 Ft külön tartalék, amelyhez nem nyúlunk.
  - A kb. 1 M Ft-os minőségi többlet csak külön, feltételes forgatókönyvként mutatható (CLAUDE.md).
- **Állapot:** INDÍTÁSRA KÉSZ. Benne van Péter 02:33 CET-es felülvizsgálata, 02:35-ös módosítása (66 prompt) és 02:43-as mentési szabálya (checkpointolás).
  - **Nem engedélyez:** képgenerálást, PR-beolvasztást, rendelést, külső kötelezettségvállalást, a 66 kép automatikus futtatását.
- **Készítette:** Claude, 2026-10-25 02:50 CET.
  - CET; a téli időszámítás 03:00 CEST = 02:00 CET-kor kezdődött.
- **Források:**
  - Péter 02:05, 02:33, 02:35 és 02:43 CET-es üzenetei;
  - a V3.1-kérés Péter által bemásolt szövege (lent, az r2-ben jelölt felülírásokkal);
  - `ai-coordination/requests/WSG-20261025-ASTRA-V3_1_INPUT_Cam12_falak_vilagitas.md`;
  - `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md` és `…_V3_TEST_gate.md`;
  - Astra V3 r1 (PR #16, `be6b1f3`);
  - Astra V2 r1 (`05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md`);
  - a KEP-004 promptsablon v3.1 (`05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md`);
  - a 66 képes regiszter (`05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv`).

**Elsőbbség:**
1. a §11.0 (Péter döntései);
2. a §11 többi része és a §0;
3. Péter V3.1-szövege (§1–10).

Ütközésnél mindig a magasabb szint érvényes. A felülírt mondatok a §1–10-ben áthúzva, **[r2]** jelöléssel szerepelnek.

## Változások az r1-hez képest

### a) Félreértés miatt javítva (Péter 02:33, 1. pont)
| Hely | r1 – téves | r2 – helyes |
|---|---|---|
| §0, „Nem jó” lista | „a »minden fal burkolt« elvet sem látja jónak, főleg a nagy, egybefüggő falakon” | a korábban kért átfogó faltervezést **nem látja megvalósulni a képeken**, főleg a nagy falszakaszokon |
| §0.1, F4 | „Mindenhol ugyanaz a halk fal” → falhierarchia | a kísérőfalak kezelése túl gyenge volt ahhoz, hogy a képen látsszon → teljes faltervezés |
| §11.3 | „Falhierarchia: nem minden fal burkolt”; a többi fal „nyugodt keret: a meglévő fehér fal”; a V3 B-csomag „nem automatikus” | **minden jelentős, látható tömör falnak tudatos belsőépítészeti terve van**; nem alapmegoldás az egy hangsúlyos fal mellett üresen maradó fehér felület |
| GOAL 7. pont (02:05 és 02:30 CET) | ugyanez a téves értelmezés | áthúzva és javítva |

### b) Péter 02:33-as döntései miatt módosítva
- **§11.2 TV-fal:**
  - a mennyezetig futó elem vagy a közös felső vonal preferencia, nem tilalom;
  - a V3 KI3/BN3 forma és magasság nem kötelező;
  - S01-hez és S02-höz három TV-fal-koncepció kell.
- **§11.5 Berendezés:**
  - teljesebb, de nincs kötelező darabszám;
  - a közlekedési és használati méret elsőbbséget élvez;
  - az ML05 vizsgálandó, nem automatikus rögzítési engedély.
- **§11.6 Fény:**
  - az irány elfogadva;
  - a nappali képek maradnak a geometriai kontrollnézetek;
  - a LED-ek műszaki és költségellenőrzése kötelező.
- **§11.7 Elemlista:** méret, falazonosító és elhelyezési szándék kell; modellkoordináta nem, azt Claude rendeli hozzá.
- **§11.8 Elrendezés:**
  - a P902_24A nem megváltoztathatatlan, a 0,36–0,38 m nem elfogadható;
  - Claude 2–3 alternatívát vizsgál;
  - a +15 cm-es eltolás nincs jóváhagyva.
- **§11.9 Prompt:** a rövidítés cél, nem karakterplafon.
- **§11.10 Költség:**
  - a gazdaságos gyártástechnológia az alap, de a látvány nem romlik;
  - a BiBo navy laminált front az alap, festett MDF csak külön jóváhagyással;
  - a kiváltott tételeket tételesen kell kimutatni.
- **§11.12 Önellenőrzés:** helyiség és stílus szintjén, nem kivágásonként.
- **Kamerák és PR-ek:**
  - PR #16 és PR #17 kreatív forrás, merge nincs;
  - a Cam_03 új, konyhaorientált javaslatot kap;
  - nincs új S01 geometriai próba.

### c) Péter 02:35-ös módosítása miatt módosítva
- **A kimenet mind a 66 teljes kreatív prompt**, nem négy: 10 stílus × 6 kamera + 6 kalibráció (§11.12).
- **Felülírva** a „csak négy teljes prompt” és az „S03–S10-hez ne készíts további promptot” utasítás (a §1–10-ben áthúzva).
- **Új:**
  - moduláris munkarend (§11.9);
  - nézetek közötti azonosság (§11.8);
  - verziózott GitHub-kimenet manifesttel és 66/66-os teljességi ellenőrzéssel (§11.12).

### d) Péter 02:43-as kiegészítése miatt módosítva
- **Kötelező, folyamatos GitHub-checkpointolás** (§11.12):
  - CP0: alapok + 66 tételes manifest;
  - CP1: a tíz stílus-specifikáció;
  - CP2: S01/S02, előbb a négy kiemelt prompt;
  - utána stílusonként, legfeljebb 6–10 promptonként commit és push.
- **A manifest státuszai:**
  - `statusz`: PENDING, DRAFT, COMPLETE;
  - `validalas`: NEEDS_CLAUDE_VALIDATION;
  - a teljes kreatív prompt nem azonos a Claude által validált futtatási csomaggal.
- **Csak a távoli GitHubon igazolt commit számít mentésnek.**
- **Megszakításnál** folytatható a manifestből; a kész részeket nem kell újraírni.
- **A C részbe** bekerült a folytató üzenet.

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
- **a korábban kért átfogó faltervezés nem látszik megvalósulni a képeken, főleg a nagy falszakaszokon** *(r2: javítva, Péter 02:33)*;
- az első Zenit/Lake Forest képek még mindig a legjobbak, csak ott semmiről nem tudjuk, mi az és mennyibe kerül;
- kérdése: nem korlátozza-e túl a Blender a formavilágot?

**A képek** (mind a négy ugyanazt az Astra V3 r1 tartalmat mutatja):
- **`_V3_r1`** (Claude, Péter 02:06 CEST):
  - helye: `04_renderek/ai_chatgpt/STYLE10_KEP004/CREATIVE_UPGRADE_V3/`;
  - audit: `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md`;
  - eredmény: a terasz felőli padlósík 10–13,5 %-kal eltér, FAIL.
- **`_V3_TEST`** (a második Claude-munkamenet, Péter 02:22 CEST, r2-csomag javított tömbképpel):
  - helye: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/`;
  - audit: `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`;
  - S02: a héj ±1 %-on belül, `ELŐSZŰRT – FELTÉTELES`;
  - S01: a belmagasság kb. +8 %, FAIL;
  - mindkettőn magasabb a falbútor a specifikáltnál (magas szekrény ≈2,45 m, alsó ≈0,65 m), és keletebbre csúszott az étkező.

### 0.1 Claude diagnózisa: mi fékezte a képeket
Forrás: a ténylegesen futtatott V3-teszt promptok, `05_promptok/KEP004_ChatGPT_Images_V3_teszt/`.

A Blender három dolgot rögzített: a héjat, a kamerát, valamint a kanapé és az étkező helyét. A többi féket a saját szabályaink okozták:

| # | Fék | Bizonyíték | Mi változik |
|---|---|---|---|
| F1 | **Fény** | „neutral overcast daylight, no sun … no warm grading, haze or bloom … Luxury must come … not from warmer light” (KEP-004 promptsablon v3.1 §1). Hozzá a teszt saját fénybekezdése: csak a meglévő pontok, nincs LED. | §11.6: kameránkénti fényforgatókönyv |
| F2 | **Üres szoba** | „Nothing else stands in the room: no coffee table, side table, floor or table lamp, sideboard or extra seating” (Claude FRAME LAYOUT). „Keep the middle of the room free; do not add a coffee table” (V3 r1). „the living point ML05 … carries no fixture”. A függöny, a díszpárna és a pléd egyszer sem szerepelt. | §11.5: teljesebb berendezés, ahol elfér |
| F3 | **Arányok** | S01: KI3-L 48 cm magas; KI3-V 220 cm; KI3-P z 0,55–2,45. S02: BN3-P z 0,55–2,45; BN3-R z 0,40–2,20. A belmagasság 2,90 m: három különböző felső vonal, egyik sem ér a mennyezetig. | §11.2: szabadabb TV-fal, mennyezetig érő vagy tudatosan komponált magasságok |
| F4 | **A kísérőfalak kezelése nem látszik** *(r2)* | „The wallpaper is a low-contrast fine texture”, a W01–W04 kísérőfelületein (14–18 m²). Képi léptékben fehér falnak hat, így a kért teljes faltervezés nem jelenik meg. | §11.3: minden jelentős, látható tömör fal tudatos, a képen is olvasható tervet kap |
| F5 | **Kicsi gesztus** | A mű 100×180 (S01) és 120×160 cm (S02); a TV-fal egyetlen sík panel | §11.4: Péter hat eszköze, nagyobb lépték |
| F6 | **A prompt formája** | Kb. 19 000 karakter, kb. 77–79 tiltó kifejezés (no, not, never, without…). A szürke tömbkép (1b) a V3 r1 rövid dobozait mutatta, és a képek ezt az arányrendszert követték. | §11.7–11.9 és a B rész |

**Következtetés:**
- **A geometria már kezelhető:** az S02 `_V3_TEST` héja ±1 %-on belül van, a WOW mégis hiányzik. A szűk keresztmetszet tehát a specifikáció, a berendezés és a fény.
- **A Blendert nem kell elengedni.** Nélküle a v1-hez hasonlóan nem létező lakás jönne vissza: a valóditól eltérő panoráma, kitalált nyílások, mennyezeti fénycsík, kiállás nélküli csillár, valódinak mutatott kő.
- **A sorrendet fordítjuk meg:**
  1. Astra kreatív koncepciója, szabadon a rögzített héjon belül;
  2. Claude Blender-validálása és független áraudita;
  3. végül a ChatGPT Images.
- **A régi tömbök nem kötelező befoglalók:** sem a V3 r1 tömbjei, sem a P902_24A bútortömbjei.

### 0.2 A WOW-mérce: a v1 Zenit és Lake Forest
**Fájlok:**
- `04_renderek/ai_chatgpt/A902_Zenit_1_nappali_chatgpt.png`, `…_2_etkezo_konyha_chatgpt.png`, `…_3_master_chatgpt.png`;
- `04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png`, `…_2_…`, `…_3_…`.
- Státuszuk `KONCEPCIÓ – NEM VALIDÁLT`, a geometriájuk nem a lakásé.

**A hat erősség, amit át kell venni (az érzetet):**
1. **Rétegzett, meleg fény:** alkonyat vagy kék óra belső fényekkel (Zenit); lágy, világos nappal, átsütő áttetsző függönnyel (Lake Forest).
2. **Padlótól mennyezetig futó függőleges elemek:** függöny; bordázott, LED-del súrolt TV-fal (Zenit).
3. **Teljes textil és styling:** nagy szőnyeg, párnák, pléd, dohányzóasztal, kisasztal, álló- és asztali lámpa, nagy növény, tárgycsoportok.
4. **Egy nagy, karakteres mű:** nagy texturált relief (Lake Forest), vagy egységes képsor (Zenit).
5. **Erős anyagkontraszt:** meleg fa, bouclé és szövet, fém; matt és selyemfényű felületek.
6. **Látványos lámpatest a nappali mennyezeti pontján:** Zenitnél gyűrű, Lake Forestnél gömbcsillár. Nálunk ez az ML05 meglévő, terv szerinti pont, vizsgálattal (§11.5).

**Ezt ne vedd át:**
- a valóditól eltérő panoráma (pl. Parlament) és kitalált nyílások;
- mennyezeti fénycsík, álmennyezet;
- lámpa kiállás nélkül;
- valódinak mutatott kő;
- nem létező fülke.

**Értékelés:** stílusonként, a helyiség egészére írd le, melyik erősséget hogyan valósítod meg, valós termékkel, mérettel és bruttó árral. Nem kell mind a hatnak minden kivágásban látszania.

---

## Péter V3.1-szövege (2026-10-25 02:05 CET) – az r2-ben felülírt mondatok áthúzva, [r2] jelöléssel
- Minden más szó szerint.
- Az eredeti, változtatás nélküli szöveg az r1-ben van: sha256 `577ee52f009964c296e01bb91ed8f5169711c45cb39303f3ec45d1d97b92c1c1`.
- A cím a fájl címe.

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

**[r2 – Péter 02:33: a stílusok identitása marad, de a V3-elemek formája és magassága nem kötelező; a TV-falhoz három koncepció kell (§11.1–11.2).]**

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
3. Az S01 Kyoto Ink és S02 BiBo Nocturne esetén dolgozz ki pontos, kreatív V3.1 világítási módosítást a meglévő Cam_02 promptokhoz, valamint alkalmazási elvet az új hero kamerához. **[r2: ez a 66 teljes prompt része, §11.12.]**
4. ~~A többi nyolc stílusnál egyelőre stratégiai szinten dolgozz, hogy ne készítsünk fölöslegesen 66 új részletes promptot az első teszt előtt.~~ **[r2 – felülírva, Péter 02:35: mind a tíz stílus teljes részletességgel, és mind a 66 teljes prompt, §11.12.]**
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
~~Készíts négy TELJES, részletes, angol nyelvű V3.1 kreatív renderpromptot:~~ **[r2 – Péter 02:35: a kimenet pontosan 66 önálló prompt (§11.12); az alábbi négy a különösen részletes mintaprompt, és ezek készülnek el elsőként (CP2):]**
1. S01 Kyoto Ink – nappali–terasz, Cam_02.
2. S02 BiBo Nocturne – nappali–terasz, Cam_02.
3. S01 Kyoto Ink – második nappali hero kamera, a TV-fal irányából.
4. S02 BiBo Nocturne – második nappali hero kamera, a TV-fal irányából.
Mind a ~~négy~~ **[r2: 66]** prompt egységesen tartalmazza, a nézetre értelmezve:
- a korábbi Astra V2-ből megtartott, pontosan azonosított bútorokat;
- a Creative Upgrade V3-ban kialakított teljes fal-, burkolat- és integrált tárolókoncepciót;
- a karakteres, emlékezetes WOW-elemeket;
- az új, kiemelt rejtett LED- és Hue-világítási koncepciót;
- a megfelelő kanapétípust (Kyoto: L, BiBo: U) **[r2: a többi stílusnál a saját L- vagy U-megoldását]**;
- a tényleges kameranézetből látható kompozíciót;
- a valós geometriára, villamos kiállásokra és meglévő felületekre vonatkozó korlátokat;
- a listán kívüli bútorok és kitalált fényforrások tiltását;
- a választott fő anyagváltozatot, valamint külön gazdaságos alternatívát.
Ne pusztán LED-sorokat fűzz a V3 végére. A kreatív utasításokat teljes egészükben szerkeszd újra, hogy ne legyen köztük ellentmondás.
A Cam_02-höz már elkészült Claude geometriai v2 blokkja. Ezt használd kreatív referenciaként.
Az új hero kamera pontos Blender-pozícióját Claude véglegesíti. A hozzá készülő promptok legyenek teljes kreatív tartalmúak, de a még nem igazolt kamerageometriát jelöld integrálásra váró adatként; ne találj ki kameraértékeket.
Kimeneti követelmény: a ~~négy~~ **[r2: 66]** új kreatív prompt külön-külön legyen átadható Claude-nak, aki a végleges FIXED blokkokkal, referenciákkal és ellenőrzött geometriával teljes, futtatható ChatGPT Images-csomagot készít belőlük.
~~A további nyolc stílushoz most csak a tízstílusos V3.1 világítási és anyagstratégiát készítsd el. A teljes 66 képes sorozat további promptjait az első sikeres képteszt után dolgozzuk ki.~~ **[r2 – felülírva, Péter 02:35: mind a 66 teljes prompt most, egyetlen Work-feladatban, checkpointolva (§11.12).]**
Az A-902 18 millió Ft-os bruttó berendezési célkerete és a 2 millió Ft-os tartalék változatlan. A V3.1-ben szereplő világítás és falkezelés költségét is számold.
Az eredeti V2 és V3 fájlokat ne írd felül. Az új promptok külön V3.1 fájlokba kerüljenek GitHubon.
Ne indíts képgenerálást vagy Blender-módosítást.

---

## 11. KIEGÉSZÍTÉS (r2) – kötelező, elsőbbséget élvez

### 11.0 Péter döntései (2026-10-25 02:33 és 02:35 CET) – minden más pont előtt érvényesek
| Kérdés | Döntés |
|---|---|
| PR #16 – Astra V3 | Maradjon meg verziózott kreatív forrásként; egyelőre ne tekintsük véglegesnek. |
| PR #17 – Cam_12 | Az ÉNy-i, 22 mm-es irány tetszik. Kreatív alapként használható, de a PR beolvasztását még ne engedélyezzük a végleges ellenőrzés előtt. |
| Cam_03 | Legyen inkább konyhaorientált, ne szinte ugyanaz, mint a Cam_12. |
| Újabb S01 geometriai teszt | Most ne. Előbb valódi kreatív áttörést szeretnénk látni. |
| Kanapé–szék közlekedő | A 36–38 cm nem megfelelő végleges közlekedési megoldás. Claude vizsgáljon több alternatívát; a +15 cm önmagában kevés. |
| W02 + W07 | Igen, ez a hálókhoz vezető összekötő falszakasz, egyetlen átfogó belsőépítészeti kompozícióként. |
| BiBo festett MDF | Navy laminált legyen a költséghatékony alap. Festett front csak külön indoklással és jóváhagyással. |
| Fő vagy gazdaságos falcsomag | A gazdaságos gyártástechnológia legyen az alap, de a látvány színvonala ne romoljon. |
| Rejtett LED | Magas prioritás, Hue-kompatibilitással; a szekrénybelső funkcionális világítás kivétel. |
| Nappali mennyezeti lámpa | A meglévő ML05 terv szerinti pont használata vizsgálandó, nem automatikus rögzítési engedély. |
| Képsorozat | 66 tervezett kép, fokozatos generálás. A nappali és esti nézetek egyező szabályrendszer alapján készüljenek. |
| Költség | 18 M Ft bruttó tervezhető összeg, 2 M Ft külön tartalék. Minden új csomag teljes bekerülését és a kiváltott tételeket is számolni kell. |
| **Mentés (02:43)** | Kötelező, folyamatos GitHub-checkpointolás: CP0 alapok → CP1 tíz stílus-specifikáció → CP2 S01/S02 (előbb a négy kiemelt prompt) → stílusonként, legfeljebb 6–10 promptonként commit és push. A manifest minden checkpointnál frissül. Csak a távoli GitHubon igazolt commit számít mentésnek. Tilos egyetlen záró nagy commit, és tilos hiányos promptot késznek jelölni. GitHub-akadálynál azonnali jelzés. |
| **Prompt-kimenet (02:35)** | **Mind a 66 teljes kreatív renderprompt egyetlen Work-feladatban:** 60 fő prompt (10 stílus × 6 kamera) + 6 Zenit/Lake Forest kalibráció, a benchmark-terv szerinti nézetekkel; a kalibrációk az S06/S07 teljes, újratervezett stílusain felül, nem azok helyett. |

**Sorrend:** Astra kreatív koncepciója → Claude Blender-validálása és független áraudita → ChatGPT Images. A képgenerálás nem helyettesíti sem a kreatív tervezést, sem a műszaki ellenőrzést (Péter 02:33).

### 11.1 Stílusidentitás – mi marad, mi szabad
**A V3 r1 falstratégiái (§5) és a V2 r1 stílusai kreatív alapként megmaradnak.** Az elemek formája, magassága és léptéke szabadon továbbfejleszthető (Péter 02:33, 2. pont).

**S01 Kyoto Ink – identitás:**
- grafit „tintavonal”, papírrost-hatás, monumentális tusgrafika;
- termékek: Lennon L (P14), Toni (P09), 6 db Eamy, Nifelia szőnyeg, Somar Ø76 az ML04-en.

**S02 BiBo Nocturne – identitás:**
- mélykék tárolófal, keskeny valódi tükörsáv, ezüstszürke textilhatás;
- termékek: JÄTTEBO U (P04), Anouk (P08), 6 db Ciselia, Brisia Ø50 az ML04-en;
- a front **navy laminált** a költséghatékony alap; festett MDF csak külön indoklással és Péter jóváhagyásával.

**S03–S10, C1, C2:** a V2 r1 és a V3 r1 §5 stílus-DNS-e a kiindulás, a §11.2–11.10 szerinti teljes szinten.

**A §6 V3-elemei kiindulási ötletek, nem kötelező formák.** Ezek: 240 cm-es alacsony médiatároló, keskeny magas szekrény, rétegzett panelek.

### 11.2 TV-fal (W01) – több formai szabadság
**Tények (TERV SZERINT):**
- **W01 nappali felőli síkja:** x 3,67; y 4,05–8,05 (4,00 m hosszú).
- **Belmagasság:** 2,90 m a modellben; mért 2,90–2,93 m (Kémeri, 2026-10-21).
- **Kiállások a W01-en:**
  - D16/D17 (y 6,45 / 6,25);
  - G01–G04 (y 6,03–6,52), G08 (y 6,05);
  - D18 (y 4,75);
  - FL02 fali lámpakiállás (y 7,85; z 2,85).
- **Mennyezet:** a hűtő-fűtő HF03 mező x 3,77-nél kezdődik, kb. 10 cm-re a falsíktól.

**Szabadság:**
- Tervezhető mennyezetig futó, aszimmetrikus, több mélységi rétegből álló, integrált szekrény- és panelrendszer.
- A V3 KI3/BN3 forma és magasság nem kötelező.

**Preferencia, nem tilalom:**
- Padlótól mennyezetig futó kompozíció, a mennyezet alatt 10–20 mm-es árnyékfugával, falra rögzítve.
- Vagy egyetlen közös felső vonal, például az üvegfal szemöldökének alsó éle (z ≈ 2,53 m).
- Tudatosan komponált, eltérő magasságú elemek is jöhetnek, ha az összhatás erősebb.
- Kerülendő a véletlenszerű, egymáshoz nem igazodó magasság, mint a V3-tesztben.

**Koncepciók:**
- **S01 és S02:** stílusonként **három érdemben eltérő** TV-fal-koncepció, közülük egy javasolt főváltozat, indoklással. A promptok a főváltozatot mutatják.
- **S03–S10:** stílusonként egy kidolgozott TV-fal-koncepció.

**Műszaki keret:**
- **Mennyezetig érő zárt szekrénytest:** legfeljebb 60 cm mély. A teteje és a HF-mező kapcsolata **FELTÉTELES – CLAUDE AUDIT SZÜKSÉGES**: szellőzés, páralecsapódás, a mező hatásfoka, hozzáférés.
- **Legfeljebb 4 cm-es panel és burkolat** árnyékfugával felmehet a mennyezetig. A teteje még a HF-mező előtt van (x 3,67–3,71), a 60 cm-es szekrényé már alatta (x 3,67–4,27).
- **Szerviz:**
  - a D16/D17 és a G-pontok hozzáférhetők;
  - a D18-hoz szervizkivágás kell;
  - a TV saját teherhordó tartón áll.
- **A sarok szabadon marad:** x < 4,40 és y > 7,70 között ne legyen magas szekrény, mert ott áll a Cam_12.
- **Változatlan:** a falak, nyílászárók, a mennyezeti rendszer, a parketta és a villamos adottságok.

### 11.3 Teljes faltervezés – minden jelentős, látható tömör falnak legyen terve (r2 – javítva)
**Péter, 02:33:** minden jelentős, látható tömör falnak legyen tudatos belsőépítészeti terve.
- **Ez nem jelenti,** hogy minden fal teljes felületén fizikai burkolat kell.
- **Eszközök:** tapéta, dekorpanel, nyomtatott grafika, integrált tároló, karakteres nagyméretű mű, textil, strukturált felület, megvalósítható rejtett fény.
- **Nem alapmegoldás,** hogy egyetlen hangsúlyos fal mellett a többi nagy felület üres fehér marad.
- **A főfal és a kísérőfalak erőssége eltérhet,** de az összkép legyen következetesen prémium, és a képen is olvasható. A V3 halk kísérőtapétája képi léptékben fehér falnak hatott.

**Kifejezetten tervezendő** (falazonosítóval; források: V3.1-bemenet §2, V3 r1 §5, a promptsablon v3.1 §2):

| Felület | Hol (TERV SZERINT) | Kamera | Megkötés |
|---|---|---|---|
| **W01 TV-fal** | x 3,67; y 4,05–8,05 | Cam_02 | §11.2 |
| **W02 + W07 összekötő fal** – egyetlen kompozíció (Péter 02:33) | W02: a nappali déli fala, y 4,05; x 5,20–7,30 (2,10 × 2,90 m). W07: a hálókhoz vezető közlekedő torka (az x 5,20-as visszafordulás, a pillér, a közlekedő déli fala) | Cam_12 | A közlekedőben legfeljebb 2–3 cm-es kezelés. A kapcsolóoszlop (x 7,149: K10–K12, T01, S01, D19) körül 10–15 cm szabad. A K25–K27 + D46 szabad. Mélyebb rendszer csak a W02 nappali síkján. |
| **A 05.3 szürke ajtó környezete** | W03, y 6,05–6,95; szemöldöksáv z 2,10–2,90 | Cam_12, Cam_03 | Az ajtó, a tok, a kilincs és a szín változatlan. |
| **Az étkező fala (W03-a)** | x 10,75; y 5,05–6,05 | Cam_12, Cam_03 | Hűtőhely (D13). A K07–K09 + D12 szabad. A hűtőoszloppal és a magasszekrénnyel együtt tervezendő. |
| **Konyha: K-csonk és K-pultfal** | x 10,55; y 1,35–5,05 | Cam_12, Cam_03 | Konyhabútor nincs: front, munkalap, hátfal stílusonként. A pult mögött csak tisztítható, konyhai anyag. |
| **Homlokzati tömör mezők (W04)** | a teraszüveg körüli pillérek és szemöldök | Cam_02 | Keret, redőny-szervizfedél, tömítés szabad; tokot nem burkolunk. |
| **Master 05.1** | a fejvégfal (keleti fal); az északi fülke teljes gardróbfala (kötelező, Péter 2026-10-24 22:37); a déli gardróbsáv az ajtónál | Cam_04, Cam_11 | A D20–D23, a K13/K14 és a D26 szabad. |
| **Fürdő 06.2** | a burkolt falak maradnak; tükörkompozíció, tároló, textil | Cam_10 | Nincs új burkolat. |

**Költség:** a kísérőfalak kezelése (a V3 r1 B csomagjának megfelelője) a terv része. Falanként kell mutatni, fő és gazdaságos változatban.

### 11.4 Péter hat eszköze – kötelezően vizsgálandó
A költségek Péter 02:05 CET-es üzenetéből valók: forrás nélküli becslések. Astra saját forrással árazza, Claude függetlenül ellenőrzi.

| # | Eszköz | Változatok | Becsült bruttó ár | Mit ad |
|---|---|---|---|---|
| 1 | **Teljes TV-fal tapéta vagy dekorpanel** | textilhatású prémium tapéta; japán- vagy lenvászonhatású falburkolat; finoman bordázott vagy paneles MDF/melamin; nagy mintás, de nyugodt falpanel | tapéta + felrakás 80–250 eFt/fal; egyszerű dekorpanel, lamella vagy bútorlap 150–400 eFt/fal; egyedi asztalos TV-fal 350–900 eFt+ | azonnal karaktert ad; a TV kevésbé „fekete lyuk” |
| 2 | **TV-tároló kompozíció** | alacsony konzol + két oldalt keskeny, magas zárt elem + fölötte panel/tapéta; vagy aszimmetrikus, lebegő polcos–zárt kombináció | egyszerűbb asztalos vagy standard rendszer 250–600 eFt; komolyabb egyedi 0,7–1,5 M Ft | „standard alsó bútor + nagyon erős háttérfal + 1–2 egyedi elem”: sokkal olcsóbb, majdnem ugyanaz a látvány |
| 3 | **Nagy, karakteres egyedi print vagy vászon** | absztrakt; japános vagy tusfestéses; textilre nyomott; semleges, de nagyvonalú | nagy print/vászon 40–180 eFt; prémium keretezéssel 100–300 eFt | gyakran jobban emeli a drága érzetet, mint egy drága bútor |
| 4 | **Szélesebb, teljesebb, texturált kárpitozott panel** | a TV-falon vagy egy másik fal nagyobb részén; a hálóban is | egyszerű kárpitozott panel 100–300 eFt; nagyobb egyedi rendszer 300–700 eFt | luxusérzet |
| 5 | **„Titkos fegyver”** | jó minőségű melamin, dekor MDF, nyomott panel, tapétázott bútorfront | 120–350 eFt/falrész | látványban gyakran többet ad, mint amennyibe kerül |
| 6 | **Grafikus vagy mintás tárolófrontok** | semleges textilhatás, finom japános grafika, festményszerű front, matt, puha tónusú minta | a 2. és az 5. sorral együtt árazandó | sok tároló „gardróbszekrény-érzet” nélkül |

**Követelmény:**
- **S01 és S02:** a három TV-fal-koncepció és a falterv együtt legalább hármat használjon láthatóan; mindegyikről egy sor indoklás.
- **S03–S10:** a stílus-specifikációban jelöld, melyiket használod és hol.

### 11.5 Teljesebb berendezés – ahol valóban elfér (r2)
**Visszatér:** függöny, párna, pléd, dohányzóasztal vagy puff, kisasztal, lámpák, nagy műalkotások, személyesebb dekoráció.
- **Nincs kötelező darabszám:** stílusonként a koncepcióhoz és a helyhez igazodva.
- **A valódi közlekedési és használati méretek elsőbbséget élveznek.** A projekt szabálya (promptsablon v3.1 §1):
  - a fő közlekedő legalább 90 cm; 75 cm-es mellékút csak az étkezőasztal terasz felőli oldalán;
  - kanapé és dohányzóasztal között 45–50 cm;
  - 90 cm a szék kihúzásához;
  - 60 cm az ágy mellett;
  - az ajtók szabadon nyílnak.
  - Claude ellenőrzi.
- **ML05** (x 5,62; y 6,27; meglévő, terv szerinti mennyezeti kiállás):
  - karakteres, Hue-kompatibilis lámpatest tervezhető;
  - a tényleges helyszíni kiállás, a rögzítés és a HF-mezővel való kapcsolat ellenőrzendő;
  - **nem automatikus rögzítési engedély**;
  - más mennyezeti fúrás nincs.
- **Függöny:**
  - sín vagy karnis falra szerelve, a szemöldök belső síkján (nappali: y 8,05; z 2,53–2,90; master: a 0,33 m-es falsáv az üveg fölött);
  - az R01/R02 redőny szervizfedele szabad marad;
  - a mennyezetbe nem fúrunk;
  - az S02 U északi vége 0,225 m-re van az üvegtől: ott vékony függöny, vagy az elrendezési alternatíva oldja meg (§11.8).
- **Teljes lista:** listán kívüli nagy bútor nem kerülhet a képre, ezért a stílus saját listája legyen teljes. Ez vonatkozik a nappali–étkező–konyhára, a masterre és a fürdőre is.

### 11.6 Fény és Hue – kameránkénti forgatókönyv (elfogadva, Péter 02:33)
| Kamera | Fényforgatókönyv | Szerep |
|---|---|---|
| **Cam_02** nappali–terasz | világos, természetes nappali fény; a terv szerint északi homlokzat, nincs napfolt; tiszta vagy enyhén felhős ég; a LED-ek és lámpák visszafogottan | **geometriai kontrollnézet** |
| **Cam_12** nappali hero | karakteres kék óra / kora este, rétegzett Hue-világítás, 2200–2700 K, RGB nélkül | hangulatkép |
| **Cam_03** konyha–étkező | nappali fény; a konyhai pult- és szekrényfény visszafogottan | kontroll és konyharészlet |
| **Cam_04** master | kora este: Hue-jelenet, fejvégfény, olvasólámpák | hangulatkép |
| **Cam_11** master panoráma | nappali fény, a valódi panoráma | **geometriai kontrollnézet** a masterhez |
| **Cam_10** fürdő 06.2 | csak műfény, a meglévő pontokról; ablaktalan, nincs kitalált nappali fény | – |

- A Cam_03, Cam_04 és Cam_11 fénye Claude alapjavaslata. Ha Péter másként dönt, Claude a csomagépítésnél cseréli.
- **Azonos szabályok:** minden stílus és kalibráció ugyanabban a kamera–fény forgatókönyvben, azonos szabályrendszerrel készül, a nappali és az esti nézetek is (Péter: „Képsorozat”).
- **Az esti képeken is olvashatók maradnak** a falélek, a nyílások és a padló–fal vonal; nincs bebukó fekete. A Gate a Blender-alapképpel veti össze.
- **Hue:** minden általános és dekoratív fény Philips Hue-integrálható. Kivétel a szekrénybelső funkcionális fény.
- **A rejtett LED magas prioritás.** Kötelező műszaki és költségellenőrzés:
  - profil, diffúzor, tápegység, vezérlő, kábelút;
  - ahol a táp nem igazolt: **FELTÉTELES – CLAUDE VILLAMOS AUDIT SZÜKSÉGES**;
  - a kiállás-mátrix: V3.1-bemenet §4.
- **Fény és áram csak a meglévő pontokról:**
  - nappali: ML04, ML05, FL01, FL02, D-pontok;
  - master: ML06, D20–D23, D26;
  - fürdő: a mennyezeti pont és a mosdó feletti pont.

### 11.7 Méretezett elemlista (r2)
**Astra minden új vagy megváltozott elemhez megadja:**
- ID;
- falazonosító vagy hely (W01, W02, „ülőcsoport”, „étkező”, „05.1 fejvégfal”…);
- **elhelyezési szándék** szavakkal, például „a W01 közepén, a TV-tengelyre szimmetrikusan, padlótól mennyezetig”;
- szélesség × magasság × mélység;
- anyag vagy termék (cikkszám, link, dátum);
- rögzítés;
- táp (melyik meglévő pontról, vagy nincs);
- fő és gazdaságos bruttó ár;
- státusz (becslés vagy ellenőrzött).

**Modellkoordinátát nem kell megadni és nem kell kitalálni.** Claude rendeli hozzá és ellenőrzi.

**Részletesség:**
- **S01 és S02:** minden elem (mindhárom TV-fal-koncepció, falak, konyha, master, fürdő, textil, lámpák, LED).
- **S03–S10, C1, C2:** a fő elemek (TV-fal, falkezelések, kanapé, étkező, konyhafront, ágy és fejvég, gardróbfront, fürdőkiegészítők, lámpák, LED, függöny, szőnyeg, mű).

**Claude ebből:**
- koordinátákat rendel hozzá;
- új Blender-tömböt (1b) készít;
- validátort futtat;
- ellenőrzi a kiállásokat, a közlekedőt, az ajtólendületet és az árakat;
- az eltéréseket a generálás előtt jelzi.

### 11.8 Rögzített héj, felülvizsgálható elrendezés, nézetek közötti azonosság (r2)
**Változatlan építészet:**
- falak, nyílások, üvegfalak és szemöldökök;
- belmagasság 2,90 m;
- a meglévő szürke tölgy padló (pontos dekorja NEM IGAZOLT);
- fehér mennyezet a hűtő-fűtő mezőkkel, ahova nem fúrunk;
- szürke belső ajtók (szín, hely, fekete kilincs);
- a nyílászárók belül fehérek, a téglakáva sötét;
- villamos kiállások (TERV SZERINT);
- a terasz (burkolat, WPC, zöldtető, korlát) és a valódi panoráma;
- a fürdő 06.2 teljes beépített állapota (`05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md`).

**Elrendezés – felülvizsgálható (Péter 02:33, 5. pont):**
- **A P902_24A a jelenlegi referencia,** nem olyan megváltoztathatatlan, mint az építészet.
- **A kanapé–étkező közlekedő 0,36–0,38 m:** nem elfogadható végleges megoldás. A +15 cm-es keleti eltolás nincs jóváhagyva.
- **Claude 2–3 valódi, használható alternatívát vizsgál:**
  - hat étkezőhely, székmozgatási tér, használható konyhai hozzáférés;
  - valós termékmérettel igazolva, költségkülönbséggel;
  - fájl: `ai-coordination/results/WSG-20261025-A902-ELRENDEZES-ALT_r1.md` (készül; Péter választ).
- **Kiindulópont:** S01 Lennon L, S02 JÄTTEBO U.
- **A többi stílusnál** különböző L- vagy U-megoldás (CLAUDE.md: minimum L, inkább U), ha a nyugati TV-fallal és a közlekedési méretekkel elfér.
- **Astra feladata:**
  - A falterv, a TV-fal, a konyha, a master, a fürdő, a fény és az anyagok nem függenek az étkező pontos helyétől.
  - A nappali–étkező kapcsolatát minőségi kapcsolatként írd le („az étkezőcsoport a konyha felé, a kanapé hátától tisztes távolságra”), ne képszázalékkal.
  - A pontos képtéri helyet Claude a választott alternatívával adja hozzá a futtatási csomagokban.

**Nézetek közötti azonosság (Péter 02:35):**
- **Stílusonként egyetlen** nappali–étkező–konyha terv: a Cam_02, a Cam_12 és a Cam_03 ugyanazt a bútort, falat, anyagot és fényt mutatja.
- **Egyetlen master-terv:** a Cam_04 és a Cam_11 ugyanazt az ágyat (180×200, tengely y 6,40), gardróbot és berendezést mutatja.
- **Anyag- és termékazonosság:** ugyanaz a termék minden nézetben ugyanazzal a névvel, mérettel és színnel szerepel.

### 11.9 A 66 prompt formája és moduláris munkarend (r2)
**Moduláris felépítés (Péter 02:35):**
1. **10 részletes, egységes stílus- és helyiség-specifikáció** (S01–S10), a C1/C2 kalibrációs koncepció-cellákkal. Minden specifikáció ugyanazt a szerkezetet követi:
   - stílus-DNS;
   - nappali–étkező–konyha terv;
   - master;
   - fürdő 06.2;
   - termék- és elemlista;
   - fény;
   - költség.
2. **Kamera- és helyiség-specifikus kompozíciós leírások:** a hat kamerára és a kalibrációs nézetekre (§11.11).
3. **Közös, újrahasználható Reality/FIXED-elvek**, angolul, tömören:
   - **Átveendő a sablon v3.1 §1-éből:** geometria és kamera, meglévő felületek, őszinte anyagnevek, közlekedési méretek.
   - **Nem átveendő, felülírva:**
     - a „Walls and ceilings: painted white” mondat helyett a stílus falterve (a mennyezet fehér marad);
     - a „Light and grading – Series A neutral overcast…” szabály helyett a §11.6.
4. **Ezekből összeállított 66 önálló kreatív prompt.**

**Minden prompt önálló:** önmagában tartalmazza
- a stílus-DNS-t;
- a helyiség tervét;
- a kamera kompozícióját;
- a fényt;
- a berendezést és a stylingot;
- az anyagokat;
- a tömör reality-részt.

**Tilos:**
- „lásd az előző promptot”, „same as above”, helykitöltő vagy hiányos vázlat;
- 66 közel azonos szöveg. Minden prompt stílus- és nézetspecifikus.

**Hossz – irányérték, nem plafon:**
- a négy mintaprompt (S01/S02 × Cam_02/Cam_12) különösen részletes, kb. 5–7 ezer karakter;
- a többi 62 teljes értékű, kb. 3–5 ezer karakter.
- A rövidítés cél, de a műszaki szükségletek nem vesznek el: héj, kiállások, padló, ajtók, nyílászárók, Hue, bizonyított hibák.

**Kevesebb tiltás:** pozitív, leíró nyelv; képenként legfeljebb kb. 8 tiltás, a bizonyított hibákra:
- fizikailag lehetetlen tükörkép;
- világos téglakáva a valódi sötét helyett;
- a valósnál világosabb padló;
- eltérő frontszám;
- padlóig érő tükör;
- a specifikáltnál magasabb vagy elcsúszott bútor (a magasságot számmal kell megadni).

**Claude a futtatási csomagban** hozzáteszi a Blenderből ellenőrzött FIXED- és FRAME LAYOUT-blokkot, és szükség esetén ezzel cseréli a prompt reality-részét.

### 11.10 Költség (r2)
**Keret:** a §9 érvényes – 18 M Ft bruttó tervezhető összeg + 2 M Ft külön tartalék.

**Alap a gazdaságos gyártástechnológia:** egyszerűbb anyag, standard korpusz, gazdaságosabb gyártási mód. A legerősebb látványelemek nem tűnhetnek el (Péter 02:33). A fő anyagváltozat külön sorban.

**BiBo:** a navy laminált front az alap; festett MDF csak külön indoklással és jóváhagyással.

**Stílusonként a teljes bekerülés, fő és gazdaságos változatban:**
- nappali–étkező–konyha: TV-fal, kísérőfalak, mű, LED, függöny, textil és styling, ML05-lámpatest, konyha;
- master;
- fürdő.

**Tételesen kimutatandó:**
- mit vált ki (V2 03a, V3 r1 A/B/C, korábbi lámpák, LED);
- mi esik ki a 18 M-ból.

**Viszonyítás – V3 r1 nappali-csomag (Astra-becslés):**
- S01: 740–1040 eFt, gazdaságos 535–740 eFt;
- S02: 855–1160 eFt, gazdaságos 650–860 eFt.

**Konyha:**
- A 18 M „mindennel” értendő, a konyhagépekkel együtt (GOAL §3).
- Konyhabútor nincs. A promptsablon v3.1 Cam_03 FIXED-blokkja szerint:
  - IKEA METOD-váz;
  - két sor, 62 cm mélyen, a sorok között 85–86 cm (FELTÉTELES K1; tartalékként 45 cm-es sekély sor);
  - a kb. 85 cm magas nyugati mellvéd marad: nincs sziget, nincs mennyezetig érő fal;
  - a gépek külön sorban.

A §11.4 becslései nem ellenőrzöttek. Minden ár becslés, amíg nincs konkrét termék vagy ajánlat.

### 11.11 Kamerák és nézetek – mit mutat a 6 kamera és a kalibráció
**Az alapképek** nézetenként a regiszter `alapkep` oszlopában vannak.

**Kameraértéket ne találj ki;** a pontos kamera és a FRAME LAYOUT Claude-é.

| Kamera | Helyzet (tájékoztató) | Mi látszik | Különleges kötöttség |
|---|---|---|---|
| **Cam_02** nappali–terasz (lock) | [8,30; 4,40; 1,55], 20 mm, ÉNy felé | a W01 TV-fal balra; az üvegfal, a terasz és a valódi panoráma jobbra; az ülőcsoport; az étkező nyugati hosszoldala a jobb alsó sarokban; az ML05 a kép felső szélén | terasz: −0,15-ös greslap, +0,62-es WPC-dobogó, zöldtető, antracit korlát, Buda és a városi tetők |
| **Cam_12** nappali hero (PR #17, JAVASLAT – kreatív alap, merge nincs) | [3,95; 7,90; 1,45], 22 mm, vízszintes, DK felé | a kanapé eleje az előtérben; az étkező az ML04 függesztékével (u 0,21; v 0,05); a konyha pultfala; a W03-a és a 05.3 ajtó; a W02 (u 0,54–0,81); a W07 a jobb szélen (u 0,82–0,99) | **a TV-fal, az üvegfal és a terasz nem látszik**; az ML05 lámpatest függesztékként a kép felső szélén látszhat (Claude vetíti) |
| **Cam_03** konyha–étkező – **ÚJ, KONYHAORIENTÁLT JAVASLAT KÉSZÜL** (Claude; Péter 02:33) | a jelenlegi [4,70; 7,70; 1,50] szinte ugyanaz, mint a Cam_12 → nem kompozíciós alap | **a konyha a kép fő témája:** a két sor frontja, munkalapja és hátfala, a hűtőoszlop (W03-a), a mellvéd; az étkező széle, a székek és az ML04 az előtérben vagy oldalt; minimális átfedés a Cam_12-vel | a kompozíciót a látható elemek hierarchiájaként írd le; a végleges kivágást Claude Blenderből adja |
| **Cam_04** master (lock) | [0,35; 4,30; 1,50], 20 mm, ÉK felé | a fejvégfal az ággyal, az északi fülke teljes gardróbfala, az éjjeliszekrények és olvasólámpák | 3,57 × 5,50 m a fülkével; az ágy 180×200, tengelye y 6,40; legalább 60 cm az ágy mellett; a D20–D23 hozzáférhető; a K13/K14 szabad; ML06, D26 |
| **Cam_11** master panoráma (lock) | [3,20; 6,10; 1,20], 20 mm, ülő szemmagasság az ágyon, nyugat felé | a 3,64 m-es nyugati üvegfal (három fehér keretes mező), az erkély, a valódi kilátás (városi tetők, templomtorony, budai hegyek); az ágy lábvége; a jobb szélen az északi fülke gardróbfala; a bal szélen a déli gardróbsáv; ablakkezelés, szőnyeg | **a fejvég a kamera mögött van, nem látszik**; a függöny a 0,33 m-es falsávon, a nézet szabadon marad; részletek: `05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md` |
| **Cam_10** fürdő 06.2 (lock) | [14,50; 6,62; 1,50], 16 mm, az ajtóból kelet felé | Geostone Grigio burkolat, Esagonetta dekor a zuhany hátfalán, walk-in zuhany üvegfal nélkül, fekete Grohe szerelvények, Geberit mosdó és WC | ablaktalan; **csak hozzáadható:** tükörkompozíció, tároló, lámpatest a meglévő pontokon, textil, kiegészítők, növény; részletek: `05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md` |

**Kalibráció (C1 Zenit, C2 Lake Forest × Cam_02, Cam_04, Cam_11; regiszter 61–66. sor):**
- **Mit mutat:** a v1 eredeti koncepcióját újratervezve, a valódi héjban, őszinte anyagokkal.
  - Források: promptsablon v3.1 §3, `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` és a v1 képek.
- **Szabályok:** ugyanazok a reality-szabályok és ugyanaz a kamera–fény forgatókönyv, mint a stílusoknál.
- **Szerep:** a kreatív minimum referenciája, nem versenyző.
- **Nem helyettesítik** az S06 Zenit Atelier és az S07 Lake Forest Couture teljes, újratervezett stílusát.

### 11.12 Astra kimenete – egyetlen Work-feladat, verziózott GitHub-kimenet (r2)
**Tartalom** (Péter 02:33, 8. pont és 02:35):
1. **TV-fal-koncepciók:** S01 és S02 stílusonként három érdemben eltérő koncepció, egy javasolt főváltozattal.
2. **Stílus-specifikációk:** a tíz stílus részletes, egységes specifikációja:
   - nappali–étkező–konyha, master, fürdő;
   - teljes, gazdagon berendezett terv;
   - továbbfejlesztett fal-, berendezési, WOW- és Hue-stratégia;
   - fő és gazdaságos anyagváltozat, méretekkel és becsült bruttó költséggel;
   - a kiváltott tételek.
3. **Elemlista** (§11.7).
4. **Pontosan 66 önálló, angol kreatív renderprompt:**
   - 60 fő prompt = 10 stílus × 6 kamera (Cam_02, Cam_12, Cam_03, Cam_04, Cam_11, Cam_10);
   - 6 kalibrációs prompt = C1 Zenit és C2 Lake Forest × Cam_02, Cam_04, Cam_11;
   - azonosítók: **a regiszter `kep_id` oszlopa, betű szerint** (`05_promptok/KEP004_66_kep_keret_v1/KEP004_66_kep_regiszter.csv`, 66 sor).
5. **Integrációs instrukció Claude-nak**, a nyitott műszaki feltételek listájával.

**Kimeneti szerkezet** (új ág + draft PR; a V2 és a V3 r1 fájljai érintetlenek):
```
05_promptok/KEP004_ASTRA_V3_1_r1/
  00_README.md                     – tartalom, verzió, források
  00_CHECKPOINT_NAPLO.md           – checkpointonként: sorszám, idő, tartalom, commit SHA, távoli ellenőrzés eredménye
  01_MANIFEST_66.csv               – nr;kep_id;stilus;kamera;fajl;statusz;validalas;checkpoint;karakterszam;mintaprompt;megjegyzes
  02_KOZOS_REALITY_FIXED_elvek.md  – közös elvek, angolul
  03_KAMERA_KOMPOZICIOK.md         – a 6 kamera és a kalibrációs nézetek kompozíciós leírása
  10_STILUS_SPEC/S01_KyotoInk.md … S10_DesertModern70.md, C1_Zenit.md, C2_LakeForest.md
  20_PROMPTOK/<kep_id>.prompt.md   – 66 fájl, mindegyikben:
                                     === BEGIN PROMPT <kep_id> ===
                                     … a teljes angol prompt …
                                     === END PROMPT <kep_id> ===
  30_TV_FAL_KONCEPCIOK_S01_S02.md
  40_ELEMLISTA_V3_1.csv
  50_KOLTSEG_ES_KOCKAZAT.md        – fő/gazdaságos, kiváltott tételek, LED/Hue műszaki-költség kockázati tábla
ai-coordination/results/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r1.md – összefoglaló + integrációs instrukció
```

#### Kötelező, folyamatos GitHub-checkpointolás (Péter 02:43 CET)
**Miért:** Péter heti Work-keretéből kb. 26 % maradt, ezért egy félbeszakadó futás kész része sem veszhet el.

**Ág és PR:**
- ág: `astra/creative-upgrade-v3-1-r1-20261025`;
- draft PR címe: „WSG Creative Upgrade V3.1 r1 – 10 stílus-specifikáció + 66 kreatív prompt (checkpointolt)”.

| Checkpoint | Tartalom | Mentés |
|---|---|---|
| **CP0 – alapok** | Új ág, draft PR. A 66 tételes `01_MANIFEST_66.csv` mind a 66 regiszter-azonosítóval, `PENDING` státusszal. A `00_README.md` és a `00_CHECKPOINT_NAPLO.md`. | commit + push, majd **ellenőrzés a távoli GitHubon** |
| **CP1 – kreatív mestertervek** | A tíz stílus önálló, részletes specifikációja (`10_STILUS_SPEC/`, a C1/C2 koncepció-cellákkal). A közös elvek (02), a kamera-kompozíciók (03), az S01/S02 TV-fal-koncepciói (30). | azonnal commit + push + ellenőrzés. **Ez akkor is értékes eredmény, ha a promptgyártás félbeszakad.** |
| **CP2 – prioritás** | Előbb az S01/S02 négy kiemelt promptja (Cam_02, Cam_12), külön commitban. Utána az S01/S02 többi nyolc nézete (Cam_03, Cam_04, Cam_11, Cam_10), valamint az S01/S02 elemlistája. | minden részlet után commit + push + ellenőrzés |
| **CP3 … CPn** | S03 → S10 stílusonként 6 prompt, majd a C1/C2 kalibráció (6 prompt) | stílusonként, **legfeljebb 6–10 új promptonként** commit + push + ellenőrzés |
| **Záró CP** | Az elemlista (40) és a költség- és kockázati tábla (50) véglegesítése, a results-fájl, a 66/66 teljességi ellenőrzés | commit + push + ellenőrzés, PR-megjegyzés |

**Manifest – minden checkpoint után frissül:**
- **`statusz`**, Astra állítja:
  - `PENDING`: nem kezdett;
  - `DRAFT`: elkezdett, nem teljes;
  - `COMPLETE`: teljes, önálló, stílus- és nézetspecifikus kreatív prompt, Astra önellenőrzésével.
- **`validalas`**: minden `DRAFT` és `COMPLETE` tételnél `NEEDS_CLAUDE_VALIDATION`.
  - A `COMPLETE` kreatív promptot jelent, **nem** futtatható csomagot.
  - Futtatható csak az, amit Claude Blender- és költségaudit után validált csomaggá épít. Ezt a mezőt később Claude írja át.
- **`checkpoint`**: melyik checkpointban mentve.

**Mentésnek csak az számít,** ami ténylegesen felkerült a távoli GitHubra:
- push után olvasd vissza a fájlt vagy a fájllistát a távoli ágról, és írd be a naplóba a commit SHA-val;
- a pusztán helyi, vagy csak a Work-munkamenetben létező fájl nem elég.

**Megszakítás esetén:**
- a kész fájlok megmaradnak;
- a legutóbbi commit és a manifest alapján a munka később a `PENDING`/`DRAFT` tételekkel folytatható, a `COMPLETE` részek újraírása nélkül (folytató üzenet: C rész).

**Tilos:**
- mind a 66 promptot csak a futás végén, egyetlen nagy commitban menteni;
- hiányos vagy sablonos promptot `COMPLETE`-nek jelölni.

**Ha az írás vagy a GitHub-hozzáférés akadályba ütközik:**
- azonnal jelezd;
- ne folytass hosszú, mentés nélküli kreatív munkát.

**A checkpointolás nem jelent** új kutatást vagy külön Work-futást.

**Teljességi ellenőrzés (záró CP):**
- a manifest **66/66** sora, mindegyik `COMPLETE`, és az azonosítók megegyeznek a regiszterrel;
- stílusonként 6 prompt, plusz 6 kalibráció;
- mind a 66 fájl létezik, és a BEGIN/END jelölők a saját `kep_id`-t tartalmazzák;
- nincs „see previous”, „same as”, „TBD” vagy „…” helykitöltő.

Ha a futás nem ér végig, a PR-ben pontosan sorold fel a nem `COMPLETE` tételeket.

**Claude átvételkor** ugyanezt géppel újraellenőrzi, és megnézi a közel azonos szövegpárokat is.

**Átadás:**
- új ág és draft PR;
- a PR-be: `WSG-ASTRA-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1`;
- ha nincs írási jog: az eredmény a Workben marad, `handoff blocked` jelzéssel.

**Önellenőrzés átadás előtt** (helyiség és stílus szinten, nem kivágásonként):
- [ ] Megvan-e a §0.2 hat erőssége a stílus egészén? Nem kell mindnek minden kivágásban látszania.
- [ ] Minden jelentős, látható tömör falnak van-e terve (§11.3)?
- [ ] S01 és S02: három érdemben eltérő TV-fal-koncepció és egy főváltozat?
- [ ] Ugyanaz-e a nappali–étkező–konyha terv a Cam_02-n, a Cam_12-n és a Cam_03-on, és ugyanaz-e a master a Cam_04-en és a Cam_11-en?
- [ ] A berendezés elfér-e a közlekedési méretekkel? (Claude ellenőrzi.)
- [ ] Minden elemnek van-e mérete, falazonosítója, elhelyezési szándéka, forrása és ára?
- [ ] Kiderül-e, mit vált ki és mi esik ki a 18 M-ból?
- [ ] 66/66, hiányzó stílus, kamera vagy kalibráció nélkül?
- [ ] Minden checkpoint felkerült-e a távoli ágra, és szerepel-e a naplóban a commit SHA-val?

### 11.13 Mi NEM feladat
- képgenerálás és a 66 kép futtatása;
- Blender-módosítás;
- a V2/V3 r1 fájlok felülírása;
- PR-beolvasztás;
- rendelés, ajánlatkérés, külső kötelezettségvállalás;
- a végleges stílus kiválasztása Péter helyett.

A 66 prompt kreatív tervezési kimenet, nem Blenderrel validált futtatási csomag (Péter 02:35).

---

## B rész – Claude feladatai (r2)
1. **Elrendezési alternatívák (§11.8):**
   - 2–3 valódi változat: hat ülőhely, székmozgatás, konyhai hozzáférés;
   - valós termékmérettel, költségkülönbséggel;
   - eredmény: `ai-coordination/results/WSG-20261025-A902-ELRENDEZES-ALT_r1.md`; Péter választ.
2. **Cam_03:** új, konyhaorientált kamerajavaslat Blenderben, a választott elrendezéssel; draft PR, merge csak Péter „mehet”-jével.
3. **PR #17 (Cam_12) beolvaszthatósága:**
   - technikailag tiszta (2026-10-25: mergeable, nincs fájlütközés; a lock és a .blend a main-en azóta nem változott);
   - tartalmi feltételek:
     - a kiválasztott elrendezéssel újra kell ellenőrizni a Cam_12 kivágását;
     - javasolt az új Cam_03-mal együtt egy kamera-PR-ben;
     - validátor-újrafuttatás az egyesített állapoton;
     - Péter „mehet”-je.
4. **Átvétel:**
   - Claude Astra ágát csak olvassa, nem ír rá;
   - a checkpointokat és a manifestet a távoli ágon követi, ha Péter kéri, futás közben is;
   - a 66/66-os teljesség gépi ellenőrzése, a közel azonos szövegpárokkal együtt;
   - koordináták hozzárendelése az elemlistához;
   - új 1b tömbképek az r2-módszerrel (`03_blender/geometry_v2/tomeg_cam02_v3test/`).
5. **Független ellenőrzés:**
   - termékár és szállítás dátummal;
   - LED/Hue műszaki és költségellenőrzés: profil, tápegység, vezérlő, kábelút;
   - az ML05 helyszíni ellenőrzési terve (fotó, hétfői bejárás).
6. **Futtatási csomagok:** csak az audit után, adagonként, Péter külön „mehet”-jével.
7. **FRAME LAYOUT:** a „Nothing else stands in the room…” tiltás helyére a teljes, listázott berendezés kerül.
8. **Nem most:**
   - új S01 Cam_02 geometriai próba (Péter 02:33);
   - a diagnosztikai kalibrációs kép, csak külön „mehet”-tel.

## C rész – Péter üzenetei Astrának (Work, kézzel beillesztve)

**Indító üzenet:**
> WSG A-902 – Astra Creative Upgrade V3.1, végleges brief r2. Olvasd el és hajtsd végre a `peterkapusi88-hub/wsg-berendezes` repó `main` ágán: `ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md`. A §11.0 és a §11 elsőbbséget élvez. Egyetlen futásban kérem a tíz stílus-specifikációt, az S01/S02 TV-fal-koncepciókat és pontosan 66 önálló angol kreatív promptot, a regiszter azonosítóival és manifesttel. Kötelező a §11.12 szerinti checkpointolás: CP0 → CP1 → CP2, utána legfeljebb 6–10 promptonként commit és push, mindegyik a távoli GitHubon ellenőrizve. Ha a GitHub-írás akad, azonnal jelezd. Képet ne generálj, Blendert ne módosíts, a V2 és a V3 r1 fájlokat ne írd felül. A végén a PR-be írd: `WSG-ASTRA-RESULT: WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1`.

**Folytató üzenet – csak megszakadt futás után, új futásban:**
> WSG A-902 – Astra V3.1 folytatás. Az `astra/creative-upgrade-v3-1-r1-20261025` ág legutóbbi commitja és a `05_promptok/KEP004_ASTRA_V3_1_r1/01_MANIFEST_66.csv` alapján készítsd el a `PENDING` és `DRAFT` tételeket ugyanazzal a briefdel (`…V3_1_r2.md`) és checkpointolással. A `COMPLETE` tételeket ne írd újra.

# WSG A-902 – MASTER WORKFLOW V2: 10 teraszelrendezés × 30 kültéri stílus × prémium képrendszer

> **2026-10-28 – AKTUÁLIS MUNKASTÁTUSZ (elsőbbséget élvező állapotlink):** [A902_TERASZ_AKTUALIS_ALLAPOT_2026-10-28.md](A902_TERASZ_AKTUALIS_ALLAPOT_2026-10-28.md). A P0 kész, a két P1 kreatív kör elkészült, a P1.5-v1 elutasított, P1.6 új kreatív tervvázlatok készültek. A **P3 WORK-W01 teljes 4+2 hatnézetes pilot** elkészült; **grafikai formátumát és külalakját pozitívan értékelte a tulajdonos**, de **használhatósága, fantáziája, tényleges geometriai megfelelése és megvalósíthatósága nem jóváhagyott**. [Részletes P3-átadás](P3_A902_2026-10-28_W01_PILOT/STATUS_ES_ATADAS.md). A pilot becsült teljes költsége **8,811356 M Ft**, a friss **6–6,5 M Ft-os kültéri tervezési cél** felett; a teljes A-902 lakás kerete továbbra is **20 M Ft bruttó, minimum 10% tartalékkal**. A V2 alábbi korábbi 4–5 M Ft-os összegei **történeti kiindulók, nem az aktuális tulajdonosi teraszcél**. A P3 10×6, P4 30×4, P5 és P6 **nem indult**; a közös, validált C01–C10 nincs lezárva. **A P3 eredeti képeket és Blendert tartalmazó ZIP nincs a repóba másolva; csatolmányként kell átadni a folytatáshoz.** Az új állapotsor nem indít automatikus feladatot vagy képgenerálást.


**Projektazonosító:** `A902-TERASZ-MASTER-WORKFLOW-V2`  
**Dátum:** 2026-10-27.  
**Állapot:** **TERVEZÉSI ÉS FELADATINDÍTÁSI PROTOKOLL**. Az új master dokumentum elkészítése **nem** indítja el a Worköt, Pro Chatet, Claude-ot, Codexet, képgenerálást, HTML-készítést vagy GitHub-PR-t.  
**Felhasználó döntése:** 10 ténylegesen eltérő elrendezés 6 képpel; 30 stílus ugyanazon kiválasztott elrendezésen 4 képpel; ezután tudatos keresztezés, majd a döntősök profi fotóhoz igazított perspektivikus renderjei. Két egymástól független kreatív gondolatmenet: ChatGPT Work/Astra High és GPT-6 Pro Chat. Claude átmenetileg nem használható, 2026-10-29-től várható vissza.

> **Mottó:** Mi szeressünk bele. Teremtsünk értéket. A jó, extravagáns hatás nem jogosít nem létező teraszszintre, fiktív termékre vagy 4 M Ft-ot többszörösen meghaladó látványra.

## 0. Dokumentumhierarchia és módosítási korlát

1. Mindig a **legfrissebb** `GOAL.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`, `OPENAI_instructions.md`, `ai-coordination/RENDER_REALITY_GATE.md`, `ai-coordination/HANDOFF_PROTOCOL.md` az elsődleges projekt- és ellenőrzési forrás.
2. **A teljes tulajdonosi funkcionális brief**, biztonsági és költségigények részletes leírása: [`A902_TERASZ_10_ELRENDEZES_BRIEF_2026-10-27.md`](A902_TERASZ_10_ELRENDEZES_BRIEF_2026-10-27.md). Nem helyettesíti egy rövid megindító prompt: benne van a jakuzzi, zuhany, kutyás gyep/rampa, napozó, lounge, étkező, kültéri bár/konyha, projektor, hang, Hue, privát szféra, klíma/növények és szomszédok szükséglete.
3. **Vizuális ábrázolás**: [`WSG_ALAPRAJZI_PREZENTACIO_3_RETEG_2026-10-27.md`](WSG_ALAPRAJZI_PREZENTACIO_3_RETEG_2026-10-27.md). A három azonos feladatban csatolt referencia: `2d.jpeg`, `4es design.png`, `6os design.png`. Ezek **nem** WSG valós geometriák; a képfájlok nem biztos, hogy a repóban vannak, ezért szükség esetén mellékelni kell.
4. **Ez a V2 master** az előző két dokumentumot **nem írja felül**, hanem az aktuális sorrendet, a 30 stílust, a külön két kreatív futást, a 60 + 120 képes célmátrixot és a fotókamerás döntős köröket rögzíti. Műszaki ütközésnél a frissebb, bizonyított terv és a Render Reality Gate erősebb a kreatív briefnél.
5. **Jóváhagyás**: Péter kérésére **ennek az egy új MD-fájlnak** elkészítése engedélyezett. Semelyik modell ne módosítsa automatikusan a `GOAL.md`-t, a Blender-mastert, a projektet vagy a repó többi fájlját; minden további GitHub-írás, PR, költséges kampány, megrendelés, külső kommunikáció és fizetés előtt külön jóváhagyás szükséges. A képi státusz `KONCEPCIÓ – NEM VALIDÁLT`, amíg a bizonyítási feltételek nem teljesültek.

## 1. Közös, minden versenynél változatlan valóságmodell

### Terület és pénz
- A-902: nyilvántartott **79,22 m² terasz/erkély + 71,18 m² zöldtető = 150,40 m²** kültér. Gres: 23,62 és 19,34 m²; kiemelt WPC: 25,00 m² (terv szerint kb. +62 cm); erkély: 11,26 m². Ezek *tervi* összesítők; tényleges járhatóság és teherbírás külön igazolandó.
- A-902 **teljes bruttó lakáskerete 20 M Ft**, az aktuális GOAL.md szerint kültérre kb. **4 M Ft** cél, 10% tartalékszabállyal. **5 M Ft csak feltételes, teljes kereten belül egyeztetendő alternatíva**; nem válhat csendben a 20 M feletti új költéssé.
- Jakuzzi kb. 2 M Ft **költségfeltevés**, nem ellenőrzött teljes telepített beszerzési ár. Vizsgálandó a víz, villany, szállítás/emelés, teherbírás, szerviz, szigetelés és további költségek; nem szabad „ingyen” zuhanyt vagy vízkiállás-megosztást feltételezni.

### Valós adatok – minőségbiztosítás
- **Méretek/pozíciók**: `01_alaprajzok/terv_kivonat_2026-10-24/A902_meretezett_alaprajz_1-50_terv.png` és `A902_9emelet_megvalosulasi_terv_kivagat.png`; eredeti vektoros/megvalósulási PDF, ha elérhető. Blender előzetes: `03_blender/WSG_A902_v2_terasz_ELOZETES_20261024.blend`, plusz **a legfrissebb hiteles** geometriaverzió/lock. A régi modellt nem szabad automatikusan érvényesnek nevezni.
- **Teljes profi fotóleltár**: `08_allapotfelmeres/fotok_profi_20261025/README.md`, `LELTAR_profi_20261025.csv`, `A902/` (**33 fotó**, köztük belső nézetek és külső táj), `_kontaktlapok/A902_kontaktlap.jpg`, `FOTOKAMERA_LATVANYTERV.md`. Lehetőség szerint a releváns egyéb `KULSO_homlokzat_kozter_garazs/` nézetek is, ha szomszédok/tájolás szempontjából értékesek.
- Ne elégedjünk meg a 3488/3498 mintaképpel: **indexeld és vizsgáld át mind a 33 A902-képet**, a külső/teraszos részhalmazt előszűrve; a meglévő anyagok, vízszintek, szegélyek, korlátok, nyílások, őshonos/meglévő növények, panoráma, belátás, napsütés, fény és helyiségkapcsolat külön adatlapot kap. Bizonyítatlan növényazonosítót ne találj ki.
- Kiemelt teraszképek: **`KZS_3488-744.jpg`** (greslap), **`KZS_3498-734.jpg`** (zöldtető-homlokzat); **`KZS_3483-749.jpg`** besorolása bizonytalan. További fotók képi szerepét a leltár alapján, tényleges megnyitással azonosítsuk. A későbbi perspektivikus renderhez a **`Cam_F_3488`, `Cam_F_3498` stb. fotókamerákat külön illesszük**, a régi kamerákat ne írjuk felül.
- A profi fotók retusált/vágott, **EXIF nélküli** képek; **nem** megbízható méret-, abszolút tájolási vagy napállásforrások. Geometriát méretezett rajzból / ellenőrzött 3D-ből mérj, fényképpel az anyagokat, kilátást, formát és eltérést ellenőrizd.
- **Tér/észak/szomszéd kontroll**: a nappaliból kijövet az előre eső DK, illetve a jobb kéz felőli K/DK szomszédos belátás Péter megfigyelése; ÉNy/Ny panoráma és naplemente kívánatos, de a tényleges helyzet fotó+helyszín/alaprajz alapján igazolandó. Külön feliratos `NORTH / NEIGHBOURS / VIEW / PRIVACY / SUN` térkép kell, valós és nem igazolt rétegekkel. A kilátás ne tűnjön el a privát növényfallal; a növényfal nyitott térben **nem hangszigetelés**.

### Kötelező teraszfunkciók – választási szabadsággal
Minden elrendezésnél vizsgálandó: jacuzzi, esetleges kültéri zuhany, külön kutyás játszó/pisilő hely és csúszásmentes kutyarámpa, napozás, árnyékos és napos lounge, étkezés, panorámás laptopos munka, projektoros sport/mozi, kültéri mini konyha vagy mobil bár/hűtő, diszkrét hangszóró(k), Hue-jelenetek, növények, nyugati panoráma védelme és K/DK belátás csökkentése. **Nem mindegyik funkció fér el ugyanazzal a luxusszínvonallal ugyanazon 4 M Ft-ból.** A koncepciók vegyes hangsúlyokat használhatnak és nyíltan jelölhetik az elhagyott/halasztott tételeket.

## 2. A tervverseny három külön tengelye

| Tengely | Tartalom | Rögzítendő | Szabadon változhat |
|---|---|---|---|
| **C01–C10 elrendezés** | *Hol van* jakuzzi, étkező, lounge, napozó, munka, kutyazónák stb.? | terasz, nyílások, szintek, használható mezők, költségplafon | bútorok/zónák helye, közlekedők valós újraszámolással |
| **S01–S30 stílus** | *Milyen érzés* a rögzített elrendezésben? | ugyanaz a kiválasztott C-alap, fő funkcionális zónák és geometria | forma, szín, arány, kültéri bútor, textúra, fény, megfelelő növények |
| **V01–V06 ábrázolás** | *Hogyan látjuk* ugyanazt a tervet? | kamera, objektumazonosság, gyártási sablon és státusz | grafikus 2D / két 3D prezentáció, reggeli és esti világítás |

- A **10 elrendezés** legyen különböző térbeli kompozíció, **ugyanazzal a neutrális, igényes, valós meglévő burkolatokat megtartó prezentációs anyag- és színkódolással**. Ez az összehasonlító „Neutral Premium Rooftop” **nem** győztes designstílus, hanem közös vizuális kontroll.
- A **30 stílus** ugyanazon, az elrendezésversenyből kiválasztott és megfelelően rögzített **1 referencialayouton** versenyezzen; 3D mindegyik, **azonos két kamera és azonos reggeli/esti fényviszonyok**. A formabútorok cserélhetők, de az elrendezés/befoglaló és szabad közlekedés maradjon auditálható.
- Döntős párosítás: tipikusan **3 legjobb C × 4 legjobb S = 12 jelölt**, először egyszerűsített pilot, nem 12×6 végleges kép.
- Azonos rögzített realitás és kamera nélkül a képek szépsége **nem objektíven összehasonlítható**.

## 3. Harminc stílus – azonosítók az egész WSG-katalógussal

**S01–S17: a már meglévő beltéri WSG-stíluskísérletek, kültéri értelmezésként, nem új nevekre átírva.** A stílust nem szabad beltéri termékek és beltéri anyagok időjárásnak kitett másolásának tekinteni.

| ID | Meglévő WSG-stílus |
|---|---|
| S01 | Kyoto Ink |
| S02 | BiBo Nocturne |
| S03 | Aleli Casa |
| S04 | LA Horizon |
| S05 | Miami Streamline |
| S06 | Zenit Atelier |
| S07 | Lake Forest Couture |
| S08 | Milano Radical |
| S09 | Paris Collector |
| S10 | Desert Modern 70 |
| S11 | Zuma Inspired Luxury |
| S12 | Modern Organic |
| S13 | Westside Grand Continuum |
| S14 | Modern White Luxury |
| S15 | Authentic Japanese Modern |
| S16 | Monza Magno G63 Residence |
| S17 | Mercedes Design Collection Residence |

**S18–S29: Péter külön kért 12 kültéri stílusa; S30: egy új, szobrászi/biofilikus, kortárs luxusirány.** A közeli stílusokat (S04/S22, S05/S21, S15/S20) konkrét kültéri bútorozásban, tömegképzésben és használati élményben is meg kell különböztetni; ne ugyanazt a tervet nevezd át.

| ID | Új kültéri stílus | Látványkód |
|---|---|---|
| S18 | Tropical Luxury Resort | dús zöld, intim trópusi spa |
| S19 | Nordic Rooftop Spa | északi fa-textúra, tiszta wellness |
| S20 | Japanese Ryokan Garden | autentikus japán relaxáció és egyszerűség |
| S21 | Miami Pool Club | ívek, könnyed fehér resort, napsütés |
| S22 | LA Sunset Estate | nyugati panoráma, kaliforniai lazulás |
| S23 | Tulum Raw Earth | organikus, nyers hatású anyag és forma |
| S24 | Bali Private Villa | meleg fa, zöld és védett spa |
| S25 | Mykonos Cycladic | finom fehér, szoborszerű mediterrán |
| S26 | Ibiza Bohemian Luxe | lounge, rétegzett kültéri textúrák |
| S27 | Provence Maison Garden | lágy mediterrán kert, elegáns romantika |
| S28 | Portofino Riviera | olasz riviéra, kifinomult étkezőterasz |
| S29 | Marbella Beach Club | resort-napozó, társasági luxus |
| S30 | Sculptural Biophilic Resort | íves szobrászi tömegek, természet, prémium fény |

**Azonos kültéri realitás:** mind a 30 stílus tervezett anyagát, növényét, fényét, bútorát budapesti szél-, hő-, csapadék- és téli kitettségre szűrjük; pálma nem „magyar télre automatikusan gondozásmentes”; kültéri szövet/IP-védelem és növényterhelés is számít. Az összes stílusnál különítsük el a *kreatív vizuális ambíciót* az *ellenőrzött áraztatható kültéri megoldástól*.

## 4. Képmátrix: 10×6 + 30×4 = 180 célkép + döntős fotókamerák

### A) 10 elrendezés × 6 kép = 60

Mind a **C01–C10** elrendezés ugyanazzal a neutrális, egységes prezentációs anyagvilággal, azonos `CAM_A` / `CAM_B` kamerakerettel:

| Nézet | Jelölés | Ábrázolás |
|---|---|---|
| V01 | 2D PREMIUM | luxus, ortografikus felülnézet, `2d.jpeg` élességi minta |
| V02 | 2D TECHNICAL | igazolt hosszúság × szélesség, m², szabad közlekedő- és rámpaméretek, szintkülönbség, belátás/kilátás; vektoros PDF |
| V03 | 3D_A_DAY | a `4es design.png` építészeti/festői axonometrikus bemutatási módja, `CAM_A` |
| V04 | 3D_B_DAY | a `6os design.png` fotórealisztikus axonometrikus bemutatási módja, `CAM_B` |
| V05 | 3D_A_EVENING | V03 ugyanazon kamerája, esti valósághű világítás |
| V06 | 3D_B_EVENING | V04 ugyanazon kamerája, esti valósághű világítás |

### B) 30 stílus × 4 kép = 120

Mind a **S01–S30** a **kiválasztott azonos referencia-elrendezésen**, a jóváhagyott valós tartalommal:

| Nézet | Jelölés | Ábrázolás |
|---|---|---|
| T01 | 3D_A_MORNING | `4es design.png` prezentáció, reggeli nappali fény, `CAM_A` |
| T02 | 3D_B_MORNING | `6os design.png` prezentáció, reggeli nappali fény, `CAM_B` |
| T03 | 3D_A_EVENING | ugyanaz a `CAM_A`, valós kültéri fény és Hue |
| T04 | 3D_B_EVENING | ugyanaz a `CAM_B`, valós kültéri fény és Hue |

**A „30 stílus” nem 30 új elrendezés**. Az egyes stílusoknak egyedi, megvalósítható bútor-/anyag-/fénystratégiát kell adni, de az azonos helyiséghatárokat és funkcióhelyeket tartani kell. A 2D műszaki lap a közös alaprajzon ismert; drámai egyedi bútorméretnél újra auditálandó.

### C) A győztesek profi fotókamerás renderei

A felhasználó által kiválasztott C×S párosításokhoz 3–5 *releváns* eredeti A-902 profi fotónézet alapján külön perspektivikus, fotóhű render: terasz gres `KZS_3488`, tetőkert `KZS_3498`, további fotóazonosítók az ellenőrzött leltárból, szükség esetén beltéri kitekintés. A valós helyszíni fotó **fix és változatlan komponensei csak maszkon kívül**, a berendezésre alkalmazott új elemek a maszkban; fotó–Blender illesztés, lencseeltolás, perspektíva, növény/anyag/panoráma képpont-eltérésvizsgálat. Külön napsütéses és esti változat csak felhasználói döntéssel.

**Képsáv összesen: 60+120 = 180**, PLUSZ a döntős fotókamerák. **Ez hosszabb távú cél, nem egyetlen gombnyomásra, nem ellenőrzés nélküli 180 generált kép.**

## 5. Operatív sorrend és állapotkapuk

| Szakasz | Fő gazda | Képi volumen | Kötelező eredmény és felhasználói kapu |
|---|---|---|---|
| **P0 – Auditált közös ténycsomag** | **Work High** (olvasás, audit, fotóleltár; Codex célzott segítsége indokolt esetben) | **0** | `P0_SOURCE_AND_GEOMETRY_AUDIT`: összes 33 A-902 fotó feldolgozási leltára; megfelelő méretezett alaprajz, teraszszint- és szomszédsági/tájolási térkép; meglévő anyag/növény/water-power leltár, igazolt/nem igazolt státusz; nyitott műszaki kérdések. **Péter jóváhagyása P1 előtt.** |
| **P1 – Két független kreatív verseny** | **Work High külön chat** és **GPT-6 Pro Chat külön chat** | **0** | Mindketten ugyanazt a **P0 ténypakkot** kapják, **nem** a másik kreatív ötleteit; mindkettő 10–15 önálló teraszkoncepciót ír, prioritás/használhatóság/4–5 M sávval. Eredmények külön, változatlanul archiválandók; **csak ezután** egymás mellé helyezhetők. |
| **P2 – Kiválasztás, geometria/költségkontroll** | Work összerendez; **Codex** geometriai ellenőrzés; **Claude** független költség/Blender-kontroll **csak amikor újra elérhető** | 10 vektoros/zónás mérési lap, nem kész fotórealista sorozat | 10 valóban különböző **C01–C10** elrendezés, legalább 3 pro és kontra, nettó áthaladások, kutyarámpa, zöldtető/jakuzzi/áram/víz kockázat, 4 M és 5 M külön bruttó sáv. **Csak műszakilag vállalható jelölt lép tovább.** |
| **P3 – 10×6 prémium elrendezési képsorozat** | Work kreatív/art direction; dokumentált render pipeline; Codex/Claude geometriai kontroll | **60**, de előbb **1×6** pilotteszt | Rögzített neutrális anyagvilág és két kamera, azonos elrendezés ugyanazon hat nézetben. Az első hat kép geometriája, kontrasztja, színhűsége, mérhetősége és luxushatása jóváhagyásra kerül, csak ezután fut a többi. |
| **P4 – 30 stílus teljes próbája** | Work High (kreatív és HTML) + Pro Chat független esztétikai kihívás | **120**, de előbb **2×4** próbakép | Egy kiválasztott és rögzített C-alap, 30 különböző S; mindegyikhez kültéri valóság- és költségkártya, 2 × reggeli + 2 × esti 3D, konzisztensek az egész sorozaton. |
| **P5 – Párosítások és döntős szűrés** | Work és Pro; Claude/Codex reális audit | előbb koncepciónként 1–2 kis teszt, nem automatikus teljes sorozat | Tipikus 3 elrendezés × 4 stílus = 12 kombináció; funkcionális, érzelmi, árkockázati, privát szféra és valós megvalósíthatósági értékelés; Péter választ. |
| **P6 – Fotókamerás döntősök** | Work kreatív/mask és kép + Codex/Claude perspektíva- és geometriai kontroll | döntősönként kb. 3–5 kiválasztott nézet, nappal/este a döntés szerint | Helyszíni fotóhoz illesztett és eltérés-auditált látvány; valós termék/árajánlati státusz; finalista, de ne nevezzük kiviteli tervnek igazolás nélkül. |

**Két üzemmód**: (a) most, amíg Claude nincs: P0 + független P1, read-only forrásfeldolgozás, koncepcionális modellek csak jelölten; (b) Claude visszatérésével: P2 geometria + független pénzügyi audit. **Ne állítsd, hogy Claude lefutott vagy GitHubon eredménye van, amíg nincs bizonyított tényleges eredmény.**

**Minden szakasznál** (i) a GitHubhoz képest forrás-commit, (ii) feladat- és AI-azonosító, (iii) mi ellenőrzött vs. feltételezés, (iv) konkrét akadályok, (v) képkészítési/ráfordítási darabszám, (vi) felhasználói kapu külön. P0/P1-hez **nem** kell újrenderelni a fél házat.

## 6. Szükséges HTML-rendszer

- A Work később készítsen **egy valóban működő, egységes luxusminőségű HTML-katalógust**, nem pusztán képet egy megálmodott weboldalról.
- **Külön fülek**: `Elrendezések (C01–C10)`, `Stílusok (S01–S30)`, `Döntős kombinációk (C×S)`, `Forrás/megfelelőségi térkép`; minden kártyán egységes képarány, kameraképek, forrásállapot, aktuális bruttó költségsáv, szubjektív minőség és pro/kontra, valamint hiányzó tételek.
- Képváltó 2D/3D és reggel/este, több terv összehasonlítása, zóna-/panoráma-/szomszéd-/napfény-/közlekedő-rétegek **csak az igazolt forrásadatokból**, link az eredeti képfájlra és vektoros műszaki alaprajzra; működő navigáció és megfelelő mobilnézet.
- Ne legyen dísznek elhelyezett inert UI; a generált tervek **ugyanannak a geometriai/termékállapotnak** a különböző megjelenítései; a közös HTML sablon miatt vizuálisan összehasonlíthatók.

## 7. Értékelés és megvalósíthatósági kapuk

Elrendezések: `funkcionalitás + privát szféra + panoráma + kutyás használat + nap/árnyék + wow + fenntartás + költségkockázat`. Stílusok: `forma + szín + arány + anyag + fény + eredetiség + beltéri folytonosság + keret`. A *pontozott szubjektív előny* és a *műszaki/áras igazolás* külön mező; utóbbit nem lehet szép összpontszámmal kompenzálni.

Műszaki kritikus elemek: jakuzzi tele terhe, vízszigetelés, szerviz, lefolyó, kültéri zuhany/megfelelő fagymentesítés, két meglévő teraszdugalj és öntöző körének **valódi** alkalmas volta, tetőkert járhatósága/kutyazóna-használhatóság, a +62 cm WPC-szint leküzdhetősége, rámpa hossz/szabad sáv, növénykonténerek súlya, szélre megfogott baldachin/pergola, egész éves növényfenntartás, Hue és hang biztonság/áthallás, szomszéd belátási látószöge. Minden bizonyítatlan tétel: `FELTÉTELES / NEM VALIDÁLT / TILTOTT a bizonyításig`.

A képkövetelmény: a három eredeti feltöltött vizuális referencia **legalább célként kitűzött részletessége és élessége**, de nem lehet azonos felbontást vagy fotórealisztikus WSG-egyezést minden modellben ígérni; fotós nézet csak maszkolással és geometriateszttel nevezhető ellenőrzöttnek.

## 8. Pontos, új beszélgetésekhez szánt indítópromptok

### A) FIRST – Work High / P0 – azonnal indítható

> WSG A-902 / P0. Dolgozz a `peterkapusi88-hub/wsg-berendezes` GitHub-repó `06_koncepcio/A902_TERASZ_MASTER_WORKFLOW_V2_2026-10-27.md` master workflow-ja szerint, továbbá olvasd a hivatkozott GOAL.md, SKILL.md, OPENAI_instructions.md, a részletes A-902 teraszbrief, Render Reality Gate és prezentációs szabvány fájljait. **Most kizárólag a P0 forrás- és geometriai auditot végezd.** Vedd számba a **33 A-902 profi fotót**, a kapcsolódó külső nézeteket és az 1:50-es A-902 megvalósulási tervet; ellenőrizd a teraszszinteket, WPC/gres/zöldtető valós határait, növényeket, panorámát, szomszédokat, villamos/vízkiállásokat, tájolást és benapozottsági bizonytalanságokat. Készíts átlátható, forrásazonosítós `P0_SOURCE_AND_GEOMETRY_AUDIT` jelentést, fotókatalógust, tény/feltételezés listát és egy egységes ténycsomagot a későbbi két **független kreatív futáshoz**. Ne készíts látványképeket, ne módosíts Blender-mastert vagy GitHub-fájlt, ne indíts más AI-t, további szakaszokat vagy fizetős kampányt. Ha egy fájlhoz nincs hozzáférésed, konkrétan jelöld. Mutasd az eredményt és kérj jóváhagyást a P1-hez.

### B) SECOND – két egymástól független P1 kreatív kör (mindkettő ugyanazt a P0-t kapja)

**Work High (új munkamenet):**

> WSG A-902 / P1-WORK. Olvasd a `A902-TERASZ-MASTER-WORKFLOW-V2` fájlt és a jóváhagyott P0 ténycsomagot. **A Pro Chat tervét/ötleteit ne olvasd**; ez független kreatív elrendezésverseny. Adj **legalább 12–15 érdemben eltérő** elrendezési elképzelést a valós, azonos teraszgeometriára, különböző jacuzzi–zuhany–kutyás rámpa–napozó–lounge–étkező–bar–kilátás/munka–projektor–Hue–zöld rész kompromisszumokkal. Kreativitás, arány, társasági hangulat és luxusélmény kiemelt; a bruttó **4 M alap és 5 M feltételes** keretet ne lépd át úgy, hogy ténynek nevezed. Javasolj 10 döntőst, 3 pro/3 kontrát, forrás- és blocker jelzéssel, önálló, semleges zónarajzi leírásokkal. **Ne generálj 60–180 képet**, ne induljon következő szakasz, GitHub-írás külön jóváhagyással.

**GPT-6 Pro Chat (külön új Pro Chat; a P1-WORK ötletei nélkül):**

> WSG A-902 / P1-PRO – független luxus térszervezési kihívás. Adom ugyanazt a Work P0 által jóváhagyott, tény/feltételezés szerint jelölt geometriát, 33 fotó forrásjegyzékét, teraszprogramot, 4 M bruttó alap + 5 M csak feltételes keretet. A másik AI elképzeléseit nem adom át. Kérlek, gondolj ki **15 rendkívül kreatív, mégis megépíthető tetőterasz-elrendezési koncepciót**: legyen wow, nyugati kilátás, valóban privát jakuzzi és napozás, kutyabiztos és hozzáférhető zóna, társasági szórakozás, praktikus étkező, minőségi esti fény — szokatlan kombinációk és tértrükkök, de semmi kitalált építészeti adottság. Minden variánsnál írd le az elrendezési logikát és 3 pro/3 kontrát, a megvalósíthatósági kockázatokat, a fő költségterhelő elemeket. **Ne utánozz ismert Work-terveket, ne generálj képeket és ne módosíts repót.**

### C) THIRD – csak a két P1 után: P2 összevezetés

> WSG A-902 / P2. A `A902-TERASZ-MASTER-WORKFLOW-V2` és a két független, külön változatban őrzött `P1-WORK` és `P1-PRO` alapján állíts össze **10 különböző, tényleges méretekkel ellenőrizhető C01–C10 elrendezést**. Szűrd ki a duplikátumokat, de tarts meg merész, jó ötleteket. Kérj független geometriai ellenőrzést Codexszel, és Claude-tól pénzügyi ellenőrzést csak akkor, ha tényleg elérhető és külön indítva van. Teljes bruttó 4 M alap/5 M feltételes költségkockázat, közlekedő/rampa/szomszéd/panoráma/napfény audit és rangsor szükséges. **Most még nincs tömeges képgyártás.** Kérj jóváhagyást az 1×6 pilotteszthez.

### D) Későbbi külön indítások (most nem indítandók)

- `P3`: `C01–C10 × V01–V06`, egységes neutrális prémium külső anyagvilág, **először 1×6 pilot**, majd felhasználói jóváhagyással 60-as sorozat.
- `P4`: `S01–S30 × T01–T04`, ugyanazon kiválasztott C layout, **először 2×4 pilot**, majd jóváhagyással 120-as sorozat.
- `P5`: 3×4 döntős C×S kombináció; elsősorban kompozíciós és valós termék/áraudit, nem a 170 kombináció automatikus legyártása.
- `P6`: kedvenc párosításokból ellenőrzött `Cam_F_...` helyszínifotó-alapú nappali/esti render, valódi anyag, kilátás és szomszédság megőrzésével.

**Zárás:** Az első konkrét felhasználói indítás *csak* a `P0` Work-munka. Az indítóprompt rövid marad, mert a részleteket ez a master MD + a kapcsolt hosszú teraszbrief + a fotók + a három ábrázolási referencia hordozzák.

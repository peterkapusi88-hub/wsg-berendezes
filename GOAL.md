# GOAL.md – Westside Grand berendezés (A-811, A-812, A-902)

> Ez a fájl a projekt memóriája. Bármelyik AI (Claude, ChatGPT, Gemini) ezt olvassa el először, és ebből dolgozik. Ha valami itt nem szerepel, kérdezz, ne találd ki. Frissítve: 2026-10-24 (reggel, I. szakasz; 09:00 Rubin/Orbit képteszt; 13:18 Péter döntései a négy stílusról; 17:06 PR #8 beolvasztva, a semleges_v2b az összehasonlító alap).

## 1. Cél egy mondatban
Három új építésű, üres, kulcsrakész lakás (1134 Budapest, Szabolcs u. 11–13., Westside Grand I., átadva 2026-10-21) berendezése úgy, hogy **olcsón összerakva drágának hasson**, és eladáskor (vagy bérbeadáskor) a vevő két különböző, kész hangulatot lásson: egy **Zenit-** és egy **Lake Forest-verziót**.

## 2. A három lakás (fix adatok)
| | A-811 | A-812 | A-902 |
|---|---|---|---|
| Szint | 8. | 8. | 9., penthouse |
| Alapterület (megvalósulási terv 2026-07-08) | 90,68 m² (brosúra 92) | 102,05 m² | 99,94 m² |
| Beosztás | nappali-étkező-konyha + előtér ~41 m², 2 háló (master gardróbbal), fürdő káddal + fürdő zuhannyal | nappali-étkező-konyha ~44 m², 3 háló (2 gardróbbal), 2 fürdő | nappali-étkező-konyha ~45 m² nyitott konyhával, 3 háló, 2 fürdő (kád + walk-in zuhany) |
| Kültér | 14,30 m² erkély | 7,04 m² erkély | 79,22 m² terasz (greslap 23,62 + 19,34, emelt WPC 25,00 [+62 cm], erkély 11,26) + 71,18 m² zöldtető = 150,4 m²; jakuzzi-előkészítés a Ny greslapon |
| Belmagasság (Kémeri műszaki ellenőr mérése, 2026-10-21) | **2,69–2,72 m** | **2,69–2,73 m** | **2,90–2,93 m** |
| Padló (burkolatkiosztási terv, dosszié 194./211./228. o.) | Egger **laminált**, Classic 8/32 4V **Aqua**, Grey Soria Oak EL2065 (593610); szegőléc 6 cm (1818925) | ua. | Egger **laminált**, Classic 8/32 4V **Aqua+**, **Grey Treviso Oak EL2184** (591760); szegőléc 1818766 |
| Vevői módosítás | 05.2+05.3 összevonva (+2,70×1,70 gardrób), nagyobb nappali, épített zuhany, pengefal megszűnt | 08/09 összevont fürdő **egyedi sarokkád (beépítve)**, 06.1 → HTH, épített zuhany | épített zuhany 06.2, bidés WC |
| Adottság | Egger szürke tölgy dekorú **vízálló laminált** padló – az előtérben és a konyhában is, burkolatváltás nélkül (Andrea, 2025-09-15; a műszaki melléklet szerint ott funkció miatti garanciavesztéssel); az Egger szerint az Aqua kb. 24, az Aqua+ kb. 72 óráig véd a beszivárgó víz ellen, vízhatlan nem. Fehér fal, nyílászáró **belül fehér, kívül antracit** (IGAZOLT-F, 2026-10-21; a korábbi „fekete” téves), motoros redőny, Grohe/Geberit fürdők, mennyezeti fűtő-hűtő panel (fúrás csak ott, ahol nincs panel), riasztó, videós kaputelefon. **Konyhabútor nincs.** | ua. | ua. + jakuzzi-terasz |
| Rendeltetés | eladás/bérbeadás | eladás/bérbeadás | eladás, de Péter saját lakása is lehet |

A-902 helyiségméretek (méretezett alaprajz 1:50, vakolatlan; v2-geometria: `03_blender/geometry_v2/`, eltérés a Blender v1-hez ±15 cm; hétfőn mérendő): 05.1 master 3,57×5,50 (4,00 tiszta + gardróbfülke), 05.2 3,65×3,35 (gardróbfülkével), 05.3 3,52×3,95, 06.1 fürdő 1,75×2,65 (kád 170×70), 06.2 en-suite 1,92×2,85 (zuhany 182×85), WC 1,30, közlekedő 2,48×1,20, nappali 7,08 hosszú, étkező 2,80 mély, konyhafal 3,90, teraszüveg 4,50 + 1,80, nyugati üvegfal 3,65 + erkélyajtó 1,88. Részletek: `01_alaprajzok/`, 3D: `03_blender/`.

**Villamos kiállások mindhárom lakásban** (mennyezeti és fali lámpakiállás, kapcsoló, dugalj, TV/gyengeáram, termosztát, mennyezeti hűtő-fűtő mezők), méterben, rajzi koordinátával: `01_alaprajzok/villamos_kiallasok/` (összesítő: `OSSZESITO.md`). Forrás: M1 KORR 2 (A-902), M1 (A-811), M1 KORR (A-812); státusz **TERV SZERINT** (2026-10-24), helyszínen ellenőrizendő. A-902: 12 mennyezeti + 7 fali lámpakiállás, 29 kapcsoló, 49 dugalj.

## 3. Keret – fix plafon
- **A-811: 10 M Ft · A-812: 10 M Ft · A-902: 20 M Ft** (ebből terasz ~4 M).
- Bruttó, **mindennel**: tervezési díj, asztalos, bútor, világítás, textil, konyhagépek, kiszállítás, szerelés. Külső tervezőnél a tervezési + kivitelezési díj is benne.
- Minden listában 10% tartalék. Mindig mutasd a maradékot „hős-darabokra".
- Jelenlegi keretszámítás (2026-10-24, becslés): mindkét verzió befér; a penthouse a határon van, a jakuzzi (Heissner ~1,7 M vs Correll ~2,7 M) dönt. Részletek: `06_koncepcio/`.

## 4. Mit akar Péter
1. **Egy paletta végigvíve**, lakásonként egy akcent. Zenit: greige + füstös tölgy/dió + beton + fekete fém + bronz tükör, akcent mustár/olíva. Lake Forest: krém + travertin + világos tölgy + pezsgő-arany + fehér márvány.
2. **Különleges formák és végig burkolt/beépített falak** – ez adja a két referencia érzését. Megoldás építés nélkül: lamellapanel, kőfurnér, textúrás tapéta, kárpitpanel, padlótól plafonig bútortömegek takarólappal, rejtett LED a bútorok tetején/alján.
3. **Nincs építés**: fehér falak maradnak, nincs burkolás, bontás, gipszkarton; legfeljebb tapétázó (1 nap/lakás) és asztalos.
4. **Források**: ami látszik (kanapé, asztalok, székek, ágyak, tükrök, lámpák) → **Kave Home** vagy **Westwing** (westwing.hu – Andrea javaslata: jó ár-érték arány; saját márka a Westwing Collection); ami váz (PAX, METOD, BESTÅ) → **IKEA**; lakásonként 1–3 „forma-darab" → **asztalos** (anyagot és szabást mi adjuk a lapszabászattól, az asztalos csak a munkát számlázza).
5. **Fény = luxus**: Philips Hue, 2700 K, rétegezve, jelenetek.
6. Praktikum: minden hálóhoz gardrób, mosó-szárító a HTH-ban, előtérben pad + cipős + tükör, konyhában magasszekrény-sor.
7. **Kanapé: minimum L, inkább U alakú** mindhárom lakásban (Péter, 2026-10-24: „nagyon fontos”).

## 5. Szabályok minden terv-lépéshez
- Közlekedő 90–120 cm, mellék 60–90, szűkület min. 45; kanapé–asztal 45–50; étkezőszék hátratolás 90; ágy mellett min. 60.
- Bútorméret mindig valós termékadatból (IKEA API: `https://sik.search.blue.cdtapps.com/hu/hu/search-result-page?q=<keresés>&size=8&types=PRODUCT`; Kave Home árak csak a webshopban látszanak).
- Ár mindig dátummal és forrással; jelöld: „ellenőrzött" vagy „becslés".
- Asztalos-anyagszabály: matt/strukturált laminált bútorlap (Egger H1180 Halifax tölgy, H3710 Carini dió, F274 beton), bordázott MDF, hajlított MDF az ívekhez; furnér max. egy felületen; nincs tömörfa, kő, festett front; Blum/Hettich csak fiókban; belső mindig fehér.
- **Fény és áram csak meglévő kiállásra** (`01_alaprajzok/villamos_kiallasok/`): új kiállás és áram miatti vésés, fúrás nincs; bútor, polc, TV-konzol rögzítéséhez fúrni szabad (előtte vezetékkereső); függeszték csak a mennyezeti ⊗ fölé; a hűtő-fűtő mezőbe nem fúrunk; kapcsoló, termosztát, elosztó, kaputelefon, mozgásérzékelő nem takarható; falpanelen kivágás a dobozoknál.
- Minden küldés, rendelés, fizetés előtt Péter „mehet"-je kell. Andinak (Szakos Andrea, belsőépítész, a Zenit és a Lake Forest tervezője) csak jóváhagyás után megy anyag.
- Kivitelezőknek nem megy brosúra/látványterv („leesik, hogy van pénz").

## 6. Állapot (2026-10-24, éjjel)
- Koncepció-doksi kész (két verzió, fordítótábla, asztalos vs IKEA számítás, keret): `06_koncepcio/`.
- A-902 Blender-alap kész (falak, nyílások, bútor IKEA-méretben, 6 kamera). **Mindkét stílusréteg beépítve** (`Stil_Zenit` 180 obj., `Stil_LakeForest` 164 obj.) a `03_blender/WSG_A902_stilusok.blend`-ben; váltás: `set_style('Zenit'|'LakeForest')` a `wsg_helpers.py`-ból. 3+3 EEVEE-nézet: `04_renderek/blender_stilusok/`.
- 6 fotorealisztikus AI-kép Geminivel (`04_renderek/ai_gemini/`) és 6 ChatGPT-vel (`04_renderek/ai_chatgpt/`) az A-902-ről mindkét stílusban, összehasonlító lapokkal. Promptok: `05_promptok/`.
- Blender MCP add-on újratelepítve (Lab-repó `https://lab.blender.org/`, MCP 1.0.3, localhost:9876, Auto Start, beállítás elmentve).
- ChatGPT-munkarend eldőlt: Work = lakberendező/projektvezető, Codex = Blender-technikus (`OPENAI_instructions.md`, `AGENTS.md`).
- Külső ajánlatkérés kiment 8 lakberendező cégnek (10/10/20 M keret, tervezés + bútorválasztás + budget); IKEA teljes-lakás tervezés foglalandó.
- Fotók a lakásokról hétfőn (2026-10-27) jönnek → geometria javítása, A-811/A-812 alap.
- **Astra-inputcsomag A-902 v1 kész (2026-10-24):** `ai-coordination/inputs/A902_v1/` – rögzített geometria, stílusfüggetlen költségkiindulás (18 M tervezhető + 2 M tartalék), semleges Blender-nézetek (`04_renderek/semleges/`), kérés-tervezet. Nincs elindítva; PR #1 inaktív.
- Claude GitHub-app hozzáférés működik (közvetlen push).
- **2026-10-24 reggel – I. szakasz (hétfői állapotcsomagra felkészülés) kész:**
  - `08_allapotfelmeres/`: ellenőrzőlista, IGAZOLT / ELŐZETES / HIÁNYZIK tábla, fotóbeviteli rend 255 tervezett felvétellel, stílusfüggetlen költségstratégia 3 lakásra, II. szakasz feldolgozási rend.
  - A-902 geometria v2 (PDF vektorból) és eltéréslista.
  - A teraszvideók elemzése: a terasz többszintű tetőkert.
  - Blender `WSG_A902_v2_terasz_ELOZETES_20261024.blend` új fájlként; az élő fájl érintetlen, a nem mentett élő állapotról mentés készült a `~/Downloads/WSG_blender_mentesek/` mappába.
  - Astra input v1.1 (nincs elindítva).
  - Minden korábbi Zenit/LF-kép KONCEPCIÓ – NEM VALIDÁLT (`04_renderek/RENDER_STATUSZ.md`).
  - A műszaki ellenőri anyag (364 fotó + jegyzetelt tervek) feldolgozva: `08_allapotfelmeres/MUSZAKI_ELLENORI_ANYAG_KIVONAT_2026-10-21.md`.
    - mért belmagasság, a felületek fotóval rögzítve, az A-902 konyhapadlója laminált parketta;
    - 55 kiválogatott fotó a `fotok/` alatt;
    - a hibalista nincs a repóban.

- **2026-10-24 07:10 – első Astra-pilot (manuális):** Rubin Szalon és Ezüst Orbit (A-902 nappali), KONCEPCIÓ / ELŐSZŰRT.
  - Claude-audit: `ai-coordination/audits/WSG-20261024-PILOT-001_CLAUDE_AUDIT.md`. A számtan helyes (17,80 / 18,00 M). A CSV-sávokból számolt legrosszabb eset +3,35 M. Árajánlat: 0 Ft.
  - Javított Cam_02 geometria-alap: **függő** (a próbarenderek elbuktak, lásd `03_blender/validator_report_2026-10-24_semleges_v2.md`).
  - Tartós átadás: `ai-coordination/HANDOFF_PROTOCOL.md` (GitHub-postafiók).
  - Kész, **nem indított**, kétfázisú brief: `ai-coordination/requests/WSG-20261024-STYLE10-002.md`.
    - A fázis: 10 stílus a teljes lakásra, kép nélkül.
    - B fázis: azonos kamerás képek, zárolva az ellenőrzött Blender-alapig.
  - A Codex geometriai auditja (draft PR #2) korlátai a briefben K1–K6 alatt szerepelnek.
  - Új kockázat: a teraszüvegezés osztása a fotón eltérhet a modelltől (hétfői mérés).
- **2026-10-24 08:24–08:50 – Rubin Szalon / Ezüst Orbit képteszt (`WSG-20261024-GEMINI-RENDER-TEST-002`):**
  - Cam_02, azonos pilotprompt + 5 bemeneti kép; Gemini („3.1 Pro” + Kép létrehozása), Péter kérésére ChatGPT-kontrollal.
  - Mind a 4 kép KONCEPCIÓ – NEM VALIDÁLT, Gate-szinten FAIL-elemekkel: Gemini Orbit kitalált ajtó, ChatGPT Orbit fekete belső profil, mind a négyen nem valós teraszszintek.
  - Péter értékelése: „gagyik, semmi luxus”.
  - Diagnózis: elsősorban a prompt és a koncepció, a Gemini renderje tovább ront. Képen az Ezüst Orbit működik jobban; a kamerához a ChatGPT Rubin áll a legközelebb.
  - Képek: `04_renderek/ai_gemini/`, `04_renderek/ai_chatgpt/`. Jelentés: `ai-coordination/results/WSG-20261024-GEMINI-RENDER-TEST-002.md`.
- **2026-10-24 09:10 – villamos kiállások rögzítve mindhárom lakásra** (Péter kérésére, a méretezett PDF vektoraiból): `01_alaprajzok/villamos_kiallasok/` – JSON/CSV, összesítő, ellenőrző átfedéskép, hűtő-fűtő mezők, kinyerő szkript. Korábban csak képként volt a repóban, koordináta nélkül. Független ellenőrzés után javítva (4 hiányzó mozgásérzékelő, 1 ventilátor, 3 rossz helyiség, 6 téves doboz). A rajzlapok módosítási szövegéből: kupola = mozgásérzékelő, önálló BK = riasztóközpont (valószínű); A-902-ben szekrényvilágítás-dugalj 05.1: 1, 05.3: 2. Nyitott: R, 1/2/3 jelentése, alapértelmezett szerelési magasságok, helyszíni ellenőrzés.
- **2026-10-24 13:10 – PR #4 (kiállások) és PR #5 (A-902 geometria v2b) a main-ben** (Péter jóváhagyásával). A vevői műszaki melléklet (2024.02.13.) átnézve: az R jel motoros redőny kiállása, a kupola-jel mozgásérzékelő (igazolva); a mennyezeti hűtő-fűtő panelek a födémbe integráltak; minden lakóhelyiségben van RJ45 informatikai blokk; a riasztó az alapban csak elővezetékezés (beépült-e: nincs adat).
- **2026-10-24 14:10 – A-902 v2b: kiállás-réteg a Blender-modellben és bútor nélküli alapképek** a B fázishoz (Cam_02/03/04, semleges szórt fény; reality card: `04_renderek/A902_alap_v2b/`). Beolvasztva a mainbe (PR #7, Péter, 14:25). Észrevétel: a fő helyiségek mennyezeti kiállásai (ML03–ML08) a hűtő-fűtő mezőn belül vannak – lámparögzítés előtt hőkamerás ellenőrzés (hétfő).
- **2026-10-24 14:35 – PR #8 (17:09-kor beolvasztva Péter „mehet”-jével, `f149d98`):** alaprajzhű semleges v2b referencia (Cam_02 + ellenőrző rárajzolás + felülnézet; Cam_03/04 kiegészítő), Validator v2 PASS 0/0, reality card a bizonytalan elemekkel; közös 4-stílusos költségkeret (6,80 M fix + ≤ 11,20 M stílusfüggő); árkönyvtár (87 sor, Kave Home HU euróárak + magyar jelöltek); árhorgony-előszűrés; Astra High brief `WSG-20261024-STYLE4-003` (NEM INDÍTOTT).
  - Fő lelet: a Rubin/Orbit látható tételei a 4,90 M-os célból csak 2,6–3,0 M-t használnak, a Zenit/LF 4,0–5,2 M-t.
  - A PR #7 alapképén a nyugati fal a falon maradt Zenit-tapéta anyag miatt halványan bézs. Péter döntése (17:06): az összehasonlító alap a `semleges_v2b`.
  - 16:46: mind a három render végleges (Cam_02/03/04). Közben talált modellhibák, amelyeket a Validator nem jelez: két homlokzati rés a v2b után (7 cm a 05.1 fülkénél, 10 cm az előtér déli falán), és a tetőkert nyugati mellvédje belelóg a 05.1 fülkébe. Javítás külön lock-javító draft PR-ben (Péter 17:06: igen, ha nem visz sok időt).
- **2026-10-24 17:21 – PR #11: lock v2b-1 – 18:56-kor a main-ben (Péter: „mehet az is fel”).** Az A-902 kanapé-méretpróba (PR #13) eredménye a v2b-1 lockkal változatlan (újrafuttatva). A két homlokzati rés lezárva (7 és 10 cm), a tetőkert nyugati mellvédje kihúzva a 05.1 fülkéből, a falon maradt Zenit-tapéta anyag fehérre cserélve a .blend-ben. Új ellenőrzés: terasz ↔ belső tér átfedés. Validator PASS 0/0 (előtte is), a burok ZÁRT, a teljes fájl validátorlistája változatlan. Nyitott: a pillér 1 cm-es síkeltérése (hétfői mérés).
- **2026-10-24 15:30 – A-811 és A-812 Blender-alapmodell (ELŐZETES, tervből)**, Péter kérésére. **PR #9 a main-ben** (Péter, 18:26: „a többit addig feltöltheted, amik kész vannak”).
  - **Forrás és tartalom:** a méretezett alaprajz vektoros falvonalai. Falak, aknák, ajtók, üvegfalak, padló, erkély, kamerák, kiállás-réteg és lock.
  - **Ellenőrzés:**
    - validátor v2: PASS;
    - helyiség-m² a megvalósulási tervvel ±0,1 m²-en belül (a fürdők kivételével: előtétfal);
    - a rajzi méretszámok egyeznek.
  - **Alapképek:** bútor nélkül, az A-902-vel azonos semleges beállítással, reality carddal. Helye: `04_renderek/A811_alap_v2/`, `04_renderek/A812_alap_v2/`. Leírás: `03_blender/geometry_A811_A812/README.md`.
  - **Geometria v2 (16:35):** egy független tervhűségi ellenőrzés 5 hibát talált a v1-ben (hiányzó EL4 előtétfal, hiányzó francia erkély korlát az A-812 hálóinál, két rés és egy padlóhiány) és 11 kisebb eltérést (szűkebb ajtónyílások, fém erkélyosztó, álmennyezet stb.). Mind javítva, az alapképek újrarenderelve; validátor PASS, réskeresés 0. A validátor PASS önmagában csak a lock-egyezést igazolja.
  - **Észrevétel:** itt is hűtő-fűtő mezőben van a nappali és a hálók mennyezeti kiállása. Az A-812 hálóinak padlóig érő ablakánál korlát a rajzon nincs. Mindkettő hétfőn ellenőrizendő.

## 7. Nyitott döntések
- *(2026-10-24, rögzítve)* Az A-902 nagy terasza **meglévő, többszintű tetőkert**: greslap, emelt WPC lépcsőkkel, zöldtető két sík füves szélével és középső dombos évelőágyással, térdmagas betonszegély, pálcás korlát. Nem kitalálandó és nem építendő; a Blender és az Astra-render ezt mutassa. A kilátás a helyszíni videókból rekonstruálandó. Zöldtetőre bútor vagy jakuzzi csak igazolt terhelhetőséggel kerülhet (Péter).
- *(2026-10-24)* A-812: az egyedi sarokkád be van építve (Péter), nem költségtétel.
- *(2026-10-24, Péter)* **Nem fúrunk és nem vésünk új áramért:** mennyezeti lámpa, LED és minden áramot igénylő elem a terv szerinti kiállásokra kerül. A kiállásokat lakásonként a `01_alaprajzok/villamos_kiallasok/` rögzíti. Bútor, polc, TV-konzol rögzítéséhez fúrni szabad, ez normális (Péter, 13:15); előtte vezetékkereső, a mennyezeti hűtő-fűtő mezőbe soha.
- *(2026-10-24, Péter)* **Kanapé: minimum L, inkább U alakú** mindhárom lakásban. Első becslés (Claude, alaprajzból, nem mért): az A-902 nappaliban U kb. 300 × 230 cm-ig elfér – TV a déli falon, kanapé háttal a teraszüvegnek, mögötte 90 cm-es út, a DNy-i bejárat és a kapcsolóoszlop szabad. A-811/A-812 méretpróba (draft PR #12): az U (Gala 300 × 225) csak étkező nélkül fér el; az L elfér – A-811-ben a terv 2,59 × 2,50-es L-je szekrénysorral, étkezővel és a gyári TV-blokkal együtt. A stílustervben U és L változat is kell; a végleges méretet a validátor méri.
- *(2026-10-24 17:40–18:16, Péter – eldöntve)* **A-811 nappali-étkező:** L-kanapé (a terv 2,59 × 2,50-es L-je) a gyári TV-blokkal szemben; fent **60 cm mély szekrénysor** x 0–4,90 m-en (a konyha magas szekrényeivel egy síkban); a kanapé annyival lejjebb, hogy a szekrény éppen megközelíthető legyen (méretpróba: mögötte 0,50 m, előtte 1,00 m a TV-pultig, nézőtáv 3,20 m). **Az étkezőasztal a konyha mellett, az ML04 lámpakiállás alatt marad**; a konyhába az asztal megkerülésével lehet bejutni – „nem akkora dráma, még jól is nézhet ki az asztal a konyha mellett, ha össze van komponálva” (18:01). A nagy erkélyajtóhoz 0,75 m-es mellékút elfogadva: „ha máshol így sokkal jobb” (18:10); a kis erkélyajtóhoz 0,95 m. A szekrénysor mögé esik a D10/D11 dugalj (LED), a K03 kapcsolónál alacsony. Andrea 2025-04-28-as átterve is ezt mutatta (L, mögötte 4,90 m-es fali sáv, asztal a lámpa alatt). Rajz: PR #12, `elrendezes_dontes_A811_A812.png`.
- *(2026-10-24 18:14, Péter – eldöntve)* **A-812 nappali-étkező:** az étkező a terv helyén (ML05 alatt); a kanapé L, vagy U, amelynek rövid szára a fix üvegmező előtt, hosszabb szára a másik oldalon van; fent szekrénysor a fülke hátfalán (a terv „3,89-es” fala, belül 3,22 m), 60 cm mélyen. Méretpróba (PR #12): U 3,00 széles (1,70 / 2,25 m-es szárak) és L is megfelel; az erkélyajtóhoz 0,75 m-es mellékút, nézőtáv 3,90 m. **18:23, Péter: a 0,53–0,55 m-es konyhaút így jó** (azokon a helyeken ritkán ülnek, sok személyes az asztal); **az A-812-ben U legyen** (P812U).
- *(2026-10-24 18:23, Péter – „nagyon fontos”)* **Az A-902-ben is U legyen a kanapé, de minimum L.** Méretpróba (draft PR #13): Péter U-ja (18:36) elfér, ha 0,45 m-rel a teraszüveg felé kerül (legjobb: U 3,00 × 2,20, nyitott oldal a gyári TV-blokk felé, a teraszhoz 1,0 m, a hálók folyosójához ~0,9 m, nézőtáv 2,7 m). **18:43, Péter:** a U a TV felé nyílik (ahogy a rajz mutatja); a teraszajtó tolható része a jobb (keleti) oldalon van, így a U közelsége az üveghez a nyugati részen nem gond; a U 2,40 m mély; az asztal helyét Claude választja → **0,30 m-rel nyugatra (P902_24A)**: a 05.3-as háló ajtajához 0,90 m, a teraszhoz az asztal keleti oldalán 0,75 m, az ML04 lámpa 0,20 m-re az asztalközéptől; az asztal nyugati székei mögött a U-ig 0,51 m.
- *(2026-10-24 18:39, Péter)* **A félhold alakú, ívelt kanapé is jó**, ha pufffal kiegészítve L-ként/U-ként működik („az is szexi”) – a stílustervben (Astra) mindhárom lakásban változatként vizsgálandó.
- *(2026-10-24, Péter)* **Westwing** (westwing.hu) is forrás a látszó bútorokhoz – Andrea javaslata, jó ár-érték arány. A webshop automatikus lekérést nem enged (robots), az árat böngészőben, dátummal kell ellenőrizni.
- *(2026-10-24, Péter)* **Repó-munkamód:** a döntéseit rögzítő kis szöveges frissítések jóváhagyás nélkül a `main`-be kerülnek; Blender-geometria, kiállás-adat, költség és nagyobb változás draft PR-ben, az ő „mehet”-jével (CLAUDE.md).
- *(2026-10-24, Péter)* Kültéren a társasházi „közös rész” szabályokkal nem korlátozzuk a tervet: fal, WPC és korlát rögzítésre használható. Egyetlen kikötés: a vízszigetelés nem sérülhet.
- *(2026-10-24, Péter)* **A TV helye szabad:** a tartalom interneten jön, a TV-hez csak dugalj kell; a gyári TV-blokk nem köti a helyét. Feltétel: dugalj a TV-falnál, a kábel rejtve, vésés nélkül, a kapcsoló, a termosztát és az érzékelő szabadon marad (`01_alaprajzok/villamos_kiallasok/README.md`, 5. szabály).
- Melyik lakás melyik verzió (javaslat: A-811 Zenit, A-812 Lake Forest, A-902 amelyik saját lakásként is tetszik).
- Jakuzzi: Heissner vagy Correll.
- Tapétázó beengedhető-e.
- Asztalos: Andi zenites asztalosa + 2 másik, két ár (komplett / csak munkadíj) ugyanarra a rajzra.
- Akvárium a 902 dolgozójában csak saját használatra.
- *(2026-10-24, részben eldöntve)* A-902 nappali: a TV helye szabad (Péter), a kanapé L vagy inkább U. L1 (kanapé a nyugati falon) vagy L2 (déli TV-fal) – a stílustervezés dönti el; az L2 TV-fala a déli fal kapcsolóoszlopát (x 7,15) szabadon hagyja, dugalja a D19. (audit 9.1)
- *(2026-10-24, nyitott)* Indulhat-e a 10 stílusos Astra-kör A fázisa (STYLE10-002)? Bekapcsoljuk-e a Claude-oldali ütemezett eredmény-ellenőrzést?
- *(2026-10-24 13:07, Péter – eldöntve)* **Állókép: ChatGPT; a Gemini egyelőre nem képszerkesztésre, elsősorban videóra.** A ChatGPT-kép csak akkor számít elkészültnek, ha ténylegesen létrejött, a repóban van és ellenőrizhető.
- *(2026-10-24 13:07–13:18, Péter)* **A Zenit és a Lake Forest a luxusminőség referenciairánya** („ezerszer izgalmasabb, szexibb”). A Rubin Szalon és az Ezüst Orbit első képei túl ingerszegények. A cél nem a költségvetés leegyszerűsítése, hanem a **kiemelkedő luxushatás valóban kivitelezhető áron**.
- *(2026-10-24 13:18, Péter)* A négy stílus (Zenit, Lake Forest, Rubin Szalon, Ezüst Orbit) összevetése:
  - a **vizuális minőség** és a **geometriai hűség** külön értékelendő;
  - mind a négy **azonos, bruttó 18 M + 2 M tartalék** rendszerben;
  - a fő látható tételekhez valós termékjelölt és ellenőrizhető ár kell.
  - **Először** ellenőrizhető, alaprajzhű, semleges Cam_02 referenciakép készül, a bizonytalan elemek dokumentálásával.
  - A kreatív stílusfejlesztés és a végleges promptok **Astra High** feladata. Claude a geometriai alapot, a költségellenőrzést és a GitHub-átadást készíti elő; a kész briefek a GitHubra kerülnek, Péternek ne kelljen fájlt másolnia.
- *(2026-10-24 17:06, Péter – eldöntve)* **A stílus-összevetés alapképkészlete a `04_renderek/semleges_v2b/`.** A PR #7 `04_renderek/A902_alap_v2b/` képei nem összehasonlító alapok; a kiállás-réteg a Blender-fájlban marad.
- *(2026-10-24 17:06, Péter)* A STYLE4-003 Astra-indítása **elhalasztva**: a folyamat áttervezés alatt. Addig Claude leírja, mit csinálna, és mi van a GitHub-csomagban.

## 8. Következő lépések
1. Péter dönt: melyik stílus melyik lakásba (7. pont), és a Gemini vagy a ChatGPT képei tetszenek jobban (`04_renderek/A902_Gemini_vs_ChatGPT.jpg`).
2. Tételes lista lakásonként (helyiség · tétel · termék · méret · ár · forrás · státusz) Kave Home + IKEA + asztalos; összeg + 10% + maradék.
3. Asztalos-rajzok + szabásjegyzék a forma-darabokhoz; ajánlatkérés csak „mehet" után.
4. Hétfő: fotók és mérés → mindhárom modell véglegesítése (az A-811/A-812 alapmodell kész, ELŐZETES), AI-képek a valódi lakásról.
5. Ajánlatok összevetése (8 cég + IKEA + Andi), döntés.

## 9. Mappatérkép
`01_alaprajzok/` brosúra + lakásonkénti alaprajz · `02_referenciak/` Zenit és Lake Forest kontaktlapok · `03_blender/` .blend fájlok + `wsg_helpers.py` + rétegszkriptek · `04_renderek/` alap (Blender), `blender_stilusok/` (Zenit/LF EEVEE-nézetek), `ai_gemini/`, `ai_chatgpt/` · `05_promptok/` képgeneráló promptok · `06_koncepcio/` a koncepció-doksi markdownban · `07_skill/` a Claude-skillek forrása · `08_allapotfelmeres/` állapotfelmérés (checklist, adatstátusz, fotóbevitel, költségstratégia).


## Új, kiemelt tervezési alapelv – nyitott stíluslabor és költséghű kivitelezés

A `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` a projekt **kötelező értékalapú tervezési és költségellenőrzési irányelve**. Péter eredeti mottója: **„Mi szeressünk bele. Teremtsünk értéket.”** A luxusérzetet nem csak az anyag, hanem a **forma, szín, arány, térhasználat, fény, természetkapcsolat és funkció** alakítja. Zenit és Lake Forest **csak induló példák**: azonos, valós geometriával és azonos lakásonkénti keret mellett 10+ további hangulat vizsgálható, végleges stílust nem választunk előre. A koncepciók előszűrt költségsávval, a döntősök cikkszámos termékekkel és méretezett egyedi bútorspecifikációkkal kerülnek összehasonlításra. Végleges, kivitelezhető státuszt csak valódi árak, szükséges asztalos ajánlatok, két független ChatGPT–Claude költségellenőrzés és render–specifikáció egyezés után adunk. Mindig a **lakás teljes** bruttó, 10% tartalékot figyelembe vevő keretét kell vizsgálni. A jelen dokumentum korábbi Zenit/Lake Forest lakásonkénti párosítása csak ötlet, nem döntés. Külső kommunikációhoz és rendeléshez Péter „mehet” jóváhagyása kell.


## 10. Legfrissebb döntések és következő bizonyítékok – 2026-10-24 este

- **Main állapot:** a #7–#13 PR-ek közül a #7, #8, #9, #10, #11, #12, #13 beolvasztva; #11 = A-902 v2b-1 homlokzati rések és mellvédjavítás. A korábbi inaktív #1 PR továbbra sem automatikus trigger. Ezt minden munkamenetben friss GitHub-állapottal ellenőrizni kell, nem örök státusz.
- **A-902 vizuális referencia:** `04_renderek/semleges_v2b/` Cam_02/03/04, csak terv szerint validált; PR #11 után a helyiségek/bútorbefoglalók változatlanok. A-811/A-812 alapképek: `04_renderek/A811_alap_v2/`, `A812_alap_v2/`. Régi élő `WSG_A902_stilusok.blend` nem azonos a friss v2b-1 építészeti alappal.
- **Jóváhagyott MÉRETPRÓBÁK:** A-811 2,59×2,50 m L + 60 cm felső szekrénysor, asztal a konyha mellett; A-812 U 3,00 m szélesség, 60 cm fülkeszekrény, asztal eredeti helyén; A-902 U 3,00×2,40 m (P902_24A), nyitott oldal TV felé, asztal 0,30 m-rel nyugatra. A valós termék, tolóajtó, székhasználat, szabad sáv és kiállás végleges ellenőrzése hátravan. Félhold/ívelt kanapé puffos L/U funkcióval megfontolható.
- **Új bizonyíték várható:** profi, utómunkázott helyszíni fotók kb. 60 képpel legkorábban vasárnap 2026-10-25; hétfői ellenőrzés 2026-10-26. A méretezett megvalósulási terv az elsődleges geometriai alap; a fotók anyag-, nyílászáró-, terasz-, panoráma- és eltérésreferenciák. A képi torzítást vagy retusálást ne kezeld falméretként.
- **Szakos Andrea várható új, bútorozott alaprajzai** döntő tervezői bemenetek mindhárom lakáshoz. A korábbi 2025-04-28-as változattól és a fenti, már elfogadott elrendezésektől való eltérést külön jelölni és Péterrel eldönteni kell, nem automatikusan átírni.
- **Beszerzés:** a kiemelten látható darabokhoz Westwing vagy Kave Home, beépített részekhez IKEA-alap + egyedi front/takaró vagy versenyeztetett asztalosmunka. Végleges beszerzés és árazás konkrét termékkonfigurációval, mérettel, anyaggal, szállítással és szereléssel.
- **Pénzügyi forgatókönyv:** a hivatalos A-902 alapkeret továbbra is 18 M Ft tervezhető + 2 M Ft tartalék a 20 M Ft bruttó plafonon belül. Péter a kiemelkedően erős Zenit/Lake Forest minőségre kb. 1 M Ft többletet is mérlegelne; ez csak külön kimutatott és külön jóváhagyandó alternatíva, nem automatikus költségnövelés. A-811/A-812 10–10 M Ft változatlan.
- **Működés:** Claude = operatív projektvezető; GPT-6 Chat = független kreatív kontroll; Astra High = külön jóváhagyással kiemelt kreatív tervezés; Codex = műszaki kód; Gemini = főleg videó. A GitHub verziózott ténytár, nem az AI-k automatikus indítója. A Claude Project `Instructions` a tartós viselkedési szabály, `Context` csak tudatosan frissített snapshot, `Memory` nem helyettesíti a GitHub legfrissebb forrását.

### 10/a. Kiegészítés – 2026-10-24 késő este: STYLE10-002 tényleges állapota és Astra-kreditszabály

- **STYLE10-002 A fázis ténylegesen lefutott** a ChatGPT Work-ben 2026-10-24-én (Péter indította; ≈33 perc), tíz stílussal (S01 Kyoto Ink, S02 BiBo Nocturne, S03 Alelí Casa, S04 LA Horizon, S05 Miami Streamline, S06 Zenit Atelier, S07 Lake Forest Couture, S08 Milano Radical, S09 Paris Collector, S10 Desert Modern 70), termékjelöltekkel, költségmodellel, rangsorral és három ajánlott döntőssel (BiBo Nocturne, Lake Forest Couture, Zenit Atelier; tartalék Kyoto Ink). **Astra GitHub-mentése nem történt meg.** A GitHubon látható „NEM INDÍTOTT” státusz ezért elavult volt; a brief fájlját visszamenőleg nem írtuk át.
- **Megőrzés:** a megosztott szál pillanatképéből Claude-relay: `ai-coordination/results/WSG-20261024-STYLE10-002_RELAY_RESZLEGES_20261024.md` (**RÉSZLEGES**: a 7. fejezet, 476–514. sor hiányzik; a kanonikus `results/WSG-20261024-STYLE10-002.md` útvonal Astra eredeti, teljes mentésének van fenntartva). Eredeti JSON a Macen: `~/Downloads/WSG/astra_style10_share_cx_6adceb.json`, SHA-256 `2f430740776cf1a1e86235d44a3072df548e034cc5415f80675fa54d85afed6e`; repóba Péter döntéséig nem kerül.
- **Forráskatalógus és összevetés:** `ai-coordination/inputs/STYLE_CLAUDE_ASTRA_FORRASOK_20261024.md` – Claude „tíz stílusa” valójában keretrendszer (gesztus-mátrix A–I, L2/L3, K1–K10, sablon, 4 stílusos előszűrés, Zenit/LF fordítótábla), 0 megnevezett stílus; Astra 10 kidolgozott stílus; Péter szó szerinti irányai (japán, BiBo, Alelí, LA Skyline, Miami Art Deco, Zenit, Lake Forest + 3 szabad). Rubin Szalon / Ezüst Orbit: dokumentált pilot, nem kötelező résztvevő (Péter 19:34).
- **Következő brief:** `ai-coordination/requests/WSG-ASTRA-HIGH-KREATIV-V2.md` – **NEM INDÍTOTT**, tartalma **MEDIUM**-szintű; 1. rész: a STYLE10-002 lezárása az eredeti szálban minimális kredittel (kész fájl mentése, ha kell a 7. fejezet pótlása); 2. rész: a közös tízes kreatív brief a kreatív minőségi küszöbbel (Zenit/LF legjobb látványa = minimum; nem olcsóbbnak kinéző változat; először kivételes forma/tér/anyag/fény, utána költséghatékony valós megoldás; azonos kamera és szigor).
- **Astra-kreditszabály (Péter, 2026-10-24 19:34):** Astra Work **legfeljebb MEDIUM**; a korábbi High-engedélyek visszavonva; High/Ultra/Max csak új, külön engedéllyel; indítás csak akkor, ha a szint a felületen ténylegesen ellenőrizhető; nincs második STYLE10-002-munkamenet, új Work-feladat vagy extra kredit. **Beszerzési forrás (19:38):** Kave Home az IKEA és a Westwing mellett.
- **Nyitott döntés Péternél:** a hiányzó 7. fejezet visszanyerési útja (Codex helyi napló `~/.codex/sessions` megnyitása Claude-nak, vagy az eredeti Work-szálba küldött egyetlen mentőüzenet), és a V2 brief indítása.

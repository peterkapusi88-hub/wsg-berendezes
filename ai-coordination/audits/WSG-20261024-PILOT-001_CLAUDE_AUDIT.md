# Claude független audit – WSG-20261024-PILOT-001 (A-902 nappali, Rubin Szalon / Ezüst Orbit)

- **Auditált fájl:** `ai-coordination/results/WSG-20261024-PILOT-001.md`, commit `f307765edd2a812498287edea5645596289eafa3` (szerző: `peterkapusi88-hub`, ChatGPT GitHub-kapcsolaton át, 2026-10-24 07:08). 18 520 bájt, **sha256 `5e2f3e82f77aa7a6c1d12d9b5fb518b7c94dde58be4be4653ed21fe4f8f8343a`**. A fájlt nem módosítottam.
- **Astra bázisa:** `main` @ `4b4495a`. **Audit bázisa:** `main` @ `f307765` (a kettő között csak a pilotfájl került be).
- **Auditor:** Claude, 2026-10-24. Saját forrásból: geometry lock JSON, helyszíni fotók (ME-BAL-045, -080), műszaki ellenőri kivonat, webárak (dátummal). Astra számait nem vettem át ellenőrzés nélkül.
- **Összesített státusz:** a pilot **KONCEPCIÓ – NEM VALIDÁLT** (kreatív rész) és **ELŐSZŰRT – FELTÉTELES** (költség). Ez egyezik Astra önértékelésével. Nincs PASS, nincs ajánlattal validált tétel; írásos ajánlat: **0 Ft**.

---

## 1. Kreatív minőség

Mérce: `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` 1. és 9. pont („rohadt drágának néz ki”, hat luxusforrás, giccsvédelem). A pontszám **szubjektív Claude-értékelés** (1–10); a tényállítások külön vannak.

| Szempont | Rubin Szalon | Ezüst Orbit |
|---|---|---|
| Karakter, eltérés Zenit/LF-től | 8 – egyetlen mély rubin akcent, fehér + szürke tölgy + grafit; tisztán más | 7 – kör-motívum, ezüst, jégkék; más, de trend-közeli |
| WOW-erő (első 3 másodperc) | **6** – 3 × 60×120 cm kárpitpanel ≈ 2,16 m² a 3,93 × 2,90 m-es (11,4 m²) falon: a fal ~19%-a. Arányos, de szerény lépték; inkább „ízléses” mint „drága” | **5–6** – a nagy kerek tükör kanapé fölött a 2020-as évek leggyakoribb lakás-toposza; a drágaságot csak hibátlan kivitel (vastag tükör, csiszolt él, egyenletes halo) adja |
| A 6 luxusforrásból használt | szín, textúra, (fény részben) | forma, tükröződés, (fény részben) |
| Ami hiányzik | tér-gesztus (bútortömeg, ív, beépítés), fényarchitektúra, panoráma-keretezés; az „art déco” címkét a formák nem hordozzák (nincs ív, bordázat, lépcsőzés) | melegség-ellenpont: a hűvös szürke padló + fehér + jégkék + ezüst kórház- vagy showroomhideg lehet; textúra-gazdagság |
| Giccsvédelem | jó (egy akcent, nincs arany/márvány/vörös fal) | jó (nincs RGB, nincs tükörfal, kör csak 2×) |
| Megvalósíthatóság | 8 – kárpitos-munka, könnyű panelek | 7 – egyedi Ø140 tükör szállítása, rögzítése és halo-fénye kockázatos (lásd 6.) |
| Időtállóság / eladási vonzerő | közepes: a rubin megosztó, de cserélhető textil | közepes-jó: semleges, de trendfüggő |

**Közös gyengeség (tény):** a két stílus **azonos elrendezést és azonos kanapét** használ (Blok 240 × 100 × 69). A különbség csak egy falitárgy, az asztal és a textilszín. Tíz stílus összevetésénél ez nem elég: a stílusoknak térbeli gesztusban (tömeg, ív, fény, keretezés) is különbözniük kell, nem csak dekorációban.

**Kihasználatlan, igazolt adottságok:** a teraszajtók **sötét antracit klinker kávája** és a világos tégla (IGAZOLT-F, `MUSZAKI_ELLENORI_ANYAG_KIVONAT` 3. és 5. pont), a 2,90 m belmagasság (fényvonal, magas tömegek), a többszintű tetőkert mint ülés-irány, és a belépési nézet. Egyik stílus sem épít rájuk.

**Ítélet:** mindkettő **megtartandó jelölt**, de a 10-es körben átdolgozva: Rubin kapjon egy tér-/forma-gesztust, Orbit egy meleg ellenpontot és jobb léptéket. A tervező értékelése (Rubin intimebb, Orbit kivitelezés-érzékenyebb) egyezik az enyémmel.

---

## 2. A 17,80 / 18,00 M Ft-os keret matematikája

**Újraszámolás (Python, 2026-10-24):**

| | Rubin | Orbit | Kiindulás (`KOLTSEG_KIINDULAS_A902.csv`) |
|---|---:|---:|---:|
| Nappali + étkező (03a–f) | 3,40 | 3,60 | 3,60 |
| Teljes tervezett költés | **17,80 ✔** | **18,00 ✔** | 18,00 |
| Tartalék | 2,00 | 2,00 | 2,00 (a 20 M 10%-a) |
| Költés + tartalék | 19,80 ✔ | 20,00 ✔ | 20,00 |

- A soronkénti összegek és a végösszegek **helyesek**. A tartalék-konvenció (a 20 M keret 10%-a = a költés 11,1%-a) egyezik a repóval.
- **Sor-mozgások a kiinduláshoz képest:**
  - Rubin: 03a −0,25 · 03c +0,05 · 03e −0,05 · 03f +0,05 · 11 (falfelület) −0,50 · új TV/AV +0,50 → **−0,20**.
  - Orbit: 03a −0,10 · 03c +0,05 · 03f +0,05 · 11 −0,50 · TV/AV +0,50 → **±0,00**.
- **Helyes lépés:** külön TV/AV-sor nyitása (a kiindulásból kimaradt). A 11-es sor 0-ra vétele csak akkor tartható, ha a többi helyiség stílusa sem kér tapétát vagy panelt. A 10 stílusnál ezt stílusonként kell kimondani.
- **Pontatlanság:** a „nappali fényrész 0,15–0,25 M” a teljes lakás 1,00 M-es világítási során belül van. Ezzel a többi helyiség világítása 0,75–0,85 M-re szűkül; ezt nem mondja ki.
- **Az érzékenységi számítás alulbecsül.** Astra +1,20 M-es kockázata helyes példa, de nem felső becslés. A kiindulási CSV saját sávjainak felső értékeiből:

| Kockázat (forrás: CSV „sáv” oszlop) | +M Ft |
|---|---:|
| 01 tervezés 0,40 → 0,80 | +0,40 |
| 02a–c konyha 2,90 → 3,90 | +1,00 |
| 13a jakuzzi Heissner → Correll | +1,00 |
| 13b emelés/daru 0,30 → 0,60 | +0,30 |
| 10 világítás 1,00 → 1,40 | +0,40 |
| 14 szállítás/szerelés 0,45 → 0,70 | +0,25 |
| **Együtt (legrosszabb eset, nem előrejelzés)** | **+3,35 → 21,15 / 21,35 M** |

A 18 M tervezhető keret tehát **csak akkor tartható, ha** a jakuzzi Heissner-szintű marad vagy kiesik, és a konyha a 2,90 M-es célon marad. Felfelé is van mozgástér (lásd 3.): a kanapé kb. −0,4 M, a 13e növények kb. −0,25 M (a tetőkert beültetve van). Ha a statika nem engedi a jakuzzit, −2,0 M szabadul fel.

---

## 3. Költségbecslések realitása – független ellenőrzés

| Tétel | Astra | Claude saját adat (forrás, dátum) | Delta / állapot |
|---|---|---|---|
| IKEA BESTÅ TV-állvány 004.740.70, 180×40×38 | 30 000 Ft | **30 000 Ft, de akciós; korábbi ár 44 990 Ft** ([IKEA HU](https://www.ikea.com/hu/hu/p/besta-tv-allvany-feher-00474070/), 2026-10-24) – **ellenőrzött** | tervezéshez a 44 990 Ft a biztonságos (+15 e) |
| Kave Home Blok 3 személyes 240×100×69 (ülés 41 cm) | 0,70–1,00 M, ár nem igazolt | **1 430 €** (Vepsäläinen, Észtország, beige, [link](https://www.vepsalainen.com/en/ee/kave-home-blok-sofa-w-240-cm-beige-7177000447/), 2026-10-24) × 366,16 Ft/€ ([mataf](https://www.mataf.net/hu/currency/converter-EUR-HUF), 2026-10-23) ≈ **524 e Ft**; HU-áfára átszámítva ≈ 536 e Ft + szállítás → **0,57–0,65 M (becslés)**. Méret és 5 csomag / 62 cm min. ajtó: [Kave Home BE](https://kavehome.com/be/fr/p/canape-dehoussable-blok-3-places-en-lin-blanc-240-cm) | Astra felső értéke **kb. +0,35–0,43 M-mal konzervatív**. HU-elérhetőség és a szürke kordbársony ára **nem igazolt** (a kavehome.com robots-tiltás miatt nem olvasható). |
| Ø140 kerek tükör + keret + szerelés | 0,28–0,45 M | Magyar készletben **Ø100 a legnagyobb kerek**: 35 900–68 900 Ft ([tukromata.hu](https://tukromata.hu/kerek-tukrok), 2026-10-24). Ø140-re készletet nem találtam → **egyedi üveges**. Fizika: 1,54 m², 4 mm ≈ 15 kg, 5 mm ≈ 19 kg + keret | ár **nincs adat** (üveges-ajánlat kell); a sáv elfogadható, nem igazolt |
| 3 × 60×120 kárpitpanel | 0,18–0,28 M | használható piaci adat nem jött (2026-10-24) | **kárpitos-ajánlat kell** |
| Tárcsaasztalpár Ø70/Ø45, HPL | 0,30–0,50 M | becslés: lap + HPL + íves élzárás + munka **0,15–0,30 M** | valószínűleg konzervatív; **asztalos-ajánlat kell**. Alternatíva: kész fészekasztal-pár |
| Függöny + sín (4,50 m üveg, 2 réteg) | 0,20–0,30 M | nincs saját adat | **konfekció + szerelés ajánlat kell**; rögzítés a 2,55–2,90 közti szemöldökre (fúrás a mennyezeti panelek miatt kerülendő) |
| Füstüveg asztal + kisasztal | 0,30–0,50 M | nincs saját adat ebben a körben | konzervatív sáv |

**Hiányzó árajánlatok (mindkét stílus, nappali):**
- kárpitos (triptichon);
- üveges (Ø140 tükör, biztonsági fólia, csiszolt él, rögzítés);
- asztalos (tárcsaasztalok, médiabútor-takarás);
- függönykonfekció + sín + szerelés;
- villanyszerelő (tükör mögötti LED, táp, kapcsolás, Hue-integráció);
- TV/AV (tartó, kábelvezetés).

**Teljes lakás szinten nincs ajánlat:** konyha (3 ajánlat), jakuzzi statika + daru, külső tervező díja. Ajánlatkérés csak Péter „mehet”-je után.

---

## 4. Kamera, ablakprofil, parketta, terasz

| Elem | Astra | Ellenőrzés | Eredmény |
|---|---|---|---|
| **20 mm, Cam_02** | (8,30; 4,40; 1,55), rot (1,4791; 0; 0,8577), 20 mm, 1600×1000 | `03_blender/geometry_lock_A902.json`: **pontosan egyezik** | ✔. Az `OPENAI_instructions.md` és a `05_promptok/gemini_prompts.md` 24 mm-e **elavult** → javítva (OPENAI) / jelölve. |
| **Fehér belső ablakprofil** | belül fehér, kívül antracit | IGAZOLT-F (`MUSZAKI_..._KIVONAT` 3. pont); de a `GOAL.md` 2. táblája és a `RENDER_REALITY_GATE.md` A pontja még „fekete” | ✔ Astra helyesen döntött. **Dokumentum-ellentmondás javítva** (GOAL, Gate). **Kockázat:** az input-kép (`A902_semleges_1_nappali.jpg`) fekete profilt mutat; szöveges felülírással a képgenerátor gyakran a képet követi → új alapkép kell (lásd 4.1). |
| **Parketta** | Egger Grey Treviso Oak EL2184, deszkaméret/irány nem kitalálva | dokumentumból igazolt; fotó (ME-BAL-080): közepes, szürkésbarna, erősen erezett, csomós tölgy, azonos dekorú szegőléc | ✔. A „cool grey” szó önmagában túl hideg: a fotón **szürkésbarna (greige-szürke)**. A semleges kép lapos szürke helyőrzője félrevezető. |
| **Teraszháttér** | a régi sík kert elavult; csak kamerára illesztett javított háttér | a v2 terasz-geometria létezik (`WSG_A902_v2_terasz_ELOZETES_20261024.blend`, ELŐZETES), Cam_02-re illesztett kép nem volt | ✔ a felismerés helyes, de a **javított háttérkép hiányzott** → Claude elkészíti (4.1). A valós panoráma (Budai hegyek, tetőtáj) csak a videó-panorámából (`A902_terasz_panorama_v0*`) jöhet. |

### 4.1 Javított geometria-alap (Claude, ebben a körben)

**KIMARAD (Péter döntése, 2026-10-24 07:38) – a B fázis előtt az ellenőrzött Blender-alap pótolja.** Tervezett fájl: `04_renderek/semleges/A902_semleges_v2_1_nappali.png`. A két próbarender a saját önellenőrzésemen elbukott (bézs fal, homokszínű, napfoltos padló), ezért nem került fel. Részletek: `03_blender/validator_report_2026-10-24_semleges_v2.md`.
- **Bemenet:** a v2 .blend repóbeli másolata. Az élő fájlhoz nem nyúltam.
- **Validátor:** 0 hiba (`03_blender/validator_report_2026-10-24_semleges_v2.md`).
- **Változás az eredetihez képest:**
  - fehér belső profil;
  - világosszürke ajtók;
  - fotóhoz hangolt padlótónus (deszkaminta nincs modellezve);
  - v2 tetőkert;
  - nap nélkül.

### 4.2 Új geometriai kockázat – teraszüvegezés (a pilot nem jelezte, mert nem látta)
A modell a nappali teraszüvegét **4,50 m folytonos, 3 egyenlő mezős, padlótól induló** üvegfalként tartja. A **ME-BAL-045** helyszíni fotón a terasz felé viszont **falpillérrel osztott két nyílás** (fix/üveg + ajtó) és **küszöb/párkány** látszik. A nagylátószögű fotó miatt nem egyértelmű. **Hétfői fotón és méréssel igazolandó**, mert a Cam_02 minden stílusképén ez a legnagyobb felület. Addig a promptban a „preserve glazing divisions” a modell feltételezését rögzíti, nem a valóságot.

---

## 5. Bútorozás és közlekedők – még nem igazolt méretek

2D-számítás a lock geometriájából (nem Blender-ütközésvizsgálat; a kanapé középre tett feltételezett helyzettel):

| Tétel | Érték | Állapot |
|---|---|---|
| Bal (nyugati) fal, nappali ↔ master | x 3,62–3,72 → **10 cm-es válaszfal** a modellben; hossz 3,93 m (y 4,04–7,97) | anyaga ismeretlen → a 15–19 kg-os tükör és a sín rögzítése **ellenőrizendő** |
| Kanapé 240×100 a nyugati falon, középen | x 3,72–4,72, y 4,81–7,20 | feltételezés |
| Kanapé É-i vége ↔ üvegfal-sarok | ~0,77 m | ha a nyugati mező a tolóajtó, **akadály lehet** (mezőfunkció nem ismert) |
| Kanapé–asztal 45–50 cm | asztal x 5,17–5,87 (Ø70) | geometriailag elfér |
| Átjáró → terasz (asztal és étkezőasztal x 8,15 között) | ~2,28 m | ✔ 2D-ben |
| **A nappali DNy-i sarka nyitott a közlekedő felé** (x 3,72–5,45, y 4,04: nincs fal a lockban) | ez az út a 05.1/05.2/fürdő felé | a kanapé déli vége és bármilyen déli falra tett bútor nem zárhatja; **Blender-teszt kell** |
| **TV helye** | a kanapé kelet felé néz (konyha/étkező); a déli falszakasz (x 5,55–7,40, 1,85 m) ~90°-ban oldalt van | **megoldatlan**. A pilot 0,50 M TV/AV-t és médiabútort számol, de egyik prompt sem mutat TV-t → Gate szerint render ≠ költségvetés |
| Padló síkeltérés | 7–8 mm (nappali, Kémeri) | állítható láb az alacsony tárgyaknál (Ø70×32 asztal!) |
| Függöny-pakett | Ny-i pillér ~0,78 m, K-i ~1,0 m (x 9,0–10,0) | ~1,0–1,1 m összes pakett elfér (becslés) |

A Validator egyetlen nappali-elrendezést mért eddig (`validator_report_2026-10-24.md`): a Zenit/LF réteget, ahol a kanapé a déli TV-fallal szemben áll (109 / 90 cm). A pilot elrendezése (kanapé a nyugati falon) **új, nem mért**.

---

## 6. Kivitelezési kockázatok stílusonként

**Rubin Szalon**
- Bársony-rubin színhűsége (nappal kékes északi fény, este 2700 K): ugyanabból a gyártási tételből kell a panel és a függöny, különben két vörös látszik.
- Panelrögzítés 10 cm-es válaszfalon: z-profil, a hézagok mérettűrése ±2 mm, különben „házi” hatás.
- Por és kopás a bársonyon; a vörös függöny UV-fakulása az üvegnél.
- Lépték: ha a panelek kicsik, „hotel-folyosó kép” lesz belőlük, nem építészeti gesztus.

**Ezüst Orbit**
- Ø140 tükör szállítása: 9. emelet; lift-kabin méret ismeretlen; az ajtón (90×210) élére állítva átfér.
- Tükör: 4 mm-nél torzít → 5–6 mm javasolt (≈19–23 kg), biztonsági fólia, csiszolt él.
- Rögzítés: 10 cm-es válaszfal.
- Halo-LED: távtartó, rejtett táp, villanyszerelő; egyenetlen fénynél olcsó hatás.
- A tükör a teraszüveget veri vissza: napközbeni vakítás, és AI-képen hamis kilátás.
- Tárcsaasztalok: íves HPL-élzárás műhelyképesség kérdése; 32 cm magas asztal a 7–8 mm-es padlón.

**Mindkettő**
- A TV hiánya a képen.
- A függönysín rögzítése (mennyezeti panelek).
- A Blok mint „hős” kanapé egyszerű hasábforma; a drágaság-hatás nagy része rajta múlik.

---

## 7. Szerepkör- és átadási megfelelés

| Szabály | Teljesült? | Megjegyzés |
|---|---|---|
| Astra kreatív + prompt + előzetes költség, nem Blender | ✔ | |
| Nem módosított GitHubot / Blendert, nem generált képet, nem indított AI-t, nem vásárolt kreditet | ✔ | a GitHub-mentést utólag Péter kérte |
| Nem választott stílust Péter helyett | ✔ | szubjektív összevetés jelölve |
| Modell nem állítva, ha nem igazolt | ✔ | „nincs felületi visszaigazolásom” |
| Bázis-commit megadva | ✔ | `4b4495a` – jó gyakorlat, kötelezővé tesszük |
| Reality Card, státuszok (KONCEPCIÓ / ELŐSZŰRT, nincs PASS) | ✔ | |
| Kamerazár elsőbbsége a 24 mm-es általános szöveggel szemben | ✔ | |
| `RESULT_TEMPLATE.md` fejléc (`WSG-ASTRA-RESULT: <ID>`, TELJES/RÉSZLEGES/BLOKKOLT, terméktábla cikkszám–ár–dátum–link) | ✗ részben | fejléc és státuszmező hiányzik; csak 1 cikkszámos ár (BESTÅ), a hős-kanapéé nincs |
| Bemenet a brief szerint | eltérés, **helyesen** | a pilot-ág briefje régi inputokat sorolt (stilusok.blend, r02, ai_gemini); Astra a frissebb A902_v1 + v1.1 csomagot használta, és ezt leírta |
| Átadás | **félkézi** | Work → chat → Péter kérésére a ChatGPT GitHub-kapcsolata írta a `main`-re (`f307765`). A PR-trigger útvonal továbbra sincs tesztelve. A PR #1-hez nem nyúltunk. |
| Claude visszavétel | ✔ (második körben) | az első körben a TXT-csatolmány nem érkezett meg, és a felhős munkamenetnek nem volt repó-hitelesítése; `add_repo` + klón után működik |

---

## 8. Tanulságok a következő körhöz

1. **A ChatGPT GitHub-kapcsolata tud fájlt írni a repóba** (igazolva: `f307765`). Ez a tartós átadás alapja: nem kell fájlt másolni. Új szabály: `ai-coordination/HANDOFF_PROTOCOL.md`.
2. **Gépi fejléc kötelező** az eredményfájlban: ID, bázis-commit, modell (vagy „nem igazolt”), státusz.
3. **A képinput erősebb, mint a szöveg.** Javított alapkép kell (fehér profil, valós padlótónus, v2 terasz). **Függő** (4.1).
4. **Az elrendezést Claude rögzíti előre** (két mért opcióval), hogy a stílusok ne egy nem mért, TV nélküli elrendezésre épüljenek.
5. **Hős-tételenként legalább 1 valós magyar webár** linkkel és dátummal, akció-jelöléssel (a BESTÅ-ár akciós volt).
6. **A stílusok térbeli gesztusban is különbözzenek**, ne csak dekorációban (gesztus-kategória mátrix a briefben).
7. **A teljes lakás érzékenységét a CSV-sávokból kell számolni**, nem példákból.
8. **Claude munkamenet-indítás felhőben:** először `add_repo` + friss klón. A Project tudásbázis pillanatkép, és ma nem tartalmazta a v1/v1.1-et és a Gate-et.

---

## 9. Összevetés a Codex geometriai auditjával (draft PR #2, `62ad37c`, sha256 `dbe51229…`)

A két audit egymástól függetlenül készült. Ahol egybeesnek, ott erősítik egymást; ahol a Codex-audit többet mond, az felülírja az enyémet.
- **Kamera:** egyezik. A lock 20 mm-e helyes, a 24 mm elavult. **Kiegészítés:** a validátor az objektívet, szenzort, shiftet és az aktív kamerát nem ellenőrzi. Az én „pontosan egyezik” állításom csak a lockban tárolt értékekre igaz, nem teljes kamerazár.
- **Validátor:** a „0 hiba” a v1 lockhoz való egyezést jelenti, nem a valósághoz valót. A v2 terasz-gyűjteményt nem vizsgálja, a 05.2 erkélyajtót kihagyja. Ez érvényes az én `validator_report_2026-10-24_semleges_v2.md` riportomra is.
- **Teraszüvegezés:** a terv szerint 2,53 m magas (modell 2,55). Nyitható mezők, nyitásirány és küszöb nem validált (15 cm-es fellépés). Ez egybevág a 4.2 pontban leírt fotós megfigyeléssel. **Bizonytalan marad.**
- **Nappali hossza:** v2 terv szerint 7,08 m (v1 6,92). Az 5. pont 2D-számítása v1-en készült; a v2-n +16 cm.
- **Új, a pilotot nem érintő, de a lakásszintű stílusokat érintő korlátok:**
  - konyha: 85 cm munkalapköz;
  - 05.2 ajtó-előtér;
  - terasz: szegély a WPC-nyelv előtt, hiányzó út az északi pihenőhöz.

  Mindegyik felvéve a STYLE10-002 brief K1–K6 korlátai közé.

## 10. Péter döntésére váró kérdések
1. Legyen-e TV a nappaliban? Ha igen: L1 elrendezés (kanapé a nyugati falon) TV-megoldással, vagy L2 (déli TV-fal, kanapé vele szemben)?
2. Indítható-e a 10 stílusos Astra-kör **A fázisa** (`ai-coordination/requests/WSG-20261024-STYLE10-002.md`)? Jelenleg **NEM INDÍTOTT**. A B fázis zárolva az ellenőrzött Blender-alapig.
3. Bekapcsoljuk-e Claude oldalán az ütemezett eredmény-ellenőrzést (`HANDOFF_PROTOCOL.md` 6. pont)?
4. Mergeljük-e a Codex PR #2-t a `main`-be? Akkor Astra közvetlenül is olvashatja.

# WSG-20261024-ASTRA-KREATIV-V2 – A-902: tíz luxusstílus négy helyiségre – kreatív belsőépítészeti terv + 40 renderprompt (Astra **MEDIUM**)

- **Task ID:** `WSG-20261024-ASTRA-KREATIV-V2` · fájlnév `WSG-ASTRA-HIGH-KREATIV-V2.md` Péter 2026-10-24 19:17-es kérése szerint. **A névben szereplő „HIGH” történeti; a tartalom MEDIUM-szintű** (Péter 19:34, kötelező kreditkorlát). High/Ultra/Max: **TILOS** külön új engedély nélkül.
- **Indítás: INDÍTÁSRA KÉSZ – NEM INDÍTOTT, Péter külön engedélyére vár** (frissítve 2026-10-24 21:15: négyhelyiséges scope, kizárólag kreatív tervezés + promptírás). Automatikus felvétel TILOS. Csak Péter indítja. **Indítás előtt a futtatófelületen a Medium szint ellenőrizhetően be van állítva; ha nem állítható vagy nem igazolható, a feladat nem indul** – jelezni kell.
- **Cél AI:** ASTRA_WORK (ChatGPT Work), **MEDIUM**. Az 1. rész (lezárás) Astra nélkül megtörtént; a 2. rész futtatásának helyét (eredeti szál folytatása vagy új szál) Péter dönti el az indításkor. Átadás böngészőben (Péter beilleszti; Claude csak külön engedéllyel), az eredmény GitHubra.
- **Típus:** **STYLE_CONCEPT + RENDER_PROMPT – kizárólag kreatív belsőépítészeti tervezés és képgenerálási promptírás.** Nincs újrakutatás, nincs költség-újraszámolás, nincs projektadminisztráció (ezeket Claude végzi). **Kép, videó, Blender: nincs.**
- **Lakás:** A-902, **négy helyiség stílusonként**: 1 nappali–terasz (Cam_02) · 2 konyha–étkező (Cam_03) · 3 master háló 05.1 (Cam_04) · 4 fürdő **06.2** (javasolt; Péter dönthet 06.1-ről) új, rögzített kamerával (Cam_10, javaslat a sablonban). A-811/A-812 adatai csak referenciaként (2.5), scope nem bővül rájuk.
- **Bázis:** a `main` legfrissebb állapota (a ténylegesen olvasott commit az eredménybe kerül).
- **Előzmény, kötelező:** **`ai-coordination/results/WSG-20261024-STYLE10-002.md` – Astra eredeti, TELJES A-fázisú eredménye (elsődleges kreatív forrás, nem kutatjuk újra)** · `ai-coordination/audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md` (Péter 21:04: az audit, a termékkutatás, a Kave Home + Westwing összevetés és a geometriai korlátok **jóváhagyott kiindulás**) · `ai-coordination/inputs/STYLE_CLAUDE_ASTRA_FORRASOK_20261024.md` (A: Claude keretrendszer, B: Astra tíz stílusa, P: Péter irányai, C: összevetés, D: közös tízes) · `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` (a 40 prompt sémája és fixed blokkjai) · történeti: `results/WSG-20261024-STYLE10-002_RELAY_RESZLEGES_20261024.md`, `requests/WSG-20261024-STYLE10-002.md`.

---

## 1. RÉSZ – A STYLE10-002 A fázis lezárása: **LEZÁRVA 2026-10-24 20:20–20:30, Astra-futtatás nélkül**

**Tény:** Astra 2026-10-24-én elkészítette a tíz koncepciót, a rangsorokat, a három döntőst és a költségellenőrzést; a saját GitHub-mentése nem történt meg. 20:20-kor Péter előkerítette és csatolta a **teljes, eredeti** eredményfájlt (712 sor, SHA-256 `f94acf93b71440837808df2a1f54bab927609e24649c0d29076b34f7fed86189`); Claude ellenőrizte (1–475. és 517–712. sor betűre azonos a pillanatkép-relayjel; a 476–516. sor a 7. fejezet), és **változatlanul** a repóba tette: `ai-coordination/results/WSG-20261024-STYLE10-002.md`. A korábbi relay (`…_RELAY_RESZLEGES_20261024.md`) történeti bizonyíték.

**A fázis teljességi ellenőrzése az eredeti brief kért kimenetei szerint (Claude):** stíluskártya ✔ · teljes lakás 8 helyiségre ✔ · WOW-próba ✔ · hős-termékek HU webárral ✔ részben (Kave Home hiányzott, P15 gyenge – azóta az audit igazolta) · költség Δ ≤ 18 M (5. + 7. fejezet) ✔ · feltételes elemek ✔ · „30–50 %” ✔ · 8 szempontú profil ✔ · összehasonlító táblák, top 3, 16 kérdés, 10 B-prompt-tervezet ✔ · kép/videó/Blender/rendelés nem készült ✔. **Ítélet: a STYLE10-002 A fázis tartalmilag TELJES (KONCEPCIÓ – NEM VALIDÁLT; költség ELŐSZŰRT – FELTÉTELES).** Claude célzott auditja (21:00) átvezetve a 2.0 pontban.

---

## 2. RÉSZ – Astra Medium kreatív feladat: tíz stílus × négy helyiség + 40 renderprompt

### 2.0 Elsődleges cél és határok (Péter 20:34, 21:02, 21:04, 21:05)

1. **ELSŐDLEGES CÉL:** mind a tíz stílus **kivételes, egymástól radikálisan különböző, a Zenit/Lake Forest eredeti legerősebb látványainak WOW-szintjét elérő vagy túlszárnyaló** kreatív továbbfejlesztése – **négy összehangolt helyiségre**: nappali–terasz, konyha–étkező, master háló, fürdő. A háló és a fürdő **ne a nappali színeit ismételje**: önállóan is luxushatású, különleges, mégis egy stílus-DNA-t hordozó terek legyenek. A Zenit/LF WOW-szint **minden fő helyiségben** minimumelvárás.
2. **Kreditet nem költünk** újraszámolásra, általános projektadminisztrációra és már elvégzett termékkutatásra: a 7. fejezet összegei, az árkönyvtár, a Kave Home/Westwing jelöltek és a geometriai korlátok **jóváhagyott kiindulás** (audit). Astra a termékeket átveszi, nem kutatja újra; a költségsorokat csak megnevezi (melyik sor, melyik sáv), nem számol újra – Claude ellenőrzi.
3. **Differenciálási mátrix – kötelező minőségi követelmény** (audit H1, 2. pont táblája): egy (kanapé-sziluett, elrendezéscsalád, étkező-geometria) hármas csak egyszer; elsődleges gesztus-kód stílusonként (A–I; egy kód legfeljebb 2×, legalább 7 kód). **Astra javasolhat az árkönyvtárban nem szereplő, valós és megvásárolható Westwing/Kave Home-terméket is**, ha az jelentősen erősebb luxuskompozíciót ad – ekkor **teljes termékrekord** kötelező (gyártó/modell, konfiguráció/sarokirány, külső méret, szín/anyag, termékoldal, dátumozott ár, státusz); a konkrét méret és a kivitelezhetőség (befoglaló, utak, kiállások) ettől nem sérülhet.
4. **U csak L3** (audit H2): U kanapé a P902_24A étkezővel kizárólag nyugati TV-vel fér el; L2 (déli TV) csak L-kanapéval.
5. **Kave Home és Westwing egyenrangú főbútorforrás** (kanapé, íves/moduláris bútor, asztal, szék, ágy); IKEA a vázakhoz (METOD/PAX/BESTÅ + stílusfront); asztalos forma-darab lakásonként 1–3.
6. **Képeket most NEM generálunk.** A képfázis külön, később jóváhagyandó feladat: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004.md` (két részben, kalibrációval). A V2 kimenete a 40 renderprompt, amelyet a képfázis **változatlan fixed blokkokkal** használ – az A fázis eredeti stíluspromptjai (eredmény §10) elavultak, nem használhatók változatlanul.
7. **Kreatív minőség fontosabb a promptok mennyiségénél:** ha egy stílus valamelyik helyisége nem éri el a küszöböt, Astra ezt mondja ki és fejleszti tovább, ne adjon át gyenge promptot. A 40 prompt nem öncél.
8. **MEGŐRZÉS – nem újrakezdés (Péter 21:08):** a STYLE10-002 teljes eredménye, Astra tíz eredeti stíluspromptja (eredmény §10), a Cam_02 v2 sablon (`05_promptok/A902_STYLE10_Cam02_prompt_sablon_v2.md`) és a korábbi Zenit/Lake Forest kreatív referenciák (`06_koncepcio/`, `04_renderek/ai_chatgpt/`, `ai_gemini/`, `blender_stilusok/`) **változatlanul maradnak; a V2 ezekből indul ki és nem írja felül őket.** Az eddigi legjobb kreatív elemek megőrzése elsődleges: a legjobb eredeti megoldást nem cseréljük le pusztán az egységesítés kedvéért. A régi és az új promptok **külön, verziózott fájlokban** élnek (eredeti: eredmény §10 = v1; Claude Cam_02 kiegészítések: sablon v2; Astra V2 promptjai: új fájl, lásd 2.7). Minden stílushoz **rövid változásjegyzék**: mi maradt meg az eredeti koncepcióból és promptból, mi lett továbbfejlesztve és miért.

### 2.1 Mit kérünk egy mondatban

A STYLE10-002 kész tízes mezőnyét **nem újrakutatva**, a jóváhagyott audit-kiindulásra építve: **stílusonként egy stílus-DNA, négy helyiség kreatív terve és helyiségenként egy részletes, azonnal futtatható angol renderprompt (10 × 4 = 40 prompt)** a `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` sémájában – Zenit/LF WOW-szinten, egymástól megkülönböztethetően, valós termékekkel, a friss geometriával. **Nem szűkítünk előre háromra:** a döntősöket Péter a teljes négyhelyiséges látványvilág alapján választja a képfázis után; Astra rangsora csak javaslat.

### 2.2 Kötelező olvasnivaló (friss `main`)

1. `GOAL.md` (2., 3., 5., 10. pont), `CLAUDE.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`, `ai-coordination/RENDER_REALITY_GATE.md`, `ai-coordination/HANDOFF_PROTOCOL.md`.
2. **Kreatív források:** a teljes Astra-eredmény (`results/WSG-20261024-STYLE10-002.md`, 12 fejezet) és `ai-coordination/inputs/STYLE_CLAUDE_ASTRA_FORRASOK_20261024.md` (A: Claude keretrendszer – gesztus-mátrix A–I, elrendezéscsaládok, Zenit/LF fordítótábla, méretpróbák; B: Astra tíz stílusa; P: Péter szó szerinti irányai; C: összevetés; D: közös tízes). **Claude oldalán nem tíz megnevezett stílus van, hanem ezek a kreatív-műszaki bemenetek – teljes értékű forrásként kezelendők, utólag kitalált „Claude-stílusok” nélkül.**
3. **Audit és termékek:** `ai-coordination/audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md` (H1–H8; 2. pont differenciálási mátrix; 3. pont méretpróba; **4. pont Kave Home-tábla**), `ai-coordination/inputs/A902_v2b/ARKONYVTAR_A902_2026-10-24.csv` (87 igazolt jelölt).
4. **Geometria és kamerák:** `03_blender/geometry_lock_A902_v2b.json` (**v2b-1**), `03_blender/geometry_v2/kamera_parameterlap_v2b.md` (Cam_02/03/04), `03_blender/geometry_A811_A812/meretproba/MERETPROBA_KANAPE_A902.md` (**P902_24A**), `01_alaprajzok/villamos_kiallasok/` (A902 pontazonosítók), **`05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md`** (helyiség-kamerák, fixed blokkok, fürdő 06.2 adatai és javasolt Cam_10).
5. **Képi alap (tájékozódás):** `04_renderek/A902_alap_v2b/` (Cam_02/03/04, bútor nélkül) + reality card; `04_renderek/semleges_v2b/` ellenőrző rajzok; fürdő/terasz/anyag fotók `08_allapotfelmeres/fotok/A902/` (06-1_furdo, 06-2_furdo, 04_nappali ME-BAL-045/080); Zenit/LF eredeti látványok `04_renderek/ai_chatgpt/`, `04_renderek/ai_gemini/`, `04_renderek/blender_stilusok/` (KONCEPCIÓ – NEM VALIDÁLT, de **ez a WOW-minimum referenciája**).
6. **Költségkeret (csak tájékozódás, nem újraszámolásra):** `ai-coordination/inputs/A902_v1/KOLTSEG_KIINDULAS_A902.csv`, az eredmény 5. és 7. fejezete; fürdők+WC együtt 07 = 0,50 M (0,30–0,70); master 04a–04d ≈ 1,80 M; konyha 02a–c 2,90 M; étkező 03d 0,60 M.

### 2.3 Kreatív minőségi küszöb (Péter, 2026-10-24 19:42, 21:02) – kötelező

- **A Zenit és Lake Forest legjobb korábbi látványai a MINIMUM** minden fő helyiségben, nem a felső korlát: térélmény, karakter, elegancia, rétegzettség, érzelmi hatás – elérni vagy túlszárnyalni, nem másolni.
- **Nem fogadható el olcsóbbnak kinéző változat.** Először a kivételes forma / tér / anyag / fény megoldás, utána a költséghatékony, valós, ellenőrizhető árú kivitel azonos karakterrel.
- **Összevetés azonos szigorral és azonos kamerával** (Cam_02/03/04/10, 1600×1000, semleges nappali fény; esti sorozat külön, később). A meleg fény, színes párna vagy egy tükör önmagában nem minőségi bizonyíték.
- **Nem tíz átszínezett egyforma lakás:** a domináns bútorsziluett, térarány, anyagtapintás, fény és negatív tér együtt adja a luxust; két stílus, amely csak színben tér el, nem léphet tovább (legközelebbi párok: LA–Desert, Kyoto–Zenit).
- **Helyiségek közti koherencia és önállóság:** egy stílus négy helyisége egy anyag- és színvilágot, egy gesztuscsaládot hordoz, de mindegyiknek saját kompozíciója és legalább egy helyiség-specifikus szignatúra-eleme van (pl. master: fejvég-kompozíció és fényhangulat; fürdő: tükör–fény–textil–egy tárolódarab a meglévő burkolaton; konyha: frontritmus és pult–étkező viszony).
- Belső ellenőrzés mind a 40 helyiségtervnél Péter 8 kérdésével (P-gyűjtemény P4). **Ha nem felel meg: továbbfejleszteni, nem átadni.**
- „Mi szeressünk bele. Teremtsünk értéket.”

### 2.4 A tízes mezőny – 7 kötelező + 3 javasolt (nincs eldöntött stílus, Péter dönt)

| Hely | Irány | Eredet | Feladat a V2-ben |
|---|---|---|---|
| 1 | **Kortárs japán luxus** – Kyoto Ink (S01) | Péter → Astra | megerősíteni; „ne legyen bézs Japandi” |
| 2 | **BiBo Budapest-ihletésű mélykék, tükröződő, szobrászati** – BiBo Nocturne (S02) | Péter → Astra | valódi U L3-ban; hős-kanapé a küszöbhöz mérve; **inspiráció, nem másolat** |
| 3 | **Alelí Budapest-ihletésű terrakotta, kézműves, mediterrán-olasz** – Alelí Casa (S03) | Péter → Astra | erősíteni, ne átlagos mediterrán; **inspiráció, nem másolat** |
| 4 | **Los Angeles Skyline** – LA Horizon (S04) | Péter → Astra | elkülöníteni S10-től; L2 csak L-kanapéval; K5 teraszüveg |
| 5 | **Miami Art Deco** – Miami Streamline (S05) | Péter → Astra | időtállóság; bordázat K6 |
| 6 | **Zenit továbbfejlesztve** – Zenit Atelier (S06) | Péter → Astra (Claude fordítótábla) | a Zenit eredeti látványának szintje felett |
| 7 | **Lake Forest továbbfejlesztve** – Lake Forest Couture (S07) | Péter → Astra (Claude fordítótábla) | Wolke 258×167 bal sarok igazolt; íves alternatíva Martina + Neom puff |
| 8 | Milano Radical (S08) | Astra javaslat | megtartani; zsúfoltság ellen; valódi U L3-ban |
| 9 | Paris Collector (S09) | Astra javaslat | **megerősíteni vagy cserélni** – konkrét kép- és fotelpár nélkül nem elég; alternatíva-javaslat (cím-szintű): I-gesztusú terasz-folytonosság/biofil penthouse vagy D-gesztusú fényarchitektúra |
| 10 | Desert Modern 70 (S10) | Astra javaslat | elkülöníteni S04-től vagy javasolni összevonást |

Rubin Szalon és Ezüst Orbit: dokumentált pilotok, nem kötelező résztvevők. **Mindkét gyűjtemény forrás marad**, a V2 ezekre hivatkozik, nem írja felül. **Gesztus-ellenőrzés:** egy kód legfeljebb 2× elsődleges, ≥7 kód, legfeljebb 2 stílus azonos fő akcentszínen; D (fényarchitektúra) és I (terasz-folytonosság) jelenleg üres – jelezni és kezelni.

### 2.5 Műszaki alap – rögzített valóság (nem kreatív döntés)

- **A-902 általános:** v2b-1 lock; belmagasság 2,90–2,93 m; fehér fal/mennyezet, **belül fehér** nyílászáró, kívül antracit; szürke ajtó fekete kilinccsel; **Egger Grey Treviso Oak EL2184** laminált (szegőléc 6 cm) a lakótereken; mennyezeti hűtő-fűtő mezők → nincs álmennyezet, nincs mennyezeti fúrás a mezőkbe; fény és áram **csak meglévő kiállásra** (A902-ML/FL/D azonosítók); valós budai panoráma.
- **Nappali–terasz (Cam_02):** 7,08 m tagolt kontúr, DNy-sarok nyitott; 10 cm-es nyugati válaszfal; **P902_24A** (U 3,00×2,40 befoglaló, TV felé nyitva, asztal −0,30 m); **U csak L3**; terasz gres −0,15 / WPC +0,62 / zöldtető.
- **Konyha–étkező (Cam_03):** konyhabútor nincs – IKEA METOD-váz + stílusfront a tervi kiosztáson; **K1:** a két pultsor közti köz 85–86 cm (<90), FELTÉTELES; tartalék: egyoldali gépsor + 45 cm-es száraz tároló; a ~85 cm-es nyugati mellvédfal marad; gépek a 02b sorban; étkező = ugyanaz az asztal/szék, mint a nappaliképen; ML04 az asztal fölött (−0,30 m-rel elcsúszva még az asztal fölé esik).
- **Master 05.1 (Cam_04):** 3,57×5,50 m (4,00 tiszta + gardróbfülke); ágy 180×200 valós külső mérettel; 60 cm az ágy mellett; D20–23 (fejvég), D26 (fülke), ML06; 3,65 m-es üvegfal + erkélyajtó, redőny; PAX-váz + front a gardróbhoz.
- **Fürdő 06.2 (Cam_10 – javasolt):** 1,925×2,85 m; ajtó a nyugati falon (y 6,33–7,02); **meglévő és megőrzendő:** nagyformátumú világos meleg szürke kőhatású lap padlón és falon, épített walk-in zuhany 182×85 vonalas lefolyóval, fekete esőztető, csaptelep, törölközőszárító, nyomólap, mosdó, WC; lámpakiállás a mosdó fölött. A stílus csak hozzáad: tükörkompozíció, fény a meglévő ponton, egy szabadon álló vagy falra függesztett tároló a szabad zónában, textil, kiegészítők, növény. Nincs újraburkolás, új fülke, új gépészet. (Alternatíva 06.1: 1,75×2,65, kád 170×70 – Péter dönt.) **A Cam_10 még nincs a lockban: Claude rögzíti és rendereli a bútor nélküli alapot Péter „mehet”-jével – a V2 promptjai a sablon javasolt kameráját használják, a végleges paraméter a képfázis előtt kerül be.**
- **K1–K10** továbbra nyitott; helyszíni fotók (≈60, 2026-10-25/26) és Szakos Andrea bútorozott alaprajzai még nincsenek → ezekre épülő részlet FELTÉTELES.
- **Tilos:** fiktív fal, nyílás, kilátás, padló, burkolat, szaniter, kiállás; új mennyezeti szerkezet; rejtett építés; „lebegő” bútor valódi rögzítés nélkül; generikus skyline.
- **A-811 / A-812 (csak referencia):** 8. emelet, 2,69–2,73 m, Egger Grey Soria Oak EL2065; A-811 L 2,59×2,50 + 60 cm szekrénysor (T0SZ60_50); A-812 U 3,00 m + 60 cm fülkeszekrény (P812U); 10–10 M Ft.

### 2.6 Termék-, anyag- és költségszabályok (röviden – a részletes ellenőrzés Claude-é)

- Látszó darabok **Kave Home és Westwing** egyenrangúan (ágy is: pl. Kave Home Selven/Martina/Nahiri 180×200 vs. IKEA NORDLI P10), váz IKEA, forma-darab asztalos. Az audit 4. pontjának és az árkönyvtárnak a jelöltjeit **átveszi**; új jelöltet csak teljes termékrekorddal (2.0/3).
- Minden hős-tételhez termékrekord (konfiguráció/sarokirány!), státusz **ellenőrzött / becsült / ajánlatköteles / nem igazolt**. Ismeretlen ár nem nulla.
- **Kanapé:** minimum L, lehetőleg valódi U (csak L3); félhold/ívelt + puff alternatíva a befoglalón belül.
- **Költség – csak megnevezés, nem újraszámolás:** stílusonként melyik költségsorhoz tartozik a hős-tétel és a helyiség szignatúra-eleme, és a 7. fejezet szabad helyén belül marad-e; ami a sor plafonja felett van (pl. Kave Home Gala U ≈1,32 M a 03b 1,00 M felett; fürdő 07 = 0,50 M két fürdőre + WC), **PREMIUM-jelöléssel** külön, soha csendben. Claude számol újra.

### 2.7 Kért eredmény (stílusonként, magyarul a terv, angolul a promptok)

Kimenet: **új fájl** `ai-coordination/results/WSG-20261024-ASTRA-KREATIV-V2.md` (RESULT_TEMPLATE fejléc: `WSG-RESULT`, Szerző-AI, Modell | nem igazolt, Bázis-commit, Státusz), semmit nem ír felül. Tartalma stílusonként (S01–S10):

1. **Stílus-DNA (3–5 mondat):** anyag- és színvilág, gesztuscsalád, a négy helyiség közös nyelve; mi a stílus egyetlen, első pillantásra felismerhető identitása.
2. **Négy helyiségterv** (nappali–terasz · konyha–étkező · master · fürdő 06.2), mindegyikhez: kompozíció (tömegek, arányok, negatív tér), **a helyiség saját szignatúra-eleme** (1–2 domináns WOW-elem, valós termék vagy gyártható megoldás méretével), hős-termékek rekorddal (Kave Home és Westwing), egyedi darab(ok) rövid gyártható leírása, fény a meglévő pontokon, érintett költségsor(ok) és FELTÉTELES-jelölések (K-kódok), kerülendő giccs és a többi stílustól való elhatárolás.
3. **Négy renderprompt angolul** – a sablon 4. pontjának sémája szerint (`### Sxx — <Név> · <helyiség> (Cam_xx)` + Style DNA / Room composition / Products / Custom pieces / Light / Avoid / Output), **a sablon fixed blokkjait nem ismételve, azokra hivatkozva**. A prompt a megerősített koncepciót írja, nem az A fázis szövegét.
4. **Differenciálási megfelelés** egy sorban: elsődleges gesztus-kód, kanapé-sziluett, elrendezéscsalád, étkező-geometria – és a legközelebbi stílustól való eltérés egy mondatban.
5. **Változásjegyzék (3–6 sor):** az eredeti Astra-koncepcióból (eredmény §6) és az eredeti promptból (§10) **mi maradt meg változatlanul**, mi lett továbbfejlesztve és miért (küszöb, differenciálás, geometria, termékrekord); a megtartott legjobb elemek kimondva.

**Fájlok:** a terv és a változásjegyzékek a fenti eredményfájlban; **a 40 prompt külön, verziózott fájlban is:** `05_promptok/A902_STYLE10_4helyiseg_promptok_ASTRA_V2_r1.md` (új fájl; az eredeti §10 promptok és a `…Cam02_prompt_sablon_v2.md` érintetlenek). Ha Astra később javít: `_r2`, nem felülírás.

A fájl végén: a tíz stílus **összehasonlító táblája** (gesztus, hármas, négy helyiség szignatúrája), a differenciálási szabály teljesülésének ellenőrzése, Astra **javaslata** a két legkarakteresebben eltérő stílusra a képfázis 1. üteméhez (Péter dönt), nyitott kérdések Claude-nak (max. 10), és a szokásos záró státusz. **Nincs:** újraszámolt költségtábla, rangsor-újraírás, új termékkutatás a már igazolt tételekre.

### 2.8 Tilalmak és átadás

- Nincs új tízstílusos kutatás, képgenerálás, videó, Blender-módosítás, rendelés, ajánlatkérés, külső levél. Nincs High/Ultra/Max, extra kredit, párhuzamos munkamenet.
- Minden állítás forrással; „ellenőrzött” / „becslés” / „nem igazolt” jelöléssel; v2b-1 nem helyszíni validáció.
- Mentés új fájlba, commit után visszaolvasás; a chatben: lényeg, fennmaradó kockázat, ellenőrzött commit. A GitHubra mentett fájl az átadás.
- Péter döntései indítás előtt: (a) fürdő **06.2** vagy 06.1; (b) S09 csere / S10 összevonás nyitva maradjon-e; (c) eredeti szál vagy új szál; (d) Medium igazolása a felületen.

### 2.9 Indítómondat (egyetlen; csak Péter küldi, Medium igazolása és külön engedélye után)

> WSG: dolgozd fel a `WSG-20261024-ASTRA-KREATIV-V2` feladatot a GitHubról (`ai-coordination/requests/WSG-ASTRA-HIGH-KREATIV-V2.md`, 2. rész) Medium szinten: kizárólag kreatív tervezés és promptírás – a STYLE10-002 kész tíz koncepciójára építve, újrakutatás és újraszámolás nélkül, mind a tíz stílushoz nappali–terasz, konyha–étkező, master és fürdő kreatív terve plus helyiségenként egy részletes renderprompt (40 prompt) a `05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md` sémájában; képet ne generálj; mentsd az eredményt a repóba új fájlba.

---

**Státusz: INDÍTÁSRA KÉSZ – NEM INDÍTOTT (Péter külön engedélyére vár).** Készítette: Claude, 2026-10-24 este; frissítve 20:30 (teljes Astra-eredmény), 21:00 (Claude-audit), 21:15 (négyhelyiséges scope, kizárólag kreatív tervezés + 40 prompt, Péter 20:34–21:05 pontosításai). A korábbi STYLE10-002 és STYLE4-003 briefeket nem írja át, hanem hivatkozik rájuk.

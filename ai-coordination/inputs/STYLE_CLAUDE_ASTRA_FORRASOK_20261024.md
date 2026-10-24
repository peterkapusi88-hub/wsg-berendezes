# STYLE_CLAUDE_ASTRA_FORRASOK_20261024 – a két „tízstílusos” anyag forráskatalógusa és összevetése (A-902)

- **Típus:** forráskatalógus + összehasonlító mátrix + döntés-előkészítés. **Nem új tervezés, nem stílusjavaslat.**
- **Készítette:** Claude (operatív projektvezető), 2026-10-24 este. **Bázis:** `main` @ `09e86c217ce990933970043af757ad750f84b9f1` (2026-10-24 19:03).
- **Szabály:** semmit nem találunk ki; ami hiányzik, az „HIÁNYZIK” jelölést kap. Cím-szintű ötlet nem számít kész koncepciónak, és nem kap teljes pontszámot.
- **Kapcsolódó fájlok:** **Astra eredeti, TELJES eredménye: `ai-coordination/results/WSG-20261024-STYLE10-002.md`** (712 sor, SHA-256 `f94acf93…`; Péter csatolta 2026-10-24 20:20; bájtra változatlan) – **ez az elsődleges kreatív forrás.** Történeti bizonyíték: `ai-coordination/results/WSG-20261024-STYLE10-002_RELAY_RESZLEGES_20261024.md` (a megosztott szál pillanatképe, 7. fejezet nélkül; nem elsődleges forrás) · folytató brief (MEDIUM, NEM INDÍTOTT): `ai-coordination/requests/WSG-ASTRA-HIGH-KREATIV-V2.md` · eredeti brief: `ai-coordination/requests/WSG-20261024-STYLE10-002.md`.

---

## 0. Összefoglaló öt tényben

1. **Claude „tíz stílusa”: 0 megnevezett stílus.** Claude a STYLE10-002 brief szerint *„stílust nem javasol”* (brief 1. pont); ami tőle van: keretrendszer – 9 kategóriás gesztus-mátrix, L1/L2/L3 elrendezéscsaládok, K1–K10 korlátok, B-fázisú promptsablon, 4 stílusos költség-előszűrés 87 soros árkönyvtárral, Zenit/Lake Forest fordítótábla, méretpróbák (P902_24A). Ezek **ellenőrző- és bemeneti anyagok**, nem koncepciók.
2. **Astra tíz stílusa létezik:** S01 Kyoto Ink … S10 Desert Modern 70, mindegyik teljes lakásos recepttel, HEX-palettával, főbútor-jelölttel (P01–P15b), WOW-táblával és költségsávval; közös költségmodell, **stílusonkénti költségeltérés és stresszteszt (7. fejezet)**, 4 rangsor, 3 ajánlott döntős + 1 tartalék, 16 kérdés Claude-nak, 10 nem futtatható B-prompt. **Státusz: TELJES** – az eredeti fájl 2026-10-24 20:20-kor előkerült (Péter), bájtra változatlanul a repóban; Astra saját GitHub-mentése nem történt meg; modell/gondolkodási szint nem igazolt. Korábbi állapot (19:45–20:19): csak a megosztott pillanatkép, 7. fejezet nélkül → relay, RÉSZLEGES.
3. **A tízes mezőny 7 kötelező irányát Péter adta** futás közben (japán, BiBo, Alelí, LA Skyline, Miami Art Deco, Zenit, Lake Forest), a kreatív minimummal („Zenit/LF látványminősége a küszöb”) együtt; Astra a 8–10. helyre Milano Radical, Paris Collector, Desert Modern 70 irányokat javasolt.
4. **Megnevezett, kidolgozott irány összesen 12:** Astra 10 + a két pilot (Rubin Szalon, Ezüst Orbit; eredmény + Claude-audit + költség-előszűrés van hozzájuk). Claude-tól 0 új név, de 9 gesztuskategória és 2 referenciairány (Zenit/LF) költséghű fordítása.
5. **Közös tízes javaslat (nem döntés):** Astra S01–S10 változatlanul – a 7 kötelező benne van, a 3 javasolt kidolgozott; Rubin/Orbit marad dokumentált pilot (Péter 19:34: nem kötelező résztvevő). Két összecsúszás-gyanús pár (LA–Desert, Kyoto–Zenit) és két kihasználatlan gesztuskategória (D fényarchitektúra, I terasz-folytonosság) külön döntési pont.

---

## A. CLAUDE 10 STÍLUS – ami ténylegesen létezik (A-gyűjtemény)

| # | Elem | Hol található (fájl @ commit) | Tartalom röviden | Státusz | Hiány / megjegyzés |
|---|---|---|---|---|---|
| A1 | **Gesztus-mátrix A–I** (kötelező sokszínűség) | `ai-coordination/requests/WSG-20261024-STYLE10-002.md` @ `1bda13e` (2026-10-24 07:45), 2. pont; **eltávolítva** @ `a62a552` (kétfázisú átírás) → ma csak a git-történetben | 9 elsődleges luxusgesztus: **A** textil-/színmező (falon álló tárgy, nem festés) · **B** tükröző vagy geometrikus objekt · **C** beépített hatású tömeg (IKEA-váz + takarás / asztalos forma-darab) · **D** fényarchitektúra · **E** panoráma-keretezés · **F** szobrászati bútor · **G** anyagritmus (bordázat, kőfurnér, lamella) · **H** galéria / műtárgy-kuráció · **I** természet / terasz-folytonosság. Szabály: egy kategória legfeljebb 2× a tízben, legalább 7 különböző; legfeljebb 2 stílus azonos fő akcentszínen. | KERETRENDSZER | Nem stílus. A mai briefből kimaradt; a C. pontban Astra tízesének ellenőrzésére használjuk. |
| A2 | **Elrendezéscsaládok** | L1/L2 @ `1bda13e` 4. pont; a mai briefben L2/L3 (`main`, „Nappali elrendezéscsaládok”); elfogadott méretpróba **P902_24A**: U 3,00×2,40 m, TV felé nyitva, asztal 0,30 m-rel nyugatra (`GOAL.md` 10., `03_blender/geometry_A811_A812/meretproba/MERETPROBA_KANAPE_A902.md`) | L1 pilot-elrendezés (kanapé a nyugati falon); L2 kanapé háttal az üvegnek, déli TV (D19); L3 beljebb húzott ülőcsoport, nyugati TV (D16/D17). | MÉRETPRÓBA, nem kivitelezési terv | Astra csak L2/L3-at használta; a P902_24A U-befoglalót (3,00×2,40) nem ismerte (bázisa `cb8080a`). |
| A3 | **Rögzített valóság + K1–K10 nyitott korlátok** | brief 3–4. pont (`main`), Codex-audit `ai-coordination/audits/A902_geometriai_audit_folytatas_2026-10-24.md`, v2b lock | fehér fal/profil, EL2184 padló, 2,90–2,93 m, HF mezők, 10 cm-es válaszfal, DNy-i nyitott sarok, terasz szintek; K1 konyha 85–86 cm, K2 05.2 ágy, K3 terasz, K4 kamera, K5 teraszüveg, K6 falsík/rögzítés, K7 TV, K8 árak, K9 áram, K10 kanapé U/L. | IGAZOLT-M/F ill. NYITOTT | Astra 1:1 átvette (eredmény 3. fejezet). v2b-1 (PR #11) és a kiállás-réteg (`a085eec`) utána jött. |
| A4 | **B-fázisú promptsablon v1** | `05_promptok/A902_STYLE10_Cam02_prompt_sablon_v1.md` | FIXED blokk (Cam_02 (8,30; 4,40; 1,55) m, 20 mm, 1600×1000; padló/fal/profil tiltások) + STYLE blokk; státusz CONCEPT – NOT VALIDATED | SABLON, B fázis ZÁROLVA | Bemeneti kép 1 (régi semleges) elavult → a V2 briefben `04_renderek/semleges_v2b/` Cam_02 kell. |
| A5 | **Zenit / Lake Forest fordítótábla** | `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` | a két referencia DNS-e; „drága eredeti → olcsó, építés nélküli WSG-megoldás”; asztalos vs IKEA számítás; lakásonkénti verziók; keretszámítás | KONCEPCIÓ – NEM VALIDÁLT | Ez Claude egyetlen „stílus-szintű” anyaga, de két meglévő irány fordítása, nem új stílus. |
| A6 | **4 stílusos költség-előszűrés + árkönyvtár** | `ai-coordination/inputs/A902_v2b/KOLTSEG_ELOSZURES_4STILUS_A902.md`, `KOLTSEG_KERET_4STILUS_A902.csv`, `ARKONYVTAR_A902_2026-10-24.csv` (87 adatsor), `arforras/` | Zenit, Lake Forest, Rubin Szalon, Ezüst Orbit horgonytermékei (Kave Home EUR ×367 Ft + 5 % ÁFA-korrekció, Westwing, IKEA, OBI). Fő megállapítás: a vizsgált 4,90 M-os sorokból Rubin/Orbit látható tételei **2,56–3,01 M** („a pénz nem a képen van”), Zenit 3,98–4,89, LF 4,30–5,20 (Gala U 300×225: 3605 € → +0,3 M). | ELŐSZŰRT – FELTÉTELES | **Kave Home árak itt vannak igazolva** (webshop, HU végösszeg nem) – Astra kosarában Kave Home nincs. |
| A7 | **Pilot-audit átdolgozási irányai** (Rubin, Orbit) | `ai-coordination/audits/WSG-20261024-PILOT-001_CLAUDE_AUDIT.md` (1., 6., 8. pont) | hiányzó tér-gesztus, fényarchitektúra, panoráma-keretezés; Orbit meleg ellenpont, tükör rögzítés/visszatükröződés; „a stílusok térbeli gesztusban is különbözzenek” | AUDIT | Péter: az 1. és 6. pont csak javaslat. |
| A8 | **Kanapé-méretpróbák** | `03_blender/geometry_A811_A812/meretproba/MERETPROBA_KANAPE_A902.md`, `MERETPROBA_KANAPE_A811_A812.md`; `GOAL.md` 10. | A-902 U 3,00×2,40 (P902_24A); A-811 L 2,59×2,50 + 60 cm szekrénysor; A-812 U 3,00 m + 60 cm fülkeszekrény; félhold/ívelt + puff megfontolható | ELFOGADOTT MÉRETPRÓBA | valós termék, székhasználat, szabad sáv, kiállás végleges ellenőrzése hátravan |
| A9 | **STYLE4-003 brief** (4 stílus luxusszintre emelése) | `ai-coordination/requests/WSG-20261024-STYLE4-003.md` | Zenit, LF referenciaként; Rubin, Orbit felemelése; Astra High-ra írva | NEM INDÍTOTT, **elhalasztva** (Péter 17:06) | High már nem engedélyezett (19:34) → ha valaha indul, Medium-ra kell átírni; most nem feladat. |

**Őszinte számlálás:** Claude-tól **0 megnevezett új stílus**, 2 fordított referenciairány (Zenit, LF), 9 gesztuskategória, 3 elrendezéscsalád, 10 korlát, 1 sablon, 87 árjelölt. Az „A1–A10 Claude-kollekció” mint tíz stílus **nem létezik** – a korábbi beszélgetésekben ennek a keretrendszernek a neve volt. Ezt nem egészítjük ki utólag kitalált stílusokkal.

---

## B. ASTRA 10 STÍLUS – STYLE10-002 A fázis (B-gyűjtemény)

**Forrás (elsődleges):** `ai-coordination/results/WSG-20261024-STYLE10-002.md` – Astra eredeti, teljes fájlja (712 sor, SHA-256 `f94acf93b71440837808df2a1f54bab927609e24649c0d29076b34f7fed86189`, Péter csatolta 2026-10-24 20:20, bájtra változatlan). **Történeti bizonyíték:** `…_RELAY_RESZLEGES_20261024.md` (a megosztott szál pillanatképéből, 7. fejezet nélkül; az eredeti JSON SHA-256 `2f430740776cf1a1e86235d44a3072df548e034cc5415f80675fa54d85afed6e`, a Macen). Ellenőrzés: a két szöveg az 1–475. és a 517–712./516–711. sorokban betűre azonos; a 7. fejezet a pillanatképhez képest egy sorral (515.) bővült. **Astra státusza:** KONCEPCIÓ – NEM VALIDÁLT; költség ELŐSZŰRT – FELTÉTELES; ajánlat nincs. **Dokumentum: TELJES.** Bázisa `cb8080a` (v2b, **nem** v2b-1; P902_24A-t nem ismerte). Modell és gondolkodási szint: **nem igazolt** (Astra saját fejléce).

### B1. A tíz stíluskártya kivonata (Astra szövegéből, nem átírva – részletek a forrásfájl 6. fejezetében)

| ID | Név · egy mondat (Astra) | Saját tömeg-/térnyelv (Astra 8. fej.) | Főbútor + étkező (P-jelölt) | 2 kiemelt WOW (sáv, M Ft) | Elrendezés | Gesztus-kód (Claude A1 szerint, utólagos besorolás) |
|---|---|---|---|---|---|---|
| S01 | **Kyoto Ink** · kortárs kiotói magánrezidencia fegyelmezett, érzéki nyugalma | lapos horizont + függőleges áttetsző mező; alacsony súlypont | P14 Lennon L 238×180 (0,80) + P09 Toni ovál 200×90 (0,32); U-próba P05 | „tintavonal” média-bútor 240×40×48 (0,45–0,65); áttetsző textilmező 100×180 (0,10–0,15) | L3, D16/D17 | **A** (textilmező), másodlagos C |
| S02 | **BiBo Nocturne** · intim, művészi penthouse-szalon, mélykék ülőtömeg + szabálytalan tükröződés | záródó U, organikus tükörkontúr, tömb–tükröződés | P04 IKEA JÄTTEBO U 285×160 (0,928) + P08 Anouk üveg 180×90 (0,32); L-tartalék P14 | szobrászati tároló 240×40×50 + tükör 80×190 (0,65–0,90); opál fénytömeg ML04 (0,12–0,20) | L3 | **B** (tükröző objekt), másodlagos F |
| S03 | **Alelí Casa** · művelt, vendégszerető olasz rezidencia erős étkezővel | ovális étkezői központ, lekerekített tárolóvég, kerámia | P02 Melva olíva L 238×143 (0,85) + P09 Toni 200×90 | ívelt végű tároló 210×40×50 (0,45–0,65); valódi kerámia relief 100×100 (0,12–0,20) | L2, D19 | **F** (ovális étkező mint szobrászati bútor), másodlagos H |
| S04 | **LA Horizon** · filmszerű, levegős penthouse, hosszú vízszintes vonalak | alacsony nyitott lounge, egymás mögötti vékony horizontok | P14 Lennon L + P07 Anouk barna üveg 180×90 (0,32); U-próba P05 | kétrétegű horizont-bútor 240 cm (0,55–0,80); master horizont 280×85 (0,25–0,35) | L2, D19 | **E** (panoráma-keretezés), másodlagos C |
| S05 | **Miami Streamline** · könnyed, sikkes, kissé filmsztáros rezidencia | lépcsőzött/lekerekített profil, függőleges bordaritmus | P03 Melva rózsa kord L 238×143 (0,75–1,00) + P08 Anouk | streamline tároló 220×40×55 (0,50–0,70); két bordázott ritmuselem (0,08–0,10) | L3 | **G** (anyagritmus), másodlagos F |
| S06 | **Zenit Atelier** · sötét tónusú, nyugodtan magabiztos penthouse | alacsony mély főtömeg és magas oldaltömeg feszültsége | P14 Lennon L + P07 barna üveg; U-próba P05 (+0,128 csak tételcserével) | aszimmetrikus média-kompozíció 240×40×45 + 45×35×190 (0,60–0,90); triptichon-fejvég 270×110 (0,28–0,40) | L3 | **C** (beépített hatású tömeg), másodlagos D |
| S07 | **Lake Forest Couture** · világos couture-szalon, puha szobrászati formák | puha nagy kanapétömeg, domború és sima felületek | **P15 Wolke L 258×167×65 (1,05 – gyenge bizonyíték)** + P09 Toni; tartalék P01 Melva | világos tároló + valódi relief 100×130 (0,60–0,85); fémes asztaltömeg Ø75–90 (0,12–0,22) | L3 | **F** (szobrászati kanapé), másodlagos G |
| S08 | **Milano Radical** · magabiztos designgyűjtő lakása, minden nagy forma másképp viselkedik | eltérő magasságú geometrikus testek és áttetsző sík | P04 U + P08 üveg; L-tartalék P14 | „három test” tároló 220×40×70 (0,50–0,75); geometrikus szőnyeg 240×340 (0,18–0,25) | L3 | **B** (geometrikus objekt), másodlagos A |
| S09 | **Paris Collector** · személyes, művelt, rétegzett luxus katalógusszett-hatás nélkül | eltérő tárgysziluettek, szalonarány, egy nagy mű | P02 Melva olíva L + P07 barna üveg + fotel (0,15–0,22, SKU nyitott) | nagy műtárgymező 140×180 (0,12–0,20 + textilháttér 0,08–0,15); sötét tárolókompozíció 220×40×60 (0,55–0,80) | L3, állólámpa D18 | **H** (műtárgy-kuráció) |
| S10 | **Desert Modern 70** · sivatagi modernizmus és hetvenes évek egy európai penthouse-ban | lépcsőző bútorprofil, nagy geometrikus relief, széles horizont | P14 Lennon L + P09 Toni | lépcsőzött tároló 220×35/45×35/60 (0,50–0,75); nagy grafikus relief 120×120 (0,12–0,20) | L2, D19 | **C** (lépcsőző tömeg), másodlagos G |

Minden stílushoz tartozik Astránál: 5 ismertetőjel + kerülendő giccs, 5 HEX-szín valós anyaggal, 8 helyiséges „karakter / nyugalom” tábla, 4 WOW-sor költségsorral és beszerzési úttal, FELTÉTELES-jelölés (K6/K8/K10/K5), „30–50 %-kal olcsóbb WOW-csomag” mondat.

### B2. Termékjelöltek (Astra 4. fejezete, lekérés 2026-10-24; webár, nem ajánlat)

| ID | Termék | Méret (cm) | Bruttó ár (Ft) | Bizonyíték ereje | Használja |
|---|---|---|---|---|---|
| P01 | Westwing Melva világosbézs L | 238×143×75 | 650 000 | termékoldal, 9–10 hét | S07 tartalék |
| P02 | Melva olíva L | 238×143×75 | 650 000 oldal / 850 000 kivonat → keret 850 000 | ellentmondó | S03, S09 (S01/S10 alternatíva) |
| P03 | Melva törtrózsaszín kord L | 238×143×75 | 750 000 / 850 000 / 1 000 000 → keret 1 000 000 | ellentmondó | S05 |
| P04 | IKEA JÄTTEBO 3,5 + 2 heverő, Samsala sötétkék (496.076.48) | **285×160×71 U** | 928 000 | termékoldal | S02, S08 |
| P05 | JÄTTEBO Samsala szürke-bézs (294.713.87) | 285×160×71 U | 928 000 | termékoldal | U-próba S01/S03/S04/S05/S06/S10 |
| P06 | JÄTTEBO 2,5 + bal heverő, sötétkék | 190×160×71 L | 551 500 | kategóriaár | kompakt tartalék |
| P07 | Westwing Anouk áttetsző barna üveg asztal | 180×90×75, 84 kg | 320 000 | termékoldal | S04, S06, S09 |
| P08 | Anouk áttetsző üveg | 180×90×75 | 320 000 | termékoldal, 13–14 hét | S02, S05, S08 |
| P09 | Westwing Toni ovál, tölgyfurnér, 200-as | 200×90×75 | 320 000 | termékoldal | S01, S03, S07, S10 |
| P09s | Toni 160-as konfiguráció | 160×90×75 | 199 990 (korábbi 259 990) | kivonat | tartalék |
| P10 | IKEA NORDLI tárolós ágykeret, fehér (203.498.53) | 180×202×30 | 189 900 | termékoldal | master, mind a tíz |
| P11 | Westwing Sato tárolós ágy, 140 | 146×206×37 | 370 000 | termékoldal | **elutasítva (K2)** |
| P12 | Westwing Dream kárpitozott ágy, 140 | 156×222 | 350 000 | termékoldal | 05.2-be túl hosszú |
| P13 | Westwing Sofia szürke L | 312×235×72 | 1 000 000 / 1 250 000 | – | kiesik (méret) |
| P14 | **Westwing Lennon L, szövött szürkésbarna, jobb sarok** (DEQ21WES12329-168260) | **238×180×68** | **800 000** | termékoldal, 9–10 hét | S01, S04, S06, S10 (+ L-tartalék S02/S08) |
| P15 | Wolke világosbézs texturált L (25WES29958) | 258×167×65 | 1 050 000, 12–13 hét | **gyenge: keresési kivonat, oldal nem nyílt** | S07 |
| P15b | Wolke Teddy Bouclé törtfehér (24WES78013) | méret nem olvasható | 900 000, 7–8 hét | HU oldal, más SKU | S07 nem kész helyettesítés |

**Hiány Péter 19:38-as szabályához képest:** Kave Home egyetlen jelöltben sem szerepel; Astra: *„Kave Home HU ár ebben az eredményben továbbra sem igazolt.”* A Claude-árkönyvtár (A6) viszont 87 Kave Home/Westwing/IKEA jelöltet tartalmaz EUR-árral – a V2 brief kötelező bemenete.

### B3. Költségmodell, rangsor, döntősök (Astra 5. és 8. fejezete)

- Közös módosítások mind a tízhez (M Ft): 03a 1,10→0,80 · 03c 0,45→0,40 · 03e 0,20→0,25 · 03f 0,25→0,35 · 04b 0,55→0,35 · 11 0,50→0,20 · 12 0,50→0,40 · 14 0,45→0,65 · **új 15_AV 0→0,50** → **18,00 → 17,90** (1,00 M kanapéval); 2,00 M tartalék érintetlen.
- **7. fejezet – stílusonkénti végső célkeretek (M Ft, teljes lakás / szabad hely a 18 M-on belül / felső sávos stressz tartalék nélkül):** S01 Kyoto 17,650 / 0,350 / 26,250 · S02 BiBo 17,928 / 0,072 / 26,378 · S03 Alelí 17,750 / 0,250 / 26,300 · S04 LA 17,828 / 0,172 / 26,378 · S05 Miami 17,850 / 0,150 / 26,450 · S06 Zenit 17,900 / 0,100 / 26,250 · S07 LF 17,950 / 0,050 / 26,500 · S08 Milano 17,778 / 0,222 / 26,378 · S09 Paris 17,850 / 0,150 / 26,300 · S10 Desert 17,650 / 0,350 / 26,300. Astra: a webárral azonosított kanapé + asztal + ágykeret stílusonként 1,3–1,6 M-ot (a keret 7–9 %-át) támaszt alá; *„Egyik stílus teljes 18 M-os kivitelezhetősége sincs még igazolva.”* Pénzügyi PASS csak tételes bontással, ≤18 M beszerzés + fuvar + szerelés, 2 M érintetlen.
- Szubjektív profil 1–10 (karakter, WOW, térélmény, funkció, keretkockázat, kivitelezési nehézség, időtállóság, eladási vonzerő) mind a tízre – forrásfájl 8. fejezet.
- **Rangsorok:** WOW: S02, S07, S06, S08, S05, S01, S04, S09, S03, S10 · Karakteres különállás: S02, S08, S05, S01, S09, S07, S06, S03, S10, S04 · Kivitelezhetőség (kedvezőbbtől): S01, S03, S10, S04, S06, S09, S05, S08, S02, S07 · Pénzügyi kockázat (alacsonyabbtól): S01, S10, S03, S04, S09, S08, S05, S06, S02, S07.
- **Három ajánlott döntős:** S02 BiBo Nocturne, S07 Lake Forest Couture, S06 Zenit Atelier; **tartalék:** S01 Kyoto Ink. *„Ez ajánlott döntős mezőny, nem Péter helyett meghozott végső stílusválasztás.”*
- Legközelebbi párok Astra szerint: **LA–Desert**, **Kyoto–Zenit** → B-próba első feladata a sziluett szerinti elkülönülés.
- 16 műszaki/beszerzési kérdés Claude-nak (9. fejezet), 10 angol B-prompt-tervezet NEM FUTTATHATÓ (10.), másolható Medium/High/audit promptok (11.).

### B4. A két pilot (nem a tízben, dokumentált előzmény)

| Pilot | Forrás | Lényeg | Teljes lakás (pilot) | Claude-audit / előszűrés |
|---|---|---|---|---|
| **Rubin Szalon** | `results/WSG-20261024-PILOT-001.md` | egy rubin akcent, textiltriptichon 3×60×120 cm, L kanapé (Blok), art déco címke | 17,80 M (tartalék előtt) | tér-gesztus hiányzik, a panel a falnak ~19 %-a; látható tételek 2,56–2,66 M a 4,90-ból |
| **Ezüst Orbit** | ugyanott | Ø140 tükör (biztonsági hátoldal) a 10 cm-es válaszfalon, hűvös szürke–jégkék–ezüst, L kanapé | 18,00 M | meleg ellenpont hiányzik; kórház/showroom-hideg kockázat; látható tételek 2,64–3,01 M |

Péter (Work [18], 19:34): Rubin/Orbit **nem kötelező résztvevő**; megőrizhetők pilotként, a tízbe csak akkor, ha igazoltan erősebbek egy új jelöltnél. Astra: *„korábbi pilot marad; nem töröljük és nem számítjuk a tízhez.”*

---

## P. PÉTER IRÁNYAI ÉS KORREKCIÓI – szó szerint (P-gyűjtemény)

Ezek a mezőny valódi forrásai; a V2 briefbe változtatás nélkül kerülnek.

**P1 – Work-indítás (megosztott szál [0], 2026-10-24):** *„Én két mélységi szintet alkalmaznék: – Most, Astra Medium: tíz erősen különböző stílus, mindegyikhez ténylegesen beazonosított fő bútorok, WOW-elemek, piaci árak és teljes lakásos előzetes költségvetés. – Később, Astra High + Claude: a három döntős minden bútorának és anyagának pontos darabjegyzéke, végső árak, szállítás, kivitelezés és független költségellenőrzés.”* … *„Nagyon fontos hogy már az új javított geometriával dolgozz, legyenek pontosak a tervek”* … *„adj tervet hogy lehetne ez … egyszerre … drága és menő a terv de férjen bele a budgetbe.”*

**P2 – Mezőny ([4]):** *„Fontos hogy a 10 stílis a most menő legmenőbb stílusok legyenek. Amúgy legyen 1 japán benne, egy BIbo Budapestre hajazó, egy Aleli Budapestre hajazó, egy Los Angeles skyline stílus, 1 Miami Art Deco stíllus, a többit rádbízom, a githubra feltöltött elvek alapján dolgozz.”*

**P3 – FONTOS KREATÍV KORREKCIÓ ([18]):** a 10 stílus összetétele: 1. Japán ihletésű kortárs luxus · 2. BiBo Budapest ihletésű szobrászati luxus · 3. Alelí Budapest ihletésű mediterrán-olasz luxus · 4. Los Angeles Skyline luxus · 5. Miami Art Deco · 6. Zenit – az eredeti erős koncepció kreatív továbbfejlesztése · 7. Lake Forest – az eredeti erős koncepció kreatív továbbfejlesztése · 8–10. három szabadon választott, naprakész, igazán különleges nemzetközi luxusirány. *„A Rubin Szalon és az Ezüst Orbit NEM kötelező résztvevő többé.”* *„A Zenit és Lake Forest látványminősége a kreatív minimum, nem felső korlát. Ne egyszerű, dekorációval feldobott szobákat tervezz. Különleges bútortömegeket, rétegzett anyagokat, elegáns fényeket, erős térkompozíciókat és valóban drágának ható, szexi, nemzetközi színvonalú enteriőröket akarok.”* *„Mindegyik a teljes A-902-re szóljon. A v2b alaprajzi geometria a kiindulás, az ellenőrizetlen részletek maradjanak feltételesek. A 18 M Ft bruttó tervezési keret és 2 M Ft érintetlen tartalék kötelező.”* *„Ahol a tényleges luxusbútor túl drága, keress azonos karakterű, valóban megépíthető, ellenőrizhető árú megoldást. A kreatív WOW-t ne áldozd fel automatikusan a költségcsökkentésért.”* *„A feladatot NE kezdd újra.”*

**P4 – KRITIKUS KREATÍV MINŐSÉGI IRÁNYELV ([22]):** *„Tíz olyan, egymástól radikálisan különböző, nemzetközi színvonalú luxusenterőrt szeretnék, amelyek első látásra lenyűgöznek, érzelmi reakciót váltanak ki, egy csúcskategóriás designhotel, penthouse vagy építészetileg kiemelkedő magánrezidencia karakterét sugározzák. A cél: a valós berendezési költség többszörösét sugalló esztétikai és ingatlanpiaci érték, hamis anyagok és megvalósíthatatlan látványelemek nélkül.”* Kötelező mind a tíznél (1–10): saját, azonnal felismerhető identitás · emlékezetes, nagyvonalú nappali-kompozíció · kanapé minimum L, lehetőleg valódi U ellenőrizhető befoglalóval · sziluett + anyag + arány + fény + rétegzettség + negatív tér együtt · 2–3 domináns, valós terméken/gyártható megoldáson alapuló WOW-elem · ugyanaz a karakter a teljes lakásban (nappali, étkező, konyha, hálók, előtér, fürdők, tetőterasz) · nemzetközi élvonal, nem trendparódia · valós termékek pontos modellel, mérettel, színnel, anyaggal, linkkel, aktuális árral, HU beszerezhetőséggel; nem igazolt ár nem tény · a TELJES A-902 a 18 M-ba, 2 M tartalék érintetlen, költségkockázat nem rejthető · megvalósíthatóság ≠ ambíció feladása (IKEA-váz + egyedi front, valódi formabútor, fókuszált asztalosmunka, rétegzett világítás a meglévő kiállásokhoz). Belső minőségellenőrzés 8 kérdése (magazin? drágának hat? saját térkarakter? izgalmasabb a pilotoknál? versenyképes Zenit/LF-fel? meleg fény nélkül is működik? megvásárolható/legyártható? alaprajz–parketta–fehér nyílászáró–terasz–villamos adottság megmarad?) – *„Ha nem, a koncepciót fejleszd tovább, ne add át kész stílusként.”*

**P5 – Claude-munkamenet, 2026-10-24 (19:17–19:42):** a 7 kötelező + 3 javasolt irány megerősítése; BiBo/Alelí = karakter- és anyaginspiráció, nem másolat; nem tíz átszínezett egyforma nappali; **Astra legfeljebb MEDIUM** (minden High-engedély visszavonva; csak ha a szint beállítható és igazolható, különben nem indul – 19:34); **Kave Home is forrás az IKEA és Westwing mellett** (19:38); **KREATÍV MINŐSÉGI KÜSZÖB** (19:42): a Zenit/LF legjobb látványai a MINIMUM; nem fogadható el olcsóbbnak kinéző változat; először a kivételes forma/tér/anyag/fény, utána a költséghatékony valós megoldás; összevetés azonos szigorral és azonos kamerával; nem indítunk második STYLE10-002-t, új Work-feladatot vagy extra kreditet; a feltételes PREMIUM +≈1 M forgatókönyv külön, soha csendben.

---

## C. Összehasonlító mátrix (Claude független, csak szövegen alapuló koncepcióértékelés, 1–5)

**Olvasat:** 1 = gyenge … 5 = kiemelkedő; **Költségkockázat: 1 = alacsony … 5 = magas.** Kép nem készült egyik irányhoz sem, ezért ez **koncepció-szintű, szubjektív** értékelés, nem render-ítélet és nem Péter döntése. Astra saját 1–10-es profilja a forrásfájl 8. fejezetében; ahol eltérünk, jelölve.

| Irány | Vizuális karakter / eredetiség | Luxushatás (meleg fény nélkül) | Térkompozíció | Bútorkoncepció (valós termék) | Egész-lakás kiterjeszthetőség | Megvalósíthatóság | Költségkockázat | Fejlesztésre érdemes | Megjegyzés |
|---|---|---|---|---|---|---|---|---|---|
| S01 Kyoto Ink | 4 | 4 | 4 | 4 | 4 | 4 | 2 | **igen – tartalék döntős** | legkisebb kockázat; veszély: túl szikár, „Japandi” |
| S02 BiBo Nocturne | 5 | 5 | 4 | 3 | 4 | 3 | 4 | **igen – döntős** | hős-kanapé IKEA JÄTTEBO: a luxusérzetet a tároló+tükör és a textil viszi; U beférése (K10) és tükör (K6) nyitott |
| S03 Alelí Casa | 3 | 3 | 4 | 4 | 4 | 4 | 2 | feltételes | étkezőközpont jól különböztet; kockázat: átlagos mediterrán |
| S04 LA Horizon | 3 | 4 | 4 | 4 | 4 | 4 | 3 | feltételes | összecsúszhat S10-zel és részben S06-tal; K5 teraszüveg |
| S05 Miami Streamline | 4 | 3 | 3 | 4 | 3 | 3 | 3 | feltételes | erős karakter, trend-elavulás (Astra időtállóság 7); bordázat K6 |
| S06 Zenit Atelier | 4 | 4 | 4 | 4 | 4 | 4 | 3 | **igen – döntős** | a legbiztosabb „sötét” irány; aszimmetrikus tömeg 0,60–0,90 |
| S07 Lake Forest Couture | 4 | 5 | 4 | 3 | 4 | 3 | 5 | **igen – döntős, feltételes SKU** | P15 Wolke bizonyíték gyenge, 1,05 M a plafonon; relief gyárthatóság |
| S08 Milano Radical | 5 | 4 | 3 | 4 | 3 | 3 | 3 | feltételes | legeredetibb a nem kötelezők közül; zsúfoltság és showroom-kockázat |
| S09 Paris Collector | 3 | 3 | 3 | 3 | 3 | 4 | 3 | feltételes / most nem | kép- és fotelválasztás nélkül „jó bútorok egy fal előtt” (Astra is jelzi) |
| S10 Desert Modern 70 | 3 | 3 | 4 | 4 | 4 | 4 | 2 | feltételes | S04-gyel összevonható egy „horizont” irányba; alacsony kockázat |
| Rubin Szalon (pilot) | 3 | 2 | 2 | 3 | 3 | 4 | 2 | nem (marad pilot) | Péter: „ingerszegény”; a pénz nem a képen van |
| Ezüst Orbit (pilot) | 3 | 2 | 2 | 3 | 2 | 3 | 2 | nem (marad pilot) | tükör a 10 cm-es falon; hűvös összhatás |
| Claude A-gyűjtemény (A1–A9) | – | – | – | – | – | – | – | **nem pontozható** | nem stílus, hanem ellenőrző keret és bemenet; a C2 pontban használjuk |

**Eltérések Astra önértékelésétől:** Astra S02-nél a bútorkoncepciót nem gyengíti (U = WOW); Claude szerint az IKEA-kanapé mint hős-darab a 19:42-es minőségi küszöbbel (nem olcsóbbnak kinéző) külön vizsgálandó – a kárpit és a tároló+tükör együttes minősége dönt. S07-nél Astra is kimondja a gyenge P15-bizonyítékot; Claude ezért a bútorkoncepciót 3-ra teszi, amíg nincs SKU–méret–ár–sarokirány együtt.

### C2. Astra tízesének ellenőrzése Claude gesztus-mátrixával (A1)

Elsődleges gesztus: S01 **A**, S02 **B**, S03 **F**, S04 **E**, S05 **G**, S06 **C**, S07 **F**, S08 **B**, S09 **H**, S10 **C** → 7 különböző kategória, egyik sem több 2-nél → **a sokszínűségi szabály a határon teljesül.** Kihasználatlan: **D fényarchitektúra** és **I természet/terasz-folytonosság** (A-902 egyedi értéke a többszintű tetőkert és a budai panoráma). Akcentszín: két kék (S02, S08) rendben; három olívás (S01 taupe/olíva, S03, S09) a határon → S09 színvilága újragondolandó, ha marad.

### C3. Legerősebb inspirációk (mindkét gyűjteményből, a V2 briefbe)

1. **Tér-gesztus mint luxus** (Claude A1/A7 + Péter P4): a kompozíció tömege, nem a dekor – Astra ezt S02, S06, S07, S08-ban váltja be.
2. **Egyetlen egyedi forma-darab lakásonként 1–3** (CLAUDE.md, Claude A5, Astra 1. fej.): IKEA-korpusz + egyedi front/él; a látható illesztés minősége számít.
3. **„A pénz legyen a képen”** (Claude A6, pilot-tanulság): a látható hős-tételekre menjen a 03a/03b/03e/03f/10 keret.
4. **Valódi U vizsgálata az étkezővel együtt** (Péter P4/3, Claude P902_24A, Astra K10): a 285×160 U vs. a 3,00×2,40 elfogadott befoglaló – össze kell vetni.
5. **Azonos kamera, azonos semleges fény** (Claude A4, Astra 8. fej., Péter 19:42): a meleg fény nem bizonyíték.
6. **Kave Home + Westwing + IKEA hármas** (Péter 19:38, Claude A6 árkönyvtár): Astra kosarát Kave Home-jelöltekkel kell kiegészíteni (Martina L 287 cm 3235 €, Gala U 300×225 3605 €, Neom modulok, Nealy Ø150, Naanim Ø120 – A6 szerint).

---

## D. Közös tízes – javaslat Péter döntéséhez (nem döntés)

| Hely | Irány | Forrás | Státusz | Döntési pont |
|---|---|---|---|---|
| 1 | Kyoto Ink (japán kortárs) | Péter P2/P3 → Astra S01 | kidolgozott | – |
| 2 | BiBo Nocturne | Péter P2/P3 → Astra S02 | kidolgozott | U beférés P902_24A-val; IKEA-kanapé minőségi küszöb |
| 3 | Alelí Casa | Péter P2/P3 → Astra S03 | kidolgozott | „ne legyen átlagos mediterrán” – erősíteni |
| 4 | LA Horizon | Péter P2/P3 → Astra S04 | kidolgozott | összecsúszás S10-zel |
| 5 | Miami Streamline | Péter P2/P3 → Astra S05 | kidolgozott | időtállóság |
| 6 | Zenit Atelier | Péter P3 → Astra S06 (Claude A5 fordítótábla) | kidolgozott | – |
| 7 | Lake Forest Couture | Péter P3 → Astra S07 (Claude A5) | kidolgozott, **P15 nem igazolt** | SKU–ár–méret együtt |
| 8 | Milano Radical | Astra javaslat | kidolgozott | maradjon (legeredetibb javasolt) |
| 9 | Paris Collector | Astra javaslat | kidolgozott, kreatív kockázat | **csere jelölt** – alternatíva: I-gesztusú „terasz-folytonosság / biofil penthouse” vagy D-gesztusú „fényarchitektúra” irány (**cím-szintű ötlet, nem koncepció, nem pontozott**) |
| 10 | Desert Modern 70 | Astra javaslat | kidolgozott | **összevonás jelölt** S04-gyel, ha a B-próba nem különíti el |
| – | Rubin Szalon, Ezüst Orbit | pilot | dokumentált, nem a tízben | Péter 19:34 szerint nem kötelező |

A V2 brief ezt a listát kapja „7 kötelező + 3 javasolt” formában; a 9–10. hely cseréjéről/összevonásáról Péter dönt, Astra csak javaslatot tesz.

---

## E. Hiányok és blokkolók (2026-10-24 este)

| # | Hiány / blokkoló | Hatás | Kezelés |
|---|---|---|---|
| 1 | ~~Astra eredményének 7. fejezete nincs meg~~ → **MEGOLDVA 2026-10-24 20:20:** Péter előkerítette a teljes eredeti fájlt; a repóban bájtra változatlanul | a 17,650–17,950 M célkeretek stílusonként ellenőrizhetők | a STYLE10-002 A fázis tartalmilag **lezárt**; újabb Astra-futtatás a lezáráshoz nem kell; Claude-audit következik |
| 2 | Az eredeti Work-szál innen nem volt elérhető (Chrome: csak a megosztott pillanatkép; Codex-lista üres); a Medium-szint nem igazolható → **nem folytattuk**, és a teljes fájl előkerülésével a lezáráshoz már **nem is szükséges** | – | V2 brief NEM INDÍTOTT; bármely későbbi Astra-futás csak Medium igazolásával, Péter külön engedélyével |
| 3 | Modell/gondolkodási szint az A fázisban **nem igazolt** | a kreditszabály visszamenőleg nem ellenőrizhető | dokumentálva; nem állítjuk, hogy Medium volt |
| 4 | **Kave Home** hiányzik Astra kosarából (Péter 19:38) | hős-darabok forrása hiányos | A6 árkönyvtár kötelező bemenet a V2-ben |
| 5 | **P15 Wolke** bizonyíték gyenge; P02/P03 ár ellentmondó | S07 költségplafon, S03/S05/S09 ár | V2: SKU–méret–ár–sarokirány együtt, dátummal |
| 6 | Astra bázisa `cb8080a` → **v2b-1 (PR #11), kiállás-réteg, P902_24A** nem volt ismert | geometriai/U-befoglaló eltérés lehet | V2: friss `main`, lock v2b-1, P902_24A kötelező |
| 7 | Helyszíni fotók (≈60, 2026-10-25/26) és Szakos Andrea bútorozott alaprajzai még nincsenek | K5/K6/K3 és elrendezés feltételes marad | V2 A-fázis szöveges; B fázis zárolva |
| 8 | Az eredeti JSON csak a Macen (`~/Downloads/WSG/…json`), repóban nincs | a teljes fájl előkerülésével a JSON már csak másodlagos bizonyíték | Péter dönt a feltöltésről (érzékenységi vizsgálat: nincs titok); nem sürgős |
| 9 | Független Claude-audit az Astra-eredményre **még nem készült** | költség/geometria állítások ellenőrizetlenek | külön `audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md`, következő lépés |

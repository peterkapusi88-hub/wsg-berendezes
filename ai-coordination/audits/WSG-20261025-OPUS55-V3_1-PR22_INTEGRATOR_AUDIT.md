# A-902 · Opus 5.5 V3.1 (PR #22) – független integrátori audit (Claude integrátor, 2026-10-25, r2 – végleges forrás)

**Ág:** `integrator/opus55-v3-1-audit-20261025` (a `competition/baseline-20261025-v3` @ `45632b5`-ből). A PR #22 ága, a `main`, a versenyzői fájlok és az élő Blender-fájl érintetlen. Rendelés, ajánlatkérés, merge, külső kommunikáció nem történt. **Végleges renderengedély nincs.**

## 0. Forrásverziók
| | Érték |
|---|---|
| **Auditált végleges forrás** | `competition/opus55-v3-1-20261025` @ **`7d3c67f823c646d9daef06b294826e89c1c61467`** (CP14 + naplózárás, 2026-10-25 06:51) – a távoli GitHub-állapottal egyezik (Péter ellenőrzése) |
| Hogyan került a gépre | A terminálos `git fetch` ebből a munkamenetből nem tud hitelesíteni („could not read Username for https://github.com”). A `7d3c67f` a helyi repóban a `origin/competition/opus55-v3-1-20261025` ref frissülése után jelent meg (nem ennek a munkamenetnek a fetch-e). |
| Korábbi (r1) audit alapja | `b24bee7` (CP10) – a hibajegyzék leletei a végleges forráson újraellenőrizve; ahol eltér, jelölve |
| b24bee7 → 7d3c67f | +`40_ELEMLISTA_V3_1.csv` (511 tétel), +`50_KOLTSEG_ES_KOCKAZAT.md`, +integrációs összefoglaló; 10 spec frissítve; 32 prompt módosult. **S01 Cam_02/Cam_12 azonos, S02 Cam_02/Cam_12 eltér** (ML04: Kave Home Idela, ML05: Westwing Dancing). Termékcserék: S04 Wolke → **Westwing Lilo 260 × 176**; S05 → **Westwing Melva 238 × 143**; S07 → **Westwing Wolke Teddy 256 × 118**. |

Forrásdokumentumok (baseline v3): `GOAL.md` (main `114988f`), `ai-coordination/RENDER_REALITY_GATE.md`, `.agents/skills/wsg-stiluslabor/SKILL.md`, `ai-coordination/inputs/A902_verseny/GEOMETRIA_C_KAMERACSOMAG_v2.md`, `KOZOS_FIX_ALAP_v1`, `HUE_ALAPCSOMAG_v1`, `A902_villamos.csv`, `REFERENCIA_KARTYA_A902_Cam02_v2b.md`, `KEP004_ChatGPT_Images_v1/README.md`.

## 1. Kapuverdikt
| Kapu | Eredmény |
|---|---|
| 1. AUDIT – 7d3c67f | **FELTÉTELES – nem indítható** a K-01…K-06 nyitott pontjai miatt. Az 511 tételes lista: **szerkezeti és számtani audit kész; a termék- és árhitelesség webes visszaellenőrzése NEM készült** (lásd 3.2). |
| 2. BLENDER – S01/S02 Cam_02 + Cam_12 (v1.2 promptokkal) | **FELTÉTELES PASS** (`03_blender/integrator_opus55/BLENDER_JELENTES_OPUS55_S01_S02.md`, 5. pont) |
| 2. BLENDER – S04, S05, S07, S08, S09, S10 | **lefutott, 3 stílus nem felel meg** a kötelező méreteknek a specifikáció szerint (S04 olajfa, S05 05.3-út 0,89, S08 torony/MR-2); a gyártói belső méretek (ülésmélység, sarokelem) feltételezések |
| K-02 / K-03 javítás | **kész a négy induló promptra** – integrátori v1.2 a végleges forráson (`05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_2_7d3c67f/`); a b24bee7-alapú v1.1 csak tervezet |

## 2. Hibajegyzék (végleges forrás)
Súlyosság: KRITIKUS / MAGAS / KÖZEPES / ALACSONY. **KB** = képgenerálást blokkol. Státusz: NYITOTT / JAVÍTVA (v1.2) / RÉSZBEN.

| ID | Súly | KB | Státusz | Lelet | Bizonyíték | Javítás |
|---|---|---|---|---|---|---|
| K-01 | MAGAS | KB (mind) | RÉSZBEN | Forrásverzió. A 7d3c67f most auditálva; a négy induló prompt v1.2-je erre készült. **Nyitott:** az 511 tétel termék- és árvisszaellenőrzése; push a távoli GitHubra (lásd 6.). | 0. pont | 3.2 pont; Péter push-a |
| K-02 | MAGAS | **KB (mind a 10 Cam_02)** | JAVÍTVA az S01/S02 Cam_02-ben (v1.2); **NYITOTT S03–S10** | Mind a tíz Cam_02 prompt a jobb képszélen akarja megjeleníteni az ML04 étkezőlámpát, de az a képkereten **kívül** van. | Szög 56,6° vs. fél látószög 42°; Blender-vetítés minden stílusra: ML04 x 1,04–2,33 (a 0–1-en kívül) | Csere: „The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; at most a faint warm spill of its light reaches the right edge of the floor and the table.” + tiltósor |
| K-03 | MAGAS | KB (S01, S02, S04 Cam_12) | JAVÍTVA az S01/S02 Cam_12-ben (v1.2); **NYITOTT S04** és a stílusdokumentáció (Péter kérésére érintetlen) | A W02 melletti növény/olajfa a hálók felé vezető fő utat elzárja és a W02-műalkotás elé áll. | 2D: S01 1,00 → 0,70; S02 0,90 → elzárva; S04 0,94 → elzárva; 3D: Cam_12-ben átfedés a művel | Törlés a renderpromptból + tiltósor. A `10_STILUS_SPEC` (S01 §2 textil, S02 §2 textil, S04 §2 textil) **érintetlen** – Opus/Péter frissítse. |
| K-04 | MAGAS | – | NYITOTT (hétfő) | Teraszajtó: ha csak a keleti, 0,93 m-es szárny nyílik, a 2+2+1+1 egyik stílusban sem tartja a terasz felé vezető utat. Opus 5+1-gyel helyesen kezeli. | 2D, terasz: S01 0,75 · S02 0,70 · S04 0,75 · S05 0,70 · S06 0,75 · S07 0,75 · S08 0,75 (45 cm-es toronnyal 0,77) · S09 0,65 · S10 0,75; 5+1-gyel 0,95–1,00 | Hétfői mérés (2026-10-26); a kép felirata „teraszajtó feltételes” |
| K-05 | MAGAS | KB: S02 (Cam_02/03/12), S05, S08 nappali-nézetek | NYITOTT | Hue-foglalat: **S05 ML04 Kave Home Novae** – a repó jegyzete szerint beépített LED (10 W, 3000 K) → Hue nem megy. **S02 és S08 ML04 Kave Home Idela** – foglalat nem igazolt; az Idela asztali lámpa G9-es (kiszűrve). Opus maga is FELTÉTELES-nek jelöli (S02-L04, S05-L04, S08-L04). Az S05 ML05 Brisia ára FELTÉTELES. | `KEP004_ChatGPT_Images_v1/README.md`; 50_KOLTSEG §4, §6 | Foglalatigazolás dátummal, vagy Opus saját alternatívája (Westwing Misaki / Dancing / Styrka, E27, igazolt) |
| K-06 | KÖZEPES | KB (S02 nappali-nézetek) | NYITOTT | Fekete Westwing Toni ovális 160 × 90 (S02-N02): az elemlista „ellenőrzött”-nek jelöli, ugyanazzal a linkkel és árral (259 990 Ft), mint a világos tölgyet. Az integrátor a fekete változatot nem tudta visszaellenőrizni (a Westwing ebből a munkamenetből nem kérdezhető le). | 40-es lista S01-N02, S02-N02 | Termékoldal-képernyőkép vagy cikkszám a fekete változatra |
| K-07 | KÖZEPES | – | NYITOTT | Spec ↔ prompt: az S01 spec 36. sora „ML05 – Ø 80 cm-es papírlámpás”, a lámpatestlista és a prompt Westwing Misaki Ø 40 × 70 (DEQ21WES21200, 107 970 Ft, ellenőrzött). A prompt az érvényes; a spec ellentmond magának. | `10_STILUS_SPEC/S01_KyotoInk.md` 36. és 120. sor | Opus javítsa a spec 36. sorát |
| K-08 | KÖZEPES | – | NYITOTT | Dohányzóasztal a JÄTTEBO U-ban (S02, S06, S10): a U belseje 0,95 × 0,65 m, a 45–50 cm-es szabály mellett az asztal csak a U szájában fér el, és a TV-bútorhoz szorul. **S10 Adularia 85 × 85: 0,23 m a mesa fiókos DM-1 lépcsőjétől** (a fiók nem nyitható). S06 Sculpt Ø90: 0,16 m a TV-sávtól. S02: nincs nevesítve. | 2D `03_kozlekedes_2d_opus_S04_S10.json` | Ø50–60-as kisasztal, vagy két kisasztal a karok mellett |
| K-09 | KÖZEPES | – | NYITOTT | Márvány dohányzóasztal S07 (Kave Home Sheffield, valódi márvány, kész termék) és S08 (Westwing Naruto, valódi márványlap) – most nevesítve; az ár és a kép–valóság egyezés a kép utáni auditban ellenőrizendő. | S07/S08 spec §2 | – (r1-hez képest javult) |
| K-10 | KÖZEPES | – | NYITOTT | **Padló EL2184:** a GOAL §2 szerint Egger **laminált**, Classic 8/32 4V Aqua+, Grey Treviso Oak EL2184 (591760) – IGAZOLT-D (burkolatkiosztási terv). A ME-BAL-080 közeli fotón göcsös, szürkésbarna tölgyhatású laminált és azonos dekorú szegőléc látszik: vizuálisan összeillő, de termékazonosság (címke/szállítólevél), deszkaméret és fektetési irány nem igazolt. Dokumentum-ellentmondás: RRG §A és a westside-skill „parketta”, a v2b referenciakártya „IGAZOLT-D + IGAZOLT-F”, a GEOMETRIA v2 §4 „NEM IGAZOLT”. Opus helyesen, terméknév nélkül, a fotó szerint ír. | GOAL §2; RRG §A; ME-BAL-080 (sha `88f93864…`) | Egységes státuszsor; „parketta” → „laminált padló” (Péter jóváhagyásával); ME-BAL-080 minden képhez |
| K-11 | KÖZEPES | – | NYITOTT | TV-fal-kiállások: D16/D17/D18, G01–G04, G08 minden stílusban a TV-bútor mögé kerül (9–12 villamos figyelmeztetés stílusonként); a G01–G04 a rajzon x 3,91–4,03. | `ki_vegleges/validator_integrator_k13_vegleges_*.json` | Szerviznyílás a hátfalon; hétfői mérés |
| K-12 | KÖZEPES | – | NYITOTT | ML04/ML05 a HF03 hűtő-fűtő mezőben; a rögzítés csak a kiállás dobozába, hőkamera után (Opus: lámpatest ≤ 5 kg cél). Az S10 Styrka Ø 75 × 75 az ML05-ön alsó él 2,15 csak rövid függesztéssel. | 50_KOLTSEG §4, §7 | Hétfő |
| K-13 | MAGAS | – | NYITOTT | **S08 TV-fal nem fér el a leírt módon.** (a) MR-1 torony 60 cm mélyen a D18 előtt: kanapé–torony **0,58 m** (< 0,60); a fal déli végére tolva 0,72 m, de a hálók felé vezető út **0,85 m**-re szűkül. (b) Az MR-2 sárga doboz (120 cm, „a TV-től délre”) a torony és a TV közé nem fér: **40 cm-es ütközés** a toronnyal. | 2D: 0,58 / 0,72 + 0,85; Blender-validátor: ÁTFEDÉS MR-1 ↔ MR-2 40 cm | Opus 45 cm-es „biztonsági” tornya: 0,73 m és minden út ≥ 0,90 – ez legyen a fő változat; az MR-2 ≤ 45 cm széles vagy a TV fölé/északra kerüljön |
| K-14 | KÖZEPES | – | NYITOTT | **S05:** (a) a hat Samantha szék (55 × 55) mellett a 05.3 ajtaja felé 0,89 m (1 cm hiány); (b) a W02-re írt Ø 90 tükör + 100 × 140 vászon együtt 1,90 m, a W02 kapcsolóoszloptól 15 cm-mel szabad része ≈ 1,8 m → a kompozíció a K10–K12 kapcsolókra/T01 termosztátra csúszik. | 2D 1 cm-es felbontás; Blender-validátor: 4 villamos hiba a tükör integrátori helyén | (a) az asztal 2 cm-rel nyugatra vagy 53 cm mély szék; (b) kisebb tükör (Ø 60–70) vagy a vászon a W07-re |
| K-15 | KÖZEPES | – | NYITOTT | Kivitelezhetőség (S01/S02): S02 füstbronz tükör hátfal a mosogató mögött; S02 tükörgardrób (Opus a déli sávot navy lamináltra cserélte – javult); BN-A1 R50 postforming; S01 fürdő faliszekrény a 3D dekorcsempén; S02 fürdő IP67 tükörglória a D43/D44-ről (Opus FELTÉTELES). | 50_KOLTSEG §7 | Gyártói igazolás, villamos zónaellenőrzés |
| K-16 | KÖZEPES | – | NYITOTT | S09: a boiserie-díszlécek **festést** igényelnek (W01, W02, W07, master) – az RRG szerint külön tétel és Péter-jóváhagyás kell (Opus jelzi). | 50_KOLTSEG §7 S09 | Péter döntése |
| K-17 | KÖZEPES | – | – | Költség: lásd 3. pont. | | |
| K-18 | ALACSONY | – | NYITOTT | Fotóazonosító-ütközés: ME-BAL-045 az A-811 erkély és az A-902 nappali fotója is. | két útvonal | Teljes útvonal + sha256 a kártyán |
| K-19 | ALACSONY | – | NYITOTT | S03/S10 ML04 Kave Home Drava: a 50-es fájl „1×E27” Hue-izzót számol, a Kave-oldal szerint E14 (2026-10-24). | KEP004 README; 50 §6 | E14 Hue-izzó |
| K-20 | ALACSONY | – | – | A validátor S08-érzékelő hibája minden stílusnál **téves riasztás** (a 05.1-ben, a fal túloldalán). | `A902_villamos.csv` S08 | Nem tervezési hiba |
| K-21 | ALACSONY | – | NYITOTT | S04: Opus aggálya (a Lilo 176 cm + konzol a 0,60 m-t szűkíti) alaptalan: a HZ-1 konzol 32 cm magas, 40 cm mély → kanapé–konzol 0,80 m. | 2D | – |

**Ami rendben van (7d3c67f):** 60/60 prompt, 511 tétel; a 60 prompt minden megnevezett Westwing/Kave Home/IKEA-terméke szerepel az adott stílus elemlistájában; státuszsor, kameránkénti fény, terméknév nélküli padló, C elrendezés, z 2,53-nál megálló szekrénytestek (kivéve S08 MR-1 60 cm – K-13); Cam_12 állóhelye minden stílusban szabad; a stílusfüggő összegek ≤ 9,60 M mind a tízben.

## 3. Költség – 18 M tervezhető + 2 M tartalék
### 3.1 Opus 50_KOLTSEG összesítője (fő változat, M Ft)
| | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Stílusfüggő Σ | 8,87 | 9,29 | 8,72 | 8,98 | 8,79 | 8,60 | 8,96 | 8,48 | 8,87 | 8,75 |
| + fix 8,40 = lakás | 17,27 | 17,69 | 17,12 | 17,38 | 17,19 | 17,00 | 17,36 | 16,88 | 17,27 | 17,15 |
| **Ennyi fix felett lépi túl a 18,00-t** | 9,13 | **8,71** | 9,28 | 9,02 | 9,21 | 9,40 | 9,04 | 9,52 | 9,13 | 9,25 |

- **Számtan:** az 511 tételből számolt stílusonkénti és soronkénti összegek forintra egyeznek az 50-es fájl 1. táblázatával; a tételszám (53/55/47/51/52/51/48/53/51/50) egyezik a 2. táblázattal.
- **Becslési arány:** 309 becslés, 130 ellenőrzött, 13 árkönyvtári, 47 egységár/mennyiségbecslés, 12 FELTÉTELES. Stílusonként a fő összeg 4,5–5,3 M-ja becslés (Opus: ±20–25 %).
- **A közös fix 8,40 M realitása (integrátori becslés, webár nélkül):** ≈ 8,9–10,0 M (B-01: elszívó a fal nélküli főzőlapsoron +0,3–0,7; szállítás/szerelés 0,45 → 0,6–0,9; terasz árnyékoló/növény 0,45 → 0,6–0,9; emelés a sáv felső végén). **Már 8,9 M-os fixnél az S02 túllépi a 18,00 M-ot; 9,45 M-nál kilenc stílus (az S08 kivételével).**
- **Sávon kívüli sorok** (a célok átcsoportosíthatók, de jelzés): 04c gardróbfal mind a tízben 0,79–0,99 (sáv 0,35–0,70); 03d étkező S04 1,13, S05 0,95, S08 0,92, S09 1,09, S10 1,14 (sáv 0,40–0,90).
- **Terasz-keret ellentmondás** (GOAL §3 ~4 M, skill ~5 M, KOZOS_FIX 3,60 M) és **tartalék** (Correll +1,0 M → 1,0 M tartalék, 5 %) – változatlanul nyitott (B-02, B-03), Péter döntése.

### 3.2 Az 511 tételes lista – ami NEM készült el
- A 130 „ellenőrzött” és 13 árkönyvtári tétel **árát és termékazonosságát az integrátor nem ellenőrizte vissza** a webshopokban (a Westwing és a GitHub ebből a munkamenetből nem érhető el; Kave Home HU-ár Opus szerint is részben nem olvasható). Ez a lépés **nyitott**, nem „kész”.
- Az S04–S10 cseretermékeinek (Lilo, Melva, Wolke Teddy) **gyártói belső méreteit** (ülésmélység, sarokelem szélessége, sarokirány) a lista nem adja meg; a méretpróba feltételezett értékekkel futott (Blender-jelentés 6. pont).

## 4. Kivitelezhetőség – összefoglaló
TV-falak: S01, S02, S04, S07, S09, S10 elfér; S05 a W02-n ütközik (K-14); S08 csak 45 cm-es toronnyal és áthelyezett MR-2-vel (K-13). Kanapék: Lennon, JÄTTEBO U igazolt; Lilo, Melva, Wolke Teddy a feltételezett belső méretekkel elfér (kanapé–TV-bútor 0,80 / 1,12 / 1,33 m). Étkező: 160 × 90 mindenhol; S09 karfás végszék (66 cm) kihúzása ≥ 1,05 m. Hue: K-05, K-19. Asztalos: Egger-anyagszabály tartva; a hajlított elemek (S02 R50, S03 ívek, S05 portál, S07 íves konzol) gyártói igazolást kérnek.

## 5. Teendők
1. Péter: a 7d3c67f-alapú v1.2 négy promptjának elfogadása; push a távoli GitHubra (6. pont).
2. Opus/Péter: K-05 (Idela, Novae foglalat), K-06 (fekete Toni), K-07 (S01 spec), K-03 a stílusdokumentációban és S04-ben, K-02 S03–S10-ben, K-13, K-14.
3. Integrátor (hozzáféréssel): az 511 tétel webes ár- és termékvisszaellenőrzése; Lilo/Melva/Wolke gyártói méretlap.
4. Hétfő (2026-10-26): teraszajtó, kávamélység, G-dobozok, padlócímke, HF03 hőkamera.

## 6. Mentés és push
Lásd a záró commit üzenetét és az átadási csomag végét: a távoli push ebből a munkamenetből nem lehetséges (nincs GitHub-hitelesítés).

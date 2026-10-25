# KEP-004 · V3_TEST (r2-csomag) · S01 és S02 Cam_02 tesztkép – Render Reality Gate-audit

**Készítette:** Claude, 2026-10-25. A képek 02:31 és 02:39 CEST között készültek; az audit a téli időre átállás után (≈02:15 CET) zárult. Protokoll: `ai-coordination/RENDER_REALITY_GATE.md`, B–D pont.

**Jóváhagyás (Péter):**
- **01:55 CEST:** V3 azonnali képteszt két képpel (S01 Kyoto Ink, S02 BiBo Nocturne, Cam_02).
  - Előtte egyesíteni kellett: a V3-blokkokat, a geometria v2-t, a tömbreferenciát, a FIXED/Hue szabályokat, a helyszíni és a termékfotókat.
  - „Ne generáljunk ismét geometriailag hibás képet.”
- **02:22 CEST, „1. opció”:** ez a munkamenet az egyetlen felelős.
  - A két javított tömbkép és a PASS validátor az alap.
  - A tükör csak fizikailag lehetséges képet mutathat. A kültéri pad ellenőrzött hely nélkül nem jelenhet meg.
  - „MEHET pontosan két ChatGPT Images-generálás … egy-egy kép.” „Ne indíts további képeket.”

**A másik munkamenet képei:**
- A másik munkamenet Péter 02:06-os „mehet”-jére 02:18-kor és ≈02:23-kor két `_V3_r1` képet készített, a régi r1-csomaggal. Auditjuk: `WSG-20261025-KEP-004_V3teszt_r1.md`.
- A 02:22-es döntés szerinti tesztpár ez a két `_V3_TEST` kép.
- Összesen 4 V3 Cam_02 kép létezik. A `_V3_r1` képek itt A/B-referenciák. További kép nem készült.

## 0. Összefoglaló

| | S01 Kyoto Ink · V3_TEST | S02 BiBo Nocturne · V3_TEST |
|---|---|---|
| Képstátusz | `KONCEPCIÓ – NEM VALIDÁLT` | `KONCEPCIÓ – NEM VALIDÁLT` |
| Geometriai kontroll (tűrés ±3 % = ±30 px) | **FAIL, javítható:**<br>– a mennyezet és az ablakfej ~35–45 px-szel feljebb van, ezért a tér **~8 %-kal magasabbnak** hat (≈3,1 m a 2,90 helyett);<br>– a padló és a falsarok a helyén van | **A héj megfelel:** a mennyezet, a sarok és az ablakfej ±1 %-on, a küszöb −2 %-on belül van |
| Bútorok a képen | a magas szekrény ≈2,45 m (2,20 helyett), az alsó ≈0,6–0,7 m (0,48 helyett), a TV ~75″-nak hat; az étkező ≈0,3–0,4 m-rel keletebbre | a magas szekrény ≈2,45 m, az alsó ≈0,65 m (0,50 helyett), a tükör alja ≈0,55 m (0,40 helyett), a TV ~72″; az étkező keletebbre |
| Gate összesítve | **FAIL** a belmagasság miatt. Stílus-összevetésre jelöléssel használható | **`ELŐSZŰRT – FELTÉTELES`** stílusdöntéshez. Kivitelezési bizonyítéknak nem alkalmas |
| Elrendezés | Megfelel: TV-fal-együttes balra, kanapé háttal, 3 nyugati szék jobb alul. Nincs függeszték, dohányzóasztal és pad | Megfelel, ugyanígy. A tükör a TV-panel felőli oszlopban van, belső teret tükröz |
| Kreatív (Claude, 1–10) | prémium 7 · WOW 6 | prémium 8 · WOW 7,5 |

**Fő tanulság:**
- Működött a javított tömbkép, a képkeret-százalékok és a fizikailag levezetett tükörszöveg:
  - az S02 héja ±1 %-on belül van, a tükör belső teret mutat, a pad nem jelenik meg;
  - a héj átlagos eltérése 8–26 px, az r1-képeken 34–37 px volt.
- Két hiba megmaradt:
  - A ChatGPT Images **felnagyítja a falbútorokat**, és **keletre tolja az étkezőt**.
  - Ezért a kép tágasabb közlekedést mutat a tervnél: a kanapéhát és a széktámla között ~0,7 m látszik, a terv szerint 0,36–0,38 m van.

## 1. Futtatás

| | S01 | S02 |
|---|---|---|
| Kép-ID | `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_TEST` | `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_TEST` |
| Prompt | KEP004-CGI-V3TEST-r2 · 20 238 karakter · sha256 `eb4f1908…970c` | KEP004-CGI-V3TEST-r2 · 21 327 karakter · sha256 `aea9d602…7f16` |
| Promptforrás | `05_promptok/KEP004_ChatGPT_Images_V3_TEST/`. Az r1→r2 változtatások: `_eszkozok/epito_r2.py`, napló, diff; az integráció leírása: `INTEGRACIO_V3_TEST.md` | ua. |
| Csatolmány (9, sorrendben) | alapkép · **1b javított V3-tömbkép S01** (`ed70d29e…`) · padló ME-BAL-080 · helyszíni lap · panoráma · Lennon · Toni · Eamy · Nifelia | alapkép · **1b javított V3-tömbkép S02** (`b78dd073…`) · padló · helyszíni lap · panoráma · JÄTTEBO U · Anouk · Ciselia · Marely |
| Bemenet-ellenőrzés | Mind a 9 pixelazonos a forrással. 5 fájlról leválasztottam a munkamenet saját C2PA-bélyegét (APP11, 5769 B). Az Eamy és a Nifelia fotója más kivágás, mint a v1-nyilvántartásban; a termék azonosságát szemrevételezéssel ellenőriztem | ua.; a Ciselia és a Marely más kivágás, a termék ugyanaz |
| Beküldött szöveg | bájtra egyezett a fájllal (a záró sortörés nélkül) | ua. |
| Chat | https://chatgpt.com/c/6add4e63-b7c4-83ed-aefc-821359a091f3 | https://chatgpt.com/c/6add4f5c-edf0-83eb-ba22-703be2d0c91b |
| Felület | ChatGPT Plus · Chat mód · „Kép létrehozása” · Gondolkodási erőfeszítés: Erős (High). A pontos képmodell nevét a felület nem mutatja | ua. |
| Idő | küldés 02:31 és 02:35 között; letöltés **02:35:31 CEST** (00:35:31Z) | küldés az S01 letöltése után; letöltés **02:38:54 CEST** (00:38:54Z) |
| Kimenet | 1586 × 992 PNG (natív), sha256 `2fd2bd78…3f8a`. Átvételi név: „Modern Nappali Terasszal és Városi Kilátással.png” | 1586 × 992 PNG, sha256 `e580f2fd…a4f4`. Átvételi név: „Modern nappali terasszal és városi panorámával.png” |
| Újragenerálás | 0 | 0 |

Archív: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/` (kép, futtatott prompt, manifest, `_gate_V3TEST/`).

## 2. Generálás előtti ellenőrzés
Részletek: `05_promptok/KEP004_ChatGPT_Images_V3_TEST/INTEGRACIO_V3_TEST.md`.

**Források és egyesítés:**
- Astra V3 r1 (PR #16, `be6b1f3`) + geometria v2 FRAME LAYOUT + FIXED/Hue + helyszíni és termékfotók.
- A falfelület-kivétel csak a W01–W04 felületekre szól.
- A promptokban nincs ellentmondó utasítás: tiltott kifejezés 0, kötelező elem mind megvan.

**V3-tömbök (Blender v2b-1-k11b):**
- A .blend nem mentődött, sha256 előtte és utána `9875cd57…`.
- Validátor: üres PASS 0/0, S01 PASS 0/8, S02 PASS 0/9.
- A figyelmeztetések:
  - a TV-blokk kiállásai (D16/D17, G01–G04, G08) az alsó szekrény kivehető szervizhátfala mögött vannak;
  - a D18 a magas szekrény mögött van: S01-ben a torony legalsó rekeszének hátfalán át, S02-ben a tükör alatti szervizlapon át érhető el.

**TV-szekrény és magas tároló:**
- A V3 méretei váltották a régi 180 × 45-ös konzoltömböt:
  - S01: KI3-L 240×48×40, KI3-V 60×220×30, KI3-P 260×190;
  - S02: BN3-L 240×50×40, BN3-V 90×220×32, BN3-P 240×190.
- A régi tömbkép KI3-P osztása a TV közepe mögé esett. Ezt kivettem, a KI3-P egy befoglalóként szerepel.
- A tükröt tartalmazó oszlop a TV felőli oldalra került.

**Tükör (S02):**
- Helye: x 3,99; y 4,70–5,15; z 0,40–2,20.
- A kamerából nézve a kamerától keletre–északkeletre eső sávot (y ≈ 5,0–6,2) tükrözi: kanapé, étkezőszékek, asztalél, keleti fal, ajtóél.
- A prompt csak ezt engedi.

**Kültéri pad (KI-O / BN-O):** ellenőrzött helye nincs, ezért nem jelenik meg. A karfatálca marad.

**Távolságok:**
- TV-tengely y 6,35, kanapétengely y 6,40; nézőtáv 2,93 m.
- Az L északi vége 0,46 m-re, a U északi vége 0,225 m-re van az üvegtől.
- Kanapéhát – nyugati széktámla: **0,38 / 0,36 m** (nyitott döntés).

## 3. Reality card – A-902, nappali–terasz, Cam_02 (B pont)

| Felület / elem | Besorolás | Specifikáció és forrás | Bruttó költség | S01 képen | S02 képen |
|---|---|---|---|---|---|
| Padló | MEGLÉVŐ / MEGTARTOTT | Egger Grey Treviso Oak EL2184 (IGAZOLT-D: burkolatkiosztási terv; IGAZOLT-F: ME-BAL-080) | 0 | Szürkésbarna, csomós tölgy. L* 43–59, a fotón 49; a* +3…+4. Közeli, kissé melegebb | Világosabb és sárgább: L* 54–56, b* +6…+13 |
| Mennyezet | MEGLÉVŐ | sima fehér, 2,90 m, hűtő-fűtő panelek | 0 | fehér, de magasabbnak hat | fehér, helyes |
| W01–W04 fal | ÚJ / JAVASOLT | S01: füstös világosszürke papírszálas vlies. S02: halvány ezüstszürke, szövéshatású vlies. Astra V3 „B” csomag, minta még nincs kiválasztva | 160–260 eFt (Astra, becslés) | meleg greige: L* 50–55, b* +5…+6 | meleg greige: L* 51–56, b* +6…+8; nem ezüstös |
| TV-háttér | ÚJ / JAVASOLT | KI3-P: két grafit laminált sík 260×190, ≤ 4 cm, z 0,55–2,45. BN3-P: navy laminált 240×190 | Astra „A” csomag: S01 520–680, S02 650–820 eFt | egy sík; ≈ +0,15–0,2 m-rel feljebb | egy navy sík, a „széles panelfuga” hiányzik |
| Magas szekrény | ÚJ / JAVASOLT | KI3-V: 60×220×30, fehér korpusz, 3 × 64 cm-es nyomott front. BN3-V: 90×220×32 – ajtós oszlop (festett MDF, szatén) + fix ezüsttükör 45×180 (z 0,40–2,20) + szervizlap | az „A” csomagban | ≈2,45 m; 3 front, de nem egyforma magasak | ≈2,45 m; a tükör alja ≈0,55 m; az ajtós oszlop egy frontnak látszik |
| Alsó szekrény | ÚJ / JAVASOLT | KI3-L: 240×48×40, 4 × 60 grafit laminált front, lábazat. BN3-L: 240×50×40, 4 × 60 navy laminált front | az „A” csomagban | 4 front ✓; ≈0,6–0,7 m magas | 4 front ✓; ≈0,65 m magas |
| TV | külön tétel | 65″ (1b) | – | ~75″-nak hat | ~72″ |
| Kanapé | TERMÉK | S01: P14 Westwing Lennon jobbos L, 238×180×68, taupe. S02: P04 IKEA JÄTTEBO U, 285×160×71, Samsala sötétkék (496.076.48) | ebben a körben nem ellenőrzött | ✓ forma, szín | ✓ U, kordbársony, karfatálca |
| Étkező | TERMÉK | S01: P09 Toni 200×90 + 6 Kave Eamy. S02: P08 Anouk üveg 180×90 + 6 Kave Ciselia | nem ellenőrzött | ✓, de ≈0,3–0,4 m-rel keletebbre | ✓, keletebbre; a Ciselia bouclé-hatású, a termék sima zsenília |
| Szőnyeg | TERMÉK | Kave Nifelia 200×300 / Marely 200×300 | nem ellenőrzött | részben látszik: bézs, sötétebb szegély | krémszínű, magas szálú |
| Nyílászáró, káva | MEGLÉVŐ | belül fehér, kívül antracit; sötét téglakáva | 0 | ✓ | ✓ (sötét tégla) |
| Terasz, kilátás | MEGLÉVŐ | gres, emelt WPC lépcsővel, zöldtető, antracit korlát; budai panoráma | 0 | ✓, bútor nélkül | ✓, bútor nélkül |
| Fény | MEGLÉVŐ pontok | Az ML04 a képen kívül van, az ML05 üres. LED nincs, a V3.1-ben jön | – | ✓ | ✓ |

## 4. Geometriai audit: összevetés az alapképpel (C pont)

**Módszer:**
- A v2b-1 modell vonalait és pontjait a Cam_02 paramétereivel vetítettem a képre: [8,30; 4,40; 1,55], Euler [1,479; 0; 0,858], 20 mm, 36 mm-es szenzor, 1600 × 1000.
- A vetítést az alapképen ellenőriztem: a sarok, a padló és az üvegvonal pixelre egyezik (`alap_vetitett_ellenorzes.jpg`).
- Az automatikus mérés (`_eszkozok/kontrollpont_lapok.py` → `kontrollpontok_meres.json`):
  - a fal–mennyezet vonalat a legerősebb világos→sötét lépcsőből olvassa ki;
  - az ablakfejet az alapkép saját mérése szerint korrigálja;
  - a módszer állandó eltérése −5 px, ezt levontam.
- Kézi leolvasás a nagyított lapokról (`kp1`–`kp5`): a küszöb, a padlósarok, a bútormagasságok és az étkező.
- Negatív Δ: a képen feljebb van.

**Héj – kontrollpontok (px):**

| Kontrollpont | Modell | S01 V3_TEST | S02 V3_TEST | S01 V3_r1 (másik) | S02 V3_r1 (másik) | V2 S01 (01:04) |
|---|---|---|---|---|---|---|
| Fal–mennyezet sarok (x 750–800) | 207 / 196 | **−38** | −7 | −25 | −22 | −10 |
| Homlokzati mennyezetvonal (x 1000–1200) | 139 → 82 | **−42…−45** | −5…−6 | −25 | nem mérhető | nem mérhető |
| Ablakfej, z 2,53 (x 1000 / 1450, az alapképhez mérve) | – | **−28 / −36** | −5 / 0 | −24 / −25 | −18 / −22 | −6 / −5 |
| Fal–padló sarok (kézi) | 649 | ≈ −2 | ≈ −2 | −44 ¹ | −34 ¹ | – |
| Üveg alsó éle / küszöb, x 860–920 (kézi) | 680–699 | ≈ −30 | ≈ −20 | ≈ −55 | ≈ −60 | ≈ −65 |
| Üveg alsó éle a jobb szélen | ≈ 880 | székek takarják | székek takarják | −135 ¹ | −100 ¹ | ~−200 ² |
| **A 4 héjpont átlagos \|Δ\|-je** | | **≈ 26 px (2,6 %)** | **≈ 8 px (0,8 %)** | ≈ 37 px | ≈ 34 px | FAIL ² |

¹ A másik munkamenet mérése (`WSG-20261025-KEP-004_V3teszt_r1.md`, 3. pont). ² Az 1a-audit szerint (`WSG-20261024-STYLE10-KEP-004_r1.md`).

**Bútor és elrendezés (kézi; `kp3`, `kp4`, `kp5`):**

| Elem | Terv (1b) | S01 V3_TEST | S02 V3_TEST |
|---|---|---|---|
| Magas szekrény teteje | 2,20 m | ≈ 2,45 m (+60 px) | ≈ 2,45 m (+55–65 px) |
| Alsó szekrény (előlap) | 0,48 / 0,50 m | ≈ 0,6–0,7 m | ≈ 0,62–0,70 m |
| TV-háttér felső éle | 2,45 m | +42 px (a mennyezettel együtt emelkedett) | +24 px |
| Tükör alsó éle (S02) | 0,40 m | – | ≈ 0,55 m; alatta zárt szervizlap ✓ |
| TV (65″ modell: x 366–635, y 391–563) | – | x 338–634, y 329–536 → ~75″, a közép ≈ 40 px-szel feljebb | x 348–643, y 349–539 → ~72″, a közép ≈ 28 px-szel feljebb |
| Étkező (a nyugati széktámlák teteje) | P902_24A | 90–130 px-szel jobbra, vagyis ≈ 0,3–0,4 m-rel keletre | 140–170 px-szel jobbra |
| Kanapé | S01: Lennon L, hát x 7,17. S02: JÄTTEBO U | egyezik a tömbbel (±0,1 m) | egyezik (±0,1 m) |

**Értékelés:**
- **S02:** a héj ±1 %-on belül van, ez eddig a legpontosabb kép. A mennyezet, a sarok, az ablakfej és a profilok egyeznek; a küszöb ~20 px-szel feljebb van.
- **S01:** a padló és a sarkok jók. A mennyezet és az ablakfej azonban ~40 px-szel feljebb került, ezért a tér ~8 %-kal magasabbnak hat. Ez hízelgő, de hamis: a prompt kifejezetten tiltja a megnagyobbított teret. Ezért FAIL.
- **Mindkét képen:**
  - a nyugati falbútorok 10–25 %-kal magasabbak, a TV nagyobb;
  - az étkező keletre tolódott, így a kép elrejti a szűk, 0,36–0,38 m-es kanapé–szék távolságot.
- **Az r2-csomag hatása:** a héjhiba az r1-képekhez képest S02-ben ~4-szer, S01-ben ~30 %-kal kisebb.
  - Ezek ugyanarra a kamerára és ugyanarra az Astra-blokkra készültek. A különbség a javított 1b tömbkép, a pontosított képkeret-százalékok, a tükörszöveg és a nyílászáró/padló-mondat.

## 5. Anyag-, termék- és felületaudit (C pont)

| Elem | Terv | S01 | S02 | Döntés |
|---|---|---|---|---|
| Padló | EL2184, közepes szürkésbarna, csomós | közeli (árnyékban sötétebb, a* +3) | világosabb és sárgább | S01: közeli, de nem igazolt; S02: javítandó |
| Tapéta | S01: füstös világosszürke; S02: halvány ezüstszürke | meleg greige | meleg greige, nem ezüstös | javítandó (tónus); mintafotó kell |
| Fal „bézsítése” | a nem kijelölt fal fehér marad | csak a kijelölt W01/W04 látszik | ua. | rendben (a tónus eltér) |
| Magas szekrény | lásd 3. pont | 3 front, nyomott grafika, fehér korpusz ✓; túl magas | ajtós oszlop egy frontként; tükör és szervizlap ✓; túl magas | javítandó |
| Tükörkép (S02) | csak fizikailag lehetséges | – | belső teret mutat: kanapé a tálcával, székek, üveglap, fehér fal, világosszürke ajtó – **lehetséges** | rendben. Az r1-kép tükre a teraszt mutatta, ott ez FAIL-elem |
| TV-háttér | S01: két sík 15 mm eltolással; S02: széles fugák | egy sík | egy sík, fuga nélkül | javítandó. Az osztás a TV-n kívül legyen (a régi tömbkép TV mögötti osztását kivettem) |
| Alsó szekrény | 4 × 60 front, lábazat | 4 front ✓ | 4 front ✓ | rendben; a magasság javítandó |
| Anyagjelleg | laminált laminált, nyomat nyomat legyen | matt grafit lap, nyomott front; nem kő, nem lakk | matt navy; magasfény nincs, a szatén festett MDF nem látszik | rendben, nem mutat drágább anyagot |
| Kanapé | Lennon taupe L / JÄTTEBO sötétkék U | ✓ | ✓ kordbársony, karfatálca | rendben |
| Székek | Eamy / Ciselia | ✓ | bouclé-hatású (a termék sima zsenília) | S02: kisebb eltérés |
| Szőnyeg | Nifelia / Marely | részben ✓ | ✓ | rendben |
| Kiegészítők | csak a listás bútorokon | tál, könyvek, ágas váza a konzolon | ágas váza, könyvek, kerámia; díszedény az asztalon | rendben (kis tárgyak) |
| Kiállások | kapcsoló, dugalj, FL02 szabadon | új dugalj nem látszik; az FL02 helyén tapéta van, fedlap nélkül | ua. | kivitelezési megjegyzés: a tapéta nem takarhatja az FL02-t |
| Fény, expozíció | azonos, semleges nappali fény | mennyezet L* 69,7, ég 87,2 | mennyezet 72,1, ég 89,8 | ≈ 0,1–0,2 Fé eltérés; elfogadható |

## 6. Költségkockázat (B5)

**Melyik anyagváltozat látszik:**
- A képek **Astra fő (erősebb) anyagváltozatát** mutatják: S01 740–1040 eFt, S02 855–1160 eFt (Astra becslése, 2026-10-25, ajánlatköteles).
- A keretvédő alapértelmezés a **gazdaságos változat**: S01 535–740, S02 650–860 eFt.
- A fő változat az alapszámnál +240, illetve +260 eFt-tal többe kerülhet (Astra V3 r1, 5.1).

**A képen látszó méretek:**
- A magasabb magas szekrény (2,45 m) és alsó szekrény (0,65 m) több anyagot és frontfelületet jelent. Becslés: +5–10 % az „A” csomagon.
- A kivitel a specifikált méretekkel készül, nem a képről.

**Festett MDF (BN3-V):**
- A GOAL 5. pontja szerint „nincs festett front”.
- Astra azt írja, hogy Péter utasítása megengedte a festett MDF-et, de a GOAL ezt nem rögzíti.
- **Tulajdonosi döntés kell.** Alternatíva: Astra gazdaságos változata, kész navy laminált fronttal.

**Ami még nincs kész:**
- Claude független árellenőrzése (termékek + V3-csomagok) még nem készült el.
- A V3-csomagok beillesztése a 18 M + 2 M keretbe sem.
- Árral igazolt elem nincs, ezért a kép az `ELŐSZŰRT` szintnél tovább nem léphet.

**Rejtett költség:** nincs. A képeken nincs listán kívüli bútor, kőhatású tárgy vagy új lámpa.

## 7. Kreatív összevetés: V2 próbakép → V3

| Kép | Geometria (mért) | Prémium* | WOW* | Megjegyzés |
|---|---|---|---|---|
| V2 S01 próbakép (01:04) | FAIL: a tér szélesebb és mélyebb, az étkező rossz helyen | 5 | 4 | csupa bézs japandi; listán kívüli travertinasztal; függeszték nem létező ponton |
| **S01 V3_TEST** | ≈ 26 px; belmagasság +8 % | **7** | **6** | Építészeti falegyüttes, a tusgrafikás torony erős fókusz. A meleg greige tapéta és a taupe kanapé miatt még mindig bézs hangsúlyú; a kompozíció statikus |
| **S02 V3_TEST** | **≈ 8 px** | **8** | **7,5** | Karakteres navy–krém kontraszt, a tükör mélyíti a teret, butikhotel-hatás. A navy tömeg nehéz lehet; a tapéta nem ezüstös |
| S01 V3_r1 (másik) | ≈ 37 px | 6,5 | 6 | a síkok osztása a TV mögött; 3 front |
| S02 V3_r1 (másik) | ≈ 34 px | 7 | 7 | lehetetlen tükörkép (a teraszt mutatja); világos téglakáva |

\* Claude szubjektív értékelése, 1–10. A két V3_TEST kép egymás mellett: `_gate_V3TEST/V3TEST_kreativ_osszevetes.jpg`.

**Javulás V2 → V3_TEST:**
- prémiumérzet +2…+3, WOW +2…+3,5 pont;
- az S02 héjeltérése ±1 %-ra csökkent; az S01-ben megmaradt a belmagasság-torzítás.

## 8. Státusz és döntési kérdések (D pont)

**Státusz:**
- **S01:** `KONCEPCIÓ – NEM VALIDÁLT`, Gate FAIL (belmagasság). Stílus-összevetésre jelöléssel használható.
- **S02:** `KONCEPCIÓ – NEM VALIDÁLT`, Gate `ELŐSZŰRT – FELTÉTELES`. Feltételek:
  - falbútor-magasság a specifikáció szerint;
  - az étkező a P902_24A helyén;
  - a tapéta tónusa mintafotóval;
  - a padló az EL2184 szerint;
  - festett front vagy laminált – döntés;
  - független árellenőrzés.

**Tulajdonosi döntés kell:**
1. **BN3-V front:** festett MDF (GOAL-kivétel kell) vagy navy laminált (gazdaságos változat).
2. **Kanapé–szék távolság, 0,36–0,38 m:** marad, vagy az étkező 0,15 m-rel keletre kerül (→ 0,51–0,53 m). A képek a valóságnál tágasabbnak mutatják.
3. **Anyagváltozat a végleges S01/S02 képekhez:** fő vagy gazdaságos. A 18 M-es egyeztetés még hátravan.
4. **PR #16** (Astra V3 r1): nincs beolvasztva.
5. **A geometria következő javítása:**
   - (a) magassági és helymegkötések a V3.1-promptban;
   - (b) a másik munkamenet A0-javaslata: egy kép szerkesztő módban, S01 – külön „mehet” kell.
   - Claude javaslata: (a) és (b) együtt, egyetlen S01-képen.

**Javaslat a V3.1-promptba (nem indítva):**
- **Magasság:**
  - a magas szekrény fölött kb. 0,7 m széles falsáv maradjon;
  - az alsó szekrény térdmagasságú (≈ 0,5 m), a TV alja ≈ 0,35 m-rel fölötte;
  - a TV 65″.
- **Étkező:** „a jobb alsó sarokban marad, nem tolódik keletre”.
- **TV-háttér:** a KI3-P osztása a TV-n kívül legyen.
- **Anyagok:**
  - tapétatónus anyagmintafotóval („materials only”);
  - S02-ben a padló: EL2184, ne világosodjon;
  - a Ciselia sima zsenília.

## 9. Bizonyítékok
Mappa: `04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/_gate_V3TEST/`

- **Vetítés:**
  - `S0x_V3TEST_vetitett_atfedes.jpg` – piros: fal és nyílás; narancs: üvegprofil; cián: V3-tömbök; sárga: kiállások;
  - `alap_vetitett_ellenorzes.jpg` – a vetítés ellenőrzése az alapképen.
- **Átfedések:**
  - `S0x_V3TEST_blend50_alapkep.jpg` – 50 %-os átfedés az alapképpel;
  - `S0x_V3TEST_elatfedes_alap_piros_tomeg_cian.jpg` – élátfedés.
- **Összevetések:**
  - `S0x_V3TEST_geometriai_osszevetes.jpg` – alapkép, 1b tömbkép, generált kép és vetített ellenőrzés egy lapon;
  - `V3TEST_kreativ_osszevetes.jpg` – V2 → V3_TEST és a másik munkamenet két képe.
- **Részletek:** `S0x_V3TEST_reszletek.jpg` – szekrények, TV-fal, pillér, étkező, terasz.
- **Kontrollpontok:**
  - `kp1` mennyezet és ablakfej; `kp2` sarok és küszöb (6 kép); `kp3` alsó szekrény magassága; `kp4` étkező helye; `kp5` nyugati fal bal része; `kp6` padlóminta-területek;
  - a mért értékek: `kontrollpontok_meres.json`.
- **Eszközök:** `05_promptok/KEP004_ChatGPT_Images_V3_TEST/_eszkozok/`: `gate_atfedes.py`, `osszevetes_lapok.py`, `reszlet_lap.py`, `kontrollpont_lapok.py`.

**Nem történt:** további generálás, Astra-indítás, a PR #16 beolvasztása, külső megrendelés vagy ajánlatkérés.

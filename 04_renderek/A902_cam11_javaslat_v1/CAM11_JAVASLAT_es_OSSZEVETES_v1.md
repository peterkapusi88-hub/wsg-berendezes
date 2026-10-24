# A-902 · 05.1 master – Cam_11_Master_Panorama JAVASLAT és Cam_04 összevetés (KEP-004, v1, 2026-10-24 22:45)

**Státusz:** JAVASLAT – draft PR (v2b-1-k11). A **Cam_04_Master marad az összehasonlító master**, amíg Péter külön jóvá nem hagyja a cserét. Az Astra Cam_04-promptok változatlanok.
- Az ágyat, a falakat és a nyílásokat nem mozdítottam. A színes testek a képeken csak jelölések.
- A képek ellenőrzőképek, nem látványtervek.
- Képgenerálás nem indult.

## 1. Rövid válasz

**Az ágyból a panorámát nézzük? IGEN.**
- Az ágy fejvége a modellben és a tervrajzon is a keleti (nappali felőli) falon van, a lábvége nyugatra mutat, így az ágyból szemből a 3,64 m-es nyugati üvegfalat és mögötte a valós budai panorámát látjuk (ME-BAL-077).
- Ülve (szem ≈1,20 m) az erkélykorlát teteje 3°-kal a szemmagasság alatt van, ezért a távoli tetőtáj és a hegyek a korlát fölött látszanak.
- Fekve, párnán (≈0,90 m) a korlát nagyjából szemmagasságban van: a közeli tetők a pálcák között, a hegyek fölöttük látszanak.

**Melyik kamera mutatja jobban a luxusenteriőrt és a kilátást?**
- **A kilátást egyértelműen a Cam_11.** Az üvegfal a képkocka 38 %-át adja, a Cam_04-en 0 %-ot (vetítéssel számolva).
- **A luxusenteriőrt összességében szintén a Cam_11.** Szimmetrikus, egyenes függőlegesű kép, középen a tér legnagyobb értékével (panoráma), két oldalról a gardróbfalak keretezik, elöl az ágy lábvége horgonyoz.
- A Cam_04 a fejvéget (a képkocka 11 %-a) és az északi fülkét mutatja, ablak nélkül. A stílusok fejvég-szignatúrája ott látszik jobban.

**Javaslat:**
- A Cam_11 legyen a master-kamera.
- Ehhez kell Péter jóváhagyása és a Cam_11 kamerablokk (`05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md`), a v3.1 §2 Cam_04-blokkja helyett.
- Az Astra-stílusblokk szó szerint marad. A kamerablokk kimondja, hogy a fejvég a kamera mögött van, és a stílusnak a látható elemekben kell megjelennie: lábvég, ágynemű, gardróbfrontok, függöny, szőnyeg, fények.
- Ha Péternek a fejvég-szignatúra fontosabb, a Cam_04 marad, a Cam_11 pedig a döntősöknél lehet kiegészítő kép.

## 2. Az ágy helye és tájolása (ellenőrzés)

| Forrás | Hely | Tájolás | Megjegyzés |
|---|---|---|---|
| Blender-modell (`A902_Butor`, renderben rejtve) | `Agy_05_1_TALLASEN_180x200`: keret x 1,56–3,56, y 5,10–6,90, h 0,30; fejtámla x 3,50–3,56, h 1,05 | fejvég a keleti falon, lábvég nyugat felé | a Zenit (`Z_agy_*`) és a Lake Forest (`L_agy_*`) réteg ugyanezen a befoglalón van |
| Tervrajz (brosúra + 1:50, KORR 2025-10-13) | ágyjel ≈1,98 × 1,79, **tengely ≈ y 6,40** (rajzból mérve, ±5 cm) | ugyanígy | párnák a keleti falnál |
| Villamos kiállások (terv szerint) | éjjeli csoportok 0,65 m-en a keleti falon: D22/D23 + K14 y 5,16–5,36; D20/D21 + K13 y 7,47–7,71 → **közép y 6,41**, tiszta köz 2,19 m | – | a terv szándéka: legfeljebb kb. 2,10 m széles ágy + fejvég a két csoport között |

- **Eltérés:** a modell ágya 0,40 m-rel délebbre van, mint a terv. Ezen a helyen a 2,60 m-es fejvég-befoglaló (és a modell TÄLLÅSEN-fejtámlája) **eltakarja a D22/D23 dugaljat és a K14 kapcsolót**. A kapcsoló a GOAL 5. pontja szerint nem takarható.
- **Nem mozdítottam.** Döntés Péteré. Javaslatom: a terv szerinti y 6,40 tengely. Ha a fejvég 2,10 m-nél szélesebb, kivágás kell a kiállásoknál.
- **Hiteles befoglaló a képeken:**
  - IKEA NORDLI 203.498.53, **180 × 202 × 30 cm** (IKEA HU termékoldal, 2026-10-24, ellenőrzött; egyezik Astra S01/S02 rekordjával).
  - Matrac: magassága ismeretlen. A képen 22 cm-es becslés (sárga).
  - Fejvég: Astra-befoglaló W260 × H85/H100 × D8/D6 (tervezett, nem gyártmány; lila).
  - 60 cm-es szabad sáv mindkét oldalon (zöld).
  - A tervrajz ágyhelye kék kontúrral.

## 3. Cam_11_Master_Panorama – paraméterek és indoklás

| Paraméter | Érték | Miért |
|---|---|---|
| Hely | [3,20; 6,10; 1,20] | x 3,20: kb. 0,30 m-re a fejvég síkja (x 3,49) előtt, ahol egy ülő ember szeme van. y 6,10: az üvegfal közepe (szimmetrikus kép); a modell ágytengelyétől 0,10, a tervétől 0,30 m-re, mindkét esetben az ágyon. z 1,20: NORDLI 0,30 (ellenőrzött) + matrac ~0,20–0,25 (ismeretlen) + ülő szemmagasság a fekvőfelület fölött ~0,70 (becslés) → ±10 cm |
| Forgatás | [π/2; 0; π/2] | vízszintes (a függőlegesek egyenesek), pontosan nyugat felé |
| Objektív | 20 mm, 36×24 AUTO, 1600×1000 | ugyanaz, mint a Cam_02/03/04 – a sablon szerint a luxus nem jöhet szélesebb objektívből; a teljes üvegfal belefér (±28°, a látószög ±42°) |
| Clip | 0,1–200 | mint a többi kamera |

## 4. Számszerű összevetés (vetítés a lock geometriájával – `vetitesi_elemzes_cam04_cam11.json`)

| Elem a képkockán | Cam_04 | Cam_11 |
|---|---|---|
| Nyugati üvegfal (kilátás) | **0 %** | **38 %** (x 329–1270, y 153–804 px) |
| Fejvég homlokfelülete | 11 % | 0 % (a kamera mögött) |
| Ágy teteje | 10 % | 10 % (lábvég, alsó sáv) |
| Északi fülke – gardróbfal helye | 23 % (bal oldal, szemből-ferdén) | jobb szél, élben |
| Déli gardrób (2,42 m, modell: PAX) | 0 % | 11 % (bal szél) |
| Keleti fejvégfal | 39 % | 0 % |

## 5. Látóvonal az ágyból

- **Erkély:**
  - padló −0,15 m; pálcás korlát teteje +0,95 m a szobapadlóhoz képest;
  - az üvegfal északi kétharmada előtt az erkély csak 0,82 m mély (korlát x −1,12), délen 1,71 m (x −2,01).
- **Ülve (1,20 m):** a korlát teteje −3,3° / −2,7°. Félig ülve (1,05 m): −1,3°. Fekve, párnán (0,90 m): +0,7°.
- **Az üvegfal:** alja +0,05, teteje +2,54 m. Ülve −18,9° és +21,3° között látszik.
- **Valós kilátás:**
  - Forrás: ME-BAL-077 (2026-10-21 14:52, a 05.1-ből). Az üvegfal három mezője, az északi fülke és az ÉK-i pillér azonosítja a helyiséget.
  - Tartalom: városi tetőtáj, templomtorony, a budai hegyek a horizonton.
  - A Blender égboltja egyszínű, a kilátást képgeneráláskor ez a fotó adja.

## 6. Gardróbfal az északi fülkében – Péter döntése (22:37–22:40)

- **Mindkét kamerára érvényes:**
  - padlótól plafonig érő gardróbfal az északi fülkében, ≈3,00 × 0,90 × 2,90 m;
  - a front a pillér síkjában van (y 8,04/8,05);
  - a fülkében nincs mennyezeti hűtő-fűtő mező (a HF02 csak y 8,05-ig tart);
  - a hátfalon a D26 dugalj és a G05 adataljzat kivágással marad elérhető.
- **A front stílusonként változik, Péter szerint „bármi, ami szexi”.** Őszinte anyagnévvel: tükör, tapétával vagy textillel bevont, bőrhatású kárpitozott.
  - S01: halvány kőszínű, szőtt hatású textiltapéta.
  - S02: füstös bronz tükör.
  - Részletek: `05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md` (main).
- Ellenőrzőképek: `ellenorzes_Cam04_gardrobfal_javaslat_v1.png`, `ellenorzes_Cam11_gardrobfal_javaslat_v1.png`.
  - A Cam_04-en a gardróbfal a kép bal 40 %-át adja.
  - A Cam_11-en a déli PAX-szal együtt két oldalról keretezi az üvegfalat.

## 7. Nyitott műszaki kérdések

1. **Ágy y-helye:** modell 6,00, terv és kiállások 6,40 (lásd 2.). Péter dönt.
2. **Az erkély északi vége:** a ME-BAL-077-en világos téglafal látszik az üvegfal jobb (északi) széle mellett (homlokzati visszafordulás). A modellben itt pálcás korlát van (`v2_Korlat_erkely_3`). A Cam_11 kép jobb szélén látszik. A hétfői fotóval/méréssel kell javítani, külön PR-ben. Addig a Cam_11 kamerablokk a fotót követi.
3. **Matrac és fejvég végleges terméke.** Ezektől függ az ülő szemmagasság (±10 cm) és a fejvég takarása.
4. **Függöny:**
   - Csak falra szerelt sín jöhet az üvegfal feletti 0,33 m-es falsávban; a mennyezet (HF02 hűtő-fűtő mező) nem fúrható.
   - Az árnyékoló külső motoros redőny (R03/R04).
5. **Gardróbfal-mélység** (0,90 m fülke). Három lehetőség, ajánlat kell:
   - PAX 58 cm, 30 cm-rel beljebb (fülkés hatás);
   - előrehozott front, mögötte üreggel;
   - asztalos 85–90 cm mély korpusz.
6. **Fotóbesorolás:**
   - A ME-BAL-060 és -069 a zöldtetős teraszajtót mutatja, tehát 05.3.
   - A ME-BAL-063 időbélyege és sorrendje alapján valószínűleg 05.3.
   - A ME-BAL-072 kétszárnyú erkélyajtó, tehát 05.2.
   - **A 05.1 helyszíni fotója a ME-BAL-077.**
   - Astra Cam_04-bemenetlistáját nem írtam át. A ChatGPT Images-csomag dokumentáltan a ME-BAL-077-et használja.
7. **A Cam_11 alapkép** (`A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png`) csak jóváhagyás után válik hivatalos „image 1”-gyé.

## 8. Fájlok (`04_renderek/A902_cam11_javaslat_v1/`)

| Fájl | Tartalom |
|---|---|
| `A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png` | Cam_11 üres alapkép-javaslat – az alapképekkel azonos beállítás (EEVEE, egyszínű égbolt 0,86/0,88/0,92, AgX MHC, exp. +0,75) |
| `ellenorzes_Cam04_agybefoglalo_v1.png`, `ellenorzes_Cam11_agybefoglalo_v1.png` | az ágy valós befoglalójával, a 05.1 kiállásaival (Cam_04-en látszanak) |
| `ellenorzes_Cam11_fekve_z090_v1.png` | ugyanez fekvő (0,90 m) szemmagasságból |
| `ellenorzes_Cam04_gardrobfal_javaslat_v1.png`, `ellenorzes_Cam11_gardrobfal_javaslat_v1.png` | gardróbfal-befoglaló az északi fülkében + a modell déli PAX-a |
| `ellenorzes_05_1_felulnezet_Cam04_Cam11_v1.png` | felülnézet: látómezők, ágyhelyek, kiállások, erkély, korlát, látóvonal |
| `osszevetes_Cam04_Cam11_v1.jpg` | összehasonlító lap (6 kép) |
| `render_log_*.json`, `vetitesi_elemzes_cam04_cam11.json`, `vizsgalat_05_1_modell_objektumok.json` | naplók, vetítési számítás, a modell 05.1-es objektumai |

Szkriptek: `03_blender/geometry_v2/cam11/`. Validátor: `03_blender/validator_report_2026-10-24_v2b1k11_cam11.md`.

## Reality card – Cam_11 alapkép (JAVASLAT)

- **Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Helyszínen nem mért, ±5 cm.
- **Változatlanul a képen:**
  - fehér falak és mennyezet, 2,90 m;
  - EL2184 padló (a modellben semleges szürke, az anyaghűséget a ME-BAL-080 fotó adja);
  - üvegfal: 3 mező, fehér profil;
  - erkély, greslap, pálcás korlát.
- **Bizonytalan:**
  - az erkély északi vége (téglafal vs. korlát);
  - az üvegfal-osztás pontos mezőszélessége (a modell 0,90/0,90/1,84 m; a fotó perspektívája nem mond ellent, mérendő).
- **Nincs a képen:** bútor, kilátás (egyszínű égbolt).

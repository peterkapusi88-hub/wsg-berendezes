# A-902 · Opus 5.5 V3.1 (PR #22) – Blender-méretpróba, 2. kapu (Claude integrátor, 2026-10-25)

**Státusz:** `MÉRETPRÓBA – TERV SZERINTI GEOMETRIA` (helyszínen nem mért, ±5–15 cm).
- **1–4. pont:** az Opus-ág `b24bee7` állapotára (az első kör, a végleges forrás előtt).
- **5–6. pont: a végleges forrás, `7d3c67f`** (S01/S02 a v1.2 javított promptokkal; S04, S05, S07, S08, S09, S10).

## Bemenet és sértetlenség
- .blend: `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` (v2b-1-k13), sha256 `e01170d3…70ddbd`. **Másolaton** fut (`A902_k13_MASOLAT_integrator.blend` a scratch mappában); a szkript nem ment.
- Az eredeti és a másolat sha256-ja a futás előtt és után is `e01170d3…` (`ki/eredeti_sha_elotte.txt`, `ki/sha_utana.txt`).
- Blender 5.2.3 LTS, háttérfolyamat; lock: `03_blender/geometry_lock_A902_v2b.json`; villamos: `01_alaprajzok/villamos_kiallasok/A902_villamos.json`.
- Szkriptek: `01_kozlekedes_2d_opus_S01_S02.py` (a repó 2D motorja, `elrendezes_alt_a902.py`, csak olvasva) és `02_blender_opus_S01_S02.py` (tömbök, validátor, sugárvetés, tömbképek).

## Tömbök (integrátori koordináta-hozzárendelés; Opus koordinátát nem adott)
| Elem | S01 | S02 |
|---|---|---|
| Kanapé | Lennon jobbos L 238 × 180 × 68, háttámla x 6,67, chaise délen | JÄTTEBO U 285 × 160, háttámla x 6,60, x 5,00–6,60 / y 4,975–7,825 |
| Étkező | Toni 160 × 90, x 8,00–8,90 / y 5,40–7,00, 6 × Eamy 55 × 53 | ua., fekete (nem igazolt), 6 × Ciselia 52,5 × 55 |
| TV-fal | KI-A: washi-panel ≤ 4 cm (padlótól 2,885-ig); torony 60 × 40 × 253 a D18 előtt (y 4,45–5,05); úszó pad 260 × 42, alja 18 cm (y 5,05–7,65) | BN-A: déli kabinet 80 × 45 × 253 (y 4,05–4,85), északi 70 × 40 × 253 (y 7,35–8,05), ezüst mező ≤ 4 cm, úszó pad 220 × 40, alja 22 cm (y 5,00–7,20), 2 tükörrés |
| TV | 65", tengely y 6,25, képközép z 1,15 | ua. |
| Dohányzóasztal | **FELT.** Ø80, h 35, középpont (4,85; 6,85) | **FELT.** 60 × 60, x 4,60–5,20 / y 6,10–6,70 |
| ML04 | Somar Ø76, **FELT.** z 1,55–1,90 | Brisia Ø50 gömb, **FELT.** középpont z 1,70 |
| ML05 | Misaki Ø40 × 70, alja 2,15 | sárgaréz-opál, **FELT.** Ø60, alja 2,15 |
| W02 | tusvonás-mű 120 × 200 (4 cm), tintavonal-sín z 2,10 (8 cm mély) | navy lábazat 1,8 cm z 1,10-ig, mű 140 × 180 |
| Növény | **FELT.** Ø45-ös kaspó a W02 DNy-i sarkában (5,45; 4,285), h 1,80 | olajfa, ua., h 2,00 |

## 1. Közlekedés (2D, betolt székkel; fő út ≥ 0,90 m)
| Eset | Konyha | Hálók | 05.3 | Terasz | Székkihúzás min | Kanapé–TV-bútor | Kötelező |
|---|---|---|---|---|---|---|---|
| S01 alap, középső szárny | 1,00 | 1,00 | 0,90 | 0,90 | 1,05 | 0,74 | **OK** |
| S01 + dohányzóasztal + W02-mű | 1,00 | 1,00 | 0,90 | 0,90 | 1,05 | 0,74 | **OK** |
| S01 + függöny a szemöldökben | 1,00 | 1,00 | 0,90 | 0,90 | **0,93** | 0,74 | **OK** |
| S01 + **W02-növény** | 1,00 | **0,70** | 0,90 | 0,90 | 1,05 | 0,74 | **NEM** |
| S01, **csak keleti szárny**, 2+2+1+1 | 1,00 | 1,00 | 0,90 | **0,75** | 1,05 | 0,74 | **NEM** |
| S01, csak keleti szárny, **5+1** | 1,00 | 1,00 | 0,90 | 0,95 | 1,33 | 0,74 | **OK** |
| S02 alap, középső szárny | 0,95 | 0,90 | 0,90 | 0,90 | 1,05 | 0,89 | **OK** |
| S02 + navy lábazat + dohányzóasztal | 0,95 | 0,90 | 0,90 | 0,90 | 1,05 | 0,89 | **OK** (a hálók felé 0,925 − 0,018 ≈ 0,907 m – határeset) |
| S02 + függöny a szemöldökben | 0,95 | 0,90 | 0,90 | 0,90 | **0,93** | 0,89 | **OK** |
| S02 + **W02-olajfa** | 0,95 | **elzárva (< 0,50)** | 0,90 | 0,90 | 1,05 | 0,89 | **NEM** |
| S02, **csak keleti szárny**, 2+2+1+1 | 0,95 | 0,90 | 0,90 | **0,70** | 1,05 | 0,89 | **NEM** |
| S02, csak keleti szárny, **5+1** | 0,95 | 0,90 | 0,90 | 1,00 | 1,35 | 0,89 | **OK** |

A W02 és a kanapé távolsága: S01 1,16 m, S02 0,93 m. A motor felbontása 5 cm; a teljes táblázat: `01_kozlekedes_2d_opus_S01_S02.json`.

**Teraszajtó – két forgatókönyv (a 2026-10-26-i mérésig):**
- **A) Középső szárny nyílik:** mindkét stílus hat székkel megfelel.
- **B) Csak a keleti, 0,93 m-es szárny nyílik:** a hat szék nem tartható (0,75 / 0,70 m). Az 5+1 (északi végszék alkalmi pótszék) megfelel. Ez megegyezik a GEOMETRIA v2 §4-gyel és Opus specifikációjával.

## 2. Validátor (geometry_validator_v2)
| Mód | Eredmény | Megjegyzés |
|---|---|---|
| üres | **PASS – 0/0** | lock, terasz, kamerák változatlanok |
| referencia (beépített szaniterek) | FAIL – 6 hiba, 3 figyelmeztetés | **a Cam_10 ismert régi szaniterhibái**, változatlanok: törölközőszárító 06.1 ↔ fal 3 cm; zuhanytálca 3 cm, zuhanyüveg 2 cm, mosdó 10 cm ↔ a 06.2 keleti fala; WC-tartály ↔ akna 2 cm és ↔ déli fal 2 cm. Csak a fürdőmodellt érinti; javítás a hétfői mérés után, külön PR-ben (`validator_nyilvantartas_A902_kameracsomag_C.md`). |
| OPUS_S01 | FAIL – 1 hiba, 14 figyelmeztetés | a hiba **téves riasztás** (S08 érzékelő a 05.1-ben, a fal túloldalán; 12 cm-es tűrés). Figyelmeztetések: D16/D17/D18, G01–G04, G08 a TV-fal mögött (szerviznyílás kell); a W02-mű ↔ növény 3 cm; a mű ↔ tintavonal-sín 4 cm (a sín a mű fölött fusson, vagy a mű teteje z 2,05 alatt legyen). |
| OPUS_S02 | FAIL – 1 hiba, 13 figyelmeztetés | ugyanaz a téves S08; D/G-pontok a TV-fal mögött; a W02-mű ↔ olajfa 3 cm |

Kanapé, asztal és székek ↔ fal vagy nyílászáró ütközése: **0**. Ajtóforgás-hiba: **0**.

## 3. Kamera – képterület és kitakarás (sugárvetés 160 × 100)
| | Cam_02 S01 | Cam_02 S02 | Cam_12 v3 S01 | Cam_12 v3 S02 |
|---|---|---|---|---|
| Kanapé | 13,2 % | 16,8 % | **16,5 %** | **23,3 %** |
| TV-fal (bútor + panel + TV) | 25,1 % | 24,7 % | – | – |
| Üveg, terasz, kilátás | 26,4 % | 25,0 % | – | – |
| W02 + mű | – | – | 16,5 % | 12,6 % (+1,0 % lábazat) |
| W07 | – | – | 7,1 % | 6,9 % |
| W03 (05.3 ajtó) | – | – | 8,1 % | 8,2 % |
| Étkező | 4,8 % | 4,9 % | 8,5 % | 6,9 % |
| Növény (W02) | **4,5 %** | **4,9 %** | **4,9 %** | **3,8 %** |
| W01 takaratlan (a képben lévő részből) | 67 % | 61 % | – | – |
| W02 takaratlan | – | – | 83 % | 72 % |

- **ML04 a Cam_02-ben:** a képen kívül (vízszintes vetület x > 1,04). Ezért mind a tíz Cam_02 prompt „ML04 a jobb szélen” mondata hibás (audit K-02).
- **ML05:** Cam_02-ben a felső szélen, középen; Cam_12-ben a felső szélen lép be. Ez egyezik a promptokkal.
- **Cam_12 állóhely** (x 4,30–4,50; y 7,75–8,05): csak a szőnyeg ér bele (padlószint) – szabad.
- **A növény** Cam_12-ben a W02-mű jobb részét takarja, Cam_02-ben a bal szélen a torony vagy kabinet elé áll (audit K-03, K-16).
- **A dohányzóasztal** a Cam_02-ben a kanapé háttámlája mögött 0,6–0,7 %-ot ad – kép szempontjából nem kritikus.

Tömbképek (EEVEE, 800 × 500): `ki/A902_OPUS55_{S01,S02}_{Cam02,Cam12v3}_tomeg_integrator.png`. Ezek **tömb-ellenőrző képek**, nem a képgeneráláshoz csatolandó semleges alapképek.

## 4. Verdikt (S01/S02, Cam_02 + Cam_12)
**FELTÉTELES PASS:**
- a W02 melletti növény törlésével minden kötelező méret teljesül (középső szárnyas esetben hat székkel, keleti szárnyas esetben 5+1-gyel);
- villamos hozzáférés: szerviznyílás a TV-bútor hátfalán (D16/D17/D18/G);
- az ML04-mondat cseréje a Cam_02-promptokban.

Nem igazolt (hétfő, 2026-10-26): teraszajtó, kávamélység (az S02 U-kar és a függöny), G-dobozok helye, padlócímke és deszkairány, HF03 hőkamera az ML04/ML05-nél, a 06.2 szaniterei.

---

## 5. Végleges forrás (7d3c67f) – S01/S02 a v1.2 promptokkal
Szkript: `04_blender_opus_vegleges.py` (ugyanazon a másolaton; sha előtte/utána `e01170d3…`); kimenet: `ki_vegleges/`. Változás az 1–4. ponthoz képest: a W02-növény törölve (v1.2), az S02 lámpái a végleges forrás szerint (ML04 Kave Home Idela Ø26, ML05 Westwing Dancing Ø65 × 38), a W02-mű alsó éle S01-ben 2,05 alá igazítva (a tintavonal-sín fölötte).

| | S01F | S02F |
|---|---|---|
| Validátor | 1 téves hiba (S08 érzékelő, fal túloldala), 12 villamos figyelmeztetés (D/G a TV-fal mögött) | ua. |
| Bútor ↔ bútor átfedés | **0** (az r1-ben lévő mű ↔ növény és mű ↔ sín megszűnt) | **0** |
| Cam_02: TV-fal / takaratlan W01 | 25,5 % / 96,8 % | 25,0 % / 94,0 % |
| Cam_02: ML04 vetület | x 1,04–2,33 – **képen kívül** | x 1,23–1,56 – **képen kívül** |
| Cam_12 v3: kanapé | 16,5 % | 23,3 % |
| Cam_12 v3: W02 takaratlan | **100 %** (r1: 83 %) | 85,7 % (a U háttámlája takar alul; r1: 72 %) |
| Cam_12 állóhely | szabad | szabad |
| Közlekedés (2D, 1. pont) | változatlan: minden kötelező út OK középső szárnnyal; keleti szárnynál 5+1 | ua. |

## 6. Végleges forrás – S04, S05, S07, S08, S09, S10 (prioritás szerint)
Szkriptek: `03_kozlekedes_2d_opus_S04_S10.py`, `03b_finomitas_S04_S05_S08.py` (1 cm-es felbontás), `04_blender_opus_vegleges.py`. A kanapék gyártói belső méretei nincsenek az elemlistában – **FELT** (lásd a táblát); a koordinátákat az integrátor rendelte hozzá. Teraszajtó, csak keleti szárny: minden stílusban 0,65–0,77 m → 5+1 kell (5+1-gyel 0,95–1,00 m).

| Stílus | Ellenőrzött elem | Eredmény (középső szárny) | Verdikt |
|---|---|---|---|
| **S04** Lilo bouclé L 260 × 176 × 79 (FELT: ülés 100, sarokelem 100, sarok délen, északi vég y 7,59) | kanapé–HZ-1 konzol (32 magas, 40 mély) | 0,80 m; W02–kanapé 0,94; hálók felé 0,94 **olajfa nélkül**, az olajfával elzárva; északra tolva (y 7,70) a hálók felé 1,05, de az olajfával 0,55 | **NEM** a spec szerint (olajfa – K-03); olajfa nélkül **OK** |
| **S05** Melva kord L 238 × 143 × 75 (FELT: ülés 90, sarok délen) | kanapé–MS-1 konzol; Samantha 55 × 55 székek; W02 tükör + vászon | kanapé–konzol 1,12; **05.3 felé 0,89 m** (1 cm hiány); a Ø 90 tükör + 100 cm vászon nem fér a W02 kapcsolóoszlop előtti ≈ 1,8 m-ére (villamos hiba K10–K12, T01) | **NEM** (K-14) – kis módosítással javítható |
| **S07** Wolke Teddy 256 × 118 × 65 (FELT: ülés 95, rövid szár délen) | kanapé–LF-2 konzol | 1,33 m; minden út ≥ 0,90 (hálók 0,95) | **OK** – a nappali üresebb (Opus is jelzi) |
| **S08** Lennon L + MR-1 grafit torony 60 × 253 × 60 | kanapé–torony; MR-2 sárga doboz | a D18 előtt: **0,58 m**; a fal déli végén: 0,72 m, de a hálók felé **0,85**; **MR-2 ↔ MR-1 40 cm-es ütközés**. 45 cm-es toronnyal: 0,73 m, minden út ≥ 0,90 (05.3 0,92) | **NEM** 60 cm-mel; **OK 45 cm-mel**, ha az MR-2 áthelyezve (K-13) |
| **S09** Lennon L + 2 Calan karfás végszék (66 × FELT 60) | végszék-kihúzás, utak | kihúzás min. 1,05; konyha 0,90 (határ); terasz 0,90 | **OK**; keleti szárnynál 5+1 (az északi végre oldalszék) |
| **S10** JÄTTEBO U + mesa (DM-1 400 × 30 × 45; DM-2 130 × 60 × 40; DM-3 70 × 160 × 40; napkorong Ø 100) | kanapé–mesa; Adularia 85 × 85 a U-ban; napkorong | kanapé–mesa 0,88; utak OK; **Adularia ↔ DM-1 fiókos lépcső 0,23 m** (a fiók nem nyitható); a napkorong (y 7,00–8,00) a TV és az üvegsarok közé épp befér | **OK** az utakra; **NEM** a dohányzóasztalra (K-08) |

Kamera (minden stílus): az ML04 a Cam_02 képkeretén kívül van (x 1,14–1,84) – K-02 mind a tízben; a Cam_12 állóhelye szabad; az ML04 a Cam_12-ben mindenütt a képen van. Validátor: mindenütt a téves S08-érzékelő hiba + 9–12 villamos figyelmeztetés (D/G a TV-fal mögött); valódi ütközés csak az S08-ban (MR-1 ↔ MR-2). Az S05 portál ↔ TV 4,9 cm-es átfedése modellezési egyszerűsítés (a portál tömör tömbként), nem tervezési hiba.

**A Cam_10 régi szaniterhibái** (6 hiba, 3 figyelmeztetés) változatlanok; külön kezelve (2. pont), a hétfői mérés után külön PR.

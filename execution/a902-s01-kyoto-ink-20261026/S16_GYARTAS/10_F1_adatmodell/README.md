# S16 R14 médiafal – 1. fázis: gyártási adatmodell + QA

Készült: 2026-10-30, Claude (Opus 5.5). Státusz: **TERVI ADATMODELL – nem gyártási kiadás.** A QA jelenleg **BLOKKOL** (lásd lent), ez a várt és helyes eredmény: az R14 adatokban valódi hibák vannak.

## Mi ez?

Az R14 `parts.json` 120 fő alkatrészéből egy forrásból generált gyártási adatmodell, plusz egy visszaolvasó QA, ami minden későbbi exportot (DWG/DXF, Excel, címke, MPR) kapuként megelőz. Az S01 R16 tanulsága (`212×-222×18` a 101. oldalon) itt gépi blokkoló szabály.

```
forras_R14/              változatlan R14 másolat (SHA-256 egyezik az R14 audit/SHA256SUMS.txt-vel)
gyartasi_szabalyok_v1.json   MINDEN műhelyi feltételezés egy helyen (élanyag, előmarás, ráhagyás, lapméret, A-oldal, ütköző) – jelölve
s16_geom.py              helyi koordináta-rendszer, zárt testek (R14 háló → kontúr-extrudálás → Boole), mintavételes érintkezés
build_parts_v1.py        → parts_v1.json (igazság-forrás) + parts_v1.csv (gyors nézet, Excel-be nyitható ;-vel)
qa_parts_v1.py           → qa_report.md / qa_report.json, kilépési kód 2 ha BLOKKOLO
test_qa_v1.py            önteszt: szándékosan elrontott adaton (negatív/nulla méret, lista≠modell, duplikált ID, ütközés) blokkol-e
```

Futtatás (Python 3.11+): `pip install numpy trimesh shapely manifold3d rtree` → `python3 build_parts_v1.py && python3 qa_parts_v1.py && python3 test_qa_v1.py`. A `parts_v1.json`-t kézzel nem szerkesztjük.

Forrás: `execution/a902-s01-kyoto-ink-design-to-budget-20261026` ág, commit `2514579`, `CLAUDE_ATADAS/S16_MEDIAFAL_R14/` (data/ + 06_CAD_SEGITSEG). A main-en ez a mappa nincs, ezért a szükséges 5 JSON másolatként ide került.

## Az adatmodell alkatrészenként

| Mező | Tartalom |
|---|---|
| `id`, `cimke_id` | R14 ID; címke-ID = későbbi MPR fájlnév (`S16_D2-L`, ASCII) |
| `gyartasi_tipus`, `lap_alkatresz` | LAP / IVES_SZERELVENY / OSSZEALLITAS / BURKOLAT_RETEG / TEXTIL_BETET – az összeállítások (íves sapkák, 69 mm-es TV-távtartó) nem íródnak ki egy lapként |
| `helyi_rendszer` | A oldal felől nézve U jobbra, V fel, N az A oldal normálisa; nullpont = bal alsó sarok a B síkon; globális nullpont és tengelyek megadva |
| `lapoldal` | A = látszó/dekor-irányadó, B = szerelési oldal (front: szoba felé; külső véglap: kifelé) |
| `elek.E1–E4` | E1 alsó, E2 jobb, E3 felső, E4 bal (A felől); globális irány, hossz, **szerep geometriából** (CSATLAKOZO / SZABAD_ELOL / SZABAD_EGYEB a többi zárt testtel ±0,6 mm-en mért érintkezés alapján, szomszéd-ID-kkal), él-jel, élanyag, vastagság, gépi ütköző |
| `el_kod` | 4 jel E1-E2-E3-E4 sorrendben: V élzárt, F festett, L lakkozott, K kárpitozott, 0 nincs |
| `meret` | kész / élzárás előtti / nyers + a nyers szabálya; `geometriabol` = befoglalóból újraszámolt L/W/T |
| `szalirany` | R14 erezet → helyi tengely (U/V) és globális irány |
| `muveletek` | kontúrmarás, átmenő kivágás, kimetszés, fényfalcok helyi koordinátában; vasalat-műveletek **koordináta nélkül** (nincs kitalált furatkép), szerszám = null |

A 32 R14 jelenet-segédobjektum is be van sorolva (fényforrás-felület / LED-profil helyfoglaló / vásárolt készülék / **gyártandó takaró, ami hiányzik az anyagjegyzékből**).

## QA eredmény (2026-10-30)

**2 BLOKKOLO · 17 HIBA · 12 FIGYELMEZTETÉS · 41 INFO** – részletek: `qa_report.md`.

Blokkoló:
- **BG-1 és BG-FINISH: nyers magasság 2315 < kész 2405 mm.** Az R14 explicit `raw_W` egy korábbi háttérmagasságból maradt; ebből a szabásból a darab nem gyártható le. Ugyanaz a hibatípus, mint az S01 negatív mérete.

Hiba:
- **6 fiók: a fiókfenék egy síkban van az oldal alsó élével**, a Blum MOVENTO-hoz ≥ 12 mm (max. 15 mm mély) besüllyesztés kell ([Blum](https://ea.blum.com/en/building-a-movento-drawer/)). Az SKW = LW − 42 és az oldalhossz = NL − 10 egyezik.
- **BATTEN-1…5:** 8 mm vastag, de anyaga M01 (18 mm bútorlap) – anyag- vagy méretdöntés kell.
- **T-DOOR-L-BACK:** 12 mm, de M02 (18 mm festett MDF).
- **TV-FIELD 2630×1580, függőleges erezettel:** becsült 2800×2070-es táblából erezettel nem jön ki (90°-kal igen). **Tulajdonosi/látvány-döntés** (lásd lent).
- **BG-1 szabály-szöveg ↔ adat:** a szöveg kész L = 801 mm-t ír, az adat 811 mm; a BG-FINISH ugyanezt a BG-1-re írt szöveget örökölte.
- **BG-UPPER-/BG-LOWER-HIDDEN-RETURN:** az R14 layout „módosított fő alkatrésznek” nevezi őket, de sem a listában, sem a modellben nincs ilyen test (a 130/100 mm-es takart túlfutás).

Figyelmeztetés: 9 valós fénytakaró/tálca/baffle (TOP-WASH-*, UPLIGHT-*, DECK-*, LOW-INTERNAL-LIGHT-VISOR) csak segédobjektum, az anyagjegyzékből hiányzik; 3 nyers-szabály ellentmondás.

Rendben (bizonyított a tömör geometrián): 120/120 alkatrész lista ↔ R14 zárt jelenet ↔ `mesh_mm` befoglaló egyezik (≤ 0,05 mm); nincs negatív/nulla méret; nincs statikus ütközés (27 átfedő befoglalójú pár Boole-metszéssel); mind a 6 fiók 300 mm-es kihúzása ütközésmentes; minden szemben álló homlokzati rés 3,0 mm; mennyezeti rés 25 mm.

## Amit ez NEM bizonyít

Valós pánt/sín kinematika, ajtónyitás (pántoldal nincs rögzítve), kábelpálya, LED-profilok ütközése; termék-lapméret és élanyag (becslés); a műhely nullpont-, ütköző- és él-kód konvenciója; helyszíni méretek. Ezek a 2. fázis és az asztalos válaszának tárgyai.

## Nyitott kérdések

**Asztalosnak (a válasz a `gyartasi_szabalyok_v1.json`-ba kerül, utána újragenerálás):**
1. Az etalon él-kódjában (`V0VV`, `V000`, `A0VV`) mi a pozíciók sorrendje, és mit jelent az `A`?
2. Gépi nullpont és ütköztetett élek konvenciója (mi most E1+E4, A oldal felfelé).
3. Élanyag-vastagság és előmarás (mi 1 mm ABS + 1 mm előmarás élenként – becslés), festett MDF ráhagyás (+10/+10 az R14 szerint).
4. Minta `.mpr` + szerszámtábla (már kérve).

**Péternek (döntés):**
- TV-FIELD erezet: (a) marad a függőleges erezet → nagyobb formátumú furnér/lap vagy látható toldás kell; (b) vízszintes erezet → egy darabból kijön 2800×2070-es táblából. Ez a látványt érinti, ezért a te döntésed.

**Tervezői javítás (2. fázis elején, R15):** fiókfenék besüllyesztés, BG-1/BG-FINISH nyers méret + szöveg, BATTEN és T-DOOR-L-BACK anyag/vastagság, a hiányzó BG-visszafordulások és fénytakarók felvétele a listába.

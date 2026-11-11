# R16 eredeti ↔ R16J javított – eltérés-jelentés

Készült: 2026-10-30, Claude. Forrás: `forras_R16/` = git `execution/a902-s01-kyoto-ink-design-to-budget-20261026` @ `2514579`, `R16_feluletek_fiokok/data` (parts.json SHA-256 `c5e09f71…`, azonos a ChatGPT-audit forrás-hashével). Minden javítás gépi: `r16_forras_javitas.py` → `forras_R16J/javitasi_naplo.json`.

## 1. A ChatGPT-audit 12 méreteltérése (mind javítva, a befoglalóból)

Az R16 `parts.json` listázott x/y/t mezője hibás; az `assembly_box_mm` (az R16 natív STL-visszaolvasása szerint is helyes, max. 1,9e-6 mm) a forrás. 8 tételnél negatív méret (−222) állt, 4-nél 48 / 408 mm.

| ID | R16 listázott x×y×t | R16J kész L×W×T | javítás forrása |
|---|---|---|---|
| KI14-BAT-03 | 212 × 48 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-04 | 212 × 48 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-05 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-06 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-07 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-08 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-09 | 212 × 408 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-10 | 212 × 408 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-11 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI14-BAT-12 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI16-M6-BAT-06 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |
| KI16-M6-BAT-07 | 212 × -222 × 18 | 18 × 212 × 18 | assembly_box_mm (18×18×212 léc) |

## 2. Egyéb adat-javítások

| Tétel | Volt | Lett | Miért |
|---|---|---|---|
| KI12-TV01H-01 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV01H-01 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI12-TV02H1-01 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV02H1-01 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI12-TV02H2-01 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV02H2-01 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI12-TV02H2-02 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV02H2-02 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI12-TV02H2-03 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV02H2-03 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI12-TV02H2-04 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI12-TV02H2-04 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| KI16-M6-BACK-05 | material: M03 | M03-8 | ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból) |
| KI16-M6-BACK-05 | outline: befoglaló + notches.json (külön) | 8 pontos kontúr | notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa) |
| anyag:BEECH18 | materials.json: nincs definiálva az R16 materials.json-ban | 18×18 mm bükk léc (hátlaprögzítő) | R16 parts.json |
| anyag:M01 | materials.json: nincs definiálva az R16 materials.json-ban | 18 mm MDF, matt bronzbarna 2KPU festés (alsó frontok, összefüggő fedő) | R16 face_finishes.json / 00_OLVASD_EL: alsó front bronzbarna; kód az R12–R16 alkatrészlistából |
| anyag:M01+nyomat | materials.json: nincs definiálva az R16 materials.json-ban | 18 mm MDF, bronzbarna matt alap + tusgrafika nyomott/UV réteg (toronyajtók) | R16 materials.json M16-TOWER |
| anyag:M02 | materials.json: nincs definiálva az R16 materials.json-ban | 18 mm MDF hordozó + Vescom Bely+Print 1040.01 textilhatású burkolat (dekor panel) | R16 materials.json M16-WALL |
| anyag:M03 | materials.json: nincs definiálva az R16 materials.json-ban | 18 mm laminált bútorlap (korpusz belső) – dekor nyitott | R16 face_finishes.json: interior M03; R12 OLVASD_EL: tervezett 1 mm élzárás |
| anyag:M03-8 | materials.json: nincs definiálva az R16 materials.json-ban | 8 mm hátlap, M03 korpuszdekorban | R16 parts.json: TV01-H/TV02-H2 M03 kóddal, t = 8 mm |
| anyag:PLY18 | materials.json: nincs definiálva az R16 materials.json-ban | 18 mm rétegelt lemez merevítő keresztléc | R16 parts.json |

## 3. R16 MPR-tervezetek `??` kulcshibája

Az R16 mind a 111 `mpr_aktiv_tervezet/*.mpr` fájljában, összesen **956** furat-makróban `??="1"` sor áll (git grep, 2026-10-30) – ez nem woodWOP-paraméter; a fájlok így nem tekinthetők érvényes MPR-nek. Az R16J nem használja ezeket: a furatok a `holes.json`-ból jönnek, az MPR-t a S16 lánc (`f34_dokumentacio.py`) generálja tiszta kulcskészlettel. Az eredeti MPR-fájlokat nem másoltuk át.

## 4. Koordináta-átvezetés (nem méretváltozás)

R16 jobbkezes rajzi rendszer (Y=0 a korpusz front síkja, Y nő a fal felé) → S16 konvenció (Y a faltól a szoba felé): `Y_S16 = 418 − Y_R16`, X és Z változatlan. A 418 mm-es falsík FELTEVÉS (R16 M16-BRONZE: „frontY382; 18 mm szerelőtér a fal előtt”); csak eltolás, alakot/méretet nem változtat. Helyszíni felmérés nincs.

## 5. QA (R16-J-GY-v1)

F1: {'HIBA': 2, 'FIGYELMEZTETES': 12, 'INFO': 13} – BLOKKOLÓ: 0. A két HIBA valós, nyitott tétel:

- Q10: KI12-TV02CAP-01 összefüggő fedő 3600 (nyers 3610) mm – a becsült 2800×2070 táblából nem jön ki (toldás vagy hosszú tábla – döntés).
- Q18: a torony teteje Z = 2880, a névleges 2900-as mennyezetig 20 mm (S16 min. 25) – helyszíni felmérés kell.

F2b: 956 furat, 395 vasalat-tétel, problémák: {'FIGYELMEZTETES': 6} (a 6 figyelmeztetés a fiókonkénti nyitott MOVENTO/TIP-ON gyári sablonművelet).


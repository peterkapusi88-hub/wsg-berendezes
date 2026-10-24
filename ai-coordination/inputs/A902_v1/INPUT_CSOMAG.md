# A-902 – Astra kreatív inputcsomag v1 (2026-10-24)

**Státusz: KÉSZ ÁTADÁSRA (adatok) · NINCS ELINDÍTVA.** PR #1 inaktív marad; ehhez a csomaghoz még nincs PR. Indítás csak a Work-keret megléte és Péter „mehet"-je után, a `ROUTER.md` szerint.

Astra feladata a kreatív döntés. Ez a csomag **nem tartalmaz stílusjavaslatot** – csak azt, ami fix, amit mérni kell, amennyi pénz van, és ahol mozgástér van.

## 1. Kötelező olvasnivaló (ebben a sorrendben)
1. `GOAL.md` · 2. `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` · 3. `OPENAI_instructions.md`
4. Ebből a mappából: `GEOMETRIA_A902.md` (fix geometria, ellenőrizendő méretek), `KOLTSEG_KIINDULAS_A902.md` + `.csv` (keret-elosztás).

## 2. Képek – mi mire való
| Fájl | Mire használd | Mire NE |
|---|---|---|
| `04_renderek/semleges/A902_semleges_0_alaprajz_meretekkel.jpg` | alaprajz, helyiséghatárok, méretek | – |
| `04_renderek/semleges/A902_semleges_1_nappali.jpg` (Cam_02) | **geometria-alap** a nappali renderpromptjához (üres tér, valós falak/üvegek) | – |
| `04_renderek/semleges/A902_semleges_2_etkezo_konyha.jpg` (Cam_03) | geometria-alap étkező–konyha (konyhabútor szándékosan nincs: a lakásban sincs) | – |
| `04_renderek/semleges/A902_semleges_3_master.jpg` (Cam_04) | geometria-alap master | – |
| `04_renderek/semleges/A902_semleges_4_terasz.jpg` (Cam_05) | terasz, üvegfal kívülről | – |
| `02_referenciak/Z*.jpg`, `L*.jpg` | Péter korábbi két projektje (Zenit Residence, Lake Forest) – **a minőség és a „drágaság" szintje**, amit el kell érni | nem másolandó stílus; nem ez a két irány a cél |
| `04_renderek/alap/WSG_A902_r02–r04` | korábbi IKEA-alap bútorelrendezés (méretpróba) | nem esztétikai minta |
| `04_renderek/blender_stilusok/*`, `04_renderek/ai_gemini/*`, `04_renderek/ai_chatgpt/*` | eddigi Zenit/LF-kísérletek – megmutatják, mi működött és mi nem | nem döntés; a Blender-stílusrenderek étkezője **elavult** (2026-10-24-én ütközés miatt átépítve) |

## 3. Fix keretek (röviden – részletek a GEOMETRIA-fájlban)
- 2,90 m belmagasság (mérés függőben), padlótól nyíló üvegfalak: nappali 4,50 m (terasz), 05.3 1,80 m, master 3,65 m + 05.2 erkélyajtó 1,88 m; szürke tölgy parketta, fehér fal, fekete nyílászárók – maradnak.
- Nincs építés: bútor, panel/lamella/tapéta, asztalos tömeg, LED – igen; bontás, gipszkarton, burkolás, áthelyezés – nem. Mennyezet: fúrás csak a fűtő-hűtő panelek közé.
- Kamerák rögzítve (Cam_02–05): minden stílus ugyanebből a nézetből készüljön, hogy összevethető legyen.
- Funkció nem áldozható: minden hálóban gardrób, konyhában magasszekrény-sor, mosó-szárító helye kell, előtérben cipős + pad + tükör.

## 4. Mért funkcionális korlátok (Geometry Validator, `03_blender/validator_report_2026-10-24.md`)
- Ajtók előtt 90 cm szabad sáv kell – **a 05.2 hálóban 160-as ágy két éjjelivel ezt nem engedi** (opció: 140-es ágy vagy fali olvasólámpa + lebegő polc).
- Étkező: a 2,7 m-es sávban kerek asztal + 6 szék nem fér el a 05.3 ajtó és az akna miatt; működő minta: **160×90 asztal, pad az északi oldalon, 3 szék délen**.
- Konyha: a két pultsor között a modellben **~0,89 m** marad (szűk; 1,0–1,2 m a kényelmes) → a sziget nem fér, a nyugati pultsor mélysége/hossza tervezési kérdés.
- Átjáró (előtér → nappali, x 7,40–8,45): a nappali bútorai nem zárhatják el.

## 5. Ahol a „drágának ható" hatás születhet (lehetőségek, nem javaslatok)
- **Nappali fő fala** az akna/WC-blokk felőli oldalon (x 5,45–7,40, y = 4,04) – a nappali legnagyobb zárt fala, a terasz felé néző ülésirány háttere.
- **4,50 m-es üvegfal a terasz felé** – panoráma keretezése, nappali–terasz folytonosság (anyag, fény, ülés iránya).
- **Belépési élmény**: előtér 2,90 × 1,95 + átjáró – az első 3 másodperc.
- **Master ágyfal** (keleti fal, x ≈ 3,56–3,62) és az **északi nyúlvány** (2,95 × 0,98) – fülke, öltöző vagy olvasósarok lehetősége.
- **Konyha mint bútor**: nyitott a nappali felé, magasszekrény-sor a keleti falon – tömeg, front, fény.
- **Terasz**: jakuzzi-előkészítés, lounge, étkező, növény – a penthouse fő értékpontja.
- **Fény**: 2,90 m belmagasság, rétegzett Hue + rejtett LED.

## 6. Nyitott döntések (Péteré – Astra opciókat ad, nem dönt)
05.3 funkciója (háló vs dolgozó) · jakuzzi szintje (Heissner vs Correll) · 05.2 ágyméret · tapétázó beengedése · külső tervező bevonása · stílusok száma és sorrendje.

# A-902 fürdő 06.2 – r1b, 10 kép (Cam_10), ChatGPT Images – 2026-10-25

**Minden kép: KONCEPCIÓ – NEM VALIDÁLT.** A DC2026-versenynek nem része. A kérés: `ai-coordination/requests/WSG-20261025-A902-FURDO-R1B-IMAGES.md`.

## Futás
- **Forrás:** `wsg/a902-furdo-r1b-20261025` @ `252d924308b55a29284ddfc6345c85378a69daf4`. A promptok szó szerint a `05_promptok/A902_furdo_r1b_20261025/promptok/`-ból; mind a 10 BEGIN–END blokk bájtra egyezik a forrással.
- **Fejléc:** a 60-as futás Cam_10-fejléce (`renders/opus55-v3-1-60-tests`, `uzenetek/06_…Cam_10_A.txt`), a kérés 3. pontjának két módosításával:
  - **2. f) pont – új:** a pult, az üveg és a mosdó helye a képen százalékban; az üveg 200 cm-es.
  - **3. pont – kiegészítés:** egy kivétel, amely engedi az üveget, a lebegő pultot és a fali oszlopot.
  - Az elküldött üzenetek: `uzenetek/`, sha256-tal a naplóban.
- **Csatolmányok** minden képnél ebben a sorrendben:
  1. Blender `A902_Alap-v2b1_blender_10_furdo-06-2.png` (sha256 `25c818fd…`);
  2. ME-BAL-064 (`6e577ef4…`);
  3. ME-BAL-066 (`6b50e8a5…`).
- **Modell:** ChatGPT Images, „Kép létrehozása” eszköz. Csevegőmodell: GPT-6 (gondolkodás: High). A képmodell külön neve a felületen nem látszik.
- **Menet:** egy fiók, saját lap, képenként új beszélgetés, képenként pontosan 1 kép. 16:28–16:49. Újrapróba nem kellett; limit és CAPTCHA nem volt.
- **Sorrend:** előbb az S01. A kapukép alapján az üveg, a pult, a süllyesztett mosdó és a geometria rendben volt (Péter 16:32-kor szintén elfogadta), utána ment le az S02–S10.

## Eredmény: 10/10 DONE · 0 FAILED · 0 BLOCKED · 0 SKIPPED_LIMIT
Fájlok: `<kep_id>__FURDO_R1B__v1.png`, eredeti 1586 × 992-es PNG, nem újratömörítve. Kapuképek: `_gate/`. Kontaktlap: `A902_FURDO_R1B_kontaktlap.jpg`.

### Képenkénti ellenőrzés
Jelölés: ✓ = rendben, ~ = részben vagy kis eltéréssel, ✗ = hiba.

| # | Stílus | Burkolat / dekor | Mosdó a helyén, pultba ülve, bal rés | Pult üvegtől aknáig, alatta padló | 1 fix üveg, ajtó nélkül | Oszlop jobb sarok / dugaljak | Ablak nincs | LED folytonos | Stílustárgy | Geometria |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | S01 Kyoto Ink | ✓ | ✓ (a front nem színel) | ✓ | ✓ (fekete profil a szabad élen is) | ✓ / **nem látszanak** | ✓ | ✓ | teakzsámoly, ikebana | PASS – feltételes |
| 02 | S02 BiBo Nocturne | ✓ | ✓ | ✓ | ✓ | ✓ / **nem látszanak** | ✓ | ✓ | hold-váza, karaffa | PASS – feltételes |
| 03 | S03 Alelí Casa | **~ a dekor kavicsmintás lett** | ✓ | ✓ | ✓ | ✓ / ✓ szabad | ✓ | ✓ | terrakotta korsó | PASS – feltételes |
| 04 | S04 LA Horizon | ✓ | ✓ | ✓ | ✓ | ✓ / ✓ szabad | ✓ | ✓ | borostyán váza, bronz | PASS – feltételes |
| 05 | S05 Miami Streamline | ✓ | ✓ (lekerekített vég) | ✓ | ✓ bordázott (magasság nem látszik) | ✓ / ✓ szabad | ✓ | ✓ | kagylótál | PASS – feltételes |
| 06 | S06 Zenit Atelier | ✓ | **✗ a mosdó 2–3 cm-rel kiemelkedik, a szifon a front előtt** | ✓ | ✓ szürke | ~ (a pultra ül) / ✓ | ✓ | ✓ | fekete váza | PASS – feltételes (mosdóhiba) |
| 07 | S07 Lake Forest Couture | **~ a dekor hullámos lett** | ~ (a perem kissé magas) | ✓ | ✓ | ✓ / ✓ szabad | ✓ | ✓ | orchidea | PASS – feltételes |
| 08 | S08 Milano Radical | ✓ | ~ (a perem kissé magas) | ✓ | ✓ | ✓ / ✓ szabad | ✓ | ✓ | csíkos váza | PASS – feltételes |
| 09 | S09 Paris Collector | ✓ | ✓ | ~ (a bal vége az üvegvonalba ér) | ✓ atelier-rács | ✓ / ✓ szabad | ✓ | ✓ | sárgaréz tálca, páfrány | PASS – feltételes |
| 10 | S10 Desert Modern 70 | ✓ | **~ U-fiók nincs, a szifon látszik** | ~ (a bal vége az üvegvonalba ér) | ✓ bronz | ✓ / ✓ szabad | ✓ | ✓ | terrakotta korsó | PASS – feltételes |

**Mind a 10 képen közös eltérés:** a távoli fal jobb sarka kb. 5–8 %-kal jobbra csúszik (~70 % → ~77–78 %), vagyis a fal szélesebbnek látszik, hogy elférjen a pult és az oszlop. Ami a lockon maradt: a zuhanyfal, a fejzuhany, a keverők, a padka és az akna-diagonál. A 60-as futás Cam_10-képei pontosabban fedtek; ott a fal nem kapott új bútort.

### Legerősebb képek
1. **S04 LA Horizon** – a mosdó pontosan a helyén van és egy síkban ül a pulttal, a dugaljak látszanak és szabadok, a dekorfal hiteles.
2. **S09 Paris Collector** – a legerősebb luxushatás; egy pontosítás kell: a pult bal végén maradjon meg a 4 cm-es hézag.
3. **S02 BiBo Nocturne** és **S01 Kyoto Ink** – technikailag tiszták, de a dugaljak nem látszanak rajtuk.

### Hibás vagy javítandó képek
- **06:** a mosdó félig ráültetett hatású, és a szifon látszik.
- **10:** a szifon látszik, U-fiók nincs.
- **03, 07:** a dekorcsempe mintája eltér.
- **01, 02:** a dugaljak hiányoznak a képről (a valóságban ott vannak).
- **09, 10:** a pult bal vége az üvegvonalba ér.

Újragenerálni csak akkor érdemes, ha a stílus döntős lesz. A szabály szerint egy képre legfeljebb 1× `__v2`, és a fejléc-változtatást naplózni kell.

## Műszaki megjegyzés a rejtett fényekhez
Forrás: villamos kiállások, `01_alaprajzok/villamos_kiallasok/A902_villamos.csv`.
- **Betáplálás új kiállás nélkül:**
  - a rejtett 24 V-os fények az **FL04** pontról („g” kör, ~2,00 m, a mosdó fölött; saját kapcsoló: K24);
  - a spotsín az **ML10** pontról („f” kör);
  - a **D43/D44** dugaljak szabadok maradnak.
- **Feltételek:**
  - a tükör (3 cm-es távtartón) takarja el az FL04 dobozt, különben a vezeték 15–20 cm-en látszik;
  - a táp a pultban hozzáférhető helyen legyen; csak SELV szalag kerüljön be, IP65-ös;
  - a vízóra revíziós ajtaja a mosdótól jobbra lent van, ezért a fiókblokkba szervizkivágás kell;
  - a fürdőzóna-besorolást (MSZ HD 60364-7-701) villanyszerelőnek kell igazolnia;
  - minden méret a hétfői (2026-10-26) helyszíni méréssel véglegesítendő.

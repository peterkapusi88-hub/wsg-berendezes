# Opus 5.5 V3.1 – integrátori szövegcsere v1.1 (K-02, K-03) – **TERVEZET, b24bee7-alapú, NEM FUTTATHATÓ**

> **Elavult forrás.** Ez a változat a `b24bee7` (CP10) állapotra készült, mielőtt a végső `7d3c67f` elérhető lett. Az S02 két fájlja a végleges forrásban eltér (ML04: Kave Home Idela, ML05: Westwing Dancing). Az itteni S02 fájlok a régi lámpákat (Brisia, sárgaréz-opál) tartalmazzák, ezért **nem vehetők át**. Az S01 két fájlja bájtra azonos a v1.2-vel. **Érvényes változat:** `../KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_2_7d3c67f/`. Ez a mappa csak verziózott tervezetként marad meg.

**Claude integrátor, 2026-10-25.** A versenyzői fájlok (PR #22 ága) változatlanok; ezek javított másolatok. Képet nem generáltam.

## Mit cserél
| Kép | Lelet | Csere |
|---|---|---|
| S01 Cam_02, S02 Cam_02 | **K-02** – az ML04 a Cam_02 képkeretén kívül van (56,6° a tengelytől, fél látószög 42°) | Az „ML04 a jobb szélen világít” mondat helyett: *„The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; at most a faint warm spill of its light reaches the right edge of the floor and the table.”* A tiltólistába: *„a pendant lamp drawn at the right edge or anywhere above the dining table”* |
| S01 Cam_12, S02 Cam_12 | **K-03** – a W02 melletti növény/olajfa a hálók felé vezető fő utat 0,70 m-re szűkíti (S01), illetve elzárja (S02), és a W02-mű elé áll | A növény-/olajfa-mondat törlése. A tiltólistába: *„a plant, tree or any object standing in front of W02 or in the mouth of the bedroom corridor”* |

Más szöveg nem változott (soronkénti diff: két csere fájlonként).

## Verziók
| Kép | Alap (b24bee7) sha256 | Javított `_v1_1` sha256 | Karakter |
|---|---|---|---|
| `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A` | `914f0b9e…` | `95a34f6998b5fec723f7d1f275f3ce959c970c59807bfc8ce08d328494e9bfa1` | 5629 → 5601 |
| `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | `7096e13f…` | `68f66d63581ff31e18fd0ee267eb8fcde2a942410473dabea812f1a691846651` | 6168 → 6299 |
| `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A` | `5085ab2c…` | `0e103d813ae481df1a5e2aaa9fde240e92271e248f144b20a80011f0b8e12689` | 5221 → 5224 |
| `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | `dfd6ecf0…` | `b24fcdcaced164455ba672596259214cd3bd207637c90a92523f1da361e12df6` | 5767 → 5885 |

Napló: `patch_v1_1_naplo.json`.

## Újraalkalmazás a 7d3c67f-re (a lehúzás után)
```
python3 -I apply_patch_v1_1.py <a 7d3c67f 05_promptok/KEP004_OPUS55_V3_1_r1/20_PROMPTOK mappája> <kimeneti mappa>
```
- `alap=b24bee7` → a négy prompt a végső commitban nem változott, a fenti v1.1 érvényes.
- `ALAP ELTÉR` → a csere lefutott, de a prompt tartalma más; új audit és új sha kell.
- `HIBA … 0×` → a mondat a 7d3c67f-ben már más, vagy eltűnt; a cserét kézzel kell egyeztetni.

## Nem része (nyitva marad)
- **K-01:** a 7d3c67f egyezése – amíg nincs meg, a csomag nem indítható.
- **K-06:** az S02 fekete Toni 160 × 90 igazolása (a 3. és 4. kép feltétele).
- **K-03 a többi helyen:** az S04 Cam_12 olajfája, valamint a S01/S02 stílusspecifikáció növénysorai – ezek nem a négy induló prompt részei.
- **Új, K-21 (alacsony):** mindkét S02 prompt „brushed-brass rod”-ot ír a Brisiához; a rögzített termékadat szerint szálcsiszolt sárgaréz rozetta és fekete, állítható drót tartja (L00152CR05). A Cam_02-ből a v1.1 kivette a mondatot; a Cam_12-ben még benne van.

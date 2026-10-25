# A-902 Cam_02 – szürke bútortömbös elrendezés-referencia (v1, 2026-10-25)

**Mi ez:** a KEP-004 Cam_02-promptok 1b képe – Péter 2026-10-25 01:23-kor engedélyezte. Megmutatja, **hol állnak** a bútorok az elfogadott P902_24A elrendezésben. Nem stílus-, szín- vagy anyagreferencia.

| Fájl | Tartalom |
|---|---|
| `A902_Cam02_tomeg_P902_24A_v1.png` | Cam_02, 1600 × 1000. Az 1. alapképpel azonos beállítás. Rajta: U-kanapé-zóna 3,00 × 2,40, TV-konzol 1,80 × 0,45 + 65"-os képernyő a nyugati falon, a terv 80 × 180-as asztala 0,30 m-rel nyugatra, 3 + 3 székkel |
| `A902_Cam02_tomeg_P902_24A_felulnezet_v1.png` | felülnézeti ellenőrző kép (mennyezet nélkül) |

- **Modell:** v2b-1-k11b (`main`), sha256 `9875cd57…`. A .blend nem változott; a szkript csak renderel, nem ment.
- **Szkript és vetített képtéri helyek:** `03_blender/geometry_v2/tomeg_cam02/`.
- **Egyezés az 1. alapképpel:** a tömbök nélküli ellenőrző render a v1-csomag 01-es alapképétől átlagosan 0,008/255, legfeljebb 1/255 eltérést mutat. A beállítás tehát azonos.

**Felhasználás:** a geometriai blokkal együtt (`05_promptok/KEP004_ChatGPT_Images_v2_geometria/Cam02_GEOMETRIA_v2.md`), csak az Astra V3-mal egyesített, Péter által jóváhagyott promptban.

## V3 tömbképek (2026-10-25, Astra Creative Upgrade V3 r1 befoglalói)
| Fájl | Tartalom | sha256 |
|---|---|---|
| `A902_Cam02_tomeg_S01_V3_v1.png` | S01: KI3-V torony, KI3-P két sík, KI3-L, TV, Lennon jobbos L (hát x 7,17), Toni 200×90 + 6 Eamy | `2629cb2d…f9c4` |
| `A902_Cam02_tomeg_S02_V3_v1.png` | S02: BN3-V (ajtós + tükörmező), BN3-P, BN3-L, TV, JÄTTEBO U 285×160, Anouk 180×90 + 6 Ciselia | `a37ead52…0036` |

- Renderelve a v2b-1-k12 javaslati fájlból (`blender_cam12_v1/03_ellenorzes_tomegek.py`). A Cam_02 és minden geometria azonos a main v2b-1-k11b fájljával, csak a Cam_12 kamera többlet.
- Validátor: mindkettő **PASS 0 hiba / 8 figyelmeztetés** – a TV-blokk és a D18 dugalj a szekrények mögött van. Részletek: `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md` (2. pont).
- Képtéri befoglalók és távolságok: `A902_Cam02_tomeg_V3_kepteri_v1.json`.
- Felhasználás: 1b képként a V3 próbakép-promptokban (`05_promptok/KEP004_ChatGPT_Images_V3_teszt/`).


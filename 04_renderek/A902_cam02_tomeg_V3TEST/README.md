# A-902 Cam_02 – javított V3-tömbképek a V3_TEST-hez (v1, 2026-10-25)

**Mi ez:** az 1b kép a két `_V3_TEST` promptban. Szürke tömbökkel mutatja, hol állnak az Astra V3 r1 bútorai az elfogadott P902_24A elrendezésben.
- Nem stílus-, szín- vagy anyagreferencia.
- Péter (02:22) ezt a két javított tömbképet és a PASS validátort jelölte meg kiindulásnak.

| Fájl | Tartalom | sha256 |
|---|---|---|
| `A902_Cam02_tomeg_S01_V3TEST_v1.png` | S01: KI3-V torony, KI3-P egy befoglaló (260×190, z 0,55–2,45), KI3-L 240×48, TV 65″, Lennon jobbos L (hát x 7,17), Toni 200×90 + 6 Eamy | `ed70d29e…` |
| `A902_Cam02_tomeg_S02_V3TEST_v1.png` | S02: BN3-V (ajtós oszlop + **világos tükörmező a TV-panel felől**, alatta sötét szervizlap), BN3-P, BN3-L 240×50, TV, JÄTTEBO U 285×160, Anouk 180×90 + 6 Ciselia | `b78dd073…` |
| `A902_Cam02_tomeg_S0x_V3TEST_felulnezet_v1.png` | felülnézeti ellenőrző kép | `41d45eb9…` / `f9d42a73…` |

**Eltérés a korábbi V3-tömbképektől** (`../A902_cam02_tomeg_v1/A902_Cam02_tomeg_S0x_V3_v1.png`, a másik munkamenet r1-csomagja):
1. **S01:** a KI3-P két síkjának osztása a régi képen a TV közepe mögé esett. Itt egy befoglaló szerepel; az osztás helyét a stílusblokk adja.
2. **S02:** a tükörmező a TV-panel felőli oszlopba került, alatta zárt szervizlappal. A D18 dugalj (y 4,749; z 0,30) így a szervizlap mögül érhető el.
3. A tükör tónusát (0,45) úgy választottam, hogy elváljon a faltól. Az első renderben (0,62) beleolvadt; az a `_munka/…/kepek_r1` mappában maradt a Macen.

**Készítés:**
- Szkript: `03_blender/geometry_v2/tomeg_cam02_v3test/01_tomeg_cam02_v3test.py` (+ `tomeg_lib.py`, `futtat.sh`).
- Blender 5.2.3, a v2b-1-k11b `main`-másolatán. A .blend nem mentődött: sha256 előtte és utána `9875cd57…`. Az élő Blender-jelenethez nem nyúlt.
- A kamera azonos az 1. alapképével: Cam_02, 20 mm, 1600 × 1000. A tömbök nélküli ellenőrző render az alapképtől átlagosan 0,008/255-tel, legfeljebb 1/255-tel tér el (újramérve 2026-10-25), vagyis a beállítás azonos.
- Validátor: üres PASS 0/0 · S01 PASS 0/8 · S02 PASS 0/9. Riport: `03_blender/validator_report_2026-10-25_V3TEST_tomeg_cam02.md`.
- Képtéri befoglalók, vetített pontok, távolságok: `tomeg_cam02_V3TEST_log_v1.json`.

**Felhasználás:** `05_promptok/KEP004_ChatGPT_Images_V3_TEST/` (1b kép), és a Gate vetítése (`_eszkozok/gate_atfedes.py`).

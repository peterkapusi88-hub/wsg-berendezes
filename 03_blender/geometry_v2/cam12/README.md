# Cam_12_Nappali_Hero – vizsgálat és rögzítés (2026-10-25, Claude)

| Fájl | Mit csinál |
|---|---|
| `tomeg_lib.py` | Közös segédfüggvények: render-alapbeállítás (azonos a v1 alapképekkel), dobozok, generikus P902_24A tömb, vetítés |
| `stilus_tomeg_v3.py` | Astra V3 r1 (PR #16, `be6b1f3`) S01/S02 befoglalói szürke tömbként |
| `01_sarok_jeloltek.py` + `futtat1.sh` | K1 ÉNy-i sarok, K2 ÉNy beljebb, K3 DNy-i sarok (20/22/24 mm): üres, S01, S02 render; célpontok vetítése; **falszakasz-láthatóság ray casttal** (csak építészet / + stílustömb). Napló: `cam12v2_jeloltek_log.json` |
| `02_finomitas.py` + `futtat2.sh` | R1 (20 mm), **R2 (22 mm, választott)**, R3 (1,35 m). Napló: `finomitas_log.json` |
| `03_cam12_rogzites_v2.py` + `futtat3.sh` | A Cam_12 hozzáadása a main v2b-1-k11b fájljához (sha256 `9875cd57`), mentés új fájlba (k12 v2) |
| `04_ellenorzes_v2.py` | Validátor 5 módban; Cam_12 alapkép és tömbrenderek; képtéri befoglalók, célpontok, láthatóság. Napló: `cam12v2_ellenorzes_log.json` |
| `futtat3_sha.txt` | a k12 v2 .blend és a lock sha256-ja |
| `v1_H1_tengelyes_elvetve/` | a 01:39-es tengelyes jelölt (H1, x 4,25, kelet felé) szkriptjei és naplói – Péter 01:58-as kérése után elvetve |

- Minden szkript a Mac élő Blenderéből indított háttérfolyamatban fut (`Blender -b <forrás.blend> --python …`). Az élő, nem mentett fájlt nem írja.
- A `04_ellenorzes_v2.py` a `01_sarok_jeloltek.py` célpont- és falszakasz-definícióit tölti be, így a jelöltek és a választott kamera mérése azonos.

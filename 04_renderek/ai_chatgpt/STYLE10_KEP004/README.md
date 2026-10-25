# STYLE10 · KEP-004 – ChatGPT Images archívum, A-902 (v1, 2026-10-24 23:30)

**Állapot (2026-10-25 01:20):** 1 kép – `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A.png`, az első automatizált futás (Claude in Chrome, Péter „mehet”, 01:01).
- Gate: FAIL / ÚJRATERVEZÉS (geometria és elrendezés), `KONCEPCIÓ – NEM VALIDÁLT`.
- Audit: `ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md`; bizonyítékképek: `_gate_r1/`.
- Minden további lépéshez Péter „mehet”-je kell.

**Állapot (2026-10-25 02:40):** +2 V3 próbakép a `CREATIVE_UPGRADE_V3/` almappában (S01 Kyoto Ink, S02 BiBo Nocturne, Cam_02; Péter „mehet”, 02:06; képenként egy generálás).
- Elrendezés megfelel; geometria FAIL (a terasz felőli padlósík 10–13,5 %); `KONCEPCIÓ – NEM VALIDÁLT`.
- Audit: `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md`; bizonyítékok: `_gate_v3teszt/`; manifest: `archiv_manifest_v3teszt.json`.

**Állapot (2026-10-25, 02:39 CEST):** +2 kép a `V3_TEST/` almappában. Ez **Péter 02:22-es döntése szerinti tesztpár**: S01 és S02 Cam_02, r2-csomag, javított 1b tömbkép; Péter „mehet” 01:55 és 02:22; képenként egy generálás. A fenti két `_V3_r1` kép A/B-referencia.
- **S02:** a héj ±1 %-on belül – ez eddig a legpontosabb kép. A tükör fizikailag lehetséges belső teret mutat. Gate: `ELŐSZŰRT – FELTÉTELES`.
- **S01:** a belmagasság ~+8 %, ezért geometriai kontrollként FAIL (javítható).
- **Mindkettő:** a falbútorok magasabbak, az étkező keletebbre került. `KONCEPCIÓ – NEM VALIDÁLT`.
- Audit: `ai-coordination/results/WSG-20261025-KEP-004_V3_TEST_gate.md`; bizonyítékok: `V3_TEST/_gate_V3TEST/`; manifest: `V3_TEST/archiv_manifest_V3_TEST.json`.

**Mi kerül ide** (lépésenként egy commit):
- a KEP-004 ChatGPT-ben (normál chat, nem Work) generált képei, kanonikus néven: `<kép-ID>.png`, ismétlésnél `<kép-ID>_v2.png`;
- mellettük a futtatott prompt: `<kép-ID>.prompt.txt`;
- `archiv_manifest_<forduló>.json`: sha256, átvételi fájlnév, időpont;
- `ATVETELI_NAPLO.csv`: a Mac átvételi naplójának repó-másolata (chat-link, képmodell, időpont, újragenerálás, Gate). Claude vezeti.

**Kép-ID** = Astra V2 „Output” sora, pl. `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A`.

**Státusz:** minden kép `KONCEPCIÓ – NEM VALIDÁLT`, amíg a Gate-audit (Render Reality Gate) le nem futott. Az audit helye: `ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md` (1a–1c), majd `_r2a.md`, `_r2b.md`.

**Útvonal:**
1. Mac: `~/Downloads/WSG/KEP-004/04_chatgpt_images_atvetel/<forduló>/<NN_kép-ID>/` – Péter ide teszi a letöltött képet, átnevezés nélkül.
2. Claude lefuttatja: `archivalas_elokeszito.py` (csak másol, nem töröl, nem ír felül).
3. Az előkészített fájlok: `_github_elokeszites/04_renderek/ai_chatgpt/STYLE10_KEP004/`.
4. Commit ide.

**Források:**
- promptok: `05_promptok/KEP004_ChatGPT_Images_v1/`;
- végrehajtási terv: `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004_CHATGPT_IMAGES_v1.md`.

A képcsomagok (csatolandó képek) csak a Macen vannak, a Kave/IKEA/Westwing termékképek miatt nem kerülnek a repóba.

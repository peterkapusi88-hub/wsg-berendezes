# Validator-riport: A-902 semleges geometria-alap v2, Cam_02 (2026-10-24 07:29)

- **Bemenet:** `03_blender/WSG_A902_v2_terasz_ELOZETES_20261024.blend` **másolata**, a felhős munkaterületen.
  - Az élő `~/Downloads/WSG_A902_stilusok.blend`-hez és a repóbeli v2-fájlhoz nem nyúltam; a módosított másolatot nem mentettem.
- **Szkript:** `03_blender/geometry_v2/render_semleges_v2_cam02.py` (bpy 5.2.3). A validátort (`geometry_validator.py`, lock: `geometry_lock_A902.json`) a módosítás után, a render előtt futtatja.
- **Eredmény:** `0 hiba, 0 figyelmeztetés`.
  - LOCK: falak 54, nyílások 52, padlók 19, kamerák 6 – a helyükön.
  - BURKOLÓ/ÜTKÖZÉS: 0 látható bútor (szándékosan üres).
  - AJTÓ-ELŐTÉR: minden ajtólap két oldalon szabad.

**Mit változtat a szkript (csak megjelenés, geometria nem):**
- Rejtve: `A902_Butor`, `Stil_LakeForest`, `Stil_Zenit`, a régi `A902_Terasz`, a narancs JELÖLŐ-k, a belső lámpák és a „Nap”.
  - A nap iránya a modellben nem igazolt, ezért a kép csak égbolt-szórt fényt használ.
- Nyílászáró-profilok **belül fehérek** (IGAZOLT-F). Beltéri ajtólap világosszürke, tok szürke.
- Fal és mennyezet semleges fehér.
- A padló tónusa a ME-BAL-080 fotóhoz hangolt, szürkésbarna. **Deszkaminta nincs modellezve.**
- Render: Cycles CPU, 64 minta, denoise, AgX, expozíció +1,3, 1600×1000.

**Két próbarender (07:28, 07:40) – mindkettő FAIL, egyik sem került a repóba.** A második javította a falszínt és a JELÖLŐ-ket, de az égbolt-textúra napkorongja továbbra is irányított fényt adott:
- bézsnek látszó fal;
- homokszínű padló;
- látható JELÖLŐ-k;
- befelé tűző, nem igazolt irányú napfény.

**Következő lépés (Péter döntése után):** egyenletes, semleges háttérfény napkorong nélkül, majd újrarender és vizuális ellenőrzés a ME-BAL-045/-080 fotókhoz.

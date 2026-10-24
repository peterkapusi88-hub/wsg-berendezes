# Validator-riport: A-902 terasz v2 (ELŐZETES), 2026-10-24 06:00

- **Ellenőrzött fájlok** (a `geometry_validator.py` változatlan, a lock a `geometry_lock_A902.json` v1):
  1. `WSG_A902_stilusok_MEMORIA_20261024_0544.blend`: az élő Blender nem mentett állapotáról készült biztonsági másolat (`~/Downloads/WSG_blender_mentesek/`).
  2. `WSG_A902_v2_terasz_ELOZETES_20261024.blend`: az 1. pontból épített új fájl (`~/Downloads/` és `03_blender/`).
- **Élő fájl** (`~/Downloads/WSG_A902_stilusok.blend`): nem nyúltunk hozzá. A futó Blender-munkamenetben nem mentett változás van (`is_dirty = True`). Ezt sem mentettük rá, csak a fenti másolat készült róla.
- A v2 Blender 5.2.3-ban készült, a Mac verziójával azonos konténeres `bpy`-modullal. Az élő munkamenetet nem érintette.

| Ellenőrzés | MEMÓRIA-mentés | v2 terasz | Megjegyzés |
|---|---|---|---|
| LOCK falak / nyílások / padlók / kamerák | 54 / 52 / 19 / 6 OK | 54 / 52 / 19 / 6 OK | belső geometria érintetlen |
| BURKOLÓ / ÜTKÖZÉS | 247 látható bútor OK | 195 látható bútor OK | 52 régi teraszbútor elrejtve (nem törölve) |
| AJTÓ-előtér | 9 hiba | 9 hiba | **ugyanazok a régi belső hibák** (05.1 éjjeliszekrény, 05.2 ágy, 05.3 PAX, cipős a WC-ajtónál); a v2 nem hozott újat |
| TÁVOLSÁG | kanapé–dohányzóasztal 67 cm | ua. | LF-réteg, régi |
| KÖZLEKEDŐ | átjáró (x 7,40–8,45) vonalában LF TV-fal és étkezőasztal | ua. | LF-réteg, régi |

**A v2-ben változott (gyűjtemény: `A902_Terasz_v2_ELOZETES`, 41 objektum; validátor újrafuttatva 06:10, ugyanaz a 9 + 2 régi tétel):**
- greslap T09/T10 a −0,15 szinten;
- WPC-dobogó: középső sáv, harántsáv, északi nyelv és pihenő a +0,47 szinten;
- 2 × 3 fokos lépcső;
- zöldtető +0,77-en (ELŐZETES): sík fű Ny és K, középen domb (+0,25) évelőkkel és virágokkal, mulcs- és kavicságyás (Péter megfigyelése + 2. videó), betonszegéllyel, öntözőszelep-akna JELÖLŐ;
- antracit pálcás korlát (1,10 m, ELŐZETES) és mellvéd;
- narancs JELÖLŐ: jakuzzi-előkészítés 2×2 m (mélysége HIÁNYZIK), áramkiállás, fagymentes csap;
- 3 új kamera: Cam_07 a greslapról, Cam_08 madártávlat, Cam_09 felülnézet.

**Elrejtve, nem törölve:** a régi `A902_Terasz` gyűjtemény (üvegkorlát, kitalált fák és bokrok, jakuzzi-tárgy, napozóágyak), a régi T_09–T_12 padlók és a teraszra tett stílus- és alapbútorok. Ezek a brosúra alapján készültek, és sík teraszt feltételeztek.

**Nincs modellezve, szándékosan:**
- a videón látható járósáv a korlát mentén (nincs a terven, HIÁNYZIK);
- a belső falak legfeljebb 15 cm-es eltérései (lásd `geometry_v2/A902_eltereslista_v1_v2.md`). Ezeket csak hétfői mérés után vezetjük át.

**Státusz:** a geometria ELŐZETES (tervdokumentum és videó). A renderek **geometria-ellenőrző nézetek**, nem stílusképek.

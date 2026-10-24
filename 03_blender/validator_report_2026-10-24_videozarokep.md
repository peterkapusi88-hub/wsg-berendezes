# Geometry Validator – 2026-10-24 05:15, videó-záróképkocka előtt (A-902, Stil_LakeForest)

**Futtatás:** `03_blender/geometry_validator.py` az élő Blender-jeleneten (`/Users/peterkapusi/Downloads/WSG_A902_stilusok.blend`, `WSG_A902` jelenet). Lock: `03_blender/geometry_lock_A902.json`. Csak olvasás, a jelenet nem módosult.

**A jelenet állapota a futtatáskor:** a fájl **nem mentett változásokat tartalmaz** (`is_dirty = True`, utolsó mentés kb. 2,6 órával korábban, ~02:30). Ezeket **nem mentettem el és nem írtam felül**. A renderhez ideiglenes kamerák kellettek; ezeket a render után töröltem, és visszaállítottam az eredeti `scene.camera` (Cam_04_Master) és `render.filepath` értéket.

## Eredmény (aktív réteg: Stil_LakeForest)

| Ellenőrzés | Eredmény |
|---|---|
| LOCK falak / nyílászárók / padlók / kamerák | ✅ 54 / 52 / 19 / 6, 0 eltérés |
| Burkoló, ütközés | ✅ 247 látható bútor |
| Ajtó-előtér | ❌ 9 elem: a már ismert, nyitott hibák (05.1 éjjeli, 05.2 ágy és éjjeli, előtéri cipős, 05.3 PAX). **A nappaliban nincs.** |
| Kanapé–dohányzóasztal | ⚠ 67 cm (cél 45–50) |
| Kanapé–TV-fal közlekedő | ✅ 90 cm |
| **ÚJ figyelmeztetés** | ⚠ KÖZLEKEDŐ: az átjáró vonalában (x 7,40–8,45) áll az `L_TVfal_travertin`, a `L_TVfal_bronzkeret_b/top`, az `L_fuggonysin` és az `L_etkezo_lap/lab0`. A TV-fal x 5,45–7,40 között van, így a 7,40-es élnél csak érinti a sávot. Mérési szélhatás, nem tényleges akadály – Codexnek ellenőrizendő. |

## Videó-záróképkocka kamerái (ideiglenes, nem kerültek a lockba)

Kiindulás: `Cam_02_Nappali_terasz` (8,30; 4,40; 1,55), irány 49,1°, 20 mm, szenzor 36 mm.

| Jelölt | Előre | Elfordulás balra | Pozíció (x, y, z) | Irány | Fájl |
|---|---:|---:|---|---:|---|
| **A (választott)** | 40 cm | 20° | (8,00; 4,66; 1,55) | 69,1° | `04_renderek/ai_video_tests/A902_LakeForest_1_nappali_blender_zarokep_jelolt_A.png` |
| B | 60 cm | 30° | (7,85; 4,79; 1,55) | 79,1° | `…_jelolt_B.png` |
| C | 80 cm | 38° | (7,70; 4,92; 1,55) | 87,1° | `…_jelolt_C.png` |

**A választás indoka:** a prompt szerinti ~40 cm-es előremozgás, a TV-fal bal szélen megjelenik, a teraszüveg és a jakuzzi a kép jobb felén marad. B-nél a TV közelről, éles szögből tölti ki a bal ötödöt. C-nél a terasz teljesen kiesik.

**Megjegyzés:** a Blender LF-rétegben a TV-fal travertin panel bronz kerettel, mindkét oldalon **világos tölgy lamellákkal** (`L_lamella_*`). A Veo Lite első tesztje tehát véletlenül a tervezett rétegnek megfelelő lamellás falat „találta ki”. A ChatGPT-forrásképben ez nem látszik.

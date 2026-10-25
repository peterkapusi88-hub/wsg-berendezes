#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12C_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v2_sarok/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k12_JAVASLAT_v2.blend
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k13_KAMERACSOMAG_C.blend
shasum -a 256 "$SRC" > "$W/futtat3_sha_forras_elotte.txt"
"$BL" -b "$SRC" --python "$W/03_rogzites_C.py" -- "$UJ" > "$W/03_rogzites.log" 2>&1
[ -f "$UJ" ] || { echo HIBA_03 > "$W/futtat3.done"; exit 1; }
"$BL" -b "$UJ" --python "$W/04_ellenorzes_C.py" -- "$W/kepek_k13" > "$W/04_ellenorzes.log" 2>&1
shasum -a 256 "$SRC" "$UJ" "$W/lock_k13/geometry_lock_A902_v2b.json" > "$W/futtat3_sha.txt"
echo KESZ > "$W/futtat3.done"

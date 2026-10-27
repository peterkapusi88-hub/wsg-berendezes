#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v2_sarok
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k12_JAVASLAT_v2.blend
"$BL" -b "$SRC" --python "$W/03_cam12_rogzites_v2.py" -- "$UJ" > "$W/03_rogzites.log" 2>&1
[ -f "$UJ" ] || { echo HIBA_03 > "$W/futtat3.done"; exit 1; }
"$BL" -b "$UJ" --python "$W/04_ellenorzes_v2.py" -- "$W/kepek_k12v2" > "$W/04_ellenorzes.log" 2>&1
shasum -a 256 "$UJ" "$W/lock_k12v2/geometry_lock_A902_v2b.json" > "$W/futtat3_sha.txt"
echo KESZ > "$W/futtat3.done"

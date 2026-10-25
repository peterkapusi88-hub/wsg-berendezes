#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k12_JAVASLAT.blend
"$BL" -b "$SRC" --python "$W/02_cam12_rogzites.py" -- "$UJ" > "$W/02_rogzites.log" 2>&1
[ -f "$UJ" ] || { echo HIBA_02 > "$W/futtat2.done"; exit 1; }
"$BL" -b "$UJ" --python "$W/03_ellenorzes_tomegek.py" -- "$W/kepek2" > "$W/03_ellenorzes.log" 2>&1
shasum -a 256 "$UJ" "$W/lock_k12/geometry_lock_A902_v2b.json" > "$W/futtat2_sha.txt"
echo KESZ > "$W/futtat2.done"

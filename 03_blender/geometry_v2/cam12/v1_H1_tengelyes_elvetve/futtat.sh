#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
"$BL" -b "$SRC" --python "$W/01_cam12_jeloltek.py" -- "$W/kepek" > "$W/01_cam12.log" 2>&1
echo KESZ > "$W/futtat.done"

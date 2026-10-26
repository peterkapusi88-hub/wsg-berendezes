#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v2_sarok
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
"$BL" -b "$SRC" --python "$W/02_finomitas.py" -- "$W/kepek_finom" > "$W/02_finomitas.log" 2>&1
echo KESZ > "$W/futtat2.done"

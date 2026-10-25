#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_elrendezes_cam03_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v2_sarok/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k12_JAVASLAT_v2.blend
C3='{"nev": "K1_EK_konyhatengely_20", "loc": [9.45, 7.55, 1.50], "theta": -90.0, "lens": 20.0, "shift_y": -0.08}'
shasum -a 256 "$SRC" > "$W/futtat2_sha_elotte.txt"
"$BL" -b "$SRC" --python "$W/02_alternativak_renderek.py" -- "$W/kepek_alt" "$C3" > "$W/02_alt.log" 2>&1
shasum -a 256 "$SRC" > "$W/futtat2_sha_utana.txt"
echo KESZ > "$W/futtat2.done"

#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12C_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12_v2_sarok/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k12_JAVASLAT_v2.blend
shasum -a 256 "$SRC" > "$W/futtat2_sha_elotte.txt"
"$BL" -b "$SRC" --python "$W/01_cam12C_jeloltek.py" -- "$W/kepek_r2b" "$W/jeloltek_r2.json" nincs > "$W/02_cam12C_r2b.log" 2>&1
shasum -a 256 "$SRC" > "$W/futtat2_sha_utana.txt"
echo KESZ > "$W/futtat2.done"

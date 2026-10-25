#!/bin/bash
# KEP-004 V3_TEST – Cam_02 bútortömbös referencia S01/S02 (Claude, 2026-10-25). A main v2b-1-k11b modell MÁSOLATÁN fut, nem ment.
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_tomeg_cam02_v3test_v1
M=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=$W/src_main_v2b1k11b.blend
export WSG_LOCK=$M/blender_agy640_v1/lock_k11b/geometry_lock_A902_v2b.json
export WSG_VILLAMOS=$M/blender_cam11_v1/A902_villamos.json
export WSG_VALIDATOR=$M/blender_cam11_v1/geometry_validator_v2.py
shasum -a 256 "$SRC" "$WSG_LOCK" "$WSG_VILLAMOS" "$WSG_VALIDATOR" > "$W/futtat_sha_elotte.txt"
"$BL" -b "$SRC" --python "$W/01_tomeg_cam02_v3test.py" -- "$W/kepek" > "$W/01_tomeg_v3test.log" 2>&1
shasum -a 256 "$SRC" > "$W/futtat_sha_utana.txt"
echo KESZ > "$W/futtat.done"

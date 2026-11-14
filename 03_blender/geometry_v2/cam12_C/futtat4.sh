#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam12C_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
SRC=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k13_KAMERACSOMAG_C.blend
shasum -a 256 "$SRC" > "$W/futtat4_sha_elotte.txt"
"$BL" -b "$SRC" --python "$W/05_kerek_meretproba.py" -- "$W/kepek_kerek" > "$W/05_kerek.log" 2>&1
shasum -a 256 "$SRC" > "$W/futtat4_sha_utana.txt"
echo KESZ > "$W/futtat4.done"

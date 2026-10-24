#!/bin/bash
# Végső validáció a PR #15 lockjával (v2b-1-k11b, sha256 7aa85d70…154b) – 2026-10-25
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
export WSG_LOCK=$W/lock_k11b/geometry_lock_A902_v2b.json
for m in ures referencia master_butor; do
  "$BL" -b "$UJ" --python "$W/02_validator_agy640.py" -- $m v2b1k11b > "$W/02_validator_v2b1k11b_$m.log" 2>&1
done
for m in zenit_master lakeforest_master; do
  "$BL" -b "$UJ" --python "$W/02b_validator_stil_master.py" -- $m v2b1k11b > "$W/02b_validator_v2b1k11b_$m.log" 2>&1
done
shasum -a 256 "$UJ" "$WSG_LOCK" > "$W/futtat4_sha.txt"
echo KESZ > "$W/futtat4.done"

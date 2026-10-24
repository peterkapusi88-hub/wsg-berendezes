#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
K11=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261024_v2b1k11_JAVASLAT.blend
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
for m in zenit_master lakeforest_master; do
  "$BL" -b "$K11" --python "$W/02b_validator_stil_master.py" -- $m k11_regi > "$W/02b_validator_k11_regi_$m.log" 2>&1
  "$BL" -b "$UJ" --python "$W/02b_validator_stil_master.py" -- $m k11b_agy640_r2 > "$W/02b_validator_k11b_agy640_r2_$m.log" 2>&1
done
echo KESZ > "$W/futtat3b.done"

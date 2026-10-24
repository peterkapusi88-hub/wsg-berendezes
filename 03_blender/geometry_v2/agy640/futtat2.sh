#!/bin/bash
W=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1
BL=/Applications/Blender.app/Contents/MacOS/Blender
K11=/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/WSG_A902_v2b_alaprajz_ELOZETES_20261024_v2b1k11_JAVASLAT.blend
UJ=$W/WSG_A902_v2b_alaprajz_ELOZETES_20261025_v2b1k11b_agy640_JAVASLAT_r2.blend
"$BL" -b "$K11" --python "$W/01_agy640_athelyezes.py" -- "$UJ" "$W/01_agy640_naplo_r2.json" > "$W/01_agy640_r2.log" 2>&1
if [ ! -f "$UJ" ]; then echo HIBA_01 > "$W/futtat2.done"; exit 1; fi
"$BL" -b "$UJ" --python "$W/04_vizsgal.py" -- "$W/04_vizsgal_r2.json" > "$W/04_vizsgal_r2.log" 2>&1
for m in ures referencia master_butor; do
  "$BL" -b "$UJ" --python "$W/02_validator_agy640.py" -- $m k11b_agy640_r2 > "$W/02_validator_k11b_agy640_r2_$m.log" 2>&1
done
mkdir -p "$W/kepek_r2"
"$BL" -b "$UJ" --python "$W/03_render_ellenorzes_agy640.py" -- "$W/kepek_r2" > "$W/03_render_r2.log" 2>&1
echo KESZ > "$W/futtat2.done"

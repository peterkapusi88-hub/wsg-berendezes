#!/bin/bash
# qa3.sh <seq> -> gate image for V3.2 plan entry (image already staged from Mac)
SEQ=$1
read CAM DIR IMG < <(python3 -c "import json,os;p=[x for x in json.load(open('/home/claude/work/v32_plan.json'))+json.load(open('/home/claude/work/v32_fix_plan.json')) if x['seq']==$SEQ][0];print(p['kamera'],p['dir'],p['kep_fajl'])")
IMG=${2:-$IMG}
U=/mnt/user-data/uploads/Downloads/WSG_ASTRA_V3_2_RENDEREK/images/$IMG
BASE=$(ls /home/claude/work/$DIR/01_image1_*)
mkdir -p out32/img out32/gate; cp "$U" out32/img/
python3 py/gate.py $CAM "$BASE" out32/img/$IMG out32/gate/${IMG%.png}_gate.jpg >/dev/null && echo out32/gate/${IMG%.png}_gate.jpg

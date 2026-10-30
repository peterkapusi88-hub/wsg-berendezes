# S16 F2 – CAD-terv önellenőrzés (S16-R15-GY-v1)

Generálva: 2026-10-30 · `f2_cad_export.py` · 129 alkatrész

A `cad_terv.json`-ból Pythonban újraépített testet (ugyanaz a terv, amiből a .lsp készül) összevetem a QA által ellenőrzött testtel (R14/R15 zárt jelenet hálója vagy kontúr-extrudálás). Ez a terv helyességét bizonyítja; az AutoCAD-beli végrehajtást a `(s16-readback)` + `f2_readback.py` igazolja majd.

**Eredmény: 129/129 egyezik** (térfogat ≤ 0,5 %, befoglaló ≤ 0,05 mm, zárt test); legnagyobb térfogat-eltérés 0.040 %.

## Megjegyzések

- T-DOOR-L-BACK: curve_vertices ellentmond a kontúrnak (max. eltérés 12.071 mm) – a sokszögelt kontúr készül
- TV-FIELD: curve_vertices ellentmond a kontúrnak (max. eltérés 2001.5 mm) – a sokszögelt kontúr készül

## Alkatrészek

| ID | réteg | test | kivonás | térfogat mm³ | ref mm³ | Δ% | befoglaló Δ mm |
|---|---|---|---|---|---|---|---|
| D1-L | `$PART_S16_D1-L#0V00` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| D1-R | `$PART_S16_D1-R#0V00` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| D1-T | `$PART_S16_D1-T#F0F0` | box | 0 | 2420334 | 2420335 | -0.0 | 0.0 |
| D1-BACK | `$PART_S16_D1-BACK#0000` | box | 0 | 1225728 | 1225728 | -0.0 | 0.0 |
| D1-FRONT | `$PART_S16_D1-FRONT#VVVV` | box | 0 | 2939328 | 2939329 | -0.0 | 0.0 |
| D1-BOX-L | `$PART_S16_D1-BOX-L#LLLL` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D1-BOX-R | `$PART_S16_D1-BOX-R#LLLL` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D1-BOX-F | `$PART_S16_D1-BOX-F#00L0` | box | 0 | 1124550 | 1124550 | 0.0 | 0.0 |
| D1-BOX-H | `$PART_S16_D1-BOX-H#00L0` | box | 0 | 1124550 | 1124550 | 0.0 | 0.0 |
| D1-BOX-B | `$PART_S16_D1-BOX-B#L0L0` | box | 0 | 1552950 | 1552950 | 0.0 | 0.0 |
| D2-L | `$PART_S16_D2-L#VVV0` | box | 0 | 2547720 | 2547721 | -0.0 | 0.0 |
| D2-R | `$PART_S16_D2-R#VVV0` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D2-B | `$PART_S16_D2-B#V000` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D2-T | `$PART_S16_D2-T#F0F0` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D2-BACK | `$PART_S16_D2-BACK#0000` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D2-FRONT | `$PART_S16_D2-FRONT#VVVV` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D2-BOX-L | `$PART_S16_D2-BOX-L#LLLL` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D2-BOX-R | `$PART_S16_D2-BOX-R#LLLL` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D2-BOX-F | `$PART_S16_D2-BOX-F#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D2-BOX-H | `$PART_S16_D2-BOX-H#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D2-BOX-B | `$PART_S16_D2-BOX-B#L0L0` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D3-L | `$PART_S16_D3-L#VVV0` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D3-R | `$PART_S16_D3-R#VVV0` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D3-B | `$PART_S16_D3-B#V000` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D3-T | `$PART_S16_D3-T#F0F0` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D3-BACK | `$PART_S16_D3-BACK#0000` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D3-FRONT | `$PART_S16_D3-FRONT#VVVV` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D3-BOX-L | `$PART_S16_D3-BOX-L#LLLL` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D3-BOX-R | `$PART_S16_D3-BOX-R#LLLL` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D3-BOX-F | `$PART_S16_D3-BOX-F#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D3-BOX-H | `$PART_S16_D3-BOX-H#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D3-BOX-B | `$PART_S16_D3-BOX-B#L0L0` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D4-L | `$PART_S16_D4-L#VVV0` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D4-R | `$PART_S16_D4-R#VVV0` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D4-B | `$PART_S16_D4-B#V000` | box | 0 | 6029604 | 6029606 | -0.0 | 0.0 |
| D4-T | `$PART_S16_D4-T#F0F0` | box | 0 | 6029604 | 6029606 | -0.0 | 0.0 |
| D4-BACK | `$PART_S16_D4-BACK#0000` | box | 0 | 3053568 | 3053569 | -0.0 | 0.0 |
| D4-FRONT | `$PART_S16_D4-FRONT#VVVV` | box | 0 | 6987708 | 6987710 | -0.0 | 0.0 |
| D4-BOX-L | `$PART_S16_D4-BOX-L#LLLL` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D4-BOX-R | `$PART_S16_D4-BOX-R#LLLL` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D4-BOX-F | `$PART_S16_D4-BOX-F#00L0` | box | 0 | 2998800 | 2998800 | 0.0 | 0.0 |
| D4-BOX-H | `$PART_S16_D4-BOX-H#00L0` | box | 0 | 2998800 | 2998800 | 0.0 | 0.0 |
| D4-BOX-B | `$PART_S16_D4-BOX-B#L0L0` | box | 0 | 4141200 | 4141200 | 0.0 | 0.0 |
| D5-L | `$PART_S16_D5-L#VVV0` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D5-R | `$PART_S16_D5-R#VVV0` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D5-B | `$PART_S16_D5-B#V000` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D5-T | `$PART_S16_D5-T#F0F0` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D5-BACK | `$PART_S16_D5-BACK#0000` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D5-FRONT | `$PART_S16_D5-FRONT#VVVV` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D5-BOX-L | `$PART_S16_D5-BOX-L#LLLL` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D5-BOX-R | `$PART_S16_D5-BOX-R#LLLL` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D5-BOX-F | `$PART_S16_D5-BOX-F#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D5-BOX-H | `$PART_S16_D5-BOX-H#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D5-BOX-B | `$PART_S16_D5-BOX-B#L0L0` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D6-L | `$PART_S16_D6-L#VVV0` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D6-R | `$PART_S16_D6-R#0F0F` | box | 0 | 1577160 | 1577171 | -0.001 | 0.0 |
| D6-B | `$PART_S16_D6-B#V000` | box | 0 | 1983582 | 1983584 | -0.0 | 0.0 |
| D6-T | `$PART_S16_D6-T#F0F0` | box | 0 | 1983582 | 1983584 | -0.0 | 0.0 |
| D6-BACK | `$PART_S16_D6-BACK#0000` | extrude_y/bulge | 0 | 1181807 | 1181790 | 0.001 | 0.0 |
| D6-FRONT | `$PART_S16_D6-FRONT#VVVV` | extrude_y/bulge | 0 | 2711712 | 2711678 | 0.001 | 0.0 |
| D6-BOX-L | `$PART_S16_D6-BOX-L#LLLL` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D6-BOX-R | `$PART_S16_D6-BOX-R#LLLL` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D6-BOX-F | `$PART_S16_D6-BOX-F#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D6-BOX-H | `$PART_S16_D6-BOX-H#00L0` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D6-BOX-B | `$PART_S16_D6-BOX-B#L0L0` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| T-L | `$PART_S16_T-L#0V00` | box | 0 | 15316650 | 15316650 | -0.0 | 0.0 |
| T-R | `$PART_S16_T-R#0F0F` | box | 0 | 13375530 | 13375536 | -0.0 | 0.0 |
| T-B | `$PART_S16_T-B#V000` | box | 1 | 4874364 | 4874364 | 0.0 | 0.0 |
| T-C | `$PART_S16_T-C#0V00` | box | 0 | 13763754 | 13763759 | -0.0 | 0.0 |
| T-L-S1 | `$PART_S16_T-L-S1#V000` | box | 0 | 2119320 | 2119321 | -0.0 | 0.0 |
| T-L-S2 | `$PART_S16_T-L-S2#V000` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-L-S3 | `$PART_S16_T-L-S3#V000` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-L-S4 | `$PART_S16_T-L-S4#V000` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-L-S5 | `$PART_S16_T-L-S5#V000` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-L-BACK | `$PART_S16_T-L-BACK#0000` | extrude_y/bulge | 0 | 6228450 | 6228437 | 0.0 | 0.0 |
| T-L-SERVICE | `$PART_S16_T-L-SERVICE#VVVV` | box | 0 | 1120560 | 1120558 | 0.0 | 0.0 |
| T-R-S1 | `$PART_S16_T-R-S1#V000` | box | 0 | 2119320 | 2119321 | -0.0 | 0.0 |
| T-R-S2 | `$PART_S16_T-R-S2#V000` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-R-S3 | `$PART_S16_T-R-S3#V000` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-R-S4 | `$PART_S16_T-R-S4#V000` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-R-S5 | `$PART_S16_T-R-S5#V000` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-R-BACK | `$PART_S16_T-R-BACK#0000` | extrude_y/bulge | 0 | 6228450 | 6228438 | 0.0 | 0.0 |
| T-R-SERVICE | `$PART_S16_T-R-SERVICE#VVVV` | box | 0 | 1120560 | 1120558 | 0.0 | 0.0 |
| T-DOOR-L | `$PART_S16_T-DOOR-L#VVVV` | extrude_y/bulge | 2 | 3800306 | 3800240 | 0.002 | 0.0 |
| T-DOOR-R | `$PART_S16_T-DOOR-R#VVVV` | extrude_y/bulge | 0 | 16912315 | 16912284 | 0.0 | 0.0 |
| TEXTILE | `$PART_S16_TEXTILE#KKKK` | extrude_y/bulge | 0 | 7218474 | 7218454 | 0.0 | 0.0 |
| BG-1 | `$PART_S16_BG-1#0000` | box | 0 | 33157735 | 33157734 | 0.0 | 0.0 |
| BG-2 | `$PART_S16_BG-2#0000` | box | 0 | 27781358 | 27781363 | -0.0 | 0.0 |
| BG-3 | `$PART_S16_BG-3#0000` | box | 0 | 27781358 | 27781363 | -0.0 | 0.0 |
| BG-4 | `$PART_S16_BG-4#0000` | box | 0 | 27720030 | 27720030 | -0.0 | 0.0 |
| BATTEN-1 | `$PART_S16_BATTEN-1#0000` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-2 | `$PART_S16_BATTEN-2#0000` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-3 | `$PART_S16_BATTEN-3#0000` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-4 | `$PART_S16_BATTEN-4#0000` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-5 | `$PART_S16_BATTEN-5#0000` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| CURVE-T-TOP | `$PART_S16_CURVE-T-TOP#FFFF` | extrude_y/bulge | 0 | 5798408 | 5797676 | 0.013 | 0.0 |
| FRAME-T-TOP | `$PART_S16_FRAME-T-TOP#FFFF` | extrude_y/bulge | 0 | 309707 | 309670 | 0.012 | 0.0 |
| CURVE-T-BOT | `$PART_S16_CURVE-T-BOT#F0FF` | extrude_y/bulge | 0 | 5537914 | 5537559 | 0.006 | 0.0 |
| FRAME-T-BOT | `$PART_S16_FRAME-T-BOT#FFFF` | extrude_y/bulge | 0 | 295794 | 295775 | 0.006 | 0.0 |
| FRAME-T-L | `$PART_S16_FRAME-T-L#0F0F` | box | 0 | 818100 | 818100 | -0.0 | 0.0 |
| FRAME-T-R | `$PART_S16_FRAME-T-R#0F0F` | box | 0 | 714420 | 714421 | -0.0 | 0.0 |
| FRAME-T-MID | `$PART_S16_FRAME-T-MID#F0FF` | box | 0 | 140454 | 140454 | -0.0 | 0.0 |
| FRAME-B-LOW-1 | `$PART_S16_FRAME-B-LOW-1#F0F0` | box | 0 | 275400 | 275400 | -0.0 | 0.0 |
| FRAME-B-LOW-2 | `$PART_S16_FRAME-B-LOW-2#F0F0` | box | 0 | 333720 | 333720 | -0.0 | 0.0 |
| FRAME-B-LOW-3 | `$PART_S16_FRAME-B-LOW-3#F0F0` | box | 0 | 249480 | 249480 | -0.0 | 0.0 |
| FRAME-B-HIGH-1 | `$PART_S16_FRAME-B-HIGH-1#F0F0` | box | 0 | 275400 | 275400 | -0.0 | 0.0 |
| FRAME-B-HIGH-2 | `$PART_S16_FRAME-B-HIGH-2#F0F0` | box | 0 | 333720 | 333720 | -0.0 | 0.0 |
| FRAME-B-HIGH-3 | `$PART_S16_FRAME-B-HIGH-3#F0F0` | box | 0 | 249480 | 249480 | -0.0 | 0.0 |
| FRAME-B-TOP | `$PART_S16_FRAME-B-TOP#FFFF` | extrude_y/bulge | 0 | 36135 | 36120 | 0.04 | 0.0 |
| CURVE-B-TOP | `$PART_S16_CURVE-B-TOP#FFFF` | extrude_y/bulge | 0 | 676521 | 676249 | 0.04 | 0.0 |
| FRAME-B-BOT | `$PART_S16_FRAME-B-BOT#FFFF` | extrude_y/bulge | 0 | 36135 | 36120 | 0.04 | 0.0 |
| CURVE-B-BOT | `$PART_S16_CURVE-B-BOT#FFFF` | extrude_y/bulge | 0 | 676521 | 676249 | 0.04 | 0.0 |
| FRAME-B-R | `$PART_S16_FRAME-B-R#0F0F` | box | 0 | 84240 | 84241 | -0.001 | 0.0 |
| TV-SPACER-1 | `$PART_S16_TV-SPACER-1#FFFF` | box | 0 | 5237100 | 5237095 | 0.0 | 0.0 |
| TV-SPACER-2 | `$PART_S16_TV-SPACER-2#FFFF` | box | 0 | 4181400 | 4181429 | -0.001 | 0.0 |
| T-LOW-DIV | `$PART_S16_T-LOW-DIV#0V00` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| T-LOW-BACK | `$PART_S16_T-LOW-BACK#0000` | extrude_y/bulge | 0 | 1271639 | 1271623 | 0.001 | 0.0 |
| T-DOOR-L-BACK | `$PART_S16_T-DOOR-L-BACK#FFFF` | extrude_y | 0 | 11167415 | 11167407 | 0.0 | 0.0 |
| TV-FIELD | `$PART_S16_TV-FIELD#VVVV` | extrude_y | 1 | 67265790 | 67265790 | 0.0 | 0.0 |
| BG-FINISH | `$PART_S16_BG-FINISH#0000` | box | 0 | 6871085 | 6871079 | 0.0 | 0.0 |
| TOP-WASH-COVER | `$PART_S16_TOP-WASH-COVER#0000` | box | 0 | 68568 | 68568 | -0.001 | 0.0 |
| TOP-WASH-BAFFLE | `$PART_S16_TOP-WASH-BAFFLE#0000` | box | 0 | 205704 | 205703 | 0.001 | 0.0 |
| TOP-WASH-HIDDEN-END | `$PART_S16_TOP-WASH-HIDDEN-END#0000` | box | 0 | 240 | 240 | 0.008 | 0.0 |
| UPLIGHT-TRAY | `$PART_S16_UPLIGHT-TRAY#0000` | box | 0 | 68280 | 68275 | 0.007 | 0.0 |
| UPLIGHT-FRONT-VISOR | `$PART_S16_UPLIGHT-FRONT-VISOR#0000` | box | 0 | 34140 | 34138 | 0.007 | 0.0 |
| UPLIGHT-REAR-VISOR | `$PART_S16_UPLIGHT-REAR-VISOR#0000` | box | 0 | 25605 | 25603 | 0.007 | 0.0 |
| DECK-CONTINUOUS-COVER | `$PART_S16_DECK-CONTINUOUS-COVER#0000` | box | 0 | 84096 | 84096 | -0.0 | 0.0 |
| DECK-CONTINUOUS-BAFFLE | `$PART_S16_DECK-CONTINUOUS-BAFFLE#0000` | box | 0 | 178704 | 178704 | -0.0 | 0.0 |
| LOW-INTERNAL-LIGHT-VISOR | `$PART_S16_LOW-INTERNAL-LIGHT-VISOR#0000` | box | 0 | 24480 | 24480 | 0.0 | 0.0 |

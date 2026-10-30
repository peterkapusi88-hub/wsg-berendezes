# S16 F2 – CAD-terv önellenőrzés (S16-R15C-GY-v1)

Generálva: 2026-10-30 · `f2_cad_export.py` · 129 alkatrész

A `cad_terv.json`-ból Pythonban újraépített testet (ugyanaz a terv, amiből a .lsp készül) összevetem a QA által ellenőrzött testtel (R14/R15 zárt jelenet hálója vagy kontúr-extrudálás). Ez a terv helyességét bizonyítja; az AutoCAD-beli végrehajtást a `(s16-readback)` + `f2_readback.py` igazolja majd.

**Eredmény: 129/129 egyezik** (térfogat ≤ 0,5 %, befoglaló ≤ 0,05 mm, zárt test); legnagyobb térfogat-eltérés 0.040 %.

## Megjegyzések

- T-DOOR-L-BACK: curve_vertices ellentmond a kontúrnak (max. eltérés 12.071 mm) – a sokszögelt kontúr készül
- TV-FIELD: curve_vertices ellentmond a kontúrnak (max. eltérés 2001.5 mm) – a sokszögelt kontúr készül

## Alkatrészek

| ID | réteg | test | kivonás | térfogat mm³ | ref mm³ | Δ% | befoglaló Δ mm |
|---|---|---|---|---|---|---|---|
| D1-L | `$PART_S16_D1-L˙0˙0¨V000˙0¨#0¨16001` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| D1-R | `$PART_S16_D1-R˙0˙0¨V000˙0¨#0¨16002` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| D1-T | `$PART_S16_D1-T˙0˙0¨FF00˙0¨#0¨16003` | box | 0 | 2420334 | 2420335 | -0.0 | 0.0 |
| D1-BACK | `$PART_S16_D1-BACK˙0˙0¨0000˙0¨#0¨16004` | box | 0 | 1225728 | 1225728 | -0.0 | 0.0 |
| D1-FRONT | `$PART_S16_D1-FRONT˙0˙0¨VVVV˙0¨#0¨16005` | box | 0 | 2939328 | 2939329 | -0.0 | 0.0 |
| D1-BOX-L | `$PART_S16_D1-BOX-L˙0˙0¨LLLL˙0¨#0¨16006` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D1-BOX-R | `$PART_S16_D1-BOX-R˙0˙0¨LLLL˙0¨#0¨16007` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D1-BOX-F | `$PART_S16_D1-BOX-F˙0˙0¨L000˙0¨#0¨16008` | box | 0 | 1124550 | 1124550 | 0.0 | 0.0 |
| D1-BOX-H | `$PART_S16_D1-BOX-H˙0˙0¨L000˙0¨#0¨16009` | box | 0 | 1124550 | 1124550 | 0.0 | 0.0 |
| D1-BOX-B | `$PART_S16_D1-BOX-B˙0˙0¨LL00˙0¨#0¨16010` | box | 0 | 1552950 | 1552950 | 0.0 | 0.0 |
| D2-L | `$PART_S16_D2-L˙0˙0¨V0VV˙0¨#0¨16011` | box | 0 | 2547720 | 2547721 | -0.0 | 0.0 |
| D2-R | `$PART_S16_D2-R˙0˙0¨V0VV˙0¨#0¨16012` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D2-B | `$PART_S16_D2-B˙0˙0¨V000˙0¨#0¨16013` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D2-T | `$PART_S16_D2-T˙0˙0¨FF00˙0¨#0¨16014` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D2-BACK | `$PART_S16_D2-BACK˙0˙0¨0000˙0¨#0¨16015` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D2-FRONT | `$PART_S16_D2-FRONT˙0˙0¨VVVV˙0¨#0¨16016` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D2-BOX-L | `$PART_S16_D2-BOX-L˙0˙0¨LLLL˙0¨#0¨16017` | box | 0 | 1030950 | 1030949 | 0.0 | 0.0 |
| D2-BOX-R | `$PART_S16_D2-BOX-R˙0˙0¨LLLL˙0¨#0¨16018` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D2-BOX-F | `$PART_S16_D2-BOX-F˙0˙0¨L000˙0¨#0¨16019` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D2-BOX-H | `$PART_S16_D2-BOX-H˙0˙0¨L000˙0¨#0¨16020` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D2-BOX-B | `$PART_S16_D2-BOX-B˙0˙0¨LL00˙0¨#0¨16021` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D3-L | `$PART_S16_D3-L˙0˙0¨V0VV˙0¨#0¨16022` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D3-R | `$PART_S16_D3-R˙0˙0¨V0VV˙0¨#0¨16023` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D3-B | `$PART_S16_D3-B˙0˙0¨V000˙0¨#0¨16024` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D3-T | `$PART_S16_D3-T˙0˙0¨FF00˙0¨#0¨16025` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D3-BACK | `$PART_S16_D3-BACK˙0˙0¨0000˙0¨#0¨16026` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D3-FRONT | `$PART_S16_D3-FRONT˙0˙0¨VVVV˙0¨#0¨16027` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D3-BOX-L | `$PART_S16_D3-BOX-L˙0˙0¨LLLL˙0¨#0¨16028` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D3-BOX-R | `$PART_S16_D3-BOX-R˙0˙0¨LLLL˙0¨#0¨16029` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D3-BOX-F | `$PART_S16_D3-BOX-F˙0˙0¨L000˙0¨#0¨16030` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D3-BOX-H | `$PART_S16_D3-BOX-H˙0˙0¨L000˙0¨#0¨16031` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D3-BOX-B | `$PART_S16_D3-BOX-B˙0˙0¨LL00˙0¨#0¨16032` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D4-L | `$PART_S16_D4-L˙0˙0¨V0VV˙0¨#0¨16033` | box | 0 | 2547720 | 2547704 | 0.001 | 0.0 |
| D4-R | `$PART_S16_D4-R˙0˙0¨V0VV˙0¨#0¨16034` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D4-B | `$PART_S16_D4-B˙0˙0¨V000˙0¨#0¨16035` | box | 0 | 6029604 | 6029606 | -0.0 | 0.0 |
| D4-T | `$PART_S16_D4-T˙0˙0¨FF00˙0¨#0¨16036` | box | 0 | 6029604 | 6029606 | -0.0 | 0.0 |
| D4-BACK | `$PART_S16_D4-BACK˙0˙0¨0000˙0¨#0¨16037` | box | 0 | 3053568 | 3053569 | -0.0 | 0.0 |
| D4-FRONT | `$PART_S16_D4-FRONT˙0˙0¨VVVV˙0¨#0¨16038` | box | 0 | 6987708 | 6987710 | -0.0 | 0.0 |
| D4-BOX-L | `$PART_S16_D4-BOX-L˙0˙0¨LLLL˙0¨#0¨16039` | box | 0 | 1030950 | 1030957 | -0.001 | 0.0 |
| D4-BOX-R | `$PART_S16_D4-BOX-R˙0˙0¨LLLL˙0¨#0¨16040` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D4-BOX-F | `$PART_S16_D4-BOX-F˙0˙0¨L000˙0¨#0¨16041` | box | 0 | 2998800 | 2998800 | 0.0 | 0.0 |
| D4-BOX-H | `$PART_S16_D4-BOX-H˙0˙0¨L000˙0¨#0¨16042` | box | 0 | 2998800 | 2998800 | 0.0 | 0.0 |
| D4-BOX-B | `$PART_S16_D4-BOX-B˙0˙0¨LL00˙0¨#0¨16043` | box | 0 | 4141200 | 4141200 | 0.0 | 0.0 |
| D5-L | `$PART_S16_D5-L˙0˙0¨V0VV˙0¨#0¨16044` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D5-R | `$PART_S16_D5-R˙0˙0¨V0VV˙0¨#0¨16045` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D5-B | `$PART_S16_D5-B˙0˙0¨V000˙0¨#0¨16046` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D5-T | `$PART_S16_D5-T˙0˙0¨FF00˙0¨#0¨16047` | box | 0 | 2359674 | 2359675 | -0.0 | 0.0 |
| D5-BACK | `$PART_S16_D5-BACK˙0˙0¨0000˙0¨#0¨16048` | box | 0 | 1195008 | 1195008 | -0.0 | 0.0 |
| D5-FRONT | `$PART_S16_D5-FRONT˙0˙0¨VVVV˙0¨#0¨16049` | box | 0 | 2871288 | 2871289 | -0.0 | 0.0 |
| D5-BOX-L | `$PART_S16_D5-BOX-L˙0˙0¨LLLL˙0¨#0¨16050` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D5-BOX-R | `$PART_S16_D5-BOX-R˙0˙0¨LLLL˙0¨#0¨16051` | box | 0 | 1030950 | 1030941 | 0.001 | 0.0 |
| D5-BOX-F | `$PART_S16_D5-BOX-F˙0˙0¨L000˙0¨#0¨16052` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D5-BOX-H | `$PART_S16_D5-BOX-H˙0˙0¨L000˙0¨#0¨16053` | box | 0 | 1093050 | 1093050 | 0.0 | 0.0 |
| D5-BOX-B | `$PART_S16_D5-BOX-B˙0˙0¨LL00˙0¨#0¨16054` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| D6-L | `$PART_S16_D6-L˙0˙0¨V0VV˙0¨#0¨16055` | box | 0 | 2547720 | 2547738 | -0.001 | 0.0 |
| D6-R | `$PART_S16_D6-R˙0˙0¨00FF˙0¨#0¨16056` | box | 0 | 1577160 | 1577171 | -0.001 | 0.0 |
| D6-B | `$PART_S16_D6-B˙0˙0¨00V0˙0¨#0¨16057` | box | 0 | 1983582 | 1983584 | -0.0 | 0.0 |
| D6-T | `$PART_S16_D6-T˙0˙0¨00FF˙0¨#0¨16058` | box | 0 | 1983582 | 1983584 | -0.0 | 0.0 |
| D6-BACK | `$PART_S16_D6-BACK˙0˙0¨0000˙0¨#0¨16059` | extrude_y/bulge | 0 | 1181807 | 1181790 | 0.001 | 0.0 |
| D6-FRONT | `$PART_S16_D6-FRONT˙0˙0¨VVVV˙0¨#0¨16060` | extrude_y/bulge | 0 | 2711712 | 2711678 | 0.001 | 0.0 |
| D6-BOX-L | `$PART_S16_D6-BOX-L˙0˙0¨LLLL˙0¨#0¨16061` | box | 0 | 878700 | 878700 | 0.0 | 0.0 |
| D6-BOX-R | `$PART_S16_D6-BOX-R˙0˙0¨LLLL˙0¨#0¨16062` | box | 0 | 878700 | 878700 | 0.0 | 0.0 |
| D6-BOX-F | `$PART_S16_D6-BOX-F˙0˙0¨L000˙0¨#0¨16063` | box | 0 | 910875 | 910875 | 0.0 | 0.0 |
| D6-BOX-H | `$PART_S16_D6-BOX-H˙0˙0¨L000˙0¨#0¨16064` | box | 0 | 910875 | 910875 | 0.0 | 0.0 |
| D6-BOX-B | `$PART_S16_D6-BOX-B˙0˙0¨LL00˙0¨#0¨16065` | box | 0 | 1509450 | 1509450 | 0.0 | 0.0 |
| T-L | `$PART_S16_T-L˙0˙0¨V000˙0¨#0¨16066` | box | 0 | 15316650 | 15316650 | -0.0 | 0.0 |
| T-R | `$PART_S16_T-R˙0˙0¨FF00˙0¨#0¨16067` | box | 0 | 13375530 | 13375536 | -0.0 | 0.0 |
| T-B | `$PART_S16_T-B˙0˙0¨V000˙0¨#0¨16068` | box | 1 | 4874364 | 4874364 | 0.0 | 0.0 |
| T-C | `$PART_S16_T-C˙0˙0¨V000˙0¨#0¨16069` | box | 0 | 13763754 | 13763759 | -0.0 | 0.0 |
| T-L-S1 | `$PART_S16_T-L-S1˙0˙0¨V000˙0¨#0¨16070` | box | 0 | 2119320 | 2119321 | -0.0 | 0.0 |
| T-L-S2 | `$PART_S16_T-L-S2˙0˙0¨V000˙0¨#0¨16071` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-L-S3 | `$PART_S16_T-L-S3˙0˙0¨V000˙0¨#0¨16072` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-L-S4 | `$PART_S16_T-L-S4˙0˙0¨V000˙0¨#0¨16073` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-L-S5 | `$PART_S16_T-L-S5˙0˙0¨V000˙0¨#0¨16074` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-L-BACK | `$PART_S16_T-L-BACK˙0˙0¨0000˙0¨#0¨16075` | extrude_y/bulge | 0 | 6228450 | 6228437 | 0.0 | 0.0 |
| T-L-SERVICE | `$PART_S16_T-L-SERVICE˙0˙0¨VVVV˙0¨#0¨16076` | box | 0 | 1120560 | 1120558 | 0.0 | 0.0 |
| T-R-S1 | `$PART_S16_T-R-S1˙0˙0¨V000˙0¨#0¨16077` | box | 0 | 2119320 | 2119321 | -0.0 | 0.0 |
| T-R-S2 | `$PART_S16_T-R-S2˙0˙0¨V000˙0¨#0¨16078` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-R-S3 | `$PART_S16_T-R-S3˙0˙0¨V000˙0¨#0¨16079` | box | 0 | 2119320 | 2119307 | 0.001 | 0.0 |
| T-R-S4 | `$PART_S16_T-R-S4˙0˙0¨V000˙0¨#0¨16080` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-R-S5 | `$PART_S16_T-R-S5˙0˙0¨V000˙0¨#0¨16081` | box | 0 | 2119320 | 2119335 | -0.001 | 0.0 |
| T-R-BACK | `$PART_S16_T-R-BACK˙0˙0¨0000˙0¨#0¨16082` | extrude_y/bulge | 0 | 6228450 | 6228438 | 0.0 | 0.0 |
| T-R-SERVICE | `$PART_S16_T-R-SERVICE˙0˙0¨VVVV˙0¨#0¨16083` | box | 0 | 1120560 | 1120558 | 0.0 | 0.0 |
| T-DOOR-L | `$PART_S16_T-DOOR-L˙0˙0¨VVVV˙0¨#0¨16084` | extrude_y/bulge | 2 | 5495681 | 5495615 | 0.001 | 0.0 |
| T-DOOR-R | `$PART_S16_T-DOOR-R˙0˙0¨VVVV˙0¨#0¨16085` | extrude_y/bulge | 0 | 16912315 | 16912284 | 0.0 | 0.0 |
| TEXTILE | `$PART_S16_TEXTILE˙0˙0¨KKKK˙0¨#0¨16086` | extrude_y/bulge | 0 | 6463974 | 6463942 | 0.0 | 0.0 |
| BG-1 | `$PART_S16_BG-1˙0˙0¨0000˙0¨#0¨16087` | box | 0 | 33157735 | 33157734 | 0.0 | 0.0 |
| BG-2 | `$PART_S16_BG-2˙0˙0¨0000˙0¨#0¨16088` | box | 0 | 27781358 | 27781363 | -0.0 | 0.0 |
| BG-3 | `$PART_S16_BG-3˙0˙0¨0000˙0¨#0¨16089` | box | 0 | 27781358 | 27781363 | -0.0 | 0.0 |
| BG-4 | `$PART_S16_BG-4˙0˙0¨0000˙0¨#0¨16090` | box | 0 | 27720030 | 27720030 | -0.0 | 0.0 |
| BATTEN-1 | `$PART_S16_BATTEN-1˙0˙0¨0000˙0¨#0¨16091` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-2 | `$PART_S16_BATTEN-2˙0˙0¨0000˙0¨#0¨16092` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-3 | `$PART_S16_BATTEN-3˙0˙0¨0000˙0¨#0¨16093` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-4 | `$PART_S16_BATTEN-4˙0˙0¨0000˙0¨#0¨16094` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| BATTEN-5 | `$PART_S16_BATTEN-5˙0˙0¨0000˙0¨#0¨16095` | box | 0 | 715200 | 715199 | 0.0 | 0.0 |
| CURVE-T-TOP | `$PART_S16_CURVE-T-TOP˙0˙0¨FFFF˙0¨#0¨16096` | extrude_y/bulge | 0 | 5798408 | 5797676 | 0.013 | 0.0 |
| FRAME-T-TOP | `$PART_S16_FRAME-T-TOP˙0˙0¨FFFF˙0¨#0¨16097` | extrude_y/bulge | 0 | 309707 | 309670 | 0.012 | 0.0 |
| CURVE-T-BOT | `$PART_S16_CURVE-T-BOT˙0˙0¨FFF0˙0¨#0¨16098` | extrude_y/bulge | 0 | 5537914 | 5537559 | 0.006 | 0.0 |
| FRAME-T-BOT | `$PART_S16_FRAME-T-BOT˙0˙0¨FFFF˙0¨#0¨16099` | extrude_y/bulge | 0 | 295794 | 295775 | 0.006 | 0.0 |
| FRAME-T-L | `$PART_S16_FRAME-T-L˙0˙0¨FF00˙0¨#0¨16100` | box | 0 | 818100 | 818100 | -0.0 | 0.0 |
| FRAME-T-R | `$PART_S16_FRAME-T-R˙0˙0¨FF00˙0¨#0¨16101` | box | 0 | 714420 | 714421 | -0.0 | 0.0 |
| FRAME-T-MID | `$PART_S16_FRAME-T-MID˙0˙0¨FFF0˙0¨#0¨16102` | box | 0 | 140454 | 140454 | -0.0 | 0.0 |
| FRAME-B-LOW-1 | `$PART_S16_FRAME-B-LOW-1˙0˙0¨FF00˙0¨#0¨16103` | box | 0 | 275400 | 275400 | -0.0 | 0.0 |
| FRAME-B-LOW-2 | `$PART_S16_FRAME-B-LOW-2˙0˙0¨FF00˙0¨#0¨16104` | box | 0 | 333720 | 333720 | -0.0 | 0.0 |
| FRAME-B-LOW-3 | `$PART_S16_FRAME-B-LOW-3˙0˙0¨FF00˙0¨#0¨16105` | box | 0 | 249480 | 249480 | -0.0 | 0.0 |
| FRAME-B-HIGH-1 | `$PART_S16_FRAME-B-HIGH-1˙0˙0¨FF00˙0¨#0¨16106` | box | 0 | 275400 | 275400 | -0.0 | 0.0 |
| FRAME-B-HIGH-2 | `$PART_S16_FRAME-B-HIGH-2˙0˙0¨FF00˙0¨#0¨16107` | box | 0 | 333720 | 333720 | -0.0 | 0.0 |
| FRAME-B-HIGH-3 | `$PART_S16_FRAME-B-HIGH-3˙0˙0¨FF00˙0¨#0¨16108` | box | 0 | 249480 | 249480 | -0.0 | 0.0 |
| FRAME-B-TOP | `$PART_S16_FRAME-B-TOP˙0˙0¨FFFF˙0¨#0¨16109` | extrude_y/bulge | 0 | 36135 | 36120 | 0.04 | 0.0 |
| CURVE-B-TOP | `$PART_S16_CURVE-B-TOP˙0˙0¨FFFF˙0¨#0¨16110` | extrude_y/bulge | 0 | 676521 | 676249 | 0.04 | 0.0 |
| FRAME-B-BOT | `$PART_S16_FRAME-B-BOT˙0˙0¨FFFF˙0¨#0¨16111` | extrude_y/bulge | 0 | 36135 | 36120 | 0.04 | 0.0 |
| CURVE-B-BOT | `$PART_S16_CURVE-B-BOT˙0˙0¨FFFF˙0¨#0¨16112` | extrude_y/bulge | 0 | 676521 | 676249 | 0.04 | 0.0 |
| FRAME-B-R | `$PART_S16_FRAME-B-R˙0˙0¨FF00˙0¨#0¨16113` | box | 0 | 84240 | 84241 | -0.001 | 0.0 |
| TV-SPACER-1 | `$PART_S16_TV-SPACER-1˙0˙0¨FFFF˙0¨#0¨16114` | box | 0 | 5237100 | 5237095 | 0.0 | 0.0 |
| TV-SPACER-2 | `$PART_S16_TV-SPACER-2˙0˙0¨FFFF˙0¨#0¨16115` | box | 0 | 4181400 | 4181429 | -0.001 | 0.0 |
| T-LOW-DIV | `$PART_S16_T-LOW-DIV˙0˙0¨V000˙0¨#0¨16116` | box | 0 | 2438532 | 2438533 | -0.0 | 0.0 |
| T-LOW-BACK | `$PART_S16_T-LOW-BACK˙0˙0¨0000˙0¨#0¨16117` | extrude_y/bulge | 0 | 1271639 | 1271623 | 0.001 | 0.0 |
| T-DOOR-L-BACK | `$PART_S16_T-DOOR-L-BACK˙0˙0¨FFFF˙0¨#0¨16118` | extrude_y | 0 | 10031165 | 10031165 | 0.0 | 0.0 |
| TV-FIELD | `$PART_S16_TV-FIELD˙0˙0¨VVVV˙0¨#0¨16119` | extrude_y | 1 | 67265790 | 67265790 | 0.0 | 0.0 |
| BG-FINISH | `$PART_S16_BG-FINISH˙0˙0¨0000˙0¨#0¨16120` | box | 0 | 6871085 | 6871079 | 0.0 | 0.0 |
| TOP-WASH-COVER | `$PART_S16_TOP-WASH-COVER˙0˙0¨0000˙0¨#0¨16121` | box | 0 | 68568 | 68568 | -0.001 | 0.0 |
| TOP-WASH-BAFFLE | `$PART_S16_TOP-WASH-BAFFLE˙0˙0¨0000˙0¨#0¨16122` | box | 0 | 205704 | 205703 | 0.001 | 0.0 |
| TOP-WASH-HIDDEN-END | `$PART_S16_TOP-WASH-HIDDEN-END˙0˙0¨0000˙0¨#0¨16123` | box | 0 | 240 | 240 | 0.008 | 0.0 |
| UPLIGHT-TRAY | `$PART_S16_UPLIGHT-TRAY˙0˙0¨0000˙0¨#0¨16124` | box | 0 | 68280 | 68275 | 0.007 | 0.0 |
| UPLIGHT-FRONT-VISOR | `$PART_S16_UPLIGHT-FRONT-VISOR˙0˙0¨0000˙0¨#0¨16125` | box | 0 | 34140 | 34138 | 0.007 | 0.0 |
| UPLIGHT-REAR-VISOR | `$PART_S16_UPLIGHT-REAR-VISOR˙0˙0¨0000˙0¨#0¨16126` | box | 0 | 25605 | 25603 | 0.007 | 0.0 |
| DECK-CONTINUOUS-COVER | `$PART_S16_DECK-CONTINUOUS-COVER˙0˙0¨0000˙0¨#0¨16127` | box | 0 | 84096 | 84096 | -0.0 | 0.0 |
| DECK-CONTINUOUS-BAFFLE | `$PART_S16_DECK-CONTINUOUS-BAFFLE˙0˙0¨0000˙0¨#0¨16128` | box | 0 | 178704 | 178704 | -0.0 | 0.0 |
| LOW-INTERNAL-LIGHT-VISOR | `$PART_S16_LOW-INTERNAL-LIGHT-VISOR˙0˙0¨0000˙0¨#0¨16129` | box | 0 | 24480 | 24480 | 0.0 | 0.0 |

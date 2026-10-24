# PDF-kinyerés (reprodukálható)
A bemeneti PDF (`WGR1_meretezett_alaprajzok.pdf`) vevői adatot tartalmaz, ezért **nincs a repóban**. A szkriptek helyi útvonalról olvassák; az útvonalat futtatás előtt át kell írni.
- 18. old. (A-902, 1:50 A3): 1 m = 56,693 pt. Origó: 05.1 Ny-i belső falsík = x 0 (157,3 pt), 05.2 D-i belső falsík = y 0 (626,4 pt). Falkontúr: fekete 0,71 pt vonalak.
- 3. old. (9. emelet, megvalósulási terv, 1:125 A1): 1 m = 22,677 pt. Illesztés a 18. oldalhoz: dx −4,14 m, dy +23,97 m (`p3_align.json`, vonal-korrelációval).
- Kimenet: `p18_falvonalak_m.json`, a falvonalak Blender-koordinátában.

# KEP-004 · Cam_02 nappali–terasz · GEOMETRIAI v2 blokk (2026-10-25 01:35, Claude)

**Státusz: KÉSZ, DE NEM EGYESÍTETT.** Péter döntése (2026-10-25 01:23):
- a Cam_02 geometriai javítása és a szürke bútortömbös referencia „mehet”;
- a kreatív v2 és az újragenerálás áll;
- Astra „Creative Upgrade V3” kiegészítése után Claude ezt a blokkot egy új, verziózott promptba egyesíti;
- generálás csak az egyesített változat jóváhagyása után.

Az eredeti v1 promptok (`05_promptok/KEP004_ChatGPT_Images_v1/`) és képek változatlanok.

**Miért kell:** az első teszt (S01 Cam_02, r1) Gate-auditja FAIL lett:
- a tér szélesebb és mélyebb lett;
- az étkező a nappali bal előterébe került;
- a függeszték nem létező mennyezeti ponton lógott.

Részletek: `ai-coordination/results/WSG-20261024-STYLE10-KEP-004_r1.md`.

**Források:**
- Elrendezés: a P902_24A elfogadott méretpróba (`03_blender/geometry_A811_A812/meretproba/terv_elrendezes_A902.json`).
  - U 3,00 × 2,40, nyitott oldala a nyugati TV-blokk felé; befoglaló [4,77; 4,95; 7,17; 7,95].
  - TV-konzol [3,67; 5,15; 4,12; 6,95].
  - A terv 80 × 180-as asztala 0,30 m-rel nyugatra [7,95; 5,37; 8,75; 7,17], 3 + 3 székkel.
- Képtéri helyek: Blenderrel vetítve a Cam_02-re (v2b-1-k11b, sha256 `9875cd57…`): `03_blender/geometry_v2/tomeg_cam02/tomeg_cam02_log_v1.json`.
- Új referenciakép, **1b kép**: `04_renderek/A902_cam02_tomeg_v1/A902_Cam02_tomeg_P902_24A_v1.png`.
  - A beállítás azonos az 1. alapképével: a bútor nélküli ellenőrző render átlagos eltérése 0,008/255, a legnagyobb 1/255.

**Stílusfüggő rész az egyesítéskor:**
- a kanapé valós alakja (U, vagy L az U-zónán belül), a TV-szekrény szélessége (pl. KI-L/BN-L W240) és az asztal mérete (pl. Toni 200 × 90, Anouk 180 × 90);
- ha a V3 más elrendezést kér, a tömbképet a szkript paramétereivel újrarenderelem, és a vetített helyeket újraszámolom.

**C1 Zenit és C2 Lake Forest** (kalibráció): ezek az eredeti koncepciók déli, WC-tömb előtti TV-falát követik. Erre a blokk **nem** érvényes; ott külön tömbkép kell, ha Péter kéri.

---

## A promptba kerülő szöveg (angol, a v1 prompt „RUN NOTES” része elé)

```
=== GEOMETRY v2 – Cam_02 frame layout (Claude, 2026-10-25; computed from the v2b-1-k11b model and the accepted layout P902_24A) ===
Image 1b is a grey massing render from exactly the same camera as image 1. It shows only WHERE the furniture stands – it is not a style, colour or material reference.
- Room shell: copy image 1 exactly – the same long left wall and corner position (about 47 % from the left edge), the same glass wall and sill line (the sill reaches the right frame edge at about 91 % of the image height), the same railing segment in front of the left glass pane and the same plain ceiling. Do not widen or deepen the room and do not move the glass wall back.
- TV wall = the long left wall (factory block, sockets D16/D17, antenna G08): the TV hangs at about 18–37 % of the image width and 39–57 % of the height, above a low media unit at about 16–41 % / 60–78 %.
- Sofa zone (U 3.00 × 2.40 m, accepted layout P902_24A): in the centre foreground, seen from BEHIND – its back faces the camera and the dining area, its open side faces the TV on the left. The near back runs across the lower centre (about 25–83 % of the width) and is cut by the bottom edge; the north arm reaches towards the glass (about 46–69 %). An L-shaped sofa stands inside the same zone, also with its back to the camera.
- Dining: only the west long side of the table and the backs of the three west-side chairs enter the frame, at the lower right (from about 67 % of the width to the right edge, below about 70 % of the height); the rest of the table and the east-side chairs are outside the frame to the right.
- Ceiling: the dining pendant point ML04 is outside the frame, so no pendant over the dining table is visible. The living point ML05 is at about 44 % of the width at the top edge; a living pendant may hang only there, and only if the style block specifies one. No other ceiling fixtures, cords or tracks.
- Nothing else stands in the room: no coffee table, side table, floor or table lamp, sideboard or extra seating unless the style block lists it with its dimensions. Small accessories only on the listed pieces.
```

**Csatolási sorrend a v2-ben:** 1. kép (alap), **1b (tömbkép)**, majd a 2., 2b., 2c. kép és a termékfotók, mint a v1-ben.

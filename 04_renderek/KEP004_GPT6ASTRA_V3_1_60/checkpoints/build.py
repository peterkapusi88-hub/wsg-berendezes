import os, shutil, hashlib, json
A='/home/claude/astra'; I='/home/claude/integ'; OUT='/mnt/user-data/outputs/WSG_ASTRA_V3_1_RENDEREK'
SRC_SHA='2bef09ae6081b5bafb86bc876ef8410be44bb567'
PD='05_promptok/KEP004_GPT6ASTRA_V3_1_r1/20_PROMPTOK/'
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
F080=A+'/08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg'
F045=A+'/08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg'
F046=A+'/08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-046_nappali_eloter_fele.jpg'
F056=A+'/08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg'
F077=A+'/08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg'
F064=A+'/08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg'
PANO=A+'/02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0_videobol.jpg'
SOMAR=OUT+'/pilot_S01/refs/P_Somar_L00148FA05_termekfoto_kivagas.jpg'
B02='/home/claude/work/cam02_KORR.png'
B12=I+'/04_renderek/A902_cam12_v3_korrekcio/A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png'
B03=I+'/04_renderek/A902_cam03_bibo_u_ellenorzes/A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_KORR_semleges.png'
B04=A+'/04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png'
B11=A+'/04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png'
B10=A+'/04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png'

FLOOR_ROLE="real site photo of the EXISTING floor and skirting in this apartment – cool grey-brown oak-effect planks with visible grain and knots, matching grey-brown skirting. Material and colour reference ONLY (not a camera, not a layout). The floor in the result must match this: not light oak, not honey/warm oak, not whitened, not dark-stained, not replaced."

COMMON_FORBID="any new wall, partition, column, beam, bulkhead, niche, room or opening; moving, resizing, removing or adding doors, windows or glazing; raising or lowering the 2.90 m white ceiling or adding coves, recessed spots or new light points; changing the floor level; rotating, re-aiming, raising, zooming or re-cropping the camera to show something more attractive; showing anything that this camera cannot see"

def hdr(c):
    L=[f"WSG A-902 · GPT-6 ASTRA V3.1 · {c['style']} · {c['cam']} · CAMERA-LOCKED CONCEPT TEST (2026-10-25)",
       "STATUS: CONCEPT – NOT VALIDATED (KONCEPCIÓ – NEM VALIDÁLT)","",
       "Please generate exactly ONE image. Read the GEOMETRY LOCK first. Image 1 and the GEOMETRY LOCK override anything in the creative brief that follows; the creative brief decides everything else (furniture, wall designs, materials, objects, light).","",
       f"IMAGE ID: {c['id']}",
       f"SOURCE VERSION: GPT6ASTRA-V3.1 (branch competition/gpt6astra-v3-1-20261025 @ {SRC_SHA}), file {PD}{c['id']}.prompt.md",
       "",f"ATTACHED IMAGES AND THEIR ROLES (in this order: {', '.join('image '+str(i+1) for i in range(len(c['att'])))})"]
    for i,(path,name,role) in enumerate(c['att']):
        L.append(f"- Image {i+1} ({name}): {role}")
    L+=["","GEOMETRY LOCK (mandatory)"]
    L+=c['lock']
    L+=["","RUN NOTES – how to read the creative brief for THIS camera (integrator clarifications; the brief itself is unchanged)"]
    L+=c['notes']
    L+=["",f"CREATIVE BRIEF – GPT-6 Astra V3.1, {c['id']}, complete and verbatim (source: competition/gpt6astra-v3-1-20261025 @ {SRC_SHA}, {PD}{c['id']}.prompt.md):",""]
    return "\n".join(L)

CAMS=[
dict(nr='01',cam='Cam_02',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A',
 att=[(B02,'01_image1_A902_Cam02_KORR_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty apartment shell from the exact camera of this view (Cam_02). MANDATORY camera and geometry reference: walls, wall corner, glazing, frames, terrace levels, railing, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. It is deliberately neutral: white = existing white walls and ceiling; the flat grey floor tone is NOT the material (see image 2); the pale exterior is only a placeholder for the real view (see images 3–4)."),
      (F080,'02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR_ROLE),
      (F045,'03_image3_A902_ME-BAL-045_nappali_terasz_fele.jpg',"real site photo of this living room taken from a DIFFERENT position, looking towards the terrace glazing: real white window frames, the terrace beyond, real wall and ceiling surfaces. Surfaces and exterior only – do NOT copy its camera, framing or the ladder/cables/construction clutter."),
      (PANO,'04_image4_A902_terasz_panorama_v0_videobol.jpg',"real panorama of THIS terrace and its view, stitched from an iPhone video (strongly distorted, black borders are empty). Content reference ONLY for what is outside: light-grey terrace tiles, the higher dark WPC deck with steps, the planted green roof, the anthracite vertical-bar railing, the real city roofs and the Buda hills. Do not copy its distortion, its black borders or its viewpoint.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera standing near the north-east corner of the living room at 1.55 m eye height, 20 mm lens, looking north-west. Verticals stay vertical. Same landscape 16:10 framing as image 1. No rotation towards the TV wall, no frontal view of the TV wall, no zoom, no crop, no wider view.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, measured from the Blender projection of this camera):",
  "   a) 0–47 %: the long TV wall W01, seen OBLIQUELY and receding from the left edge to the room corner. Its floor line rises from about 82 % image height at the left edge to about 65 % at the corner; its ceiling line falls from the top-left corner to about 21 % at the corner. The south end of W01 lies just beyond the left edge.",
  "   b) the centre of the TV screen bay on W01 sits at about 31 % across and 48 % down (1.20 m above the floor).",
  "   c) about 47–48 %: the vertical inner corner between W01 and the north wall.",
  "   d) 48–52 %: the short white north-wall pier between the corner and the glazing.",
  "   e) 52–100 %: the terrace glazing (full-height sliding glass wall, white inner frames): its west frame edge at about 52 %, glass head at about 25 % down, one vertical mullion at about 69–70 %, the next mullion at the right edge. Through it, the terrace exactly as in image 1: light-grey tiles about 15 cm below the interior floor, the separate higher dark WPC deck with its steps on the right, the green planted roof and the anthracite vertical-bar railing, then the real view.",
  "   f) top edge at about 44 % across: the ML05 living-room ceiling point; its fitting may just touch the top edge.",
  "   g) lower-right corner only (from about 86 % across and 85 % down): the western long edge of the dining table with its chairs. Nothing more of the dining zone.",
  "3. Outside this frame (behind or beside the camera) and therefore NOT shown: walls W02, W03, W07, the grey 05.3 door, the kitchen, and the ML04 dining pendant (the Somar pendant hangs outside the upper-right edge – do not draw it).",
  "4. Furniture positions (from the creative brief, placed into the locked view): the sofa group in the middle third with its back towards the camera and the dining zone, long seat run north–south, opening towards the TV wall; the free strip along the glazing stays clear; the rug under the group; the TV-wall composition fixed flat to W01 inside 0–47 %.",
  f"5. Forbidden: {COMMON_FORBID}; a single flat terrace; a different, generic or invented city view (no Parliament, no Danube, no skyscrapers, no sea).",
  "6. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no watermark, no collage.",
  "7. If anything in the creative brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- \"The television wall is the visual protagonist\" means design emphasis and light, NOT camera direction: W01 stays oblique in the left 47 % exactly as in image 1.",
  "- The WALL CONTINUITY paragraph (W02 print, W07, W03, 05.3 door) describes walls outside this frame; the brief itself says reverse-facing walls are not rotated in. Draw none of them here.",
  "- The dining pendant ML04 (Somar) is outside this frame; only the table's west edge with chairs appears in the lower right.",
  "- Blue hour: the exterior stays a readable deep-blue dusk with the real roofs and hills as silhouettes; terrace tiles, WPC deck, steps and railing stay readable."]),
dict(nr='02',cam='Cam_12',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_1_nappali-hero_Cam_12_A',
 att=[(B12,'01_image1_A902_Cam12v3_KORR_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty apartment shell from the exact camera of this view (Cam_12 v3). MANDATORY camera and geometry reference: walls, wall steps, door, parapet, opening, corridor, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. Deliberately neutral: white = existing white walls and ceiling; mid-grey = the existing light-grey 05.3 door leaf; darker grey = its frame; the flat floor tone is NOT the material (see image 2). There is no kitchen yet in reality – the kitchen comes from the creative brief, inside the fixed shell."),
      (F080,'02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR_ROLE),
      (F046,'03_image3_A902_ME-BAL-046_nappali_eloter_fele.jpg',"real site photo taken from a DIFFERENT position (looking the other way) – only to check the existing surfaces: white walls, grey skirting, light-grey doors with darker frames, ceiling, floor. Do NOT copy its camera, framing, layout or the construction clutter."),
      (SOMAR,'04_image4_Kave_Home_Somar_L00148FA05_termekfoto.jpg',"product photo of the specified dining pendant, Kave Home Somar Ø76 cm, white (L00148FA05). Product identity only (silhouette, ribs, white synthetic-fibre shade). Ignore its background, the second lamp and the dark wood – they are NOT part of the design.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera in the north-west corner of the living room at 1.60 m, 22 mm lens, looking diagonally south-east, slight downward shift. Verticals stay vertical. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–1 %: the narrow white side of the shaft wall at the very left edge.",
  "   b) 0–12 %: the existing light-grey 05.3 door with its darker grey frame and black handle (its right jamb at about 12 %), head at 2.10 m (about 33 % down), and above it the plain wall band up to the ceiling. The door stays closed, same size, same place.",
  "   c) 12–23 %: the 1.00 m dining-side wall section W03-a, receding.",
  "   d) about 23 %: a 0.20 m step back in the wall (vertical corner line).",
  "   e) 24–45 %: the K-stub and the long east kitchen wall, running away from the camera. The kitchen is open to the dining area; no wall between them.",
  "   f) 45–56 %: the free end of the low, about 0.85 m high parapet on the kitchen's west side, running away from the camera; above it the opening under a 2.10 m lintel with a white pier, the entrance hall visible through it.",
  "   g) 55–86 %: wall W02 – one solid, full-height wall, 2.10 m wide, 2.90 m high, seen almost frontally; its floor line runs from about 70 % down (left end) to the lower edge (right end); the switch column sits near its left (east) edge.",
  "   h) 86–92 %: the W07 return (side face of the corridor wall) and the narrow pillar behind it.",
  "   i) 92–100 %: the throat of the corridor to the bedrooms, full width.",
  "   j) ML04 dining ceiling point at about 19 % across, 10 % down: the Somar pendant hangs there (shade bottom about 38 % down); the dining table stands below it (table top at about 19 % across, 79 % down).",
  "   k) Ceiling: flat, white, continuous at 2.90 m.",
  "3. Outside this frame: the TV wall, the glass wall and the terrace (behind the camera). Do not show them.",
  "4. Kitchen inside the fixed shell, per the creative brief and the apartment's electrical plan (no new walls): (i) the tall refrigerator tower against W03-a (12–23 %), left of the kitchen, right of the 05.3 door, chalk doors with a graphite side panel, integrated with the K-stub in one flat front grid; (ii) along the receding east kitchen wall (24–45 %) the main run with upper cabinets – sink run; (iii) on the right of the kitchen only a LOW run of base cabinets standing against the kitchen side of the existing ~0.85 m parapet (attached to the parapet – NOT an island, no upper cabinets, nothing rises above the parapet zone); (iv) the far south end closed by tall units. No island, no peninsula, no rear kitchen wall.",
  "5. Furniture: only as named in the creative brief, at realistic sizes; the sofa forms a modest lower foreground (about the bottom 16–23 % of the image, left and centre); the oval dining table lengthwise with six chairs under the pendant, between the camera and the kitchen.",
  f"6. Forbidden: {COMMON_FORBID}; a kitchen island or a kitchen on any other wall; moving, widening or shortening W02; changing the corridor; removing or moving the 05.3 door.",
  "7. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- The W02 ink-on-textile artwork (150 × 220 cm) hangs on W02 (55–86 %) over the smoke-grey paper-effect wallcovering; W07 gets only the thin 2 mm wallcovering; the switch column on W02 keeps a clear border.",
  "- The TV-wall cabinetry described in the brief is behind the camera; it is not transplanted onto W02 (the brief says the same).",
  "- Daylight from the glass wall behind the camera; Hue off."]),
dict(nr='03',cam='Cam_03',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A',
 att=[(B03,'01_image1_A902_Cam03K1_KORR_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty apartment shell from the exact camera of this view (Cam_03 K1). MANDATORY camera and geometry reference: walls, wall stub, column, parapet, opening, lintel, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. Deliberately neutral: white = existing white walls; the flat floor tone is NOT the material (see image 2). There is no kitchen yet in reality – the kitchen comes from the creative brief, inside the fixed shell."),
      (F080,'02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR_ROLE),
      (F056,'03_image3_A902_ME-BAL-056_konyhafal_kiallasok.jpg',"real site photo of the empty kitchen zone from a DIFFERENT position: the real east kitchen wall with its service outlets, the low parapet, the column, white walls, floor. Shell and surfaces only – do NOT copy its camera, framing, ladder or cables."),
      (SOMAR,'04_image4_Kave_Home_Somar_L00148FA05_termekfoto.jpg',"product photo of the specified dining pendant, Kave Home Somar Ø76 cm, white (L00148FA05). Product identity only. Ignore its background, the second lamp and the dark wood – they are NOT part of the design.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera at the north-east edge of the dining zone, 1.50 m, 20 mm lens, looking due south along the kitchen axis, with the locked downward shift. Verticals stay vertical. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–21 %: the near dining-side wall section W03-a on the left, running towards the camera (the grey 05.3 door is just beyond the left edge – not in frame).",
  "   b) 21–32 %: the K-stub wall (the corner block where the kitchen begins).",
  "   c) 32–40 %: the east kitchen wall receding to the far corner at about 40 % (floor corner about 59 % down, ceiling corner about 17 % down).",
  "   d) 40–53 %: the far south end wall of the kitchen (the place of the southern tall-unit wall).",
  "   e) 53–61 %: the full-height white column / wall step at the far west side of the kitchen.",
  "   f) 61–67 %: the low, about 0.85 m high parapet on the kitchen's west side, running towards the camera (its top at about 48 % down far, 54 % down near).",
  "   g) 66–84 %: above and beyond the parapet the opening to the entrance hall under the 2.10 m lintel (lintel band at the top, about 0–22 % down); the hall and its door visible through it.",
  "   h) 84–100 %: the east end of the solid wall W02, seen almost frontally at the right edge.",
  "   i) Right foreground: the edge of the dining table (lower right corner) and, at about 89 % across, the lower part of the Somar pendant at ML04 entering from the top edge (cut by the frame).",
  "3. Outside this frame: the TV wall, the terrace and the living room. Do not show them.",
  "4. Kitchen inside the fixed shell (creative brief + the apartment's electrical plan; no new walls): (i) LEFT/EAST run along the receding east kitchen wall (32–40 % zone, front edge at about 42–45 % across): base cabinets with worktop and the sink, UPPER cabinets above, the under-cabinet light line; (ii) RIGHT/WEST run: only LOW base cabinets with worktop against the kitchen side of the ~0.85 m parapet (front edge at about 54–56 % across), the hob in this run; no upper cabinets and nothing tall on the parapet side; (iii) the far south end wall (40–53 %) closed by the tall-unit wall (oven/microwave column); (iv) the tall refrigerator tower D13 stands against W03-a on the near left, chalk doors and graphite side panel, integrated with the K-stub in one flat front grid; (v) the open aisle between the two runs about 85–86 cm, floor visible down to the far wall. No island, no peninsula, no U-turn of the worktop along the south wall, rows not swapped.",
  f"5. Forbidden: {COMMON_FORBID}; a kitchen island; swapping the two runs or the sink and hob sides; rotating, enlarging or extending the kitchen.",
  "6. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- The FURNITURE and PLAN paragraphs list the whole living-dining set for consistency; in this frame only the dining table edge, chairs and the Somar pendant appear (right foreground). The sofa and the rug are outside the frame.",
  "- ADJOINING WALLS: only W02 (right edge, 84–100 %) is visible; W07 and the W03 dry-wall treatment above the 05.3 door are outside or at the frame edge.",
  "- Daylight; ML04 dim or off; under-cabinet strip as restrained task light."]),
dict(nr='04',cam='Cam_04',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_3_master_Cam_04_A',
 att=[(B04,'01_image1_A902_Cam04_master_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty master bedroom 05.1 from the exact camera of this view (Cam_04). MANDATORY camera and geometry reference. It is very pale: read it as two white wall planes meeting a narrow white pillar block in the middle, a white ceiling and a grey floor. Nothing in image 1 may be moved, added or removed. The flat floor tone is NOT the material (see image 2)."),
      (F080,'02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR_ROLE)],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – camera standing in the south-west part of the bedroom, close to the west glass wall, at 1.50 m, 20 mm lens, looking north-east, tilted slightly down. Verticals stay vertical. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–38 %: the back wall of the existing NORTH NICHE (3.02 m wide, 0.90 m deep, full height). In this design the WHOLE niche is filled by the north wardrobe: its fronts stand in the plane of the pillar's front face, so the wardrobe front occupies 0–43 % of the frame width, floor to ceiling (its top edge about 9 % down at its right end).",
  "   b) 43–46 %: the narrow front face of the white pillar, beside the wardrobe.",
  "   c) 46–48 %: a short white return to the room corner; the vertical inner corner at about 48 % (floor about 64 % down, ceiling about 11 % down).",
  "   d) 48–100 %: the EAST wall = the headboard wall, receding to the right; its south end is beyond the right edge.",
  "   e) The bed: head against the east wall, the headboard spanning about 54–78 % across; the bed (180 × 202 cm) runs from the east wall towards the camera-left, its foot corners low in the frame at about 30 % across / 72 % down and 52 % across / 96 % down. The 270 cm headboard panel on the east wall spans about 50–88 % across. Bedside blocks at both sides of the bed against the east wall (about 50–54 % and 78–86 % across).",
  "   f) Ceiling: flat, white, uninterrupted at 2.90 m.",
  "3. NOT in this frame: the west glass wall, its curtains and the balcony (behind and left of the camera); the south wardrobe strip and the room door (behind and right of the camera). There is NO window, NO glass, NO balcony and NO door anywhere in this picture.",
  f"4. Forbidden: {COMMON_FORBID}; turning the bed or putting it on another wall; moving the wardrobe out of the niche or onto another wall; any glass wall or window on the left; enlarging the room.",
  "5. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- \"The south wardrobe strip ... retains its actual visibility at the edge of the locked frame\": its actual visibility from this camera is NONE – it is outside the frame. Do not draw it.",
  "- The curtain track above the 3.64 m glazing belongs to the west wall outside the frame; no curtain or window appears here.",
  "- \"The complete north wardrobe wall visibly closing its existing niche\" = the six-front wardrobe filling 0–43 % on the left.",
  "- Evening light only from the named Hue layers (headboard seam, two Hue Go lamps, restrained ceiling fitting)."]),
dict(nr='05',cam='Cam_11',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_3_master_Cam_11_A',
 att=[(B11,'01_image1_A902_Cam11_master_panorama_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty master bedroom 05.1 from the exact camera of this view (Cam_11). MANDATORY camera and geometry reference: the 3.64 m glass wall with exactly three white-framed fields, the balcony and its railing, walls, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. The pale exterior is only a placeholder for the real view (see image 3); the flat floor tone is NOT the material (see image 2)."),
      (F080,'02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR_ROLE),
      (F077,'03_image3_A902_ME-BAL-077_master_uvegfal_kilatas.jpg',"real site photo of THIS bedroom's glass wall from a DIFFERENT position: the real white frames, the balcony with light-grey tiles and black vertical railing, the brick facade return on the right, and the REAL view (city roofs, church spire, Buda hills). Use it for the glass wall's appearance and the exact exterior view only – do NOT copy its camera or framing.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera at seated eye height 1.20 m on the bed, 20 mm lens, looking due west at the glass wall. Verticals stay vertical. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–13 %: the white south wall at the left edge (the south wardrobe stands here, entering from the left edge).",
  "   b) 13–21 %: the white wall pier left of the glazing.",
  "   c) 21–79 %: the 3.64 m glass wall with EXACTLY THREE white-framed fields: the opening sash 21–35 %, the narrow middle field 35–50 %, the wide fixed field 50–79 %; glass head at about 15 % down, sill at floor level about 81 % down. Same width, same divisions, same height as image 1.",
  "   d) 79–84 %: the white wall pier right of the glazing; 84–100 %: the north wardrobe front at the right edge.",
  "   e) Above the glass: the 33 cm white wall strip up to the ceiling (about 3–15 % down) carrying the wall-mounted curtain track; curtains stacked at the sides, the three fields stay clear.",
  "   f) Beyond the glass: the balcony about 15 cm lower, light-grey tiles, black vertical-bar railing, the brick facade return at the right; then the REAL view of image 3.",
  "   g) Lower foreground: the foot of the bed across about 30–90 % of the width at the very bottom (top of the bedding about 87 % down).",
  "3. NOT in this frame: the headboard and the east wall (behind the camera). Do not show them.",
  f"4. Forbidden: {COMMON_FORBID}; a narrower, wider, taller or differently divided glass wall; a fourth glass field; a different balcony or railing; a generic or invented view.",
  "5. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- The headboard description is for design consistency; the headboard is behind the camera and invisible.",
  "- Daylight; all Hue layers off or barely perceptible."]),
dict(nr='06',cam='Cam_10',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A',
 att=[(B10,'01_image1_A902_Cam10_furdo06-2_semleges_blender.png',"Blender render 1600 × 1000 of the real, windowless bathroom 06.2 as built, from the exact camera of this view (Cam_10). MANDATORY camera and geometry reference: the L-shaped room, the existing tiles, the hexagon relief wall, the black Grohe fittings, the existing white basin, the shower kerb and linear drain, the shaft block, ceiling and floor lines. Nothing in image 1 may be moved, added or removed; only the new items named in the brief are added."),
      (F064,'02_image2_A902_ME-BAL-064_zuhany_mosdo.jpg',"real site photo of this bathroom from a DIFFERENT position: the real Geostone Grigio 60 × 60 tiles, the Esagonetta hexagon relief, the black fittings, the existing white basin, the kerb and drain. Materials and existing fittings only – do NOT copy its camera, framing, the bare wires or the temporary bulb.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – camera in the bathroom doorway at 1.50 m, 16 mm lens, looking east, tilted slightly down. Verticals stay vertical. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–20 %: the left (north) wall = the shower back wall with the Esagonetta hexagon relief, the black overhead shower on its arm, the concealed mixer and the handset – all exactly where image 1 shows them.",
  "   b) 20–67 %: the far (east) wall in 60 × 60 Geostone Grigio tiles; the existing white Geberit basin in the centre at about 50 % across (rim about 59–60 % down) with its black tap; the floor–wall line at about 87 % down.",
  "   c) 67–100 %: the shaft block projecting into the room on the right.",
  "   d) Floor: the shower zone on the left; the existing kerb line meets the far wall at about 38 % across and runs towards the camera, out of the frame at the lower left; the linear drain lies inside the shower along the far wall (about 20–37 %).",
  "3. New items from the creative brief, placed into this locked view: (i) the 100 cm fixed clear glass screen stands on the existing kerb line, starting at the far wall at about 38 % across and running towards the camera (its near end leaves the frame at the lower left, the walk-in entry stays open); 200 cm high – at the far wall its top is about 16 % down; (ii) the continuous integrated vanity along the far wall from the glass (about 38 %) to the shaft block (about 68 %): counter top about 60 % down at the wall, front edge about 68 % down; the existing basin stays exactly in place (centre about 50 %) nested into the counter; (iii) the mirror with its offset shallow storage wing on the far wall above the vanity, dry side, outside the shower; (iv) the two hidden light layers and the named objects.",
  "4. NOT in this frame: the WC niche (behind the right edge), the door and the towel radiator (behind the camera).",
  f"5. Forbidden: {COMMON_FORBID}; any window, daylight or exterior view; a glass door or full shower enclosure; moving or replacing the basin, the fittings, the drain or the kerb; new or different tiles; pulling the WC into view.",
  "6. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- The REALITY AND MATERIALS paragraph is shared text for all rooms: in this bathroom the floor is the EXISTING grey 60 × 60 Geostone tile (not the oak floor), and there is NO window and NO external view.",
  "- Artificial light only (3500 K facial/general, 2700 K concealed layers); grey tiles readable, no blown highlights."]),
]
if __name__=='__main__':
    log=[]
    for c in CAMS:
        pf=A+'/'+PD+c['id']+'.prompt.md'; prompt=open(pf,encoding='utf-8').read().rstrip('\n')
        assert prompt.startswith('=== BEGIN PROMPT '+c['id']) and prompt.endswith('=== END PROMPT '+c['id']+' ===')
        msg=hdr(c)+prompt+"\n"
        mp=f"{OUT}/prompts_sent/{c['nr']}_{c['id']}__ASTRA_V3_1__v1.txt"; open(mp,'w',encoding='utf-8').write(msg)
        rd=f"{OUT}/pilot_S01/refs/{c['cam']}"; os.makedirs(rd,exist_ok=True)
        att=[]
        for i,(src,name,role) in enumerate(c['att']):
            shutil.copyfile(src,rd+'/'+name); att.append(dict(sorrend=i+1,fajl=name,forras=src.replace('/home/claude/astra/','astra:').replace('/home/claude/integ/','integ:').replace('/home/claude/work/','mac:WSG_CAM02_KORREKCIO/vegleges/ (cam02_KORR.png = ').replace(OUT+'/',''),sha256=sha(src),szerep=role[:120]))
        log.append(dict(nr=c['nr'],kep_id=c['id'],kamera=c['cam'],prompt_forras=f"{PD}{c['id']}.prompt.md",prompt_sha256=sha(pf),prompt_chars=len(prompt),uzenet=mp.replace(OUT+'/',''),uzenet_chars=len(msg),uzenet_sha256=hashlib.sha256(msg.encode()).hexdigest(),csatolmanyok=att))
    json.dump(log,open(OUT+'/attachments_log/pilot_S01_csatolmanyok.json','w'),ensure_ascii=False,indent=1)
    for l in log: print(l['nr'],l['kamera'],l['prompt_chars'],l['uzenet_chars'],len(l['csatolmanyok']))

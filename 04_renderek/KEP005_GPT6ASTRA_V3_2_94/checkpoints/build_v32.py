"""Astra V3.2 – 47 prompt × A (eredeti) / B (profi fotóalapú) üzenet- és csatolmánycsomagok.
Astra-prompt szó szerint (BEGIN..END); csak a technikai fejléc (képszerepek, GEOMETRY LOCK, RUN NOTES) a mi részünk.
A: V3.1 run54-elv (FLOOR3 + ME-BAL-080), a KÖTELEZŐ eredeti Cam_11 (nem Cam_11c).
B: V3.1 run2-elv (FLOOR4 + KZS_3695, Cam_02 LEPCSO15 + STEP2, MAT/BATH)."""
import copy, os, shutil, hashlib, json, sys, csv
from PIL import Image
sys.path.insert(0,'/home/claude/work/build'); import build as B
FLOOR3=("real site photo of the EXISTING floor and skirting in this apartment – oak-effect planks in a cool grey-brown, photographed in cool daylight. Material and colour reference ONLY (not a camera, not a layout). "
        "In the result the floor must read as this same cool grey-brown oak with visible grain and knots: under warm evening light it may look slightly warmer, but never honey, orange-brown, reddish, whitened or dark-stained, and never replaced by another floor.")
sha=B.sha
V='/home/claude/v32'; PR='05_promptok/KEP005_GPT6ASTRA_V3_2_r1/'
SRC_BR='competition/gpt6astra-v3-2-five-new-20261025'; SRC_SHA='973865596180c8549a5765ac5c8beb38f49a047d'
OUT='/mnt/user-data/outputs/WSG_ASTRA_V3_2_RENDEREK'; UP='/home/claude/work/upload/v32'
W='/home/claude/work/v32'; FOTO=W+'/foto'
REF='/mnt/user-data/uploads/Downloads/WSG_ASTRA_V3_1_RENDEREK/v32_refs/'
V31=B.OUT
BRISIA=V31+'/pilot_S01/refs/P_Brisia50_L00152CR05_termekfoto_kivagas.jpg'; SOMAR=B.SOMAR
PADLO='/home/claude/work/padlo_profi_3695.jpg'; B02S='/home/claude/work/cam02_LEPCSO15.png'
C11C='/home/claude/work/cam11c_base.png'
F077=B.F077; F080=B.F080; F064=B.F064; B10=B.B10
STY={'S11':'S11 Zuma Inspired Luxury','S12':'S12 Modern Organic','S13':'S13 Westside Grand Continuum','S14':'S14 Modern White Luxury','S15':'S15 Authentic Japanese Modern'}
PEND={'S11':'Kave Home Brisia Ø50','S12':'Kave Home Somar Ø76','S13':'Kave Home Novae Ø40','S14':'Kave Home Novae Ø40','S15':'Kave Home Somar Ø76'}
PPHOTO={'S11':(BRISIA,'Kave_Home_Brisia50_L00152CR05_termekfoto.jpg',"product photo of the specified dining pendant, Kave Home Brisia Ø50 cm (L00152CR05): single frosted-glass globe with brushed-brass suspension. Product identity only (silhouette, globe, brass canopy and fitting); ignore the background."),
        'S12':(SOMAR,'Kave_Home_Somar_L00148FA05_termekfoto.jpg',"product photo of the specified dining pendant, Kave Home Somar Ø76 cm, white (L00148FA05). Product identity only (silhouette, ribs, white synthetic-fibre shade). Ignore its background, the second lamp and the dark wood – they are NOT part of the design."),
        'S15':(SOMAR,'Kave_Home_Somar_L00148FA05_termekfoto.jpg',"product photo of the specified dining pendant, Kave Home Somar Ø76 cm, white (L00148FA05). Product identity only (silhouette, ribs, white synthetic-fibre shade). Ignore its background, the second lamp and the dark wood – they are NOT part of the design.")}
# Astra saját képreferenciái (a promptban név szerint hivatkozva)
STYLEREF={'S12':[(REF+'IMG_2589.jpg','IMG_2589_tulajdonosi_montazs.jpg',"the owner's mood montage IMG_2589 named in the creative brief (a phone screenshot). STYLE MOOD ONLY: rough mineral surfaces, pillowy pale upholstery, a few dark reflective objects, large quiet wall fields with hidden light. Do NOT copy its architecture (cave forms, double height, giant chandelier, monumental plants), its camera or any of its text, icons or interface overlays.")],
          'S13':[(REF+'KZS_3896-336_lobby_1600.jpg','KZS_3896_WSG_lobby.jpg',"real photo of the Westside Grand building lobby named in the creative brief: warm-grey timber planes, dark mineral base, pale luminous frames, round mirror. MATERIAL GRAMMAR ONLY – not this apartment, not a camera, not a layout; no letterboxes, no reception desk, no logo, no lobby floor."),
                 (REF+'KZS_3914-318_lobby_1600.jpg','KZS_3914_WSG_lobby_kor.jpg',"second real lobby photo: the vertical timber rhythm, the circular cut-out detail and the luminous framed plane. MATERIAL GRAMMAR ONLY – not this apartment, not a camera, not a layout; no letterboxes, no logo.")]}
FLOOR4=("real professional photo of the EXISTING floor in this apartment (KZS_3695) – a cool light-to-mid grey oak-effect laminate, long planks, fine straight grain, only few small knots, low contrast, matching grey-taupe skirting about 6 cm high. Material and colour reference ONLY (not a camera, not a layout). This exact floor stays: under warm evening light it may look only slightly warmer (a hint of taupe), but it must never read as honey, golden, orange-brown, reddish or dark-stained oak, and never as rustic or heavily knotted oak.")
MAT=("- MATERIALS FIRST (verified on the professional site photos 2026-10-25): light may warm the image, it must not change the materials. Floor = the KZS_3695 colour (cool grey oak effect, at most slightly warmer); skirting grey-taupe, not white, not dark wood; walls pure white wherever the brief assigns no finish; ceiling flat white 2.90 m with no recessed spots, coves or hidden LED lines; interior doors mid-grey with darker grey frame and black handle; white interior window frames; switches and sockets anthracite at their real positions.")
STEP2=("   h) along the full length of the terrace glazing there is a continuous low INTERIOR STEP about 15 cm high and about 25 cm deep, clad in the same grey oak-effect floor; the glass frames sit on it (visible in image 1 as the darker band at the foot of the glass, from the room corner at about 47 % to the right edge). Keep it; do not remove it, do not turn it into a bench, do not put furniture on it.")
BATH=("- EXISTING BATHROOM MATERIALS (verified on professional photo KZS_3598): the large-format stone-look tiles are a NEUTRAL COOL GREY (Geostone Grigio) and must stay grey under warm light, never beige or cream; the shower back wall is a HEXAGONAL 3D relief tile (Esagonetta), never a square mosaic; black Grohe fittings.")
TERR=("- EXISTING TERRACE (verified on the professional photos 2026-10-25): light-grey large-format paving; the dark-brown WPC platforms keep their exact outline, heights and steps; the planted green roof stays planted and untouched; anthracite vertical-bar railing; grey-brick facade with dark window frames; the real city skyline (including the cranes visible today) – no invented view, no sea, no river, no new planters.")
MAT2=MAT+" Even where warm lamplight or LED falls on it, the floor stays visibly GREY (at most a faint warm tint) – never honey, golden, orange or reddish brown, also not in the foreground; create warmth with the light sources, textiles and walls, not by recolouring the floor."
SENT_B={'02','08','14','20','26','01','03'}  # 2026-10-26 10:20 előtt elküldött B-csomagok: változatlan MAT
RULES="- Reference rules: 05_promptok/PROMPT_ELVEK_FOTOVALIDALT_A902.md v1 (Claude, 2026-10-25, owner-approved)."

def hdr(c):
    pd=PR+('21_EXTRA_PROMPTOK/' if c['extra'] else '20_PROMPTOK/')
    var={'A':'A – ORIGINAL ASTRA V3.2 (Astra references, original materials brief)','B':'B – PROFESSIONAL-PHOTO-BASED (same Astra design; real site materials and architecture from the professional photos)'}[c['var']]
    L=[f"WSG A-902 · GPT-6 ASTRA V3.2 · {c['style']} · {c['cam']} · VARIANT {var} · CAMERA-LOCKED CONCEPT TEST (2026-10-26)",
       "STATUS: CONCEPT – NOT VALIDATED (KONCEPCIÓ – NEM VALIDÁLT)"+(" · CAMERA CONDITIONAL (proposed, not Blender-validated)" if c.get('cond') else ""),"",
       "Please generate exactly ONE image. Read the GEOMETRY LOCK first. Image 1 and the GEOMETRY LOCK override anything in the creative brief that follows; the creative brief decides everything else (furniture, wall designs, artworks, materials, objects, light).","",
       f"IMAGE ID: {c['id']}",
       f"SOURCE VERSION: GPT6ASTRA-V3.2 (branch {SRC_BR} @ {SRC_SHA[:7]}), file {pd}{c['id']}.prompt.md",
       "",f"ATTACHED IMAGES AND THEIR ROLES (in this order: {', '.join('image '+str(i+1) for i in range(len(c['att'])))})"]
    for i,(path,name,role) in enumerate(c['att']): L.append(f"- Image {i+1} ({name}): {role}")
    L+=["","GEOMETRY LOCK (mandatory)"]+c['lock']
    L+=["","RUN NOTES – how to read the creative brief for THIS camera (integrator clarifications; the brief itself is unchanged)"]+c['notes']
    L+=["",f"CREATIVE BRIEF – GPT-6 Astra V3.2, {c['id']}, complete and verbatim (source: {SRC_BR} @ {SRC_SHA[:7]}, {pd}{c['id']}.prompt.md):",""]
    return "\n".join(L)

CAM={c['cam']:c for c in B.CAMS}
def base(cam,s):
    """V3.1 kamera-lock, V3.2 stílusra általánosítva (run54 gen logika, de Cam_11 = eredeti)."""
    c=copy.deepcopy(CAM[cam]); pend=PEND[s]
    c['att']=[(p,n,FLOOR3 if '080_parketta' in n else r) for p,n,r in c['att'] if 'Somar' not in n]
    if cam in ('Cam_12','Cam_03') and s in PPHOTO:
        p,n,r=PPHOTO[s]; c['att'].append((p,f'0{len(c["att"])+1}_image{len(c["att"])+1}_{n}',r))
    L=c['lock']; N=c['notes']
    if cam=='Cam_02':
        L[:]=[x.replace('(the Somar pendant hangs outside the upper-right edge – do not draw it)','(the dining pendant hangs outside the upper-right edge – do not draw it)') for x in L]
        N[:]=[x.replace('The dining pendant ML04 (Somar)',f'The dining pendant ML04 ({pend})') for x in N]
        N[3]="- Light exactly as the LIGHT paragraph of the brief says; the exterior stays readable with the real roofs and hills; terrace tiles, WPC deck, steps and railing stay readable."
        N[1]="- The WALL CONTINUITY paragraph describes walls outside this frame (W02, W07, W03, 05.3 door); reverse-facing walls are not rotated in. Draw none of them here."
    if cam=='Cam_12':
        L[:]=[x.replace('the Somar pendant hangs there (shade bottom about 38 % down)',f'the dining pendant named in the brief ({pend}) hangs there at its true size')
               .replace('chalk doors with a graphite side panel','finished as named in the creative brief')
               .replace('the oval dining table lengthwise with six chairs under the pendant','the dining table named in the brief, lengthwise, with its chairs under the pendant') for x in L]
        N[0]="- The W02 treatment named in the creative brief (artwork/relief and its surrounding finish) sits on W02 (55–86 %); W07 receives only what the brief names for it; the switch column on W02 keeps a clear border."
        N[2]="- Light exactly as the LIGHT paragraph of the brief says (daylight from the glass wall behind the camera unless the brief says otherwise)."
    if cam=='Cam_03':
        L[:]=[x.replace('the lower part of the Somar pendant at ML04',f'the lower part of the dining pendant ({pend}) at ML04')
               .replace('chalk doors and graphite side panel','finished as named in the creative brief') for x in L]
        N[0]="- The FURNITURE and PLAN paragraphs list the whole living-dining set for consistency; in this frame only the dining table edge, chairs and the ML04 pendant appear (right foreground). The sofa and the rug are outside the frame."
        N[2]="- Light exactly as the LIGHT paragraph of the brief says; under-cabinet strip only as restrained task light."
    if cam=='Cam_04':
        L[:]=[x.replace('The 270 cm headboard panel on the east wall spans about 50–88 % across. Bedside blocks at both sides of the bed against the east wall (about 50–54 % and 78–86 % across).',
                        'The headboard composition named in the brief sits on the east wall centred on the bed (roughly 50–88 % across); the bedside pieces named in the brief stand at both sides of the bed against the east wall.') for x in L]
        N[-1]="- Light only from the light sources named in the brief; no new ceiling light points."
    if cam=='Cam_10':
        L[:]=[x.replace('(iii) the mirror with its offset shallow storage wing on the far wall above the vanity','(iii) the mirror and wall storage named in the brief on the far wall above the vanity') for x in L]
    if cam=='Cam_11':
        N.append("- This is the MANDATORY V3.2 Cam_11 (frontal, three white-framed fields) exactly as the CAMERA paragraph of the brief says – not Cam_11c.")
        N[1]="- Light exactly as the LIGHT paragraph of the brief says; the view and the three fields stay readable."
    return c

def to_b(c,cam,photo_native=False):
    att=[]
    for p,n,r in c['att']:
        if '080_parketta' in n: att.append((PADLO,'02_image2_A902_KZS3695_profi_padlo.jpg',FLOOR4))
        elif cam=='Cam_02' and n.startswith('01_image1'): att.append((B02S,'01_image1_A902_Cam02_KORR_LEPCSO15_semleges_blender.png',r.replace('glazing, frames,','glazing, frames, the low interior step at the foot of the glazing,')))
        elif cam=='Cam_10' and '064_zuhany' in n: photo1('3598-634'); att.append((W+'/foto_2400/KZS_3598-634_2400.jpg','02_image2_A902_KZS_3598_furdo_profi_foto.jpg',"real PROFESSIONAL photo of this bathroom as built (KZS_3598), from a DIFFERENT position: the neutral cool-grey Geostone Grigio 60 × 60 tiles, the Esagonetta hexagonal 3D relief on the shower wall, the black Grohe fittings, the existing white basin, the shower floor and linear drain. Materials and existing fittings only – do NOT copy its camera or framing."))
        else: att.append((p,n,r))
    c['att']=att
    if cam=='Cam_02':
        i=[k for k,x in enumerate(c['lock']) if x.strip().startswith('g)')][0]; c['lock'].insert(i+1,STEP2)
    return c

# ---------- fotóhoz kötött (Cam_F) és tervezett (Cam_X) extrák ----------
def photo1(n):
    dst=f'{W}/foto_2400/KZS_{n}_2400.jpg'
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst),exist_ok=True); Image.open(f'{FOTO}/KZS_{n}.jpg').convert('RGB').resize((2400,1602),Image.LANCZOS).save(dst,quality=90)
    return dst
FORB=B.COMMON_FORBID
PHOTO={
 '3659-573':dict(room='living room',interior=True,pend=False,step=True,
   desc="professional photo of the EMPTY living room as built, looking west: the plain wall ahead (with the TV sockets) is W01, the TV wall; the terrace glazing with the low interior step is on the right; the white wall with switches and thermostat on the left.",
   fix=["   a) the plain wall ahead (W01, about 20–50 % across) with its socket group is the TV wall – the TV-wall composition of the brief goes flat on THIS wall only, centred on the real TV socket group;",
        "   b) the terrace glazing on the right (about 53–90 %): the two-part sliding door and the fixed field with white inner frames, the brick reveal, the terrace, WPC steps and railing beyond – unchanged;",
        "   c) the continuous low interior step (about 15 cm) along the foot of the glazing, clad in floor – unchanged, nothing placed on it;",
        "   d) the left wall with its switches and thermostat, the opening at the far left, the ceiling and every socket – unchanged.",
        "Furniture: the sofa stands in the middle ground with its BACK towards the camera and its long seat run across the frame, parallel to the TV wall, facing the TV wall ahead (opening towards W01; the L chaise end towards the glazing side); the rug under it; the free strip along the glazing and the step stay clear; the dining zone is behind the camera."]),
 '3708-524':dict(room='living-dining-kitchen',interior=True,pend=True,step=True,
   desc="professional photo of the EMPTY living-dining area as built, looking east: terrace glazing with the low interior step on the left, the grey 05.3 door ahead in the middle, the kitchen service wall (with sockets and the drain stub) right of it, the low white parapet block and the wall with the switch column on the right.",
   fix=["   a) left (about 0–22 %): the terrace glazing with white inner frames and the low interior step – unchanged;",
        "   b) about 37–46 %: the grey 05.3 door with its darker frame and black handle, closed or ajar exactly as photographed, same size and place;",
        "   c) about 46–56 %: the wall section W03-a right of the door (the refrigerator tower named in the brief stands here); a small step back at about 56 %;",
        "   d) about 56–81 %: the kitchen service wall with its real sockets and drain stub = the main kitchen run named in the brief (base cabinets, worktop, sink, upper cabinets as the brief says);",
        "   e) about 73–81 %: the low white parapet block (about 0.85 m) – it stays low: only low base cabinets against its kitchen side, nothing tall on it, no island;",
        "   f) right (about 81–100 %): the wall with the switch column and thermostat (W02 side) – unchanged, finished only as the brief names.",
        "Dining: the dining table named in the brief with its chairs in the open floor between the camera and the kitchen, under the pendant; the sofa and the TV wall are outside this frame."]),
 '3726-506':dict(room='dining towards terrace',interior=True,pend=True,step=True,
   desc="professional photo of the EMPTY living-dining area as built, looking towards the terrace glazing: the large lift-and-slide glazing with the low interior step ahead-left, the terrace paving and WPC steps beyond, the grey 05.3 door on the right, the wall with the large switch plate at the right edge.",
   fix=["   a) about 20–57 %: the terrace glazing with white inner frames on its low interior step – unchanged; beyond it the light-grey paving, the WPC steps and platform, railing and real skyline;",
        "   b) about 72–80 %: the grey 05.3 door and its darker frame – unchanged;",
        "   c) the left wall, the right-edge wall with its switch plate, the ceiling and every socket – unchanged.",
        "Dining: the dining table named in the brief with its six chairs in the foreground at real scale, under the pendant; only those parts of sofa and kitchen that fall inside this field of view; curtains only at the real glazing, stacked clear of the sliding sash."]),
 '3741-491':dict(room='master bedroom 05.1',interior=True,pend=False,step=False,
   desc="professional photo of the EMPTY master bedroom 05.1 as built: the western glass wall with exactly three white-framed fields and the balcony on the left, the north wall with its niche on the right.",
   fix=["   a) about 8–55 %: the glass wall with EXACTLY THREE white-framed fields (opening sash at the left with its handle, middle field, fixed field with the brick facade return), the balcony with light-grey tiles, black vertical railing and the real view – unchanged;",
        "   b) about 55–88 %: the north wall niche – in this design the full-height north wardrobe fronts fill the whole niche, floor to ceiling, their plane aligned with the pillar face;",
        "   c) about 88–100 %: the pillar / wall return at the right edge – unchanged;",
        "   d) ceiling flat white, the curtain track on the 33 cm wall strip above the glass, curtains stacked clear of the three fields.",
        "The bed and headboard stand against the east wall, which is behind and right of the camera: show at most what this photo camera can see (nothing, or a foot corner at the lower right edge); never move the bed into the centre of the room."]),
 '3488-744':dict(room='terrace',interior=False,pend=False,step=False,
   desc="professional photo of the EMPTY terrace as built, looking along the lower paved terrace beside the grey-brick facade towards the living-room glazing; the dark WPC platform and its steps in the left foreground, the planted roof at the far left.",
   fix=["   a) the WPC platform and steps in the left foreground keep their outline, heights and steps;",
        "   b) the light-grey paving, the facade with its glazing, the railing and the skyline – unchanged;",
        "   c) the planted roof stays planted; furniture stands only on the hard paving."]),
 '3498-734':dict(room='terrace from the planted roof',interior=False,pend=False,step=False,
   desc="professional photo of the terrace as built, seen from the planted-roof side towards the grey-brick facade: the 05.3 terrace door at left, the living-room glazing at right, the dark WPC deck and the paved terrace in the middle, the planted roof in the foreground.",
   fix=["   a) the planted foreground stays exactly as photographed – no furniture, path or new planting on it;",
        "   b) the facade, both glazings, the WPC deck levels, the thresholds and the railing – unchanged;",
        "   c) furniture only on the existing hard paving behind the planting."]),
 '3539-693':dict(room='terrace panorama',interior=False,pend=False,step=False,
   desc="professional photo from the existing WPC deck towards the planted roof, the railing and the city skyline.",
   fix=["   a) the deck outline, its level changes and steps, the planting and the railing – unchanged;",
        "   b) the real skyline including the structures visible in the photo – unchanged;",
        "   c) furniture only on the usable hard surface; step access and drainage stay free."]),
}
def photo_cam(cam,s,var,pend_s):
    n=cam.replace('Cam_F_',''); n=[k for k in PHOTO if k.startswith(n)][0]; P=PHOTO[n]
    att=[(photo1(n),f'01_image1_A902_KZS_{n}_profi_foto.jpg',
          f"{P['desc']} MANDATORY camera and geometry reference: this is the camera of this view. Keep its exact framing, perspective, horizon, lens and aspect ratio; every wall, opening, glazing, frame, door, step, socket, switch, ceiling and the existing floor stay exactly as photographed – only the items named in the creative brief are added. The empty state, bare sockets and daylight of the photo are NOT the design.")]
    lock=["1. Camera: identical to image 1 – same position, height, lens, perspective, horizon and the same 3:2 landscape frame. No rotation, no zoom, no crop, no wider view, no change of viewpoint.",
          "2. Fixed elements of image 1 (horizontal positions measured on the photo):"]+P['fix']+[
          "3. Anything outside this photo stays outside: designed surfaces that the brief places on walls not visible here are not shown.",
          f"4. Forbidden: {FORB}; replacing or recolouring the existing floor{', terrace paving or WPC' if not P['interior'] else ''}; a different city view.",
          "5. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."]
    notes=["- The CAMERA paragraph of the brief names this professional photo; image 1 IS that photo (photo-native camera; numeric Blender match not proven – the photo itself is the reference)."]
    if cam=='Cam_F_3659': notes.append("- W01 identification (brief: 'bind the W01 composition to its actual surveyed wall'): W01 is the plain wall ahead with the TV socket group; the TV-wall composition goes there and nowhere else.")
    if P['interior']: notes.append("- Sections about rooms outside this field of view (terrace furniture, other walls) are for consistency only; show only what this camera sees.")
    else: notes.append("- Sections about interior walls and furniture are for consistency; through the glass at most a glimpse of the interior is visible.")
    if P['pend'] and pend_s in PPHOTO:
        p,nm,r=PPHOTO[pend_s]; att.append((p,f'0{len(att)+1}_image{len(att)+1}_{nm}',r))
    if var=='B':
        if P['interior']:
            att.append((PADLO,f'0{len(att)+1}_image{len(att)+1}_A902_KZS3695_profi_padlo.jpg',FLOOR4))
            notes.append(MAT2)
            if P['step']: notes.append("- The low interior step (about 15 cm) at the foot of the terrace glazing stays exactly as in image 1, clad in the same grey floor; nothing stands on it.")
        else: notes.append(TERR)
        notes.append("- PHOTO-REAL EDITION: the photographed surfaces of image 1 are the material truth; warm light may change the mood, never the colour of the grey floor, the grey door, the white frames or the terrace paving.")
        notes.append(RULES)
    return dict(att=att,lock=lock,notes=notes)

def vanity(s,var):
    att=[(B10,'01_image1_A902_Cam10_furdo06-2_semleges_blender.png',"Blender render of the real, windowless L-shaped bathroom 06.2 as built, from the DIFFERENT fixed camera Cam_10 (doorway, looking east). Room geometry reference: walls, shaft block, shower kerb and drain, existing basin and fittings positions, ceiling. It is NOT the camera of this view."),
         ('/home/claude/work/v32/foto_2400/KZS_3598-634_2400.jpg','02_image2_A902_KZS_3598_furdo_profi_foto.jpg',"professional photo of this bathroom as built: Geostone Grigio 60 × 60 grey tiles, the Esagonetta hexagon 3D relief on the shower wall, black Grohe fittings, the existing white basin, the linear drain. MATERIALS AND FITTINGS ONLY – not the camera of this view (the brief says so).")]
    photo1('3598-634')
    lock=["1. Camera: the PROPOSED second bathroom camera from the CAMERA paragraph of the brief – eye inside the real dry-side doorway area at about 1.35 m, 20–24 mm lens, turned obliquely towards the integrated vanity and the dry edge of the new fixed shower glass. Level, verticals vertical, 16:10 landscape. This camera is CONDITIONAL (not yet validated in Blender); it must fit inside the existing room with all walls present.",
          "2. Fixed elements (from images 1 and 2): the real L-shaped windowless room, the shaft block, the existing grey tiles and the hexagon relief wall, the black fittings at their real positions, the shower floor, kerb line and linear drain, the existing basin connection position, the flat ceiling.",
          "3. In frame together: the two drawers of the continuous vanity, the wall cupboard, the mirror and the glass-to-counter joint; the WC may stay outside the frame; the entry to the shower stays open.",
          f"4. Forbidden: {FORB}; any window, daylight or exterior view; a glass door or full enclosure; moving the drain, the kerb or the fittings; new or different tiles; an invented bathroom socket.",
          "5. Output: exactly one photorealistic image, 16:10, no people, no text, no labels, no collage. If anything in the brief conflicts with images 1–2 or this lock, the images and this lock win."]
    notes=["- The REALITY AND MATERIALS paragraph is shared text for all rooms: in this bathroom the floor is the EXISTING grey Geostone tile, not the oak floor; there is no window.",
           "- Status: proposed camera – the result is a CONDITIONAL concept view until the camera is validated in Blender."]
    if var=='B': notes+= [BATH,"- PHOTO-REAL EDITION: tiles, relief, fittings and basin exactly as in image 2; warm concealed light must not turn the grey tiles beige.",RULES]
    return dict(att=att,lock=lock,notes=notes,cond=True)

def cam11c(var):
    sys.argv=['x']; src=open('/home/claude/work/build/build_cam11c.py').read().split('pf=B.A+')[0]
    g={}; exec(src,g); c=copy.deepcopy(g['c'])
    c['att']=[(p,n,FLOOR3 if '080_parketta' in n else r) for p,n,r in c['att']]
    c['notes']=["- Cam_11c is the separately owner-approved supplementary camera (Péter, 2026-10-25 18:19) named in the CAMERA paragraph of this EXTRA brief; it does NOT replace the mandatory Cam_11.",
                "- From this camera the SOUTH wardrobe is visible on the left; the north wardrobe is outside the frame.","- Daylight; all Hue layers off or barely perceptible."]
    return c

# ---------- terv ----------
def stylerefs(s,att):
    for p,n,r in STYLEREF.get(s,[]):
        k=len(att)+1; att.append((p,f'0{k}_image{k}_{n}',r))
plan=[]
m30=list(csv.DictReader(open(V+'/'+PR+'01_MANIFEST_30.csv',encoding='utf-8'),delimiter=';'))
mex=list(csv.DictReader(open(V+'/'+PR+'02_MANIFEST_EXTRA.csv',encoding='utf-8'),delimiter=';'))
ORDER=['Cam_12','Cam_02','Cam_03','Cam_04','Cam_11','Cam_10']
jobs=[]
for cam in ['Cam_12']:
    for s in STY:
        r=[x for x in m30 if x['stilus']==s and x['kamera']==cam][0]; jobs.append(('hero',r['nr'],r['kep_id'],s,cam,False))
for s in STY:
    for cam in ORDER[1:]:
        r=[x for x in m30 if x['stilus']==s and x['kamera']==cam][0]; jobs.append(('alap',r['nr'],r['kep_id'],s,cam,False))
for r in sorted(mex,key=lambda x:int(x['prioritas'])):
    jobs.append(('extra','X%02d'%int(r['prioritas']),r['kep_id'],r['stilus'],r['kamera'],True))
assert len(jobs)==47
seq=0
os.makedirs(OUT+'/prompts_sent',exist_ok=True)
for faz,nr,kid,s,cam,extra in jobs:
    for var in ('A','B'):
        if not extra: c=base(cam,s); c=to_b(c,cam) if var=='B' else c
        elif cam.startswith('Cam_F_'): c=photo_cam(cam,s,var,s)
        elif cam=='Cam_X_06_2_Vanity': c=vanity(s,var)
        elif cam=='Cam_11c':
            c=cam11c(var)
            if var=='B':
                c['att']=[(PADLO,'02_image2_A902_KZS3695_profi_padlo.jpg',FLOOR4) if '080_parketta' in n else (p,n,r) for p,n,r in c['att']]
        else: raise SystemExit(cam)
        if not extra and var=='B': c['notes'].append(BATH if cam=='Cam_10' else (MAT if nr in SENT_B else MAT2)); c['notes'].append(RULES)
        if extra and cam=='Cam_11c' and var=='B': c['notes']+= [MAT2,RULES]
        stylerefs(s,c['att'])
        c.update(id=kid,style=STY[s],cam=cam,var=var,extra=extra)
        pf=V+'/'+PR+('21_EXTRA_PROMPTOK/' if extra else '20_PROMPTOK/')+kid+'.prompt.md'
        prompt=open(pf,encoding='utf-8').read().rstrip('\n')
        assert prompt.startswith('=== BEGIN PROMPT '+kid+' ===') and prompt.endswith('=== END PROMPT '+kid+' ==='),kid
        h=hdr(c); msg=h+prompt+"\n"
        for bad in ('Kyoto','S01 ','V3.1 ·','Ink'):
            assert bad not in h,(kid,var,bad)
        if PEND[s]!='Kave Home Somar Ø76': assert 'Somar' not in h,(kid,var)
        tag=f"V32_{var}_v1"; seq+=1
        name=f"{nr}_{kid}__{tag}.txt"; open(OUT+'/prompts_sent/'+name,'w',encoding='utf-8').write(msg)
        rd=f"{UP}/{nr}_{var}"; os.makedirs(rd,exist_ok=True)
        for f in os.listdir(rd): os.remove(rd+'/'+f)
        for src,n,_ in c['att']: shutil.copyfile(src,rd+'/'+n)
        shutil.copy(OUT+'/prompts_sent/'+name,rd+'/_msg.txt')
        plan.append(dict(seq=seq,fazis=faz,nr=nr,valtozat=var,kep_id=kid,stilus=s,kamera=cam,kamera_statusz=('FELTÉTELES' if c.get('cond') else 'FOTÓ-NATÍV' if cam.startswith('Cam_F') else 'BLENDER-LOCK'),
            uzenet=name,kep_fajl=f"{kid}__{tag}.png",dir=f"upload/v32/{nr}_{var}",prompt_fajl=pf.replace(V+'/',''),
            uzenet_chars=len(msg),uzenet_sha256=hashlib.sha256(msg.encode()).hexdigest(),prompt_sha256=sha(pf),
            csatolmanyok=[dict(sorrend=i+1,fajl=n,sha256=sha(p)) for i,(p,n,_) in enumerate(c['att'])]))
os.makedirs(OUT+'/attachments_log',exist_ok=True)
json.dump(plan,open(OUT+'/attachments_log/v32_94_csatolmanyok.json','w'),ensure_ascii=False,indent=1)
json.dump(plan,open('/home/claude/work/v32_plan.json','w'),ensure_ascii=False,indent=1)
print(len(plan)); [print(p['seq'],p['nr'],p['valtozat'],p['stilus'],p['kamera'],len(p['csatolmanyok']),p['uzenet_chars']) for p in plan]

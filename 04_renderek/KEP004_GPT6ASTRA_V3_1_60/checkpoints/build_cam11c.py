import sys, shutil
sys.path.insert(0,'/home/claude/work/build'); import build as B
import importlib; FLOOR3=("real site photo of the EXISTING floor and skirting in this apartment – oak-effect planks in a cool grey-brown, photographed in cool daylight. Material and colour reference ONLY (not a camera, not a layout). "
        "In the result the floor must read as this same cool grey-brown oak with visible grain and knots: under warm evening light it may look slightly warmer, but never honey, orange-brown, reddish, whitened or dark-stained, and never replaced by another floor.")
import os, hashlib
c=dict(nr='05',cam='Cam_11c',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_3_master_Cam_11_A',
 att=[('/home/claude/work/cam11c_base.png','01_image1_A902_Cam11c_master_panorama_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty master bedroom 05.1 from the exact camera of this view (Cam_11c, owner-approved). MANDATORY camera and geometry reference: the 3.64 m glass wall with exactly three white-framed fields, the balcony and railing, the south wall, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. The pale exterior is only a placeholder for the real view (see image 3); the flat floor tone is NOT the material (see image 2)."),
      ('/home/claude/work/upload/Cam_11/02_image2_A902_ME-BAL-080_parketta_szegely.jpg','02_image2_A902_ME-BAL-080_parketta_szegely.jpg',FLOOR3),
      ('/home/claude/work/upload/Cam_11/03_image3_A902_ME-BAL-077_master_uvegfal_kilatas.jpg','03_image3_A902_ME-BAL-077_master_uvegfal_kilatas.jpg',"real site photo of THIS bedroom's glass wall from a DIFFERENT position: the real white frames, the balcony with light-grey tiles and black vertical railing, the brick facade return outside on the right, and the REAL view (city roofs, church spire, Buda hills). Use it for the glass wall's appearance and the exact exterior view only – do NOT copy its camera or framing.")],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera at seated eye height 1.20 m on the bed, on its north half near the headboard, 20 mm lens, looking west and turned slightly to the left (south-west). Verticals stay vertical; the eye-level horizon is at 50 % of the image height. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–24 %: the SOUTH wardrobe on the left, seen at an angle: it fills the existing 2.42 m south strip, its front plane receding from the left edge towards the window wall; floor to ceiling.",
  "   b) 24–32 %: the white wall pier between the south wardrobe and the glazing.",
  "   c) 32–92 %: the 3.64 m glass wall with EXACTLY THREE white-framed fields: the opening sash 32–44 %, the narrow middle field 44–58 %, the wide fixed field 58–92 % (the widest field). The glass head falls from about 19 % (left end) to about 10 % (right end); the sill/floor line runs from about 77 % (left) to about 86 % (right).",
  "   d) 92–100 %: the narrow white wall pier right of the glazing; the north wardrobe is just beyond the right edge (not in frame).",
  "   e) Above the glass: the 33 cm white wall strip carrying the wall-mounted curtain track; curtains stacked only at the very ends, never over the three fields.",
  "   f) Beyond the glass: the balcony about 15 cm lower, light-grey tiles, black vertical-bar railing; the brick facade return is outside, seen through the right end of the fixed field; then the REAL view of image 3.",
  "   g) Lower foreground: the foot end of the bed across the bottom of the frame (its south foot corner at about 34 % across, 93 % down).",
  "3. NOT in this frame: the headboard and east wall (behind the camera), the north wardrobe (beyond the right edge), the room door.",
  f"4. Forbidden: {B.COMMON_FORBID}; a narrower, wider or differently divided glass wall; a fourth glass field; a different balcony or railing; a generic or invented view; moving the wardrobe out of the south strip.",
  "5. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- Camera change approved by the owner (Péter, 2026-10-25 18:19): the CAMERA paragraph of the creative brief describes the earlier frontal Cam_11; for this run only that camera description is replaced by Cam_11c (image 1). Everything else in the brief applies unchanged.",
  "- From this camera the SOUTH wardrobe is visible on the left; the north wardrobe is outside the frame.",
  "- Daylight; all Hue layers off or barely perceptible."])
pf=B.A+'/'+B.PD+c['id']+'.prompt.md'; prompt=open(pf,encoding='utf-8').read().rstrip('\n')
msg=B.hdr(c)+prompt+"\n"; name=f"05_{c['id']}__ASTRA_V3_1__Cam11c_v1.txt"
open(B.OUT+'/prompts_sent/'+name,'w',encoding='utf-8').write(msg); shutil.copy(B.OUT+'/prompts_sent/'+name,'/home/claude/work/upload/msgs/')
rd='/home/claude/work/upload/Cam_11c'; os.makedirs(rd,exist_ok=True)
for s,n,r in c['att']: shutil.copyfile(s,rd+'/'+n)
print(name,len(msg),hashlib.sha256(msg.encode()).hexdigest())

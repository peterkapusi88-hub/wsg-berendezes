import copy, hashlib, os, shutil, sys
sys.path.insert(0,'/home/claude/work/build'); import build as B, build_v3 as V
IMG='/home/claude/work/out/img/'
c=dict(nr='05',cam='Cam_11b',style='S01 Kyoto Ink',id='A902_S01_KyotoInk_3_master_Cam_11_A',
 att=[('/home/claude/work/cam11b_base.png','01_image1_A902_Cam11b_master_panorama_atlos_semleges_blender.png',"Blender render 1600 × 1000 of the real, empty master bedroom 05.1 from the exact camera of this view (Cam_11b, owner-approved diagonal panorama camera). MANDATORY camera and geometry reference: the 3.64 m glass wall with exactly three white-framed fields, the balcony and railing, the north niche, walls, ceiling and floor lines. Nothing in image 1 may be moved, added or removed. The pale exterior is only a placeholder for the real view (see image 3); the flat floor tone is NOT the material (see image 2)."),
      ('/home/claude/work/upload/Cam_11/02_image2_A902_ME-BAL-080_parketta_szegely.jpg','02_image2_A902_ME-BAL-080_parketta_szegely.jpg',V.FLOOR3),
      ('/home/claude/work/upload/Cam_11/03_image3_A902_ME-BAL-077_master_uvegfal_kilatas.jpg','03_image3_A902_ME-BAL-077_master_uvegfal_kilatas.jpg',"real site photo of THIS bedroom's glass wall from a DIFFERENT position: the real white frames, the balcony with light-grey tiles and black vertical railing, the brick facade return outside on the right, and the REAL view (city roofs, church spire, Buda hills). Use it for the glass wall's appearance and the exact exterior view only – do NOT copy its camera or framing."),
      V.ident(IMG+'A902_S01_KyotoInk_3_master_Cam_04_A__ASTRA_V3_1__v1.png','04_image4_A902_S01_Cam04_v1_butorazonossag_referencia.png','Cam_04, master bedroom evening view')],
 lock=["1. Camera: keep the exact framing, perspective, horizon and vanishing points of image 1 – level camera at seated eye height 1.20 m on the SOUTH half of the bed, close to the headboard, 20 mm lens, looking diagonally west-north-west across the bed towards the glass wall. Verticals stay vertical; the eye-level horizon is at 50 % of the image height. Do not crop, zoom, rotate, raise, widen or re-frame. Same landscape 16:10 framing as image 1.",
  "2. Fixed elements of image 1, from LEFT to RIGHT (horizontal position in the frame, from the Blender projection of this camera):",
  "   a) 0–5 %: a narrow white wall pier at the left edge.",
  "   b) 5–66 %: the 3.64 m glass wall, seen at an angle, with EXACTLY THREE white-framed fields: the opening sash 5–24 %, the narrow middle field 24–40 %, the wide fixed field 40–66 %. The glass head falls from about 10 % (left end) to about 19 % (right end); the sill/floor line rises from about 86 % (left) to about 78 % (right).",
  "   c) 66–70 %: the narrow white wall pier and corner right of the glazing.",
  "   d) 70–100 %: the existing NORTH NICHE. In this design the whole niche is filled by the north wardrobe, its fronts in the plane of the pillar face, receding from 70 % to the right edge, floor to ceiling.",
  "   e) Beyond the glass: the balcony about 15 cm lower, light-grey tiles, black vertical-bar railing, then the REAL view of image 3 (city roofs, church spire, Buda hills).",
  "   f) Lower foreground: the bed – the camera sits on it; its foot edge crosses the lower part of the frame, the north foot corner at about 78 % across / 90 % down.",
  "3. NOT in this frame: the headboard and east wall (behind the camera), the south wardrobe strip (beyond the left edge), the room door. Do not show them.",
  f"4. Forbidden: {B.COMMON_FORBID}; a narrower, wider or differently divided glass wall; a fourth glass field; a different balcony or railing; a generic or invented view; moving the wardrobe out of the niche.",
  "5. Output: exactly one photorealistic image, same framing and aspect as image 1, no people, no text, no labels, no collage. If anything in the brief conflicts with image 1 or this lock, image 1 and this lock win."],
 notes=["- Camera change approved by the owner (Péter, 2026-10-25 17:58): the CAMERA paragraph of the creative brief describes the earlier frontal Cam_11; for this run only that camera description is replaced by Cam_11b (image 1). Everything else in the brief applies unchanged.",
  "- From this camera the north wardrobe is visible on the right and the south wardrobe is outside the frame.",
  "- Image 4 keeps the wardrobe fronts, headboard materials, bedding and bedside objects identical to the Cam_04 view of this style; image 1 alone defines the geometry.",
  "- Daylight; all Hue layers off or barely perceptible."])
name,rd=V.write(c,'Cam11b_v1'); shutil.copy(B.OUT+'/prompts_sent/'+name,'/home/claude/work/upload/msgs/'); print(rd)

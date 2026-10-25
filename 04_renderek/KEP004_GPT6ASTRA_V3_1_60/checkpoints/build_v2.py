import hashlib
OUT='/mnt/user-data/outputs/WSG_ASTRA_V3_1_RENDEREK/prompts_sent/'
V2={
'01_A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A':[
"V2 CORRECTION (2026-10-25) – a first attempt with this exact package drifted. Keep the creative design; correct ONLY these measured geometry errors:",
"- W01 was drawn too frontal and too short. It is a 4.00 m wall seen at a grazing angle and must recede strongly. Its floor line: about 81 % of the image height at the left edge, 76 % at 14 % across, 71 % at 28 %, 68 % at 39 %, 65 % at the corner (47–48 %). Its ceiling line: about 5 % at the left edge, 10 % at 14 %, 15 % at 28 %, 18 % at 39 %, 21 % at the corner.",
"- The eye-level horizon (1.55 m) lies at about 42 % from the top of the image (the camera is tilted slightly down).",
"- Glazing: west frame at 52 %, first mullion at 69–70 % (not further right); its sill follows the floor line (about 67 % down at 52 %, 76 % down at 70 %).",
"- The TV-wall composition is mounted flat on W01 and follows exactly these receding lines; nothing on W01 turns towards the camera."],
'02_A902_S01_KyotoInk_1_nappali-hero_Cam_12_A':[
"V2 CORRECTION (2026-10-25) – a first attempt with this exact package drifted. Keep the creative design; correct ONLY these measured geometry errors:",
"- The whole room was placed about 15 % too high in the frame and the sofa filled the bottom third. Correct vertical anchors: the eye-level horizon (1.60 m) is at about 42 % from the top; the 05.3 door head at about 33 % and its foot at about 70 %; the W02 floor line at about 70 % at its left end (56 % across) and about 88 % at its right end (86 % across); the W02 top edge (ceiling) at about 19 % at its left end; the far kitchen floor corner at about 62 % and the far kitchen ceiling corner at about 26 %. The sofa occupies only the bottom 16–23 % of the frame.",
"- The opening to the entrance hall between 45 % and 55 % across stays OPEN above the low parapet, under the lintel (lintel underside at about 33 % down). W02 starts at 55–56 %; it does not extend over the opening.",
"- The tall unit on W03-a (12–23 %) is the refrigerator tower – chalk doors with a graphite side panel – not an oven column."],
'05_A902_S01_KyotoInk_3_master_Cam_11_A':[
"V2 CORRECTION (2026-10-25) – a first attempt with this exact package drifted. Keep the creative design; correct ONLY these measured geometry errors:",
"- The glazing was drawn about 10 % too narrow. The white frame of the 3.64 m glass wall spans from 21 % to 79 % of the image width: opening sash 21–35 %, narrow middle field 35–50 %, wide fixed field 50–79 % (the widest of the three, about twice the middle field).",
"- The brick facade return seen in image 3 is OUTSIDE the building, visible THROUGH the right part of the wide fixed field beyond the glass and the balcony; it does not shorten, frame or replace any part of the glazing. Inside, right of the frame, there is only the narrow white wall pier (79–84 %) and then the north wardrobe.",
"- Vertical anchors: the eye-level horizon (1.20 m, seated) is at 50 % of the image height; glass head at about 15 %; sill and floor line at about 81 %; the foot of the bed at the very bottom."]}
for k,blk in V2.items():
    v1=open(OUT+k+'__ASTRA_V3_1__v1.txt',encoding='utf-8').read()
    v1=v1.replace('CAMERA-LOCKED CONCEPT TEST (2026-10-25)','CAMERA-LOCKED CONCEPT TEST (2026-10-25) · RUN v2',1)
    mark='\nRUN NOTES – how to read'
    assert v1.count(mark)==1
    v2=v1.replace(mark,'\n'+'\n'.join(blk)+'\n'+mark,1)
    p=OUT+k+'__ASTRA_V3_1__v2.txt'; open(p,'w',encoding='utf-8').write(v2)
    print(k,len(v2),hashlib.sha256(v2.encode()).hexdigest()[:16])

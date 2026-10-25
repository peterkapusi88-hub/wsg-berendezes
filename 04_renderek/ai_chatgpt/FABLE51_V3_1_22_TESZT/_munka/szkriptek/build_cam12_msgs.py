import re, os, hashlib
SRC = open('/home/claude/wsg-cam12-csomag/UZENET_S01_Cam12_v3_KORR.txt', encoding='utf-8').read()
head = SRC[:SRC.find('CREATIVE BRIEF')]
P = '/home/claude/wsg-berendezes/05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/'
OUT = '/home/claude/fable_msgs/cam12_v3/'
os.makedirs(OUT, exist_ok=True)
items = [('06', 'A902_S03_AleliCasa_1_nappali-hero_Cam_12_A', 'S03 Aleli Casa'),
         ('08', 'A902_S06_ZenitAtelier_1_nappali-hero_Cam_12_A', 'S06 Zenit Atelier'),
         ('10', 'A902_S04_LAHorizon_1_nappali-hero_Cam_12_A', 'S04 LA Horizon'),
         ('12', 'A902_S05_MiamiStreamline_1_nappali-hero_Cam_12_A', 'S05 Miami Streamline'),
         ('22', 'A902_S07_LakeForestCouture_1_nappali-hero_Cam_12_A', 'S07 Lake Forest Couture')]
for nr, kid, sname in items:
    h = head.replace('S01 Kyoto Ink', sname)
    # image roles without 1b (no style-specific block render exists for this style)
    h = re.sub(r'- Image 1b \(.*?\n(?=- Image 2)', '', h, flags=re.S)
    h = h.replace('ATTACHED IMAGES AND THEIR ROLES', f'IMAGE ID: {kid}\nSOURCE VERSION: FABLE51-V3.1 (competition/fable51-v3-1-20261025 @ b44541205cdd79e3d1f33ee8074c2bc280beb7a7) · integrator geometry wrapper Cam_12 v3 KORR (integrator/cam12-v3-korrekcio-20261025 @ 09c2762)\n\nATTACHED IMAGES AND THEIR ROLES (in this order: image 1, image 2, image 3)')
    h = h.replace('the place of the fridge column (see image 1b)', 'the place of the fridge column')
    h = re.sub(r'4\. Kitchen exactly as in image 1b:.*?Nothing else\.',
               '4. Kitchen layout (owner decision, same layout for every style): along the receding east kitchen wall one run of base cabinets with the sink and the hob, upper cabinets above and a closed top-box row to 2.75 m, closed at the far (south) end by a tall appliance column (oven and microwave); on the right of the kitchen only low base cabinets with a worktop standing against the kitchen side of the existing ~0.85 m parapet – attached to the parapet, NOT an island – ending at the white pier; a tall fridge column 0.60 m wide stands against the dining-wall section W03-a, left of the kitchen and right of the 05.3 door. Fronts, worktop and colours exactly as named in the creative brief. Nothing else.', h, flags=re.S)
    h = re.sub(r'5\. Furniture only as in image 1b:.*?moved\.',
               '5. Furniture only as named in the creative brief, at realistic sizes: the sofa in the foreground (lower left and centre), the dining table lengthwise with its chairs under the dining pendant between the camera and the kitchen; nothing added, nothing enlarged.', h, flags=re.S)
    h = h.replace('If anything in the creative brief below conflicts with image 1 or 1b, image 1 and 1b win.', 'If anything in the creative brief below conflicts with image 1 or with this geometry lock, image 1 and the lock win.')
    t = open(P + kid + '.prompt.md', encoding='utf-8').read()
    m = re.search(r'=== BEGIN PROMPT (\S+) ===\n(.*?)\n=== END PROMPT \1 ===', t, re.S)
    assert m and m.group(1) == kid
    brief = (f'CREATIVE BRIEF – Fable 5.1, {sname} Cam_12 prompt, verbatim and unchanged (source: competition/fable51-v3-1-20261025 @ b44541205cdd79e3d1f33ee8074c2bc280beb7a7, '
             f'05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/{kid}.prompt.md, text between the BEGIN/END markers):\n\n')
    msg = h + brief + m.group(2)
    assert '1b' not in h, (kid, [l for l in h.splitlines() if '1b' in l])
    fn = f'{OUT}{nr}_{kid}__CAM12V3KORR.txt'
    open(fn, 'w', encoding='utf-8').write(msg)
    print(fn, len(msg), hashlib.sha256(m.group(2).encode()).hexdigest()[:12])

"""Usage: python3 compare.py <kep_id> [<kep_id> ...]
Builds base | render side-by-side + 50% blend + edge overlay for each id."""
import sys, re, os
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops
R = '/home/claude/wsg-berendezes/04_renderek/'
BASE = {
    'Cam_02': R + 'A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png',
    'Cam_12': R + 'A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png',
    'Cam_03': R + 'A902_kameracsomag_C/A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png',
    'Cam_04': R + 'A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png',
    'Cam_11': R + 'A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png',
    'Cam_12KORR': '/home/claude/wsg-cam12-csomag/01_image1_A902_Cam12v3_KORR_semleges.png',
    'Cam_10': R + 'A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png',
}
SRC = '/mnt/user-data/uploads/Downloads/WSG_FABLE51_V3_1_RENDEREK/'
OUT = '/home/claude/fable_out/gate/'
os.makedirs(OUT, exist_ok=True)
for kid in sys.argv[1:]:
    cam = re.search(r'(Cam_\d+)', kid).group(1)
    if os.environ.get('KORR') and cam=='Cam_12': cam='Cam_12KORR'
    base = Image.open(BASE[cam]).convert('RGB')
    rp = sorted([f for f in os.listdir(SRC) if f.startswith(kid + '__')])[-1] if len(sys.argv) > 0 else None
    ren = Image.open(SRC + rp).convert('RGB')
    W, H = 800, 500
    b = base.resize((W, H)); r = ren.resize((W, H))  # stretch to base frame (aspect differences noted separately)
    blend = Image.blend(b, r, 0.5)
    eb = ImageOps.autocontrast(b.convert('L').filter(ImageFilter.FIND_EDGES)).point(lambda v: 255 if v > 40 else 0)
    er = ImageOps.autocontrast(r.convert('L').filter(ImageFilter.FIND_EDGES)).point(lambda v: 255 if v > 60 else 0)
    ov = Image.merge('RGB', (eb, er, Image.new('L', (W, H), 0)))  # red = base edges, green = render edges
    sheet = Image.new('RGB', (2 * W, 2 * H + 40), 'white')
    for img, (x, y) in [(b, (0, 0)), (r, (W, 0)), (blend, (0, H + 20)), (ov, (W, H + 20))]:
        sheet.paste(img, (x, y))
    d = ImageDraw.Draw(sheet)
    d.text((5, H + 4), f'BASE {cam}', fill='black'); d.text((W + 5, H + 4), f'RENDER {ren.size}', fill='black')
    d.text((5, 2 * H + 24), 'blend 50%', fill='black'); d.text((W + 5, 2 * H + 24), 'edges: red=base green=render', fill='black')
    sheet.save(OUT + rp.replace('.png','') + '__gate.jpg', quality=82)
    print(OUT + rp.replace('.png','') + '__gate.jpg', ren.size, round(ren.size[0] / ren.size[1], 3))

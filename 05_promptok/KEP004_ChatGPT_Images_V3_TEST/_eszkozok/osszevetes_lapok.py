# KEP-004 V3_TEST – geometriai és kreatív összevető lapok (Claude, 2026-10-25). Csak olvas, új JPG-t ír.
import sys
from PIL import Image, ImageDraw, ImageFont
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
def tile(path, cim, al='', w=800, h=500):
    im = Image.open(path).convert('RGB').resize((w, h), Image.LANCZOS); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w, 64 if al else 38], fill=(0, 0, 0)); d.text((10, 6), cim, font=FONT, fill=(255, 220, 0))
    if al: d.text((10, 38), al, font=FS, fill=(230, 230, 230))
    return im
def lap(tiles, cols, out, fejlec):
    w, h = tiles[0].size; rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * w, rows * h + 50), (25, 25, 25)); d = ImageDraw.Draw(sheet)
    d.text((12, 10), fejlec, font=FONT, fill=(255, 255, 255))
    for i, t in enumerate(tiles): sheet.paste(t, ((i % cols) * w, 50 + (i // cols) * h))
    sheet.save(out, quality=88)
if __name__ == '__main__':
    G = sys.argv[1]
    for k, nev in (('S01', 'S01 Kyoto Ink'), ('S02', 'S02 BiBo Nocturne')):
        lap([tile(f'{G}/alap.png', '1. alapkép (Blender v2b-1, Cam_02)'), tile(f'{G}/tomeg_{k}.png', '1b V3-tömbkép (Blender, validátor PASS)'),
             tile(f'{G}/{k}_V3TEST.png', f'{nev} – V3_TEST (ChatGPT, 1586×992)'),
             tile(f'{G}/{k}_V3TEST_vetitett_atfedes.jpg', 'vetített ellenőrzés', 'piros: falak/nyílás · narancs: üvegprofil · cián: V3-tömbök')],
            2, f'{G}/{k}_V3TEST_geometriai_osszevetes.jpg', f'A-902 · Cam_02 · {nev} · V3_TEST geometriai összevetés (Claude, 2026-10-25)')
    lap([tile(f'{G}/V2_S01_r1.png', 'V2 próbakép – S01 (01:04)', 'Gate: FAIL / ÚJRATERVEZÉS'),
         tile(f'{G}/S01_V3TEST.png', 'V3_TEST – S01 Kyoto Ink (02:33)', 'r2-csomag, javított tömbkép'),
         tile(f'{G}/S02_V3TEST.png', 'V3_TEST – S02 BiBo Nocturne (02:38)', 'r2-csomag, javított tömbkép'),
         tile(f'{G}/S01_V3r1_masik.png', 'másik munkamenet – S01 V3 (02:21)', 'r1-csomag, régi tömbkép – nem a jóváhagyott kettő'),
         tile(f'{G}/S02_V3r1_masik.png', 'másik munkamenet – S02 V3 (02:24)', 'r1-csomag, régi tömbkép – nem a jóváhagyott kettő'),
         tile(f'{G}/alap.png', '1. alapkép (geometriai referencia)')],
        3, f'{G}/V3TEST_kreativ_osszevetes.jpg', 'A-902 · Cam_02 · V2 próbakép → Creative Upgrade V3 tesztképek (Claude, 2026-10-25)')
    print('ok')

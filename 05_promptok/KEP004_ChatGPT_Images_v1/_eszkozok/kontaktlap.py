# Helyszíni fotók egy lapon (Cam_02 „image 2b”): kis azonosítókkal, felirat nélküli képtartalommal.
from PIL import Image, ImageDraw, ImageFont
R = '/home/claude/wsg-berendezes/08_allapotfelmeres/fotok/A902/'
def lap(kepek, ki, cols=3, tile=(800, 600)):
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)
    rows = (len(kepek) + cols - 1) // cols; W, H = cols * tile[0] + (cols + 1) * 8, rows * tile[1] + (rows + 1) * 8
    s = Image.new('RGB', (W, H), (255, 255, 255)); d = ImageDraw.Draw(s)
    for i, (p, cimke) in enumerate(kepek):
        im = Image.open(p).convert('RGB'); im.thumbnail(tile, Image.LANCZOS)
        x = 8 + (i % cols) * (tile[0] + 8); y = 8 + (i // cols) * (tile[1] + 8)
        s.paste(im, (x + (tile[0] - im.width) // 2, y + (tile[1] - im.height) // 2))
        d.rectangle((x + 4, y + tile[1] - 30, x + 4 + 11 * len(cimke), y + tile[1] - 6), fill=(255, 255, 255)); d.text((x + 8, y + tile[1] - 29), cimke, font=F, fill=(60, 60, 60))
    s.save(ki, quality=92); return s.size
if __name__ == '__main__':
    print(lap([(R + '04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg', 'ME-BAL-045'),
               (R + '04_nappali/A902_04_20261021_ME-BAL-046_nappali_eloter_fele.jpg', 'ME-BAL-046'),
               (R + '00_besorolando/A902_00_20261021_ME-BAL-042_greslap_lepcso_teglafal.jpg', 'ME-BAL-042'),
               (R + '00_besorolando/A902_00_20261021_ME-BAL-044_greslap_kozel.jpg', 'ME-BAL-044'),
               (R + '00_besorolando/A902_00_20261021_ME-BAL-053_teraszajto_sotet_tegla_kava.jpg', 'ME-BAL-053')],
              '/tmp/claude-0/-home-claude/a6ba6a27-0f48-546e-b8bb-fd2d0d27539e/scratchpad/csomag/helyszin_kontaktlap_Cam02.jpg'))

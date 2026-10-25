# KEP-004 V3_TEST Gate – részletkivágás-lap (Claude, 2026-10-25). Egységes 3×2-es rács, minden csempe azonos keretben,
# arányhelyesen kicsinyítve/nagyítva. Használat: python3 reszlet_lap.py <generalt_kep.png> S01|S02 <kimenet.jpg>
import sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1600, 1000          # a vetítés és a Gate-mérések kerete
CW, CH, FEJ = 520, 440, 26  # csempe mérete és felirat-sáv
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
KIVAGAS = {
    'S01': [('KI3-V torony: 3 front, tusgrafika, fehér korpusz', (0, 150, 260, 800)),
            ('KI3-P grafit sík + TV + KI3-L (4 front, lábazat)', (190, 150, 760, 780)),
            ('W01 sarok, FL02 környéke, tapéta, szegőléc', (640, 120, 860, 700)),
            ('W04 pillér, fehér keret, sötét téglakáva', (760, 200, 1010, 720)),
            ('Étkező: Toni tölgy + Eamy (nyugati sor)', (1080, 560, 1600, 1000)),
            ('Terasz és panoráma (bútor nélkül)', (880, 150, 1600, 720))],
    'S02': [('BN3-V: ajtós oszlop + fix tükör + szervizpanel', (0, 150, 300, 820)),
            ('BN3-R tükör – fizikailag lehetséges belső kép', (120, 180, 290, 700)),
            ('BN3-P navy sík + TV + BN3-L (4 front, lábazat)', (250, 150, 760, 780)),
            ('W04 pillér, fehér keret, sötét téglakáva', (760, 200, 1010, 720)),
            ('Étkező: Anouk üveg + Ciselia; kartámla-tálca', (1080, 560, 1600, 1000)),
            ('Terasz és panoráma (bútor nélkül)', (880, 150, 1600, 720))],
}
if __name__ == '__main__':
    src, kod, out = sys.argv[1:4]
    im = Image.open(src).convert('RGB').resize((W, H), Image.LANCZOS)
    f = ImageFont.truetype(FONT, 15)
    lap = Image.new('RGB', (3 * CW + 4 * 8, 2 * (CH + FEJ) + 3 * 8), (24, 24, 24))
    for i, (cim, (x0, y0, x1, y1)) in enumerate(KIVAGAS[kod]):
        c = im.crop((x0, y0, x1, y1))
        s = min(CW / c.width, CH / c.height)
        c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
        r, k = divmod(i, 3)
        X, Y = 8 + k * (CW + 8), 8 + r * (CH + FEJ + 8)
        ImageDraw.Draw(lap).text((X + 2, Y + 4), f'{kod} · {cim}', fill=(255, 220, 0), font=f)
        lap.paste(c, (X + (CW - c.width) // 2, Y + FEJ + (CH - c.height) // 2))
    lap.save(out, quality=88)
    print(out, lap.size)

from PIL import Image, ImageDraw, ImageFont
R = '/home/claude/wsg-berendezes/'
U = '/mnt/user-data/uploads/WSG/KEP-004/01_blender_ellenorzo/Cam11_v1_2026-10-24/'
F = lambda s, b=False: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if b else ''), s)
tiles = [
 (R + '04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png', 'Cam_04 (meglévő master) · üres alapkép', 'üvegfal a képen 0 % · fejvégfal + északi fülke + pillér'),
 (U + 'A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png', 'Cam_11_Master_Panorama · JAVASLAT · üres alapkép', '[3,20; 6,10; 1,20] · 20 mm · vízszintes · üvegfal a képen 38 %'),
 (R + '08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg', 'Helyszíni fotó ME-BAL-077 (2026-10-21) – 05.1', 'a valós nyugati panoráma: budai hegyek, tetőtáj, pálcás korlát'),
 (U + 'ellenorzes_Cam04_gardrobfal_javaslat_v1.png', 'Cam_04 + ágy valós befoglalója + gardróbfal-javaslat', 'narancs NORDLI 180×202×30 · sárga matrac (becslés) · lila fejvég · kék gardróbfal'),
 (U + 'ellenorzes_Cam11_gardrobfal_javaslat_v1.png', 'Cam_11 + ágy valós befoglalója + gardróbfal-javaslat', 'jobbra az északi gardróbfal, balra a modell déli PAX-a (szürke)'),
 ('ellenorzes_05_1_felulnezet_Cam04_Cam11_v1.png', 'Felülnézet – látómezők, ágyhelyek, kiállások', 'kék szaggatott: a tervrajz ágyhelye (≈0,40 m-rel északabbra)'),
]
TW, TH, CAP = 800, 500, 64
W, H = 3 * TW + 4 * 12, 2 * (TH + CAP) + 3 * 12 + 92
sheet = Image.new('RGB', (W, H), (246, 246, 244)); d = ImageDraw.Draw(sheet)
d.text((16, 14), 'A-902 · 05.1 master – Cam_04 vs Cam_11_Master_Panorama (JAVASLAT) · KEP-004 · 2026-10-24 · Claude', font=F(26, True), fill=(20, 20, 20))
d.text((16, 52), 'Blender v2b-1-k10 munkamásolat, az alapképekkel azonos fény (EEVEE, egyszínű égbolt, AgX MHC, exp. +0,75). Az ágy és a falak nem mozdultak; a színes testek csak jelölések. Státusz: ELLENŐRZŐKÉP – nem látványterv.', font=F(17), fill=(70, 70, 70))
for i, (p, t1, t2) in enumerate(tiles):
    im = Image.open(p).convert('RGB')
    r = min(TW / im.width, TH / im.height); im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    cx = 12 + (i % 3) * (TW + 12); cy = 92 + (i // 3) * (TH + CAP + 12)
    sheet.paste((255, 255, 255), (cx, cy, cx + TW, cy + TH))
    sheet.paste(im, (cx + (TW - im.width) // 2, cy + (TH - im.height) // 2))
    d.rectangle((cx, cy + TH, cx + TW, cy + TH + CAP), fill=(255, 255, 255))
    d.text((cx + 10, cy + TH + 6), t1, font=F(19, True), fill=(11, 90, 86) if 'Cam_11' in t1 else (40, 40, 40))
    d.text((cx + 10, cy + TH + 34), t2, font=F(16), fill=(80, 80, 80))
sheet.save('osszevetes_Cam04_Cam11_v1.jpg', quality=90)
print(sheet.size)

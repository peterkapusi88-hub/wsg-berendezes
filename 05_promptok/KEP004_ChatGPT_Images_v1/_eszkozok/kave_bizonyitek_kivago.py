# A Kave-oldalak képernyőképeinek bizonyító kivágása (csak a Kave-oldal; Péter csevegőablaka, fülei és könyvjelzői nélkül). Claude, 2026-10-24.
import sys, json, hashlib
from PIL import Image
A = '/mnt/user-data/attachments/a6ba6a27-0f48-546e-b8bb-fd2d0d27539e/'
OUT = sys.argv[1]
L = [('Eamy_szek_vilagosszurke','31dbc4ef','22:56'),('Nifelia_szonyeg','5c0747e7','22:55'),('Somar_fuggesztek','8b375ff9','22:56'),('Ciselia_szek_bezs_fekete','334f4833','22:56'),
     ('Marely_szonyeg','1f39c132','22:56'),('Brisia_lampa','49f13037','22:56'),('Somar_SPECIFIKACIO','9c638983','23:02'),('Brisia_SPECIFIKACIO','fa75308b','23:02'),
     ('Eamy_szek_barna','0b5d4bc0','23:09'),('Ciselia_szek_bezs_bezs','b6c129f6','23:09'),('Corvena_fotel','a4a2521b','23:09'),('Sheffield_dohanyzoasztal','55d44a00','23:09'),
     ('Argo_uvegasztal','47ba8ade','23:10'),('Naanim_asztal','957b3108','23:10'),('Nealy_asztal','75da4516','23:10'),('Madali_allolampa','83f5264b','23:10'),
     ('Ardali_fuggesztek','ee4fc760','23:11'),('Drava_fuggesztek','f094bb43','23:11'),('Novae_lampa','0fe6d684','23:11'),('Malenka_szonyeg','31ad0a3b','23:11'),
     ('Blok_sarokkanape','036a48b4','23:11'),('Neom_kanape','e1d04d19','23:12'),('Ciselia_szek_bezs_fekete_meretrajzzal','fc68165f','23:12')]
man = []
for nev, f, ido in L:
    im = Image.open(A + f + '-image.png').convert('RGB')
    box = (1700, 152, 3065, 1330) if im.size == (3440, 1440) else (0, 90, im.size[0], 1250)
    p = OUT + f"KH_{nev}_oldal_{ido.replace(':','')}.jpg"; im.crop(box).save(p, quality=85)
    man.append(dict(fajl=p.split('/')[-1], forras=f + '-image.png', ido='2026-10-24 ' + ido, kivagas=box, sha256=hashlib.sha256(open(p,'rb').read()).hexdigest()))
im = Image.open(A + '989bce26-image.png').convert('RGB'); p = OUT + 'KH_Brisia_MERETRAJZ_2306.jpg'; im.save(p, quality=92)
man.append(dict(fajl='KH_Brisia_MERETRAJZ_2306.jpg', forras='989bce26-image.png', ido='2026-10-24 23:06', kivagas=None, sha256=hashlib.sha256(open(p,'rb').read()).hexdigest()))
json.dump(man, open(OUT + 'forras_manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(man), 'fájl')

# Kave Home termékképek kivágása Péter képernyőképeiből (2026-10-24). Csak olvas az attachments mappából; kimenet: kivagas/
import json, hashlib, sys
from PIL import Image
A = '/mnt/user-data/attachments/a6ba6a27-0f48-546e-b8bb-fd2d0d27539e/'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'kivagas/'
# név → (képernyőkép, kivágás (x0,y0,x1,y1) a képernyőkép pixelében, mi látszik)
K = {
 'KH_Eamy_szek_vilagosszurke':      ('31dbc4ef', (0, 166, 560, 790), 'termék, kivágott háttér'),
 'KH_Nifelia_szonyeg_200x300':      ('5c0747e7', (1722, 296, 2312, 988), 'termék, kivágott háttér'),
 'KH_Somar_fuggesztek_76':          ('8b375ff9', (2318, 996, 2908, 1322), 'termék, kivágott háttér'),
 'KH_Ciselia_szek_bezs_fekete':     ('334f4833', (1728, 300, 2156, 780), 'termék, kivágott háttér'),
 'KH_Marely_szonyeg_feher_200x300': ('1f39c132', (1728, 292, 2156, 784), 'termék, kivágott háttér'),
 'KH_Brisia_fuggesztek_sargarez':   ('49f13037', (1728, 300, 2156, 780), 'termék, kivágott háttér'),
 'KH_Eamy_szek_barna':              ('0b5d4bc0', (2156, 956, 2370, 1224), 'termék, kivágott háttér (kis kép)'),
 'KH_Ciselia_szek_bezs_bezs':       ('b6c129f6', (2370, 746, 2586, 986), 'termék, kivágott háttér (kis kép)'),
 'KH_Corvena_fotel_oliva':          ('a4a2521b', (1728, 150, 2156, 476), 'termék, kivágott háttér'),
 'KH_Sheffield_dohanyzoasztal':     ('55d44a00', (1728, 250, 2156, 546), 'termék, kivágott háttér'),
 'KH_Argo_uvegasztal_119':          ('47ba8ade', (1728, 150, 2156, 540), 'termék, kivágott háttér'),
 'KH_Naanim_asztal_dio_120':        ('957b3108', (1728, 150, 2156, 546), 'termék, kivágott háttér'),
 'KH_Nealy_asztal_sotet_dio_150':   ('75da4516', (1728, 150, 2156, 550), 'termék, kivágott háttér'),
 'KH_Madali_allolampa':             ('83f5264b', (2156, 960, 2370, 1226), 'termék, kivágott háttér (kis kép)'),
 'KH_Ardali_fuggesztek_50':         ('ee4fc760', (2156, 500, 2586, 1024), 'enteriőrkép (a teljes függeszték látszik)'),
 'KH_Drava_fuggesztek_bordo':       ('f094bb43', (1728, 150, 2156, 526), 'termék, kivágott háttér'),
 'KH_Novae_fuggesztek_40':          ('0fe6d684', (1728, 552, 2156, 1090), 'termék közeli, világítva'),
 'KH_Malenka_szonyeg_barna_200x300':('31ad0a3b', (1728, 250, 2156, 680), 'termék, kivágott háttér'),
 'KH_Blok_sarokkanape_290x230':     ('036a48b4', (1728, 330, 2586, 820), 'termék, kivágott háttér'),
 'KH_Neom_kanape_chaise_263':       ('e1d04d19', (1728, 330, 2586, 800), 'termék, kivágott háttér'),
 # méretrajzok (K8 és a 2–3. adag)
 'KH_Ciselia_szek_MERETRAJZ':        ('fc68165f', (1940, 924, 2156, 1192), 'méretrajz (Ciselia, fekete láb)'),
 'KH_Ciselia_szek_bezs_bezs_MERETRAJZ': ('b6c129f6', (1940, 746, 2156, 1014), 'méretrajz (Ciselia, bézs láb)'),
 'KH_Eamy_szek_vilagosszurke_MERETRAJZ': ('31dbc4ef', (300, 860, 560, 1100), 'méretrajz (Eamy)'),
 'KH_Eamy_szek_barna_MERETRAJZ':     ('0b5d4bc0', (1940, 956, 2156, 1224), 'méretrajz (Eamy barna)'),
 'KH_Corvena_fotel_MERETRAJZ':       ('a4a2521b', (1940, 970, 2156, 1236), 'méretrajz (Corvena)'),
 'KH_Argo_uvegasztal_MERETRAJZ':     ('47ba8ade', (1940, 1160, 2156, 1310), 'méretrajz (Argo, részleges)'),
 'KH_Naanim_asztal_MERETRAJZ':       ('957b3108', (1940, 1120, 2156, 1320), 'méretrajz (Naanim, részleges)'),
 'KH_Drava_fuggesztek_MERETRAJZ':    ('f094bb43', (1940, 1066, 2156, 1300), 'méretrajz (Drava)'),
 'KH_Sheffield_dohanyzoasztal_MERETRAJZ': ('55d44a00', (1726, 1084, 2156, 1320), 'méretrajz (Sheffield, részleges)'),
 'KH_Novae_fuggesztek_MERETRAJZ':    ('0fe6d684', (1726, 1096, 1940, 1310), 'méretrajz (Novae)'),
}
if __name__ == '__main__':
    man = []
    for nev, (f, box, mi) in K.items():
        im = Image.open(A + f + '-image.png').convert('RGB').crop(box)
        p = OUT + nev + '.jpg'; im.save(p, quality=92)
        man.append(dict(nev=nev + '.jpg', kepernyokep=f + '-image.png', kivagas=box, meret=im.size, tartalom=mi,
                        sha256=hashlib.sha256(open(p, 'rb').read()).hexdigest()))
        print(f'{nev:40s} {im.size}')
    json.dump(man, open(OUT + 'kivagas_manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

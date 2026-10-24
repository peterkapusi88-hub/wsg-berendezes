# =====================================================================================
# A-902 – Péter U-kanapéja (2026-10-24 18:36, a terv 18. oldalára rajzolva) ugyanazzal az ellenőrzővel. 2026-10-24, Claude.
# MÉRETPRÓBA – nem stílusterv. Geometria: geometry_lock_A902_v2b (main, terv szerinti), helyszínen nem mért.
# Péter rajza (a képről mérve, ±5 cm): U kb. 2,40 (x) × 3,00 (y), x 4,77–7,19, y 4,49–7,48; a gyári TV-blokk a nyugati falon.
# Az étkező a terv helyén (80 × 180 asztal, 3 + 3 szék, betolt székekkel [7,98; 5,37; 9,32; 7,17], az ML04 lámpa alatt).
# Változatok:
#   - 'P902_rajz': a rajz helye és mérete;
#   - 'P902': ugyanaz a U 0,46 m-rel északabbra (y 4,95–7,95), hogy a bejárat és a hálók folyosója között 0,90 m maradjon;
#   - 'P902_29': U 2,40 × 2,90 (y 4,95–7,85), az üveg előtt 0,20 m.
# A U nyitott oldala a TV felé (nyugatra) néz, a háta az étkező felé; a szárak 0,95 m mélyek (jelzés).
# Kimenet: terv_elrendezes_A902.json, terv_elrendezes_A902.png. Futtatás: python3 terv_elrendezes_a902.py
# =====================================================================================
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kanape_meretproba_a8 as K
import kanape_meretproba_a902 as M
import terv_elrendezes_a811 as T8
import shapely
from shapely.geometry import box
from shapely.ops import unary_union
from PIL import ImageDraw

TV = (3.67, 5.15, 4.12, 6.95)              # 180 × 45 konzol a gyári blokk előtt (G08 y = 6,054; D16, D17 mögötte)
ZONA = box(7.98, 5.37, 9.32, 7.17); ASZTAL = box(8.25, 5.37, 9.05, 7.17)
M_ULO = 0.95

def u_alak(x0, y0, x1, y1):   # nyitott oldal nyugatra (a TV felé), háttámla keleten
    return unary_union([box(x1 - M_ULO, y0, x1, y1), box(x0, y0, x1, y0 + M_ULO), box(x0, y1 - M_ULO, x1, y1)])

EL = [dict(kod='P902_rajz', nev='Péter rajza szerint', S=(4.77, 4.49, 7.19, 7.48)),
      dict(kod='P902', nev='Péter U-ja 0,46 m-rel északabbra', S=(4.77, 4.95, 7.17, 7.95)),
      dict(kod='P902_29', nev='U 2,40 × 2,90, az üveg előtt 0,20 m', S=(4.77, 4.95, 7.17, 7.85)),
      dict(kod='P902_22', nev='U 2,20 × 3,00 (a TV felé 20 cm-rel rövidebb)', S=(4.77, 4.95, 6.97, 7.95)),
      dict(kod='P902_22A', nev='U 2,20 × 3,00, az asztal 0,30 m-rel nyugatra', S=(4.77, 4.95, 6.97, 7.95), zona=(7.68, 5.37, 9.02, 7.17))]


def ellenoriz(A, e):
    Z = box(*e['zona']) if 'zona' in e else ZONA
    S = box(*e['S']); Tb = box(*TV); akad = [S, Tb, Z]
    cm = T8.cel_max(A, akad)
    K.MELLEK_UT = None
    utak = K.utak_hossza(A, akad)
    sb = S.bounds
    return dict(kod=e['kod'], nev=e['nev'], kanape=[round(v, 2) for v in sb], meret=f"{sb[2] - sb[0]:.2f} × {sb[3] - sb[1]:.2f}".replace('.', ','),
                cel_max_szelesseg_m=cm, uthossz_090_m=utak, ures_uthossz_m=A['ures_tav'],
                nezotav_m=round(sb[2] - K.SZEM - (TV[0] + K.KEPERNYO), 2), kanape_tv_m=round(sb[0] - TV[2], 2),
                deli_sav_m=round(sb[1] - 4.05, 2), uveg_elott_m=round(8.05 - sb[3], 2), etkezo_tav_m=round(Z.bounds[0] - sb[2], 2), etkezo_zona=[round(v, 2) for v in Z.bounds],
                tv_eltolas_m=round(abs((sb[1] + sb[3]) / 2 - (TV[1] + TV[3]) / 2), 2)), akad


def rajz(A, e, r, akad, px=80):
    im = K.panel(A, '', None, dict(alak='U'), None, px=px); dr = ImageDraw.Draw(im, 'RGBA')
    x0, y0, x1, y1 = A['C']['nezet']; T = lambda x, y: (round((x - x0) * px), round(62 + (y1 - y) * px))
    def poly(g, fill=None, outline=None, width=1):
        for p in shapely.get_parts(g):
            if p.geom_type == 'Polygon': dr.polygon([T(*c) for c in p.exterior.coords], fill=fill, outline=outline, width=width)
    ok, parts, be = K.szabad_ter(A, akad, K.UT)
    for p, b in zip(parts, be if be is not None else []):
        if b: poly(p, fill=K.SZIN['ut'] + (90,))
    poly(box(*e['S']), outline=K.SZIN['kanape'] + (255,), width=2); poly(u_alak(*e['S']), fill=K.SZIN['kanape'] + (120,), outline=K.SZIN['kanape'] + (255,))
    Z = box(*r['etkezo_zona']); dx = Z.bounds[0] - ZONA.bounds[0]
    poly(box(*TV), fill=K.SZIN['tv'] + (180,)); poly(Z, fill=K.SZIN['etk'] + (45,), outline=K.SZIN['etk'] + (255,), width=2)
    poly(box(ASZTAL.bounds[0] + dx, ASZTAL.bounds[1], ASZTAL.bounds[2] + dx, ASZTAL.bounds[3]), fill=K.SZIN['etk'] + (200,))
    for nev, k in (('ML04', 'A902-ML04'), ('ML05', 'A902-ML05')):
        p = T(M.KV[k]['x_m'], M.KV[k]['y_m']); dr.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=(255, 210, 0, 255), outline=(0, 0, 0, 255)); dr.text((p[0] + 9, p[1] - 7), nev, fill=(0, 0, 0), font=K.FS)
    cm = r['cel_max_szelesseg_m']; f = lambda v: (f'{v:.2f}' if v else '0').replace('.', ',')
    dr.rectangle([0, 0, im.size[0], 60], fill=(255, 255, 255, 255))
    dr.text((8, 4), f"{e['kod']} · {e['nev']} · U {r['meret']} m", fill=(0, 0, 0), font=K.FB)
    dr.text((8, 22), f"legszélesebb út: terasz {f(cm['terasz (tolóajtó)'])} · hálók folyosója {f(cm['hálók folyosója'])} · konyha {f(cm['konyha (a pultsorok közé)'])} · 05.3 háló {f(cm['05.3 háló ajtaja'])} m",
            fill=(20, 120, 40) if min(v or 0 for v in cm.values()) >= 0.60 else (200, 30, 30), font=K.F)
    dr.text((8, 41), f"nézőtáv {f(r['nezotav_m'])} · U–TV {f(r['kanape_tv_m'])} · déli sáv {f(r['deli_sav_m'])} · az üveg előtt {f(r['uveg_elott_m'])} · U–asztal {f(r['etkezo_tav_m'])} m", fill=(60, 60, 60), font=K.FS)
    return im


if __name__ == '__main__':
    A = M.lakas(); A['C'] = dict(nezet=(3.2, 0.9, 11.2, 8.6), pult=M.PULT); A['lock'] = M.LOCK
    A['nappali_aljzatok'] = [k for k in M.V['kiallasok'] if ('NAPPALI' in k['helyiseg'] or 'ÉTKEZ' in k['helyiseg']) and k['tipus'] in ('dugalj', 'antenna_tv_aljzat', 'gyengearamu_aljzat')]
    eredmeny, panelek = [], []
    for e in EL:
        r, akad = ellenoriz(A, e); eredmeny.append(r); panelek.append(rajz(A, e, r, akad))
        print(e['kod'], r['meret'], r['cel_max_szelesseg_m'], 'nézőtáv', r['nezotav_m'], 'U–TV', r['kanape_tv_m'], 'déli', r['deli_sav_m'], 'üveg', r['uveg_elott_m'], 'asztal', r['etkezo_tav_m'], 'TV-eltolás', r['tv_eltolas_m'])
    lab = ['MÉRETPRÓBA – nem stílusterv; geometry_lock_A902_v2b, helyszínen nem mért. Péter U-ja (18:36): a nyitott oldal a TV (nyugati fal, gyári blokk) felé, a háta az étkező felé; az étkező a terv helyén, betolt székekkel.',
           'Kék: U (sötétebb: ülőrészek 95 cm – jelzés); barna: TV-konzol 180 × 45; narancs: étkező; halványzöld: a bejáratból 0,90 m-es úttal elérhető tér. A fejlécben célonként a legszélesebb út (5 cm-es lépés).',
           'A 05.3 háló ajtajához a terv asztalhelye miatt a pult sarkánál kb. 0,6 m marad – ez a kanapétól független.']
    K.lap(panelek, 'A-902 – Péter U-kanapéja ugyanazzal az ellenőrzővel (2026-10-24)', lab).save(os.path.join(K.HERE, 'terv_elrendezes_A902.png'), optimize=True)
    json.dump(dict(datum='2026-10-24', statusz='MÉRETPRÓBA – nem stílusterv; geometry_lock_A902_v2b, helyszínen nem mért', forras='Péter rajza 2026-10-24 18:36 (WGR1 18. o.)',
                   tv_konzol=TV, etkezo_zona=list(ZONA.bounds), eredmeny=eredmeny), open(os.path.join(K.HERE, 'terv_elrendezes_A902.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész')

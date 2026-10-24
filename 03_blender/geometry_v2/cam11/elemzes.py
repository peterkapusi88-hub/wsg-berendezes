import json, math, numpy as np, sys
sys.path.insert(0, '.')
from vetites import Kamera, lap_vetulet
L = json.load(open('/home/claude/wsg-berendezes/03_blender/geometry_lock_A902_v2b.json'))
c4 = L['cameras']['Cam_04_Master']
K = {'Cam_04_Master': Kamera(c4['loc'], c4['rot'], c4['lens_mm']),
     'Cam_11_Master_Panorama': Kamera((3.20, 6.10, 1.20), (math.pi/2, 0, math.pi/2), 20.0),
     'Cam_11_fekve_z090': Kamera((3.25, 6.10, 0.90), (math.pi/2, 0, math.pi/2), 20.0)}
g = L['openings']['Uvegfal_05_1_erkely_uveg']  # [x0,y0,z0,x1,y1,z1]
xg = (g[0] + g[3]) / 2
uveg = [(xg, g[1], g[2]), (xg, g[4], g[2]), (xg, g[4], g[5]), (xg, g[1], g[5])]
# fejvég-befoglaló homlokfelülete (x 3,49) és a modell ágyának fejvége
fejveg = [(3.49, 4.70, 0.0), (3.49, 7.30, 0.0), (3.49, 7.30, 1.0), (3.49, 4.70, 1.0)]
# ágy teteje (matrac felső síkja, becslés 0,52)
agy_teto = [(1.48, 5.11, 0.52), (3.48, 5.11, 0.52), (3.48, 6.89, 0.52), (1.48, 6.89, 0.52)]
# gardróbfront (PAX a déli sávban, front y 4,02)
pax = [(0.0, 4.02, 0.0), (2.42, 4.02, 0.0), (2.42, 4.02, 2.36), (0.0, 4.02, 2.36)]
# északi fülke hátfala (y 8,95)
fulke = [(0.0, 8.95, 0.0), (3.02, 8.95, 0.0), (3.02, 8.95, 2.9), (0.0, 8.95, 2.9)]
# keleti fal (fejvégfal) x 3,57 y 4,05–8,05
kfal = [(3.57, 4.05, 0.0), (3.57, 8.05, 0.0), (3.57, 8.05, 2.9), (3.57, 4.05, 2.9)]
out = {}
for n, k in K.items():
    d = dict(hfov=round(k.hfov(), 1), vfov=round(k.vfov(), 1))
    for ln, poly in [('uvegfal', uveg), ('fejveg_homlok', fejveg), ('agy_teteje', agy_teto), ('pax_front', pax), ('eszaki_fulke_hatfal', fulke), ('keleti_fejvegfal', kfal)]:
        cp, a = lap_vetulet(k, poly)
        d[ln] = dict(kepterulet_szazalek=round(100 * a, 1), bbox_px=[int(min(q[0] for q in cp)), int(min(q[1] for q in cp)), int(max(q[0] for q in cp)), int(max(q[1] for q in cp))] if cp else None)
    out[n] = d
# látóvonalak a korlát felső éle fölött (korlát teteje z 0,95; nyúlvány x -1,12, fő erkély x -2,01)
lat = {}
for nev, z in [('ulve_1.20', 1.20), ('felulve_1.05', 1.05), ('fekve_0.90', 0.90)]:
    for kn, xk in [('nyulvany_x-1.12', -1.12), ('fo_erkely_x-2.01', -2.01)]:
        dist = 3.20 - xk
        lat[f'{nev}|{kn}'] = round(math.degrees(math.atan2(0.95 - z, dist)), 1)
out['latovonal_korlat_teteje_fok'] = lat
out['uveg_teteje_fok_ulve'] = round(math.degrees(math.atan2(g[5] - 1.20, 3.20 - xg)), 1)
out['uveg_alja_fok_ulve'] = round(math.degrees(math.atan2(g[2] - 1.20, 3.20 - xg)), 1)
print(json.dumps(out, ensure_ascii=False, indent=1))
json.dump(out, open('vetitesi_elemzes_cam04_cam11.json', 'w'), ensure_ascii=False, indent=1)

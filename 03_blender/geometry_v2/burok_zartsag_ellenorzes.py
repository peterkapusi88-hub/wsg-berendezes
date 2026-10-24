# A-902 – épületburok-zártság ellenőrzése a lock alapján (2026-10-24, Claude)
# Csak olvas: a lock falai és nyílászárói (üveg, profil, ajtólap) 1 cm-es rácson, adott magasságokban.
# Kívülről "elárasztja" a szabad cellákat úgy, hogy a helyiségeken nem halad át, és kiírja, hol ér a külső tér
# KÖZVETLENÜL helyiséghez – ez rés a falak/nyílászárók között. A tűrés (TOL_CM) alatti rések (pl. a tok és a káva
# közti 3 cm-es modell-egyszerűsítés) zárva számítanak.
# Futtatás: python3 burok_zartsag_ellenorzes.py <repo>/03_blender/geometry_lock_A902_v2b.json [TOL_CM=2]
import sys, json
import numpy as np
from scipy import ndimage

lock = json.load(open(sys.argv[1], encoding='utf-8'))
TOL = int(sys.argv[2]) if len(sys.argv) > 2 else 2
RES = 0.01
xs = [b[0] for b in lock['walls'].values()] + [b[3] for b in lock['walls'].values()]
ys = [b[1] for b in lock['walls'].values()] + [b[4] for b in lock['walls'].values()]
X0, Y0, X1, Y1 = min(xs) - 1, min(ys) - 1, max(xs) + 1, max(ys) + 1
nx, ny = int((X1 - X0) / RES), int((Y1 - Y0) / RES)


def ij(x, y):
    return int(round((x - X0) / RES)), int(round((y - Y0) / RES))


room = np.zeros((ny, nx), bool)
for rects in lock['rooms'].values():
    for r in rects:
        i0, j0 = ij(r[0], r[1]); i1, j1 = ij(r[2], r[3]); room[j0:j1, i0:i1] = True

found = []
for Z in (0.3, 1.5, 2.6):
    block = np.zeros((ny, nx), bool)
    for grp in ('walls', 'openings'):
        for n, b in lock[grp].items():
            if n.startswith('Plafon') or not (b[2] <= Z <= b[5]):
                continue
            i0, j0 = ij(b[0], b[1]); i1, j1 = ij(b[3], b[4])
            block[max(j0, 0):max(j1, j0 + 1), max(i0, 0):max(i1, i0 + 1)] = True
    bd = ndimage.binary_dilation(block, iterations=TOL) if TOL else block
    lab, _ = ndimage.label(~bd & ~room)
    out = lab == lab[0, 0]
    contact = room & ~bd & ndimage.binary_dilation(out, iterations=1)
    l2, n2 = ndimage.label(contact)
    for k in range(1, n2 + 1):
        yy, xx = np.nonzero(l2 == k)
        g = (round(X0 + xx.min() * RES, 2), round(X0 + xx.max() * RES, 2), round(Y0 + yy.min() * RES, 2), round(Y0 + yy.max() * RES, 2))
        found.append((Z, g))
print(f'Burokzártság (tűrés: {2 * TOL} cm alatti rés zárt):', 'ZÁRT' if not found else f'{len(found)} érintkezés')
for Z, g in found:
    print(f'  z={Z} m: x {g[0]}–{g[1]}, y {g[2]}–{g[3]}')

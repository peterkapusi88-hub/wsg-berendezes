# KEP-004 V3_TEST Gate – vetítéses átfedés (Claude, 2026-10-25). A Cam_02 paramétereiből (v2b-1-k11b) számolt építészeti
# vonalakat (piros) és a V3-tömbök élvázát (cián) rajzolja a generált képre; ellenőrző pontokat jelöl.
import sys, json, math, numpy as np
from PIL import Image, ImageDraw
W, H = 1600, 1000
C = np.array([8.30, 4.40, 1.55]); ax, ay, az = 1.4791, 0.0, 0.8577; F = 20.0; SW = 36.0
def Rx(a): return np.array([[1,0,0],[0,math.cos(a),-math.sin(a)],[0,math.sin(a),math.cos(a)]])
def Ry(a): return np.array([[math.cos(a),0,math.sin(a)],[0,1,0],[-math.sin(a),0,math.cos(a)]])
def Rz(a): return np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])
R = Rz(az) @ Ry(ay) @ Rx(ax)
def proj(P):
    p = R.T @ (np.array(P, float) - C)
    if p[2] >= -1e-6: return None
    s = F / SW * W
    return (W / 2 + s * p[0] / -p[2], H / 2 - s * p[1] / -p[2])
def seg(d, A, B, col, w=3, n=40):
    pts = [proj(np.array(A) + (np.array(B) - np.array(A)) * t / n) for t in range(n + 1)]
    pts = [p for p in pts if p is not None]
    if len(pts) > 1: d.line(pts, fill=col, width=w)
def box(d, a, b, col, w=2):
    x0, y0, z0 = a; x1, y1, z1 = b
    V = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    for i, j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]: seg(d, V[i], V[j], col, w)
ARCH = [((3.67, 4.30, 0), (3.67, 8.05, 0)), ((3.67, 4.30, 2.90), (3.67, 8.05, 2.90)), ((3.67, 8.05, 0), (3.67, 8.05, 2.90)),
        ((3.67, 8.05, 2.90), (9.6, 8.05, 2.90)), ((4.38, 8.05, 0), (4.38, 8.05, 2.53)), ((4.38, 8.05, 2.53), (9.0, 8.05, 2.53)),
        ((4.38, 8.05, 0.0), (9.0, 8.05, 0.0)), ((3.67, 8.05, 0), (4.38, 8.05, 0))]
PROF = [(4.41, 4.47), (6.227, 6.287), (7.919, 7.979), (8.91, 8.97)]
if __name__ == '__main__':
    gen, logf, kod, out = sys.argv[1:5]
    L = json.load(open(logf, encoding='utf-8'))
    im = Image.open(gen).convert('RGB').resize((W, H), Image.LANCZOS)
    g = Image.blend(im, im.convert('L').convert('RGB'), 0.55); d = ImageDraw.Draw(g)
    for A, B in ARCH: seg(d, A, B, (255, 40, 40), 3)
    for x0, x1 in PROF:
        for x in (x0, x1): seg(d, (x, 8.21, 0.0), (x, 8.21, 2.53), (255, 140, 0), 2)
    for nev, bb in L['stilus'][kod]['tomegek'].items():
        if 'szek' in nev and '_hat' not in nev: continue
        box(d, bb[:3], bb[3:], (0, 230, 255), 2)
    for nev, P in [('sarok', (3.67, 8.05, 0)), ('D16/D17', (3.67, 6.29, 0.30)), ('ML05', (5.619, 6.274, 2.90)), ('FL02', (3.67, 7.849, 2.85))]:
        p = proj(P)
        if p: d.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], outline=(255, 255, 0), width=3); d.text((p[0] + 9, p[1] - 9), nev, fill=(255, 255, 0))
    g.save(out, quality=90)
    print('ellenőrzés: sarok_padlo', [round(v) for v in proj((3.67, 8.05, 0))], 'várt [760, 649]; uveg_bal_also', [round(v) for v in proj((4.44, 8.05, 0))], 'várt [838, 673]')

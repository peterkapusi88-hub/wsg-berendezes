# Blender-kompatibilis pinhole vetítés + képkivágás (sensor_fit AUTO, fekvő kép: 36 mm vízszintes szenzor)
import numpy as np, math
def rot_xyz(rx, ry, rz):
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]]); Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]); Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx
class Kamera:
    def __init__(s, loc, rot, lens, sensor=36.0, W=1600, H=1000):
        s.loc = np.array(loc, float); s.R = rot_xyz(*rot); s.f = lens; s.sw = sensor; s.W = W; s.H = H
        s.sh = sensor * H / W  # AUTO, fekvő
    def cam(s, p):  # világ → kamera (x jobbra, y fel, -z előre)
        return s.R.T @ (np.array(p, float) - s.loc)
    def px(s, pc):  # kamera-koordináta (z<0) → pixel
        x, y, z = pc; d = -z
        u = s.f * x / d / s.sw * s.W + s.W / 2; v = s.H / 2 - s.f * y / d / s.sh * s.H
        return np.array([u, v])
    def hfov(s): return 2 * math.degrees(math.atan(s.sw / 2 / s.f))
    def vfov(s): return 2 * math.degrees(math.atan(s.sh / 2 / s.f))
def clip_near(poly, zn=-0.1):
    out = []
    for i in range(len(poly)):
        a, b = poly[i], poly[(i + 1) % len(poly)]
        ia, ib = a[2] <= zn, b[2] <= zn
        if ia: out.append(a)
        if ia != ib:
            t = (zn - a[2]) / (b[2] - a[2]); out.append(a + t * (b - a))
    return out
def clip_rect(poly, W, H):
    def clip(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            if inside(b):
                if not inside(a): out.append(inter(a, b))
                out.append(b)
            elif inside(a): out.append(inter(a, b))
        return out
    def ix(x0):
        return lambda a, b: a + (x0 - a[0]) / (b[0] - a[0]) * (b - a)
    def iy(y0):
        return lambda a, b: a + (y0 - a[1]) / (b[1] - a[1]) * (b - a)
    p = list(poly)
    for ins, inter in [(lambda q: q[0] >= 0, ix(0)), (lambda q: q[0] <= W, ix(W)), (lambda q: q[1] >= 0, iy(0)), (lambda q: q[1] <= H, iy(H))]:
        if not p: break
        p = clip(p, ins, inter)
    return p
def area(p):
    if len(p) < 3: return 0.0
    x = np.array([q[0] for q in p]); y = np.array([q[1] for q in p])
    return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
def lap_vetulet(kam, pts):
    pc = [kam.cam(p) for p in pts]; pc = clip_near(pc)
    if len(pc) < 3: return [], 0.0
    pp = [kam.px(q) for q in pc]; cp = clip_rect(pp, kam.W, kam.H)
    return cp, area(cp) / (kam.W * kam.H)

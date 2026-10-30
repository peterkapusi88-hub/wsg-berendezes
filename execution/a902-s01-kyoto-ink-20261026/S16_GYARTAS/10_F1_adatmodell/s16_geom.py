"""S16 F1 – közös geometriai segédfüggvények (build + QA).

Globális rendszer: R14 helyi rajzi mm (X jobbra a szobából nézve, Y faltól a szoba felé, Z fel).
Nem tükrözünk újra.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

AXIS_VEC = {
    "+X": np.array([1.0, 0, 0]), "-X": np.array([-1.0, 0, 0]),
    "+Y": np.array([0, 1.0, 0]), "-Y": np.array([0, -1.0, 0]),
    "+Z": np.array([0, 0, 1.0]), "-Z": np.array([0, 0, -1.0]),
}
IRANY_NEV = {
    "+X": "jobb", "-X": "bal", "+Y": "elöl (szoba)", "-Y": "hátul (fal)",
    "+Z": "fent", "-Z": "lent",
}


def neg(a: str) -> str:
    return ("-" if a[0] == "+" else "+") + a[1]


def vec_to_axis(v) -> str:
    v = np.asarray(v, float)
    i = int(np.argmax(np.abs(v)))
    return ("+" if v[i] > 0 else "-") + "XYZ"[i]


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def box_min_max(box):
    x, y, z, dx, dy, dz = box
    return np.array([x, y, z], float), np.array([x + dx, y + dy, z + dz], float)


class LocalFrame:
    """Alkatrész helyi rendszere az A oldal felől nézve."""

    def __init__(self, box, a_normal: str, nezetek: dict):
        self.a_normal = a_normal
        self.u_ax = nezetek[a_normal]["U"]
        self.v_ax = nezetek[a_normal]["V"]
        self.n_ax = a_normal
        self.U = AXIS_VEC[self.u_ax]
        self.V = AXIS_VEC[self.v_ax]
        self.N = AXIS_VEC[self.n_ax]
        lo, hi = box_min_max(box)
        origin = np.zeros(3)
        for vec in (self.U, self.V, self.N):
            i = int(np.argmax(np.abs(vec)))
            origin[i] = lo[i] if vec[i] > 0 else hi[i]
        self.origin = origin
        size = hi - lo
        self.L = float(abs(self.U) @ size)
        self.W = float(abs(self.V) @ size)
        self.T = float(abs(self.N) @ size)

    def to_local(self, p):
        d = np.asarray(p, float) - self.origin
        return np.array([d @ self.U, d @ self.V, d @ self.N])

    def to_global(self, uvn):
        u, v, n = uvn
        return self.origin + u * self.U + v * self.V + n * self.N

    def box_to_local(self, gbox):
        lo, hi = box_min_max(gbox)
        corners = np.array([[a, b, c] for a in (lo[0], hi[0]) for b in (lo[1], hi[1]) for c in (lo[2], hi[2])])
        loc = np.array([self.to_local(c) for c in corners])
        mn, mx = loc.min(0), loc.max(0)
        return {"u": [round(float(mn[0]), 3), round(float(mx[0]), 3)],
                "v": [round(float(mn[1]), 3), round(float(mx[1]), 3)],
                "n": [round(float(mn[2]), 3), round(float(mx[2]), 3)]}

    # élek: E1 V=0, E2 U=max, E3 V=max, E4 U=0
    def edge_dirs(self):
        return {
            "E1": vec_to_axis(-self.V), "E2": vec_to_axis(self.U),
            "E3": vec_to_axis(self.V), "E4": vec_to_axis(-self.U),
        }

    def edge_samples(self, edge: str, offset: float = 0.5, step: float = 25.0, inset: float = 2.0):
        """Mintapontok az él síkja előtt `offset` mm-rel kifelé."""
        L, W, T = self.L, self.W, self.T
        if edge in ("E1", "E3"):
            length = L
            along = np.linspace(min(inset, L / 2), max(L - inset, L / 2), max(5, int(L // step) + 1))
            v = -offset if edge == "E1" else W + offset
            pts = [(a, v, t) for a in along for t in (0.2 * T, 0.5 * T, 0.8 * T)]
        else:
            length = W
            along = np.linspace(min(inset, W / 2), max(W - inset, W / 2), max(5, int(W // step) + 1))
            u = L + offset if edge == "E2" else -offset
            pts = [(u, a, t) for a in along for t in (0.2 * T, 0.5 * T, 0.8 * T)]
        return length, np.array([self.to_global(p) for p in pts])


def mesh_from_obj(vertices, faces):
    import trimesh
    tris = []
    for f in faces:
        for k in range(1, len(f) - 1):
            tris.append([f[0], f[k], f[k + 1]])
    m = trimesh.Trimesh(vertices=np.asarray(vertices, float), faces=np.asarray(tris, int), process=True)
    m.merge_vertices(digits_vertex=3)
    m.update_faces(m.nondegenerate_faces())
    m.update_faces(m.unique_faces())
    m.remove_unreferenced_vertices()
    trimesh.repair.fix_normals(m)
    return m


def extrude_outline_y(part, holes=()):
    """y-tengelyű (A=+Y) R14 kontúr (U=X, V=Z) extrudálása T vastagságra, globális hálóként."""
    import trimesh
    from shapely.geometry import Polygon
    x, y, z, dx, dy, dz = part["box"]
    from shapely.validation import make_valid
    poly = largest_polygon(Polygon(part["outline"]))
    for h in holes:
        poly = largest_polygon(poly.difference(largest_polygon(Polygon(h))))
    import shapely
    poly = largest_polygon(shapely.set_precision(poly, 0.001))
    m = trimesh.creation.extrude_polygon(poly, height=dy)
    v = m.vertices.copy()
    g = np.column_stack([x + v[:, 0], y + v[:, 2], z + v[:, 1]])
    # (x,y,z)->(x,z,y) tükrözés: a háromszögek körüljárását meg kell fordítani
    out = trimesh.Trimesh(vertices=g, faces=m.faces[:, ::-1], process=True)
    return out


def largest_polygon(geom):
    from shapely.validation import make_valid
    g = make_valid(geom)
    if g.geom_type == "Polygon":
        return g
    polys = [p for p in getattr(g, "geoms", []) if p.geom_type == "Polygon"]
    return max(polys, key=lambda p: p.area)


def box_mesh(box):
    import trimesh
    lo, hi = box_min_max(box)
    return trimesh.creation.box(bounds=[lo, hi])


def build_solid(part, zobj):
    """Legjobb elérhető zárt test: R14 zárt jelenet hálója → kontúr-extrudálás → doboz − kimetszés → doboz."""
    import trimesh
    name = part["id"]
    if zobj is not None:
        try:
            m = mesh_from_obj(zobj["vertices_mm"], zobj["faces"])
            if m.is_watertight and abs(m.volume) > 0:
                if m.volume < 0:
                    m.invert()
                return Solid.from_mesh(name, m, "R14_zart_halo")
        except Exception:
            pass
    if part.get("outline") and part["axis"] == "y":
        holes = [c["outline"] for c in part.get("cutouts", []) if c.get("type") == "through_contour"]
        m = extrude_outline_y(part, holes)
        rr = part.get("rear_light_rebate")
        if rr and m.is_watertight:
            # hátsó fényfalc: a kontúr-prizma kivonása az y_mm tartományban (globális X,Z kontúr)
            x, y, z = part["box"][:3]
            sub = extrude_outline_y({"box": [x, rr["y_mm"][0] - 1, z, 0, rr["y_mm"][1] - rr["y_mm"][0] + 1, 0],
                                     "outline": [[a - x, b - z] for a, b in rr["outline_xz_mm"]]})
            m = m.difference(sub, engine="manifold")
        if m.is_watertight:
            return Solid.from_mesh(name, m, "R14_kontur_extrudalas")
    if part.get("assembly_rebate"):
        try:
            m = box_mesh(part["box"]).difference(box_mesh(part["assembly_rebate"]))
            if m.is_watertight:
                return Solid.from_mesh(name, m, "doboz_minusz_kimetszes")
        except Exception:
            pass
    s = Solid(name, box=part["box"])
    s.method = "bbox"
    return s


class Solid:
    """Alkatrész-test: zárt háló, ha vízzáró; különben befoglaló doboz."""

    def __init__(self, name, box=None, vertices=None, faces=None):
        self.name = name
        self.mesh = None
        if vertices is not None and faces:
            try:
                m = mesh_from_obj(vertices, faces)
                if m.is_watertight and m.volume > 0:
                    self.mesh = m
                elif m.is_watertight and m.volume < 0:
                    m.invert()
                    self.mesh = m
            except Exception:  # pragma: no cover
                self.mesh = None
            v = np.asarray(vertices, float)
            self.lo, self.hi = v.min(0), v.max(0)
        else:
            self.lo, self.hi = box_min_max(box)
        self.method = "mesh" if self.mesh is not None else "bbox"

    @classmethod
    def from_mesh(cls, name, mesh, method):
        s = cls.__new__(cls)
        s.name, s.mesh, s.method = name, mesh, method
        s.lo, s.hi = mesh.bounds[0].copy(), mesh.bounds[1].copy()
        return s

    def contains(self, pts):
        pts = np.atleast_2d(pts)
        inb = np.all((pts > self.lo - 1e-6) & (pts < self.hi + 1e-6), axis=1)
        if self.mesh is None or not inb.any():
            return inb
        res = np.zeros(len(pts), bool)
        # determinisztikus: előjeles távolság (trimesh: belül pozitív); a sugaras contains véletlen irányt használ
        from trimesh.proximity import signed_distance
        res[inb] = signed_distance(self.mesh, pts[inb]) > 1e-6
        return res

    def bbox_overlap(self, other, tol=0.0):
        return bool(np.all(self.lo < other.hi - tol) and np.all(other.lo < self.hi - tol))


EL_PRIORITAS = {"SZABAD_ELOL": 0, "SZABAD_EGYEB": 1, "CSATLAKOZO": 2}


def etalon_el_kod(rec):
    """Él-kód az asztalos etalonjának (coo1.dwg) sorrendjében – FELTEVÉS, az asztalos megerősítéséig:
    hossz-él 1 (a látszó/elülső), hossz-él 2, szél-él 1, szél-él 2. A hosszél az L ≥ W oldal; E1/E3 az U (L) irányú élek.
    Indok: coo1 – Oldal V0VV (elöl V, hátul 0, fent/lent V), Polc/Tető V000 (csak az elülső él), Kötő VV00, Front AAAA.
    Visszaad: (kód, élsorrend)."""
    e = rec["elek"]
    L, W = rec["meret"]["kesz"]["L"], rec["meret"]["kesz"]["W"]
    hossz, szel = (["E1", "E3"], ["E4", "E2"]) if L >= W else (["E4", "E2"], ["E1", "E3"])
    key = lambda k: (EL_PRIORITAS.get(e[k]["szerep"], 9), k)
    order = sorted(hossz, key=key) + sorted(szel, key=key)
    return "".join(e[k]["jel"] for k in order), order

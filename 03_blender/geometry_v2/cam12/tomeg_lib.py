# Közös segédfüggvények a KEP-004 tömb- és kamerarenderekhez (Claude, 2026-10-25). A betöltött .blend-et NEM menti.
import bpy, math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
def alap_beallitas(sc):
    """Azonos a render_alapkepek_v2b1.py Cam_02/03/04 részével (semleges, bútor nélkül)."""
    r = sc.render; vs = sc.view_settings
    for c in bpy.data.collections:
        if c.name.startswith('Stil_') or c.name.startswith('VK_') or c.name == 'A902_Villamos_TERV': c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        if not o.name.startswith(MARAD): o.hide_render = True
    fal = bpy.data.materials['Fal_feher']
    for o in bpy.data.collections['A902_Falak'].objects:
        if o.name.startswith('Plafon'): continue
        for s in o.material_slots:
            if s.material and s.material.name != 'Fal_feher': s.material = fal
    r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
    sc.eevee.taa_render_samples = 128
    vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; r.image_settings.file_format = 'PNG'
    nt = sc.world.node_tree; bg = nt.nodes['Background']
    for l in list(nt.links):
        if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
    bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
    for o in bpy.data.objects:
        if o.type == 'LIGHT': o.hide_render = True
    vs.exposure = 0.75
_M = {}
def anyag(nev, v):
    if nev in _M: return _M[nev]
    m = bpy.data.materials.new(nev); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (v, v, v, 1); b.inputs['Roughness'].default_value = 0.85; _M[nev] = m; return m
SZIN = dict(kanape=0.30, etkezo=0.42, tv=0.22, kepernyo=0.02, tarolo=0.26, panel=0.36, mu=0.50)
def doboz(col, nev, a, b, fajta, log=None):
    me = bpy.data.meshes.new(nev); x0, y0, z0 = a; x1, y1, z1 = b
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    me.from_pydata(v, [], [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]); me.update()
    o = bpy.data.objects.new(nev, me); col.objects.link(o); me.materials.append(anyag('JEL_t_' + fajta, SZIN[fajta]))
    if log is not None: log[nev] = [round(t, 3) for t in tuple(a) + tuple(b)]
    return o
def u_kanape(col, X0, Y0, X1, Y1, D=0.90, log=None, elotag='T_kanape'):
    """U, hát kelet (X1) felé, nyitott nyugat (X0) felé."""
    U, H, HV = 0.42, 0.80, 0.20
    doboz(col, elotag + '_hat_ules', (X1 - D, Y0, 0), (X1, Y1, U), 'kanape', log)
    doboz(col, elotag + '_del_kar', (X0, Y0, 0), (X1 - D, Y0 + D, U), 'kanape', log)
    doboz(col, elotag + '_eszak_kar', (X0, Y1 - D, 0), (X1 - D, Y1, U), 'kanape', log)
    doboz(col, elotag + '_hattamla_k', (X1 - HV, Y0, U), (X1, Y1, H), 'kanape', log)
    doboz(col, elotag + '_hattamla_d', (X0, Y0, U), (X1 - HV, Y0 + HV, H), 'kanape', log)
    doboz(col, elotag + '_hattamla_e', (X0, Y1 - HV, U), (X1 - HV, Y1, H), 'kanape', log)
def l_kanape_del_sarok(col, XB, YS, YN, D, CH, CW, H=0.68, log=None, elotag='T_kanape'):
    """L: fő rész háttal kelet (XB) felé, y YS–YN; a sarokrész (chaise) a déli végén nyugat felé CH mélyen, CW szélesen."""
    U, HV = 0.42, 0.20
    doboz(col, elotag + '_fo_ules', (XB - D, YS + CW, 0), (XB, YN, U), 'kanape', log)
    doboz(col, elotag + '_chaise', (XB - CH, YS, 0), (XB, YS + CW, U), 'kanape', log)
    doboz(col, elotag + '_hattamla_k', (XB - HV, YS, U), (XB, YN, H), 'kanape', log)
    doboz(col, elotag + '_kartamla_e', (XB - D, YN - 0.18, U), (XB - HV, YN, 0.60), 'kanape', log)
def etkezo(col, AX0, AY0, AX1, AY1, szekek, log=None, elotag='T'):
    doboz(col, elotag + '_asztal_lap', (AX0, AY0, 0.72), (AX1, AY1, 0.75), 'etkezo', log)
    doboz(col, elotag + '_asztal_lab_d', (AX0 + 0.20, AY0 + 0.25, 0), (AX1 - 0.20, AY0 + 0.33, 0.72), 'etkezo', log)
    doboz(col, elotag + '_asztal_lab_e', (AX0 + 0.20, AY1 - 0.33, 0), (AX1 - 0.20, AY1 - 0.25, 0.72), 'etkezo', log)
    for i, (oldal, yc, sz, mely) in enumerate(szekek):
        if oldal == 'ny':
            x1 = AX0 + 0.18; x0 = x1 - mely
            doboz(col, f'{elotag}_szek_{i}_ules', (x0, yc - sz / 2, 0), (x1, yc + sz / 2, 0.46), 'etkezo', log)
            doboz(col, f'{elotag}_szek_{i}_hat', (x0, yc - sz / 2, 0.46), (x0 + 0.06, yc + sz / 2, 0.80), 'etkezo', log)
        else:
            x0 = AX1 - 0.18; x1 = x0 + mely
            doboz(col, f'{elotag}_szek_{i}_ules', (x0, yc - sz / 2, 0), (x1, yc + sz / 2, 0.46), 'etkezo', log)
            doboz(col, f'{elotag}_szek_{i}_hat', (x1 - 0.06, yc - sz / 2, 0.46), (x1, yc + sz / 2, 0.80), 'etkezo', log)
def tv(col, Y0, Y1, D=0.45, H=0.50, yk=None, log=None, elotag='T'):
    doboz(col, elotag + '_tv_konzol', (3.67, Y0, 0), (3.67 + D, Y1, H), 'tv', log)
    yk = (Y0 + Y1) / 2 if yk is None else yk
    doboz(col, elotag + '_tv_kepernyo', (3.70, yk - 0.725, 0.85), (3.75, yk + 0.725, 1.68), 'kepernyo', log)
def generikus_P902_24A(col, log=None):
    u_kanape(col, 4.77, 4.95, 7.17, 7.95, log=log)
    tv(col, 5.15, 6.95, yk=6.05, log=log)
    etkezo(col, 7.95, 5.37, 8.75, 7.17, [('ny', y, 0.45, 0.45) for y in (5.67, 6.27, 6.87)] + [('k', y, 0.45, 0.45) for y in (5.67, 6.27, 6.87)], log=log)
def kamera(nev, loc, rot, lens=20.0, col=None):
    cd = bpy.data.cameras.new(nev); cd.type = 'PERSP'; cd.lens = lens; cd.sensor_width = 36.0; cd.sensor_height = 24.0; cd.sensor_fit = 'AUTO'
    cd.clip_start = 0.1; cd.clip_end = 200.0
    o = bpy.data.objects.new(nev, cd); (col or bpy.context.scene.collection).objects.link(o); o.location = loc; o.rotation_mode = 'XYZ'; o.rotation_euler = rot
    return o
def vetit(sc, cam, P):
    p = world_to_camera_view(sc, cam, Vector(P)); return [round(p.x, 3), round(1 - p.y, 3), round(p.z, 2)]
def kepteri(sc, cam, o):
    pts = [world_to_camera_view(sc, cam, o.matrix_world @ Vector(c)) for c in o.bound_box]; pts = [p for p in pts if p.z > 0]
    if not pts: return None
    return [round(min(p.x for p in pts), 3), round(min(1 - p.y for p in pts), 3), round(max(p.x for p in pts), 3), round(max(1 - p.y for p in pts), 3)]

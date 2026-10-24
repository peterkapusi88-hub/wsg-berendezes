# Csak olvas: a v2b-1-k10 munkamásolat 05.1 környezete (ágyak, stílusrétegek, kamerák, fények). Claude, 2026-10-24.
import bpy, json, os, sys
OUT = sys.argv[sys.argv.index('--') + 1]
def wb(o):
    if o.type != 'MESH' or not o.data.vertices: return None
    M = o.matrix_world; pts = [M @ v.co for v in o.data.vertices]
    return [round(min(p[i] for p in pts), 3) for i in range(3)] + [round(max(p[i] for p in pts), 3) for i in range(3)]
cols = [[c.name, c.hide_render, len(c.objects), [ch.name for ch in c.children]] for c in bpy.data.collections]
room = (0.0, 3.45, 3.57, 8.95)
in051, beds = {}, []
for o in bpy.data.objects:
    b = wb(o)
    if 'agy' in o.name.lower() or 'bed' in o.name.lower():
        beds.append([o.name, [c.name for c in o.users_collection], b, o.hide_render])
    if b and b[3] > room[0] + 0.02 and b[0] < room[2] - 0.02 and b[4] > room[1] + 0.02 and b[1] < room[3] - 0.02 and b[2] < 2.85 and b[5] > 0.01:
        cn = o.users_collection[0].name if o.users_collection else '-'
        in051.setdefault(cn, []).append([o.name, b, [s.material.name for s in o.material_slots if s.material]])
cams = {o.name: dict(loc=[round(x, 4) for x in o.location], rot=[round(x, 4) for x in o.rotation_euler], lens=o.data.lens, coll=[c.name for c in o.users_collection]) for o in bpy.data.objects if o.type == 'CAMERA'}
lights = [[o.name, o.data.type, [round(x, 2) for x in o.location], o.hide_render, [c.name for c in o.users_collection]] for o in bpy.data.objects if o.type == 'LIGHT']
sc = bpy.context.scene; w = sc.world
res = dict(version=bpy.app.version_string, file=bpy.data.filepath, camera=sc.camera.name if sc.camera else None, engine=sc.render.engine,
           view=[sc.view_settings.view_transform, sc.view_settings.look, sc.view_settings.exposure], collections=cols, beds=beds,
           in051=in051, cams=cams, lights=lights, world=[[n.name, n.type] for n in w.node_tree.nodes] if w and w.node_tree else [],
           materials=sorted(m.name for m in bpy.data.materials))
json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('VIZSGALAT KESZ')

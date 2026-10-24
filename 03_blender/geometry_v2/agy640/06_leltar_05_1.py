# 05.1 leltár a matrix_basis-ből (a futásidejű matrix_world a nem kiértékelt objektumoknál Blender 5.2-ben egységmátrix).
import bpy, sys, json, mathutils
out = sys.argv[sys.argv.index('--') + 1]
def vilag(o):
    M = o.matrix_basis.copy(); p = o
    while p.parent:
        M = p.parent.matrix_basis @ p.matrix_parent_inverse @ M if p is o else M
        p = p.parent
    if o.parent:  # szülőlánc pontosan
        M = o.matrix_basis.copy(); q = o
        while q.parent:
            M = q.parent.matrix_basis @ q.matrix_parent_inverse @ M; q = q.parent
    return M
def bb(o):
    M = vilag(o)
    if o.type == 'MESH' and len(o.data.vertices): pts = [M @ v.co for v in o.data.vertices]
    else: pts = [M.translation.copy()]
    return [round(min(p[i] for p in pts), 3) for i in range(3)] + [round(max(p[i] for p in pts), 3) for i in range(3)]
R = []
for cn in ('A902_Butor', 'Stil_Zenit', 'Stil_LakeForest'):
    c = bpy.data.collections[cn]
    for o in c.all_objects:
        b = bb(o)
        if b[3] < -0.1 or b[0] > 3.7 or b[4] < 3.9 or b[1] > 9.0: continue
        R.append(dict(nev=o.name, koll=cn, tipus=o.type, bb=b, loc=[round(v, 3) for v in o.location], szulo=o.parent.name if o.parent else None,
                      mw_eltér=max(abs(a - b) for a, b in zip(o.matrix_world.translation, vilag(o).translation)) > 1e-4))
json.dump(R, open(out, 'w'), ensure_ascii=False, indent=0)
print('DB', len(R))

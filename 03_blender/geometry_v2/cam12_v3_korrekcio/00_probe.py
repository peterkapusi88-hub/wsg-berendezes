# Cam_12 v3 korrekció – csak olvasó felmérés a MÁSOLAT blendből (Claude, 2026-10-25). NEM MENT.
import bpy, math, json, sys, os, hashlib
from mathutils import Vector
OUT = sys.argv[sys.argv.index('--') + 1]
sc = bpy.context.scene
c = bpy.data.objects['Cam_12_Nappali_Hero']; d = c.data
fwd = c.matrix_world.to_3x3() @ Vector((0, 0, -1)); up = c.matrix_world.to_3x3() @ Vector((0, 1, 0))
r = dict(blender=bpy.app.version_string, file=bpy.data.filepath,
         sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(), scene=sc.name,
         cam=dict(loc=[round(v, 5) for v in c.matrix_world.translation], rot_deg=[round(math.degrees(a), 4) for a in c.rotation_euler],
                  mode=c.rotation_mode, lens=d.lens, sensor=[d.sensor_width, d.sensor_height, d.sensor_fit], shift=[d.shift_x, d.shift_y],
                  clip=[d.clip_start, d.clip_end], parent=str(c.parent), fwd=[round(v, 5) for v in fwd], up=[round(v, 5) for v in up],
                  heading_deg=round(math.degrees(math.atan2(fwd.y, fwd.x)), 4), pitch_deg=round(math.degrees(math.asin(max(-1, min(1, fwd.z)))), 4),
                  hfov_deg=round(math.degrees(2 * math.atan(d.sensor_width / 2 / d.lens)), 3)),
         render=dict(res=[sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage], engine=sc.render.engine,
                     vt=sc.view_settings.view_transform, look=sc.view_settings.look, exp=sc.view_settings.exposure, camera=sc.camera.name if sc.camera else None),
         colls={}, mats={}, world=None)
for col in bpy.data.collections:
    r['colls'][col.name] = dict(n=len(col.objects), hide_render=col.hide_render, objs=[(o.name, o.type, [s.material.name if s.material else None for s in o.material_slots], o.hide_render) for o in col.objects][:400])
for m in bpy.data.materials:
    e = dict(users=m.users)
    if m.use_nodes and m.node_tree and 'Principled BSDF' in m.node_tree.nodes:
        b = m.node_tree.nodes['Principled BSDF']; e['base'] = [round(x, 3) for x in b.inputs['Base Color'].default_value]; e['rough'] = round(b.inputs['Roughness'].default_value, 3)
        e['linked_base'] = b.inputs['Base Color'].is_linked
    r['mats'][m.name] = e
if sc.world and sc.world.node_tree:
    r['world'] = [(n.name, n.type) for n in sc.world.node_tree.nodes]
r['lights'] = [(o.name, o.data.type, o.data.energy, list(o.location), o.hide_render) for o in bpy.data.objects if o.type == 'LIGHT']
r['eevee'] = {k: getattr(sc.eevee, k) for k in dir(sc.eevee) if k.startswith(('use_gtao', 'gtao', 'taa', 'use_shadow', 'use_raytracing', 'fast_gi', 'ray_tracing')) and not callable(getattr(sc.eevee, k))}
r['eevee'] = {k: (v if isinstance(v, (int, float, bool, str)) else str(v)) for k, v in r['eevee'].items()}
os.makedirs(OUT, exist_ok=True)
json.dump(r, open(os.path.join(OUT, 'probe.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(OUT, 'probe.done'), 'w').write('KESZ')

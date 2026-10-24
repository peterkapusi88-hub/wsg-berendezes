# =====================================================================================
# STÁTUSZ: ELŐZETES / NEM VALIDÁLT – KÍSÉRLETI, FÉLBEHAGYOTT RENDERSZKRIPT (2026-10-24)
# Két próbafuttatás FAIL lett (bézs fal, homokszínű/napfoltos padló), a kép NINCS a repóban.
# CSAK KÉZI futtatásra: semmi (workflow, Validator, más szkript, ütemezett feladat) nem hívja.
# Nem írja felül az élő .blend-et; kimenete nem referencia. Ld. 03_blender/validator_report_2026-10-24_semleges_v2.md
# =====================================================================================
if __name__ == "__main__" and False:  # biztosíték: importkor/véletlen futtatáskor nem csinál semmit
    pass
# A-902 semleges geometria-alap v2 – Cam_02 (nappali → terasz)
# Bemenet: 03_blender/WSG_A902_v2_terasz_ELOZETES_20261024.blend MÁSOLATA (az élő fájlt és a repófájlt nem írja felül).
# Változtatás csak a másolaton, csak megjelenés: bútor- és stílusrétegek rejtve; nyílászáró-profilok BELÜL FEHÉR (IGAZOLT-F),
# beltéri ajtólap világosszürke, tok szürke (IGAZOLT-F). Geometria nem változik. Validátor a render előtt fut.
# Futtatás (bpy 5.2.3 modul, NEM a szkript mappájából indítva):
#   python3 -c "import sys,bpy; sys.argv=['x','<v2 másolat.blend>','<repo>/03_blender/geometry_lock_A902.json','<kimeneti mappa>']; exec(open('<ez a fájl>').read())"
# Kimenet: A902_semleges_v2_1_nappali.png + validator_result.json
import bpy, sys, os, json
blend, lock, outdir = sys.argv[-3], sys.argv[-2], sys.argv[-1]
bpy.ops.wm.open_mainfile(filepath=blend)
os.environ['WSG_LOCK'] = lock

for cname in ('A902_Butor', 'Stil_LakeForest', 'Stil_Zenit', 'A902_Terasz'):
    bpy.data.collections[cname].hide_render = True
    for o in bpy.data.collections[cname].objects: o.hide_viewport = True

def mat(name, rgb, rough):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Roughness'].default_value = rough
    return m
white_frame = mat('v2_nyilaszaro_belul_feher', (0.82, 0.82, 0.81), 0.45)
door_leaf = mat('v2_belteri_ajto_vilagosszurke', (0.55, 0.56, 0.57), 0.5)
door_frame = mat('v2_belteri_ajtotok_szurke', (0.45, 0.46, 0.47), 0.5)
changed = []
for o in bpy.data.collections['A902_Nyilaszarok'].objects:
    for s in o.material_slots:
        if not s.material: continue
        n = o.name
        if (n.startswith('Uvegfal_') or n.startswith('Erkelyajto_')) and s.material.name == 'Fekete_fem':
            s.material = white_frame; changed.append(n)
        elif n.startswith('Ajto_') and not n.startswith('Ajto_bejarat'):
            if n.endswith('_lap'): s.material = door_leaf; changed.append(n)
            elif '_tok_' in n: s.material = door_frame; changed.append(n)

# --- v2b kalibráció a 2026-10-21-i helyszíni fotókhoz (ME-BAL-045, -080) ---
# falak/mennyezet semleges fehér; padló közepes, szürkésbarna tölgy-tónus (sRGB ~118/112/106) zajjal, DESZKAMINTA NINCS MODELLEZVE
for mn in ('Fal_feher', 'Plafon_feher'):
    m = bpy.data.materials[mn]; b = m.node_tree.nodes.get('Principled BSDF')
    if b: b.inputs['Base Color'].default_value = (0.78, 0.78, 0.78, 1); b.inputs['Roughness'].default_value = 0.9
pm = bpy.data.materials['v2_parketta_GreyTreviso_EL2184_foto']
for n in pm.node_tree.nodes:
    if n.type == 'VALTORGB':
        els = n.color_ramp.elements
        els[0].color = (0.140, 0.128, 0.116, 1); els[-1].color = (0.215, 0.198, 0.180, 1)
# nem igazolt irányú napfény ki; csak égbolt-szórt fény; JELÖLŐ-k rejtve
bpy.data.objects['Nap'].hide_render = True
for o in bpy.data.objects:
    if any(s.material and s.material.name == 'v2_JELOLO_narancs' for s in o.material_slots): o.hide_render = True
for o in bpy.data.collections['Kamerak_Fenyek'].objects:
    if o.type == 'LIGHT' and o.name.startswith('L_'): o.hide_render = True
bpy.context.scene.view_settings.exposure = 1.3
ns = {}
exec(open(os.path.join(os.path.dirname(lock), 'geometry_validator.py')).read(), ns)
json.dump(ns['result'], open(os.path.join(outdir, 'validator_result.json'), 'w'), ensure_ascii=False, indent=1, default=str)

sc = bpy.context.scene
sc.camera = bpy.data.objects['Cam_02_Nappali_terasz']
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = 64; sc.cycles.use_denoising = True
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1600, 1000, 100
sc.view_settings.view_transform = 'AgX'
sc.render.image_settings.file_format = 'PNG'
sc.render.filepath = os.path.join(outdir, 'A902_semleges_v2_1_nappali.png')
bpy.ops.render.render(write_still=True)
print('CHANGED', len(changed)); print('DONE', sc.render.filepath)

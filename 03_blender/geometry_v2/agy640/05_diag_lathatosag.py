import bpy, sys, json
out = sys.argv[sys.argv.index('--') + 1]
koll = 'Stil_Zenit'
r = {'kollekciok': {c.name: dict(hide_render=c.hide_render, gyerekek=[g.name for g in c.children], n=len(c.objects)) for c in bpy.data.collections if c.name.startswith(('Stil_', 'A902_Butor'))}}
for c in bpy.data.collections:
    if c.name.startswith('Stil_'): c.hide_render = c.name != koll
n_all = len(bpy.data.collections[koll].all_objects)
for o in bpy.data.collections[koll].all_objects: o.hide_render = o.name not in ('Z_agy_keret',)
def allapot(n):
    o = bpy.data.objects.get(n)
    if not o: return None
    ad = o.animation_data
    return dict(hide_render=o.hide_render, koll=[c.name for c in o.users_collection], tipus=o.type,
                drivers=[d.data_path for d in ad.drivers] if ad else [], action=bool(ad and ad.action), loc=[round(v, 3) for v in o.location])
r['all_objects_db'] = n_all
r['elotte'] = {n: allapot(n) for n in ('Z_lampa_kar_0', 'Z_TV55', 'Z_agy_keret', 'Z_gyuru_0')}
bpy.context.view_layer.update()
r['update_utan'] = {n: allapot(n) for n in ('Z_lampa_kar_0', 'Z_TV55', 'Z_agy_keret', 'Z_gyuru_0')}
r['lathato_Zenit_mesh'] = [o.name for c in bpy.data.collections if c.name.startswith('Stil_') and not c.hide_render for o in c.objects if o.type == 'MESH' and not o.hide_render][:20]
json.dump(r, open(out, 'w'), ensure_ascii=False, indent=1)

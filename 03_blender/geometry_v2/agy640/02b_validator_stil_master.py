# Validator v2 – stílusréteg-master módok (2026-10-25): zenit_master | lakeforest_master.
# Csak az adott Stil_ gyűjtemény 05.1 master-objektumai láthatók (ágy, éjjeli, olvasólámpa, szőnyeg, LF bronzcsík);
# az A902_Butor teljesen rejtve. Nem ment. Futtatás: Blender -b <fájl.blend> --python 02b_validator_stil_master.py -- <mód> <címke>
import bpy, os, sys, runpy
W = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/'
L = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/'
MASTER = {
 'zenit_master': ('Stil_Zenit', ['Z_agy_keret', 'Z_agy_matrac', 'Z_agy_pled', 'Z_agy_takaro', 'Z_ejjeli_0', 'Z_ejjeli_1', 'Z_olvasolampa_0',
                  'Z_olvasolampa_1', 'Z_olvasolampa_feny_0', 'Z_olvasolampa_feny_1', 'Z_master_szonyeg']),
 'lakeforest_master': ('Stil_LakeForest', ['L_agy_keret', 'L_agy_matrac', 'L_agy_takaro', 'L_agyfal_bronz', 'L_ejjeli_0', 'L_ejjeli_1',
                       'L_ejjeli_lap_0', 'L_ejjeli_lap_1', 'L_olvasolampa_0', 'L_olvasolampa_1', 'L_olvasolampa_feny_0',
                       'L_olvasolampa_feny_1', 'L_master_szonyeg'])}
mod, cimke = sys.argv[sys.argv.index('--') + 1:][:2]
koll, nevek = MASTER[mod]
for c in bpy.data.collections:
    if c.name.startswith('Stil_'): c.hide_render = c.name != koll
bpy.data.collections['A902_Butor'].hide_render = True
for o in bpy.data.collections['A902_Butor'].objects: o.hide_render = True
# .objects (nem .all_objects): Blender 5.2-ben az all_objects-en át írt hide_render nem maradt meg (05_diag.json); gyerekgyűjtemény nincs
assert not bpy.data.collections[koll].children
for o in bpy.data.collections[koll].objects: o.hide_render = o.name not in nevek
lathato = sorted(o.name for o in bpy.data.collections[koll].objects if not o.hide_render); assert lathato == sorted(nevek), lathato
os.environ.setdefault('WSG_LOCK', L + 'lock_k11/geometry_lock_A902_v2b.json')   # a futtató felülírhatja (PR-lock)
os.environ['WSG_VILLAMOS'] = L + 'A902_villamos.json'
os.environ['WSG_REPORT_JSON'] = W + f'validator_{cimke}_{mod}.json'
runpy.run_path(L + 'geometry_validator_v2.py')

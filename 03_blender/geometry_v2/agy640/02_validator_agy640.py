# Validator v2 – módok: ures | referencia | master_butor (csak a 05.1 master bútorai láthatók: ágy, éjjeliszekrény, lámpa, szőnyeg).
# Nem ment. Futtatás: Blender -b <fájl.blend> --python 02_validator_agy640.py -- <mód> <címke>
import bpy, os, sys, runpy
W = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_agy640_v1/'
L = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/'
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
MASTER = ('Agy_05_1_', 'Ejjeli_05_1_', 'Szonyeg_05_1_')
mod, cimke = sys.argv[sys.argv.index('--') + 1:][:2]
for c in bpy.data.collections:
    if c.name.startswith('Stil_'): c.hide_render = True
bpy.data.collections['A902_Butor'].hide_render = False
for o in bpy.data.collections['A902_Butor'].objects:
    if mod == 'ures': o.hide_render = True
    elif mod == 'referencia': o.hide_render = not o.name.startswith(MARAD)
    elif mod == 'master_butor': o.hide_render = not o.name.startswith(MASTER)
    else: raise SystemExit('ismeretlen mód ' + mod)
os.environ.setdefault('WSG_LOCK', L + 'lock_k11/geometry_lock_A902_v2b.json')   # a futtató felülírhatja (PR-lock)
os.environ['WSG_VILLAMOS'] = L + 'A902_villamos.json'
os.environ['WSG_REPORT_JSON'] = W + f'validator_{cimke}_{mod}.json'
runpy.run_path(L + 'geometry_validator_v2.py')

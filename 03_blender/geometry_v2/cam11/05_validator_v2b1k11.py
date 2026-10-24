# Validator v2 a v2b-1-k11 JAVASLAT fájlon, a Cam_11-gyel bővített lockkal – nem ment. Módok: ures | referencia.
import bpy, os, sys, runpy
W = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/'
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
mod = sys.argv[sys.argv.index('--') + 1]
for c in bpy.data.collections:
    if c.name.startswith('Stil_'): c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    if mod == 'ures' or not o.name.startswith(MARAD): o.hide_render = True
os.environ['WSG_LOCK'] = W + 'lock_k11/geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = W + 'A902_villamos.json'
os.environ['WSG_REPORT_JSON'] = W + f'validator_v2b1k11_cam11_{mod}.json'
g = runpy.run_path(W + 'geometry_validator_v2.py')
r = g.get('result', {})
print('VALIDATOR', mod, r.get('status') or r.get('statusz'), len(r.get('errors', r.get('hibak', []))), len(r.get('warnings', r.get('figyelmeztetesek', []))))

# Validator v2 futtatása a referencia-állapotban (stílusrétegek és bútor rejtve, beépített szaniterek láthatók) – nem ment.
import bpy, os, sys, runpy, json
D = '/Users/peterkapusi/Downloads/WSG/_claude_kep004_alap_20261024/'
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
mod = sys.argv[sys.argv.index('--')+1]
if mod == 'ures':
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects: o.hide_render = True
if mod == 'referencia':
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        if not o.name.startswith(MARAD): o.hide_render = True
os.environ['WSG_LOCK'] = D + 'geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = D + 'A902_villamos.json'
os.environ['WSG_REPORT_JSON'] = D + f'validator_v2b1_kam10_{mod}.json'
g = runpy.run_path(D + 'geometry_validator_v2.py')
r = g.get('result', {})
print('VALIDATOR', mod, r.get('status') or r.get('statusz'), len(r.get('errors', r.get('hibak', []))), len(r.get('warnings', r.get('figyelmeztetesek', []))))

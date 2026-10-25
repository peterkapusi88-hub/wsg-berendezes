# A 10_BLOKK_VALIDALAS.md tételtáblájának generálása a blokk_spec-ből és a Blender-naplóból (bbox, képi hely). Claude, 2026-10-25.
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import blokk_spec as BS
L = json.load(open(os.path.join(HERE, 'naplok', 'cam12v3_korr_log.json'), encoding='utf-8'))
f = lambda v: f'{v:.3f}'.rstrip('0').rstrip('.').replace('.', ',')
out = []
for st in ('S01', 'S02'):
    out.append(f'\n### {st}\n\n| ID | termék / elem | befoglaló Δx × Δy × Δz (m) | hely: x0–x1 · y0–y1 · z0–z1 (Blender-bbox) | Cam_12-ben | állapot | forrás |\n|---|---|---|---|---|---|---|')
    for e in BS.K:
        if e['st'] != st: continue
        n = e['id'].replace('-', '_')
        objs = [k for k in L['blokkok'] if k == n or k.startswith(n + '_')]
        if not objs: continue
        bb = [min(L['blokkok'][o]['bbox'][i] for o in objs) for i in range(3)] + [max(L['blokkok'][o]['bbox'][i] for o in objs) for i in range(3, 6)]
        px = [L['blokkok'][o].get('kep_px') for o in objs]; px = [p for p in px if p]
        kep = f'x {min(p[0] for p in px)}–{max(p[2] for p in px)} px' if px else 'képen kívül'
        meret = f'{f(bb[3] - bb[0])} × {f(bb[4] - bb[1])} × {f(bb[5] - bb[2])}'
        if e['tipus'] == 'chair':
            meret = f"{f(e['g'][4])} × {f(e['g'][5])} × {f(e['g'][7])} (széktömb sz × mé × m, betolva 0,18)"
            # a betolt szék: a 6 szék egyenként
        hely = f'{f(bb[0])}–{f(bb[3])} · {f(bb[1])}–{f(bb[4])} · {f(bb[2])}–{f(bb[5])}'
        out.append(f"| {e['id']} | {e['nev']} | {meret} | {hely} | {kep} | {e['allapot']} | {e['forras']} |")
open(os.path.join(HERE, 'blokk_tabla.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out)[:3000])

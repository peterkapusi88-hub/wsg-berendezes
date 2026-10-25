# 03 kiegészítés (Claude integrátor, 2026-10-25): 1 cm-es útfelbontás az S05 05.3-útjára és az S04 hálók-útjára (olajfa nélkül / csak dohányzóasztallal),
# az S08 MR-1 torony 45 cm-es „biztonsági” mélységgel (Opus gazdaságos változata). A 03-as szkript függvényeit használja.
import os, json, runpy
from shapely.geometry import box
from shapely.ops import unary_union
HERE = os.path.dirname(os.path.abspath(__file__))
import builtins; _p = builtins.print; builtins.print = lambda *a, **k: None
G = runpy.run_path(os.path.join(HERE, '03_kozlekedes_2d_opus_S04_S10.py')); builtins.print = _p
E = G['E']; E.SZELESSEG = [round(0.50 + 0.01 * i, 2) for i in range(61)]
out = []
for kod in ('S05', 'S04'):
    for ext in (True, False):
        r = G['mer'](kod, 'kozepso', extra_be=ext); out.append(r); print(kod, 'extra' if ext else 'extra nélkül', r['utak_betolt'], 'OK' if r['kotelezo_ok'] else 'NEM')
s0 = G['stilus']
def s08_45(kod):
    s = s0('S08'); t = box(3.71, 4.45, 4.16, 5.05); s['tv'] = unary_union([box(3.67, 4.05, 3.71, 8.05), t, box(3.71, 5.05, 4.11, 7.45)]); s['torony'] = t; s['kanape_nev'] += ' – MR-1 45 cm'; return s
G['stilus'].__globals__['stilus'] = lambda kod: s08_45(kod) if kod == 'S08_45' else s0(kod)
for tz in ('kozepso', 'keleti'):
    r = G['mer']('S08_45', tz); out.append(r); print('S08 torony 45 cm', tz, r['utak_betolt'], 'torony', r['kanape_torony'], 'OK' if r['kotelezo_ok'] else 'NEM')
json.dump(out, open(os.path.join(HERE, '03b_finomitas_S04_S05_S08.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

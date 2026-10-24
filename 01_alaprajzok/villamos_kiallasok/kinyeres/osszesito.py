#!/usr/bin/env python3
"""Az OSSZESITO.md előállítása a <LAKÁS>_villamos.json fájlokból (a kinyerés után futtatandó)."""
import json, os, collections
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fmt = lambda v: ('%.2f' % v).replace('.', ',') if isinstance(v, (int, float)) else (v or '')
L = ['# Villamos kiállások – lakásonkénti összesítő',
     '',
     '> Generált fájl (`kinyeres/osszesito.py`). A teljes, tételes lista a `<LAKÁS>_villamos.csv` / `.json` fájlokban van.',
     '> Minden adat **TERV SZERINT**; a helyszíni ellenőrzésig nem HELYSZÍNEN MÉRT. Koordináták méterben, lakásonkénti rendszerben (lásd README).',
     '']
NICE = {'mennyezeti_lampakiallas': 'mennyezeti lámpa', 'fali_lampakiallas': 'fali lámpa', 'kapcsolo': 'kapcsoló', 'dugalj': 'dugalj',
        'gyengearamu_aljzat': 'gyengeáram', 'antenna_tv_aljzat': 'TV/antenna', 'ventilator_kiallas': 'ventilátor', 'R_jelu_kiallas': 'R (redőny?)',
        'termosztat': 'termosztát'}
for flat in ('A811', 'A812', 'A902'):
    d = json.load(open(os.path.join(OUT, f'{flat}_villamos.json')))
    m = d['meta']; K = d['kiallasok']; Z = d['hutes_futes_zonak']
    L += [f"## {m['lakas']}", '', f"Forrás: `WGR1_meretezett_alaprajzok.pdf` {m['oldal']}. oldal (dosszié {m['dosszie']}), {m['lepték']}, {m['verzio']}.", '',
          f"Koordináta-origó: {m['koordinatak']['origo']}", '']
    c = collections.Counter(r['tipus'] for r in K)
    L += ['| Típus | db |', '|---|---|'] + [f'| {t} | {n} |' for t, n in sorted(c.items(), key=lambda x: -x[1])] + ['']
    L += ['### Mennyezeti lámpakiállások', '', '| Azonosító | Helyiség | Áramkör | x | y |', '|---|---|---|---|---|']
    for r in K:
        if r['tipus'] == 'mennyezeti_lampakiallas':
            L.append(f"| {r['azonosito']} | {r['helyiseg']} | {r['aramkor']} | {fmt(r['x_m'])} | {fmt(r['y_m'])} |")
    L += ['', '### Fali lámpakiállások', '', '| Azonosító | Helyiség | Áramkör | x | y | Magasság |', '|---|---|---|---|---|---|']
    for r in K:
        if r['tipus'] == 'fali_lampakiallas':
            L.append(f"| {r['azonosito']} | {r['helyiseg']} | {r['aramkor']} | {fmt(r['x_m'])} | {fmt(r['y_m'])} | {fmt(r['magassag_m']) or 'nincs a rajzon'} |")
    L += ['', '### Helyiségenként (darab)', '']
    cols = ['mennyezeti_lampakiallas', 'fali_lampakiallas', 'kapcsolo', 'dugalj', 'gyengearamu_aljzat', 'antenna_tv_aljzat', 'ventilator_kiallas', 'R_jelu_kiallas', 'termosztat']
    L += ['| Helyiség | ' + ' | '.join(NICE[c] for c in cols) + ' | egyéb |', '|---' * (len(cols) + 2) + '|']
    rooms = sorted(set(r['helyiseg'] for r in K))
    for rm in rooms:
        rr = [r for r in K if r['helyiseg'] == rm]
        cc = collections.Counter(r['tipus'] for r in rr)
        other = [r['tipus'] for r in rr if r['tipus'] not in cols]
        L.append(f"| {rm} | " + ' | '.join(str(cc.get(c, '')) for c in cols) + f" | {', '.join(sorted(set(other)))} |")
    L += ['', '### Mennyezeti hűtő-fűtő mezők (ide nem fúrunk)', '', '| Azonosító | Helyiség | x-tól | x-ig | y-tól | y-ig |', '|---|---|---|---|---|---|']
    for z in Z:
        L.append(f"| {z['azonosito']} | {z['helyiseg']} | {fmt(z['x_min'])} | {fmt(z['x_max'])} | {fmt(z['y_min'])} | {fmt(z['y_max'])} |")
    L += ['', f"Átfedéskép: `{flat}_villamos_atfedes.png` · Tételes lista: `{flat}_villamos.csv`", '']
open(os.path.join(OUT, 'OSSZESITO.md'), 'w').write('\n'.join(L) + '\n')
print('OSSZESITO.md kész')

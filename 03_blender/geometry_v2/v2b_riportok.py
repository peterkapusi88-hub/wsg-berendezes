#!/usr/bin/env python3
"""v2b riportok: eltéréslista (előtte–utána), validátor-riport (v2 alap vs v2b), kamera-paraméterlap.
Bemenet: v2b_valtozasok.json, geometry_lock_A902_v2b.json, a geometry_validator_v2.py két JSON-kimenete.
    python3 v2b_riportok.py <validator_v2_alap.json> <validator_v2b.json>
"""
import json, os, sys, collections
G = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(G)
C = json.load(open(os.path.join(G, 'v2b_valtozasok.json'), encoding='utf-8'))
L = json.load(open(os.path.join(B, 'geometry_lock_A902_v2b.json'), encoding='utf-8'))
f2 = lambda v: ('%.3f' % v).rstrip('0').rstrip('.').replace('.', ',') if isinstance(v, (int, float)) else str(v)
bb = lambda b: '[' + '; '.join(f2(v) for v in b) + ']' if b else '–'
def dmax(a, b):
    return max(abs(x - y) for x, y in zip(a, b)) if a and b else None

# 1) eltéréslista
out = ['# A-902 geometria v2b – eltéréslista (v2 → v2b), 2026-10-24', '',
       f"Alap: `{C['alap']}` (változatlan). Kimenet: `{C['kimenet']}` (új fájl). Az élő `WSG_A902_stilusok.blend` érintetlen; a tetőkert (A902_Terasz_v2_ELOZETES, 43 elem) változatlan.", '',
       'Forrás-hierarchia: (1) méretezett megvalósulási alaprajz M1 KORR 2 (PDF vektor, 18. o.), (2) műszaki ellenőri mérés, (3) fotó/videó, (4) Blender v1/v2, (5) becslés = ELŐZETES.',
       'Bbox-formátum: [x0; y0; z0; x1; y1; z1] m, vakolatlan tervsíkok. A bútor nem mozdult – az új falakkal ütköző bútort a validátor-riport listázza.', '',
       '**Státuszosztályok:** TERV SZERINT IGAZOLT · HELYSZÍNEN MÉRT · FOTÓVAL ALÁTÁMASZTOTT · ELŐZETES · MÉRENDŐ', '']
by = collections.defaultdict(list)
for r in C['valtozasok']: by[r['tipus']].append(r)
cnt = collections.Counter(r['statusz'] for r in C['valtozasok'])
out += ['| Státusz | db |', '|---|---|'] + [f'| {k} | {v} |' for k, v in cnt.most_common()] + ['']
names = {'fal': 'Falak', 'uj_fal': 'Új falelemek', 'nyilas': 'Nyílászárók (tok, lap, profil, üveg)', 'ajto': 'Ajtók', 'ablak': 'Üvegfalak, erkélyajtók',
         'padlo': 'Padlók', 'uj_padlo': 'Új padlók', 'rejtett_padlo': 'Elavult, rejtett padlók'}
for t, rows in by.items():
    out += [f'## {names.get(t, t)} ({len(rows)})', '', '| Elem | Régi bbox | Új bbox | max Δ | Státusz | Bizonyíték |', '|---|---|---|---|---|---|']
    for r in rows:
        d = dmax(r.get('regi'), r.get('uj'))
        out.append(f"| `{r['nev']}` | {bb(r.get('regi'))} | {bb(r.get('uj'))} | {('%.0f cm' % (d * 100)) if d is not None else 'új'} | {r['statusz']} | {r.get('bizonyitek', '')} |")
    out.append('')
out += [f"## Anyagok ({len(C['anyagok'])} objektum) – FOTÓVAL ALÁTÁMASZTOTT", '',
        'Belül fehér nyílászáró-profil, világosszürke beltéri ajtólap, szürke tok, fehér fal és mennyezet, szürkésbarna parkettatónus (deszkaminta nincs modellezve).', '']
c2 = collections.Counter(a['valtozas'] for a in C['anyagok'])
out += ['| Változás | db |', '|---|---|'] + [f'| {k} | {v} |' for k, v in c2.most_common()] + ['']
out += ['## Nem változott, MÉRENDŐ (hétfő)', '',
        '- Terasz: a WPC-nyelv bejáratát keresztező betonszegély, a lépcső helye, a zöldtető +0,77 m-es szintje (Codex-audit 3.) – a modellben nem javítottuk, mert nincs bizonyíték.',
        '- Teraszüvegezés osztása (ME-BAL-045 fotó vs terv) – a terv szerinti 4,50 m-es tolóajtó maradt.',
        '- Vakolt falsíkok (a terv vakolatlan; kb. 1–2 cm-rel beljebb).', '']
open(os.path.join(G, 'v2b_elteresi_lista.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# 2) kamera-paraméterlap
K = ['# A-902 v2b – kamera-paraméterlap (2026-10-24)', '', 'A lockba rögzítve (`geometry_lock_A902_v2b.json` → `cameras`); a validátor v2 minden paramétert ellenőriz.', '',
     '| Kamera | Típus | Fókusz mm | Szenzor | Illesztés | Shift x/y | Clip | Hely [x; y; z] | Forgatás [rad] | Státusz |', '|---|---|---|---|---|---|---|---|---|---|']
for n, c in L['cameras'].items():
    K.append(f"| {n} | {c.get('tipus')} | {f2(c.get('lens_mm'))}{(' (ortho ' + f2(c.get('ortho_scale')) + ')') if c.get('tipus') == 'ORTHO' else ''} | {f2(c.get('sensor_width'))}×{f2(c.get('sensor_height'))} | {c.get('sensor_fit')} | {f2(c.get('shift_x'))}/{f2(c.get('shift_y'))} | {f2(c.get('clip_start'))}–{f2(c.get('clip_end'))} | {bb(c.get('loc'))} | {bb(c.get('rot'))} | {c.get('statusz', '')} |")
r = L.get('render', {})
K += ['', f"Render: {json.dumps(r, ensure_ascii=False)}", '']
open(os.path.join(G, 'kamera_parameterlap_v2b.md'), 'w', encoding='utf-8').write('\n'.join(K) + '\n')

# 3) validátor-riport
if len(sys.argv) >= 3:
    A = json.load(open(sys.argv[1], encoding='utf-8')); V = json.load(open(sys.argv[2], encoding='utf-8'))
    def cat(lst): return collections.Counter(e.split(':')[0].strip() for e in lst)
    R = ['# Validátor-riport – A-902 geometria v2b (2026-10-24)', '',
         '> **Státusz: ELŐZETES – a geometria TERV SZERINT javítva, a bútorréteg még nem.** PASS csak 0 hibánál; a v2b FAIL a régi bútor és az új falak/kiállások ütközése miatt, ami tervezési feladat, nem geometriai hiba.', '',
         f"- Szkript: `03_blender/geometry_validator_v2.py` · Lock: `geometry_lock_A902_v2b.json` · Kiállások: `01_alaprajzok/villamos_kiallasok/A902_villamos.json` (PR #4)",
         f"- Látható stílusréteg: {V['stilus']} · aktív kamera: {V['measurements'].get('aktiv_kamera')}", '',
         '| Futás | Eredmény | Hibák kategóriánként | Figyelmeztetések |', '|---|---|---|---|',
         f"| v2 alap (előtte) | {A['summary']} | {dict(cat(A['errors']))} | {dict(cat(A['warnings']))} |",
         f"| **v2b (utána)** | **{V['summary']}** | {dict(cat(V['errors']))} | {dict(cat(V['warnings']))} |", '',
         'A v2 alap 125 LOCK-hibája pontosan a v2b javításai (lásd `geometry_v2/v2b_elteresi_lista.md`); a v2b-ben LOCK 0, TERASZ 0 változás.', '',
         '## Rendben', ''] + [f'- {x}' for x in V['ok']] + ['', '## Hibák (v2b)', '']
    for k, n in cat(V['errors']).most_common():
        R += [f'### {k} ({n})', ''] + [f'- {e.split(":", 1)[1].strip()}' for e in V['errors'] if e.split(':')[0].strip() == k] + ['']
    R += ['## Figyelmeztetések (v2b, összesítve)', '']
    for k, n in cat(V['warnings']).most_common():
        ex = [e.split(':', 1)[1].strip() for e in V['warnings'] if e.split(':')[0].strip() == k][:6]
        R += [f'- **{k}** ({n}): ' + ' · '.join(ex) + (' …' if n > 6 else '')]
    R += ['', '## Információ', ''] + [f'- {i}' for i in V['info']] + ['',
          '## Mit jelent a tervezésnek', '',
          '- **Konyha:** a régi (LF) konyhasor a javított keleti falba (x 10,55) és a csonkfalba lóg; a két pultsor tiszta köze 85 cm (cél 90). Újratervezendő a v2b falakhoz.',
          '- **Nappali, Lake Forest TV-fal:** a déli falon (x 5,55–7,40) **eltakarja a fő kapcsolóoszlopot, a termosztátot és a mozgásérzékelőt** (A902-K10–K12, T01, S01, fali hely x 7,15 y 4,05). A terv szerinti TV-blokk a nyugati válaszfalon van (y 6,0–6,5).',
          '- **05.1:** a LF ágyfal-travertin a 65 cm-es ágy melletti kapcsolókat (t) és az ajtósarki mozgásérzékelőt (S08, becsült 2,2 m) takarja; a gardrób a 05.1 ajtó melletti kapcsolókat, termosztátot és a BK-dobozt.',
          '- **05.2:** a 160×200-as ágy a jelenlegi helyén az ajtó nyitási negyedkörében van. A forgásokon kívül: 160-as ágy fejjel a déli falnak x 1,00–2,60 (oldalt 100/105 cm, lábnál 60 cm), vagy 140-es x 1,10–2,50. A PAX 240 a 05.2 ajtó melletti kapcsolót (s) és termosztátot takarja.',
          '- **05.3, WC:** a PAX 200 az ajtó negyedkörébe és az étkező-aknába lóg; az előtéri cipős szekrény a WC-ajtó nyitásába.',
          '- **06.2:** a mosdószekrény és a zuhany a javított keleti fal (x 16,40) miatt 2–10 cm-rel ütközik – a valós szaniterek helye hétfőn mérendő.',
          '- A bútorréteget a stílusválasztás után, a v2b geometriára és a kiállásokra kell újraépíteni (Astra B fázis előtt).', '']
    open(os.path.join(B, 'validator_report_2026-10-24_v2b.md'), 'w', encoding='utf-8').write('\n'.join(R) + '\n')
print('riportok kész')

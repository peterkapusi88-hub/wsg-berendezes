# Geometry Validator v2 – WSG A-902 (2026-10-24)
# Futtatás Blenderben vagy bpy-modullal (csak olvas, semmit nem ment):
#   WSG_LOCK=<repo>/03_blender/geometry_lock_A902_v2b.json \
#   WSG_VILLAMOS=<repo>/01_alaprajzok/villamos_kiallasok/A902_villamos.json \
#   python3 -c "import bpy,runpy; bpy.ops.wm.open_mainfile(filepath='<fájl.blend>'); runpy.run_path('<repo>/03_blender/geometry_validator_v2.py')"
# Eredmény: a `result` dict; WSG_REPORT_JSON megadásakor JSON-fájlba is.
#
# Ellenőrzések (PASS csak 0 hibánál):
#  1. LOCK      – falak, nyílászárók, látható padlók a v2b lock szerint (tűrés 1 cm); új vagy hiányzó elem
#  2. TERASZ    – a v2 tetőkert (A902_Terasz_v2_ELOZETES) minden eleme változatlan (Péter: „óvatosan, a kert kész”)
#  3. KAMERA    – teljes paraméterlap: típus, fókusz, szenzor és illesztés, shift, clip, hely, forgatás; aktív kamera
#  4. BURKOLÓ   – látható bútor a helyiségekben vagy a bútorozható teraszzónán, z a padló és a belmagasság között
#  5. ÜTKÖZÉS   – bútor ↔ fal / nyílászáró (1 cm felett); bútor ↔ bútor (más tárgycsoport, 2 cm felett)
#  6. AJTÓ      – a valódi nyitási negyedkör szabad (hiba); 90 cm-es megközelítési sáv mindkét oldalon (figyelmeztetés)
#  7. KONYHA    – a két pultsor közti tiszta köz (cél ≥ 90 cm, 80 alatt hiba)
#  8. 05.2      – ágy, ajtóforgások, éjjeliszekrények: működik-e, és milyen alternatíva fér el
#  9. VILLAMOS  – bútor nem takarhat kapcsolót, termosztátot, elosztót, kaputelefont, kezelőt; dugalj elé állás figyelmeztetés;
#                 mennyezeti kiállás alatti bútor (információ)
# A bbox-ok a mesh csúcsaiból (matrix_world) számolódnak; a stílusrétegek közül csak a renderben látható számít.
import bpy, json, os, math

LOCK_PATH = os.environ.get('WSG_LOCK') or os.path.join(os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else '.', 'geometry_lock_A902_v2b.json')
VILL_PATH = os.environ.get('WSG_VILLAMOS', '')
TOL = 0.01
APPROACH = 0.90
SOFT = ('szonyeg', 'fuggony', 'parna', 'takaro', 'pled', 'kezmoso', 'wc_', 'kad', 'zuhany', 'mosdo', 'lampa_feny', 'led')

def wb(o):
    M = o.matrix_world
    pts = [M @ v.co for v in o.data.vertices] if o.type == 'MESH' else []
    if not pts:
        return None
    return [min(p[i] for p in pts) for i in range(3)] + [max(p[i] for p in pts) for i in range(3)]

def ov(a, b):
    return [min(a[i + 3], b[i + 3]) - max(a[i], b[i]) for i in range(3)]

def in_rects(x, y, rects, tol=0.03):
    return any(r[0] - tol <= x <= r[2] + tol and r[1] - tol <= y <= r[3] + tol for r in rects)

def group_key(name):
    t = name.split('_')
    return '_'.join(t[:3]) if len(t) >= 3 else name

def visible_furniture():
    out = {}
    for c in bpy.data.collections:
        if (c.name == 'A902_Butor' or c.name.startswith('Stil_')) and not c.hide_render:
            for o in c.objects:
                if o.type == 'MESH' and not o.hide_render:
                    b = wb(o)
                    if b: out[o.name] = b
    return out

def cam_params(o):
    c = o.data
    return dict(type=c.type, lens=round(c.lens, 3), sensor_width=round(c.sensor_width, 3), sensor_height=round(c.sensor_height, 3),
                sensor_fit=c.sensor_fit, shift_x=round(c.shift_x, 4), shift_y=round(c.shift_y, 4), clip_start=round(c.clip_start, 4),
                clip_end=round(c.clip_end, 2), loc=[round(v, 4) for v in o.matrix_world.translation], rot=[round(v, 5) for v in o.rotation_euler])

def run():
    bpy.context.view_layer.update()
    lock = json.load(open(LOCK_PATH, encoding='utf-8'))
    H = lock.get('H', 2.90)
    rep = dict(fajl=bpy.data.filepath, lock=os.path.basename(LOCK_PATH), stilus=[c.name for c in bpy.data.collections if c.name.startswith('Stil_') and not c.hide_render],
               errors=[], warnings=[], ok=[], info=[], measurements={})
    E, W_, OK, INFO = rep['errors'], rep['warnings'], rep['ok'], rep['info']
    # 1. LOCK
    def live(cname, only_visible=False):
        c = bpy.data.collections.get(cname)
        if not c: return {}
        return {o.name: wb(o) for o in c.objects if o.type == 'MESH' and (not only_visible or not o.hide_render)}
    for group, cname, vis in (('walls', 'A902_Falak', False), ('openings', 'A902_Nyilaszarok', False), ('floors', 'A902_Padlo', True)):
        L = live(cname, vis)
        n_bad = 0
        for name, bb in lock.get(group, {}).items():
            if name not in L or L[name] is None:
                E.append(f'LOCK: hiányzik {group}/{name}'); n_bad += 1; continue
            d = max(abs(a - b) for a, b in zip(L[name], bb))
            if d > lock.get('tolerance_m', TOL):
                E.append(f'LOCK: eltér {group}/{name} ({d * 100:.1f} cm)'); n_bad += 1
        extra = sorted(set(L) - set(lock.get(group, {})))
        if extra: W_.append(f'LOCK: nem rögzített {group}: {extra[:10]}' + (' …' if len(extra) > 10 else ''))
        OK.append(f'LOCK {group}: {len(lock.get(group, {}))} elem, {n_bad} eltérés')
    # 2. TERASZ
    T = live('A902_Terasz_v2_ELOZETES')
    tl = lock.get('terrace_v2', {})
    nbad = 0
    for name, bb in tl.items():
        if name not in T: E.append(f'TERASZ: hiányzik {name}'); nbad += 1; continue
        d = max(abs(a - b) for a, b in zip(T[name], bb))
        if d > TOL: E.append(f'TERASZ: megváltozott {name} ({d * 100:.1f} cm)'); nbad += 1
    OK.append(f'TERASZ v2 (tetőkert): {len(tl)} elem, {nbad} változás')
    # 3. KAMERA
    sc = bpy.context.scene
    rep['measurements']['aktiv_kamera'] = sc.camera.name if sc.camera else None
    for name, cam in lock.get('cameras', {}).items():
        o = bpy.data.objects.get(name)
        if not o: E.append(f'KAMERA: hiányzik {name}'); continue
        p = cam_params(o)
        p['tipus'] = p.pop('type'); p['lens_mm'] = p.pop('lens'); p['ortho_scale'] = round(o.data.ortho_scale, 3)
        for k in ('tipus', 'sensor_fit'):
            if k in cam and cam[k] != p[k]: E.append(f'KAMERA {name}: {k} {p[k]} ≠ {cam[k]}')
        for k in ('lens_mm', 'sensor_width', 'sensor_height', 'shift_x', 'shift_y', 'clip_start', 'clip_end', 'ortho_scale'):
            if k in cam and cam[k] is not None and abs(cam[k] - p[k]) > 1e-3: E.append(f'KAMERA {name}: {k} {p[k]} ≠ {cam[k]}')
        if 'loc' in cam and max(abs(a - b) for a, b in zip(p['loc'], cam['loc'])) > TOL: E.append(f'KAMERA {name}: elmozdult')
        if 'rot' in cam and max(abs(a - b) for a, b in zip(p['rot'], cam['rot'])) > 0.002: E.append(f'KAMERA {name}: elfordult')
        if cam.get('statusz'): INFO.append(f'KAMERA {name}: {cam["statusz"]}')
    OK.append(f'KAMERA: {len(lock.get("cameras", {}))} kamera teljes paraméterrel; aktív: {rep["measurements"]["aktiv_kamera"]}')
    # helyiségek, zónák
    rooms = {k: v for k, v in lock.get('rooms', {}).items()}
    room_rects = [r for rr in rooms.values() for r in (rr if isinstance(rr[0], list) else [rr])]
    tz = lock.get('terrace_zones', {})
    furn_rects = room_rects + [z['r'] for z in tz.values() if z.get('butorozhato')]
    green = [z['r'] for z in tz.values() if not z.get('butorozhato')]
    # 4. BURKOLÓ
    fb = visible_furniture()
    walls = {n: b for n, b in live('A902_Falak').items() if b and not n.startswith('Plafon')}
    opens = {n: b for n, b in live('A902_Nyilaszarok').items() if b}
    for n, b in fb.items():
        corners = [(b[0], b[1]), (b[3], b[1]), (b[0], b[4]), (b[3], b[4])]
        if not all(in_rects(x, y, furn_rects) for x, y in corners):
            W_.append(f'BURKOLÓ: {n} kilóg a helyiségből vagy bútorozható zónából ({[round(v, 2) for v in (b[0], b[1], b[3], b[4])]})')
        if any(in_rects(x, y, green, -0.02) for x, y in corners):
            E.append(f'BURKOLÓ: {n} a zöldtetőn (terhelhetőség nem igazolt)')
        if b[2] < -0.20 or b[5] > H + 0.005:
            E.append(f'BURKOLÓ: {n} magasság {b[2]:.2f}–{b[5]:.2f} m')
    OK.append(f'BURKOLÓ: {len(fb)} látható bútorelem')
    # 5. ÜTKÖZÉS
    nfw = 0
    for n, b in fb.items():
        for wn, w in walls.items():
            o_ = ov(b, w)
            if min(o_) > TOL:
                E.append(f'ÜTKÖZÉS: {n} ↔ fal {wn} ({min(o_) * 100:.1f} cm)'); nfw += 1
        if any(k in n.lower() for k in ('fuggony',)): continue
        for on_, w in opens.items():
            o_ = ov(b, w)
            if min(o_) > TOL:
                E.append(f'ÜTKÖZÉS: {n} ↔ nyílászáró {on_} ({min(o_) * 100:.1f} cm)'); nfw += 1
    names = sorted(fb)
    ff = []
    for i, a in enumerate(names):
        if any(k in a.lower() for k in SOFT): continue
        for b_ in names[i + 1:]:
            if group_key(a) == group_key(b_) or any(k in b_.lower() for k in SOFT): continue
            o_ = ov(fb[a], fb[b_])
            if min(o_) > 0.02:
                ff.append((round(min(o_) * 100, 1), a, b_))
    for d, a, b_ in sorted(ff, reverse=True)[:40]:
        W_.append(f'ÁTFEDÉS: {a} ↔ {b_} ({d} cm)')
    rep['measurements']['butor_butor_atfedes_db'] = len(ff)
    OK.append(f'ÜTKÖZÉS: bútor–fal/nyílászáró {nfw}, bútor–bútor átfedés {len(ff)}')
    # 6. AJTÓ – negyedkör + megközelítés
    def swing_hits(meta):
        h = meta.get('zsaner'); r = meta.get('r'); ir = meta.get('irany')
        if not (h and r and ir): return []
        ax = meta.get('fal')
        lo, hi = meta['nyilas']
        d1 = None
        if ax == 'x':   # fal az x tengely mentén, a nyílás x-ben
            d1 = (1 if abs(h[0] - lo) < 1e-3 else -1, 0)
        else:
            d1 = (0, 1 if abs(h[1] - lo) < 1e-3 else -1)
        d2 = {'+x': (1, 0), '-x': (-1, 0), '+y': (0, 1), '-y': (0, -1)}[ir]
        hits = []
        step = 0.04
        for n, b in fb.items():
            if b[5] < 0.05 or b[2] > 2.0 or any(k in n.lower() for k in ('szonyeg', 'fuggony')): continue
            hit = False
            u = 0.0
            while u <= r and not hit:
                v = 0.0
                while v <= r and not hit:
                    if u * u + v * v <= r * r:
                        x = h[0] + d1[0] * u + d2[0] * v; y = h[1] + d1[1] * u + d2[1] * v
                        if b[0] + 0.005 < x < b[3] - 0.005 and b[1] + 0.005 < y < b[4] - 0.005: hit = True
                    v += step
                u += step
            if hit: hits.append(n)
        return hits
    for name, meta in lock.get('openings_meta', {}).items():
        if meta.get('tipus') == 'tolo': continue
        hits = swing_hits(meta)
        for n in hits: E.append(f'AJTÓ-FORGÁS: {n} a(z) {name} nyitási negyedkörében (r {meta.get("r")} m)')
        # megközelítési sáv mindkét oldalon
        lo, hi = meta['nyilas']; f0, f1 = meta['fal_sik']
        for sgn in (-1, 1):
            if meta.get('fal') == 'x':
                zone = [lo, f0 - APPROACH, 0, hi, f0, 1.0] if sgn < 0 else [lo, f1, 0, hi, f1 + APPROACH, 1.0]
            else:
                zone = [f0 - APPROACH, lo, 0, f0, hi, 1.0] if sgn < 0 else [f1, lo, 0, f1 + APPROACH, hi, 1.0]
            for n, b in fb.items():
                if any(k in n.lower() for k in SOFT) or n in hits: continue
                o_ = ov(b, zone)
                if min(o_) > 0.02: W_.append(f'AJTÓ-ELŐTÉR: {n} a(z) {name} 90 cm-es megközelítési sávjában ({min(o_) * 100:.0f} cm)')
    OK.append(f'AJTÓ: {len(lock.get("openings_meta", {}))} nyílás negyedkörrel/sávval vizsgálva')
    # 7. KONYHA – pultsorok közti tiszta köz
    kitchen = [r for r in rooms.get('konyha', [])]
    tops = {n: b for n, b in fb.items() if 'munkalap' in n.lower() and kitchen and any(in_rects((b[0] + b[3]) / 2, (b[1] + b[4]) / 2, [k], 0.05) for k in kitchen)}
    if len(tops) >= 2:
        xs = sorted(tops.items(), key=lambda kv: kv[1][0])
        west = max(b[3] for n, b in xs if b[3] < 9.8); east = min(b[0] for n, b in xs if b[0] > 9.2)
        g = east - west
        rep['measurements']['konyha_pultkoz_cm'] = round(g * 100, 1)
        (E if g < 0.80 else W_ if g < 0.90 else OK).append(f'KONYHA: pultsorok közti tiszta köz {g * 100:.0f} cm (cél ≥ 90; a nyers szerkezeti szélesség 2,10 m → két 62 cm-es pulttal 86 cm)')
    else:
        INFO.append('KONYHA: nincs két munkalap-sor a látható rétegben – a pultköz nem mérhető')
    # 8. 05.2 funkcionális vizsgálat
    r52 = rooms.get('05_2', [[0, 0, 3.65, 2.65]])[0]
    beds = {n: b for n, b in fb.items() if n.lower().startswith(('agy_05_2', 'l_agy_05_2', 'z_agy_05_2')) or ('agy' in n.lower() and '05_2' in n and 'keret' in n.lower())}
    sw = {k: v for k, v in lock.get('openings_meta', {}).items() if k in ('Ajto_05_2', 'Erkelyajto_05_2')}
    alt = []
    for w in (1.40, 1.60, 1.80):
        for x0 in [round(0.05 * i, 2) for i in range(0, 60)]:
            bb = [x0, 0.0, 0, x0 + w, 2.05, 0.5]  # fejjel a déli falnak, 200 cm + 5 cm fejtámla
            if bb[3] > r52[2]: break
            free = True
            for name, meta in sw.items():
                h = meta['zsaner']; r = meta['r']
                # egyszerű: a negyedkör befoglaló négyzete az ágy-téglalappal
                d1x = 1 if meta.get('fal') == 'y' else (1 if abs(h[0] - meta['nyilas'][0]) < 1e-3 else -1)
                if meta.get('fal') == 'x':
                    sq = [min(h[0], h[0] + d1x * r), min(h[1], h[1] - r), max(h[0], h[0] + d1x * r), max(h[1], h[1] - r)]
                else:
                    sq = [h[0], min(h[1], h[1] + r), h[0] + r, max(h[1], h[1] + r)]
                if bb[0] < sq[2] and bb[3] > sq[0] and bb[1] < sq[3] and bb[4] > sq[1]: free = False
            if free:
                side_l = x0 - r52[0]; side_r = r52[2] - (x0 + w)
                alt.append(dict(agy_szelesseg=w, x0=x0, x1=round(x0 + w, 2), bal_oldal_cm=round(side_l * 100), jobb_oldal_cm=round(side_r * 100), labnal_cm=round((r52[3] - 2.05) * 100)))
    best = {}
    for a in alt:
        k = a['agy_szelesseg']
        if k not in best or min(a['bal_oldal_cm'], a['jobb_oldal_cm']) > min(best[k]['bal_oldal_cm'], best[k]['jobb_oldal_cm']): best[k] = a
    rep['measurements']['05_2_agy_alternativak'] = list(best.values())
    INFO.append('05.2: fejjel a déli falnak, az ajtóforgásokon kívül elférő ágyak (legjobb oldaltávolság): ' +
                '; '.join(f"{int(a['agy_szelesseg'] * 100)} cm x {a['x0']:.2f}–{a['x1']:.2f}, oldalt {a['bal_oldal_cm']}/{a['jobb_oldal_cm']} cm, lábnál {a['labnal_cm']} cm" for a in best.values()) if best else '05.2: nincs a forgásokon kívüli ágyhely – FAIL')
    # 9. VILLAMOS
    if VILL_PATH and os.path.exists(VILL_PATH):
        V = json.load(open(VILL_PATH, encoding='utf-8'))['kiallasok']
        hard = ('kapcsolo', 'termosztat', 'lakaselosztó', 'kaputelefon_belteri', 'kezelo_billentyuzet', 'BK_doboz')
        soft = ('dugalj', 'gyengearamu_aljzat', 'antenna_tv_aljzat')
        nh = ns = 0
        for v in V:
            if v['tipus'] not in hard + soft: continue
            x = v['doboz_x_m'] if v['doboz_x_m'] != '' else v['x_m']; y = v['doboz_y_m'] if v['doboz_y_m'] != '' else v['y_m']
            z = v['magassag_m'] if isinstance(v['magassag_m'], (int, float)) else (1.10 if v['tipus'] in hard else 0.30)
            for n, b in fb.items():
                if any(k in n.lower() for k in ('szonyeg', 'fuggony')): continue
                if b[0] - 0.12 <= x <= b[3] + 0.12 and b[1] - 0.12 <= y <= b[4] + 0.12 and b[2] - 0.05 <= z <= b[5] + 0.05:
                    if v['tipus'] in hard:
                        E.append(f"VILLAMOS: {n} takarja: {v['azonosito']} {v['tipus']} {v['aramkor'] or v['kod']} (x {x}, y {y}, ~{z} m)"); nh += 1
                    else:
                        W_.append(f"VILLAMOS: {n} a(z) {v['azonosito']} {v['tipus']} {v['kod']} előtt (x {x}, y {y}, ~{z} m) – hozzáférés ellenőrizendő"); ns += 1
        for v in V:
            if v['tipus'] != 'mennyezeti_lampakiallas': continue
            under = [n for n, b in fb.items() if b[0] <= v['x_m'] <= b[3] and b[1] <= v['y_m'] <= b[4] and b[5] > 0.3]
            if under: INFO.append(f"VILLAMOS: a(z) {v['azonosito']} „{v['aramkor']}” mennyezeti kiállás alatt: {sorted(set(group_key(u) for u in under))}")
        OK.append(f'VILLAMOS: {len(V)} terv szerinti kiállás vizsgálva; takarás {nh}, dugalj elé állás {ns}')
    else:
        INFO.append('VILLAMOS: a kiállás-adat (WSG_VILLAMOS) nincs megadva – a vizsgálat kimaradt')
    rep['summary'] = f"{'PASS' if not E else 'FAIL'} – {len(E)} hiba, {len(W_)} figyelmeztetés; réteg: {rep['stilus']}"
    return rep

result = run()
if os.environ.get('WSG_REPORT_JSON'):
    json.dump(result, open(os.environ['WSG_REPORT_JSON'], 'w'), ensure_ascii=False, indent=1)
print(result['summary'])

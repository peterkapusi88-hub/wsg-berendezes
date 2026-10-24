# Geometry Validator – WSG A-902
# Blenderben fut (Claude MCP-n át vagy a Text Editorból). Nem vélemény: a jelenet tényleges geometriáját méri
# és a geometry_lock_A902.json-hoz hasonlítja. Eredmény: `result` dict (REVIEW.md-be másolható).
#
# Ellenőrzések
#  1. LOCK      – falak, nyílászárók, padlók, kamerák ott vannak-e, ahol a jóváhagyott modellben (tűrés 1 cm)
#  2. BURKOLÓ   – minden látható bútor (A902_Butor + aktív Stil_* réteg) a helyiségek/teraszok területén belül van-e, z 0–2,90
#  3. ÜTKÖZÉS   – bútor nem metsz falat / nyílászárót 1 cm-nél mélyebben
#  4. AJTÓ      – minden ajtó előtt 90 cm-es megközelítési sáv szabad (mindkét oldalon)
#  5. TÁVOLSÁG  – kanapé–dohányzóasztal 45–50 cm, kanapé–TV-fal közlekedő ≥ 90, ágy mellett ≥ 60, étkezőszék hátratolás ≥ 60 (cél 90)
#
# Megjegyzés: a bbox-okat a mesh csúcsaiból számoljuk (matrix_world-del), mert a réteg-váltás után az object.bound_box
# gyorsítótára elavult lehet. Modifier (bevel) nem számít – az 1 cm-es tűrésen belül.
import bpy, json, os
from mathutils import Vector

LOCK_PATH = os.environ.get('WSG_LOCK', os.path.expanduser('~/Downloads/wsg_lock/geometry_lock_A902.json'))
TOL = 0.01
DOOR_CLEAR = 0.90

def wb(o):
    """világ-bbox a mesh csúcsaiból: [x0,y0,z0,x1,y1,z1]"""
    M = o.matrix_world
    pts = [M @ v.co for v in o.data.vertices]
    if not pts: return [0,0,0,0,0,0]
    return [min(p[i] for p in pts) for i in range(3)] + [max(p[i] for p in pts) for i in range(3)]

def overlap(a, b):
    return [min(a[i+3], b[i+3]) - max(a[i], b[i]) for i in range(3)]

def gap(a, b, axis):
    return max(b[axis] - a[axis+3], a[axis] - b[axis+3])

def inside_rooms(bb, rooms, tol=0.03):
    corners = [(bb[0],bb[1]),(bb[3],bb[1]),(bb[0],bb[4]),(bb[3],bb[4])]
    return all(any(r[0]-tol <= cx <= r[2]+tol and r[1]-tol <= cy <= r[3]+tol for r in rooms.values()) for cx, cy in corners)

def visible_furniture():
    objs = []
    for c in bpy.data.collections:
        if (c.name == 'A902_Butor' or c.name.startswith('Stil_')) and not c.hide_render:
            objs += [o for o in c.objects if o.type == 'MESH' and not o.hide_render]
    return objs

def run():
    bpy.context.view_layer.update()
    with open(LOCK_PATH, encoding='utf-8') as f: lock = json.load(f)
    rooms = dict(lock["rooms"])
    for fname, fbb in lock.get("floors", {}).items():
        if fname.startswith('T_') or fname.startswith('Erkely'): rooms[fname] = [fbb[0], fbb[1], fbb[3], fbb[4]]
    rep = {"style": [c.name for c in bpy.data.collections if c.name.startswith('Stil_') and not c.hide_render],
           "errors": [], "warnings": [], "ok": [], "measurements": {}}
    # 1. LOCK
    for group, cname in (("walls", "A902_Falak"), ("openings", "A902_Nyilaszarok"), ("floors", "A902_Padlo")):
        live = {o.name: wb(o) for o in bpy.data.collections[cname].objects if o.type == 'MESH'}
        for name, bb in lock[group].items():
            if name not in live: rep["errors"].append(f"LOCK: hiányzik {group}/{name}"); continue
            d = max(abs(a-b) for a, b in zip(live[name], bb))
            if d > lock.get("tolerance_m", TOL): rep["errors"].append(f"LOCK: elmozdult {group}/{name} ({d*100:.1f} cm)")
        extra = sorted(set(live) - set(lock[group]))
        if extra: rep["warnings"].append(f"LOCK: új, nem rögzített {group}: {extra[:8]}")
        rep["ok"].append(f"LOCK {group}: {len(lock[group])} elem")
    for name, cam in lock["cameras"].items():
        o = bpy.data.objects.get(name)
        if not o: rep["errors"].append(f"LOCK: hiányzik kamera {name}"); continue
        dl = max(abs(a-b) for a, b in zip(o.location, cam["loc"])); dr = max(abs(a-b) for a, b in zip(o.rotation_euler, cam["rot"]))
        if dl > TOL or dr > 0.002: rep["errors"].append(f"LOCK: kamera elmozdult {name} (pos {dl*100:.1f} cm, rot {dr:.4f} rad)")
    rep["ok"].append(f"LOCK kamerák: {len(lock['cameras'])}")
    # 2–3. BURKOLÓ + ÜTKÖZÉS
    walls = {o.name: wb(o) for o in bpy.data.collections['A902_Falak'].objects if o.type == 'MESH' and not o.name.startswith('Plafon')}
    opens = {o.name: wb(o) for o in bpy.data.collections['A902_Nyilaszarok'].objects if o.type == 'MESH'}
    fb = {o.name: wb(o) for o in visible_furniture()}
    H = lock.get("H", 2.9)
    for name, bb in fb.items():
        if bb[2] < -0.03 or bb[5] > H + 0.005: rep["errors"].append(f"BURKOLÓ: {name} z {bb[2]:.2f}–{bb[5]:.2f} m")
        if not inside_rooms(bb, rooms): rep["warnings"].append(f"BURKOLÓ: {name} kilóg ({[round(v,2) for v in bb[:2]+bb[3:5]]})")
        for wn, wbb in walls.items():
            ov = overlap(bb, wbb)
            if min(ov) > TOL: rep["errors"].append(f"ÜTKÖZÉS: {name} ↔ fal {wn} ({min(ov)*100:.1f} cm)")
        if 'fuggony' in name.lower(): continue
        for on_, obb in opens.items():
            ov = overlap(bb, obb)
            if min(ov) > TOL: rep["errors"].append(f"ÜTKÖZÉS: {name} ↔ nyílászáró {on_} ({min(ov)*100:.1f} cm)")
    rep["ok"].append(f"BURKOLÓ/ÜTKÖZÉS: {len(fb)} látható bútor")
    # 4. AJTÓ-ELŐTÉR: az ajtólap bbox-át a vékony tengelye mentén DOOR_CLEAR-rel kitoljuk mindkét irányba
    for on_, obb in opens.items():
        if not on_.startswith('Ajto_') or not on_.endswith('_lap'): continue
        thin = 0 if (obb[3]-obb[0]) < (obb[4]-obb[1]) else 1
        for sgn in (-1, 1):
            zone = list(obb); zone[2] = 0.0; zone[5] = 1.0
            if sgn < 0: zone[thin] = obb[thin] - DOOR_CLEAR; zone[thin+3] = obb[thin]
            else: zone[thin] = obb[thin+3]; zone[thin+3] = obb[thin+3] + DOOR_CLEAR
            for name, bb in fb.items():
                ov = overlap(bb, zone)
                if min(ov) > 0.02 and not any(k in name.lower() for k in ('szonyeg', 'fuggony', 'kezmoso', 'wc_', 'kad', 'zuhany', 'mosdo')):
                    rep["errors"].append(f"AJTÓ: {name} az {on_} előterében ({min(ov)*100:.0f} cm)")
    rep["ok"].append("AJTÓ-ELŐTÉR: minden ajtólap 2 oldalon")
    # 5. TÁVOLSÁGOK (névminták; csak az aktív stílusréteg bútorai, a terasz és a rejtett alap nem zavar be)
    stil = {o.name for c in bpy.data.collections if c.name.startswith('Stil_') and not c.hide_render for o in c.objects}
    sf = {n: bb for n, bb in fb.items() if n in stil} or fb
    def find(*keys): return [n for n in sf if all(k.lower() in n.lower() for k in keys)]
    rep["measurements"]["_butorok"] = {"kanape_ules": find('kanape', 'ules'), "dohanyzo": find('dohanyzo', 'lap') or find('dohanyzo'), "szek_ules": find('szek', 'ules')}
    def union(names):
        bbs = [fb[n] for n in names]
        return [min(b[i] for b in bbs) for i in range(3)] + [max(b[i] for b in bbs) for i in range(3)] if bbs else None
    seats = find('kanape', 'ules'); table = union(find('dohanyzo', 'lap')) or union(find('dohanyzo'))
    if seats and table:
        g = min(max(gap(fb[s], table, 0), gap(fb[s], table, 1)) for s in seats)
        rep["measurements"]["kanape_dohanyzo_cm"] = round(g*100, 1)
        if g < 0.40: rep["warnings"].append(f"TÁVOLSÁG: kanapé–dohányzóasztal {g*100:.0f} cm (cél 45–50)")
        elif g > 0.60: rep["warnings"].append(f"TÁVOLSÁG: kanapé–dohányzóasztal {g*100:.0f} cm – túl messze (cél 45–50)")
    tvwall = union([n for n in fb if 'tvfal' in n.lower() and any(k in n.lower() for k in ('pad', 'travertin', 'beton', 'hatlap'))])
    if seats and tvwall:
        g = gap(union(seats), tvwall, 1); rep["measurements"]["kanape_tvfal_kozlekedo_cm"] = round(g*100, 1)
        if g < 0.90: rep["warnings"].append(f"TÁVOLSÁG: kanapé–TV-fal közlekedő {g*100:.0f} cm (fő útvonal min. 90)")
    # közlekedő az átjáró (x 7,40–8,45) és a nappali között: ami az átjáró sávjában y 4,04–8 között áll
    blockers = [(n, bb) for n, bb in fb.items() if bb[3] > 7.40 and bb[0] < 8.45 and bb[4] > 4.04 and bb[5] > 0.3 and 'szonyeg' not in n.lower()]
    if blockers:
        w = max(bb[0] for _, bb in blockers if bb[0] > 7.40) if any(bb[0] > 7.40 for _, bb in blockers) else 7.40
        e = min(bb[3] for _, bb in blockers if bb[3] < 8.45) if any(bb[3] < 8.45 for _, bb in blockers) else 8.45
        rep["warnings"].append(f"KÖZLEKEDŐ: az átjáró vonalában (x 7,40–8,45) tárgy áll: {[n for n,_ in blockers][:6]}")
    bed = union(find('agy_keret')) or union(find('agy_', 'keret'))
    if bed:
        obst = {**walls, **{n: fb[n] for n in find('gardrob')}}
        side = [(bed[0] - wbb[3], wn) for wn, wbb in obst.items() if not (wbb[4] < bed[1] or wbb[1] > bed[4]) and wbb[3] <= bed[0] + 0.01]
        if side:
            g, wn = min(side); rep["measurements"]["agy_nyugati_oldal_cm"] = round(g*100, 1)
            if g < 0.60: rep["warnings"].append(f"TÁVOLSÁG: ágy mellett nyugaton {g*100:.0f} cm ({wn}; min. 60)")
    chairs = find('szek', 'ules')
    if chairs:
        worst = None
        others = {**walls, **{m: fb[m] for m in fb if 'szek' not in m.lower() and 'etkezo_lap' not in m.lower() and 'szonyeg' not in m.lower()}}
        for n in chairs:
            bb = fb[n]; hat = fb.get(n.replace('ules', 'hat'))
            if not hat: continue
            cx, cy = (bb[0]+bb[3])/2, (bb[1]+bb[4])/2; hx, hy = (hat[0]+hat[3])/2, (hat[1]+hat[4])/2
            axis, sgn = (0, 1 if hx > cx else -1) if abs(hx-cx) > abs(hy-cy) else (1, 1 if hy > cy else -1)
            perp = 1 - axis
            for wn, wbb in others.items():
                if wbb[5] < 0.3 or wbb[perp+3] < bb[perp] or wbb[perp] > bb[perp+3]: continue
                g = (wbb[axis] - bb[axis+3]) if sgn > 0 else (bb[axis] - wbb[axis+3])
                if 0 <= g < 0.90 and (worst is None or g < worst[0]): worst = (g, n, wn)
        if worst:
            rep["measurements"]["szek_hatratolas_min_cm"] = round(worst[0]*100, 1)
            if worst[0] < 0.60: rep["warnings"].append(f"TÁVOLSÁG: étkezőszék {worst[1]} mögött {worst[0]*100:.0f} cm ({worst[2]}; cél 90, min. 60)")
        else:
            rep["measurements"]["szek_hatratolas_min_cm"] = ">90"
    rep["summary"] = f"{len(rep['errors'])} hiba, {len(rep['warnings'])} figyelmeztetés, réteg: {rep['style']}"
    return rep

result = run()

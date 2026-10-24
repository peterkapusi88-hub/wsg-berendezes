# A-902 05.1 master – az ágy tengelye y 6,00 → 6,40 a bútorrétegben (Péter, 2026-10-25 00:05; terv és dugaljak szerint).
# r2 (2026-10-25): az eltolás a MESH-ADATBA kerül, a location 0 marad – ugyanúgy, ahogy a fájl többi bútora készült.
#   Az r1 a matrix_world-öt/location-t írta. Blender 5.x-ben a matrix_world futásidejű adat: betöltés után a nem kiértékelt
#   (rejtett) objektumoknál egységmátrix, ezért a validátor és a mérés a régi helyet látta (04_vizsgal_uj.json).
# Bemenet: a PR #15 v2b-1-k11 fájlja (sha256 33bf0af9…7661). Kimenet: ÚJ fájl (copy=True) – a forrást nem írja felül.
# Csak bútor- és stílusréteg-objektumok mozognak; fal, nyílás, padló, kamera, lock-elem nem.
# Futtatás: Blender -b <k11.blend> --python 01_agy640_athelyezes.py -- <kimenet.blend> <naplo.json>
import bpy, sys, json, hashlib, mathutils
a = sys.argv[sys.argv.index('--') + 1:]; OUT, LOG = a[0], a[1]
DY = 0.40
MOZGAT = {
 'A902_Butor': ['Agy_05_1_TALLASEN_180x200_fejtamla', 'Agy_05_1_TALLASEN_180x200_keret', 'Agy_05_1_TALLASEN_180x200_matrac',
                'Agy_05_1_TALLASEN_180x200_parna_takaro', 'Ejjeli_05_1_a', 'Ejjeli_05_1_a_lampa', 'Ejjeli_05_1_b', 'Ejjeli_05_1_b_lampa',
                'Szonyeg_05_1_200x300'],
 'Stil_Zenit': ['Z_agy_keret', 'Z_agy_matrac', 'Z_agy_pled', 'Z_agy_takaro', 'Z_ejjeli_0', 'Z_ejjeli_1', 'Z_olvasolampa_0', 'Z_olvasolampa_1',
                'Z_olvasolampa_feny_0', 'Z_olvasolampa_feny_1', 'Z_master_szonyeg'],
 'Stil_LakeForest': ['L_agy_keret', 'L_agy_matrac', 'L_agy_takaro', 'L_agyfal_bronz', 'L_ejjeli_0', 'L_ejjeli_1', 'L_ejjeli_lap_0', 'L_ejjeli_lap_1',
                     'L_olvasolampa_0', 'L_olvasolampa_1', 'L_olvasolampa_feny_0', 'L_olvasolampa_feny_1', 'L_master_szonyeg']}
# a régi éjjeliszekrények 3 cm-rel a keleti falba lógtak (fal x 3,57) → falhoz igazítva; a lámpák a szekrény elejére,
# hogy a mögöttük lévő K13/K14 kapcsoló és a D20–D23 dugalj elérhető maradjon
DX = {'Ejjeli_05_1_a': -0.04, 'Ejjeli_05_1_b': -0.04, 'Ejjeli_05_1_a_lampa': -0.14, 'Ejjeli_05_1_b_lampa': -0.14}
def bb(o):
    # csúcsokból és matrix_basis-ből (szülő nincs) – nem függ a depsgraph kiértékelésétől
    M = o.matrix_basis
    pts = [M @ v.co for v in o.data.vertices] if o.type == 'MESH' and len(o.data.vertices) else [M.translation.copy()]
    return [round(min(p[i] for p in pts), 4) for i in range(3)] + [round(max(p[i] for p in pts), 4) for i in range(3)]
nevek = [n for l in MOZGAT.values() for n in l]
hiany = [n for n in nevek if n not in bpy.data.objects]; assert not hiany, hiany
for koll, l in MOZGAT.items():
    for n in l: assert koll in [c.name for c in bpy.data.objects[n].users_collection], (n, koll)
sha = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest()
assert sha.startswith('33bf0af9') and sha.endswith('7661'), sha
naplo = dict(forras=bpy.data.filepath, forras_sha256=sha, dy=DY, dx=DX, modszer='mesh-adat eltolása, location 0 marad (r2)', objektumok={})
elotte = {n: bb(bpy.data.objects[n]) for n in nevek}
for n in nevek:
    o = bpy.data.objects[n]
    assert o.parent is None and not o.constraints and not (o.animation_data and (o.animation_data.action or o.animation_data.drivers)), n
    d = mathutils.Vector((DX.get(n, 0.0), DY, 0.0))
    rec = dict(tipus=o.type, location=[round(v, 6) for v in o.location], rot=[round(v, 6) for v in o.rotation_euler], scale=[round(v, 6) for v in o.scale])
    if o.type == 'MESH':
        assert o.data.users == 1, (n, o.data.users)
        dl = o.matrix_basis.to_3x3().inverted_safe() @ d      # helyi eltolás, amely világban pontosan d
        o.data.transform(mathutils.Matrix.Translation(dl), shape_keys=True); o.data.update()
        rec.update(mod='mesh', helyi_eltolas=[round(v, 6) for v in dl], shape_keys=bool(o.data.shape_keys))
    else:
        o.location += d; rec.update(mod='location')
    naplo['objektumok'][n] = rec
for n in nevek:
    u = bb(bpy.data.objects[n]); e = elotte[n]; d = (DX.get(n, 0.0), DY, 0.0)
    assert all(abs((u[i] - e[i]) - d[i % 3]) < 1e-3 for i in range(6)), (n, e, u)
    naplo['objektumok'][n].update(elotte=e, utana=u)
k = naplo['objektumok']['Agy_05_1_TALLASEN_180x200_keret']['utana']
assert abs(k[1] - 5.50) < 0.005 and abs(k[4] - 7.30) < 0.005, k
naplo['agy_tengely_y'] = round((k[1] + k[4]) / 2, 4)
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=True)
naplo['kimenet'] = OUT; naplo['kimenet_sha256'] = hashlib.sha256(open(OUT, 'rb').read()).hexdigest()
json.dump(naplo, open(LOG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('MENTVE', OUT, naplo['agy_tengely_y'])

import bpy, sys, json
out = sys.argv[sys.argv.index('--') + 1]
res = {}
for n in ('Agy_05_1_TALLASEN_180x200_keret', 'Agy_05_1_TALLASEN_180x200_fejtamla', 'Ejjeli_05_1_a', 'Z_agy_keret', 'L_agy_keret'):
    o = bpy.data.objects[n]
    ad = o.animation_data
    res[n] = dict(loc=list(o.location), delta=list(o.delta_location), mw=[list(r) for r in o.matrix_world], parent=o.parent.name if o.parent else None,
                  parent_type=o.parent_type, anim=bool(ad and ad.action), drivers=len(ad.drivers) if ad else 0, constraints=[c.type for c in o.constraints],
                  data=o.data.name, data_users=o.data.users, mods=[m.type for m in o.modifiers])
json.dump(res, open(out, 'w'), indent=1, default=str)
print('OK')

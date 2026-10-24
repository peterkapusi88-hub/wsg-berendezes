# WSG Blender segédfüggvények – önálló, nem függ korábbi munkamenettől.
# Futtatás a Blender MCP-n át; a függvények bekerülnek bpy.app.driver_namespace['wsg']-be is.
import bpy, bmesh, math, mathutils

def _finish_mesh(me):
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free(); me.update()

def _new_obj(name, me, material, collection):
    o = bpy.data.objects.new(name, me)
    collection.objects.link(o)
    if material is not None:
        me.materials.append(material)
    return o

def coll(name):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(c)
    return c

def mat(name, rgb, rough=0.5, metal=0.0, emit=0.0, noise=None):
    """noise = (scale, masodik_szin_rgb, bump_erosseg)"""
    m = bpy.data.materials.get(name)
    if m is not None:
        return m
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; bsdf = nt.nodes['Principled BSDF']
    bsdf.inputs['Base Color'].default_value = (*rgb, 1.0)
    bsdf.inputs['Roughness'].default_value = rough
    bsdf.inputs['Metallic'].default_value = metal
    if emit:
        bsdf.inputs['Emission Color'].default_value = (*rgb, 1.0)
        bsdf.inputs['Emission Strength'].default_value = emit
    if noise:
        scale, col2, bump = noise
        nz = nt.nodes.new('ShaderNodeTexNoise'); nz.location = (-700, 200)
        nz.inputs['Scale'].default_value = scale; nz.inputs['Detail'].default_value = 8.0
        ramp = nt.nodes.new('ShaderNodeValToRGB'); ramp.location = (-450, 200)
        ramp.color_ramp.elements[0].color = (*rgb, 1.0)
        ramp.color_ramp.elements[1].color = (*col2, 1.0)
        nt.links.new(nz.outputs[0], ramp.inputs[0])
        nt.links.new(ramp.outputs[0], bsdf.inputs['Base Color'])
        if bump:
            b = nt.nodes.new('ShaderNodeBump'); b.location = (-450, -200)
            b.inputs['Strength'].default_value = bump
            nt.links.new(nz.outputs[0], b.inputs['Height'])
            nt.links.new(b.outputs['Normal'], bsdf.inputs['Normal'])
    m.diffuse_color = (*rgb, 1.0)
    return m

def box(name, x0, y0, z0, x1, y1, z1, material, collection, bevel=0.0):
    """Téglatest abszolút koordinátákkal (objektum-origó a világ origóban)."""
    verts = [(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0),(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)]
    faces = [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); _finish_mesh(me)
    o = _new_obj(name, me, material, collection)
    if bevel:
        bm = o.modifiers.new('Bevel', 'BEVEL'); bm.width = bevel; bm.segments = 4; bm.limit_method = 'ANGLE'
        bm.harden_normals = True
        for p in me.polygons: p.use_smooth = True
    return o

def cyl(name, cx, cy, z0, r, z1, material, collection, n=32):
    """Függőleges henger: alsó z0, felső z1, sugár r."""
    verts = []
    for z in (z0, z1):
        for i in range(n):
            a = 2*math.pi*i/n; verts.append((cx + r*math.cos(a), cy + r*math.sin(a), z))
    faces = [tuple(range(n)), tuple(range(n, 2*n))]
    for i in range(n):
        j = (i+1) % n; faces.append((i, j, n+j, n+i))
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); _finish_mesh(me)
    for p in me.polygons[2:]: p.use_smooth = True
    return _new_obj(name, me, material, collection)

def sphere(name, cx, cy, cz, r, material, collection, seg=16, rings=8):
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=rings, radius=r)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(cx, cy, cz))
    bm.to_mesh(me); bm.free(); me.update()
    for p in me.polygons: p.use_smooth = True
    return _new_obj(name, me, material, collection)

def tube(name, p0, p1, r, material, collection, n=12):
    """Henger két pont között (rúd, csillárszár)."""
    p0 = mathutils.Vector(p0); p1 = mathutils.Vector(p1); d = p1 - p0
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=n, radius1=r, radius2=r, depth=d.length)
    M = mathutils.Matrix.Translation((p0 + p1) / 2) @ d.to_track_quat('Z', 'Y').to_matrix().to_4x4()
    bmesh.ops.transform(bm, matrix=M, verts=bm.verts)
    bm.to_mesh(me); bm.free(); me.update()
    return _new_obj(name, me, material, collection)

def disc(name, cx, cy, cz, r, thickness, material, collection, axis='Y', n=64):
    """Vékony korong (tükör, lámpatest): axis = a korong normálisa ('X','Y','Z')."""
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=n, radius1=r, radius2=r, depth=thickness)
    rot = {'Z': mathutils.Matrix.Identity(4),
           'Y': mathutils.Matrix.Rotation(math.radians(90), 4, 'X'),
           'X': mathutils.Matrix.Rotation(math.radians(90), 4, 'Y')}[axis]
    M = mathutils.Matrix.Translation((cx, cy, cz)) @ rot
    bmesh.ops.transform(bm, matrix=M, verts=bm.verts)
    bm.to_mesh(me); bm.free(); me.update()
    return _new_obj(name, me, material, collection)

def _layer_coll(lc, name):
    if lc.name == name: return lc
    for ch in lc.children:
        r = _layer_coll(ch, name)
        if r: return r
    return None

def set_style(style):
    """'Zenit' vagy 'LakeForest': rétegek láthatósága + fényhangulat."""
    scn = bpy.context.scene
    for cname, on in (("Stil_Zenit", style == 'Zenit'), ("Stil_LakeForest", style == 'LakeForest')):
        c = bpy.data.collections.get(cname)
        if c is None: continue
        c.hide_render = not on; c.hide_viewport = not on
        lc = _layer_coll(bpy.context.view_layer.layer_collection, cname)
        if lc: lc.exclude = not on
    sun = bpy.data.objects.get("Nap"); world = scn.world
    bg = world.node_tree.nodes.get('Background') if world and world.node_tree else None
    areas = [o for o in scn.objects if o.type == 'LIGHT' and o.data.type == 'AREA']
    if style == 'LakeForest':   # nappali, világos, spa-hangulat
        if sun: sun.data.energy = 4.5; sun.data.color = (1.0, 0.98, 0.95)
        if bg: bg.inputs[0].default_value = (0.78, 0.85, 0.95, 1); bg.inputs[1].default_value = 0.9
        for o in areas: o.data.energy = 10; o.data.color = (1.0, 0.9, 0.78)
    else:                        # esti, meleg hotel-lounge
        if sun: sun.data.energy = 2.5; sun.data.color = (1.0, 0.96, 0.9)
        if bg: bg.inputs[0].default_value = (0.8, 0.8, 0.8, 1); bg.inputs[1].default_value = 0.35
        for o in areas: o.data.energy = 18; o.data.color = (1.0, 0.8, 0.6)
    return style

bpy.app.driver_namespace['wsg'] = {'box': box, 'cyl': cyl, 'sphere': sphere, 'tube': tube, 'disc': disc,
                                   'mat': mat, 'coll': coll, 'set_style': set_style}

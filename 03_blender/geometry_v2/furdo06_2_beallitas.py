# A-902 06.2 fürdő – a beépített állapot renderbeállítása a v2b-1(+k10) modellen. CSAK MEMÓRIÁBAN, nem ment. Claude, 2026-10-24.
# Források (bizonyíték-sorrend): (1) WGR1_meretezett_alaprajzok.pdf 18. o. – M1 KORR 2 alaprajz (06.2 kontúr, akna, Geberit-előtétfal
# pm. 1,20, süllyesztett csaptelep, 70 cm-es folyóka a csaptelep tengelyében, 5/5 padka, mosdó, törölközőszárító, lámpapontok);
# (2) 23. o. – 06.2 burkolatkiosztási terv (dosszié 230); (3) WGR1_modositasok_es_extrak.pdf 36–37. o. – A-902 2. kör költségvetés
# M1 KORR (2026.06.16.): Geostone Grigio matt 60×60 (62160A) padló+fal, Geostone Geo Esagonetta Grigio 3D dekor 30×60 (63610A)
# a zuhany hátfalán és a WC-előtétfal feletti falszakaszon, fuga Holdfény 103 (2 mm), falburkolat belmagasság − 5 cm, 4 egész sor
# felülről + alsó vágott sor; Geberit Smyle Square mosdó 60×48 (500.229.01.1) + Grohe Cubeo M mosdócsaptelep fekete (1017492430);
# Grohe Cubeo süllyesztett 2 funkciós csaptelep fekete (1017782430); Grohe Cube 250 fejzuhany karral fekete (26687 2430);
# Grohe Tempesta gégecső-csatlakozó tartóval fekete (28628431); Grohe Rainshower SmartActive 130 Cube kézizuhany-szett fekete;
# Geberit Smyle Square Rimfree fali WC 35×54 (500.208.01.1), ülőke (500.237.01.1), Delta 50 nyomólap matt fekete (115.119.14.1);
# fekete törölközőszárító (Merkury 8); ajtó 75×210 Flint Grey CPL, Thema Black kilincs. (4) Helyszíni fotók ME-BAL-064/066.
# Méretek a tervről, ±5 cm; a szerelvények magassága szabványos becslés (±10 cm) – helyszínen mérendő.
import bpy

def _mat_alap(nev):
    m = bpy.data.materials.get(nev) or bpy.data.materials.new(nev); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear(); return m, nt

def anyag_geostone(nev, dekor=False, c=0.0, padlo=None):
    """Geostone Grigio NAT 60×60 (vagy Esagonetta 3D 30×60) – rétegzett, üledékes kőhatás; fuga Holdfény 103, 2 mm;
    a burkolat felső széle 2,85 m (belmagasság − 5 cm), felette fehér festés; sorok felülről egész lappal."""
    m, nt = _mat_alap(nev); N = nt.nodes.new; L = nt.links.new
    out = N('ShaderNodeOutputMaterial'); bs = N('ShaderNodeBsdfPrincipled'); geo = N('ShaderNodeNewGeometry')
    sep = N('ShaderNodeSeparateXYZ'); L(geo.outputs['Position'], sep.inputs[0])
    # falon: u = x + y − c (az egyik vízszintes koordináta a falsíkon állandó) → fuga a terv tengelyén; v = z − (2,85 − 5×0,60):
    # felülről egész sor, alul vágott sor. Padlón (padlo=(x0, y0)): rács az ajtós fal belső síkjától és a Geberit-előtétfal elejétől.
    vizsz = N('ShaderNodeMath'); vizsz.operation = 'ADD'; L(sep.outputs['X'], vizsz.inputs[0]); L(sep.outputs['Y'], vizsz.inputs[1])
    uu = N('ShaderNodeMath'); uu.operation = 'SUBTRACT'; L(vizsz.outputs[0], uu.inputs[0]); uu.inputs[1].default_value = c
    zof = N('ShaderNodeMath'); zof.operation = 'SUBTRACT'; L(sep.outputs['Z'], zof.inputs[0]); zof.inputs[1].default_value = 2.85 - 0.60 * 5
    comb = N('ShaderNodeCombineXYZ')
    if padlo:
        px = N('ShaderNodeMath'); px.operation = 'SUBTRACT'; L(sep.outputs['X'], px.inputs[0]); px.inputs[1].default_value = padlo[0]
        py = N('ShaderNodeMath'); py.operation = 'SUBTRACT'; L(sep.outputs['Y'], py.inputs[0]); py.inputs[1].default_value = padlo[1]
        L(px.outputs[0], comb.inputs['X']); L(py.outputs[0], comb.inputs['Y'])
    else:
        L(uu.outputs[0], comb.inputs['X']); L(zof.outputs[0], comb.inputs['Y'])
    br = N('ShaderNodeTexBrick'); br.offset = 0.0; br.squash = 1.0; L(comb.outputs[0], br.inputs['Vector'])
    br.inputs['Scale'].default_value = 1.0; br.inputs['Brick Width'].default_value = 0.60
    br.inputs['Row Height'].default_value = 0.30 if dekor else 0.60
    br.inputs['Mortar Size'].default_value = 0.002; br.inputs['Mortar Smooth'].default_value = 0.0
    alap = (0.44, 0.435, 0.42, 1) if dekor else (0.50, 0.495, 0.48, 1)
    br.inputs['Color1'].default_value = alap; br.inputs['Color2'].default_value = tuple(x * 0.95 for x in alap[:3]) + (1,)
    br.inputs['Mortar'].default_value = (0.56, 0.56, 0.55, 1)   # Holdfény 103 – világos szürke fuga
    # rétegzett, hullámos sávok (üledékes kő) – a fotók (064/066) szerint lágy, átlós-hullámos világosabb erek
    wave = N('ShaderNodeTexWave'); wave.wave_type = 'BANDS'; wave.bands_direction = 'DIAGONAL'
    L(comb.outputs[0], wave.inputs['Vector']); wave.inputs['Scale'].default_value = 2.2; wave.inputs['Distortion'].default_value = 6.0
    wave.inputs['Detail'].default_value = 4.0
    ramp = N('ShaderNodeValToRGB'); L(wave.outputs['Fac'], ramp.inputs['Fac'])
    ramp.color_ramp.elements[0].color = (0.44, 0.435, 0.42, 1); ramp.color_ramp.elements[1].color = (0.60, 0.595, 0.58, 1)
    mix = N('ShaderNodeMix'); mix.data_type = 'RGBA'; mix.blend_type = 'MULTIPLY'; mix.inputs['Factor'].default_value = 0.0
    lap_szin = N('ShaderNodeMix'); lap_szin.data_type = 'RGBA'; lap_szin.inputs['Factor'].default_value = 0.0 if dekor else 0.35
    L(br.outputs['Color'], lap_szin.inputs['A']); L(ramp.outputs['Color'], lap_szin.inputs['B'])
    # fuga felülírja: a brick Fac=1 a fugán
    fuga = N('ShaderNodeMix'); fuga.data_type = 'RGBA'; L(br.outputs['Fac'], fuga.inputs['Factor'])
    L(lap_szin.outputs['Result'], fuga.inputs['A']); fuga.inputs['B'].default_value = (0.56, 0.56, 0.55, 1)
    # 2,85 m felett fehér festés
    gt = N('ShaderNodeMath'); gt.operation = 'GREATER_THAN'; L(sep.outputs['Z'], gt.inputs[0]); gt.inputs[1].default_value = 2.85
    feher = N('ShaderNodeMix'); feher.data_type = 'RGBA'; L(gt.outputs[0], feher.inputs['Factor'])
    L(fuga.outputs['Result'], feher.inputs['A']); feher.inputs['B'].default_value = (0.80, 0.80, 0.80, 1)
    L(feher.outputs['Result'], bs.inputs['Base Color']); bs.inputs['Roughness'].default_value = 0.55   # natúr (matt)
    bump = N('ShaderNodeBump'); bump.inputs['Strength'].default_value = 1.0 if dekor else 0.15
    if dekor:   # Esagonetta: apró hatszög-cellás 3D domborzat (a fotón kötött-texturált hatás)
        vor = N('ShaderNodeTexVoronoi'); vor.feature = 'DISTANCE_TO_EDGE'; L(comb.outputs[0], vor.inputs['Vector'])
        vor.inputs['Scale'].default_value = 22.0; vor.inputs['Randomness'].default_value = 0.15
        L(vor.outputs['Distance'], bump.inputs['Height'])
        # a hatszögcellák pereme sötétebb (a 3D felület árnyéka) – a fotókon (064, 145104) jól látható kötött mintázat
        el = N('ShaderNodeMath'); el.operation = 'LESS_THAN'; L(vor.outputs['Distance'], el.inputs[0]); el.inputs[1].default_value = 0.08
        sotet = N('ShaderNodeMix'); sotet.data_type = 'RGBA'; L(el.outputs[0], sotet.inputs['Factor'])
        L(fuga.outputs['Result'], sotet.inputs['A']); sotet.inputs['B'].default_value = (0.30, 0.297, 0.29, 1)
        L(sotet.outputs['Result'], feher.inputs['A'])
    else:
        L(br.outputs['Fac'], bump.inputs['Height']); bump.invert = True
    L(bump.outputs['Normal'], bs.inputs['Normal']); L(bs.outputs['BSDF'], out.inputs['Surface'])
    return m

def _anyag(nev, szin, rough=0.5, metal=0.0):
    m = bpy.data.materials.get(nev) or bpy.data.materials.new(nev); m.use_nodes = True
    b = m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value = szin
    b.inputs['Roughness'].default_value = rough; b.inputs['Metallic'].default_value = metal; return m

def _doboz(nev, a, b, mat, sc):
    me = bpy.data.meshes.new(nev); import bmesh; bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(nev, me); sc.collection.objects.link(o)
    o.location = [(a[i] + b[i]) / 2 for i in range(3)]; o.scale = [b[i] - a[i] for i in range(3)]; me.materials.append(mat); return o

def furdo06_2(sc, MARAD):
    log = {}
    G = lambda n, c, d=False, p=None: anyag_geostone(f'RENDER_{"Esagonetta_3D_30x60_63610A" if d else "Geostone_Grigio_NAT_60x60_62160A"}_{n}', d, c, p)
    lap = G('alap', 0.0)
    fekete = _anyag('RENDER_fekete_matt', (0.015, 0.015, 0.015, 1), 0.45)
    feher = _anyag('RENDER_kerámia_feher', (0.85, 0.85, 0.84, 1), 0.15)
    alu = _anyag('RENDER_eloxalt_alu', (0.55, 0.55, 0.56, 1), 0.35, 1.0)
    # falak: Geostone Grigio; zuhany hátfala (É) és a WC-előtétfal feletti fal (fülke D-i fala) Esagonetta 3D
    # kiosztás a 23. o. falnézetei szerint (fuga a jelölt tengelyen; tengelyek: zuhany y 7,61, WC x 14,965, „A” fal közepe x 15,96)
    kioszt = {'Fal_05_3_06_2_0': G('D_nyugati', 14.475 + 7.61), 'Fal_05_3_06_2_1': G('D_nyugati', 14.475 + 7.61),
              'Fal_05_3_06_2_szemoldok1': G('D_nyugati', 14.475 + 7.61), 'Kulso_K_06_2_0': G('F_keleti', 16.40 + 7.61),
              'Akna_06_2_EK_v2b1k10': G('A_B_akna', 15.96 + 5.81),
              'Kulso_E_terasz_2': G('E_zuhany_hatfal', 14.475 + 8.05, True),
              'Fal_06_2_D_v2b': G('C_WC_fal', 14.965 + 5.20, True), 'Akna_06_2': G('C_WC_fal', 14.965 + 5.20, True),
              'P_furdo_06_2': G('padlo', 0.0, False, (14.475, 5.40))}
    for n, m in kioszt.items():
        o = bpy.data.objects.get(n)
        if o:
            for s in o.material_slots: s.material = m
    falak = list(kioszt)
    log['burkolat'] = dict(fal_es_padlo='Geostone Grigio matt 60×60 (Ceramiche Piemme GEO GRIGIO NAT/RET, 62160A), fuga Holdfény 103, 2 mm; fal 2,85 m-ig, felette fehér',
                           dekor='Geostone Geo Esagonetta Grigio 3D 30×60 (63610A): zuhany északi hátfala (E) + a WC-előtétfal feletti falszakasz (C)',
                           kiosztas='23. o. falnézetek: fuga a zuhanytengelyen (y 7,61) a K-i és Ny-i falon, a WC-tengelyen (x 14,965) a fülkében, az „A” fal közepén (x 15,96); sorok felülről egész lappal (fuga 2,85 / 2,25 / 1,65 / 1,05 / 0,45 m), alul vágott sor; padló az ajtós fal belső síkjától (x 14,475) és a Geberit-előtétfal elejétől (y 5,40) egész lappal',
                           objektumok=falak + ['Kulso_E_terasz_2 (dekor)', 'Fal_06_2_D_v2b (dekor)', 'P_furdo_06_2'])
    # modell-szaniterek elrejtése, terv szerinti beépített elemek (render-réteg)
    for n in ['Zuhanyuveg_06_2', 'Zuhanytalca_06_2_182x85', 'Mosdo_06_2', 'Mosdoszekreny_06_2', 'Tukor_06_2', 'WC_tartaly_06_2']:
        o = bpy.data.objects.get(n)
        if o: o.hide_render = True
    wc = bpy.data.objects['WC_csesze_06_2']; wc.hide_render = True
    D = lambda *a: _doboz(*a, sc)
    D('RENDER_Geberit_eloetetfal_pm120', (14.475, 5.20, 0.0), (15.45, 5.40, 1.20), G('C_eloetetfal', 14.965 + 5.40))               # pm. 1,20, Geostone, teteje is lap
    D('RENDER_Geberit_Delta50_nyomolap_fekete', (14.85, 5.395, 0.98), (15.10, 5.41, 1.15), fekete)
    D('RENDER_WC_Smyle_Square_35x54', (14.79, 5.40, 0.27), (15.14, 5.94, 0.42), feher)
    D('RENDER_WC_ulőke', (14.79, 5.40, 0.42), (15.14, 5.94, 0.44), feher)
    D('RENDER_mosdo_Smyle_Square_60x48', (15.92, 6.33, 0.71), (16.40, 6.93, 0.86), feher)            # tengely y 6,63 (terv)
    D('RENDER_mosdocsaptelep_Cubeo_M_fekete', (16.29, 6.61, 0.86), (16.33, 6.65, 1.02), fekete)
    D('RENDER_mosdocsaptelep_kifolyo', (16.20, 6.61, 0.99), (16.33, 6.65, 1.02), fekete)
    D('RENDER_szifon_kromozott', (16.30, 6.61, 0.35), (16.34, 6.65, 0.71), alu)
    D('RENDER_padka_5x5_eloxalt_alu', (14.475, 7.15, 0.0), (16.40, 7.20, 0.05), alu)                 # 5/5 padka, élvédő
    D('RENDER_folyoka_Geberit_70cm', (16.24, 7.24, 0.001), (16.31, 7.94, 0.004), alu)                 # a csaptelep tengelyében, K-i fal mentén
    D('RENDER_Cubeo_sullyesztett_2funkcios_fedlap', (16.39, 7.53, 1.02), (16.40, 7.69, 1.18), fekete)  # tengely y 7,61
    D('RENDER_Cubeo_kar', (16.33, 7.60, 1.09), (16.39, 7.62, 1.11), fekete)
    D('RENDER_Tempesta_gegecso_csatlakozo_tartoval', (16.37, 7.78, 1.06), (16.40, 7.83, 1.14), fekete)
    D('RENDER_Rainshower_SmartActive_130_Cube_kezizuhany', (16.33, 7.77, 1.14), (16.37, 7.84, 1.40), fekete)
    D('RENDER_Cube250_fejzuhany', (16.02, 7.485, 2.12), (16.27, 7.735, 2.135), fekete)                 # 25×25
    D('RENDER_Cube250_zuhanykar', (16.27, 7.60, 2.12), (16.40, 7.62, 2.16), fekete)
    D('RENDER_torolkozoszarito_fekete', (14.475, 5.55, 0.50), (14.51, 6.00, 1.70), fekete)             # Ny-i fal, ajtó és fülke között
    log['beepitett_elemek'] = 'terv (18. o.) és költségvetés szerint, render-réteg: Geberit-előtétfal pm 1,20 Geostone-nal + Delta 50 fekete; Smyle Square fali WC 35×54 (tengely x 14,965); Smyle Square mosdó 60×48 (tengely y 6,63) + Cubeo M fekete; 5/5 padka alu élvédővel; 70 cm-es folyóka a K-i fal mentén; Cubeo süllyesztett 2 funkciós + Cube 250 fejzuhany karral + Tempesta csatlakozó + SmartActive 130 Cube kézizuhany (tengely y 7,61); fekete törölközőszárító a Ny-i falon. Üvegfal nincs, tükör nincs (átadáskor nem volt).'
    # fény: ablak nincs -> világ 0; meglévő ML10 mennyezeti pont
    for o in bpy.data.objects:
        if o.type == 'LIGHT': o.hide_render = True
    w = sc.world.node_tree.nodes['Background']
    for l in list(sc.world.node_tree.links):
        if l.to_node == w and l.to_socket.name == 'Color': sc.world.node_tree.links.remove(l)
    w.inputs['Strength'].default_value = 0.0
    ld = bpy.data.lights.new('RENDER_ML10_mennyezet', 'POINT'); ld.energy = 180; ld.shadow_soft_size = 0.30; ld.color = (1.0, 0.90, 0.80)
    lo = bpy.data.objects.new('RENDER_ML10_mennyezet', ld); lo.location = (15.449, 6.624, 2.82); sc.collection.objects.link(lo)
    sc.eevee.use_raytracing = True
    try: sc.eevee.ray_tracing_options.method = 'SCREEN'
    except Exception: pass
    try: sc.eevee.fast_gi_method = 'GLOBAL_ILLUMINATION'
    except Exception: pass
    log['feny_motor'] = 'EEVEE raytracing + gyors GI (a kis, ablaktalan térben a visszavert fényhez)'
    log['feny'] = 'csak műfény: meglévő ML10 mennyezeti pont (15,45; 6,62), 180 W pontfény, 30 cm sugár, ~4000 K; a mosdó feletti „g” fali pont (FL04) a referencián nem világít; világ 0; nincs nappali fény'
    return log

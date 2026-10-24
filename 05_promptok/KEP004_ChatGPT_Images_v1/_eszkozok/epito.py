# KEP-004 · ChatGPT Images · próbakör 1 – csomagépítő (Claude, 2026-10-24). Csak olvas a repóból; kimenet: staging + repo/05_promptok/KEP004_ChatGPT_Images_v1/
import os, sys, json, shutil, hashlib, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import forrasok as F
R = F.R; SCR = os.path.dirname(os.path.abspath(__file__)); TERM = SCR + '/../termek/'
STAGE = '/mnt/user-data/outputs/kep004_csomag/'
KOR = STAGE + '03_chatgpt_images_csomagok/probakor1_v1_2026-10-24/'
ATV = STAGE + '04_chatgpt_images_atvetel/probakor1/'
REPO_P = R + '05_promptok/KEP004_ChatGPT_Images_v1/'
VER = 'KEP004-CGI-v1'
B1 = '04_renderek/A902_alap_v2b1/'
FOTO = '08_allapotfelmeres/fotok/A902/'
P080 = FOTO + '04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg'
P045 = FOTO + '04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg'
P056 = FOTO + '02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg'
P077 = FOTO + '00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg'
P064 = FOTO + '06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg'
P066 = FOTO + '06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg'
PANO = '02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg'
SHEET = SCR + '/helyszin_kontaktlap_Cam02.jpg'
# termékek: kulcs → (fájl a termek/ mappában vagy None = Kave Home kézi, leírás angolul, rekord-azonosító, forrás-URL)
T = {
 'LENNON': ('ww_Lennon_L_jobbos_szurkesbarna_DEQ21WES12329-168260.jpg', 'Westwing Lennon modular corner sofa, right-hand chaise, taupe woven fabric (P14)', 'https://www.westwing.hu/lennon-modularis-sarokkanape-hu-21wes12329.html?simple=DEQ21WES12329-168260'),
 'TONI': ('ww_Toni_ovalis_200x90_vilagos_tolgy_DEQ19WES60483-150724.jpg', 'Westwing Toni oval dining table 200 × 90 cm, light oak veneer (P09)', 'https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html?simple=DEQ19WES60483-150724'),
 'ANOUK': ('ww_Anouk_uveg_180x90_23WES68910.jpg', 'Westwing Anouk clear glass dining table 180 × 90 cm (P08)', 'https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes68910.html'),
 'JATTEBO': ('ikea_JATTEBO_U_Samsala_sotetkek_49607648.jpg', 'IKEA JÄTTEBO 3.5-seat modular U with two chaises, Samsala dark blue (P04)', 'https://www.ikea.com/hu/hu/p/jaettebo-3-5-szemelyes-elemes-kanape-heverok-karfak-samsala-soetetkek-s49607648/'),
 'NORDLI': ('ikea_NORDLI_20349853.jpg', 'IKEA NORDLI white storage bed 180 × 200 (P10)', 'https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/'),
 'EKB31': ('ikea_EKBACKEN_vilagosszurke_beton_40616275.jpg', 'IKEA EKBACKEN worktop, light-grey concrete-effect laminate (AG-31)', 'https://www.ikea.com/hu/hu/p/ekbacken-munkalap-vilagosszuerke-beton-hatasu-laminalt-40616275/'),
 'EKB33': ('ikea_EKBACKEN_szurke-bezs_ko_20604320.jpg', 'IKEA EKBACKEN worktop, grey-beige stone-effect laminate (AG-33)', 'https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/'),
 'EAMY': (None, 'Kave Home Eamy chair, light-grey chenille, natural ash (KH-CH-EAMY-LG)', 'https://kavehome.com/hu/en/p/eamy-chair-light-grey-chenille-and-ash-wood-veneer-with-a-natural-finish-and-black-metal', 'KH_Eamy_szek_vilagosszurke'),
 'NIFELIA': (None, 'Kave Home Nifelia beige wool jacquard rug 200 × 300 (KH-RUG-NIFELIA)', 'https://kavehome.com/hu/en/p/nifelia-beige-wool-jacquard-rug-200-x-300-cm', 'KH_Nifelia_szonyeg_200x300'),
 'SOMAR': (None, 'Kave Home Somar pendant Ø76 (KH-PL-SOMAR76)', 'https://kavehome.com/hu/en/p/somar-ceiling-lamp-made-with-synthetic-fibres-and-steel-rods-o76cm', 'KH_Somar_fuggesztek_76'),
 'CISELIA': (None, 'Kave Home Ciselia chair, beige chenille, black steel legs (KH-CH-CISELIA-BK)', 'https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-steel-legs-with-black-finish-fsc-mix-credit', 'KH_Ciselia_szek_bezs_fekete'),
 'MARELY': (None, 'Kave Home Marely white wool rug 200 × 300 (KH-RUG-MARELY-W)', 'https://kavehome.com/hu/en/p/marely-white-wool-rug-200-x-300-cm', 'KH_Marely_szonyeg_feher_200x300'),
 'BRISIA': (None, 'Kave Home Brisia ceiling-mounted light (not a pendant), brushed brass, four frosted glass globes Ø15 cm, overall Ø80 × 26 cm high (KH-PL-BRISIA)','https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-4-frosted-glass-balls-o15cm', 'KH_Brisia_fuggesztek_sargarez'),
 # Péter 2026-10-24 23:35: a Brisia helyett választhatok másikat; az olvasólámpák designosak legyenek, Hue-izzó férjen beléjük
 'BRISIA50': (None, 'Kave Home Brisia pendant: one frosted glass globe Ø50 cm on a brushed-brass canopy and a black adjustable wire (L00152CR05)', 'https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-1-frosted-glass-ball-o50cm', 'KH_Brisia_fuggesztek_1gomb_50_sargarez'),
 'RAZE': (None, 'Kave Home Raze table lamp: beige marble cylinder base and beige linen drum shade, H54 × Ø22 cm (L0300109PR46)', 'https://kavehome.com/hu/en/p/raze-table-lamp-in-beige-marble-with-a-beige-linen-shade', 'KH_Raze_asztali_lampa_bezs_marvany'),
 'ALEYLA': (None, 'Kave Home Aleyla table lamp: maroon (deep plum-red) metal dome Ø22 cm on a slim black stem and round black base, H33 cm (AA6514R34)', 'https://kavehome.com/hu/en/p/aleyla-table-lamp-in-metal-with-maroon-finish', 'KH_Aleyla_asztali_lampa_bordo'),
}
CAM11_ALAP = SCR + '/../cam11/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png'   # a PR #15 ágáról (git show), változatlan
ROOM = {'Cam_02': ('nappali–terasz', 'living room – terrace (nappali–terasz)', 'Cam_02 · nappali–terasz', 1, 'nappali-terasz'),
        'Cam_03': ('konyha–étkező', 'kitchen – dining (konyha–étkező)', 'Cam_03 · konyha–étkező', 2, 'etkezo-konyha'),
        'Cam_04': ('master', 'master bedroom 05.1 (master)', 'Cam_04 · master háló 05.1', 3, 'master'),
        'Cam_10': ('fürdő 06.2', 'bathroom 06.2 (fürdő 06.2)', None, 4, 'furdo-06-2'),
        'Cam_11': ('master', 'master bedroom 05.1 (master)', None, 3, 'master')}
STY = {'S01': ('S01 — Kyoto Ink', 'S01 Kyoto Ink', 'KyotoInk'), 'S02': ('S02 — BiBo Nocturne', 'S02 BiBo Nocturne', 'BiBoNocturne'),
       'C1': (None, 'C1 Zenit – original concept, calibration', 'Zenit'), 'C2': (None, 'C2 Lake Forest – original concept, calibration', 'LakeForest')}
KAL_KEP = {('C1', 'Cam_02'): '04_renderek/ai_chatgpt/A902_Zenit_1_nappali_chatgpt.png', ('C2', 'Cam_02'): '04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png',
           ('C1', 'Cam_04'): '04_renderek/ai_chatgpt/A902_Zenit_3_master_chatgpt.png', ('C2', 'Cam_04'): '04_renderek/ai_chatgpt/A902_LakeForest_3_master_chatgpt.png',
           ('C1', 'Cam_11'): '04_renderek/ai_chatgpt/A902_Zenit_3_master_chatgpt.png', ('C2', 'Cam_11'): '04_renderek/ai_chatgpt/A902_LakeForest_3_master_chatgpt.png'}
KAL_FRONT = {'C1': 'Wardrobe fronts (C1 Zenit calibration): bronze-tinted real mirror doors, as in the original Zenit concept.',
             'C2': 'Wardrobe fronts (C2 Lake Forest calibration): cream laminate fronts with one narrow bronze-tinted real mirror band, as in the original Lake Forest concept.'}
TERMEKEK = {('S01', 'Cam_02'): ['LENNON', 'TONI', 'EAMY', 'NIFELIA', 'SOMAR'], ('S01', 'Cam_03'): ['TONI', 'EKB31', 'EAMY', 'SOMAR'],
            ('S01', 'Cam_04'): ['NORDLI', 'RAZE'], ('S01', 'Cam_10'): [], ('S01', 'Cam_11'): ['NORDLI'],
            ('S02', 'Cam_02'): ['JATTEBO', 'ANOUK', 'CISELIA', 'MARELY', 'BRISIA50'], ('S02', 'Cam_03'): ['ANOUK', 'EKB33', 'CISELIA', 'BRISIA50'],
            ('S02', 'Cam_04'): ['NORDLI', 'ALEYLA'], ('S02', 'Cam_10'): [], ('S02', 'Cam_11'): ['NORDLI']}
CSOMAGOK = [  # (sorszám, kód, kamera, lépés, státusz)
 (1, 'C1', 'Cam_02', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'), (2, 'C2', 'Cam_02', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'),
 (3, 'S01', 'Cam_02', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'), (4, 'S02', 'Cam_02', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'),
 (5, 'S01', 'Cam_03', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'), (6, 'S02', 'Cam_03', '1a', 'INDÍTHATÓ – Péter „mehet”-je után (1a lépés)'),
 (7, 'S01', 'Cam_10', '1b', 'INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)'), (8, 'S02', 'Cam_10', '1b', 'INDÍTHATÓ az 1a Gate-je után – Péter „mehet”-je kell (1b lépés)'),
 (9, 'C1', 'Cam_04', '1c', 'INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)'), (10, 'C2', 'Cam_04', '1c', 'INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)'),
 (11, 'S01', 'Cam_04', '1c', 'INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)'), (12, 'S02', 'Cam_04', '1c', 'INDÍTHATÓ az 1a/1b Gate-je után – Péter „mehet”-je kell (1c lépés)'),
 (13, 'C1', 'Cam_11', '1c', 'A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)'), (14, 'C2', 'Cam_11', '1c', 'A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)'),
 (15, 'S01', 'Cam_11', '1c', 'A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)'), (16, 'S02', 'Cam_11', '1c', 'A PR #15 beolvasztása („mehet”) után, ugyanabban a chatben, közvetlenül a Cam_04-párja után (1c lépés)')]
def kepid(kod, cam):
    r = ROOM[cam]; s = STY[kod]
    return f"A902_{kod}_{s[2]}_{r[3]}_{r[4]}_{cam}_A"
def bemenetek(kod, cam):
    """→ csatolandó lista: (fájlnév a csomagban, forrás, szerep angolul, szerep magyarul, kötelező?)"""
    L = []
    if cam == 'Cam_02':
        L += [('01_kep1_blender_alap_Cam02_v2b1.png', R + B1 + 'A902_Alap-v2b1_blender_02_nappali-terasz.png', 'image 1 – Blender empty-room base, camera Cam_02 (authoritative geometry, camera, framing)', 'Blender-alapkép (geometria, kamera)'),
              ('02_kep2_padlo_ME-BAL-080.jpg', R + P080, 'image 2 – site photo ME-BAL-080: the existing floor laminate, its colour, grain and skirting', 'helyszíni fotó: padló'),
              ('03_kep2b_helyszin_falak-profilok-terasz.jpg', SHEET, 'image 2b – site photo sheet ME-BAL-045/046/042/044/053: white walls, white inner frames with dark brick reveal, terrace porcelain tiles, steps and raised WPC deck', 'helyszíni fotók: fal, profil, terasz (kontaktlap)'),
              ('04_kep2c_panorama_terasz.jpg', R + PANO, 'image 2c – the real panorama from the terrace (video still): the actual exterior view', 'valós panoráma')]
    elif cam == 'Cam_03':
        L += [('01_kep1_blender_alap_Cam03_v2b1.png', R + B1 + 'A902_Alap-v2b1_blender_03_etkezo-konyha.png', 'image 1 – Blender empty-room base, camera Cam_03 (authoritative geometry, camera, framing)', 'Blender-alapkép (geometria, kamera)'),
              ('02_kep2_padlo_ME-BAL-080.jpg', R + P080, 'image 2 – site photo ME-BAL-080: the existing floor laminate', 'helyszíni fotó: padló'),
              ('03_kep2b_konyhafal_ME-BAL-056.jpg', R + P056, 'image 2b – site photo ME-BAL-056: the kitchen wall with its existing outlets and the low parapet wall', 'helyszíni fotó: konyhafal, kiállások, mellvéd'),
              ('04_kep2c_nappali_terasz_fele_ME-BAL-045.jpg', R + P045, 'image 2c – site photo ME-BAL-045: white walls and white inner window frames', 'helyszíni fotó: fal, profil')]
    elif cam == 'Cam_04':
        L += [('01_kep1_blender_alap_Cam04_v2b1.png', R + B1 + 'A902_Alap-v2b1_blender_04_master.png', 'image 1 – Blender empty-room base, camera Cam_04 (authoritative geometry, camera, framing)', 'Blender-alapkép (geometria, kamera)'),
              ('02_kep2_padlo_ME-BAL-080.jpg', R + P080, 'image 2 – site photo ME-BAL-080: the existing floor laminate', 'helyszíni fotó: padló'),
              ('03_kep2b_05-1_szoba_ME-BAL-077.jpg', R + P077, 'image 2b – site photo ME-BAL-077 taken in this room 05.1: white walls, niche, pillar, white frames, floor (its glass wall lies outside this camera view)', 'helyszíni fotó: 05.1 (fal, fülke, pillér, profil)')]
    elif cam == 'Cam_11':
        L += [('01_kep1_blender_alap_Cam11_v2b1k11.png', CAM11_ALAP, 'image 1 – Blender empty-room base, camera Cam_11 master panorama (authoritative geometry, camera, framing)', 'Blender-alapkép (geometria, kamera) – PR #15'),
              ('02_kep2_padlo_ME-BAL-080.jpg', R + P080, 'image 2 – site photo ME-BAL-080: the existing floor laminate', 'helyszíni fotó: padló'),
              ('03_kep2b_05-1_uvegfal_kilatas_ME-BAL-077.jpg', R + P077, 'image 2b – site photo ME-BAL-077 taken in this room 05.1: the real glass wall, balcony railing and the actual view (city roofs, church spire, Buda hills)', 'helyszíni fotó: 05.1 üvegfal és valós kilátás')]
    elif cam == 'Cam_10':
        L += [('01_kep1_blender_alap_Cam10_v2b1k10.png', R + B1 + 'A902_Alap-v2b1_blender_10_furdo-06-2.png', 'image 1 – Blender empty-room base, fixed camera Cam_10 (authoritative geometry, camera, framing; tiles and sanitary ware simplified)', 'Blender-alapkép (geometria, kamera)'),
              ('02_kep2_furdo06-2_zuhany_mosdo_ME-BAL-064.jpg', R + P064, 'image 2 – site photo ME-BAL-064 of this bathroom 06.2: Geostone Grigio tiles, Esagonetta 3D decor wall, walk-in shower, black fittings, basin', 'helyszíni fotó 06.2: zuhany, mosdó, burkolat, dekor'),
              ('03_kep2b_furdo06-2_wc_torolkozoszarito_ajto_ME-BAL-066.jpg', R + P066, 'image 2b – site photo ME-BAL-066 of this bathroom 06.2: WC on the tiled ledge, black flush plate, black towel radiator, door', 'helyszíni fotó 06.2: WC, törölközőszárító, ajtó')]
    n = len(L) + 1
    if kod in ('C1', 'C2'):
        L.append((f'{n:02d}_kep3_eredeti_{STY[kod][2]}_referencia.png', R + KAL_KEP[(kod, cam)], f'image 3 – the original {STY[kod][2]} concept image (concept only, not validated, different camera): mood and quality bar only, never geometry', f'eredeti {STY[kod][2]}-kép (csak hangulat/minőség)'))
    else:
        for k in TERMEKEK[(kod, cam)]:
            t = T[k]
            if t[0]:
                L.append((f'{n:02d}_kep4_termek_{t[0]}', TERM + t[0], f'product photo – {t[1]}', f'termékfotó: {t[1]}')); n += 1
        for k in TERMEKEK[(kod, cam)]:
            t = T[k]
            if not t[0]:
                kh = kave_kep(t[3])
                if kh:
                    eredeti = t[3] in KAVE_EREDETI
                    L.append((f'{n:02d}_kep4_termek_{t[3]}' + os.path.splitext(kh)[1], kh, f'product photo – {t[1]}' + ('' if eredeti else ' (cropped from the Kave Home product page, reduced resolution)'), f'termékfotó: {t[1]} – Kave Home, ' + ('a termékoldal fő képe (böngészőből, 2026-10-24)' if eredeti else 'Péter képernyőképéből kivágva'))); n += 1
                else:
                    L.append((f'{n:02d}_kep4_termek_{t[3]}.jpg', None, f'product photo – {t[1]} (attached only if available)', f'termékfotó: {t[1]} – KÉZI MENTÉS (Kave Home)')); n += 1
    return L
KEZI = KOR + '00_KAVE_HOME_KEZI_MENTES/'
KAVE_EREDETI = {'KH_Brisia_fuggesztek_1gomb_50_sargarez', 'KH_Raze_asztali_lampa_bezs_marvany', 'KH_Aleyla_asztali_lampa_bordo'}   # a termékoldal fő képe, a böngészőből (Péter kérése, 23:39)
def kave_kep(nev):  # a Kave Home termékkép a kézi mentési mappában (Claude kivágása Péter képernyőképéből vagy Péter saját mentése)
    for e in ('.jpg', '.jpeg', '.png', '.webp'):
        if os.path.exists(KEZI + nev + e): return KEZI + nev + e
    return None
def futtatasi_fejlec(id_, kod, cam, L):
    sor = [f"KEP-004 · ChatGPT Images · image ID {id_} · prompt version {VER} (2026-10-24, compiled by Claude; sources and checksums in 05_promptok/KEP004_ChatGPT_Images_v1/README.md)",
           "RUN AUTHORISATION: the project owner sends this message only when the KEP-004 gate for this image is open – sending it is the approval. Generate exactly ONE image.",
           "", "ATTACHED IMAGES, in this order (the text below calls them image 1, image 2, image 2b … as listed):"]
    for f, s, en, hu in L: sor.append(f"- {en}")
    sor += ["", "OUTPUT: one photorealistic interior photograph in landscape format with exactly the framing and perspective of image 1 (16:10; if that format is not offered, use the closest landscape format and extend the frame evenly – never crop or alter the geometry). True-to-life neutral colours. No text, labels, watermarks, people or logos. File names and repository paths in the text are for the project archive only."]
    return '\n'.join(sor)
def jegyzetek(kod, cam):
    J = []
    if cam in ('Cam_02', 'Cam_03', 'Cam_04'):
        J.append("Image 1 is the current v2b-1 base (identical camera parameters to the v2b base named in the style block; Cam_02/Cam_03 pixel-identical, Cam_04 only the corrected 05.1 niche facade differs).")
    if cam == 'Cam_02':
        J.append("The annotated check drawing (semleges_v2b …_ellenorzo.png) is deliberately not attached: it contains text and hatching; its facts are already in the fixed blocks.")
    if cam == 'Cam_04':
        J.append("Master 05.1 is shown from two cameras (owner decision 2026-10-24 23:33): this Cam_04 view shows the headboard wall and the north wardrobe niche; the Cam_11 panorama view of the same furnished room follows in this chat as the next message.")
        J.append("Site photos ME-BAL-060/069/063 named in the style block show other rooms (05.3) and are not used; ME-BAL-077 (image 2b) is the room-confirmed photo of 05.1.")
        J.append("The bed stands with its headboard against the right-hand (east) wall of image 1, centred between the two bedside socket groups (the plan position, owner decision 2026-10-24 23:35), its foot towards the window wall behind the camera.")
    if cam == 'Cam_11':
        J.append("Image 1 is the Cam_11 empty-room base rendered with the same settings as the other bases (v2b-1-k11, draft PR #15).")
        J.append("Master 05.1 is shown from two cameras (owner decision 2026-10-24 23:33). Send this prompt in the same chat directly after the Cam_04 image of the same style: keep every furnishing, material, colour and light of that image identical – only the camera changes. Generate a new image from the camera of image 1 attached to this message; do not edit or crop the previous image. If this chat has no Cam_04 image of this style, follow the blocks below alone.")
        J.append("The style block below was written for Cam_04: its Output line names the Cam_04 file – this run's image ID is " + kepid(kod, cam) + ". Its headboard, the bedside blocks and the reading lamps stand behind this camera and are not visible; the north wardrobe wall is at the right edge, the south wardrobe strip at the left edge.")
        J.append("Site photos ME-BAL-060/069/063 named in the style block show other rooms (05.3) and are not used; ME-BAL-077 (image 2b) is the room-confirmed photo of 05.1 and shows its real view.")
    if kod == 'S01' and cam == 'Cam_04':
        J.append("Reading lamps (owner requirement 2026-10-24 23:35: designer pieces that take a Philips Hue bulb): one Kave Home Raze table lamp on each bedside block – beige marble cylinder base, beige linen drum shade, H54 × Ø22 cm (L0300109PR46) – plugged into D20/21 and D22/23 through the headboard cut-outs, cables hidden behind the blocks. This settles the style block's fixture gate for the reading lights.")
        J.append("Hue check (Kave Home specification, 2026-10-24): Raze has an E27 lampholder (max. 40 W) inside an open linen drum – a standard Philips Hue E27 bulb fits.")
    if kod == 'S02' and cam == 'Cam_04':
        J.append("Reading lamps (owner requirement 2026-10-24 23:35: designer pieces that take a Philips Hue bulb): one Kave Home Aleyla table lamp on each bedside block – maroon metal dome Ø22 cm on a slim black stem and round black base, H33 cm (AA6514R34) – plugged into D20/21 and D22/23 through the headboard cut-outs, cables hidden. This settles the style block's fixture gate for the reading lights.")
        J.append("Hue check (Kave Home specification, 2026-10-24): Aleyla has an E14 lampholder (max. 25 W) under the dome – a Philips Hue E14 bulb fits.")
    if cam == 'Cam_10':
        J.append("The fixed Cam_10 block above replaces the provisional camera of the template (that position fell inside the WC). Image 1 now exists and the photos of image 2/2b are room-confirmed 06.2 – the style block's statements that image 1 does not exist and that ME-BAL-064/066 are provisional are superseded.")
        J.append("Known simplifications of image 1, not validated: the model's old simplified sanitary blocks overlap the walls by 2–10 cm and the hexagonal 3D decor tile is an approximate procedural pattern – follow image 2/2b for the real tiles, decor, fittings and their exact positions.")
    if kod == 'S01' and cam in ('Cam_02', 'Cam_03'):
        J.append("Eamy chair outer dimensions from the Kave Home product drawing (screenshot by the owner, 2026-10-24): width 55 × depth 53 × height 75 cm, seat height 46 cm, seat 45 × 42 cm – use these; the 'outer dimensions NOT RECORDED' note of record KH-CH-EAMY-LG is resolved.")
    if kod == 'S01' and cam in ('Cam_02', 'Cam_03'):
        J.append("Hue check (Kave Home specification, 2026-10-24): the Somar is a wire-suspended pendant with an E27 lampholder (max. 40 W) – it is fitted with a Philips Hue E27 bulb.")
    if kod == 'S02' and cam in ('Cam_02', 'Cam_03'):
        J.append("Ciselia chair outer dimensions from the Kave Home product drawing (screenshot by the owner, 2026-10-24): width 52.5 × depth 55 × height 75 cm, seat height 47 cm, seat 46 × 43 cm, legs Ø2.5 cm – use these; the 'outer dimensions NOT RECORDED' note of record KH-CH-CISELIA-BK is resolved.")
    if kod == 'S02' and cam in ('Cam_02', 'Cam_03'):
        J.append("Dining pendant (owner decision 2026-10-24 23:35): the four-globe Brisia named in the style block (KH-PL-BRISIA) is a flush ceiling light that cannot hang over the table, so it is replaced by the Brisia pendant of the same family – one frosted glass globe Ø50 cm on a brushed-brass canopy and a black adjustable wire (Kave Home L00152CR05). It hangs straight down from the existing point ML04 (about 0.20 m from the table centre – do not move it to the table centre), the globe's lowest point about 70–75 cm above the table top. Wherever the style block says KH-PL-BRISIA or 'four frosted Brisia globes', use this single-globe pendant.")
        J.append("Hue check (Kave Home specification, 2026-10-24): the Brisia pendant has an E27 lampholder (max. 25 W) and a Ø97 mm opening in the globe – a standard Philips Hue E27 bulb fits.")
    if kod in ('C1', 'C2'):
        J.append("LED elements named in the original concept (LED mirror, LED strips) are rendered as Philips Hue light strips or Hue-bulb fittings, following the Hue requirement above.")
    if kod in ('S01', 'S02'):
        if any(not T[k][0] for k in TERMEKEK[(kod, cam)]):
            J.append("No original Zenit/Lake Forest reference is attached to this style run (to avoid mixing styles). The Kave Home product photos come from the Kave Home product pages (2026-10-24; some are crops of the owner's screenshots at reduced resolution): use them for shape, proportion, colour and material only; where a product photo is missing, follow its text record exactly.")
        else:
            J.append("No original Zenit/Lake Forest reference is attached to this style run (to avoid mixing styles).")
    if kod in ('C1', 'C2'):
        J.append("Calibration image: render the original concept honestly with buildable, honestly named materials – it sets the quality bar and is not a competitor. Peter's sofa rule applies: at least L-shaped, preferably U-shaped (a curved sofa only with a pouf that makes it work as L/U).")
    return J
def prompt(kod, cam, L):
    id_ = kepid(kod, cam); r = ROOM[cam]; s = STY[kod]
    reszek = [futtatasi_fejlec(id_, kod, cam, L)]
    kf = F.kozos_fixed().replace('{ROOM}', r[1]).replace('{STYLE_NAME}', s[1])
    reszek.append("=== COMMON FIXED BLOCK – template v3.1 §1, verbatim (room and style name filled in) ===\n" + kf)
    if cam == 'Cam_10':
        reszek.append("=== ROOM FIXED BLOCK – Cam_10 · bathroom 06.2: the fixed camera block v1 (05_promptok/A902_Cam10_furdo06_2_rogzitett_kamerablokk_v1.md) replaces the provisional template block, verbatim ===\n" + F.cam10_csere())
    elif cam == 'Cam_11':
        reszek.append("=== ROOM FIXED BLOCK – Cam_11 · master 05.1 panorama: the camera block proposal v1 (05_promptok/A902_Cam11_master05_1_kamerablokk_JAVASLAT_v1.md, draft PR #15) replaces the template's Cam_04 block, verbatim ===\n" + F.cam11_csere())
    else:
        reszek.append(f"=== ROOM FIXED BLOCK – template v3.1 §2 {r[2]}, verbatim ===\n" + F.helyiseg_fixed(r[2]))
    reszek.append("=== OWNER REQUIREMENT – Philips Hue lighting (05_promptok/A902_Hue_vilagitas_FIXED_kiegeszites_v1.md), verbatim ===\n" + F.hue_blokk())
    if cam in ('Cam_04', 'Cam_11'):
        front = KAL_FRONT[kod] if kod in KAL_FRONT else F.gardrob_front(kod)
        reszek.append("=== OWNER DECISION ADDENDUM – 05.1 wardrobe wall (05_promptok/A902_05_1_gardrobfal_FIXED_kiegeszites_v1.md), verbatim ===\n" + F.gardrob_blokk() + "\n" + front)
    if kod in ('S01', 'S02'):
        cim = f"{s[0]} · {r[0]} ({'Cam_04' if cam == 'Cam_11' else cam})"   # a Cam_11-nek nincs külön Astra-blokkja: a master (Cam_04) stílusblokk szó szerint
        reszek.append(f"=== STYLE BLOCK – Astra V2 r1, verbatim ===\n" + F.astra(cim))
    else:
        hely = 'Nappali' if cam == 'Cam_02' else 'Master háló'; ver = 'Zenit' if kod == 'C1' else 'Lake Forest'
        reszek.append(f"=== CALIBRATION BLOCK – template v3.1 §3, verbatim (Hungarian) ===\n" + F.kalibracio(kod) +
                      f"\n\nA-902 · {hely} – the original concept for this room (06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md, {ver}-verzió, verbatim, Hungarian):\n" + F.koncepcio_cella(ver, hely))
    reszek.append("=== RUN NOTES – Claude, 2026-10-24 (where the style block's 'Inputs' line differs, these notes apply) ===\n" + '\n'.join('- ' + j for j in jegyzetek(kod, cam)))
    return id_, '\n\n'.join(reszek) + '\n'
if __name__ == '__main__':
    for d in (KOR, ATV, REPO_P):
        os.makedirs(d, exist_ok=True)
    nyilv = []
    for nr, kod, cam, lepes, statusz in CSOMAGOK:
        L = bemenetek(kod, cam); id_, txt = prompt(kod, cam, L)
        mappa = KOR + f'{nr:02d}_{id_}/'; os.makedirs(mappa, exist_ok=True)
        open(mappa + f'PROMPT_{id_}.prompt.txt', 'w', encoding='utf-8').write(txt)
        open(REPO_P + f'{id_}.prompt.txt', 'w', encoding='utf-8').write(txt)
        for f, src, en, hu in L:
            if src:
                shutil.copy2(src, mappa + f)
                regi = mappa + '_HIANYZIK_' + os.path.splitext(f)[0] + '.txt'   # korábbi hiányjelző → _POTOLVA_ (nem törlés)
                if os.path.exists(regi): os.rename(regi, mappa + '_POTOLVA_' + os.path.splitext(f)[0] + '.txt')
            else:
                open(mappa + '_HIANYZIK_' + f.replace('.jpg', '.txt'), 'w', encoding='utf-8').write(
                    f"Ez a Kave Home termékfotó kézi mentést igényel (a Kave Home tiltja a gépi letöltést).\nMentsd a fő termékképet ide: ../00_KAVE_HOME_KEZI_MENTES/ – Claude szétosztja ebbe a csomagba ezen a néven: {f}\n")
        sorok = [f"# {nr:02d} · {id_}", '', f"**Státusz:** {statusz}. Képgenerálás csak Péter „mehet”-je után, normál ChatGPT-chatben (nem Work).", f"**Lépés:** {lepes} · **promptverzió:** {VER} · **prompt:** `PROMPT_{id_}.prompt.txt` ({len(txt)} karakter, sha256 `{F.sha(txt)[:16]}…`)", '',
                 '## Futtatás', '1. Új ChatGPT-chat (normál chat).', '2. Jelöld ki a **01, 02, 03 … kezdetű képfájlokat**, és húzd be őket egyszerre. Ellenőrizd, hogy a csatolmánysávban ebben a sorrendben látszanak.', '3. Másold be a `PROMPT_…prompt.txt` teljes szövegét, és küldd el.', f'4. A kész képet töltsd le, és dobd ide: `04_chatgpt_images_atvetel/probakor1/{nr:02d}_{id_}/` (átnevezni nem kell). A chat linkjét írd az `ATVETELI_NAPLO.csv`-be, vagy szólj.', '',
                 '## Csatolandó képek (sorrendben)', '| # | Fájl | Szerep | Állapot |', '|---|---|---|---|']
        for i, (f, src, en, hu) in enumerate(L, 1):
            sorok.append(f"| {i} | `{f}` | {hu} | {('megvan (Kave Home – kivágás Péter képernyőképéből, 2026-10-24)' if src and src.startswith(KEZI) else 'megvan') if src else '**HIÁNYZIK – Kave Home kézi mentés** (`00_KAVE_HOME_KEZI_MENTES/`)'} |")
        sorok += ['', '## Nem csatolandó / eltérések a stílusblokk „Inputs” sorától'] + ['- ' + j for j in jegyzetek(kod, cam)]
        open(mappa + '00_CSOMAG.md', 'w', encoding='utf-8').write('\n'.join(sorok) + '\n')
        os.makedirs(ATV + f'{nr:02d}_{id_}/', exist_ok=True)
        open(ATV + f'{nr:02d}_{id_}/_ide_tedd_a_kesz_kepet.txt', 'w', encoding='utf-8').write(
            f"Ide jön a ChatGPT-ből letöltött kép ehhez: {id_} (átnevezni nem kell).\nHa újragenerálás kell, a második kép is ide jöhet – Claude _v2 utótaggal archiválja.\nA chat linkjét írd az ATVETELI_NAPLO.csv-be (chat_link oszlop) vagy szólj Claude-nak.\n")
        nyilv.append(dict(nr=nr, id=id_, kod=kod, kamera=cam, lepes=lepes, statusz=statusz, prompt_sha256=F.sha(txt), prompt_karakter=len(txt),
                          bemenetek=[dict(fajl=f, forras=(src.replace(R, '') if src and src.startswith(R) else (('00_KAVE_HOME_KEZI_MENTES/' + os.path.basename(src) + ' (Kave Home – Péter képernyőképe vagy a böngészőből mentve)') if src and src.startswith(KEZI) else (('PR #15 ág (' + F.PR15 + '): 04_renderek/A902_cam11_javaslat_v1/' + os.path.basename(src)) if src and src == CAM11_ALAP else (os.path.basename(src) if src else 'Kave Home – kézi mentés')))), szerep=hu,
                                          sha256=(hashlib.sha256(open(src, 'rb').read()).hexdigest() if src else None)) for f, src, en, hu in L]))
    json.dump(nyilv, open(SCR + '/csomag_nyilvantartas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('KÉSZ', len(nyilv))

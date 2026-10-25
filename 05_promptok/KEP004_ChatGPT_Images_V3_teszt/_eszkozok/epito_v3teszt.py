# KEP-004 · V3 próbakép-promptok összefűzése (S01, S02 Cam_02) – Claude, 2026-10-25.
# Péter „mehet”: 2026-10-25 02:06, képenként pontosan EGY generálás. Források (nem módosítva):
#  - v1 promptok (közös FIXED, Cam_02 FIXED, Hue blokk, termékleírások): 05_promptok/KEP004_ChatGPT_Images_v1/
#  - Astra Creative Upgrade V3 r1: PR #16, commit be6b1f333cf2923790e4577c9b716f5fcb3bb417 (git show-val olvasva)
#  - Cam_02 geometriai v2 blokk (fee7123) + a V3 tömegek Blenderrel vetített képtéri helyei (cam12_ellenorzes_log_v1.json)
# Futtatás a repó gyökeréből: python3 05_promptok/KEP004_ChatGPT_Images_V3_teszt/_eszkozok/epito_v3teszt.py
import subprocess, hashlib, json, os, re
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
V1 = os.path.join(R, '05_promptok', 'KEP004_ChatGPT_Images_v1')
KI = os.path.join(R, '05_promptok', 'KEP004_ChatGPT_Images_V3_teszt')
ASTRA_COMMIT = 'be6b1f333cf2923790e4577c9b716f5fcb3bb417'
ASTRA_UT = '05_promptok/A902_S01_S02_Cam02_CREATIVE_UPGRADE_V3_r1.md'
astra = subprocess.run(['git', '-C', R, 'show', f'{ASTRA_COMMIT}:{ASTRA_UT}'], capture_output=True, text=True, check=True).stdout
sha = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
def blokk(szoveg, kezdet, veg):
    i = szoveg.index(kezdet); j = szoveg.index(veg, i + len(kezdet)); return szoveg[i:j].rstrip('\n')
# ---- Astra V3: felületkivétel + két stílusblokk (szó szerint) ----
kivetel = blokk(astra, '## Felületkivétel – angol szövegjavaslat', '### S01 — Kyoto Ink').split('\n', 1)[1].strip()
V3 = {'S01': blokk(astra, '### S01 — Kyoto Ink · nappali–terasz (Cam_02) · Creative Upgrade V3 r1', '\n---\n'),
      'S02': blokk(astra, '### S02 — BiBo Nocturne · nappali–terasz (Cam_02) · Creative Upgrade V3 r1', '## Gazdaságos anyagcsere')}
# A V3 r1 „Light:” bekezdése helyett a tesztre szóló semleges bekezdés (Péter 01:49 és 02:06: a LED-tiltás nem jövőbeli szabály; V3.1-es LED-et sem találunk ki)
FENY = {
 'S01': ("Light (V3 TEST – this paragraph replaces the V3 r1 'Light' paragraph for this test image only, owner instruction 2026-10-25): "
         "Neutral overcast daylight, identical exposure and white balance to the comparison series; no warm grading. Show only the existing, verified light points: "
         "the Kave Home Somar Ø76 pendant (E27, Philips Hue bulb) belongs only at A902-ML04, which is outside this Cam_02 frame, so no pendant is visible; "
         "A902-ML05 carries no added fixture in this test; A902-FL02, the TV service block and exterior FL05–07 stay free and accessible. "
         "Hidden Hue-compatible LED lighting is a later design stage and is not part of this test image: add no LED strips, glowing panels, illuminated cabinets, "
         "backlit art or new light fittings. No new ceiling anchor or electrical point."),
 'S02': ("Light (V3 TEST – this paragraph replaces the V3 r1 'Light' paragraph for this test image only, owner instruction 2026-10-25): "
         "Neutral overcast daylight, same exposure and white balance as S01; no warm grading. Satin fronts and actual reflections provide the richness. "
         "Show only the existing, verified light points: the Kave Home Brisia L00152CR05 single Ø50 cm globe pendant (E27, Philips Hue bulb) belongs only at A902-ML04, "
         "which is outside this Cam_02 frame, so no pendant is visible; A902-ML05 carries no added fixture in this test. TV power stays at D16/D17; FL02 and exterior FL05–07 remain accessible. "
         "Hidden Hue-compatible LED lighting is a later design stage and is not part of this test image: add no LED strips, luminous mirror edges, illuminated cabinets "
         "or new light fittings. No new ceiling anchor or electrical point."),
}
for k in ("S01", "S02"):
    sor = [l for l in V3[k].split('\n') if l.startswith('Light:')]
    assert len(sor) == 1, k
    V3[k + '_eredeti_light'] = sor[0]
    V3[k + '_teszt'] = V3[k].replace(sor[0], FENY[k])
# ---- v1 promptokból a fix blokkok (szó szerint) ----
V1F = {'S01': 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A.prompt.txt', 'S02': 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A.prompt.txt'}
FEHER = 'Walls and ceilings: painted white, smooth, no colour cast.'
FRAME = {
 'S01': """=== GEOMETRY v2 + V3 FRAME LAYOUT – Cam_02 · S01 (Claude, 2026-10-25; computed in Blender from the v2b-1-k11b model, the owner-accepted layout P902_24A and the V3 r1 envelopes) ===
Image 1b is a grey massing render from exactly the same camera as image 1. It shows only WHERE each piece stands and how big it is – it is not a style, colour or material reference.
- Room shell: copy image 1 exactly – the same long left wall and corner position (about 47 % from the left edge), the same glass wall and sill line (the sill reaches the right frame edge at about 91 % of the image height), the same railing segment in front of the left glass pane and the same plain ceiling. Do not widen or deepen the room and do not move the glass wall back.
- Visible walls: W01 is the long left wall; W04 is the solid lintel strip above the glazing and the narrow pier between the left wall and the first glass profile. W02 (south) and W03 (east) are outside this frame.
- West wall ensemble (left wall): the narrow tall cabinet KI3-V (60 × 220 cm) stands at the far left and is cut by the left frame edge (about 0–14 % of the width, 24–83 % of the height); the two graphite background planes KI3-P (together 260 × 190 cm, lower edge 55 cm above the floor) cover about 13–45 % of the width and 21–64 % of the height; the TV hangs at about 23–40 % / 39–56 %; the low floor-supported cabinet KI3-L (240 × 48 cm) runs at about 16–46 % / 59–78 %.
- Sofa: the Lennon right-hand L (238 × 180 cm) stands in the centre foreground with its BACK to the camera and its seats facing the TV on the left wall. Its back runs across about 41–81 % of the width and is cut by the bottom edge; the chaise (seat height only, no back) extends from the back towards the left wall at about 25–66 % of the width, from about 71 % of the height to the bottom edge; the short north arm is at about 64–77 % / 65–75 %.
- Dining: only the west end of the Toni table (from about 73 % of the width to the right edge, below about 74 % of the height) and the backs of the three west-side Eamy chairs (about 59–89 % of the width, 70–100 % of the height, directly behind the sofa back) enter the frame; the rest of the dining group is outside the frame to the right.
- Ceiling: the dining pendant point ML04 is outside the frame, so no pendant is visible; the living point ML05 (about 44 % of the width at the top edge) carries no fixture in this test. No other ceiling fixtures, cords or tracks.
- The KI3-A artwork on the south wall W02 is outside this frame – do not show it and do not move it into view.
- Nothing else stands in the room: no coffee table, side table, floor or table lamp, sideboard or extra seating. Small accessories only on the listed pieces.""",
 'S02': """=== GEOMETRY v2 + V3 FRAME LAYOUT – Cam_02 · S02 (Claude, 2026-10-25; computed in Blender from the v2b-1-k11b model, the owner-accepted layout P902_24A and the V3 r1 envelopes) ===
Image 1b is a grey massing render from exactly the same camera as image 1. It shows only WHERE each piece stands and how big it is – it is not a style, colour or material reference.
- Room shell: copy image 1 exactly – the same long left wall and corner position (about 47 % from the left edge), the same glass wall and sill line (the sill reaches the right frame edge at about 91 % of the image height), the same railing segment in front of the left glass pane and the same plain ceiling. Do not widen or deepen the room and do not move the glass wall back.
- Visible walls: W01 is the long left wall; W04 is the solid lintel strip above the glazing and the narrow pier between the left wall and the first glass profile. W02 (south) and W03 (east) are outside this frame.
- West wall ensemble (left wall): the asymmetrical tall cabinet BN3-V (90 × 220 cm: one door column and one fixed mirror column) stands at the far left and is cut by the left frame edge (about 0–18 % of the width, 23–84 % of the height); the navy background BN3-P (240 × 190 cm, lower edge 55 cm above the floor) covers about 17–45 % of the width and 21–64 % of the height; the TV hangs at about 23–40 % / 39–56 %; the low floor-supported cabinet BN3-L (240 × 50 cm) runs at about 18–47 % / 58–78 %.
- Sofa: the JÄTTEBO true U (285 × 160 cm) stands in the centre foreground with its BACK to the camera; its open side faces the TV on the left wall. Its back runs across about 33–83 % of the width and is cut by the bottom edge; the south arm reaches towards the left wall at about 20–46 % of the width, from about 70 % of the height to the bottom edge; the north arm reaches towards the glass at about 51–79 % / 59–84 %. The central bay of the U stays empty.
- Dining: only the west end of the Anouk glass table (from about 76 % of the width to the right edge, below about 75 % of the height) and the backs of the three west-side Ciselia chairs (about 61–87 % of the width, 70–100 % of the height, directly behind the sofa back) enter the frame; the rest of the dining group is outside the frame to the right.
- Ceiling: the dining pendant point ML04 is outside the frame, so no pendant is visible; the living point ML05 (about 44 % of the width at the top edge) carries no fixture in this test. No other ceiling fixtures, cords or tracks.
- The BN3-A graphic on the south wall W02 is outside this frame – do not show it and do not move it into view.
- Nothing else stands in the room: no coffee table, side table, floor or table lamp, sideboard or extra seating. The removable arm tray is the only small addition. Small accessories only on the listed pieces.""",
}
ID = {'S01': 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_r1', 'S02': 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_r1'}
TOMEGKEP = {'S01': 'A902_Cam02_tomeg_S01_V3_v1.png', 'S02': 'A902_Cam02_tomeg_S02_V3_v1.png'}
FUGGO = {'S01': 'Kave Home Somar pendant', 'S02': 'Kave Home Brisia pendant'}
RUNNOTES = {
 'S01': """=== RUN NOTES – Claude, 2026-10-25 (V3 test; where the style block's 'Inputs' line differs, these notes apply) ===
- Owner approval 2026-10-25 02:06: exactly one generation of this V3 test image. It tests the Creative Upgrade V3 wall concept together with the corrected Cam_02 geometry; it is not the final image series.
- Image 1 is the same verified v2b-1 Cam_02 base as in the first test. Image 1b is new: the grey massing render of exactly these V3 pieces (KI3-L, KI3-V, KI3-P, TV, Lennon L, Toni table, six Eamy chairs) at their checked positions; the Blender check found no collision with walls, openings or door swings and no covered switch.
- Known tolerance of the owner-accepted layout P902_24A: the sofa back stands only about 38 cm from the backs of the west-side chairs (table edge to sofa back about 73 cm). Render exactly this – do not move the sofa or the dining group to create space.
- The pendant photo is deliberately not attached: its point ML04 is outside this frame.
- No material sample photos are attached (samples are not selected yet): follow the text – matte graphite laminate fronts and planes, a fine smoky-light-grey paper-fibre-effect nonwoven wallpaper on the uncovered parts of W01 and on W04, a matte printed graphic on the tall cabinet fronts. Render laminate as laminate and printed nonwoven as print, not stone, silk or lacquer.
- The failed first test image is not attached and must not be imitated (no table in the left foreground, no central pendant, no widened room).
- Eamy chair outer dimensions from the Kave Home product drawing: width 55 × depth 53 × height 75 cm, seat height 46 cm. The Kave Home product photos are crops of the product pages at reduced resolution: use them for shape, proportion, colour and material only.""",
 'S02': """=== RUN NOTES – Claude, 2026-10-25 (V3 test; where the style block's 'Inputs' line differs, these notes apply) ===
- Owner approval 2026-10-25 02:06: exactly one generation of this V3 test image. It tests the Creative Upgrade V3 wall concept together with the corrected Cam_02 geometry; it is not the final image series.
- Image 1 is the same verified v2b-1 Cam_02 base as in the first test. Image 1b is new: the grey massing render of exactly these V3 pieces (BN3-L, BN3-V with its fixed mirror column, BN3-P, TV, JÄTTEBO U, Anouk table, six Ciselia chairs) at their checked positions; the Blender check found no collision with walls, openings or door swings and no covered switch.
- Known tolerance of the owner-accepted layout P902_24A: the sofa back stands only about 36 cm from the backs of the west-side chairs (table edge to sofa back about 73 cm). Render exactly this – do not move the sofa or the dining group to create space.
- The pendant photo is deliberately not attached: its point ML04 is outside this frame.
- No material sample photos are attached (samples are not selected yet): follow the text – deep navy satin painted fronts (about 20–30 gloss), matte navy laminate background, a real silver mirror strip, a pale silver-grey woven-effect nonwoven wallpaper on the uncovered parts of W01 and on W04. No glitter, metallic or mirror wallpaper.
- The failed first S01 test image is not attached and must not be imitated (no table in the left foreground, no central pendant, no widened room).
- Ciselia chair outer dimensions from the Kave Home product drawing: width 52.5 × depth 55 × height 75 cm, seat height 47 cm. The Kave Home product photos are crops of the product pages at reduced resolution: use them for shape, proportion, colour and material only.""",
}
eredmeny = {'forras': {'astra_commit': ASTRA_COMMIT, 'astra_fajl': ASTRA_UT, 'astra_fajl_sha256': sha(astra)}, 'promptok': {}}
for k in ('S01', 'S02'):
    v1 = open(os.path.join(V1, V1F[k]), encoding='utf-8').read()
    fej_csatolt = blokk(v1, 'ATTACHED IMAGES', '\n\nOUTPUT:')
    output = blokk(v1, 'OUTPUT:', '\n\n=== COMMON FIXED')
    kozos = blokk(v1, '=== COMMON FIXED BLOCK', '\n\n=== ROOM FIXED')
    szoba = blokk(v1, '=== ROOM FIXED BLOCK', '\n\n=== OWNER REQUIREMENT')
    hue = blokk(v1, '=== OWNER REQUIREMENT – Philips Hue', '\n\n=== STYLE BLOCK')
    assert kozos.count(FEHER) == 1
    kozos_v3 = kozos.replace('=== COMMON FIXED BLOCK – template v3.1 §1, verbatim (room and style name filled in) ===',
                             '=== COMMON FIXED BLOCK – template v3.1 §1, verbatim (room and style name filled in) except the white-wall sentence, replaced by the Creative Upgrade V3 surface exception (Astra V3 r1, verbatim) ===')
    kozos_v3 = kozos_v3.replace(FEHER, 'Walls and ceilings – Creative Upgrade V3 surface exception: ' + kivetel)
    sorok = [l for l in fej_csatolt.split('\n') if l.startswith('- ')]
    termek = [l for l in sorok if l.startswith('- product photo') and FUGGO[k] not in l]
    assert len(termek) == 4, (k, termek)
    kepek = [l for l in sorok if l.startswith('- image')]
    assert len(kepek) == 4
    csatolt = '\n'.join(['ATTACHED IMAGES, in this order (the text below calls them image 1, image 1b, image 2, image 2b … as listed):', kepek[0],
                         '- image 1b – Blender grey massing render from exactly the same camera: positions and sizes of the V3 furniture and joinery (layout only – not a style, colour or material reference)'] + kepek[1:] + termek)
    fej = (f"KEP-004 · ChatGPT Images · image ID {ID[k]} · prompt version KEP004-CGI-V3TEST-r1 (2026-10-25, compiled by Claude from Astra Creative Upgrade V3 r1 – PR #16, commit be6b1f3 – and the Cam_02 geometry v2; sources and checksums in 05_promptok/KEP004_ChatGPT_Images_V3_teszt/README.md)\n"
           "RUN AUTHORISATION: the project owner approved exactly one generation of this V3 test image on 2026-10-25 02:06. Generate exactly ONE image.")
    stilus = '=== STYLE BLOCK – Astra Creative Upgrade V3 r1, verbatim except the \'Light\' paragraph (test version, see its first words) ===\n' + V3[k + '_teszt']
    prompt = '\n\n'.join([fej, csatolt, output, kozos_v3, szoba, hue, FRAME[k], stilus, RUNNOTES[k]]) + '\n'
    # ellenőrzések
    assert kivetel in prompt and V3[k + '_eredeti_light'] not in prompt and FENY[k] in prompt
    for darab in V3[k + '_teszt'].split('\n'):
        assert darab in prompt
    assert hue.split('\n', 1)[1] in prompt and szoba.split('\n', 1)[1] in prompt
    assert '{' not in prompt and 'TODO' not in prompt
    ut = os.path.join(KI, ID[k] + '.prompt.txt'); open(ut, 'w', encoding='utf-8').write(prompt)
    eredmeny['promptok'][k] = dict(kep_id=ID[k], fajl=os.path.relpath(ut, R), karakter=len(prompt), sha256=sha(prompt), csatolmany=2 + 3 + len(termek),
                                   termekfotok=[t[len('- product photo – '):] for t in termek], tomegkep=TOMEGKEP[k],
                                   v1_forras=V1F[k], v1_sha256=sha(v1), csere_light_eredeti=V3[k + '_eredeti_light'])
json.dump(eredmeny, open(os.path.join(KI, '_eszkozok', 'epites_v3teszt.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: (v['karakter'], v['sha256'][:16], v['csatolmany']) for k, v in eredmeny['promptok'].items()}, ensure_ascii=False))

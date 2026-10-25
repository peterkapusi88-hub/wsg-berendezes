# KEP-004 V3_TEST – r2 promptok a párhuzamos munkamenet r1 csomagjából (Claude, 2026-10-25 02:25–02:35).
# Péter 02:22: „A már elkészített két tesztcsomagot viszont használd fel … a két javított bútor-tömegreferenciát és a PASS
# validátort tekintsd kiindulásnak … javítsd a BiBo tükörre vonatkozó promptot … a kültéri padot ne helyezd el önkényesen.”
# Minden csere pontos szövegcsere (pontosan egyszer kell előfordulnia); a végén tiltott/kötelező kifejezés-ellenőrzés.
import sys, json, hashlib, difflib, os
R1 = {'S01': sys.argv[1], 'S02': sys.argv[2]}; OUT = sys.argv[3]; os.makedirs(OUT, exist_ok=True)
ID = {'S01': 'A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A', 'S02': 'A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A'}
FEJ_R1 = ("· prompt version KEP004-CGI-V3TEST-r1 (2026-10-25, compiled by Claude from Astra Creative Upgrade V3 r1 – PR #16, commit be6b1f3 – "
          "and the Cam_02 geometry v2; sources and checksums in 05_promptok/KEP004_ChatGPT_Images_V3_teszt/README.md)")
FEJ_R2 = ("· prompt version KEP004-CGI-V3TEST-r2 (2026-10-25, compiled by Claude from Astra Creative Upgrade V3 r1 – PR #16, commit be6b1f3 – "
          "the Cam_02 geometry v2 and the verified V3 massing; built on package r1, every change listed in "
          "05_promptok/KEP004_ChatGPT_Images_V3_TEST/INTEGRACIO_V3_TEST.md)")
KOZOS = [
 ('fejléc: verzió és forrás', FEJ_R1, FEJ_R2),
 ('fejléc: jóváhagyás (Péter 02:22, ebben a munkamenetben)',
  "RUN AUTHORISATION: the project owner approved exactly one generation of this V3 test image on 2026-10-25 02:06. Generate exactly ONE image.",
  "RUN AUTHORISATION: the project owner approved exactly two V3 test generations on 2026-10-25 02:22 – one S01 Kyoto Ink and one S02 BiBo Nocturne image. Generate exactly ONE image."),
 ('geometria: nyílászárók, padló, terasz (Péter 02:22: „az eredeti geometriát, nyílászárókat és padlót őrizd meg”; a padnak nincs ellenőrzött helye)',
  "W02 (south) and W03 (east) are outside this frame.\n",
  "W02 (south) and W03 (east) are outside this frame.\n"
  "- Openings and floor: keep the glazing exactly as in image 1 – the same white profiles and their division, the same sill line and door positions, nothing added or widened – and the existing grey-brown oak laminate of image 2 with its 6 cm skirting wherever floor is visible.\n"
  "- Terrace: exactly as in images 1 and 2b – the existing porcelain tiles, the raised WPC deck with its steps, the planted green roof and the anthracite railing, including the railing segment in front of the left glass pane. No terrace furniture is shown in this test image.\n"),
 ('futtatási jegyzet: jóváhagyás',
  "- Owner approval 2026-10-25 02:06: exactly one generation of this V3 test image. It tests the Creative Upgrade V3 wall concept together with the corrected Cam_02 geometry; it is not the final image series.",
  "- Owner approval 2026-10-25 02:22: exactly two V3 test generations (S01 and S02), one image each, from package version r2. It tests the Creative Upgrade V3 wall concept together with the corrected Cam_02 geometry; it is not the final image series.\n"
  "- Daylight – identical wording in both V3 test prompts (S01 and S02): soft neutral overcast daylight entering through the glass wall, no direct sun or sun patches, all interior lights off; exposure balanced so that the white ceiling keeps its detail and the darkest fronts are not crushed."),
]
SAJAT = {
 'S01': [
  ('stílusblokk-fejléc', "=== STYLE BLOCK – Astra Creative Upgrade V3 r1, verbatim except the 'Light' paragraph (test version, see its first words) ===",
   "=== STYLE BLOCK – Astra Creative Upgrade V3 r1, verbatim except the 'Light' paragraph (test version, see its first words) and the technical integration of the position, terrace-bench, inputs and output lines (Claude, 2026-10-25) ==="),
  ('pozíciók: ellenőrizve (Blender v2b-1-k11b, validátor PASS)',
   "- Proposed, not yet validated wall positions: KI3-V y=4.35–4.95; KI3-L y=5.15–7.55; KI3-P y=5.05–7.65. Claude must verify these against devices, openings, cabinet-door sweeps and circulation before execution. Do not alter the room if a component conflicts.",
   "- Verified wall positions (Claude, 2026-10-25 – Blender v2b-1-k11b, validator PASS, shown in image 1b): KI3-V y=4.35–4.95; KI3-L y=5.15–7.55; KI3-P y=5.05–7.65. Socket D18 stays reachable through the back of the tower's lowest compartment; D16/D17/G08 sit behind the removable service back of KI3-L. Do not alter the room."),
  ('kültéri pad: nincs ellenőrzött hely → nem jelenik meg',
   "- Retain the already specified KI-O freestanding terrace bench only at the approved position on existing gres, W160×H42×D60 cm, aluminium/outdoor HPL. Do not redesign the terrace planting, railing or level changes.",
   "- KI-O terrace bench (W160×H42×D60 cm, aluminium/outdoor HPL): no verified position has been fixed yet, so it is not shown in this image. Do not redesign the terrace planting, railing or level changes."),
  ('bemenetek: a ténylegesen csatolt képek',
   "Inputs (Claude to assemble): verified Cam_02 base first; updated and approved V3 massing/layout guide as image 1b; actual EL2184 floor and frame/terrace/panorama references; exact retained product photos; selected V3 wallpaper/laminate/graphic samples explicitly labelled as materials only. Do not use the failed S01 render as the geometry or layout input. Do not change the camera to show W02 or the whole dining group.",
   "Inputs: exactly the attached images listed at the top – the verified Cam_02 base (image 1), the verified V3 massing guide (image 1b), the actual floor, wall/frame/terrace and panorama photos (images 2–2c) and the retained product photos. No material sample images are attached; follow the material descriptions in words. Do not use the failed S01 render as the geometry or layout input. Do not change the camera to show W02 or the whole dining group."),
  ('kimenet: V3_TEST mappa és név',
   "Output proposal: 04_renderek/ai_chatgpt/STYLE10_KEP004/CREATIVE_UPGRADE_V3/A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_r1.png (+ matching executed .prompt.txt). New destination only; do not overwrite any V2 or first-test image.",
   "Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_TEST.png (+ matching executed .prompt.txt). New destination only; do not overwrite any V2 or first-test image."),
  ('futtatási jegyzet: 1b tömbkép (KI3-P egy befoglaló)',
   "the Blender check found no collision with walls, openings or door swings and no covered switch.",
   "the Blender check found no collision with walls, openings or door swings and no covered switch. In image 1b the KI3-P field is drawn as one 260 × 190 cm envelope; how its two overlapping planes are divided follows the style block."),
 ],
 'S02': [
  ('stílusblokk-fejléc', "=== STYLE BLOCK – Astra Creative Upgrade V3 r1, verbatim except the 'Light' paragraph (test version, see its first words) ===",
   "=== STYLE BLOCK – Astra Creative Upgrade V3 r1, verbatim except the 'Light' paragraph (test version, see its first words) and the technical integration of the mirror, position, terrace-bench, inputs and output lines (Claude, 2026-10-25) ==="),
  ('geometria: a BN3-V két oszlopa a képen (tükör a TV-panel felőli oldalon)',
   "the asymmetrical tall cabinet BN3-V (90 × 220 cm: one door column and one fixed mirror column) stands at the far left and is cut by the left frame edge (about 0–18 % of the width, 23–84 % of the height);",
   "the asymmetrical tall cabinet BN3-V (90 × 220 cm) stands at the far left and is cut by the left frame edge (about 0–18 % of the width, 23–84 % of the height): its outer opening door column is at about 0–10 % of the width, its fixed mirror column, next to the TV wall panel, at about 10–17 % of the width and 25–71 % of the height, with a low closed service panel below the mirror;"),
  ('tükör: csak fizikailag lehetséges visszaverődés (Péter 02:22)',
   "Let the mirror reflect only real visible architecture and the actual exterior view.",
   "The mirror shows only what it can physically reflect from this camera position: the room behind and to the right of the camera – parts of the navy sofa, the beige dining chairs and the glass table edge, the white east wall, the ceiling and the edge of a light-grey interior door – in correct mirror perspective; never the exterior view, the skyline, a window or the camera."),
  ('BN3-V: melyik oszlop nyílik, melyik a fix tükörmező',
   "One 45 cm-wide storage column with vertically divided opening fronts, plus one 45 cm-wide fixed mirror/service field.",
   "One 45 cm-wide storage column with vertically divided opening fronts (the outer, left column in this view), plus one 45 cm-wide fixed mirror/service field (the column next to the TV wall panel, with a low closed service panel below the mirror)."),
  ('pozíciók: ellenőrizve (Blender v2b-1-k11b, validátor PASS)',
   "- Proposed positions, to be verified by Claude: tall cabinet y=4.25–5.15; low cabinet and background y=5.25–7.65 on the actual west wall.",
   "- Verified positions (Claude, 2026-10-25 – Blender v2b-1-k11b, validator PASS, shown in image 1b): tall cabinet y=4.25–5.15; low cabinet and background y=5.25–7.65 on the actual west wall."),
  ('kültéri pad: nincs ellenőrzött hely → nem jelenik meg; a karfatálca marad',
   "- Retain BN-O freestanding outdoor bench W150×H42×D60 cm on its approved existing gres location, aluminium/outdoor HPL with navy outdoor textile, and the W25×D35 cm removable arm tray. Do not add another central object or change the terrace.",
   "- BN-O outdoor bench (W150×H42×D60 cm, aluminium/outdoor HPL with navy outdoor textile): no verified position has been fixed yet, so it is not shown in this image. Keep the W25×D35 cm removable arm tray on the sofa arm. Do not add another central object or change the terrace."),
  ('bemenetek: a ténylegesen csatolt képek',
   "Inputs (Claude to assemble): verified Cam_02 base and updated, approved V3 massing/layout guide as image 1b; actual floor/frame/terrace/panorama photos; exact U, Anouk, Ciselia, Marely and updated Brisia reference photos; the selected V3 silver-grey wallpaper, navy front and mirror samples identified as materials only. Actual geometry overrides all mood references. No failed render as layout evidence and no camera shift to display additional walls.",
   "Inputs: exactly the attached images listed at the top – the verified Cam_02 base (image 1), the verified V3 massing guide (image 1b), the actual floor, wall/frame/terrace and panorama photos (images 2–2c) and the U, Anouk, Ciselia and Marely product photos. The Brisia pendant photo and material sample images are not attached (the pendant is outside this frame; samples are not selected yet). Actual geometry overrides all mood references. No failed render as layout evidence and no camera shift to display additional walls."),
  ('kimenet: V3_TEST mappa és név',
   "Output proposal: 04_renderek/ai_chatgpt/STYLE10_KEP004/CREATIVE_UPGRADE_V3/A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_r1.png (+ matching executed .prompt.txt). New destination only; no overwriting of earlier image packages.",
   "Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/V3_TEST/A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_TEST.png (+ matching executed .prompt.txt). New destination only; no overwriting of earlier image packages."),
  ('futtatási jegyzet: 1b tömbkép (tükörmező, szervizlap)',
   "the Blender check found no collision with walls, openings or door swings and no covered switch.",
   "the Blender check found no collision with walls, openings or door swings and no covered switch. In image 1b the lighter grey field in the tall cabinet is the fixed mirror column next to the TV wall panel, the darker outer column is the opening door column, and the low dark block under the mirror is a closed service panel."),
 ]}
TILTOTT = ['02:06', 'approved position', 'approved existing gres', 'Claude must verify', 'to be verified by Claude', 'Proposed, not yet validated',
           'Inputs (Claude to assemble)', 'Output proposal', 'CREATIVE_UPGRADE_V3/', '_V3_r1', 'KEP004-CGI-V3TEST-r1', 'architecture and the actual exterior view',
           'painted white, smooth', 'Retain the already specified', 'Retain BN-O', 'selected V3', 'keep the upper wall mostly empty']
KOTELEZO = {'S01': ['KEP004-CGI-V3TEST-r2', '02:22', 'image ID ' + ID['S01'] + '_V3_TEST', 'Creative Upgrade V3 surface exception', 'OWNER REQUIREMENT – lighting',
                    'No terrace furniture is shown', 'not shown in this image', 'Verified wall positions', 'V3_TEST/' + ID['S01'] + '_V3_TEST.png',
                    'Daylight – identical wording in both V3 test prompts'],
            'S02': ['KEP004-CGI-V3TEST-r2', '02:22', 'image ID ' + ID['S02'] + '_V3_TEST', 'Creative Upgrade V3 surface exception', 'OWNER REQUIREMENT – lighting',
                    'No terrace furniture is shown', 'not shown in this image', 'Verified positions', 'V3_TEST/' + ID['S02'] + '_V3_TEST.png',
                    'Daylight – identical wording in both V3 test prompts', 'what it can physically reflect', 'never the exterior view']}
jel = dict(r1={}, r2={}, csere={}, ellenorzes={})
for k in ('S01', 'S02'):
    t = open(R1[k], encoding='utf-8').read(); jel['r1'][k] = dict(fajl=os.path.basename(R1[k]), sha256=hashlib.sha256(t.encode()).hexdigest(), karakter=len(t))
    u = t.replace('image ID ' + ID[k] + '_V3_r1', 'image ID ' + ID[k] + '_V3_TEST', 1); assert t.count('image ID ' + ID[k] + '_V3_r1') == 1
    log = [('kép-ID', 'image ID ' + ID[k] + '_V3_r1', 'image ID ' + ID[k] + '_V3_TEST')]
    for nev, regi, uj in KOZOS + SAJAT[k]:
        n = u.count(regi)
        if n != 1: raise SystemExit(f'HIBA {k}: „{nev}” – a régi szöveg {n}× fordul elő')
        u = u.replace(regi, uj); log.append((nev, regi, uj))
    hib = [f for f in TILTOTT if f in u] + [f'HIÁNYZIK: {f}' for f in KOTELEZO[k] if f not in u]
    jel['csere'][k] = [dict(mi=a, regi=b, uj=c) for a, b, c in log]
    jel['ellenorzes'][k] = dict(hibak=hib, tiltott_lista=TILTOTT, kotelezo_lista=KOTELEZO[k])
    nev = ID[k] + '_V3_TEST.prompt.txt'; open(os.path.join(OUT, nev), 'w', encoding='utf-8').write(u)
    jel['r2'][k] = dict(fajl=nev, sha256=hashlib.sha256(u.encode()).hexdigest(), karakter=len(u))
    open(os.path.join(OUT, ID[k] + '_V3_TEST_r1_r2.diff'), 'w', encoding='utf-8').write(''.join(difflib.unified_diff(
        t.splitlines(True), u.splitlines(True), 'r1/' + os.path.basename(R1[k]), 'r2/' + nev)))
    print(k, 'r1', jel['r1'][k]['karakter'], '-> r2', len(u), 'cserék', len(log), 'hibák', hib)
json.dump(jel, open(os.path.join(OUT, 'epites_r2_naplo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

from pathlib import Path
import json,re,hashlib,shutil
P=Path(__file__).resolve().parents[1];O=P/'R07_render_trial';srcs={c:P/f'sources/A902_S01_KyotoInk_Cam_{c}__V33_C_v1.prompt.md' for c in ['02','12']}
def sections(text):
 result={}
 for p in text.split('\n\n'):
  m=re.match(r'([A-Z][A-Z0-9 –/-]+)\. ',p)
  if m:result[m.group(1)]=p
 return result
sources={c:sections(f.read_text())for c,f in srcs.items()};rows=json.loads((P/'R06/data/register_R06.json').read_text());rm={r[2]:r for r in rows[1:]}
unchanged=['STYLE DNA','CAMERA','DETAIL AND ACCESS','ART AND FURNITURE CONTINUITY']
common='''IMPLEMENTATION AUTHORITY. This is the KI-R06 full-content scheme, estimated24,482,890HUF, not an18M-approved procurement package. Use the R06 model for physical position, architecture, product envelopes and panel divisions. The original target supplies mood and composition only. Do not copy target-image geometry that contradicts the model. No object may be moved, mirrored, enlarged or reduced independently per view. Site measurements, physical finish samples, product meshes and lift mechanisms are not all approved. Do not call this a final construction render.

SELECTED PRODUCTS. KI-036: Westwing Lennon right-hand L, woven taupe, SKU DEQ21WES12329-168260,2380×1800×680mm. Use the actual2380mm back run,1800mm chaise projection,430mm seat height,320mm wide low arms and factory module arrangement. Lock the model's transform. Reference photographs govern upholstery seams and rounded form; do not render the former cuboid proxy or invent a more elegant slim-arm sofa. KI-028: Westwing Toni160, SKU DEQ19WES60483-225182,1600×900×750mm,25mm oval oak-veneer top and two curved panel supports; no single central solid pedestal. KI-029: six Kave Home Eamy C0100003HE12,550×530×750mm,460mm seat height, light-grey chenille, curved natural ash-veneer back, individual thin black metal legs. KI-109: Kave Home Somar L00148FA05,760mm diameter,360mm shade height, fibrous white shell over steel ribs; preserve its flatter actual profile rather than a generic inflated orb. These R06 meshes are dimension/photo reconstructions, not manufacturer-certified meshes; any visible mismatch stays in the audit rather than being declared exact.

MEDIA WALL IF VISIBLE. TV-01 is the700mm-wide graphite storage tower at the dining/south end,400mm deep,upper body2330mm high from z550mm. TV-03 has four650mm-wide,36mm-deep panels,from z550mm to2880mm. TV-02 is3300×400×400mm at z150mm,with five fronts700+650+650+650+650mm. Keep the dark tower distinct from the lighter greige screen field. Use INK-W01_R06 artwork mapped continuously across the different planes, with working joints, not a newly imagined brushstroke. It is a reference-based redraw proof and must be identified as such in the audit. The65inch TV has its own rear-wall mounting and a1452.9×834mm body; preserve actual screen position. Do not revert to the older3600mm wall/2400mm four-front low cabinet or720mm tower.

W02 IF VISIBLE. ART-02:2100×2880mm,36mm nominal carrier, two1050mm print fields, not the older three-panel interpretation. Use INK-W02_R06, unframed, with restrained woven-look surface. Preserve the real switch/thermostat/service strip and returns. Printing remains a print over a shallow physical substrate, not carved stone or thick relief. No new painting above the bedroom headboard is introduced through a reflected or adjoining view.

KITCHEN IF VISIBLE. Keep the R06 K-01…K-09 appliance towers, counters and front grid. Graphite matte lower fronts, warm chalk upper and tall fronts, graphite exposed fridge side. Worktop and matching backsplash use EGGER F243 ST76 Light Grey Candela Marble appearance; the countertop is38mm laminate, not thin natural marble. Show manufactured edges and a credible repeating decor. Nominal620mm counter depth must not be stretched. The closed working aisle is840mm; a600mm open dishwasher leaves240mm,so no through passage is claimed. Closed appliances for the hero image; opening clearances belong in separate controls. Do not copy the old F274 concrete finish, invent an island, move service points or widen the kitchen.

TEXTILE AND OBJECT LAYER. Preserve the approved taupe/graphite cushion and throw palette and restrained ceramic/books arrangement. CF-01 is a700×450×350mm matte graphite laminate coffee block; ST-01 is300×300×450mm. Do not replace them by premium natural stone or change dimensions to fill the image. Use the rug identified in the live register; do not reinterpret the wool-like surface as a different budget item. Keep the existing flooring, site-photo grain, skirting and window finish.

REAL LIGHTING. Preserve the view's original daylight or blue-hour photographic treatment below. Light may originate only in the R06 documented fittings/profiles: separate media-wall upper graze, tower-side reveal and lower wash where modelled and scheduled; kitchen under-cabinet task strip; actual Somar and ceiling fixture. Each source needs a real profile and accessible driver; do not illuminate every seam or add ceiling coves.2200–2700K white ambience is a mood target, not a photometric validation. Do not reinterpret wattage, add luminous surfaces or hide unresolved hardware through bloom.

TERRACE IF VISIBLE. Keep actual paving, brown WPC, levels, railings, planted roof and real panorama from the site references. Use only R06 visible objects at their modelled size. The jacuzzi envelope is2200×2200×900mm; its exact product/statics/services are unapproved. Other outdoor products remain provisional procurement envelopes and must be flagged as such. Do not borrow the older1600mm outdoor sofa description if the R06 object is2200mm, or add an outdoor ensemble merely because it appeared in the dream image. No invented city skyline.

REFERENCE AND QA CONTRACT. Image order is defined in the accompanying attachment list. The fresh native exact-camera control is the geometry authority; the dream image is appearance intent; site photos determine existing finishes, thresholds and panorama; real product photographs determine product form. Reference priority follows these roles, not whichever photograph looks best. Existing native meshes may be refined only within verified geometry and product-specific photos; any such refinement is not a proven exact match until checked. If architecture, silhouette, artwork placement, product variant, chair count or clearances change, stop and report the discrepancy. Do not use a polished image to conceal an unresolved design condition. Output one image without people or overlaid labels; write CONDITIONAL in the filename and separate audit, not into the image.
'''
for c in ['02','12']:
 v='V01'if c=='02'else'V02';s=sources[c]
 mood=('Blue hour / early evening,2200–2700K white ambience. Keep a readable blue exterior, natural warm/cool separation, restrained mid-key exposure, readable dark-front texture and controlled highlights. The terrace paving, glazing and railing remain legible.'if c=='02'else'Bright soft natural daylight, directionally credible window illumination, neutral-warm material colour. Hue ambience is off or barely perceptible. Do not turn this daylight comparison into an orange evening image.')
 text=f'''KYOTO INK — {v} / Cam_{c} — KI-R06 IMPLEMENTATION COMPARISON
Create an editorial-quality, photorealistic interior photograph of apartment A-902. Build a tactile, convincingly inhabited interior with honest materials and precise working joints. Render the selected implementation, not an aspirational upgraded substitute.

'''+s['STYLE DNA']+'\n\n'+s['CAMERA']+'\n\nLIGHT AND PHOTOGRAPHY. '+mood+' Premium editorial interior photography, realistic PBR-like surfaces, soft shadow gradients, delicate textile microtexture, balanced exposure, true depth and realistic furniture detailing.\n\n'+common+'\n'+s['DETAIL AND ACCESS']+'\n\n'+s['ART AND FURNITURE CONTINUITY']+f'\n\nOUTPUT. A902_{v}_KI-R06_IMPLEMENTATION_COMPARE_CONDITIONAL.png. Preserve the native control aspect ratio. Use the same image-generation engine/version/settings for repeat trials when available. Original dream-image model/version/seed are not proven; do not promise identical stochastic rendering or pixel-perfect comparisons. Do not proceed to additional views until this pilot is reviewed.\n'
 (O/'prompts'/f'{v}_Cam_{c}_IMPLEMENTATION_EN.txt').write_text(text)
 shutil.copy2(srcs[c],O/'references'/srcs[c].name)
# Site photos copied without editing; all seven dream targets remain in the complete R06 delivery.
photo_root=P.parent/'a902-terasz-p0-20261027/sources/08_allapotfelmeres/fotok_profi_20261025/A902'
for n in ['KZS_3659-573.jpg','KZS_3695-537.jpg','KZS_3726-506.jpg','KZS_3488-744.jpg','KZS_3708-524.jpg']:
 if(photo_root/n).exists():shutil.copy2(photo_root/n,O/'references'/n)
for source,dest in [('targets/T01_W01_nappali.png','02_DREAM_T01.png'),('targets/T02_W02_etkezo.png','DREAM_T02.png'),('products/lennon_1.jpg','07_LENNON_exact_variant.jpg'),('products/toni_1.jpg','08_TONI160_exact_variant.jpg'),('products/eamy_1.jpg','09_EAMY_exact_variant.jpg'),('products/somar_1.jpg','10_SOMAR_exact_variant.jpg'),('blender/W01_R06_colour_proof.png','11_MEDIAWALL_R06_PROOF.png')]:shutil.copy2(P/'R06'/source,O/'references'/dest)
(O/'01_CSATOLMANY_SORREND.txt').write_text('''V01 / Cam_02 első próba — képenként külön csatold:
1. controls/V01_R06_native_camera_control.png — tényleges geometria és kamera; semleges világítású műszaki kontroll.
2. references/02_DREAM_T01.png — álomkép, csak megjelenés és esti hangulat.
3. references/KZS_3659-573.jpg — valós nappali és üvegezés.
4. references/KZS_3695-537.jpg — eredeti padló és konyhacsatlakozás.
5. references/KZS_3726-506.jpg — küszöb, üvegezés és szintváltás.
6. references/KZS_3488-744.jpg — teraszburkolat és WPC.
7–10. LENNON,TONI160,EAMY,SOMAR termékfotók — pontos változatok, csak a látható részletekre.
11. references/11_MEDIAWALL_R06_PROOF.png — tényleges R06 panelosztás és grafikai próba, nem hangulatminta.
Szöveg: prompts/V01_Cam_02_IMPLEMENTATION_EN.txt.
Egyetlen képet készíts. A csomag nem tartalmaz elkészült fotorealisztikus generált próbát.
V02 prompt szintén elkészült, de a V02 friss R06 kamerakontrollja még szükséges; a V01 kép nem helyettesíti!
''')
(O/'00_ITT_KEZDD.txt').write_text('''KI-R07 renderpróba-átadás / R06 megvalósításból
Megtalált eredeti teljes promptok: Cam_02 és Cam_12 V3.3. Korábbi ellenőrzési nyugta szerinti forráscommit:4d2b7e857f034a7080bd62bd249e84a0a8e310e3. A legutóbbi hét álomkép pontos modellje/seedje/generálási promptja nem mindenhol bizonyított. V02VisualRescue szöveg is elérhető; az abban lévő régi hárompaneles W02 és CP3 adatok nem irányadók.
Megmarad: STYLE DNA, nézet/camera szövege, editorial fotós stílus, Cam_02esti/Cam_12nappali fényhangulat, valós építészeti és fotóreferencia-szabályok. Változik: konkrét R06 termékforma, méret, médiafal,2mezős W02, F243munkalap, grafikai fájlok, valódi kültéri állapot és nyitott feltételek.
Első lépés: olvasd a műszaki kontroll ellenőrzését; csak megfelelő kontrollból indíts1képes fotorealisztikus próbát. Használd az01csatolmányjegyzéket és a V01angol promptot. A kép után írásban hasonlítsd össze a termékformát, méretet, kamerát, grafikát és anyagot. Eltérés esetén ne folytasd a sorozatot.
Második lépés: elfogadott próba után a többi nézet eredeti promptját ugyanígy kell aktualizálni és hozzá új kamerakontrollt készíteni. A meglévő R06jegyzék28látvány+21funkcionális nézetet tervez; ezek nem49kész kép és nem mindegyikhez igazolt az eredeti kreatív prompt.
Álom vs megvalósítás: a képi kamera akkor egyezik pixelpontosan, ha az eredeti kép is valóban megtartotta a kamerát. Amennyiben az álomrender geometriát módosított, a különbséget jelölni kell; nem szabad a valós modell eltorzításával eltüntetni.
A csomag feltételes. Nincs18Mkeretigazolás, mindenhol felmért méret, gyári3Dazonosság vagy jóváhagyott anyagminta. Nincs automatikus tömeges képgenerálás.
''')
audit={'source_commit_from_prior_receipt':'4d2b7e857f034a7080bd62bd249e84a0a8e310e3','technical_preservation':{},'model_version_seed_of_dream_images':'UNKNOWN','generated_photoreal_trial':False}
for c in ['02','12']:
 v='V01'if c=='02'else'V02';new=(O/'prompts'/f'{v}_Cam_{c}_IMPLEMENTATION_EN.txt').read_text();audit['technical_preservation'][c]={k:sources[c][k]in new for k in unchanged};assert all(audit['technical_preservation'][c].values())
(O/'audit/source_comparison.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print('2 source-based full prompts; reference package; preservation audit created')

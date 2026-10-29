from pathlib import Path
import json,shutil,hashlib
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok'
for src,dst in [('/tmp/TV_R16_teljes_zart_v3.dwg','rajzok/TV_R16_teljes_zart.dwg'),('/tmp/TV_R16_fiokok_nyitva_v3.dwg','rajzok/TV_R16_fiokok_nyitva.dwg'),('/tmp/ki16verify01.log','audit/autocad_saved_readback.log'),('/tmp/ki16views03.log','audit/autocad_final_assembly.log'),('/tmp/ki16_blender.log','audit/blender_run.log')]:shutil.copy2(src,O/dst)
(O/'00_OLVASD_EL.txt').write_text('''KYOTO INK / MÉDIAFAL / R16 / 2026.10.29.

Ez a tulajdonosi pontosításokat átvezető új csomag. Az alsó sorra a régiR15 ajtós rajzok nem érvényesek.
Nyisd meg először: rajzok/TV_R16_asztalos_tervcsomag.pdf.
AutoCAD: rajzok/TV_R16_teljes_zart.dwg; külön kihúzott állapot: TV_R16_fiokok_nyitva.dwg.

RÖGZÍTETT TARTALOM
- Hat eltérő szélességű alsó front; mind egyetlen magas fiók. A középen látható vízszintes osztás a tulajdonosi válasz alapján elmarad.
- Névleges modulok:720+450+450+1080+450+450=3600mm. Ez képi arányértelmezés az eddigi3600/720mm tervkereten belül, nem felmért adat.
- A magas torony két ajtós marad. Külső látszó oldala és felső éle is az alsó fronttal egyező bronzbarna mintát kap; a korpusz belseje M03.
- A torony és a tapétázott merev panelmező között200mm valódi matt bronzbarna betétsáv van. A szekrény oldalán rejtett,45fokos LEDprofil világít rá. Nem üres hézag.
- Blum MOVENTO300 +TIPONBLUMOTION; hat fiók és két ajtó külön nyitásérzékelős belső világítása.
- Tusgrafika: a látható vonások technikai vektoros visszavetítése. Hat darabra osztva, közös koordinátával,10mm kifutóval. A takart részek eredeti motívumát nem találtuk ki.

MI KÉSZ?
106 lapalkatrész,956 szerkezeti furat,14 hátlapkivágás; valódi AutoCAD-testek és DWG-visszaolvasás; Blenderben a CAD-méretek ellenőrizve; PDF-alkatrészlapok; DXF-ek; revíziós címkék és kereső; Excel; grafikai állományok.

MI NINCS JÓVÁHAGYVA?
A MOVENTO kapocs/kampó/stabilizátor gyári sablonfuratai és alákivágása még külön műhelyi feladat. Nincs teljesen kiadott megmunkálási program. Az aktív MPR-tervezetek csak a megadott szerkezeti furatokat tartalmazzák. Nincs woodWOP5- vagy gépi próba.
Felmérés, szerelési hézagok, falhorgonyok, matt bronz/nyomatminta, ragasztó és lakk kompatibilitás, villamos/hő/szenzorpróba szükséges.
A jelenlegi dohányzóasztalhely akadályozza a középső fiókot.200mm eltolással a névleges frontütközés megszűnik; a37mm hézag nem közlekedő. Az eltolás és használhatósága külön döntés/próba.

KÖLTSÉG
Az élő projekt-Excel öt érintett csomagsora frissítve: KI030,031,032,034,114. Teljes előirányzat26 212 190Ft, becslés. A18Mkerethez képest+8 212 190Ft; a2Mtartalék külön maradt. R15feltételes előrejelzéshez képest+1 051 000Ft. Az eredeti Excel a sources mappában archiválva.
A műhelyi Excel nem második lakásköltségvetés: azR16médiafal részletezése és az élő főösszeg egyeztetése.

A nyomdai PDF1:1próbafájl. Nyomtatáskor100%,nem oldalhoz igazítás. Az SVG/DXF a szerkeszthető grafika. VéglegesICCprofil és anyagszín még nincs jóváhagyva.
A 3D előnézet műszaki színjelölés, nem végleges fotórealisztikus lakásrender vagy anyagminta.
Nincs rendelés, kivitelező-foglalás vagy gépi végrehajtás.
''')
(O/'render_atadas_R16.txt').write_text('''KYOTO INK / R16 MEDIA WALL — CONTENT OVERRIDE FOR THE EXISTING CAMERA-LOCKED RENDER WORKFLOW

Use the approved apartment geometry and the existing camera source. Do not infer room dimensions from the dream reference, and do not use the orthographic engineering preview as a substitute for the room camera.

Authoritative geometry: rajzok/TV_R16_koordinacio.blend and TV_R16_teljes_zart.dwg. The woodworking register uses the exact same part IDs. The Blender hardware meshes are clearance envelopes, not manufacturer product models.

Media wall width3600mm, height2880mm nominal. Left tall unit720mm. Separate200mm matte bronze-brown infill panel on18mm substrate. Four upper modules670mm nominal each, with667mm physical panels. Do not erase the bronze panel or replace it with a black void. Recessed45-degree LED profile mounted on the right side of the tall unit grazes the bronze surface;24V,2700K,2300mm active strip.

Lower sequence left-to-right:720,450,450,1080,450,450mm. SIX single high drawer fronts; no horizontal drawer split. Use the physical front widths717,447,447,1077,447,447mm, all397mm high. The tall unit remains two hinged doors. Match the visible cabinet side and top finish to the matte bronze-brown front sample.

Surface candidates: matte bronze-brown finish matching the physical sample, not polished metal; Vescom Bely+Print1040.01 linen-effect printable wallcovering on rigid18mm panels, without invented upholstery depth or relief. Use artwork/INK_W01_R16_MASTER_3600.svg with its fixed coordinates and per-panel crops. Do not redraw, beautify, rotate or replace the brushstroke. There is no artwork on the200mm bronze band. Hidden original brushwork is unknown; do not claim exact recovery behind the TV.

Use the same TV selected in the register: Samsung QE65Q7FAAUXXH,1452.9x60.6x834mm nominal. Do not scale the television or the cabinet to improve composition. Keep furnishings, curtains, ceiling light and decor from the existing approved room specification. R16 does not authorise changes elsewhere in the apartment.

The coffee table at its previous position collides with a fully extended central drawer. A200mm move away from the wall is a documented proposal, not an approved final layout. Show the conflict in a technical open-drawer view; any proposed shifted-table room image must be labelled conditional in its accompanying audit.

Internal lighting is fixed to the carcass and activated independently by each of six drawers and two tower doors. Closed fronts do not leak fictional internal light. Ambient strips are separate dimmable circuits. Do not fake light sources without a physical profile.

First make one technical test image. Compare camera, module widths,200mm band, brushstroke registration, all front seams and actual product identity against the CAD and reference. Save the prompt, source filenames, revision, output and audit. Stop if a product changes shape or geometry moves. A conditional design render is allowed; a final manufacture-validated image is not yet supported by the pending survey, material samples and hardware template tests.
''')
manifest={'revision':'R16','scope':'media wall only','authoritative_drawings':['rajzok/TV_R16_teljes_zart.dwg','rajzok/TV_R16_fiokok_nyitva.dwg'],'blend':'rajzok/TV_R16_koordinacio.blend','source_image':'sources/T16_mediafal_tulajdonosi_celkep.png','source_sha256':hashlib.sha256((O/'sources/T16_mediafal_tulajdonosi_celkep.png').read_bytes()).hexdigest(),'owner_decisions':['lower drawers; tall unit doors','every lower front one high drawer, no horizontal split','bronze-brown material band about200mm, lit from cabinet side'],'cost_items':['KI-030','KI-031','KI-032','KI-034','KI-114'],'art':'artwork/INK_W01_R16_MASTER_3600.svg','render_status':'CONDITIONAL_DESIGN_NOT_MANUFACTURING_APPROVED'}
(O/'data/handoff_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
for n in ['README.md','02_FOLYTATAS_ATADAS.md']:
 f=P/n;s=f.read_text();lead='## R16 – médiafal: bronzbetét, tusgrafika és magas fiókok (2026-10-29)\n\nAktuális médiafalcsomag: `R16_feluletek_fiokok/00_OLVASD_EL.txt`. Hat magas fiók, ajtós torony,200mm matt bronzbarna betétsáv oldalsó LED-del,8nyitásérzékelős belső fény. R16felváltja azR15alsó ajtós kiosztását. Az élő Excel öt érintett sora frissítve; becsült főösszeg26 212 190Ft. R16CAD/PDF/Blender/grafika/címke/MPR-tervezet ténylegesen átadva. Felmérés, gyári vasalati sablonművelet, anyag/nyomatminta, gépi és szakági próba nyitott. Asztal200mm eltolás: külön javaslat.\n\n'
 if not s.startswith('## R16'):f.write_text(lead+s)
print('handoff ready')

from pathlib import Path
import json, math, hashlib, csv, shutil, sys
sys.path.insert(0,'/private/tmp/s16-python')
import ezdxf
from PIL import Image
import openpyxl

O=Path(__file__).resolve().parents[1]; P=O.parent; ROOT=P.parents[1]
S=ROOT/'execution/a902-s01-kyoto-ink-20261026/R16_feluletek_fiokok'
REV='S16-R05'; DATE='2026-10-29'
def save(name,obj): (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
im=Image.open(P/'sources/S16_Cam02_C_celkep.png').convert('RGB')
assert im.size==(1586,992)
assert hashlib.sha256(im.tobytes()).hexdigest()=='2697b795cec9ef7cebbe27d55ecc2ae3f380c274a8d34f3ac537484294339cd5'
master=ROOT/'execution/a902-s01-kyoto-ink-20261026/outputs/A902_Kyoto_Ink_elo_regiszter.xlsx'
w=openpyxl.load_workbook(master,data_only=True)
ids=['KI-030','KI-031','KI-032','KI-034','KI-114']; ki=[]
for row in w['Elemregiszter'].values:
 if row[2] in ids:ki.append(dict(id=row[2],name=row[7],base=row[20],low=row[-2],high=row[-1]))
assert sum(r['base'] for r in ki)==2969300
assert w['Összesítő']['B7'].value==26212190
save('audit/baseline.json',{'remote_head':'88de4b7786dc86dc44e34435c2f94bfd12b53d4e','image_pixel_sha256':hashlib.sha256(im.tobytes()).hexdigest(),'image_file_sha256':sha(P/'sources/S16_Cam02_C_celkep.png'),'prompt_sha256':sha(P/'sources/S16_Cam02_C_eredeti_prompt.txt'),'S01':ki,'master_total':26212190,'protected_files':{str(p):sha(p) for p in [master]+list((S/'data').glob('*.json'))},'stale_source_note':'A régi CP1a és CP3 füleken 3300 mm / 5 front / korábbi árak is szerepelnek. Az Elemregiszter aktuális öt sora és az R16 adatmodell az alap.'})

layout={'revision':REV,'date':DATE,'status':'TERVEZÉSI JAVASLAT - FELMÉRÉS ÉS MŰHELYI JÓVÁHAGYÁS ELŐTT','width':3600,'height':2875,'depth':400,'ceiling_nominal':2900,'origin':'Bal alsó falsarok a kész padlón. X jobbra, Y faltól a szoba felé, Z felfelé; mm. Nem a S01 Y-tengelye.','source':'Szélesség: tulajdonosi 3600 mm döntés. Magasság: prompt és v2b modell; helyi minimum még felmérendő. Többi méret R05 tervezési javaslat.','tower_width':870,'base_z':150,'base_top':570,'tower_base':570,'module_widths':[435,425,425,1030,425,425],'screen_box':[1473.55,151,1033,1452.9,60.6,834],'screen_note':'S01 összehasonlító 65 colos QE65Q7FAAUXXH névleges készüléktest; külön meglévő TV-tétel, nem az S16 bútorár része. TV/VESA/feloldó hozzáférés nincs helyszínen igazolva.','relief':{'background_face_y':78,'TV_face_y':113,'difference':35},'tower_doors':'2 db oldalra nyíló; bal ajtó textilbetétje és peremfénye együtt mozog. 6 fiók TIP-ON BLUMOTION; ajtók rugó nélküli pánt+TIP-ON, nem csillapítottak.','room_mapping':'v2b Fal_05_1_nappali_0 keleti falsík x=3.67 m, y=4.05..8.05. Javasolt bútor: világ X=3.67+helyiY/1000, világ Y=4.25+helyiX/1000. Két oldalon 200 mm névleges maradék. Helyszíni szegőléc/függöny/kiállás nincs igazolva.'}
save('data/layout.json',layout)
layout['screen_box']=[1436.25,151,968.8,1677.5,61.1,962.4]
layout['screen_note']='Tulajdonosi kérésre65 helyett75col. Méretreferencia: Samsung QE75Q7FAAUXXH,1677,5×962,4×61,1mm talp nélkül;25,3kg;VESA400×400. Gyári HU oldal ellenőrizve2026-10-29. A konkrét modell beszerzése nincs jóváhagyva.'
layout['owner_latest']='R05 tulajdonosi kérés:870mm torony, jobboldal arányosan szűkebb;75col TV; teljes kompozíció2875mm,25mm mennyezeti fényrés; torony jobb alul szögletesen folytatódik a fióksorba; külső halo és a világos betét teljes peremfénye.'
save('data/layout.json',layout)
save('data/tv75.json',{'size_inch':75,'model_reference':'Samsung QE75Q7FAAUXXH','dimensions_mm':[1677.5,962.4,61.1],'mass_kg':25.3,'VESA_mm':[400,400],'source':'https://www.samsung.com/hu/tvs/qled-tv/q7f-75-inch-qled-4k-smart-tv-qe75q7faauxxh/','mount_source':'https://brandportal.vogels.com/m/76109be3bb82e160/original/3836050_TVM3600Series_Leaflet_Document_EN.pdf','mount_nominal_compatible':True,'mount_limit_kg':75,'mount_size_range_inch':[40,100],'mount_VESA_max_mm':[600,400],'old_KI033_estimate':250000,'new_estimate':350000,'low':300000,'high':450000,'delta_estimate':100000,'price_status':'Bruttó tervezői keret, nem webshopár. A gyári oldalon nem eladó státusz; tényleges beszerzési modell és ajánlat később.','geometry_clearance_mm':{'above_TV_to_panel':218.8,'below_TV_to_deck':398.8,'right_to_panel':386.25,'left_to_straight_panel_edge':256.25},'gate':'VESA valós magassági offset, távtartó/csavar, kábelhajlítás, hűtés és falterhelés még ellenőrizendő.'})
materials=[
 ['M01','18 mm kétoldalt melaminos grafitszürke bútorlap','Korpusz és polc; gyártó/kód műhelyi egyeztetésre. ABS 1 mm a látszó élen.','Közös S01 funkcionális tartalom','#656863'],
 ['M02','18 mm MDF + kétoldali lezárás + szatén 2K PU grafit','R35 fix keretek; NCS S 7500-N induló színminta, 10–15 GU/60° cél. Nem Monza autófesték-rendelési kód.','Minta nappal és 2700 K fényben','#3e4344'],
 ['M03','EGGER H3198 ST19 Dark Grey Fineline dekorjelölt','18 mm hordozón gyári dekor vagy kiegyenlített HPL-rétegrend; összvastagság kész 18 mm céltól eltérés esetén méretfrissítés. Erezet vízszintes fronton, függőleges TV-mezőn.','Gyári dekorazonosság ellenőrizve, HU készlet/ár és minta nyitott','#4c4e49'],
 ['M04','18 mm MDF + finomszövésű szürke falburkolat','Háttér: textilhatású, nem kő és nem vastag kárpit. Vescom Bely+Print hordozócsalád jelölt; egyedi neutrális szürke próba, grafika nélkül. Ragasztó/hátoldali kiegyenlítés gyártói egyeztetéssel.','Végleges szín/SKU nincs kiválasztva','#8c8a80'],
 ['M05','6 mm hordozó + vékony valódi elefántcsont szövet','360×2515 mm cserélhető ajtóbetét, R25; kész vastagság 8 mm cél. Csak vékony fátyol, nincs vastag hab. Szín: NCS S 1502-Y közeli mintacél.','Kárpitos szövet/ragasztó és ajtótömeg-próba kell','#d0c9b8'],
 ['M06','8×2 mm szatén ezüstszürke alumínium díszcsík','Fix torony felső és jobb éle mentén egyetlen L gesztus; R35 sarok előformázva vagy szegmensként illesztve. Rejtett rugalmas rögzítés, dilatáció.','Nem teljes fémkeret és nem fényes króm','#a3a9aa'],
 ['M07','15 mm nyír rétegelt lemez, matt vízbázisú lakk','Fiókdobozok; csiszolt élek, kész vastagság mérendő. Fenék 15 mm, oldalak 15 mm.','Blum max.16 mm oldalfal alatt','#c4af8b'],
 ['M08','8 mm grafit hátlap','Korpuszhátak, bontható szervizajtók; élek zárva.','Tervi anyag','#696c67']]
materials[1][2]='R100 torony/R80 alsó fix keret és18mm rétegvastagságú laminált sarokhéj; NCS S7500-N induló színminta,10–15GU/60° cél. Nem autófesték-kód. Íves héj rétegrendje műhelyi mintával.'
materials[4][2]='6mm hordozó +vékony valódi szövet;360×2515mm bontható ajtóbetét,R60; kész8mm céltól eltérés a geometriát módosítja.'
materials[5][2]='8×2mm szatén alumínium, rövid L a fix torony felső jobb sarkán. R90 külső/R82 belső sarok, gyári hajlítás vagy külön előformázott elem.'
materials=[m for m in materials if m[0]!='M06']
save('data/materials.json',materials)

parts=[]
def part(id,name,box,mat,cost,kind='plate',axis=None,outline=None,holes=None,grain='nincs',note=''):
 dx,dy,dz=box[3:]
 axis=axis or ('y' if dy<=min(dx,dz) else 'x' if dx<=min(dy,dz) else 'z')
 uv={'x':(dy,dz,dx),'y':(dx,dz,dy),'z':(dx,dy,dz)}[axis]
 p={'id':id,'revision':REV,'name':name,'box':box,'axis':axis,'L':uv[0],'W':uv[1],'T':uv[2],'material':mat,'cost':cost,'kind':kind,'grain':grain,'outline':outline,'cutouts':holes or [],'note':note,'status':'Tervi készméret; nem gyártási kiadás','raw_L':None,'raw_W':None,'raw_rule':'MDF keret/front: előirányzat +10/+10 mm marási ráhagyás. Melamin: élzárás után értelmezett készméret; nyers méret műhelyi élrendszer után.','edge':'E1 V=0, E2 U=max, E3 V=max, E4 U=0. M01: elülső él ABS1, többi takart; M02/M03 festett/egyező dekorél. Végleges élkiosztás műhelyi ellenőrzésre.','datum':'Helyi U,V a főlap síkjában; (0,0) bal alsó. A oldal +normál. Gépi ütköző/befogás nincs kiadva.','operations':'Kontúr és kivágás geometria. Vasalatfuratok külön gyári sablon szerint; nincs kitalált CNC-kód.','drawing':'S16_R05_tervcsomag.pdf / alkatrészlap '+id,'model':id}
 parts.append(p);return p
def rr(x,z,w,h,r):
 pts=[]
 for cx,cz,start in [(x+w-r,z+r,-90),(x+w-r,z+h-r,0),(x+r,z+h-r,90),(x+r,z+r,180)]:
  for i in range(33):
   a=math.radians(start+i*90/32);pts.append([cx+r*math.cos(a),cz+r*math.sin(a)])
 return pts

drawers=[];x=435
for i,width in enumerate(layout['module_widths'],1):
 top=570
 for hand,xx in [('L',x),('R',x+width-18)]:part(f'D{i}-{hand}',f'D{i} korpuszoldal',[xx,40,150,18,337,top-150],'M01','C01')
 for a,zz in [('B',150),('T',top-18)]:part(f'D{i}-{a}',f'D{i} fenék/tető',[x+18,40,zz,width-36,337,18],'M01','C01')
 part(f'D{i}-BACK',f'D{i} bontható hát',[x+18,40,168,width-36,8,top-186],'M08','C01')
 fx=x+1.5;fw=width-3
 if i==1:fx=x+1.5;fw=width-3
 if i==6:fw=width-22.5
 fz=171;fh=549-fz
 part(f'D{i}-FRONT',f'D{i} egy magas front',[fx,382,fz,fw,18,fh],'M03','C01',grain='U vízszintes',note='Névleges 3 mm frontköz; minimum benyomási út 2,5 mm. Korpusz elé 5 mm tervezett rés.')
 lw=width-36;skw=lw-42;sx=x+24
 for hand,xx in [('L',sx),('R',sx+skw+15)]:part(f'D{i}-BOX-{hand}',f'D{i} fiókoldal',[xx,80,210,15,290,237],'M07','C04')
 for a,yy in [('F',355),('R',80)]:part(f'D{i}-BOX-{a}',f'D{i} dobozelő/hát',[sx+15,yy,225,skw,15,222],'M07','C04')
 part(f'D{i}-BOX-B',f'D{i} fiókfenék',[sx+15,80,210,skw,290,15],'M07','C04')
 drawers.append({'id':f'D{i}','x':x,'width':width,'LW':lw,'SKW':skw,'NL':300,'inside':[skw,260,222],'litres':skw*260*222/1e6,'runner':'760H3000S pár + T51.7601 pár','tipon':'T60L7140 S1' if i in [1,4] else 'T60L7040 S0','sync':'T60.1125W + 2×T60.000D','sync_cut':lw-267,'stabilizer':'ZS7M400MU, pontos változat és helyigény ellenőrzendő','front':f'D{i}-FRONT','moving':[f'D{i}-FRONT']+[f'D{i}-BOX-{h}' for h in ['L','R','F','R','B']],'stroke':300,'weight_note':'S0 ≤10 kg / S1 >10–20 kg össztömeg a gyári működési tartomány; a sín 40 kg-ja nem írja felül. Üres/teli tömegpróba szükséges.'})
 x+=width
# Rename back to avoid same ID as right side.
for i in range(1,7):
 seen=False
 for p in parts:
  if p['id']==f'D{i}-BOX-R':
   if seen:p['id']=f'D{i}-BOX-H';p['model']=p['id'];p['drawing']='S16_R05_tervcsomag.pdf / alkatrészlap '+p['id']
   seen=True
 drawers[i-1]['moving']=[f'D{i}-FRONT']+[f'D{i}-BOX-{h}' for h in ['L','R','F','H','B']]
save('data/drawers.json',drawers)

for hand,xx in [('L',0),('R',852)]:part('T-'+hand,'Torony oldallap',[xx,40,570,18,337,2305],'M01','U03')
for n,zz in [('B',570),('T',2857)]:part('T-'+n,'Torony fenék/tető',[18,40,zz,834,337,18],'M01','U03')
part('T-C','Torony középosztó',[426,40,588,18,337,2269],'M01','U03')
for col,xx in [('L',19),('R',445)]:
 for i,zz in enumerate([935,1320,1705,2090,2475],1):part(f'T-{col}-S{i}','Állítható polc',[xx,50,zz,406,290,18],'M01','U03',note='1 mm oldalhézag; hasznos polcméret 406×290. Elülső35mm szabad sáv a fényprofilnak. Terhelést műhely igazolja.')
 part(f'T-{col}-BACK','Bontható felső hát',[xx,40,935,406,8,1921],'M08','U03')
 part(f'T-{col}-SERVICE','Bontható alsó szervizfedél',[xx,127,589,406,8,345],'M08','U03',note='Előlről csavarozva kiemelhető; alsó rekeszben 240 mm tárolási mélység.')
for hand,xx in [('L',21),('R',436.5)]:part('T-DOOR-'+hand,'Torony ajtó',[xx,382,573,412.5,18,2281],'M03','U04',grain='V függőleges',note='Rugó nélküli inset CLIP top + mágneses TIP-ON. Bal6/jobb5 pánt előirányzat, tömeg és ráütés alapján véglegesítendő; csillapítás nincs.')
part('TEXTILE','Elefántcsont szövetbetét',[47,400,255,360,8,2515],'M05','U07','rounded',outline=rr(0,0,360,2515,25),note='Bal ajtóval mozog, hátról bontható rögzítés. 24V hajlításálló pántoldali átvezetés.')
# Fixed shells split into manageable pieces along real straight joints.
part('FRAME-T-L','Torony fix bal keretléc',[0,382,185,18,18,2660],'M02','U05')
part('FRAME-T-R','Torony fix jobb keretléc',[702,382,185,18,18,2660],'M02','U05')
for n,zz,flip in [('TOP',2845,False),('BOT',150,True)]:
 poly=rr(0,0,720,70,35)
 poly=[q for q in poly if (q[1]<=35.000001 if flip else q[1]>=34.999999)]
 poly=[[q[0],q[1] if flip else q[1]-35] for q in poly]
 part('FRAME-T-'+n,'Torony R35 keretzárás',[0,382,zz,720,18,35],'M02','U05','profile',outline=poly,note='Egyenes köztes keretléchez kötött íves MDF elem; valódi R35 kontúr a DXF-ben.')
part('FRAME-T-MID','Torony alsó fiók feletti fix osztó',[436.5,382,552,433.5,18,18],'M02','U05')
for n,zz in [('LOW',150),('HIGH',550)]:
 for j,(xx,ww) in enumerate([(720,900),(1620,1080),(2700,865)],1):part(f'FRAME-B-{n}-{j}','Alsó fix vízszintes keret',[xx,382,zz,ww,18,18],'M02','U05')
part('FRAME-B-R','Alsó jobb keret',[3582,382,185,18,18,350],'M02','U05')
for n,zz,ang in [('BOT',150,0),('TOP',535,90)]:
 # Correct 35×35 quarter corner sectors; outer arc and inner returns.
 if n=='BOT': poly=[[0,0]]+[[35*math.cos(math.radians(a)),35+35*math.sin(math.radians(a))] for a in range(-90,1,5)]+[[17,35],[17,20],[0,20]]
 else:poly=[[0,35]]+[[35*math.cos(math.radians(a)),35*math.sin(math.radians(a))] for a in range(90,-1,-5)]+[[17,0],[17,15],[0,15]]
 part('FRAME-B-'+n,'Alsó jobb R35 sarokelem',[3565,382,zz,35,18,35],'M02','U05','profile',outline=poly)
for i in range(4):
 xx=870+i*682.5
 part(f'BG-{i+1}','Bontható szürke háttérpanel',[xx+(3 if i==0 else 1.5),60,570,678 if i in [0,3] else 679.5,18,2305],'M04','U01',grain='V függőleges',note='3 mm valós függőleges hézag. 20 mm felfelé emelést nem igénylő előre oldható kapocs. Panelt TV levétele után lehet bontani.')
# TV plane split at a seam behind TV, preserving rounded outer silhouette.
outer=rr(0,0,2400,1300,35)
left=[[min(q[0],1200),q[1]] for q in outer if q[0]<=1200]+[[1200,0],[1200,1300]]
# Use simple clipped polygons in order, clipping rectangle with polygon.
def clip(poly,bound,keep_left):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  ina=(a[0]<=bound) if keep_left else (a[0]>=bound);inb=(b[0]<=bound) if keep_left else (b[0]>=bound)
  if ina:out.append(a)
  if ina!=inb:
   t=(bound-a[0])/(b[0]-a[0]);out.append([bound,a[1]+t*(b[1]-a[1])])
 return out
for n,x0,bound,keep in [('L',1000,1198.5,True),('R',2201.5,1201.5,False)]:
 poly=clip(outer,bound,keep);poly=[[q[0]-(0 if keep else 1201.5),q[1]] for q in poly]
 part('TV-'+n,'TV mögötti kiemelt mező',[x0,95,800,1198.5,18,1300],'M03','U06','profile',outline=poly,grain='V függőleges',note='35 mm kiemelés a háttérhez képest. Konzol/kábel átvezetés helye TV/VESA szerint külön sablonozandó.')
for i,xx in enumerate([910,1540,2220,2900,3530],1):part(f'BATTEN-{i}','Háttér falsín',[xx,0,590,40,40,2235],'M01','F02',note='Falméret és horgony méretezés után rögzíthető. 20 mm előrefelé oldható kapocstér y40..60.')
for i,zz in enumerate([835,2030],1):part('TV-SPACER-'+str(i),'TV mező távtartó',[1040,78,zz,2320,17,35],'M02','U06',note='17 mm távtartó +18 mm panel =35 mm relief; rejtett csavarok/oldható kapcsok.')
# Silver accent kept separate from warm light route.
part('SILVER-V','8 mm ezüst függőleges részlet',[690,400,2180,8,2,625],'M06','U08')
part('SILVER-H','8 mm ezüst felső részlet',[410,400,2832,253,2,8],'M06','U08')
arc=[]
for a in range(0,91,5):arc.append([35*math.cos(math.radians(a)),35*math.sin(math.radians(a))])
for a in range(90,-1,-5):arc.append([27*math.cos(math.radians(a)),27*math.sin(math.radians(a))])
part('SILVER-C','8 mm ezüst R35 sarok',[663,400,2805,35,2,35],'M06','U08','profile',outline=arc)
# R05 owner correction: one connected stepped field, no isolated TV rectangle.
# The drawing radii are design proposals based on the selected image, not survey dimensions.
parts[:]=[p for p in parts if not p['id'].startswith(('FRAME-','TV-','SILVER-')) and p['id'] not in ['D1-B','T-T']]
def arc(cx,cz,r,a0,a1,n=32):return [[cx+r*math.cos(math.radians(a0+(a1-a0)*i/n)),cz+r*math.sin(math.radians(a0+(a1-a0)*i/n))] for i in range(n+1)]
def topband(w,r,t):return arc(r,0,r,180,90)+[[w-r,r]]+arc(w-r,0,r,90,0)+[[w-t,0]]+arc(w-r,0,r-t,0,90)+[[r,r-t]]+arc(r,0,r-t,90,180)
def bottom(poly,h):return [[x,h-z] for x,z in reversed(poly)]
# Rebuild large rounded shells as curved laminated corner assemblies.
for p in parts:
 b=p['box']
 if p['id'] in ['T-L','T-R']:b[5]=2205
 if p['id']=='T-L':b[2]=250;b[5]=2525
 if p['id']=='D1-L':b[2]=168;b[5]=402
 if p['id']=='D1-R':b[2]=168;b[5]=402
 if p['id']=='D6-R':b[2]=230;b[5]=260
 if p['id'] in ['D6-B','D6-T']:b[3]=3520-b[0]
 if p['id']=='D6-FRONT':
  fw=b[3];fh=b[5];r=59;p['outline']=[[0,0],[fw-r,0]]+arc(fw-r,r,r,-90,0)+[[fw,fh-r]]+arc(fw-r,fh-r,r,0,90)+[[0,fh]];p['kind']='profile'
 if p['id']=='D6-BACK':
  fw=b[3];fh=b[5];r=62;p['outline']=[[0,0],[fw-r,0]]+arc(fw-r,r,r,-90,0)+[[fw,fh-r]]+arc(fw-r,fh-r,r,0,90)+[[0,fh]];p['kind']='profile'
 if p['id']=='TEXTILE':p['outline']=rr(0,0,360,2515,60);p['note']='R60 cserélhető szövetbetét; tulajdonosi kép szerinti lágyabb ív javaslat.'
 # Inset tall leaves share one outer rounded top; the meeting line remains straight.
 if p['id'].startswith('T-DOOR-'):
  shape=[[0,0],[828,0],[828,2202]]+arc(749,2202,79,0,90)+[[79,2281]]+arc(79,2202,79,90,180)
  if p['id'].endswith('L'):
   b[2]=171;b[5]=2683
   p['outline']=[[79,0],[412.5,0],[412.5,2683],[79,2683]]+arc(79,2604,79,90,180)+[[0,79]]+arc(79,79,79,180,270)
  else:p['outline']=[[x-415.5,z] for x,z in clip(shape,415.5,False)]
  p['kind']='profile'
 if p['id'] in ['T-L-BACK','T-R-BACK']:
  shape=[[0,0],[834,0],[834,1839]]+arc(752,1839,82,0,90)+[[82,1921]]+arc(82,1839,82,90,180)
  shape=clip(clip(shape,1 if p['id']=='T-L-BACK' else 427,False),407 if p['id']=='T-L-BACK' else 833,True)
  off=1 if p['id']=='T-L-BACK' else 427;p['outline']=[[x-off,z] for x,z in shape];p['kind']='profile'
for id,zz,flip in [('TOP',2775,False),('BOT',150,True)]:
 shape=topband(870,100,18)
 if flip:shape=[[0,100]]+arc(100,100,100,180,270)+[[870,0],[870,18],[100,18]]+arc(100,100,82,270,180)
 part('CURVE-T-'+id,'R100 rétegelt, íves toronysapka',[0,40,zz,870,337,100],'M02','U05','curved_assembly',axis='y',outline=shape,note='18 mm rétegvastagságú hajlított/lamellázott héj, 337mm mélységben. Nem 337mm vastag MDF lap! R100 külső/R82 belső, műhelysablon és rétegrend jóváhagyása kell.')
 part('FRAME-T-'+id,'R100 frontkeret záróelem',[0,382,zz,870,18,100],'M02','U05','profile',outline=shape)
for hand,xx in [('L',0),('R',852)]:
 z0=250 if hand=='L' else 570
 part('FRAME-T-'+hand,'Torony fix függőleges keret',[xx,382,z0,18,18,2775-z0],'M02','U05')
part('FRAME-T-MID','Torony fiók feletti fix osztó',[436.5,382,552,433.5,18,18],'M02','U05')
for name,zz in [('LOW',150),('HIGH',552)]:
 for j,(xx,ww) in enumerate([(870,850),(1720,1030),(2750,770)],1):part(f'FRAME-B-{name}-{j}','Alsó fix keret, jobb végén R80',[xx,382,zz,ww,18,18],'M02','U05')
for name,zz,flip in [('TOP',490,False),('BOT',150,True)]:
 shape=arc(0,0,80,90,0)+[[62,0]]+arc(0,0,62,0,90)
 if flip:shape=bottom(shape,80)
 part('FRAME-B-'+name,'R80 alsó jobb sarok',[3520,382,zz,80,18,80],'M02','U05','profile',outline=shape)
 shape2=arc(0,0,80,90,0)+[[62,0]]+arc(0,0,62,0,90)
 if flip:shape2=bottom(shape2,80)
 part('CURVE-B-'+name,'R80 laminált alsó jobb sarok',[3520,40,zz,80,337,80],'M02','U05','curved_assembly',axis='y',outline=shape2,note='18mm rétegvastagságú íves héj,337mm mély. Nem tömörlap. Pontos rétegrend és ragasztósablon műhelyi feladat.')
part('FRAME-B-R','Alsó jobb fix keret',[3582,382,230,18,18,260],'M02','U05')
# TV field: continuous from tower at x720 and base top at z570.
# Visible upper contour: horizontal tongue, concave R160 rise, convex R140 crown, R100 right corner.
tvshape=[[870,570],[3500,570],[3500,2050]]+arc(3400,2050,100,0,90)+[[1320,2150]]+arc(1320,2010,140,90,180)+[[1180,1110]]+arc(1020,1110,160,0,-90)+[[870,950]]
for name,x0,x1 in [('LINK',870,1498.5),('MID',1501.5,2548.5),('END',2551.5,3500)]:
 shape=clip(clip(tvshape,x0,False),x1,True);local=[[x-x0,z-570] for x,z in shape]
 part('TV-'+name,'Folytonos íves TV-réteg '+name,[x0,95,570,x1-x0,18,1580],'M03','U06','profile',outline=local,grain='V függőleges',note='A kontúr a toronyhoz csatlakozik és az alsó fedlapig fut. Nem külön lebegő téglalap. R160 homorú felkanyarodás/R140 felső átfordulás/R100 jobb sarok.3mm panelhézag; bal csatlakozás takart szerelési hézaga a torony mögött.')
for i,zz in enumerate([605,2050],1):part('TV-SPACER-'+str(i),'TV réteg távtartó',[910,78,zz,2530,17,30],'M02','U06',note='Felső sín csak a panel által takart részen: LINK bal felső kivágásánál helyszíni rövidítés!')
next(p for p in parts if p['id']=='TV-SPACER-2')['box']=[1340,78,2050,2020,17,30]
# Left half is a full-height cupboard, with no drawer below it.
part('T-LOW-DIV','Bal alsó rekesz jobb oldala',[417,40,168,18,337,402],'M01','U03')
backshape=[[0,402],[399,402],[399,0],[82,0]]+arc(82,82,82,-90,-180)
part('T-LOW-BACK','Bal alsó rekesz bontható háta',[18,40,168,399,8,402],'M08','U03','profile',outline=backshape,note='A teljes magas bal ajtó mögött; nincs fiók. Alsó bal R82 illesztés.')
door=next(p for p in parts if p['id']=='T-DOOR-L')
door['light_groove']={'outer':rr(16,74,380,2535,70),'inner':rr(26,84,360,2515,60),'depth':6,'width':10,'from_front_y':400,'note':'Teljes lekerekített perem,10mm széles/6mm mély profilfészek;6mm mélység után12mm hátmaradék. Végleges profil és gyári hajlítás után műhelyi sablonozás.'}
door['note']+=' A teljes peremfény az ajtóval mozog. Pántoldali24V hajlításálló vezeték, oldható csatlakozó és húzásmentesítés; teljes nyitásnál vezetékpróba.'
layout['tower_doors']='2 nyomásra nyíló rugó nélküli pántos ajtó; bal ajtón textil és teljes peremfény együtt mozog. Rejtett24V hajlékony pántoldali átvezetés.6 fiók TIP-ON BLUMOTION.'
layout['ceiling_gap']=25
layout['top_door_gap_mm']=3
layout['top_door_curve_R']=79
layout['top_frame_inside_R']=82
layout['visible_front_gap_mm']=3
layout['bottom_frame_thickness_mm']=18
layout['base_end_front_radius_mm']=59
layout['top_gap_correction']='A korábbi20mm ajtó-felsőhézag helyett3mm. Ajtók17mm-rel magasabbak. Belső keretR82 és ajtóR79 közös ívközépponttal. A mennyezeti25mm fényrés külön változatlan.'
layout['drawer_start_x']=435
layout['textile_margins']={'top':105,'bottom':105,'light_top':100,'light_bottom':100}
layout['owner_latest']='75col TV elfogadva. Bal fél teljes magas ajtó, alatta nincs fiók. A világos betét felső/alsó margója105/105mm; peremfény100/100mm. Jobb oldali ezüst díszcsík eltávolítva. Hat különálló fiók a torony jobb fele alatt indul435mm-től.'
for p in parts:
 dx,dy,dz=p['box'][3:];uv={'x':(dy,dz,dx),'y':(dx,dz,dy),'z':(dx,dy,dz)}[p['axis']];p['L'],p['W'],p['T']=uv
 if p['kind']=='curved_assembly':p['raw_rule']='Egyedi íves héjszerelvény. L/W/T befoglaló, nem lapvastagság. Rétegvastagság18mm; sablon, lamellák és nyers szabás külön műhelyi technológia.'
layout['depth']=408;layout['curves']={'tower_outer_R':100,'base_right_R':80,'textile_R':60,'TV_concave_R':160,'TV_convex_R':140,'TV_right_R':100,'status':'R05 tulajdonosi korrekció szerinti kontúr; nem pixelből igazolt gyártási méret.'};layout['TV_field']='Folytonos, lépcsőző kontúr x870..3500,z570..2150; a toronytól indul és a fedlapig fut. 3 bontható rész, valós3mm szerelési hézagokkal.'
save('data/layout.json',layout)
def arc_vertices(poly):
 # Reconstruct exact circular arcs from the sampled contour for native CAD.
 pts=[]
 for q in poly:
  if not pts or math.dist(q,pts[-1])>1e-6:pts.append(q)
 if math.dist(pts[0],pts[-1])<1e-6:pts.pop()
 seq=pts+[pts[0]];out=[];i=0
 while i<len(pts):
  if i+2>=len(seq):out.append([*seq[i],0]);i+=1;continue
  a,b,c=seq[i:i+3];ax,ay=a;bx,by=b;cx,cy=c;d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
  if abs(d)<1e-7:out.append([*a,0]);i+=1;continue
  ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
  uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
  radius=math.hypot(ax-ux,ay-uy)
  # Only known design radii become arcs; arbitrary triples at straight joints remain lines.
  if min(abs(radius-r) for r in [25,27,35,59,60,62,65,70,79,80,82,90,100,140,160])>.0001:out.append([*a,0]);i+=1;continue
  j=i+2
  while j+1<len(seq) and abs(math.hypot(seq[j+1][0]-ux,seq[j+1][1]-uy)-radius)<1e-5:j+=1
  theta=0
  for q,r in zip(seq[i:j],seq[i+1:j+1]):
   t=math.atan2(r[1]-uy,r[0]-ux)-math.atan2(q[1]-uy,q[0]-ux);theta+=(t+math.pi)%(2*math.pi)-math.pi
  out.append([*a,math.tan(theta/4)]);i=j
 return out
for p in parts:
 if p['outline']:p['curve_vertices']=arc_vertices(p['outline'])
 if p.get('light_groove'):
  for side in ['outer','inner']:p['light_groove'][side+'_vertices']=arc_vertices(p['light_groove'][side])
assert len({p['id'] for p in parts})==len(parts)
save('data/parts.json',parts)

circuits=[]
def light(id,length,wpm,path,group,note):circuits.append(dict(id=id,length_mm=length,W_per_m=wpm,watts=round(length*wpm/1000,3),path=path,group=group,note=note,voltage=24))
# Outer halo follows the actual outer perimeter, fixed behind the body at Y25.
outer_up=[[10,250],[10,2775]]+arc(100,2775,90,180,90)+[[3590,2865],[3590,230]]
outer_low=arc(100,250,90,180,270)+[[3520,160]]+arc(3520,230,70,270,360)
light('A1-OUTER-UP',2525+90*math.pi/2+3490+2635,10,[[x,25,z] for x,z in outer_up],'PS1/Z1','Külső fix fényudvar: bal oldal, felső ív, teljes felső él és jobb oldal.25mm mennyezeti rés; fal felé sugárzó profil.')
light('A2-OUTER-LOW',90*math.pi/2+3420+70*math.pi/2,10,[[x,25,z] for x,z in outer_low],'PS2/Z2','Külső alsó fényudvar, folytonos a fióksor alatt; a torony jobb alsó csatlakozásán nincs visszakerekítés.')
path2=[[870,950],[1020,950]]+arc(1020,1110,160,-90,0)+[[1180,2010]]+arc(1320,2010,140,180,90)+[[3400,2150]]+arc(3400,2050,100,90,0)+[[3500,570]]
light('A3-TV-CONTOUR',150+900+2080+1480+math.pi/2*(160+140+100),10,[[x,88,z] for x,z in path2],'PS2/Z3','Folytonos íves TV-réteg fénye. R160/R140/R100; oldalt hajlítható, megfelelő hűtésű profil és opál fedél, fénypróbával.')
loop=rr(42,250,370,2525,65);loop.append(loop[0])
light('A4-TEXTILE-LOOP',2*(370+2525-4*65)+2*math.pi*65,10,[[x,400,z] for x,z in loop],'PS1/Z4','A világos betét TELJES lekerekített pereme. Az ajtóval mozog.24V hajlításálló kábel a pántoldalon; húzásmentesítés és oldható csatlakozó, becsípődés-próba.')
light('A5-DECK',2670,10,[[900,120,575],[3570,120,575]],'PS2/Z5','Fedlap felmosása a TV-réteg előtt: nem takarja el a Z570-ig folytonos panel. Oldható profil a fedlapon.')
for d,l in zip(drawers,[320,280,280,900,280,280]):light('I-'+d['id'],l,4.8,[[d['x']+50,355,510],[d['x']+50+l,355,510]],'PS3/S-'+d['id'],'Fix korpuszprofil külön nyitásérzékelővel; nincs fiókkábel.')
for side,x in [('L',417),('R',453)]:light('I-T'+side,2245,4.8,[[x,360,590],[x,360,2835]],'PS3/S-T'+side,'Ajtónként külön szenzor, polcok elé tett fix profil; nem a külső dekor-peremfény.')
lighting={'circuits':circuits,'ambient_mm':sum(c['length_mm'] for c in circuits if c['id'][0]=='A'),'internal_mm':sum(c['length_mm'] for c in circuits if c['id'][0]=='I'),'total_W':sum(c['watts'] for c in circuits),'supplies':[{'id':'PS1','model':'24V/200W SELV CV, pontos SKU szakági lezárás','W':200,'load_W':sum(c['watts'] for c in circuits if c['group'].startswith('PS1'))},{'id':'PS2','model':'24V/200W SELV CV, pontos SKU szakági lezárás','W':200,'load_W':sum(c['watts'] for c in circuits if c['group'].startswith('PS2'))},{'id':'PS3','model':'24V/60W kompatibilis Loox rendszerű jelölt','W':60,'load_W':sum(c['watts'] for c in circuits if c['group'].startswith('PS3'))}],'control':'5 külön Sunricher SR-ZG9101FA-CCT CV vezérlő előirányzat, 2200–6500 K 24V CCT LED, max.10W/m együttes csatornateljesítmény. Hue párosítás/fénypróba szükséges. Nem Philips Lightstrip Plus SKU. 8 belső Loox érzékelő egymástól független.','service':'D16 meglévő betáp -> elkülönített 230V doboz a torony alsó hátsó 95mm szervizében -> 3 külön DC tápegység -> biztosított ágak -> vezérlők/szenzorok -> profilok; A4 ajtóval mozgó, hajlékony24V átvezetéssel. Tápkimenetek nem köthetők párhuzamosan. G01–G04/G08 és D17/D18 hozzáférést felmérő biztosítja.','cable':'Áganként tervezett max.6m egyirányú út; 2×1,0mm² belső és 3×1,0mm² CCT induló vezetékjavaslat. A1 kb87,9W/24V=3,66A;6m oda-vissza rézhurok0,21Ω,ΔU≈0,77V=3,2%; ezért A1 kétoldali táplálás vagy2,5mm² kábel szükséges. 3×1mm² csak kisebb ágakon, végleges méretezéssel. Végleges hossz, csatlakozó, közös pozitív ér és ágvédelem villanyszerelői méretezés.','ventilation':'Szervizmodulonként alul/felül külön 200×15 mm szellőzőrés előirányzat; kész hőpróba nélkül nem elégségesnek minősített. Elektronikát tárolt textiltől el kell választani.','change_from_prompt':'Teljes külső kontúr és teljes textil-perem: a kiszámított fényutak szerinti új többlet. A30m/10m beszerzési keret nem beépülési hossz. CCT technológiai helyettesítés külön tulajdonosi döntés.'}
save('data/lighting.json',lighting)

cost=[]
def c(id,group,name,q,u,base,low,high,source):cost.append(dict(id=id,group=group,name=name,qty=q,unit=u,unit_base=base,unit_low=low,unit_high=high,base=round(q*base),low=round(q*low),high=round(q*high),status='Bruttó tervezői becslés, nem ajánlat',source=source))
common='S01 R16 cost.json és élő Elemregiszter, 2026-10-29. Azonos műszaki tartalom költségfeltevése, nem új ajánlat.'
c('C01','Alsó bútor','6 korpusz + sík dekorfront',1,'csomag',225000,175000,305000,common)
c('C02','Alsó bútor','MOVENTO300 sínpár',6,'pár',35000,28000,46000,common)
c('C03','Alsó bútor','TIP-ON + kapocs + szinkron + stabilizátor',6,'szett',30000,24000,40000,common)
c('C04','Alsó bútor','6 nyír fiókdoboz',1,'csomag',135000,100000,190000,common)
c('C05','Alsó bútor','Alsó bútor műhelymunka',1,'csomag',200000,160000,240000,common)
c('U01','Felső és felület','Háttér hordozó MDF',6.258075,'m²',12500,9500,17000,'R05 2×678×2305 és2×679,5×2305 mm; anyag becslés, gyártási hulladék U09-ben.')
c('U02','Felső és felület','Szürke textilhatású háttér, beszerzési keret',6.93,'m²',24000,16000,36000,'10,5% burkolati ráhagyás; saját becslés, nincs webshopár.')
c('U03','Felső és felület','Toronytest, 10 polc, bontható hátak',1,'csomag',155000,120000,220000,'R05 alkatrészjegyzék; anyag + élzárás, munkadíj U09.')
c('U04','Felső és felület','2 ajtó dekorral + pánt/TIP-ON',1,'csomag',190000,145000,265000,'11 pánt +2 nyitó becsült keret; rugó nélküli inset változat ellenőrzendő.')
c('U05','Felső és felület','Nagy ívű grafit keretek és laminált sarokhéjak',1,'csomag',285000,195000,430000,'R100 torony/R80 alsó keret; valódi íves sarokhéjak,sablon és2KPU; U09 csak végszerelés.')
c('U06','Felső és felület','Folytonos TV-réteg és távtartók',4.16,'m²',35000,25000,50000,'Három kontúrozott rész a toronytól a fedlapig, R160/R140/R100. Bruttó téglalapanyag-keret; nem csak látható nettó terület.')
c('U07','Felső és felület','Valódi textilbetét, bontható rögzítés',1,'db',46000,31000,71000,'360×2515; kész kárpitos elem becslés.')
c('U09','Felső és felület','Felső műhely-összeállítás és segédanyag',1,'csomag',100000,75000,150000,'A készre árazott U05–08 felületek munkája itt nem ismétlődik; hordozó hulladék és ragasztó benne.')
c('U10','Felső és felület','Együttes szín-/él-/fénypróba',1,'csomag',65000,45000,100000,'Fizikai minta elkészítése; a próba még nem történt meg.')
c('F01','Rögzítés és szerelés','7 korpusz rögzítése és helyszíni beépítés',1,'csomag',504800,429080,656240,common+' KI-032; átfedés KI-014 szerelési sorral ajánlati tisztázásra.')
c('F02','Rögzítés és szerelés','Plusz előre oldható panelkapcsok/sínek',1,'keret',60000,35000,95000,'S16 rétegzett paneltöbblet. Falhorgony végleges méretezése külön feltétel.')
c('TV01','TV-konzol','Vogel TVM3605 konzol',1,'db',32000,27200,41600,common+' KI-034; a TV vételára külön marad.')
c('L01','Világítás','Belső világítás teljes 8 érzékelős csomag',1,'csomag',196000,135000,292000,common+' 10m LED/profil keret, kábel, szenzor és szerelés; táp L07-ben.')
c('L02','Világítás','24V CCT külső LED beszerzés',30,'m',7000,4500,10000,'Teljes körbefutó kontúrok;30m beszerzési keret, 10W/m max. Saját becslés.')
c('L03','Világítás','Külső profil, opál fedél, végzáró',30,'m',4500,3000,6500,'Profilkeret, tényleges vágás/fénypróba szükséges; egyenes szakaszok.')
c('L04','Világítás','CCT vezérlők, 5 független külső fényút',5,'db',19000,14000,28000,'Sunricher SR-ZG9101FA-CCT jelölt; gyári adat ellenőrizve, ár becslés.')
c('L05','Világítás','Külső 24V/200W tápegység',2,'db',35000,25000,50000,'200W SELV CV táp, pontos SKU nyitott; konzervatív3D helyfoglalóval, villamos/hőpróba nélkül.')
c('L06','Világítás','Külső kábel, védelem, csatlakozók',1,'csomag',50000,35000,80000,'5 külön ág; nincs ingyenes elosztás vagy Hue szalagvágás feltételezve.')
c('L07','Világítás','Belső kompatibilis 24V/60W táp',1,'db',25000,18000,38000,'Loox rendszerhez illő kész táp/csatlakozó; pontos SKU szakági lezárásra.')
c('L08','Világítás','Külső villamos szerelés és hő/fénypróba',1,'csomag',90000,60000,140000,'L01 belső szerelését nem ismétli; meglévő D16 betáp alkalmassága feltétel.')
c('L09','Világítás','Torony szerviztér kialakítása',1,'csomag',35000,20000,55000,common+' S16 két hátsó bontható rekesz és szellőzés.')
tot={k:sum(r[k] for r in cost) for k in ['base','low','high']}
save('data/cost.json',{'rows':cost,'totals':tot,'S01':ki,'S01_total':2969300,'S01_low':2438726,'S01_high':4030447,'delta':tot['base']-2969300,'project_S01':26212190,'project_S16_if_replaced':26212190-2969300+tot['base'],'target':18000000,'reserve_separate':2000000,'exclusions':'TV-készülék, szobai tárgyak, W02 fal, szállítás/felhordás/daruzás és közös logisztika a projekt meglévő KI-151/KI-137 keretében; nem ingyenes, ide nem adva újra. KI-014/KI-106 szakági átfedés tisztázandó. A teljes lakás előirányzata csak W01 cserét számol, nem S16 teljes lakásár.','uncertainty':'S16 minimum/maximum soronkénti becslési sáv, anyag-, egyedi marás-, munkadíj- és villamos rendszerbizonytalanság; nem statisztikai konfidenciaintervallum. S01 és S16 sávja átfed, biztos megtakarítás nem állítható.'})

sources=[
 ['SRC01','C célkép + eredeti prompt','../sources/S16_Cam02_C_celkep.png','Pixelhash ellenőrizve; megjelenési referencia, nem felmérés.'],
 ['SRC02','Blum 2026 online katalógus, MOVENTO rendelés','https://publications.blum.com/2026/catalogue/en/520/','760H3000S, T51.7601, S0/S1 működési tartomány, szinkron LW-267. Online oldal 2027/2028 felirattal; nem utólag igazolt termékár.'],
 ['SRC03','Blum MOVENTO tervezés','https://publications.blum.com/2026/catalogue/en/521/','SKW=LW-42; SKL=NL-10; max16mm oldalfal; min2,5mm rés. Fúrás T65.1000.02 sablonnal.'],
 ['SRC04','EGGER H3198 ST19','https://www.egger.com/en/furniture-interior-design/decors/H3198_19','Sötétszürke irányított fadekor, valódi minta szükséges.'],
 ['SRC05','Sunricher CCT gyári leírás','https://www.sunricher.com/media/resources/manual/SR-ZG9101FA-CCT%20instruction%20V1.pdf','CV variáns 12–36V, 4×5A, 170×53,4×28mm; Hue kapcsolat külön próbálandó.'],
 ['SRC06','Blum pántváltozatok','https://publications.blum.com/2022/catalogue/en/74/','Inset és rugó nélküli variáns külön termék. Pántszám/talp/furat nem kiadott.'],
 ['SRC07','S01 R16 forrás','../../a902-s01-kyoto-ink-20261026/R16_feluletek_fiokok/data','Aktuális alkatrész/vasalat/fény geometria; élő regiszter öt sora visszaolvasva.'],
 ['SRC08','Építészeti v2b modell','.wsg-inputs/03_blender/geometry_lock_A902_v2b.json','W01 tervi falsík 4m; 2,90m névleges belmagasság. Falminimum és szervizpontok helyszínen ellenőrizendők.']]
save('data/sources.json',{'accessed':DATE,'sources':sources,'pricing':'Minden új S16 ár tervezői becslés. Nincs igazolt magyar webshopár vagy fix írásos ajánlat.'})
gates=[
 ['G01','Felmérési minimumok és falsík','Összes elem','Asztalos felmérő','3 magasságban szélesség, 5 ponton magasság, átlók, faleltérés, szegő/függöny; közös XYZ fotóval','Gyártási méretkiadás előtt'],
 ['G02','3600-as új frontosztás és870-es torony','D1–D6, torony','Péter + tervező','Célkép és R05 homlokzat összevetése; hatfiókos funkció elfogadása','Árajánlat véglegesítése előtt'],
 ['G03','Fal és függesztés','F01/F02','Asztalos + illetékes szakember','Falanyag/vezetékkeresés, terhek és horgony gyári méretezése, kihúzási teherpróba ha indokolt','Fúrás előtt'],
 ['G04','Fiók működés és tömeg','MOVENTO / D1–D6','Műhely + Blum szaktanácsadó','S0/S1 össztömeg; sablonfurat, min3mm rés; széles/rövid D4 stabilitás, egy teljes elsődarab','Sorozatgyártás előtt'],
 ['G05','Ajtó/textil tömeg és nyitás','T-DOOR / TEXTILE','Műhely','Inset rugó nélküli pánt/talp/TIP-ON pontos SKU; bal6/jobb5pánt előirányzat terhelési igazolás; 90° mozgáspróba','Furatkiadás előtt'],
 ['G06','Szín és rétegrend','M02–M05','Péter + asztalos/kárpitos','A3 együttminta nappali/2700K; él, ragasztó, lakk és textil','Felületgyártás előtt'],
 ['G07','Fény és szerviz','A1–A5 / I1–I8','Villanyszerelő','D16 kapacitás; végleges LED/profil/SKU/kapcsolás; Hue próba, teljes terhelésű hőpróba; vezeték/ágvédelem','Villamos kivitelezés előtt'],
 ['G08','TV és kiállások','TV-L/R, konzol','Felmérő + TV szerelő','Készülék/VESA magasság, csatlakozóhajlítás, feloldók, hűtés és D16–18/G pontok sablonja','TV-panelek kivágása előtt'],
 ['G09','Szállítás, panelbontás','2875-ös összeállítás, 2305-ös háttérpanelek','Asztalos/logisztika','Lift/ajtó/forduló mérés; helyszíni korpuszépítés; előrefelé oldható kapocs próbája 25mm mennyezeti résnél','Gyártás előtt'],
 ['G10','Szobai használat és asztal','6 nyitott fiók, torony','Péter + tervező','300mm fiókút után legalább600mm használati sáv cél; asztal tényleges helye, JÄTTEBO kézállás és nyíló teraszszárny','Végső elrendezés előtt'],
 ['G11','Ajánlati átfedés és keret','Teljes költség','Péter + ajánlatadó','F01/C05/U09 és KI-014; L08/KI-106; szállítás KI-151 és daruzás KI-137 egyeztetése','Rendelés előtt'],
 ['G12','Műhelyi gép és gyártáskiadás','Összes alkatrész','Műhely/gépkezelő','WOF211 megnevezés helyett adattábla, szerszám és befogás; sablonok/elsődarab. CNC-program nincs kiadva.','Gyártásra jóváhagyás előtt']]
save('data/gates.json',[dict(zip(['id','open','parts','owner','acceptance','deadline'],g),status='NYITOTT',evidence='',approver='') for g in gates])
save('data/deviations.json',[
 {'id':'E01','type':'Tulajdonosi változtatás','source':'240cm alsó +65cm torony','proposal':'Teljes360cm; alsó6modul, torony870mm','approval':'Szélesség eldöntött; frontosztás javaslat.'},
 {'id':'E02','type':'Funkciónormalizálás','source':'4 ajtó a promptban','proposal':'6 magas MOVENTO fiók +2 magas ajtó','approval':'Árösszevetési feltétel, nem külön elfogadott külső.'},
 {'id':'E03','type':'Render/prompt eltérés','source':'3m W01 Hue; a képen több világító kontúr','proposal':'5 külső fényút26,049m +6,83m belső; CCT rendszer','approval':'Technológiacsere külön döntés, nincs Hue SKU-ként eladva.'},
 {'id':'E04','type':'Szerelhető javaslat','source':'Egybefüggő háttérnek látszik','proposal':'678/679,5/679,5/678mm bontható háttér; folytonos TV-réteg3részes, a toronytól a fedlapig. Valós3mm szerelési hézag.','approval':'Illesztési minta szükséges.'},
 {'id':'E05','type':'Nyitott részlet','source':'Keskeny ezüst sarok a promptban, képen bizonytalan','proposal':'Tulajdonosi kérésre az ezüst díszcsík eltávolítva.','approval':'Nem része az aktuális tervnek.'},
 {'id':'E06','type':'Színértelmezés','source':'Meleg fényben barnás render','proposal':'Semleges grafit + sötétszürke fadekor, valódi ivory textil','approval':'Színminta szükséges; az esti kép nem barnára rendelési alap.'},
 {'id':'E07','type':'Kapacitás','source':'S01 R16 fiókszám és polcszám','proposal':'155,7liter fióktér a S01 180,8litere helyett; bal alsó rekesz teljes magas ajtó mögött;10db406×290polc, a S01 331×290polcainál szélesebb; R100 felső sarok környezetében kisebb szabad tér. Nem azonos téglatest-térfogat.','approval':'Szervizteret, felső sarkokat és frontszűkületet használati próbán ellenőrizni.'},
 {'id':'E08','type':'Kifejezett tulajdonosi formakorrekció','source':'2026-10-29: a réteg a bal szekrénytől indul és az alsóig fut; nagyobb ívek.','proposal':'R01 kiváltva. R05 TV kontúr R160/R140/R100; toronyR100,alsóR80,textilR60.','approval':'Folytonos forma tulajdonosi kérés; számszerű sugarak tervezési javaslatok, nem külön gyártási jóváhagyás.'}])

# Editable DXF, mm, every part as its own named layer/block in assembly.
doc=ezdxf.new('R2018');doc.units=4;m=doc.modelspace()
for layer,col in [('OUTLINE',7),('DIM',3),('TEXT',7),('LIGHT',2),('OPEN',1),('PLAN',4)]:doc.layers.new(layer,dxfattribs={'color':col})
def line(a,b,layer='OUTLINE'):m.add_line(a,b,dxfattribs={'layer':layer})
def poly(points,layer='OUTLINE'):m.add_lwpolyline(points,close=True,dxfattribs={'layer':layer})
def txt(t,x,y,h=35,layer='TEXT'):m.add_text(t,dxfattribs={'height':h,'insert':(x,y),'layer':layer})
def dim(x1,x2,y,label=None):
 line((x1,y),(x2,y),'DIM');line((x1,y-25),(x1,y+25),'DIM');line((x2,y-25),(x2,y+25),'DIM');txt(label or str(round(x2-x1,1)),(x1+x2)/2-50,y+20,35,'DIM')
for p in parts:
 x,y,z,dx,dy,dz=p['box']
 if p['axis']=='y' and p['outline']:poly([(x+a,z+b) for a,b in p['outline']])
 else:poly([(x,z),(x+dx,z),(x+dx,z+dz),(x,z+dz)])
 # top view below elevation, increasing room depth downwards on sheet
 poly([(x,-700-y),(x+dx,-700-y),(x+dx,-700-y-dy),(x,-700-y-dy)],'PLAN')
for c0 in circuits:
 path=[(a[0],a[2]) for a in c0['path']]
 for a,b in zip(path,path[1:]):line(a,b,'LIGHT')
a,b,z,dx,dy,dz=layout['screen_box'];poly([(a,z),(a+dx,z),(a+dx,z+dz),(a,z+dz)]);txt('75 INCH / 1677.5 x 962.4',a,z+dz+35,35)
for d in drawers:
 x=d['x'];ww=d['width'];poly([(x,-1100),(x+ww,-1100),(x+ww,-1400),(x,-1400)],'OPEN')
dim(0,3600,-250,'3600 mm - TULAJDONOSI TERVCEL')
x=435
dim(0,435,-120,'435 teljes magas bal ajto')
for width in layout['module_widths']:dim(x,x+width,-120);x+=width
txt('S16 R05 / 2026-10-29 / mm / TERV - NEM GYARTASI KIADAS',0,3080,45)
txt('Homlokzat es alaprajz; Y faltol a szoba fele. Nyitott fiokut 300.',0,-1600,35)
doc.saveas(O/'rajzok/S16_R05_nezetek.dxf')
assembly=ezdxf.new('R2018');assembly.units=4;ms=assembly.modelspace()
for p in parts:
 x,y,z,dx,dy,dz=p['box'];layer=p['id'];assembly.layers.new(layer,dxfattribs={'color':8})
 a=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
 for face in [(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]:ms.add_3dface([a[k] for k in face],dxfattribs={'layer':layer})
 # Manufacturing profile stored separately; these assembly faces are explicit bounding envelopes.
assembly.saveas(O/'rajzok/S16_R05_3D_befoglalok.dxf')
for p in parts:
 d=ezdxf.new('R2018');d.units=4;sp=d.modelspace();poly0=p['outline'] or [[0,0],[p['L'],0],[p['L'],p['W']],[0,p['W']]]
 if p.get('curve_vertices'):sp.add_lwpolyline(p['curve_vertices'],format='xyb',close=True)
 else:sp.add_lwpolyline(poly0,close=True)
 if p.get('light_groove'):
  d.layers.new('LIGHT_POCKET_6MM',dxfattribs={'color':2})
  for side in ['outer','inner']:sp.add_lwpolyline(p['light_groove'][side+'_vertices'],format='xyb',close=True,dxfattribs={'layer':'LIGHT_POCKET_6MM'})
 sp.add_text(p['id']+' / S16-R05 / mm / TERV',dxfattribs={'height':12,'insert':(0,-35)})
 d.saveas(O/'alkatreszek'/(p['id']+'.dxf'))
checks=[]
for f in list((O/'rajzok').glob('*.dxf'))+list((O/'alkatreszek').glob('*.dxf')):
 d=ezdxf.readfile(f);a=d.audit();assert not a.has_errors;assert d.units==4
 checks.append({'file':str(f.relative_to(O)),'entities':len(d.modelspace()),'audit_errors':len(a.errors),'units':'mm','external_refs':len([b for b in d.blocks if b.block.is_xref])})
save('audit/dxf_readback.json',checks)
with (O/'data/alkatreszek.csv').open('w',newline='') as f:
 cw=csv.writer(f);cw.writerow(['ID','Revízió','Megnevezés','Kész L mm','Kész W mm','T mm','Anyag','Költségkód','Szálirány','Státusz'])
 for p in parts:cw.writerow([p['id'],REV,p['name'],p['L'],p['W'],p['T'],p['material'],p['cost'],p['grain'],p['status']])
print(json.dumps({'parts':len(parts),'drawers_litres':sum(d['litres'] for d in drawers),'light':lighting['total_W'],'ambient_m':lighting['ambient_mm']/1000,'cost':tot,'delta':tot['base']-2969300},ensure_ascii=False))

import bpy,json,math,hashlib
from pathlib import Path
P=Path('/Users/peterkapusi/Documents/ChatGPT/WSG – Stíluslabor/execution/a902-s01-kyoto-ink-20261026');D=json.loads((P/'data/design_R02.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
# Separate, hidden, UNAPPROVED alternative: retains160 bed +1000mm desk, reduces fullheight hanging width.
alt=[dict(id='A52-WARDROBE',bounds=[.02,2.72,0,1.4,3.32,2.84],description='1380mm fullheight storage instead of2380; two690mm bays'),dict(id='A52-DESK',bounds=[1.4,2.72,0,2.4,3.32,.75],description='1000×600 integrated desk in former wardrobe bay'),dict(id='A52-UPPER',bounds=[1.4,2.72,1.84,2.4,3.32,2.84],description='1000×600×1000 upper storage,1100mm clear above desktop'),dict(id='A52-CHAIR',bounds=[1.55,1.98,0,2.26,2.69,1.14],description='FLINTAN71cm envelope; working position')]
coll=bpy.data.collections.new('KI_R02_ALT_052_UNAPPROVED');bpy.context.scene.collection.children.link(coll)
for a in alt:
 b=a['bounds'];bpy.ops.mesh.primitive_cube_add(size=1,location=[(b[i]+b[i+3])/2 for i in range(3)]);o=bpy.context.object;o.name=a['id'];o.dimensions=[b[i+3]-b[i] for i in range(3)]
 for c in list(o.users_collection):c.objects.unlink(o)
 coll.objects.link(o);o['approval']='UNAPPROVED ALTERNATIVE; not included in main model or cost';o['description']=a['description']
coll.hide_render=True;coll.hide_viewport=True

def overlap(a,b):return all(min(a[i+3],b[i+3])-max(a[i],b[i])>.005 for i in range(3))
checks=[]
for a in alt:
 for n,b in G['walls'].items():
  if not n.startswith('Plafon') and overlap(a['bounds'],b):checks.append([a['id'],n,'WALL'])
# Retained existing main furniture: exclude replaced desk/wardrobe/chair, same room only.
for a in alt:
 for it in D['units']+D['items']:
  if it['room']!='05.2' or it['id'] in ['DS52','W52-01','KI-063']:continue
  w,dd=it['w']/1000,it['d']/1000
  if it['rot']==90:w,dd=dd,w
  b=[it['x'],it['y'],it['z'],it['x']+w,it['y']+dd,it['z']+it['h']/1000]
  if overlap(a['bounds'],b):checks.append([a['id'],it['id'],'FURNITURE'])
for dn in ['Ajto_05_2','Erkelyajto_05_2']:
 m=G['openings_meta'][dn];hx,hy=m['zsaner'];base=math.pi if dn=='Ajto_05_2' else math.pi/2;sign=1 if dn=='Ajto_05_2' else -1
 for a in alt:
  b=a['bounds'];hit=False
  for deg in range(0,91,5):
   angle=base+sign*math.radians(deg)
   for step in range(1,31):
    x=hx+m['r']*step/30*math.cos(angle);y=hy+m['r']*step/30*math.sin(angle)
    if b[0]-.02<x<b[3]+.02 and b[1]-.02<y<b[4]+.02:hit=True;break
   if hit:break
  if hit:checks.append([a['id'],dn,'DOOR'])
result=dict(revision='KI-V33-R02-ALT052',approval='OWNER_DECISION_REQUIRED; not adopted',objects=alt,method='Blender-run AABB and5degree door sample; same room furniture retained',collisions=checks,status='NO_FLAGS_IN_LIMITED_SCREEN' if not checks else 'REVIEW',tradeoff='1000mm fullheight wardrobe bay replaced by desk+upper storage; fullheight wardrobe width2380→1380mm',cost='Main KI-062/DS52 costs unchanged; additional fitting/upper support allowance +80000Ft ±40000, not included until choice and quote',open=['Exact wardrobe fittings and work surface support','Wardrobe door sweep vs desk service','Owner acceptance of reduced hanging capacity','Window glare and desk light point'])
(P/'blender/alternative_052_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));bpy.ops.wm.save_as_mainfile(filepath=str(P/'blender/A902_Kyoto_Ink_R02.blend'),compress=True);print(json.dumps(result))

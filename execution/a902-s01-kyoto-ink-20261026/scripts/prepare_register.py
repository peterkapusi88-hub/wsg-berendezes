from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parents[1];r=json.loads((p/'data/elemek.json').read_text());d=json.loads((p/'data/design_R02.json').read_text());b=json.loads((p/'blender/validation_R02.json').read_text());snapshot=json.loads((p/'data/workbook_readback_CP1a.json').read_text());new=[]
for a in r:
 rel=[u for u in d['units'] if a['elemkod'] in u['cost']]
 if rel:a['szerkezet']='; '.join(u['id'] for u in rel);a['meret']='; '.join(f"{u['id']}: {u['w']}×{u['d']}×{u['h']} mm" for u in rel)
 ob=[o for o in b['objects'] if a['elemkod'] in o['element'].split(';')]
 a['blender_objektum']='; '.join(n for o in ob for n in o['blender_objects']) if ob else 'NINCS MODELL / nem térbeli költségsor; szakági kapcsolat igazolandó'
 if a['elemkod']=='KI-070':a['meret']='1800×2020×300 mm; alaprajzon2020×1800 mm';a['egyezes']='180 cm fekvőfelület megtartva; NORDLI fehér tárolós keret. Keleti fejvégű elforgatás, sekély gardrób: új helyiségjavaslat.'
 # Exact useful alternative replaces unspecified pendants: retain Somar until a real SKU is established.
 if a['elemkod']=='KI-109':a['gazdasagos']=a['egysegar'];a['optimalizalas']='Somar megtartva. A névtelen papírbúra csere nem kellően igazolt, megtakarítást nem számolunk rá.'
 # Concrete outdoor economy package found on official IKEA, its larger chaise still requires fit.
 if a['elemkod']=='KI-138':a['gazdasagos']=190500;a['optimalizalas']='NÄMMARÖ 295.752.24, Kuddarna világosszürke-bézs,210×74/137×82cm,190500Ft. Link: https://www.ikea.com/hu/hu/p/naemmaroe-3-szemelyes-kanape-labtartoval-vilagos-barnara-pacolt-kuddarna-vilagosszuerke-bezs-s29575224/ . Akác a grafit fém helyett; chaise miatt új illesztés kell. Szállítás és szerelés központi kerete változatlan. Tulajdonosi döntésre vár.'
 if a['elemkod']=='KI-139':a['gazdasagos']=a['egysegar'];a['optimalizalas']='Konkrét kültéri fotelvariáns hiányzik; nem számolunk bizonyítatlan megtakarítást.'
 a['netto_megtakaritas_afa_utan']=a['mennyiseg']*(a['egysegar']-a['gazdasagos'])
 new.append(a)
(p/'data/elemek.json').write_text(json.dumps(new,ensure_ascii=False,indent=2))
c=json.loads((p/'data/cost_snapshot_R02.json').read_text());c['economy']=sum(a['mennyiseg']*a['gazdasagos']+a['szallitas']+a['szereles']+a['egyeb'] for a in r);(p/'data/cost_snapshot_R02.json').write_text(json.dumps(c,indent=2));print('Budget',c)
tabs=[]
def tab(name,headers,values,widths):tabs.append(dict(name=name,headers=headers,values=values,widths=widths))
cov=json.loads((p/'data/lefedettseg_R02.json').read_text());tab('Lefedettség',list(cov[0]),[list(x.values()) for x in cov],[12,22,40,40,40,40,40,30])
l=d['lights'];keys=['id','source','room','target','route','driver','service','status','scene'];tab('Világítás',keys,[[x.get(k,'') for k in keys] for x in l],[20,18,24,18,50,50,42,40,50])
f=json.loads((p/'data/feluletek_textilek_R02.json').read_text());sur=f['surfaces'];tab('Felületi mennyiségek',list(sur[0]),[list(x.values()) for x in sur],[18,18,18,18,18,18,22,55,55,55]);tex=f['textiles'];tab('Textilmennyiségek',list(tex[0]),[list(x.values()) for x in tex],[15,18,18,18,18,20,20,22,22,25,50,50])
i=json.loads((p/'data/nyitott_kerdesek_R02.json').read_text());tab('Nyitott döntések',list(i[0]),[list(x.values()) for x in i],[14,42,35,20,90,18])
t=json.loads((p/'data/utemterv_R02.json').read_text());tab('Ütemterv',list(t[0]),[[','.join(v) if isinstance(v,list) else v for v in x.values()] for x in t],[14,50,18,18,28,24,90])
pr=json.loads((p/'data/termek_bovites_R02.json').read_text());pr=[x for x in pr if x['elem']!='KI-070'];pr.append(dict(pr[0],elem='KI-070',name='NORDLI fehér180×200',sku='203.498.53',dimensions='1800×2020×300mm',price_huf=189900,url='https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/',deviation='180cm fekvőfelület megőrizve; új keleti fejvégű elhelyezés'))
(p/'data/termek_bovites_R02.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2));tab('További termékek',list(pr[0]),[[x.get(k,'') for k in pr[0]] for x in pr],[14,45,30,45,20,22,50,80,20,70,35,60])
tab('CP1a eltérések',['Elem','Megnevezés','CP1a Ft','V3.3 Ft','Eltérés Ft','Tartalom'],[[x['elemkod'],x['megnevezes'],snapshot['Elemregiszter'][n+1][20],None,None,x['megjegyzes']] for n,x in enumerate(r)],[16,50,22,22,22,85])
visual=json.loads((p/'data/vizualis_elteres_R02.json').read_text());tab('Vizuális eltérések',list(visual[0]),[list(x.values()) for x in visual],[12,25,45,65,25,80,25])
cut=json.loads((p/'data/cutlist_R02.json').read_text());tab('Előzetes szabáslista',list(cut[0]),[list(x.values()) for x in cut],[20,35,35,18,18,18,12,50,30,70,55])
alt=json.loads((p/'data/alternative_052.json').read_text());tab('05.2 alternatíva',['Változat','Státusz','Fő csomag Ft','Alternatíva Ft','Projektkülönbség Ft','Kompromisszum','Rajz'],[['ALT-052',alt['approval'],315000,395000,80000,alt['tradeoff'],'drawings/ALT-052.pdf']],[22,50,22,22,25,75,45])
(p/'data/workbook_extension.json').write_text(json.dumps(tabs,ensure_ascii=False,indent=2))

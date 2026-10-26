from pathlib import Path
import json
p=Path(__file__).resolve().parents[1];d=json.loads((p/'data/design_R02.json').read_text());r=json.loads((p/'data/elemek.json').read_text())
for u in d['units']:
 u['opening_dir']= '-x' if u['rot']==90 else '-y'
 if u['id'] in ['K-05','K-06']:u['opening_dir']='+x'
 if u['id'] in ['K-01','WS-01','ENT-02','ART-02']:u['opening_dir']='+y'
 if u['id']=='TV-01':u['z']=.55;u['h']=2330
 if u['id']=='K-08':u.update(w=1460,modules=[1460],notes=u['notes'].replace('2060','1460'));u['opening_dir']='none'
 if u['id']=='HALL-01':u['opening_dir']='none'
 if u['id']=='W53-01':u['x']=13.73;u['y']=6.22
 if u['id'] in ['NT-L','NT-R']:u['opening_dir']='-x'
k=next(u.copy() for u in d['units'] if u['id']=='K-08');k.update(id='K-09',name='Nyugati munkalap',w=1600,x=8.47,y=2.42,modules=[1600]);d['units'].append(k)
for it in d['items']:
 if it['id']=='KI-070':it.update(name='NORDLI 180×200 fehér',sku='203.498.53',w=1800,d=2020,h=300,proof='CP1a NORDLI gyári méret; 180 cm funkció megőrzése')
r[69].update(megnevezes='NORDLI 180×200 fehér ágykeret',sku='203.498.53',meret='1800×2020×300 mm',egysegar=189900,gazdasagos=189900,link='https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/',arforras='CP1a ellenőrzött azonos NORDLI variáns',egyezes='05.3 meglévő 180 cm funkció megtartva; fehér tárolós keret, taupe/grafit textilekkel.')
for a in r:
 rel=[u for u in d['units'] if a['elemkod'] in u['cost']]
 if rel:a['szerkezet']='; '.join(u['id'] for u in rel);a['rajz']='; '.join('drawings/'+u['id']+'.pdf' for u in rel);a['meret']='; '.join(f"{u['id']}: {u['w']}×{u['d']}×{u['h']} mm" for u in rel)
 a['ar_also']=round((a['mennyiseg']*a['egysegar']+a['szallitas']+a['szereles']+a['egyeb'])*a['min_factor']);a['ar_felso']=round((a['mennyiseg']*a['egysegar']+a['szallitas']+a['szereles']+a['egyeb'])*a['max_factor'])
for f,o in [('data/design_R02.json',d),('data/elemek.json',r)]: (p/f).write_text(json.dumps(o,ensure_ascii=False,indent=2))
c=json.loads((p/'data/cost_snapshot_R02.json').read_text());c.update(main=sum(a['mennyiseg']*a['egysegar']+a['szallitas']+a['szereles']+a['egyeb'] for a in r),economy=sum(a['mennyiseg']*a['gazdasagos']+a['szallitas']+a['szereles']+a['egyeb'] for a in r),low=sum(a['ar_also'] for a in r),high=sum(a['ar_felso'] for a in r),verified=sum(a['mennyiseg']*a['egysegar'] for a in r if a['arstatusz']=='ellenőrzött webshopár'));(p/'data/cost_snapshot_R02.json').write_text(json.dumps(c,indent=2));print(c)

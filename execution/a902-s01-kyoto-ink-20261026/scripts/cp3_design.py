"""CP3 proposal data. Never writes the live workbook or the source model."""
from pathlib import Path
import json, csv, copy, math
P=Path(__file__).resolve().parents[1]
O=P/'CP3'; O.mkdir(exist_ok=True)
for f in ['data','drawings','blender','render_handoff','specifications','evidence','qa']:(O/f).mkdir(exist_ok=True)
def save(name,data):
 (O/name).write_text(json.dumps(data,ensure_ascii=False,indent=2))
D=json.loads((P/'data/design_R02.json').read_text());D['revision']='KI-CP3-R03';D['date']='2026-10-27'
decision={
 'date':'2026-10-26','authority':'Tulajdonos közvetlen válasza ebben a chatben',
 '05.1':'Master: nagyon nagy ruhatárolási igény; mennyezetig gardrób, sok akasztás, fiók, cipő, táska, liftek és belső fény.',
 '05.2':'Gardróbszoba / gyerekszoba: nagy ruhatárolás elsődleges; moduláris alvás, játék és későbbi átalakítás. Ütközésjavítás miatt jelentős gardróbveszteség nem elfogadott.',
 '05.3':'Vendég / dolgozó: kényelmes vendégalvás és teljes munkavégzés, gardrób, iratok. Ágy, asztal, szék és gardrób egyidejű használata.',
 'AT8-01':'4,57 m²; második fagyasztó + tartalékkészlet; két tervi dugalj, nem helyszíni igazolás.',
 'T-0-26':'4,00 m²; bőröndök, nagyobb és ritka holmik; nem napi lakáson belüli tárolás pótlása.',
 'unknown':'Leltár, kész belméretek, fotók, porszívó és vasalódeszka pontos típusa hiányzik. Nem feltétele a tervezés folytatásának.',
 'growth_reserve':.25,'reserve_rule':'A használható kapacitás 25%-a maradjon szabad; nem darabszám-előrejelzés.',
 'lighting_exception':'sources/main/GOAL.md 2026-10-25 01:49: funkcionális szekrénybelső-fény külön vezérelhető; dekor és általános fény Hue.'}
save('data/tulajdonosi_dontes.json',decision)
# Each bay uses its own 18 mm sides. Widths are clear, after carcass deduction.
# Drawers use an explicit conservative 100 mm width and 50 mm depth allowance;
# these are usable design envelopes, NOT manufacturer drilling/cutting formulas.
spec={
 'WN-01':[
  ('Hosszú ruhák + két lapos fiók',[2342],[2110],2,[],[2320,2790]),
  ('Dupla akasztás; felső CONERO lift',[2342],[1040,2160],0,[2160],[2320,2790]),
  ('Dupla akasztás; felső CONERO lift',[2342],[1040,2160],0,[2160],[2320,2790]),
  ('Hat fiók, táskák, hajtogatott ruhák',[1500,1830,2160,2342],[],6,[],[1470,1800,2130,2790])],
 'WS-01':[
  ('Cipők; sík, állítható polcok',[280,560,840,1120,1400,1680,1960,2342],[],0,[],[250,810,1370,1930,2790]),
  ('Cipők; magas csizmák alsó 540 mm',[560,840,1120,1400,1680,1960,2342],[],0,[],[530,1090,1650,2310,2790]),
  ('Táskák + négy fiók',[1080,1450,1820,2160,2342],[],4,[],[1050,1420,1790,2130,2790]),
  ('Napi háztartási eszközök; felső zárható vegyszer',[1900,2342],[],0,[],[1870,2790])],
 'W52-01':[
  ('Felnőtt ruhatöbblet; dupla rúd',[2342],[1040,2160],0,[],[2320,2790]),
  ('Hosszú ruhák; később alacsony gyerekrúd',[2342],[1960],0,[],[2320,2790]),
  ('Négy fiók; hajtogatott ruhák',[1080,1450,1820,2160,2342],[],4,[],[1050,1420,1790,2130,2790]),
  ('Játék alul; ruhák felül; állítható polc',[450,900,1350,1800,2160,2342],[],0,[],[420,1320,2130,2790])],
 'W53-01':[
  ('Vendégruha; előre kihúzható 350 mm rúd',[1800,2160,2342],[1700],0,[],[1770,2310,2790]),
  ('Iratok / mappák; 5 állítható polc',[440,880,1320,1760,2200,2342],[],0,[],[850,1730,2310,2790]),
  ('Négy fiók; irodaszer / vendégtextil',[1080,1450,1820,2160,2342],[],4,[],[1050,1790,2310,2790])],
 'ENT-01':[
  ('Napi kabát előre kihúzható rúdon',[450,2200,2600],[2000],0,[],[2170,2570]),
  ('Cipő, kutyapóráz, tiszta törlő; zárható felső',[320,640,960,1280,1640,2000,2400],[],0,[],[610,1250,1970,2370])],
 'TV-01': [('Könyv / dekor; terhelt polcpróba',[400,800,1200,1600,2000],[],0,[],[770,1570,2280])]*2,
 'TV-02': [('AV; szellőző hát',[200],[],0,[],[]),('AV; kábelút',[200],[],0,[],[]),('Társasjáték / média',[],[],0,[],[]),('Kivehető játékdoboz',[],[],0,[],[]),('Kivehető játékdoboz',[],[],0,[],[])],
 'K-01':[('Sütő / mikro; zárt felső éléskamra',[582,1262,1800,2100],[],0,[],[2070,2350])],
 'K-02':[('Beépített hűtő + ritka felső tároló',[1870],[],0,[],[2350])],
 'K-03':[('Mosogató / hulladék / kihúzható csap tömlője',[],[],0,[],[])],
 'K-05':[('Evőeszköz / főzőeszköz / edény',[],[],3,[],[])],
 'K-06':[('Előkészítés alatti élelmiszer / eszköz',[],[],3,[],[]),('Edény / száraz készlet',[],[],3,[],[])],
 'K-07':[('Pohár / napi étkészlet',[300,600],[],0,[],[570,850]),('Tányér / száraz készlet',[300,600],[],0,[],[570,850])],
 'B62-01':[('Felső szifonos, alsó hajápolás',[],[],2,[],[])],
 'B61-01':[('Szifonos felső + alsó törölköző',[],[],2,[],[])],
 'B62-02':[('Kis pipere; nem mély flakon',[240,500],[],0,[],[])],
 'WC-01':[('Papír / tiszta tartalék',[220,440],[],0,[],[])],
 'NT-L':[('Két éjjeli fiók',[],[],2,[],[])], 'NT-R':[('Két éjjeli fiók',[],[],2,[],[])],
 'NT-64':[('Fiók + nyitott rekesz',[210],[],1,[],[])], 'NT-76':[('Fiók + nyitott rekesz',[210],[],1,[],[])]}
capacities=[];lights=[];parts=[];hardware=[]
for u in D['units']:
 u['revision']=D['revision'];u['cp3_bays']=[]
 u['drawings_cp3']=f"CP3/drawings/{u['id']}_CP3.pdf"
 u['dimension_class']='[D] tervezési méret; [H] kész hely és szerelési hézag felmérendő'
 if u['id'] not in spec:
  u['hardware']='Nincs szekrénypánt. '+('Panel: rejtett mechanikus sín, biztosított leakasztás; rögzítési alap és teher ellenőrzendő.' if u['kind']=='panel' else 'Saját szerkezet szerinti rögzítés; falra rögzítést statikailag ellenőrizni.')
  u['internal_light']='Nem zárt tároló: külön belső fény nem érintett. Kapcsolódó dekorfény az R02 világítási tervben.'
  continue
 off=0
 for bi,(purpose,shelves,rails,nd,lifts,leds) in enumerate(spec[u['id']]):
  mw=u['modules'][bi];cw=mw-36;cd=u['d']-19-8-30
  if u['id']=='K-03':cd-=100
  runner=500 if u['d']>=580 else 400 if u['d']>=480 else 350 if u['d']>=420 else 250
  if u['id'].startswith('B'):runner=400 if u['d']>=500 else 350
  dh=140 if u['h']<500 else 150
  dz=[22+i*170 for i in range(nd)] if u['h']<500 else [100+i*210 for i in range(nd)]
  if u['id'] in ['K-05','K-06']:dz=[100,320,560];dh=170
  if u['id']=='WN-01' and bi==0:dz=[80,270];dh=130
  inner=[max(0,cw-100),runner-50,dh]
  drawer_l=nd*math.prod(inner)/1e6
  if u['id'].startswith('B'):
   # One U notch in upper drawer is deducted; lower drawer remains continuous.
   drawer_l-=min(inner[0],250)*min(inner[1],200)*inner[2]/1e6
  rod_lengths=[350 if u['d']<550 else cw-(160 if z in lifts else 40) for z in rails]
  # Appliance-space shelves not counted as general storage.
  storage_shelves=shelves[:]
  if u['id']=='K-01':storage_shelves=[1800,2100]
  if u['id']=='K-02':storage_shelves=[1870]
  if u['id']=='WS-01' and bi==3:storage_shelves=[1900,2342]
  shelfarea=len(storage_shelves)*cw*cd/1e6
  b=dict(id=f"{u['id']}-B{bi+1:02}",bay=bi+1,offset=off,module_w=mw,clear_w=cw,clear_d=cd,purpose=purpose,
   shelves_mm=shelves,rails_mm=rails,lift_rails_mm=lifts,rod_lengths_mm=rod_lengths,drawers=nd,drawer_z=dz,
   drawer_inner_mm=inner,runner_mm=runner,lights_mm=leds,rail_m=sum(rod_lengths)/1000,
   shelf_m2=round(shelfarea,3),drawer_l=round(max(0,drawer_l),1),usable_depth_status='Tervi belméret; vasalat és teherpróba előtt nem gyártási méret')
  b['storage_role']='háztartás' if u['id']=='WS-01' and bi==3 else 'ruházat' if u['id'] in ['WN-01','WS-01','W52-01'] else 'vegyes / vendég / munka'
  u['cp3_bays'].append(b);capacities.append(dict(unit=u['id'],room=u['room'],**b));off+=mw
  for label,qty,pw,pd,pt in [('oldal',2,u['h'],u['d']-19,18),('alj-tető',2,cw,u['d']-19,18),('hát',1,mw-36,u['h']-36,8)]:
   parts.append(dict(unit=u['id'],bay=b['id'],part=label,qty=qty,w=pw,d=pd,t=pt,z=None,edge='látható 2 mm, belső 1 mm ABS',status='előzetes; géptorony / szifon / kábelkivágás külön, nem CNC-adat'))
  for idx,z in enumerate(shelves):parts.append(dict(unit=u['id'],bay=b['id'],part=f'S{idx+1}',qty=1,w=cw,d=cd,t=18,z=z,edge='elöl 2 mm ABS',status='előzetes szabásméret; helyszíni méret és vasalat után végleges'))
  if nd:hardware.append(dict(unit=u['id'],bay=b['id'],type='Teljes kihúzású, csillapított fiókvezető',candidate='Blum MOVENTO 40 kg; pontos rendelési készlet gyártói kiosztással',qty=nd,nominal_mm=runner,net_internal_mm=inner,proof='rendszer ismert; szerelési és fiókoldal méret még jóváhagyandó'))
  for z in lifts:hardware.append(dict(unit=u['id'],bay=b['id'],type='Gardróblift',candidate='Kesseböhmer CONERO normál 0–12 kg, 625–808 mm szélesség',qty=1,nominal_mm=cw,proof='gyártói szélességtartományba esik; pontos furat / mozgáspálya és cikkszám ajánlatban'))
  for z in leds:
   large=cw>=500
   lights.append(dict(id=f"L-{b['id']}-{z}",unit=u['id'],bay=b['id'],z=z,length=460 if large else 250,watts=2.3 if large else 1.2,
    sku='305.890.98' if large else 'Loox 3042 833.76.317, 250 mm vágat - HU beszerzés egyeztetendő',
    type='ÖVERSIDAN integrált profil + érzékelő' if large else 'Loox 24 V + opál alu profil + külön ajtóérzékelő',
    kelvin='EPREL ellenőrzésre vár; próbaminta kötelező' if large else '3000 K gyártói katalógus szerint',
    cri='nem igazolt ebben a forrásban' if large else '>90 katalógus szerint',
    source='meglévő helyiség dugaljának bemérése → hozzáférhető felső tápegység → oldalsó 24 V csatorna → polc alatti frontközeli lámpa',
    position='fronttól 45 mm; polc alsó síkján, érzékelő látómezeje szabad',
    scene='ajtónyitás: funkcionális fény; bezárás: ki; külön a Hue hangulatfénytől',
    service='felső rekeszben levehető 300×100 mm fedél, hozzáférés létráról; nem ruhával takart tápegység',
    test='80% terheléssel, sötét ruhával és dobozzal: alsó polc / címke / liftkar árnyéka ellenőrizendő'))
 u['hardware']='Belső fiók mögött 155° nulla-benyúlású pánt szükséges; többi ajtón 110° jelölt. A falvégi pánt/oldaltakaró és lift ütközése külön gyártói kapu.' if u['h']>2000 else 'Csillapított pánt / teljes kihúzás a rajzi rekesztípus szerint; darabszám és csavarozás terhelési jóváhagyással.'
 u['capacity']={k:round(sum(b[k] for b in u['cp3_bays']),3) for k in ['rail_m','shelf_m2','drawer_l']}
 u['internal_light']='Belső fény a rekeszjegyzék szerint.' if any(b['lights_mm'] for b in u['cp3_bays']) else 'Külön belső fény nem szükséges a nyitott, alacsony fiókoknál; felső helyiségfény használati próbával. Fürdőnél csak vizes zóna jóváhagyása után bővíthető.'
# Closed fronts are retained; only internal functional proposal changes.
D['interior_change_log']=[
 ['WN-01','ellentmondó 1/2 dupla rudas régi leírás','egységes 1 hosszú + 2 dupla (2 lifttel) + 1 hatfiókos','nagy ruhatárolási igény; egy polcos oszlop helyett akasztás'],
 ['WS-01','általános polc / kihúzható rúd','2 cipős + 1 táskás-fiókos + 1 háztartási oszlop','egy 559 mm széles oszlop ruhakapacitása a napi eszközöké; tulajdonosi részletdöntés'],
 ['W52-01','1380 mm-re vágott ALT052','2380 mm gardrób marad; kompakt moduláris asztal alternatíva','1000 mm gardróbveszteség elkerülése'],
 ['W53-01','általános sekély gardrób','350 mm előre kihúzható rúd + irat + 4 fiók','450 mm mélységbe nem teszünk keresztirányú hagyományos vállfát']]
groups=[]
for u in D['units']:
 ls=[l for l in lights if l['unit']==u['id']]
 for typ in ['ÖVERSIDAN','Loox']:
  subset=[l for l in ls if l['type'].startswith(typ)]
  for n in range(0,len(subset),9 if typ=='ÖVERSIDAN' else 12):
   chunk=subset[n:n+(9 if typ=='ÖVERSIDAN' else 12)]
   g=dict(id=f"PSU-{u['id']}-{typ}-{n//9+1}",unit=u['id'],fixture_ids=[l['id'] for l in chunk],watts=round(sum(l['watts'] for l in chunk),1),rating_w=30 if typ=='ÖVERSIDAN' else 20,
    sku='603.426.56 + 504.468.81' if typ=='ÖVERSIDAN' else 'Loox 24 V / 20 W illesztett driver és érzékelő; végleges SKU ajánlati kapu',
    cable='IKEA: lámpánként gyári 3,5 m vezeték, saját 3,5 m hálózati kábel; toldás csak rendszerengedéllyel',control='külön belső ajtóérzékelő; Hue-párosítás nincs állítva')
   g['load_percent']=round(g['watts']/g['rating_w']*100,1);assert g['load_percent']<=80
   groups.append(g)
inventory=[
 ['Hosszú ruha','WN-01-B01 / W52-01-B02','tervezési vállfaosztás 50–70 mm; tényleges darabszám nincs'],
 ['Rövid ruha','WN-01-B02/B03 / W52-01-B01','35–60 mm osztás; kabát külön sűrűség'],
 ['Cipők','WS-01-B01/B02 / ENT-01-B02','pár szélesség 220–300 mm; csizma alsó magas rekesz; próba nélkül nincs darabszámígéret'],
 ['Táskák','WS-01-B03 / WN-01-B04','állítva; puha támasz; polcok 32 mm raszteren'],
 ['Porszívó, vasalódeszka','WS-01-B04','célmező 559×423×1780 mm; méret nélküli tervezési sablon, nem minden gép fér be'],
 ['Vegyszer','WS-01-B04 felső zárható rekesz','gyerektől elzárt, élelmiszertől és gyógyszertől külön'],
 ['Gyógyszer','W53-01-B03 felső zárható doboz','száraz; nem fürdő; hőmérséklet készítmény szerint'],
 ['Kutya napi felszerelés','ENT-01 / ENT-02','póráz kampón; nedves törlő előbb nyitott szárítás; zárt rekeszbe szárazon'],
 ['Gyerekjáték','TV-02-B04/B05 és W52-01-B04','életkor ismeretlen; kivehető könnyű doboz, borulásgátlás szakági ellenőrzéssel'],
 ['Irat és munka','W53-01-B02/B03','A4 mappa 320–350 mm magasság; mélyebb doboz a sekély szekrénybe nem feltételezett'],
 ['Tartalék élelmiszer / ritka gép','AT8-01','napi élelmiszer továbbra is a konyhában'],
 ['Bőrönd, ritka nagy holmi','T-0-26','nehéz tárgy alsó polcra; nedvesség/por ellen felmért környezetben doboz']]
save('data/design_CP3.json',D);save('data/rekesz_kapacitas.json',capacities);save('data/belso_vilagitas.json',dict(fixtures=lights,drivers=groups));save('data/vasalat.json',hardware);save('data/elozetes_szabaslista.json',parts);save('data/targyleltar_forgatokonyv.json',inventory)
for name,rows in [('kapacitas',capacities),('vilagitas',lights),('vasalat',hardware),('szabaslista',parts)]:
 with (O/'data'/f'{name}.csv').open('w',newline='') as f:
  keys=list(dict.fromkeys(k for r in rows for k in r));wr=csv.DictWriter(f,fieldnames=keys);wr.writeheader();wr.writerows(rows)
summary={}
for c in capacities:
 if c['unit'] in ['WN-01','WS-01','W52-01','W53-01']:
  a=summary.setdefault(c['room'],dict(rail_m=0,shelf_m2=0,drawer_l=0))
  for k in a:a[k]=round(a[k]+c[k],3)
save('data/kapacitas_osszesito.json',summary)
print(json.dumps(dict(units=len(D['units']),bays=len(capacities),lights=len(lights),drivers=len(groups),capacity=summary),ensure_ascii=False))

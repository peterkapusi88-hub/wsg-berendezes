from pathlib import Path
import json,copy
P=Path(__file__).resolve().parents[1];O=P/'CP3';B=json.loads((P/'data/workbook_readback_before_CP3.json').read_text());D=json.loads((O/'data/design_CP3.json').read_text());L=json.loads((O/'data/belso_vilagitas.json').read_text())
old={r[2]:r for r in B['Elemregiszter'][1:]};patches={};new=[];build=[]
def change(code,price,eco,note,**fields):
 fields.update(Q=price,AG=eco,AF=note,AI=note,X='2026-10-27',AY=.8,AZ=1.4)
 patches[code]=fields
def interior(uid):
 u=next(u for u in D['units'] if u['id']==uid);bs=u['cp3_bays'];dr=sum(b['drawers'] for b in bs);sh=sum(len(b['shelves_mm']) for b in bs);ro=sum(len(b['rails_mm'])-len(b['lift_rails_mm']) for b in bs);li=sum(len(b['lift_rails_mm']) for b in bs)
 rows=[['fiók (doboz + teljes kihúzású vasalat)',dr,28000],['állítható polc + tartó',sh,6500],['fix / előre kihúzható rúd',ro,7500],['CONERO normál lift 12 kg',li,95000],['belső fiókos ajtó pántfelár',sum(b['drawers']>0 for b in bs),12000]]
 for name,n,p in rows:
  if n:build.append(dict(unit=uid,item=name,qty=n,unit_huf=p,total=n*p,status='előirányzat, nem beszállítói ajánlat',basis='CP3 belső kiosztás; szerelés meglévő külön sorban'))
 return sum(n*p for _,n,p in rows)
master=interior('WN-01')+interior('WS-01');w52=interior('W52-01');w53=interior('W53-01')
change('KI-050',master,master-4*(28000-6500),'A 190 000 Ft régi teljes belső csomag helyett a CP3 tételes fiók/polc/rúd/lift összege. Gazdaságos: 4 fiók helyett 4 polc; 86 000 Ft megtakarítás, napi áttekinthetőség romlik.',H='Északi és déli gardróbbelsők, 2 lifttel',W='CP3/data/koltseg_bontas.json',AN='WN-01; WS-01')
change('KI-060',190000+w52,190000+w52,'Teljes korpusz + CP3 belső új előirányzata: 190 000 Ft korpusz és tételes belső; régi 150 000 Ft kiváltva, nem hozzáadva. Front és szerelés továbbra KI-061.',W='CP3/data/koltseg_bontas.json')
change('KI-072',160000+w53,160000+w53,'Teljes sekély korpusz 160 000 Ft + CP3 belső; régi 150 000 Ft kiváltva. Front és szerelés KI-073.',W='CP3/data/koltseg_bontas.json')
change('KI-025',42990,42990,'IKEA ÄLMAREN fekete kihúzható csap. Íves forma eltér a render szögletes csapjától. Tömlő és hulladéktároló együtt próbálandó. Szerelés KI-027.',H='ÄLMAREN fekete kihúzható konyhai csap',I='IKEA',J='506.034.99',K='https://www.ikea.com/hu/hu/p/aelmaren-konyhai-keverocsap-kihuzhato-veggel-fekete-50603499/',V='ellenőrzött webshopár',W='IKEA HU termékoldal; 2026-10-26',X='2026-10-26',L='H360; 35 mm furat; max 50 mm munkalap',AY=1,AZ=1.15)
# Retain original code as installation/service only; hardware split into new rows.
light_install=len(L['fixtures'])*1500+35000
change('KI-119',light_install,light_install,f"Régi 55 000 Ft világítási csomag teljesen kiváltva. Ez csak {len(L['fixtures'])} lámpa és {len(L['drivers'])} driver vezetése, rögzítése és ajtóérzékelő próbája; termékek KI-CP3-L01...L04. Általános villamos munkát KI-107 nem számlázzuk újra.",H='Szekrénybelső fények szerelése és terhelt próbája',W=f"{len(L['fixtures'])} db × 1 500 Ft + 35 000 Ft mérés/beállítás előirányzat")
def add(code,room,name,qty,price,eco=None,sku='',url='',dims='',status='becslés',install=0,shipping=0,note='',structure='',trade='bútor',low=.8,high=1.4):
 row=[None]*54
 vals={'A':'A-902','B':room,'C':code,'D':'CP3 manifest','E':'CP3 bővítés; nincs baseline duplikáció','F':'megvalósítás','G':trade,'H':name,'I':name.split(' ')[0],'J':sku or 'AJÁNLATRA VÁR','K':url,'L':dims,'M':'fehér / grafit a terv szerint','N':'termék és rajz szerint','O':qty,'P':'db','Q':price,'R':shipping,'S':install,'T':0,'V':status,'W':url or 'CP3 tervezői előirányzat, tételes alap a megjegyzésben','X':'2026-10-26' if url else '2026-10-27','Y':'szállítás / átfutás nincs visszaigazolva','Z':'A','AA':note,'AB':'tulajdonosi / szakági jóváhagyásra vár','AC':'nem rendelt','AD':'tulajdonos + szaktervező / gyártó','AE':'ár és beépítés külön ellenőrizendő','AF':note,'AG':price if eco is None else eco,'AI':'azonos műszaki tartalom' if eco is None else note,'AJ':'forgalmazói feltétel ajánlatban','AK':'magyar címre nincs visszaigazolva','AL':'lásd CP3 alternatívák','AM':'nincs önkényesen választva','AN':structure,'AO':'CP3/drawings','AP':'CP3_'+structure,'AQ':'késztermék' if sku else 'egyedi / szakmunka','AR':'gyártói befoglaló / tervi hely; felmérés vár','AS':'HUF','AT':1,'AU':'vásárlás előtt újraellenőrizendő','AV':'közös logisztikai sor, ha nincs itt külön','AW':'külön szerelési / segédanyag sor','AX':3,'AY':low,'AZ':high}
 def ci(s):
  k=0
  for c in s:k=k*26+ord(c)-64
  return k-1
 for k,v in vals.items():row[ci(k)]=v
 new.append(row)
ni=sum(l['type'].startswith('ÖVERSIDAN') for l in L['fixtures']);ng=sum(g['sku'].startswith('603.') for g in L['drivers']);nl=len(L['fixtures'])-ni
add('KI-CP3-L01','teljes lakás','IKEA ÖVERSIDAN 46 cm',ni,5490,sku='305.890.98',url='https://www.ikea.com/hu/hu/p/oeversidan-led-es-gardrobvilagitas-erzekelo-fenyereje-szabh-soetetszuerke-30589098/',dims='460 mm; 2,3 W; 140 lm; 24 V',status='ellenőrzött webshopár',trade='világítás',structure='WN-01;WS-01;W52-01;W53-01;K-01;K-02;K-07',low=1,high=1.15,note='Lámpánként gyári kábel és profil. CRI / Kelvin adat még nem igazolt; minta szükséges.')
add('KI-CP3-L02','teljes lakás','IKEA TRÅDFRI 30 W tápegység',ng,3990,sku='603.426.56',url='https://www.ikea.com/hu/hu/p/tradfri-tapegyseg-okos-eszkoez-szuerke-60342656/',dims='285×55×18 mm; 230/24 V; max 9 kimenet',status='ellenőrzött webshopár',trade='világítás',structure='PSU',low=1,high=1.15,note='Önálló belső funkcionális rendszer; nincs állított Hue-kompatibilitás.')
add('KI-CP3-L03','teljes lakás','IKEA FÖRNIMMA hálózati kábel',ng,2990,sku='504.468.81',url='https://www.ikea.com/hu/hu/p/foernimma-vezetek-50446881/',dims='3,5 m',status='ellenőrzött webshopár',trade='világítás',structure='PSU',low=1,high=1.15)
add('KI-CP3-L04','teljes lakás','Loox keskeny rekeszek teljes belső fénye',nl,11500,trade='világítás',structure='TV-01;ENT-01',note=f'{nl}×250 mm szalag + opál profil + érzékelő / csatlakozás. Összesen {len(L["drivers"])-ng} db 24 V driver költsége a készletbe osztva; nem kerül külön még egyszer hozzá. Pontos HU készlet és cikkszám ajánlatra vár.')
add('KI-CP3-S01','AT8-01','IKEA JONAXEL polc',2,23000,sku='504.199.72',url='https://www.ikea.com/hu/hu/p/jonaxel-polcos-elem-feher-50419972/',dims='800×380×1600; 4 polc; 25 kg/polc',status='ellenőrzött webshopár',structure='AT-R1;AT-R2',low=1,high=1.15,note='Fehér készpolc; fali borulásgátlás. R03 kép 2 db-ot tartalmaz.')
add('KI-CP3-S02','T-0-26','IKEA BROR polc',2,47500,sku='s59619405',url='https://www.ikea.com/hu/hu/p/bror-polcos-elem-fekete-s59619405/',dims='850×550×1900',status='ellenőrzött webshopár',structure='T-R1;T-R2',low=1,high=1.15,note='Fekete acél a világos helyiségben; polcszám és címkés teherbírás a rendelési készlettel egyeztetendő.')
add('KI-CP3-S03','AT8-01 / T-0-26','Tárolók szállítás, összeszerelés, rögzítés',1,90000,trade='logisztika',structure='AT8-01;T-0-26',note='4 polc összeállítás 40 000; 4 rögzítés alapanyag / munka 20 000; külön szállítás / felhordás 30 000 Ft. Aljzat/fal fúrás engedélye ellenőrizendő.')
add('KI-CP3-S04','AT8-01 / T-0-26','Tárolódobozok és címkézés',12,4000,trade='kiegészítő',structure='AT-R1;AT-R2;T-R1;T-R2',note='12 db hozzáférhető, emelhető doboz előirányzat; pontos típus a rekeszhez választandó. Nehéz gép alul.')
add('KI-CP3-F01','AT8-01','Liebherr második fagyasztó',1,289990,sku='FNd 4625 / GN46Vd25 egyeztetendő',url='https://www.liebherr.com/hu-hu/p/fnd-4625-3121280',dims='597×675×1455; 199 l; 37 dB',status='gyártói tájékoztató ár, SKU egyeztetésre vár',structure='AT-FR',low=1,high=1.2,note='Külön kimutatott opcionális vásárlás; a fő, fagyasztót mutató forgatókönyv tartalmazza. A termékoldal megnevezése eltér az URL-től: pontos EAN, klíma és nyitási hely kell.')
add('KI-CP3-F02','AT8-01','Fagyasztó szállítás és villamos ellenőrzés',1,45000,structure='AT-FR',trade='villamosság',note='Szállítás/felhordás25 000; meglévő két tervi dugalj és áramkör ellenőrzése20 000. Új áramkör nincs igazolva vagy benne.')
add('KI-CP3-B01','06.2','Blum AMPEROS AC fiókáram jelölt készlet',1,145000,structure='B62-01',trade='villamosság',note='230 V EU rendszer ESS.B01FA.2 jelölt, illesztett kábelvezetéssel és 25 000 Ft szereléssel együtt. Hazai ajánlat és rövid mosdófiók kompatibilitás nincs igazolva. Alternatíva: fix hozzáférhető konnektor 40 000 Ft; nincs hosszabbító a mozgó fiókban.',eco=40000)
add('KI-CP3-H01','06.1','Háztartási kihúzható csap jelölt és bekötés',1,70000,structure='H-TAP',trade='vízszerelés',note='Csak igazolt meglévő háztartási mosdó / csatlakozás után. Nincs új mosdó vagy kitalált vizes hely. Csap50 000 + bekötés20 000 előirányzat; műszaki hely még nyitott.')
add('KI-CP3-D01','01 / 05.1 / 05.2','Kutya, játék és zárható rekesz kiegészítők',1,65000,structure='ENT-02;WS-01;W52-01',trade='bútor',note='2 kivehető játékdoboz12 000; nedves/száraz tálca8 000; 3 kampó6 000; zárható vegyszer/gyógyszer elválasztás24 000; állítható géptartó15 000. Nem becsült csavardarabszám.')
# The dimensioned custom carcass is not an unverified PAX kit.
for code,uid in [('KI-048','WN-01'),('KI-049','WS-01')]:
 patches.setdefault(code,{}).update(H=('Északi' if code=='KI-048' else 'Déli')+' egyedi gardróbkorpusz CP3',I='egyedi asztalos gyártás',J=uid,K='',AQ='egyedi gyártás',AA='Egyedi 18 mm korpusz; PAX termékazonosság és beférés nincs állítva.',AF='CP3 egyedi korpuszra pontosítva. A korábbi korpusz-előirányzat változatlan becslés; ajánlat szükséges.',AR='CP3 tervi befoglaló, kész helyszíni méret és szerelési hézag ellenőrizendő.')
for code in old:
 us=[u for u in D['units'] if code in u['cost']]
 if us:patches.setdefault(code,{}).update(AN='; '.join(u['id'] for u in us),AO='; '.join(u['drawings_cp3'] for u in us),AP='; '.join('CP3_'+u['id'] for u in us),D='CP3/render_handoff/manifest_CP3.json')
# Snapshot calculation, independent of Excel formula engine.
rows=copy.deepcopy(B['Elemregiszter'][1:])
def ci(s):
 n=0
 for c in s:n=n*26+ord(c)-64
 return n-1
for r in rows:
 for k,v in patches.get(r[2],{}).items():r[ci(k)]=v
rows+=new
def total(r,eco=False):return r[14]*r[32 if eco else 16]+sum(float(r[i] or 0) for i in [17,18,19])
main=sum(total(r) for r in rows);eco=sum(total(r,True) for r in rows)
snap=dict(main=main,economy=eco,low=round(sum(total(r)*r[50] for r in rows)),high=round(sum(total(r)*r[51] for r in rows)),budget=18000000,reserve=2000000,reserve_used=0,
 verified=sum(total(r) for r in rows if r[21]=='ellenőrzött webshopár'),quotes=0,rows=len(rows),r02=20554190,delta=main-20554190,freezer_with_service=334990,without_freezer=main-334990,status='Teljes projekt-előirányzat, nem fix ajánlat; gazdaságos változat tulajdonosi döntésre vár.')
(O/'data/cost_patch.json').write_text(json.dumps(dict(patches=patches,new_rows=new),ensure_ascii=False,indent=2));(O/'data/koltseg_bontas.json').write_text(json.dumps(build,ensure_ascii=False,indent=2));(O/'data/cost_snapshot_CP3.json').write_text(json.dumps(snap,ensure_ascii=False,indent=2));print(json.dumps(snap,ensure_ascii=False))

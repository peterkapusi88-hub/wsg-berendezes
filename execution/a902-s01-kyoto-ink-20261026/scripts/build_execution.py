from pathlib import Path
import json,csv,math,hashlib,shutil
P=Path(__file__).resolve().parents[1]
G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
R=json.loads((P/'data/elemek.json').read_text())
REV='KI-V33-R02';DATE='2026-10-26'
def save(name,x): (P/name).parent.mkdir(parents=True,exist_ok=True);(P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2))
def row(n):return R[n-1]
units=[]
def unit(id,name,room,cost,w,d,h,xy,rot=0,z=0,mods=None,kind='cabinet',notes='',shelves=4,drawers=0,front='kréta matt',opening=600):
 u=dict(id=id,name=name,room=room,cost=[f'KI-{n:03}' for n in cost],w=w,d=d,h=h,x=xy[0],y=xy[1],z=z,rot=rot,modules=mods or [w],kind=kind,notes=notes,shelves=shelves,drawers=drawers,front=front,opening=opening,revision=REV,date=DATE,status='FELMÉRÉSRE ÉS GYÁRTÓI EGYEZTETÉSRE VÁRÓ AJÁNLATI TERV',dimension_source='geometry_lock_A902_v2b: terv szerinti falsíkok + R02 tervezési méret; helyszínen nem mért',material='18 mm laminált korpusz; 19 mm MDF front; 8 mm hátlap',edge='látható él 2 mm ABS, belső él 1 mm; vizes élek PUR/gyártói vízzárás',grain='egyszínű: nincs erezet; textil/nyomat: függőleges folytonosság',hardware='csillapított 110° pánt; teljes kihúzású fiók; pontos típusszám és teherbírás gyártói kiosztás szerint',handle='matt fekete fogásprofil / hosszú fogantyú a nézet szerint',plinth='80 mm visszahúzott lábazat; falibútornál nincs',clearance='3 mm frontrés; 20 mm szerelési oldaltakaró tervezési minimum; kész falsíkhoz felmérendő',service='levehető hát/szervizpanel; kötés és meghajtó nem lezárható véglegesen')
 units.append(u);return u
# Kitchen: real 2.10 m galley. West and east worktops 620 mm => 860 mm clear.
unit('K-01','Sütő és mikro torony','02',[8,9,10,13,15],600,600,2400,(9.15,1.37),mods=[600],notes='Sütőnyílás 564×590×550; mikro 564×365×min300. Sütő alja 600; mikro alja 1280 mm. Gyári átszellőzés és ajtónyitás kötelező. Felső polc 1800 mm. D08/D09 hozzáférés.',shelves=2)
unit('K-02','Hűtőtorony és felső tároló','02',[8,9,10,13,15],600,620,2400,(9.93,3.43),rot=90,notes='KIN86VSE0 1772×541×548; 1780×564×550 tervezési niche. Alsó/felső szellőzés gyári szerelési rajz szerint, nem lezárt lábazat. D13 marad.',shelves=1)
unit('K-03','Mosogató alsó','02',[6,9,10,15],800,620,900,(9.93,2.57),rot=90,notes='700×500 mosogató cél; kivágás csak végleges sablonról. Szifon mögött 100 mm szerelősáv; kivehető tálca. Nem két teljes mélységű fiók.',shelves=0,front='grafit matt')
unit('K-04','Mosogatógép helye és frontja','02',[6,9,13,15],600,620,900,(9.93,1.97),rot=90,kind='appliance',notes='600 mm beépítési nyílás; gép nincs duplán a korpuszárban. A lábazat és front geometria a kiválasztott gép ajtópályájával egyeztetendő.',shelves=0,front='grafit matt')
unit('K-05','Főzőlap alatti fiókos','02',[6,9,10,15],600,620,900,(8.47,2.42),rot=90,notes='PUE611BB5E kivágás 560×490–500, test 592×522×51 mm; szellőzés és hővédő elválasztó a gyári rajz szerint. A 860 mm folyosó nyitott fióknál nem átjáró.',shelves=0,drawers=3,front='grafit matt')
unit('K-06','Előkészítő fiókos','02',[6,9,10,15],1000,620,900,(8.47,3.02),rot=90,mods=[500,500],shelves=0,drawers=6,front='grafit matt',notes='2×500 mm modul; evőeszköz, edény, nehéz kisgépek. Pult 38 mm F274 család; oldalt 20 mm takarás.')
unit('K-07','Mosogató feletti felsők','02',[7,9,10,15],1400,350,900,(10.18,1.97),rot=90,z=1.45,mods=[600,800],notes='Alja 1450 mm tervezési szint; felnyitó helyett nyíló front. FL01 és pultfény szerelősáv szabad; felfüggesztő sín falanyaghoz méretezendő.',shelves=2)
unit('K-08','Munkalapok és hátfal','02',[11,12,14],2060,620,38,(9.93,1.97),rot=90,z=.9,kind='panel',notes='Keleti pult névleges 1460 + nyugati 1600 mm: külön darabok; 38 mm laminált F274 dekorcsalád, pontos felület mintáról. A rajz befoglaló anyagvizsgálat, a hűtőt nem fedi pult. Nettó pult 1.897 m², rendelés 2.18 m² (15%). Hátfal 1.4×0.55=0.77 m² + végek; nyitott elszívóút.',shelves=0,front='F274 betonhatás')
# TV and art
unit('TV-01','W01 torony','04',[30,32],700,400,2480,(3.71,7.3),rot=90,z=.4,mods=[350,350],notes='Két nyíló front, folyamatos tusmotívum a szomszéd panellel. 5 polcszint, hosszú fekete fogantyú. Ajtók előtt 700 mm használati hely.',front='textilhatású kréta + tusnyomat',opening=400)
unit('TV-02','W01 alsó médiafal','04',[31,32],3300,400,400,(3.71,4.7),rot=90,z=.15,mods=[600,600,600,750,750],notes='Öt nyíló front, 3 mm rések; TV-01 ráépítése külön falrögzítéssel. Bal/szélső szervizmező 300×200. Router szellőzése 20 mm hátsó rés, táp nem zárt fiókban.',shelves=1,front='grafit matt',opening=400)
unit('TV-03','W01 TV hordozó és dekorpanel','04',[30,32,34,114],2600,36,2330,(3.674,4.7),rot=90,z=.55,mods=[650,650,650,650],kind='panel',notes='Négy 650-es mező; TV 65 col külön falra rögzített konzolon. A dekorpanel nem teherhordó. Kábelút 40×60 mm javasolt, D16/D17/G pontok előtt levehető mező. Felső LED 2600 mm és függőleges 2330 mm külön profil.',shelves=0,front='greige textil + nyomtatott tus')
unit('ART-02','W02 teljes magasságú művészeti mező','04',[123,131,132,133],2100,36,2880,(5.2,4.052),mods=[700,700,700],kind='panel',notes='3×700 mm hordozó, képfolytonos illesztés. Végleges befoglaló csak kapcsoló/termosztát helyszíni felmérésével. 100–150 mm tiszta kezelősáv. Nem megy ajtóra, kapcsolóra vagy a sarkon át új tusmotívummal.',shelves=0,front='greige textilszövés + fekete tus')
unit('ART-07','W07 visszaforduló csendes felület','07',[124,127,128],1530,18,2880,(3.67,3.96),kind='panel',notes='Max18 mm rétegrend; K25–K27 és D46 kezelhető. Nyomat nélkül folytatott alapszín. Sarkon 3 mm árnyékrés, nem vastag relief.',shelves=0,front='greige vlies')
unit('CF-01','Grafit dohányzó dobozasztal','04',[37],700,450,350,(4.48,5.55),kind='table',notes='V3.3 prompt szerinti 700×450×350 mm; 18 mm hordozó + matt laminát; 2 mm ABS; rejtett 20 mm talp, filc. Tervezett tömeg/hajlás gyártóval ellenőrizendő.',shelves=0,front='grafit matt',opening=0)
unit('ST-01','Grafit mellékkocka','04',[38],300,300,450,(6.0,4.42),kind='table',notes='300×300×450 mm; azonos grafit laminát és él mint CF-01.',shelves=0,front='grafit matt',opening=0)
# Master, additional rooms and entrance
unit('WN-01','Északi gardrób','05.1',[48,50,51,52],2920,600,2840,(.05,8.3),mods=[730]*4,notes='3020 mm tervfülke: 50+2920+50 mm névleges. Egyedi korpusz; PAX 2994 mm helyett szerelhetőbb ajánlati változat. 1 hosszú akasztós, 1 dupla akasztós, 2 polcos/fiókos modul. Front felső vízszintes osztás 2360 mm-nél.',shelves=4,drawers=4,front='kréta + folytonos tusnyomat',opening=750)
unit('WS-01','Déli sekély gardrób','05.1',[49,50,51,52],2380,480,2840,(.02,3.47),mods=[595]*4,notes='2420 mm fülke, 20 mm kétoldali hézag. 480 mm teljes mélység miatt hajtogatott ruhák + keresztirányú kihúzható akasztó; normál 580 mm PAX nem bizonyított. 4 modul, 3 polcos, 1 kihúzható.',shelves=5,drawers=2,front='kréta matt',opening=600)
unit('HB-01','Kárpitozott aszimmetrikus fejvég','05.1',[46,47,118],2700,60,1500,(3.49,5.05),rot=90,mods=[1800,900],kind='upholstery',notes='Két külön levehető panel; 18 mm rétegelt lemez, 30 mm hab, vatta és textil. Bal mező taupe, jobb grafit; tetején alu/opal LED profil, hozzáférhető tápegység az éjjeliből. Nincs új grafika felette.',shelves=0,front='taupe/grafit kárpit')
for a,y in [('L',5.12),('R',7.35)]:unit('NT-'+a,'Grafit éjjeli '+a,'05.1',[53],300,420,450,(3.07,y),rot=90,drawers=2,shelves=0,notes='2×210 mm névleges fiókelőlap; 350 mm sín cél, végleges vasalatra szabás. Kábel átvezető a hátlapon; D21/D23 hozzáférés.',front='grafit matt',opening=400)
unit('W52-01','05.2 gardrób','05.2',[60,61],2380,600,2840,(.02,2.72),mods=[595]*4,notes='2 akasztós + 2 polcos; 4 fiók. 2380 mm egyedi szélesség, 20 mm kétoldali takarás. Fehér/kréta alapon egy keskeny grafit mező.',drawers=4,front='kréta/grafit',opening=600)
unit('W53-01','05.3 gardrób','05.3',[72,73],1800,600,2840,(13.73,6.21),rot=90,mods=[600]*3,notes='Keleti fal déli nyitási tartománya és fürdőajtó nem takarható. 2 akasztós, 1 polcos 3 fiókkal. Elhelyezés vizsgálat alatt.',drawers=3,front='kréta/grafit',opening=600)
unit('ENT-01','Előtéri kabát és cipő','01',[82,85],860,540,2840,(8.39,1.37),rot=90,mods=[430,430],notes='1000 mm hosszú fülke; 860 mm bútor + takarás; keresztirányú akasztó, 5 cipőpolc, felső szezonális rekesz. Kaputelefon/elosztó nem takarható.',opening=450)
unit('ENT-02','Előtéri pad és fogas','01',[83],800,350,450,(5.65,.15),kind='bench',notes='18 mm korpusz, 30 mm kárpitozott ülőlap. 800×1200 fogaspanel falra, rögzítés feltárás után.',shelves=1,opening=0,front='grafit/taupe')
unit('HALL-01','Közlekedő keskeny lerakó','07',[86],600,150,180,(4.2,3.78),z=.8,kind='shelf',notes='150 mm mély, csak holttérben; a 900 mm fő közlekedést vagy kapcsolókat érintő elhelyezés elvetendő.',shelves=0,opening=0,front='grafit matt')
unit('B62-01','06.2 integrált mosdóbútor','06.2',[92,95,96],900,500,350,(15.88,6.02),rot=90,z=.5,drawers=2,shelves=0,notes='900×500×350 mm feltételes szélesség; mosdóperem 850 mm cél. Szifon körül 250×200 mm U-kivágás csak szerelési sablonból. Meglévő Smyle kerámia nem vágható. Szükség esetén beépíthető mosdó külön KI-095 kerettel.',front='vízálló grafit',opening=450)
unit('B62-02','06.2 oldalsó zárt tároló','06.2',[94],300,200,800,(16.18,7.02),rot=90,z=1.05,notes='Nedvességálló zárt szekrény; zuhanyzóna és tükör oldalán felmérendő; 3 polc, rejtett pánt.',shelves=3,front='vízálló grafit',opening=300)
unit('B61-01','06.1 mosdó alatti tároló','06.1',[98],600,450,350,(5.0,1.25),rot=90,z=.45,drawers=2,shelves=0,notes='Szifonkivágás sablon szerint; meglévő medence és szerelvény marad. Az alsó fiók sekélyebb; vizes illesztések teljesen lezárva.',front='vízálló grafit',opening=400)
unit('WC-01','WC tároló és tükör','08',[101],450,180,700,(5.34,2.85),rot=90,z=1.1,notes='Aknaajtó, vízóra és szellőző előtt nem szerelhető. Rejtett vízálló hát és biztonsági fóliás tükör; 2 polc.',shelves=2,opening=300,front='kréta matt')
# Product proposal geometry, explicit dimensions separate from detailed manufacturer mesh.
items=[]
def item(id,room,name,sku,w,d,h,x,y,rot=0,z=0,kind='product',proof='tervezési befoglaló, gyártó igazolandó'):
 items.append(dict(id=id,room=room,name=name,sku=sku,w=w,d=d,h=h,x=x,y=y,rot=rot,z=z,kind=kind,proof=proof))
item('KI-036','04','Lennon right L','DEQ21WES12329-168260',1800,2380,680,4.87,4.77,kind='sofa',proof='gyártói befoglaló; kar/modul mesh és kéz iránya még igazolandó')
item('KI-028','03','Toni160','DEQ19WES60483-225182',900,1600,750,8.0,5.4,kind='oval',proof='CP1a termékoldal')
for i,(x,y,w,d) in enumerate([(7.42,5.57,530,550),(7.42,6.26,530,550),(8.95,5.57,530,550),(8.95,6.26,530,550),(8.17,4.82,550,530),(8.17,7.05,550,530)]):item('KI-029-'+str(i+1),'03','Eamy','C0100003HE12',w,d,750,x,y,proof='CP1a termékoldal; ülő és kihúzott állapot külön ellenőrzendő')
item('KI-043','05.1','NORDLI','203.498.53',2020,1800,300,1.47,5.5,proof='IKEA gyári méret, 180×202×30 cm elforgatva')
item('KI-058','05.2','SLATTUM','405.712.48',2060,1640,850,1.5,.3,proof='IKEA termékoldal 2026-10-26')
item('KI-070','05.3','SLATTUM','405.712.48',1640,2060,850,11.8,4.16,proof='IKEA termékoldal 2026-10-26; 160 cm matrac a korábbi 180 cm proxy helyett, tulajdonosi döntés')
item('KI-062','05.2','Egyedi kompakt íróasztal','DS52',1000,450,750,.05,.35,proof='R02 tervezési méret; TROTTEN 120×70 nem fér a kívánt közlekedéssel')
item('KI-074','05.3','TROTTEN kőris/fehér','196.219.19',1200,700,750,11.2,7.25,proof='IKEA termékoldal')
item('KI-063','05.2','FLINTAN','704.922.02',710,710,1140,.6,.65,proof='IKEA termékoldal, használati hely vizsgálandó')
item('KI-075','05.3','FLINTAN','704.922.02',710,710,1140,11.45,6.5,proof='IKEA termékoldal')
unit('DS52','05.2 kompakt íróasztal','05.2',[62],1000,450,750,(.05,.35),kind='table',notes='A 1200×700 TROTTEN túl mély az ágy melletti használati helyhez. 1000×450×750 matt grafit asztal, 18+18 mm duplázott lap, acél láb; ergonómia ülőpróbával.',shelves=0,front='grafit matt',opening=0)
for n,room,x,y in [(64,'05.2',3.1,2.02),(76,'05.3',13.47,4.2)]:unit('NT-'+str(n),'Kisebb háló éjjeli',room,[n],350,350,450,(x,y),drawers=1,shelves=1,front='grafit matt',opening=300)
item('KI-087','06.1','Mosó-szárító torony hely','PENDING',600,650,1800,3.82,.1,proof='foglalási tér, termék és vízkiállás még igazolandó')
item('KI-091','06.2','100 cm fix zuhanyüveg','GL-01',8,1000,2000,15.35,7.02,kind='glass',proof='1000 mm tulajdonosi igény; szakági vastagság és méret még jóváhagyandó')
# Terrace all zones: only hardscape, no green roof loading.
item('KI-136','09','Jakuzzi hely és szerviz','PENDING',2200,2200,900,4.0,9.3,z=-.15,proof='tervezési helyfoglaló, konkrét kád és statika nincs igazolva')
item('KI-138','10','Kültéri grafit lounge kanapé','RFQ-OUT-01',2200,850,750,13.7,11.35,z=-.15)
for i,x in enumerate([12.0,15.3]):item('KI-139-'+str(i+1),'10','Kültéri lounge fotel','RFQ-OUT-02',750,800,750,x,10.1,z=-.15)
item('KI-140','10','Kültéri alacsony asztal','RFQ-OUT-03',800,600,350,14.0,10.25,z=-.15)
item('KI-141','09','Kültéri étkezőasztal','RFQ-OUT-04',1800,900,750,6.9,10.8,z=-.15)
for i,(x,y) in enumerate([(6.85,10.15),(7.5,10.15),(8.15,10.15),(6.85,11.75),(7.5,11.75),(8.15,11.75)]):item('KI-142-'+str(i+1),'09','Kültéri szék','RFQ-OUT-05',550,550,800,x,y,z=-.15)
for i,x in enumerate([9.4,10.5]):item('KI-143-'+str(i+1),'WPC','Napozó','RFQ-OUT-06',650,1950,350,x,9.4,z=.47)
item('KI-147','13','Párnatároló','RFQ-OUT-07',900,450,550,-1.85,3.85,z=-.15)
# Cost links and specs; unchanged existing manual values remain authoritative.
for r in R:
 related=[u for u in units if r['elemkod'] in u['cost']];r['szerkezet']='; '.join(u['id'] for u in related) or r['elemkod'];r['rajz']='; '.join('drawings/'+u['id']+'.pdf' for u in related) or 'drawings/P-01_alaprajz.pdf';r['blender_objektum']='; '.join('KI_'+u['id'] for u in related) or 'KI_'+r['elemkod'];r['penznem']='HUF';r['arfolyam']=1;r['ar_ervenyesseg']='nincs visszaigazolt ajánlati érvényesség';r['meret_statusz']='felmérés/gyártói rajz szükséges';r['felhordas']='KI-151 központi keret; daruzás KI-137';r['szakmai_aproanyag']='KI-014 asztalos / KI-106 villamos / KI-026 és KI-096 víz / KI-127 fal';r['min_factor']=.85;r['max_factor']=1.3;r['hatarido_het']=4 if related else 6
 if related:r['meret']='; '.join(f"{u['id']}: {u['w']}×{u['d']}×{u['h']} mm" for u in related);r['meret_statusz']='R02 méretezett ajánlati terv; nem helyszíni méret';r['kesz_egyedi']='egyedi gyártás'
 else:r['kesz_egyedi']='késztermék / szakági munka'
 if r['arstatusz']=='ellenőrzött webshopár':r['min_factor']=1;r['max_factor']=1.12
 if r['elemkod'] in ['KI-136','KI-137','KI-146','KI-159']:r['max_factor']=1.6
# Concrete choices: product price and separate component allowance; no inflated verified subtotal.
products=[]
def product(n,name,sku,dim,price,url,note,verified=True,extra=0):
 r=row(n);r.update(megnevezes=name,marka='IKEA' if 'ikea' in url else 'Bosch',sku=sku,meret=dim,link=url,egysegar=price,gazdasagos=price,egyeb=extra,arstatusz='ellenőrzött webshopár' if verified and extra==0 else 'előzetes becslés',arforras=url,datum=DATE,egyezes=note,meret_statusz='gyártói termékoldal/adatlap',szallithatosag='magyar címre és darabszámra nem visszaigazolt',min_factor=1 if verified else .85,max_factor=1.12 if verified else 1.3)
 products.append(dict(elem=r['elemkod'],name=name,sku=sku,dimensions=dim,price_huf=price,additional_allowance_huf=extra,price_evidence='webes termékoldal, nem lekötött ár' if verified else 'tervezői becslés; gyári méret ellenőrizve',url=url,checked=DATE,deviation=note,availability='címre nem igazolt',product_photo='termékoldal képei; letölthető gyártói referencia még nincs csomagolva'))
product(58,'SLATTUM Vissle sötétszürke 160×200','405.712.48','1640×2060×850 mm',54990,'https://www.ikea.com/hu/hu/p/slattum-karpitozott-agykeret-vissle-soetetszuerke-40571248/','Új 05.2 terv; ágyrács része a csomagnak. Alacsonyabb, egyszerűbb varrású, mint master.')
product(70,'SLATTUM Vissle sötétszürke 160×200','405.712.48','1640×2060×850 mm',54990,'https://www.ikea.com/hu/hu/p/slattum-karpitozott-agykeret-vissle-soetetszuerke-40571248/','05.3: 160 cm fekvőfelület a forrásproxy 180 cm helyett; NEM jóváhagyott funkcióváltás.')
product(74,'TROTTEN kőris hatású/fehér','196.219.19','1200×700×750 mm',39990,'https://www.ikea.com/hu/hu/p/trotten-iroasztal-koris-hatasu-feher-s19621919/','05.3 új terv; világos fa az étkezővel rokon, fehér fém láb eltér a grafittól.')
for n in [63,75]:product(n,'FLINTAN bézs karfa nélkül','704.922.02','710×710×max1140 mm',24990,'https://www.ikea.com/hu/hu/p/flintan-irodai-szek-bezs-70492202/','Működő munkaszék; hálós háttámla funkcionális, nem Eamy sziluett.')
product(117,'2×FADO fehér opálgömb + 2×Hue E27','800.963.72 + Hue E27 variáns PENDING','Ø250×240 mm; 2 darab',11980,'https://www.ikea.com/hu/hu/p/fado-asztali-lampa-feher-80096372/','2×5990 Ft igazolt test + 24000 Ft becsült Hue izzópár. A célképnél nagyobb gömb, nincs magas fém talp. Beférés próba kötelező.',extra=24000)
product(16,'Bosch HBA534EB3 fekete sütő','HBA534EB3','594×548×595 mm; niche 560–568×550×585–595',180000,'https://media3.bsh-group.com/Documents/specsheet/en-MT/HBA534EB3.pdf','Fekete üveg az egyeztetett toronyban; pirolízis helyett EcoClean.',False)
product(17,'Bosch PUE611BB5E indukciós főzőlap','PUE611BB5E','592×522×51 mm; kivágás 560×490–500',120000,'https://media3.bosch-home.com/Documents/specsheet/en-GB/PUE611BB5E.pdf','Gyári adatlap szerint 4.6 kW; nem a kereskedői 7.2 kW állítás. Villanyszerelő igazolja az áramkört.',False)
product(19,'Bosch KIN86VSE0 integrált hűtő','KIN86VSE0','541×548×1772 mm',380000,'https://www.bosch-home.fr/fr/product/le-froid/refrigerateurs-combines/combines-avec-congelateurs-en-bas-encastrable/KIN86VSE0','Chalk bútorfront takarja; 999 EUR francia ár csak támpont, HU ajánlat hiányzik.',False)
product(21,'Bosch BFL524MB0 fekete mikro','BFL524MB0','594×317×382 mm; niche 560–568×300×362–365',145000,'https://media3.bosch-home.com/Documents/specsheet/sk-SK/BFL524MB0.pdf','Sütővel összehangolt fekete front; bal oldali zsanér.',False)
# Full custom envelopes may cost more than CP1a generic assumptions.
for n,v in [(48,350000),(49,230000),(62,65000)]:row(n)['egysegar']=v;row(n)['gazdasagos']=v
# Explicit, bounded economising alternatives, not invented price discounts.
opts=[(30,350000,'Textilnyomat a kiemelt mezőkön; oldalpanelen egyszínű laminát. 100000 Ft becsült nettó projektmegtakarítás; kevesebb textúra.'),(31,210000,'Öt nyíló front, egy belső polc; belső fiókok helyett egyszerűbb tárolás. 50000 Ft becsült megtakarítás.'),(46,210000,'Azonos2700×1500 fejvég két nagy kárpitpanellel, egyforma taupe szövet; aszimmetrikus grafit mező helyett csak varrás. 90000 Ft becsült megtakarítás.'),(50,130000,'Gardróbban4 belső fiókkal kevesebb, helyettük4 állítható polc; 60000 Ft becsült megtakarítás.'),(51,170000,'Tusnyomat csak északi főfrontokon, déli front egyszínű kréta. 80000 Ft becsült megtakarítás.'),(109,155000,'Somar helyett külön beszerezendő Ø70–80 papírbúra E27 kábelszettel és Hue-val; pontos termék még nyitott, 105000 Ft célmegtakarítás NEM bizonyított.'),(132,120000,'Levehető textilborítás helyett sík vlies nyomat azonos kompozícióval; 65000 Ft becsült megtakarítás; kisebb tapintható textúra.'),(133,45000,'Vlies változatnál hordozósínek helyett falfelület-előkészítés és élzárás; 50000 Ft becsült megtakarítás.'),(138,250000,'Grafit fém lounge helyett tömör akác, méretezett 2200×850 pad ülőpárnával; 100000 Ft célmegtakarítás, látható anyagváltás.'),(139,120000,'Két grafit fotel helyett két akác lounge fotel párnával; 60000 Ft célmegtakarítás, pontos SKU még nyitott.')]
for n,v,note in opts:row(n)['gazdasagos']=v;row(n)['optimalizalas']=note+' Tulajdonosi döntés és ajánlat szükséges; főösszegbe csak választás után.'
for r in R:
 r['netto_megtakaritas_afa_utan']=r['mennyiseg']*(r['egysegar']-r['gazdasagos']) # net project effect, gross currency
 r['ar_also']=round((r['mennyiseg']*r['egysegar']+r['szallitas']+r['szereles']+r['egyeb'])*r['min_factor'])
 r['ar_felso']=round((r['mennyiseg']*r['egysegar']+r['szallitas']+r['szereles']+r['egyeb'])*r['max_factor'])
# quantified provisional cut schedule, no machine-ready manufacturing release.
cut=[]
for u in units:
 if u['kind'] in ['panel','upholstery']:
  for j,w in enumerate(u['modules']):cut.append(dict(unit=u['id'],part=f'Panel{j+1}',qty=1,width_mm=w-3,height_mm=u['h'],thickness_mm=18,material=u['front'],status='ELŐZETES, helyszíni méret + szerelési rendszer után újraszámítandó'))
 else:
  for j,w in enumerate(u['modules']):
   h=u['h']-(80 if u['h']>800 else 0);d=u['d']-28
   for part,qty,a,b,t in [('oldal',2,h,d,18),('fenék/tető',2,w-36,d,18),('hát',1,w-36,h-36,8),('polc',u['shelves'],w-38,d-20,18),('front',1,w-3,h-3,19)]:
    if qty:cut.append(dict(unit=u['id'],part=f'{j+1}-{part}',qty=qty,width_mm=a,height_mm=b,thickness_mm=t,material=u['front'] if part=='front' else 'laminált korpusz',status='AJÁNLATI LAPMÉRET; fiók/vasalat és rések után gyártó pontosítja'))
# Light routes every existing ML/FL retained, furniture strips linked to outlet.
E=list(csv.DictReader((P/'sources/main/01_alaprajzok/villamos_kiallasok/A902_villamos.csv').open()))
light=[]
for e in E:
 if e['azonosito'].startswith(('A902-ML','A902-FL')):
  n=e['azonosito'];short=n[5:];mapping={'ML04':109,'ML05':113,'ML06':116,'ML07':69,'ML08':81,'ML09':120,'ML10':120,'ML03':111,'FL01':111,'FL02':114,'FL03':120,'FL04':120}
  ki=mapping.get(short,145 if short in ['FL05','FL06','FL07'] else 110)
  light.append(dict(id=short,source=n,room=e['helyiseg'],x=float(e['x_m']),y=float(e['y_m']),circuit=e['aramkor'],target=f'KI-{ki:03}',route='meglévő nyomvonal, felméréssel igazolandó',driver='gyári lámpa integrált táp / E27 Hue',service='lámpatest gyári szerelőtere; hozzáférhető',status='TERV SZERINT; helyszíni ellenőrzés kell',scene='általános3000K / este2700K; vizes és kültéri IP gyári megfelelőséggel'))
for id,src,ki,length,service in [('L-TV-TOP','D16',114,2.6,'TV-01 alsó szervizmező'),('L-TV-VERT','D16',114,2.33,'TV-01 alsó szervizmező'),('L-TV-LOW','D16',114,3.3,'TV-02 szélső rekesz'),('L-W02','D19',115,2.1,'ART-02 levehető oldalsó mező'),('L-HB','D20',118,2.7,'NT-L hozzáférhető táp'),('L-WN','D26',119,2.92,'WN-01 felső szerelőrekesz'),('L-WS','D26',119,2.38,'WS-01 felső szerelőrekesz'),('L-KITCHEN','D02',112,1.4,'K-07 hozzáférhető felső rekesz'),('L-B62-M','FL04',121,.9,'száraz oldali tápdoboz KI-122'),('L-B62-U','FL04',121,.9,'száraz oldali tápdoboz KI-122')]:
  e=next((e for e in E if e['azonosito']=='A902-'+src),None)
  light.append(dict(id=id,source='A902-'+src,room=e['helyiseg'] if e else 'PENDING',x=float(e['x_m']) if e else 0,y=float(e['y_m']) if e else 0,circuit=e['aramkor'] if e else 'PENDING',target=f'KI-{ki:03}',length_m=length,route='fal/panel szerelősáv; külön folytonos kábelút, toldás csak hozzáférhető dobozban',driver='egy gyári kompatibilis Hue készlet/ág vagy jóváhagyott 24V CCT vezérlő+táp; nem feltételezett Hue split',service=service,status='TÁP/VEZÉRLŐ SKU ÉS MÉRETEZÉS NYITOTT',scene='2700K este;22–30% induló dim; helyszíni fénypróba'))
save('data/design_R02.json',dict(revision=REV,date=DATE,units=units,items=items,lights=light,rooms=G['rooms'],terrace_zones=G['terrace_zones']))
save('data/elemek.json',R);save('data/termek_bovites_R02.json',products);save('data/cutlist_R02.json',cut)
with (P/'data/elozetes_szabaslista.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cut[0].keys());w.writeheader();w.writerows(cut)
main=sum(r['mennyiseg']*r['egysegar']+r['szallitas']+r['szereles']+r['egyeb'] for r in R);eco=sum(r['mennyiseg']*r['gazdasagos']+r['szallitas']+r['szereles']+r['egyeb'] for r in R)
save('data/cost_snapshot_R02.json',dict(main=main,economy=eco,low=sum(r['ar_also'] for r in R),high=sum(r['ar_felso'] for r in R),budget=18000000,reserve=2000000,reserve_used=0,verified=sum(r['mennyiseg']*r['egysegar'] for r in R if r['arstatusz']=='ellenőrzött webshopár'),quotes=0,cp1a=20083350,cpv33=20293350,unproven_savings=True))
print('Design',len(units),'custom units;',len(items),'furniture; cost',main,eco)

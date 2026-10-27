"""R05 design / finish / cost inputs. Does not write the live workbook."""
from pathlib import Path
import json,copy,hashlib,csv,math
P=Path(__file__).resolve().parents[1];O=P/'R05'
def read(p):return json.loads((P/p).read_text())
def save(n,d): (O/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
before=read('R05/sources/workbook_before_R05.json'); raw=before['Elemregiszter']; rows=copy.deepcopy(raw[1:]); by={r[2]:r for r in rows}
units=read('R04/data/design_R04.json')['units']
variants=[read('R04/data/WN-01_R04A_alternative.json'),read('R04/data/B62-01_R04A_alternative.json')]+read('R04/data/TV_R04A_frontjavaslat.json')
vmap={u['id'].split('-R04')[0]:u for u in variants}
for i,u in enumerate(units):
 if u['id'] in vmap:units[i]=copy.deepcopy(vmap[u['id']]);units[i]['id']=u['id']
for u in units:
 u['revision']='KI-R05';u['status']='ÁRAZÁSI ÉS FELMÉRÉSI TERVVÁLTOZAT; gyártásra nincs jóváhagyva'
 u['drawers']=sum(b['drawers'] for b in u['cp3_bays']);u['shelves']=sum(len(b['shelves_mm']) for b in u['cp3_bays'])
 u['interior']=copy.deepcopy(u['cp3_bays'])
 u['drawings_base']='R04/drawings/'+u['id']+'_01.pdf'
 if (O/'data/drawing_index.json').exists():
  u['drawings_current']=[i['path'] for i in json.loads((O/'data/drawing_index.json').read_text()) if i['unit']==u['id']]
  if u['drawings_current']:u['drawings_base']=u['drawings_current'][0]
 u['material_ids']=[]
 if u['id']=='TV-01':u['y']=4.7
 if u['id']=='TV-03':u['y']=5.4
 if u['id']=='ART-02':u['modules']=[1050,1050];u['front_modules']=[1050,1050]
 if u['id']=='TV-02':
  # Accepted Cam02 rescue: tower at camera-side end, away from terrace window.
  u['modules']=[700,650,650,650,650];u['front_modules']=u['modules'][:];off=0
  for j,b in enumerate(u['cp3_bays']):
   b.update(id=f'TV-02-B{j+1:02}',offset=off,module_w=u['modules'][j],clear_w=u['modules'][j]-36)
   b['shelf_m2']=len(b['shelves_mm'])*b['clear_w']*b['clear_d']/1e6;off+=u['modules'][j]
  u['notes']='Világkoordináta Y növekvő irányában700+4×650. Torony Y=4,70–5,40m, ablak felé panel Y=5,40–8,00m. Ez felel meg a kiválasztott VISUAL_RESCUE kép bal oldali tornyának. Régi torony Y=7,30–8,00m elrendezés javítva.'
 u['capacity']={k:round(sum(b[k] for b in u['cp3_bays']),3) for k in ('rail_m','shelf_m2','drawer_l')}

materials=[
 dict(id='MAT-01',name='Világos matt, kész gyári front',candidate='EGGER U702 PM Cashmere Grey',method='19 mm PerfectSense MDF jelölt; színazonos ABS él. Csak a 2800 mm táblaméretbe beleférő frontokra. A hazai vastagság/tabla és hátoldal beszállítói egyeztetés.',hex='#c5bbae',use='K-01,K-02,K-07; nem a 2837 mm magas gardróbfront',source='https://www.egger.com/en/furniture-interior-design/decors/U702_PM?country=US',gate='Fizikai minta, hazai termékkód és táblaformátum; nem fényképből mért szín',price='A KI-009 meglévő frontkeretén belüli jelölt; írásos ár nincs.'),
 dict(id='MAT-02',name='Grafit matt, kész gyári front',candidate='EGGER U961 PM Graphite Grey',method='19 mm lakkozott MDF jelölt, egyező ABS él. Külső alsó front, éjjeli és asztal. Tartós vizes helyre nem automatikusan alkalmazható.',hex='#45423e',use='K-03..K-06,TV-02,CF-01,ST-01,NT-L,NT-R,DS52,NT-64,NT-76,HALL-01',source='https://downloads.egger.com/static/uk/FY_EGGER_PerfectSense_Portfolio_A4_Screen.pdf',gate='Karc-, szín- és élminta; magyar szállítás, készlet, pontos vastagság nyitott',price='Meglévő egyedi bútor keretében, nincs újra hozzáadva.'),
 dict(id='MAT-03',name='Teljes magasságú festett front',candidate='Egyedi 19 mm MDF, U702 fizikai mintához színre festve',method='2837 mm tervezett ajtóhoz legalább 2900 mm hasznos nyerslap és megfelelő prés/fülke szükséges. Kétoldali kiegyenlített bevonat, élfestés; grafika csak tapadási próba után. Nem toldható észrevétlenül 2800-as lapból.',hex='#c5bbae',use='WN-01,WS-01,W52-01,W53-01,ENT-01; kisebb világos elemek azonos színcsalád',source='R04/data/WN-01_R04A_alternative.json',gate='Nyerslap SKU, alakstabilitás, merevítő és pántszám gyártói méretezése; teljes magas front próba',price='KI-051 +120000 Ft R04 felár, más egységek saját frontkerete.'),
 dict(id='MAT-04',name='W01 médiafal textúra és tus',candidate='Egyedi matt ásványi hatású, mintázott felület + védett nyomat',method='TV-03: 18 mm hordozó + 18 mm szerelőlégrés a 36 mm befoglalóban. Toronyfront: 19 mm MDF, sötét alapszín. Nyomat az elfogadott kép kompozíciójából külön grafikai masterrel. Legfeljebb 1 mm próbatextúra; nincs automatikus dombormű.',hex='#a99b87',use='TV-01,TV-03',source='CP3/reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png',gate='600×600 minta, világító sarok és nyomatpróba; eredeti 1:1 tusmaster nincs; az AI-kép nem nyomdakész fájl',price='KI-030 690000 + KI-031 320000; teljes csomagbontás R05 költséglapon.'),
 dict(id='MAT-05',name='W02 teljes falgrafika nyomtatható hordozója',candidate='Vescom Bely+Print 1040.01',method='Vinil felület viszkóz/poliészter hátoldallal, 350 g/m²; 134 cm teljes / 133 cm nyomtatható szélesség. Két 1050 mm tervezett mező, 50 mm technológiai ráhagyás a széleken. Nyomdai illesztés és ICC a gyártóval véglegesítendő.',hex='#b4a793',use='ART-02',source='https://vescom.com/en/products/belyprint',gate='Nem valódi lenvászon és nem relief. Tónus, szövés, fekete, ragasztó és hordozó együtt mintázandó; nyomda még nincs kiválasztva',price='8,0 m² rendelendő előirányzat ×28000 Ft =224000 Ft; nem webshopár.'),
 dict(id='MAT-06',name='Csendes csatlakozó fal',candidate='Festett, finoman szemcsés greige felület',method='Az ART-02 színmintájához helyszíni próbafal; W07 és csatlakozó sarok. A falgrafika nyomtatott hordozóját nem számítjuk automatikusan erre is.',hex='#b4a793',use='ART-07',source='targets/A902_S01_KyotoInk_Cam_12__V33_C_v1.png',gate='A szög és súrolófény miatt eltérhet a fényesség; 1 m² próbafal',price='KI-124/127/128 meglévő falkezelési keret.'),
 dict(id='MAT-07',name='Világos betonhatású konyhapult',candidate='EGGER F274 ST9 Light Concrete dekor',method='38 mm munkalap és illesztett hátfal jelölt. Konkrét hazai munkalap SKU és élprofil még igazolandó; nem kő és nem vékony kerámia.',hex='#c7c0b3',use='K-08,K-09',source='https://www.egger.com/get_download/1ed4150d-4c94-4717-a4d9-81d28cacddf0/Product_Availability_Industrial_Decors_English.pdf?country=NL',gate='Kivágási rajz, vízzárás, géphő és hátfal alkalmasság; 38 mm él a renderen is látszódjon',price='KI-011/012/014 meglévő keretek, egy tétel csak egyszer.'),
 dict(id='MAT-08',name='Aszimmetrikus taupe–grafit kárpit',candidate='Kárpitos által biztosítandó két színű szövet, SKU nyitott',method='18 mm hordozó + kb.30 mm hab + vatelin és szövet; 60 mm befoglaló. Két külön levehető színmező, varratkiosztás a célkép szerint.',hex='#8b7b68',use='HB-01,ENT-02',source='targets/A902_S01_KyotoInk_3_master_Cam_04_A__ASTRA_V3_1__v1.png',gate='Szövet SKU, kopásállóság, tisztíthatóság és színminta; végleges shader még nincs',price='KI-046/047 meglévő keret; a grafit mező nem törlődik az olcsóbb változatban.'),
 dict(id='MAT-09',name='Fürdő sötét front és lezárt élek',candidate='19 mm nedvességálló MDF + kétoldali matt bevonat',method='Minden furat és vágott él lezárva. Kivehető szifonos fiók, fröccsenési és ragasztási próba. Az MDF nem vízálló.',hex='#45423e',use='B62-01,B62-02,B61-01',source='R04/data/B62-01_R04A_alternative.json',gate='Bevonatrendszer pontos gyártó/SKU, mosdó, szifon, falrögzítés',price='KI-092 270000 Ft, többi külön fürdősor. Szifon-kivágás felárát ajánlat igazolja.'),
 dict(id='MAT-10',name='Belső laminált korpusz',candidate='18 mm világos melaminbevonatú bútorlap; konkrét dekor nyitott',method='18 mm korpusz/polc,8 mm hát; látható él2 mm, belső1 mm ABS. Festett MDF-re nem írunk ABS-t. Nagy fesztávú polc terhelési ellenőrzéssel.',hex='#ede9e1',use='Valamennyi száraz szekrénybelső',source='R04/data/design_R04.json',gate='Lap-/élgyártó és dekor összehangolása, emissziós igazolás; előzetes szerkezet nem gyártási darabjegyzék',price='Korpusz és belső sorokban; nincs külön dupla elszámolás.')]
for u in units:
 uid=u['id']
 ids=['MAT-10'] if u['kind']=='cabinet' else []
 if uid in ['K-01','K-02','K-07']:ids+=['MAT-01']
 elif uid in ['K-03','K-04','K-05','K-06','TV-02','CF-01','ST-01','NT-L','NT-R','DS52','NT-64','NT-76','HALL-01']:ids+=['MAT-02']
 elif uid in ['WN-01','WS-01','W52-01','W53-01','ENT-01','WC-01']:ids+=['MAT-03']
 elif uid in ['TV-01','TV-03']:ids+=['MAT-04']
 elif uid=='ART-02':ids+=['MAT-05']
 elif uid=='ART-07':ids+=['MAT-06']
 elif uid in ['K-08','K-09']:ids+=['MAT-07']
 elif uid in ['HB-01','ENT-02']:ids+=['MAT-08']
 elif uid.startswith(('B61','B62')):ids+=['MAT-09']
 u['material_ids']=ids
geometry=read('data/design_R02.json');items=copy.deepcopy(geometry['items'])
for it in items:
 if it['id']=='KI-033':it['y']+=.7
save('data/design_R05.json',{'revision':'KI-R05','units':units,'items':items,'rooms':geometry['rooms'],'terrace_zones':geometry['terrace_zones'],'selection':'Tervezési és árazási munkaváltozat, nem rendelési vagy gyártási jóváhagyás'})
save('data/materials.json',materials)
patch={};notes={}
def edit(id,reason,**fields):
 patch.setdefault(id,{}).update(fields);notes[id]=reason
 for c,v in fields.items():
  n=0
  for a in c:n=n*26+ord(a)-64
  by[id][n-1]=v
edit('KI-030','R04 médiafal +240000: 160000 felületi többlet és80000 grafika/minta; különbözeti becslés, nem új teljes csomag.',Q=690000,H='W01 panelkompozíció és sötét tusgrafikás torony',N='MAT-04',AN='TV-01; TV-03',AF='R05: referencia a VISUAL_RESCUE. 450000 eredeti+160000 felület+80000 grafika/minta. Nem külön újra összegezendő.',AY=560000/690000,AZ=950000/690000)
edit('KI-031','R04 +60000 nagy front merevítés/új osztás; az alsó700 mm a torony alá igazítva.',Q=320000,H='W01 alsó ötfrontos médiabútor; torony felől700+4×650',N='MAT-02',AF='260000 eredeti+60000 front/illesztés felár. Belső fiókelhagyásból nem számolunk fiktív megtakarítást.',AY=.8,AZ=1.4)
edit('KI-050','WN 8 szélesebb fiók+60000; 5 polc+1rúd elmarad−40000. A polckapacitás csökkenése jóváhagyásra vár.',Q=806000,AF='WN:3,350m rúd;436,914l fiók;2,036m²polc. RégiWNhez−1,356m²polc. Két lift és8fiók megmarad. WS változatlan.',AY=.8,AZ=1.45)
edit('KI-051','6 teljes magas front ×20000 felár; nem2800 mm táblából toldva.',Q=370000,N='MAT-03',AF='6×2837 mm magas keskeny északi front. 250000+120000 becslés. Merevítés és műhelyméret nyitott.',AY=.75,AZ=1.55)
edit('KI-092','Két egymás melletti600/300fiók; szifon és vasalat módosítása.',Q=270000,H='06.2 mosdóbútor; 600+300 oldalankénti fiók',N='MAT-09',AY=.8,AZ=1.45)
edit('KI-CP3-L01','12régiWN lámpa kivéve; új7 hosszabb külön KI-R05-L01.',O=49,AF='A61darab CP3 listából a12WN darabot felváltja a7×710mm KI-R05-L01. Minden más lámpa változatlan.')
edit('KI-119','Öttel kevesebb belső lámpa.73helyett68×1500+35000.',Q=137000,W='68 db ×1500 Ft +35000 Ft mérés/beállítás; előirányzat',AF='WN érzékelés és kábelút helyszíni próba; TRÅDFRI nem automatikusan Hue-képes.')
edit('KI-CP3-S04','AT8:12,T026:9tervezett próbadoboz; valós típus még nincs.',O=21,AF='21×4000 Ft. Dobozméret a használati terv szerint, nem mind azonos termék. Előirányzat, szállítás központi keretben.')
edit('KI-132','Régi150×220kép helyett teljes2100×2880falmező.2×2,98fm×1,34m=7,9864m²,8,0m²előirányzat.',H='W02 teljes magasságú szövethatású nyomat',I='Vescom jelölt',J='Bely+Print1040.01',K='https://vescom.com/en/products/belyprint',L='2100×2880 mm nettó; 2×1050 mm mező, nyomdai szabás egyeztetendő',N='MAT-05',O=8,P='m²',Q=28000,V='előzetes becslés',W='R05:8,0m²×28000Ft gyártási előirányzat; Vescom hordozó műszaki adat ellenőrzött, ár nem',AF='Sík szövethatású nyomat, nincs térbeli relief. KI-131 grafika; KI-133 hordozó/rögzítés. Nem számolható külön keretezett kép is.',AY=.7,AZ=1.6)
edit('KI-133','Keretezett kép helyett36mm teljes falpanel és oldható rögzítés.',H='W02 keret nélküli hordozó, élképzés és szerelés',Q=177000,W='61000 hordozó+36000 szerelőlécek/rögzítés+24000 él/sarok+56000 helyi szerelés; becslés',AF='6,048m²nettó;18mm lap+18mm tervezett szerelőlégrés. Szállítás/felhordás központi KI-151, nincs duplázás.',AY=.7,AZ=1.5)
edit('KI-123','Nincs önálló nullaértékű hiány: a W02 felületet KI-132/133 tartalmazza.',AF='W02 nettó6,048m²; anyag/nyomat KI-132, hordozó/él/szerelés KI-133, grafika KI-131. Ez a hivatkozósor nem összegezhető többlet.')
edit('KI-114','R05 konkrét fényforrás és áramköri bontás, a150000Ft előirányzat változatlan.',J='Loox5 LED2074 833.74.308; GL-C-009P jelölt',K='https://files.hafele.co.uk/catalogfiles/www/25-1010.pdf',L='Felső2,60m + függőleges2,33m + alsó3,30m; összes8,23m,10m rendelés',N='12V;2700K;9,6W/m;CRI>90;2×60W táp',AF='R05/data/W01_light_circuit.json:47,328W és31,680W körök. PS-A két párhuzamos ág, mind4m alatt. Hue és hőpróba, PSU/profile SKU nyitott. Tételes45000+25000+24000+24000+12000+20000=150000Ft becslés.')
def newrow(id,name,room,trade,qty,unit,price,sku,link,status,reason,low=.7,high=1.5):
 r=[None]*54
 vals={0:'A902',1:room,2:id,3:'V27/V28' if room=='T-0-26' else 'V04/V12',5:'stílus',6:trade,7:name,9:sku,10:link,14:qty,15:unit,16:price,17:0,18:0,19:0,21:status,22:link or reason,23:'2026-10-27',24:'nem visszaigazolt',25:'B',26:'feltételes',27:'tervezési javaslat',28:'nincs megrendelve',29:'tulajdonos / kivitelező',30:reason,31:reason,32:price,34:'azonos',39:'T-0-26' if room=='T-0-26' else 'WN-01',42:'késztermék + szerelés',43:'gyártói adat / helyszíni illesztés nyitott',44:'HUF',45:1,46:'nincs ajánlati érvényesség',47:'KI-151 közös logisztika',48:'a sor tartalma',49:1,50:low,51:high}
 for k,v in vals.items():r[k]=v
 rows.append(r);by[id]=r;notes[id]=reason
 return r
newrow('KI-R05-L01','WN ÖVERSIDAN710mm belső fény','05.1','világítás',7,'db',6490,'205.894.85','https://www.ikea.com/hu/hu/p/oeversidan-led-es-gardrobvilagitas-erzekelo-fenyereje-szabh-feher-20589485/','ellenőrzött webshopár','24,5W összesen;30Wdriveren81,7%. Táp/kábel meglévőCP3sorokban, szerelésKI-119.',1,1.15)
newrow('KI-R05-B01','Fali biciklitartó és rögzítés','T-0-26','tároló',1,'csomag',70000,'Steadyrack Classic Road jelölt','https://eu.steadyrack.com/products/classic-road-bike-rack','előzetes becslés','89,99EUR gyártói oldal;420Ft tervezési árfolyammal37796Ft,45000Ft beszerzési keret+25000Ft falrögzítés.35kg,20–29col,max2,1colgumi,sárvédő nélkül. Valós bicikli és fal/ajtó ismeretlen. HU szállítás nem igazolt.',.5,120000/70000)
# Ordinary finish mappings: do not overwrite prices or manual notes for unaffected rows.
for id,mat in [('KI-009','MAT-01 / MAT-02'),('KI-011','MAT-07'),('KI-012','MAT-07'),('KI-037','MAT-02'),('KI-038','MAT-02'),('KI-046','MAT-08'),('KI-048','MAT-10'),('KI-049','MAT-10'),('KI-124','MAT-06')]:edit(id,'R05 anyagkód hozzárendelése; ár változatlan.',N=mat)
# Reset ONLY previous alternative assumptions explicitly superseded by storage / appearance requirements.
economy=[]
for r in rows:
 if r[16]!=r[32] or r[2] in patch:
  patch.setdefault(r[2],{})['AG']=r[16];r[32]=r[16]
  patch[r[2]]['AI']='R05 főváltozat tartalma; korábbi fiók-/aszimmetria-elhagyás nincs automatikusan kiválasztva.';r[34]=patch[r[2]]['AI']
def eco(id,price,basis,compromise):
 r=by[id];saving=(r[16]-price)*r[14]
 edit(id,notes.get(id,'')+' Gazdaságos összehasonlítás külön.',AG=price,AI=basis+' Eltérés: '+compromise+'; nem jóváhagyott. Nettó projektmegtakarítás '+str(round(saving))+' Ft, bruttó költségek különbsége.')
 economy.append(dict(id=id,main=r[16]*r[14],economy=price*r[14],saving=saving,basis=basis,compromise=compromise,status='BECSÜLT, ajánlat és minta szükséges'))
eco('KI-030',590000,'Kézzel texturált mezők helyett sík, gyári szövethatású nyomtatott hordozó;160000 felületi felárból60000 marad. A torony és tuskompozíció változatlan.','súrolófényben laposabb felület, nem teljes anyagazonosság')
eco('KI-132',22000,'Ugyanazon8m²rendelési mennyiség; prémium vinil-szövethatás helyett matt vlies nyomat 22000Ft/m²előirányzattal.','a szövés tapintása és tisztíthatósága változik; hordozó SKU még kiválasztandó')
eco('KI-CP3-B01',40000,'145000Ft mozgó fiókáram helyett40000Ft fix, hozzáférhető dugalj és szabályos szerelés, ugyanabban a szervizzónában.','a készülék töltéséhez ki kell venni a fiókból; vizes zóna szakemberrel')
# Safe savings are modest. Never fake a 18m total by deleting jacuzzi / wardrobes.
tot=lambda r:r[14]*r[16]+sum((r[j] or 0) for j in (17,18,19))
main=sum(tot(r) for r in rows);eco_total=sum(r[14]*r[32]+sum((r[j] or 0) for j in (17,18,19)) for r in rows)
snapshot={'revision':'KI-R05','main':main,'economy':eco_total,'saving':main-eco_total,'low':sum(round(tot(r)*r[50]) for r in rows),'high':sum(round(tot(r)*r[51]) for r in rows),'budget':18000000,'gap':main-18000000,'economy_gap':eco_total-18000000,'reserve':2000000,'reserve_used':0,'verified':sum(tot(r) for r in rows if r[21]=='ellenőrzött webshopár'),'quotes':sum(tot(r) for r in rows if r[21]=='beszállítói ajánlat'),'rows':len(rows),'r04':23791890,'CP3':23253840,'status':'A teljes R04 javaslat és W02 javítás árazási munkaváltozata. Nem költési/gyártási jóváhagyás.'}
snapshot['estimated']=main-snapshot['verified']-snapshot['quotes']
save('data/cost_R05.json',snapshot);save('data/economy_options.json',economy)
save('data/register_patch.json',{'patches':patch,'new_rows':rows[172:],'reasons':notes,'expected':snapshot})
save('data/register_proposal.json',[raw[0]]+rows)
print(json.dumps(snapshot,ensure_ascii=False))

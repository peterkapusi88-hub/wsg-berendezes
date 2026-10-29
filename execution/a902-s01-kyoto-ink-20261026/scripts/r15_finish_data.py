from pathlib import Path
import json,hashlib,shutil,collections,math,csv
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
def r(n):return json.loads((O/n).read_text())
def w(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2))
# Fix exact cut plan after reserving end-cap space.
l=r('data/lighting.json');l['circuits'][0].update(LED_mm=3550,unlit_end_total_mm=50,W=28.4,A=28.4/24)
c=l['circuits'][0];c['voltage_drop_V']=2*.0225*3*c['A']/.75;c['voltage_drop_pct']=c['voltage_drop_V']/24*100
l['strip']['cutting']='A tekercs:3550mm+1450mm maradék. B tekercs:2750mm+2250mm. L03=2250+50mm az A maradékból,forrasztott vezetékes híddal. Beépített8.60m,maradék1.40m. Végzáróknak L01-ben25-25mm;L02-ben5-5mm;L03-ban a híd és végzárók együtt30mm helyet kapnak.'
l['total_W']=sum(c['W'] for c in l['circuits']);l['total_A']=l['total_W']/24;l['driver_load_pct']=l['total_W']/151.2*100;w('data/lighting.json',l)
cost=r('data/cost_allowance.json');cost[6][7]='2x5m;8.60mbeépül,1.40mmaradék';w('data/cost_allowance.json',cost)
pilot=r('pilot/pilot_manifest.json');ph=r('pilot/data/holes.json');dowels=sum(h['kind'].startswith(('CSAP','MEREVITO')) for h in ph)//2
for item in pilot['hardware']:
 if item['sku']=='8x30 bükk csap':item['qty']=dowels
w('pilot/pilot_manifest.json',pilot)
for rel in ['audit/mpr_readback.json','pilot/audit/mpr_readback.json']:
 a=r(rel);a['limitations']='Active drilling draft only. Back-corner notches are separate saw operations. No actual tool IDs, feeds, fixture, woodWOP5 parse or machine simulation. Hardware bodies are simplified coordination envelopes in separate DWG.';w(rel,a)
hardware=json.loads((P/'R14_muhely/data/hardware.json').read_text())
hardware[11]=['HW12','Blum','609.1500','3.5x15 süllyesztett pánt/pánttalp csavar',64,'Gyártói cikkszám;laphoz próbafúrás']
hardware += [
 ['HW14','Camar','80702Z1INSX','Bal belső függesztő',6,'32x64 Ø10/12 mintázat a CAD-ben;alkalmazáspróba'],
 ['HW15','Camar','80702Z1INDX','Jobb belső függesztő',6,'Ugyanaz tükrözve'],
 ['HW16','Camar','897ASZ11212','120x120 anti-drop fali lemez',12,'Rögzítő furatokat a tényleges lemezről átjelölni;falhorgony külön'],
 ['HW17','Monarch','MF375 /50.8mm','Paneloldali klipsz',48,'2furat/klipsz;32.004középtáv'],
 ['HW18','Monarch','MF375 /2500mm','Faloldali sín rendelési szál',5,'4x2760mm toldott kész hossz;vágásveszteség'],
 ['HW19','Tervezési specifikáció','3.5x16 pan-head','Klipsz paneloldali csavar',96,'12.825mm névleges beülés a3.175mmklipsz alatt;próba18mmhordozón'],
 ['HW20','Vogel','3836050 TVM3605','Fix TV-konzol',1,'675x428x22 befoglaló;valósfal/TVsablon szükséges'],
 ['HW21','Egyedi','KI15-WALL-PACK','Szilárd falsík-kiegyenlítés',1,'Névleges31mm aCamarlemezhez,11.647mm a panelsínhez;felmérés és teherátadásellenőrzés'],
 ['HW22','Fischer / feltételes jelölt','SXRL10x120T /522700','Falhorgony-jelölt csavarral',0,'NEM kiválasztott végleges darabszám. Csak megfelelő ETA-falazat/teher/vastagság esetén;faladat nélkül nincs kiadott furat. A költség nem nulla: H04 előirányzat.'],
 ['HW23','Egyedi','KI15-EL-TRAY','430x240x2 tálca +17mm távtartók',1,'4db3.5x30 csavar;11mm beülés;elölről kiszerelhető'],
 ['HW24','LED line PRIME','476821','COB2700K8W24V szalag5m',2,'8.60m beépített;50mm vágás'],
 ['HW25','KLUS','B1718K7_3','PDS4 fekete3m profilszál',4,'Régi B1718 cikkszám,gyártó aktuális megfelelőjét beszállítóval igazolni'],
 ['HW26','KLUS','LIGER17037','Szatén diffúzor, méter',12,'Profilcsaláddal egyező szállított verzió szükséges'],
 ['HW27','KLUS','24066 /24081','Zárt/kivezetett végzáró',8,'4+4'],
 ['HW28','KLUS','24189','Profilrögzítő',22,'Rögzítési próba a valós felületre'],
 ['HW29','MEAN WELL','LPV-150-24','24V151.2W tápegység',1,'68.8W névleges szalagterhelés'],
 ['HW30','Sunricher','SR-ZG9101FA-DIM','CV PWM Zigbee dimmer',3,'Külön3egység,CH1 áganként;firmware/párosításpróba'],
 ['HW31','Villamos specifikáció','2A DC áganként','Biztosító és hozzáférhető tartó',3,'Vezeték és tápegység alapján villanyszerelő véglegesíti'],
 ['HW32','Villamos specifikáció','2x0.75mm²Cu','SELV kábel rendelési méter',16,'12m egyirányú tervezett út +30%tartalék;helyszínhez mérendő']]
w('data/hardware_bom.json',hardware)
sources=[
 ['S01','Camar807 IN furatkép','Camar807_IN.pdf','https://webdata.drevotrust.cz/montazni_navody/camar/807/camar_807_provedeni_F1.pdf','Gyártói lap forgalmazói tárhelyről;2016F1,aktuális alkalmazás megerősítendő'],
 ['S02','MonarchMF375 méretrajz','MF375.pdf','https://monarchmetal.eu/wp-content/uploads/2025/01/MF375-Rail-and-Clip-Package-EVEN-1250-2500MM.pdf','Gyártói'],
 ['S03','SunricherCV DIM útmutató','Sunricher_DIM.pdf','https://www.lemona.lt/Files/Instrukcijos/Pdf/SR-ZG9101FA-DIM%20instruction%20V1.pdf','GyártóiV1 másolata;termékoldalon kisebb régi ház,tervben nagyobb170x53.4x28'],
 ['S04','VogelTVM3605 adatlap','Vogel3605.pdf','https://brandportal.vogels.com/m/76109be3bb82e160/original/3836050_TVM3600Series_Leaflet_Document_EN.pdf','Gyártói;konzolfurat-sablont nem tartalmaz'],
 ['S05','MEANWELL táp','MeanWell.pdf','https://www.meanwell.com/Upload/PDF/LPV-150/LPV%2CLPVL-150-SPEC.pdf','Gyártói'],
 ['S06','LEDline476821','web','https://ledline.pl/produkty/tasmy-led/tasmy-led-cob/tasma-led-320-cob-24v-2700k-8w-ip20-8mm-5m-800lmm-prime/','Gyártói termékoldal'],
 ['S07','KLUSprofil és tartozékok','web','https://www.kitokogroup.com/wp-content/uploads/catalogs/KLUS%20CATALOG.pdf','Gyártói katalógus forgalmazónál;legacy rendelési kódok'],
 ['S08','Blum609.1500','web','https://www.hpponline.co.uk/DocumentHandler/547504/20k1101t22-product-data-sheet.pdf','Gyártói csavaradatlap forgalmazónál'],
 ['S09','KEKUAS alternatíva','web','https://www.hafele.com/INTERSHOP/static/WFS/Haefele-HAC-Site/-/Haefele/en_US/documents/02594429_0.pdf','Gyártói alkalmazási feltétel;nem fedélzeti függesztés,legalább4pár éspróba'],
 ['S10','FischerSXRL feltételes család','web','https://www.fischer-international.com/-/media/fixing-systems/rebrush/fide/xxx---fide---alt/service/informationsmaterial/documents/prospekte/holzbau.pdf','Gyártói;nem konkrét A902falrögzítési méretezés']]
w('data/source_register.json',[dict(id=a,title=b,file=c,url=d,evidence=e,checked='2026-10-29',sha256=hashlib.sha256((O/'sources'/c).read_bytes()).hexdigest() if (O/'sources'/c).exists() else None) for a,b,c,d,e in sources])
for source,target in [('/tmp/TV_R15_koordinacio_v2.dwg','TV_R15_vasalat_koordinacio.dwg'),('/tmp/TV_R15_robbantott_v2.dwg','TV_R15_robbantott.dwg')]:
 if Path(source).exists():shutil.copy2(source,O/'rajzok'/target)
for log in ['ki15views02','ki15verify01']:
 if Path('/tmp/'+log+'.log').exists():shutil.copy2('/tmp/'+log+'.log',O/'audit'/(log+'.log'))
print('Selected hardware',len(hardware),'pilot dowels',dowels,'LED W',l['total_W'])

"""Additional quotation details, derived from the same R02 records. Not manufacturing release."""
import draw_package as base
from draw_package import *
extra=[]
for u in D['units']:
 if not u.get('interior'):continue
 d=frame('I-'+u['id']+' | belső kiosztás / nyitott fronttal');sc=min(850/u['w'],550/u['h']);ox=100;oy=125
 rect(d,ox,oy,u['w']*sc,u['h']*sc,PAPER);line(d,ox,oy+2360*sc,ox+u['w']*sc,oy+2360*sc);pos=0
 for v in u['interior']:
  bi=v['bay']-1;mw=u['modules'][bi];xx=ox+pos*sc
  if bi:rect(d,xx-9*sc,oy,18*sc,u['h']*sc,TAUPE)
  txt(d,xx+8,oy+u['h']*sc-20,'Rekesz '+str(bi+1),10)
  for zz in v['shelves_mm']:line(d,xx+18*sc,oy+zz*sc,xx+(mw-18)*sc,oy+zz*sc);txt(d,xx+20,oy+zz*sc+4,str(zz),9)
  for zz in v['rails_mm']:line(d,xx+30*sc,oy+zz*sc,xx+(mw-30)*sc,oy+zz*sc,RED,2,[5,3]);txt(d,xx+15,oy+zz*sc+8,'Rúd '+str(zz),9,RED)
  for j in range(v['drawers']):rect(d,xx+35*sc,oy+(100+j*180)*sc,(mw-70)*sc,160*sc,TAUPE)
  dim(d,xx,oy-25,xx+mw*sc,oy-25,str(mw));pos+=mw
 dim(d,ox-30,oy,ox-30,oy+u['h']*sc,str(u['h']))
 txt(d,100,80,'Szintek: korpusz aljától mm. Polc18; osztó18; belső fióktest16 mm javaslat. Frontszabás külön jegyzék.',11)
 txt(d,100,60,'Rúd: '+u['interior'][0]['rail_type']+'. A kihúzható vasalat cikkszáma, teherbírása és belső hézagai gyártóval lezárandók.',10)
 name='I-'+u['id'];export(d,name);extra.append(name)
# TV-wall front with all three structures plus real detail concepts.
d=frame('CS-TV | W01 teljes kompozíció és szerelési metszetek');sc=.16;ox=70;oy=260
rect(d,ox,oy,3300*sc,400*sc,TAUPE);pos=0
for mw in [600,600,600,750,750]:line(d,ox+pos*sc,oy,ox+pos*sc,oy+400*sc);pos+=mw
rect(d,ox,oy+400*sc,2600*sc,2330*sc,PAPER);rect(d,ox+2600*sc,oy+400*sc,700*sc,2330*sc,TAUPE)
for n in range(1,4):line(d,ox+n*650*sc,oy+400*sc,ox+n*650*sc,oy+2730*sc)
rect(d,ox+580*sc,oy+800*sc,1452.9*sc,834*sc,INK);txt(d,ox+620*sc,oy+1200*sc,'65 col / 1452,9 × 834',10,colors.white)
dim(d,ox,oy-25,ox+3300*sc,oy-25,'3300');dim(d,ox-25,oy,ox-25,oy+2730*sc,'2730 +150 padlóhézag')
txt(d,70,715,'TV-01 / TV-02 / TV-03: frontirány +X; nézet a nappaliból a W01 felé',12)
txt(d,675,700,'CS-TV-01 / panel-fal részlet',13);rect(d,690,470,18,170,GREY);rect(d,758,470,36,170,TAUPE);dim(d,708,450,758,450,'25 cél');dim(d,758,430,794,430,'18+18 rétegrend')
para(d,675,400,'Fal → igazolt rögzítésű tartóléc → szerviz/kábelrés → levehető18mm hordozó és18mm dekorréteg. A TV-konzol közvetlen teherhordó falhoz fogjon, ne csak a dekorpanelhez.',69,11,16)
txt(d,675,280,'CS-TV-02 / rejtett fény',13);rect(d,700,180,180,18,TAUPE);rect(d,700,198,35,24,None,RED);line(d,700,222,735,222,RED,2);dim(d,900,180,900,222,'21 cél')
para(d,675,145,'LED alumíniumprofil + opál fedél:20×12mm foglalási cél. Gyártói profil és hőleadás még nyitott. Szalag ne látszódjon ülve. Táp a TV-01 levehető alsó rekeszében; csatlakozás hozzáférhető.',68,10,14)
para(d,70,160,'TV VESA400×300,16,7kg készülék; konzol és alapfal teherbírását szakember igazolja. Kábelek a TV mögötti szerviznyíláson, külön erős-/gyengeáramú út. D16/FL02 és redőnyfedél nem zárható el.',78,11,16)
export(d,'CS-TV');extra.append('CS-TV')
# Kitchen clear openings / working-top fabrication templates.
d=frame('CS-K | Konyhai gépnyílások és pultvágások');txt(d,60,705,'Minden kivágás végleges gyári sablon és készre szerelt korpusz alapján.',13,RED)
for x,y,title,w,dep,cutw,cutd in [(70,470,'K-09 / főzőlap PUE611BB5E',1600,620,560,490),(650,470,'K-08 / mosogató',1460,620,0,0)]:
 sc=.25;rect(d,x,y,w*sc,dep*sc,PAPER);dim(d,x,y-25,x+w*sc,y-25,str(w));dim(d,x+w*sc+15,y,x+w*sc+15,y+dep*sc,str(dep));txt(d,x,y+dep*sc+22,title,12)
 if cutw:rect(d,x+50*sc,y+65*sc,cutw*sc,cutd*sc,None,RED);txt(d,x+5,y+40,'560×490–500; sarokrádiusz gyári sablonból',10)
 else:txt(d,x+5,y+60,'Nincs jóváhagyott mosogató-kivágás.',11,RED);txt(d,x+5,y+40,'KI-024 exact SKU / sablon még nyitott.',10)
para(d,60,380,'K-01: sütő niche564×590×550, alj600mm. Mikro niche564×365×min300, alj1280mm. A külső595/382magasságú készülék előlapja takar; a nyílás nem azonos a készülék előlapméretével. Polc teherbírás, rés és szellőzés gyártói dokumentáció szerint.',135,12,18)
para(d,60,290,'K-04: 600mm szabad gépnyílás! 600mm külső korpuszba18mm oldallapokkal nem fér az598mm gép. Nincs külön korpusz; pultáthidalás és rögzítés szomszédos elemekhez. 1150mm nyitott mélységből600mm plusz benyúlás: a840mm folyosón csak240mm marad, nincs átjárás nyitott gép mellett.',135,12,18)
para(d,60,200,'K-02: hűtő1772×541×548; niche1780×564×550tervezési cél. Folytonos alsó/felső szellőzés. Frontosztás700/1852mm jelenleg ajánlati, a pontos gyári csúszópántos kiosztás és légszabad keresztmetszet nélkül nem szabható.',135,12,18)
para(d,60,110,'A pult névleges38mm. F274 ST9 dekorra mutató látványjavaslat nem anyagminta. Minden vágott él, mosogatófurat és falcsatlakozás vízzárása gyártó által jóváhagyott rendszerből; fugák és kivágáseltolás felmérésre vár.',135,11,16)
export(d,'CS-K');extra.append('CS-K')
# Bath glass: dimensioned elev/plan & drainage/siphon concept.
d=frame('GL-01 / CS-B | Zuhanyüveg és mosdóbútor csatlakozások');sc=.22;rect(d,90,260,1000*sc,2000*sc,None,INK,2);dim(d,90,235,310,235,'1000 cél');dim(d,60,260,60,700,'2000 cél');txt(d,90,205,'8mm előzetes; üveges méretezés kell',11,RED)
rect(d,500,390,900*.4,350*.4,PAPER);rect(d,630,450,100,80,None,RED);txt(d,510,550,'B62-01 / mosdó és felső fiók kivágása',12);dim(d,630,440,730,440,'250 cél');dim(d,750,450,750,530,'200 cél')
para(d,480,340,'Kivágás csak a tényleges szifon és csap bekötésének sablonja alapján. Felső fiók U alakú; oldalfalak és fenék vízálló lezárása. Alsó fiók teljes kihúzás; a szifon tisztítása szerszám nélkül hozzáférhető front mögül.',82,12,18)
para(d,90,160,'Üveg: falprofil és felső stabilizátor méretezés/terhelés szerint; padlófúrás csak vízszigetelési jóváhagyással. Síkeltérés és lejtés helyszíni sablonnal. Zuhanybelépés és meglévő zuhanyfej szórása próba után. Kész burkolatra mérni, nem renderből.',140,12,18)
export(d,'GL-01_CS-B');extra.append('GL-01_CS-B')
w=PdfWriter();w.append(str(P/'outputs/A902_R02_rajzcsomag.pdf'))
for n in extra:w.append(str(P/'drawings'/f'{n}.pdf'))
w.write(str(P/'outputs/A902_R02_rajzcsomag.pdf'))
# Preliminary BOM: finished size; edge allowance/CNC drilling and special appliance parts not released.
rows=[]
def part(u,n,a,b,t,q,notes):rows.append(dict(szerkezet=u['id'],elem=';'.join(u['cost']),alkatresz=n,hossz_mm=a,szeles_mm=b,vastag_mm=t,db=q,anyag=u['material'],felulet=u['front'],megjegyzes=notes,status='AJÁNLATI KÉSZMÉRET; NEM CNC/GYÁRTÁSI KIADÁS'))
for u in D['units']:
 w,dep,h=u['w'],u['d'],u['h'];ms=u['modules'];kind=u['kind']
 if u['id']=='K-04':part(u,'Gépfront',597,732,19,1,'Frontmagasság és lábazatkivágás gyári sablonnal; nincs korpusz.');continue
 if kind in ['panel','upholstery']:
  for j,m in enumerate(ms):part(u,'Mező '+str(j+1),m-3,h,18,1,'Nyomat/kárpit ráhagyás külön; hordozó vastagság egyeztetendő.')
  continue
 if kind in ['table','bench','shelf']:
  part(u,'Tető / munkalap',w,dep,min(h,38) if kind=='table' else 18,1,'Egyedi tartóváz/láb külön gyártói méretezéssel; nem zárt szabáslista.');continue
 part(u,'Oldal',h,dep,18,2,'Látható él2mmABS; készméretből élvastagság gyártó szerint levonandó.');part(u,'Alsó/felső',w-36,dep-19,18,2,'Felső lap gép/szifon körül kiváltandó a részletrajz szerint.');part(u,'Hát',w-36,h-36,8,1,'Levehető szervizhát; géptorony szellőzőnyílások külön.');part(u,'Belső osztó',h-36,dep-27,18,max(0,len(ms)-1),'Nem automatikus modulonkénti duplaoldal.')
 if u.get('interior'):
  part(u,'Felső fix polc',w-36,dep-27,18,1,'Felső szint2360mm.');
  for v in u['interior']:
   mw=ms[v['bay']-1];part(u,'Rekesz'+str(v['bay'])+' polc',mw-36,dep-27,18,len(v['shelves_mm']),'Szerelési polcrés gyártóval.');part(u,'Rekesz'+str(v['bay'])+' fiókfront',mw-70,160,16,v['drawers'],'Belső fióktest és sín szabása választott vasalat szerint.')
  for j,m in enumerate(ms):part(u,'Alsó ajtó'+str(j+1),m-3,2357,19,1,'110°csillapított; pontos pántszám gyártói tömeg alapján.');part(u,'Felső ajtó'+str(j+1),m-3,h-2363,19,1,'Fogásprofil; nyomat illesztés csukott frontállapotban.')
 elif u['id'] in ['K-01','K-02']:
  part(u,'Géptorony köztes polc',w-36,dep-27,18,3 if u['id']=='K-01' else 1,'Pontos szintek CS-K; géptartó teherbírás ellenőrizendő.');part(u,'Front anyagelőirányzat',w-3,h-3,19,1,'NEM egy darab gyártási front! Kivágás/frontosztás CS-K szerint, gyári sablonra vár.')
 else:
  part(u,'Polc',w-36,dep-27,18,u['shelves'],'Osztott elemnél rekeszenként újraméretezendő.')
  for j,m in enumerate(ms):
   n=max(1,round(u['drawers']/len(ms)));part(u,'Front'+str(j+1),m-3,round(h/n-3,1),19,n,'Fiókrendszer hézagai, szifon és lábazat még gyártói egyeztetés.')
(P/'data/cutlist_R02.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (P/'data/elozetes_szabaslista.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
print('Total drawing pages',len(PdfReader(P/'outputs/A902_R02_rajzcsomag.pdf').pages),'BOM rows',len(rows))

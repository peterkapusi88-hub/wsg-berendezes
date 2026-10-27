import json,copy
from pathlib import Path
P=Path(__file__).resolve().parents[1];O=P/'R06'
base=json.loads((O/'sources/workbook_before_R06.json').read_text())['Elemregiszter'];rows=copy.deepcopy(base);rm={r[2]:r for r in rows[1:] if r[2]};changes=[]
def patch(id,fields,reason):
 r=rm[id];old=copy.deepcopy(r)
 for k,v in fields.items():r[int(k)]=v
 changes.append({'id':id,'reason':reason,'before':old[14]*old[16]+sum(old[k] or 0 for k in [17,18,19]),'after':r[14]*r[16]+sum(r[k] or 0 for k in [17,18,19]),'fields':fields})
patch('KI-044',{8:'IKEA',9:'004.507.57',10:'https://www.ikea.com/hu/hu/p/vagstranda-zsakrugos-matrac-kemeny-vilagoskek-00450757/',11:'1800×2000×280 mm',16:229900,32:229900,21:'Ellenőrzött webshopár',22:'IKEA HU 2026-10-27; komfortpróba és szállítás visszaigazolása nincs',23:'2026-10-27'},'VÅGSTRANDA pontos méret és friss ár, -30100 Ft; keménység kipróbálandó.')
patch('KI-117',{7:'2×EGLO RONDO 85264 Ø200 opálgömb + 2×Hue E27',8:'EGLO',9:'85264',10:'https://www.egloshop.hu/85264-eglo-rondo-asztali-lampa',11:'Ø200×200 mm; E27',16:21980,32:21980,22:'2×10990 Ft ellenőrzött lámpaár; 24000 Ft Hue előirányzat változatlan',23:'2026-10-27',26:'Kisebb gömb közelebb áll a célképhez; fehér talp a sötét referencia helyett.'},'FADO25cm helyett20cm Rondo; +10000Ft. Összetett csomag, nem teljes fix ajánlat.')
patch('KI-043',{7:'BED-01 egyedi kárpitozott tárolóágy, közös felnyíló kerettel',8:'Egyedi ajánlatkérés',9:'BED-01-R06',11:'2020×1800×300 mm külső, matrac1800×2000',16:250000,32:250000,21:'Becslés',22:'R06 bontás: váz80000+kárpit50000+közös keret és kétoldali emelőszerkezet80000+összeépítés40000; vasalat ajánlatra vár',26:'Fehér/kréta alacsony ágytest megtartva; oldalfiók helyett felnyíló tároló',39:'BED-01',40:'R06/drawings/R06_valtozott_szerkezetek.pdf',41:'R06_BED01_*',42:'Egyedi',43:'Tervezési befoglaló; vasalat és gyártás nincs jóváhagyva',50:.85,51:1.45},'NORDLI oldalfiókok helyett felnyíló tároló: éjjelikkel való használati ütközés csökkentése. +60100Ft becslés.')
patch('KI-051',{16:450000,32:450000,7:'Északi és déli teljes magasságú grafikás frontok és pántok',22:'Korábbi370000+80000 előirányzat a déli négy hosszú front merevítésére/pántolására; gyártói árajánlat szükséges',26:'Észak6 és dél4 folytonos magas front; délen hosszú fekete fogantyú; eredeti grafika helyett R06 próbaváltozat',40:'R06/drawings/R06_valtozott_szerkezetek.pdf'},'Déli vízszintes frontosztás elhagyva a T05 alapján; belső kapacitás megmarad. +80000Ft előirányzat.')
patch('KI-011',{9:'EGGER F243 ST76 / 4100×920×38',11:'1460×620 +1600×620 +900×620; 4100×920 nyerslapból',13:'Világosszürke Candela márvány dekor, laminált forgácslap; nem valódi kő',22:'96750Ft széles lap jelzett kereskedői ár +53250Ft szabás/él/kivágás előirányzat; széles SKU véglegesítendő',10:'https://www.okftfaaruhaz.hu/ML-EGGER-F243-ST76-4100x600x38mm-munkalap',26:'Képi kőhatás közelítése lamináttal; élek és ismétlődés látszhat. 600mm lap NEM elegendő620mm mélységre.'},'F274 beton helyett F243 finom erezetű kődekor.150000Ft csomagkeret nem változik; széles lapra külön ajánlat.')
patch('KI-012',{9:'EGGER F243 ST76 hátfal',22:'4100×640×8 jelzett59445Ft +40555Ft szabás/ragasztás/él előirányzat. Nem dupla munkadíj a KI-014-gyel; ajánlatban bontandó',26:'Azonos dekor az összes konyhanézetben; mosható hátfal, főzőlap gyártói távolságával'},'Konyha minden nézetében egységes kődekor; költség változatlan.')
patch('KI-036',{23:'2026-10-27',22:'Westwing HU pontos SKU JSON-LD:800000Ft; HU szállítás visszaigazolása nincs',41:'R06_Lennon_*',43:'Gyártói2380×1800×680; fotó/méret alapján felépített forma, nem gyári3D',26:'Alacsony, széles karú jobb sarokkanapé; a célkép szövete és párnázottsága eltérhet.'},'Pontos SKU megerősítve; új méretezett forma a régi dobozproxy helyett.')
patch('KI-028',{23:'2026-10-27',22:'Westwing HU SKU160cm259990Ft',41:'R06_Toni*',26:'160×90 ovális tölgy asztal, két hajlított laplábbal; nem a renderben esetenként megjelenő központi tömb.'},'Valódi lábszerkezetet mutató modell.')
patch('KI-029',{41:'R06_Eamy_*',43:'Gyártói55×53×75cm, ülés46cm; fotó alapján görbített háttámla rekonstrukció'},'Hajlított kőris háttámla, világosszürke zsenília és fekete acélláb a képeken is.')
patch('KI-109',{41:'R06_Somar_*',43:'Ø760×360mm búra, E27; fotó alapján rekonstruált bordás forma',26:'A gyári Somar laposabb búra, mint a konyhai render felfújt gömbje; a render igazodjon a gyárihoz.'},'A tényleges760mm Somar forma követése.')
patch('KI-076',{31:'R06: változatlan350×350×450 test; új helyX14025,Y5920mm. Fiók/ajtó mozgás részletesen ellenőrzendő.'},'Vendégszobai éjjeli a munkaszék kihúzási sávjából az ágy fejrészéhez kerül.')
patch('KI-091',{31:'R06: északi zuhanytálca déli élén keleti1000mm fixüveg,780mm névleges belépő. Kiviteli helyszíni vízzárás/üvegméret szakági jóváhagyásra vár.'},'Az örökölt, zuhanytálcán keresztbe álló üveg helyett a tálca éléhez igazított tervváltozat.')
new=[]
for id,name,amt,desc,structure in [
 ('KI-R06-01','06.2 WC feletti lamellás tölgyhatású tároló, világított fülkével',220000,'900×200×1400mm; z1300;600ajtó+300nyitottfülke. Korpusz45000+front/lamella65000+vasalat20000+LED/táp25000+szerelés65000.','B62-WC'),
 ('KI-R06-02','06.2 ág motívumos vízálló művészeti felület',110000,'900×2400mm tervi felület; 2.16m²+15%rendelési ráhagyás. Védett hátoldali nyomat, üveg/szakági rendszer50000+grafika/nyomat25000+rögzítés35000. Zuhanyzónában akasztó/pad nem kerülhet elé.','ART-B62'),
 ('KI-R06-03','06.2 fekete törölközőszárító és csatlakozás előirányzat',120000,'400×1200mm tervi befoglaló; késztermék70000+bekötés/rögzítés50000. Pontos modell, hőigény, zóna és kiállás nyitott; meglévő esetén csak igazolás után levonható.','RAD-B62')]:
 r=[None]*54;r[:8]=['A902','06.2',id,'T07','R06 új célkép','Stílus','Asztalos / szakági',name];r[8]='Ajánlatkérés';r[9]=structure+'-R06';r[11]=desc;r[14:20]=[1,'csomag',amt,0,0,0];r[21]='Becslés';r[22]=desc;r[23]='2026-10-27';r[24]='6–10 hét feltételes';r[26]='T07 alapján, hiteles geometria miatti eltérés dokumentálva';r[27]='Tervjavaslat, nem gyártási jóváhagyás';r[28]='Nincs megrendelve';r[29]='Asztalos / szakági tervező';r[31]=desc;r[32]=amt;r[34]='Tartalom megőrizve';r[39]=structure;r[40]='R06/drawings/R06_valtozott_szerkezetek.pdf';r[41]='R06_'+structure+'*';r[42]='Egyedi / jelölt';r[43]='Tervi, felmérés szükséges';r[44]='HUF';r[45]=1;r[46]='Nem ajánlat';r[47]=0;r[48]=0;r[49]=2;r[50]=.8;r[51]=1.5;rows.append(r);new.append(r)
for i,r in enumerate(rows[1:],2):
 if not r[2]:continue
 for c,f in [(20,f'=O{i}*Q{i}+SUM(R{i}:T{i})'),(33,f'=O{i}*AG{i}+SUM(R{i}:T{i})'),(52,f'=ROUND(U{i}*AY{i},0)'),(53,f'=ROUND(U{i}*AZ{i},0)')]:r[c]=f
calc=lambda r,e=False:r[14]*r[32 if e else 16]+sum(r[k] or 0 for k in [17,18,19])
tot=sum(calc(r) for r in rows[1:] if r[2]);eco=sum(calc(r,True) for r in rows[1:] if r[2]);lo=sum(round(calc(r)*(r[50] or 1)) for r in rows[1:] if r[2]);hi=sum(round(calc(r)*(r[51] or 1)) for r in rows[1:] if r[2])
summary={'main':tot,'economy':eco,'low':lo,'high':hi,'target':18000000,'reserve':2000000,'reserve_used':0,'gap':tot-18000000,'economy_gap':eco-18000000,'R05':23912890,'delta':tot-23912890,'quote_huf':0,'rows':len(rows)-1,'note':'Teljes árbecslés, nem vállalkozói ajánlat.18M teljes tartalommal nincs igazolva.'}
for n,d in [('register_R06.json',rows),('register_changes.json',changes),('register_new_rows.json',new),('budget_R06.json',summary)]: (O/'data'/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
d=json.loads((P/'R05/data/design_R05.json').read_text());d['revision']='KI-R06'
for u in d['units']:
 if u['id']=='WS-01':u['full_height_front']=True;u['visual_status']='T05:4 teljes magasságú grafikás front, hosszú fekete fogantyú';u['front_height_mm']=2837
 if u['id']=='NT-76':u['x']=14.025;u['y']=5.92
for i in d['items']:
 if i['id']=='KI-070':i['y']=4.15
 if i['id']=='KI-075':i['y']=6.70
 if i['id']=='KI-043':i.update(name='BED-01 custom lift storage',sku='BED-01-R06',proof='Tervezési méret; emelőmechanika, terhelés és nyitási mozgás szakági jóváhagyásra vár.')
 if i['id']=='KI-091':i.update(x=15.4,y=7.1,w=1000,d=8,z=.03)
(O/'data/design_R06.json').write_text(json.dumps(d,ensure_ascii=False,indent=2));print(summary)

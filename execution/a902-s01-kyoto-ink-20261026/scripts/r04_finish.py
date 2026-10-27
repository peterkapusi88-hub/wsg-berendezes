"""Reference/material sheets, concrete storage schedule, honest release manifest."""
from r04_drawing_book import *
from PIL import Image as PILImage
import csv

def picture(g,path,x,y,w):
    im=PILImage.open(path);h=w*im.height/im.width
    g.add(Image(x,y,w,h,str(reference_preview(path))));return h

def finish_cards():
    manifest=json.loads((P/'data/render_manifest.json').read_text())
    refs={m['camera']:P/m['project_path'] for m in manifest}
    refs['W01']=CP/'reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png'
    cards=[
    ('M01','W01','Médiafal: ezt a külsőt kell megőrizni','TV-01 / TV-02 / TV-03',[
    ('Képi követelmény','Sötét, egybefüggő bal torony; a torony és az alsó bútor vízszintes kapcsolata; nagy függőleges falmezők; átmenő tusgesztus; keskeny világító rés; lebegő alsó tároló.'),
    ('Javasolt kivitel','18 mm mérettartó hordozó, kétoldali kiegyenlítéssel. Matt ásványi hatású bevonat vagy annak sík nyomtatott megfelelője. A sötét torony felülete a kép alapján külön mintázandó, nem automatikusan kréta.'),
    ('Grafika és felület','A kép az elsődleges kompozíciós referencia. A vektoros rajzon lévő fekete jel csak helyfoglaló. A tényleges ecsetszélek, kopások és felületi textúra külön jóváhagyandó grafikai állományt igényelnek.'),
    ('Szerkezeti feltétel','A nagy működő front merevségét, pántolását és súlyát az asztalos igazolja. A TV a teherbíró falhoz rögzül. Oldható panel és hozzáférhető LED-táp; a torony külön függesztése szükséges.'),
    ('Átadandó minta','Legalább 600×600 mm felület, mellette 3 mm frontfuga és sarok; fekete motívum mindkét hordozón. Esti súrolófény és nappali megtekintés. Sík nyomat / texturált bevonat / relief külön árajánlati opció.'),
    ('Nyitott eltérés','A CP3 TV-01 kétajtós külsője és TV-02 frontosztása nem egyezik a választott képpel. W01/03 az új kompozíciós javaslat; a régi részletrajz nem gyártási alap ehhez.')]),
    ('M02','04','Master: a kép szerinti nyugodt szekrényfal','WN-01 / WS-01 / HB-01 / NT-L / NT-R',[
    ('Képi követelmény','Világos, keskeny frontok; a fő célképen folyamatos magasság; fekete keretezés és lábazat; finom átlós és hangsúlyos függőleges tusmotívum. Taupe–grafit, osztott kárpitos fejvég.'),
    ('Fronttechnológia [J]','19 mm festett MDF, matt greige/kréta alap és védett tusnyomat. A polcok 18 mm laminált lapok; a látható élek az alapszínnel egyező lezárást kapnak. A pontos szín nem állapítható meg a meleg képfényből.'),
    ('Új belső','WN-01-R04A: 3 belső rekesz, kívül 6 keskeny ajtó; hosszú ruhák, dupla akasztás, két lift és nyolc fiók. A kép takart széle miatt a hat ajtó tervi választás, nem bizonyított képi ajtószám.'),
    ('Fejvég [J]','18 mm hordozó + kb. 30 mm hab + vatelin és szövet a 60 mm befoglalóban. Külön levehető világos/sötét kárpitmodul, megtartott aszimmetria; felső rejtett fény hozzáférhető kábelúttal.'),
    ('Nyitási próba','A teljes magasságú ajtó alakstabilitása, pántszáma, széles nyitása és fiókkiemelése 1:1 próbával. A gardróblift karja, a lehúzó és az akasztott ruha nem ütközhet a fiókokkal.'),
    ('Minta / eltérés','Festett front + nyomat + védőlakk összeférhetősége, kárpit és grafit éjjeli minta szükséges. A WN új belseje még külön változat; az ár és Blender nem követi automatikusan.')]),
    ('M03','03','Konyha: egy anyagkészlet minden nézetben','K-01 … K-09',[
    ('Képi követelmény','Grafit alsó frontok, világos greige magas és felső elemek, világos ásványi munkalap/hátfal, sötét gépfrontok. A látható él, lábazat és fogás részlete is egyezzen.'),
    ('Tervi anyagváltozat','18 mm korpusz; 19 mm matt festett MDF front vagy pontosan mintázott gyári lap külön alternatívaként. A korábbi F274 dekor csak jelölt: nem nevezhető a képpel azonosnak mintázás nélkül.'),
    ('Fiókok','K-05 három fiók a főzés eszközeinek. K-06 két oszlopban három-három fiók. Frontosztás és belső magasság összehangolva, nem nyílóajtó-jellel. Vasalat saját szerelési hézagai alapján véglegesítendő.'),
    ('Gépek és víz','Minden kivágás a tényleges SKU beépítési rajza szerint. Szifon, mosogatógéptömlő, csapkihúzás és főzőlap szellőzés külön szerelési próba. A sütő/mikró mellett nem számítunk rejtett kamratérre.'),
    ('Napi kisgépek','Kávégép és vízforraló a pulton, a pirító csak méretpróba után. A dagasztó nehéz gép: alsó tároló, teljes kihúzással. Forró gép zárt bútorban nem működtethető gyártói jóváhagyás nélkül.'),
    ('Nyitott eltérés','A V3.3 nappaliból látható konyhát ezzel a célképpel közösen kell ellenőrizni. A frontmodulok, készülékek és munkalap anyaga még nem egységesen lezárt render–rajz–ár lánc.')]),
    ('M04','10','Fürdő: a mosdóbútor külső aránya is számít','B62-01 / B62-02',[
    ('Képi követelmény','Sötét lebegő mosdóbútor, a célképen két egymás melletti front; világos mosdófelület. A tükör melletti zárt tároló és a világított nyitott részek külön kezelendők.'),
    ('Új frontjavaslat','B62-01-R04A: 600 + 300 mm oldalankénti osztás, balra szifonos fiók, jobbra keskeny mély fiók. A 2:1 arány képi közelítés; mosdó és kiállás felmérése határozza meg a végső osztást.'),
    ('Anyag [J]','Nedvességálló hordozó, minden vágott él és furat lezárva; kétoldali matt bevonat. A „vízálló” megnevezés nem helyettesíti a gyártó rétegrendjét és az élzárási előírást.'),
    ('Használat','Balra napi kozmetikum, a szifon körül; jobbra kefe és kikapcsolt, lehűlt hajszárító. Száraz törölköző külön magas tárolóban. Üveg és falcsatlakozás szerelési hézaggal, takaríthatóan.'),
    ('Szerelés','Szifonhoz és elzárókhoz szerszámmal hozzáférhető, kivehető fiók. A falfüggesztés, mosdó tömege és tényleges falanyag szakmai ellenőrzése kötelező.'),
    ('Nyitott rész','B62-02 300 mm szélessége a teljes képi tükörfal-kompozíciót még nem írja le. A kivágás, mosdó SKU, szerelvény és világítás egyeztetése nélkül gyártás nem indulhat.')]),
    ('M05',None,'A nem renderelt szobák Kyoto Ink részletei','W52-01 / W53-01 / ENT-01 / WC-01',[
    ('Közös forma','Sík, matt, visszafogott világos front; grafit belső keret vagy lábazat; azonos 3 mm tervezett fugacsalád. Új, hangsúlyos tusmotívumot nem adunk hozzá automatikusan.'),
    ('05.2 gardrób / gyerekszoba','A magas ruhakapacitás megtartandó. Állítható polcok és átcsavarozható gyerekrúd; négy fiók. Játék alacsonyan, a magas rész szezonális ruháé; később a belső elemek cserélhetők, a korpusz marad.'),
    ('05.3 vendég / munka','Sekély akasztós rész előre kihúzható rúddal. A4 iratokhoz megfelelő polcmagasság; négy fiók irodaszernek és vendégtextilnek. Az ágy, szék és ajtó együtt használhatósága még nyitott geometriai kérdés.'),
    ('Előtér','Napi kabát és cipő, póráz, kulcs és tiszta törlő elérhető magasságban. A pad stabil szerkezetet és levehető kárpitot kap; a nedves cipő nem a ruhás rekeszbe kerül.'),
    ('Azonos részletek','Korpusz 18 mm; a gyári lap látható éle 2 mm ABS javaslattal. Festett MDF élein csiszolt, festett zárás; nem kötelező rá ABS. Pánt, fiók és fogás szobánként, funkció szerint választható.'),
    ('Rögzítendő döntés','A színkód, pontos lapgyártó, kárpit és vasalat még mintára/ajánlatra vár. Ezek javasolt új formák; nem állítjuk róluk, hogy korábban elfogadott render mutatta őket.')])]
    source=[]
    for code,ref,name,ids,notes in cards:
        d,g=sheet(code+' / '+name,ids+' - képi cél és kivitelezési követelmény','referenciakép / anyaglap',code)
        if ref:
            path=refs[ref];picture(g,path,14,113,190)
            source.append({'sheet':code,'path':str(path.relative_to(P)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
            yy=103
            for lab,col in [('világos matt / mintázandó',CREAM),('grafit matt / mintázandó',GRAPHITE),('fekete tus / grafikai master nyitott',INK)]:
                rect(g,14,yy-5,20,8,col);txt(g,39,yy-2,lab,2.8);yy-=16
            wrap(g,14,47,'Az eredeti kép változtatás nélkül szerepel. A mellette látható színmezők semleges tervi jelölések, nem mért festékszínek vagy nyomdai színminták.',188,2.7,4)
        else:
            yy=222
            for lab,col in [('matt világos front',CREAM),('grafit lábazat / keret',GRAPHITE),('világos belső',CORE)]:
                rect(g,25,yy-15,135,22,col);txt(g,25,yy-22,lab,3);yy-=50
        yy=250
        for label,body in notes:
            txt(g,220,yy,label,3.0,True);yy=wrap(g,220,yy-6,body,184,2.7,3.9)-7
        save(d,code+'_referencia_anyag',ids,'referencia és anyagspecifikáció')
    (O/'data/material_reference_sources.json').write_text(json.dumps(source,ensure_ascii=False,indent=2))


def bath_option():
    u=copy.deepcopy(next(x for x in D['units'] if x['id']=='B62-01'))
    u.update(id='B62-01-R04A',name='Mosdóbútor / egymás melletti frontjavaslat',modules=[600,300],front_modules=[600,300],front='grafit matt, nedvességálló hordozó, teljes éllezárás',visual_status='Kép szerinti oldalankénti frontok; a 600/300 osztás és szifon kivágás javaslat, még nem gyártási adat.')
    bs=[]
    for j,m in enumerate([600,300]):
        b=copy.deepcopy(u['cp3_bays'][0]);b.update(id=f'B62-01-R04A-B{j+1:02}',bay=j+1,offset=600*j,module_w=m,clear_w=m-36,purpose='Napi pipere / szifonkivágás' if j==0 else 'Hajszárító / kefék',drawers=1,drawer_z=[35],drawer_inner_mm=[m-136,400,220],shelves_mm=[],rails_mm=[],lift_rails_mm=[],lights_mm=[],rod_lengths_mm=[])
        b.update(rail_m=0,shelf_m2=0,drawer_l=round((m-136)*400*220/1e6,3))
        bs.append(b)
    u['cp3_bays']=bs;u['notes']='Két egymás melletti fiók; a bal fiókból a szifon tényleges burkolóterét le kell vonni. Nincs fiókba épített dugalj igazolva.'
    u['capacity']={'drawer_l_before_siphon':sum(b['drawer_l'] for b in bs),'siphon_deduction':'UNKNOWN'}
    (O/'data/B62-01_R04A_alternative.json').write_text(json.dumps(u,ensure_ascii=False,indent=2))
    cabinet_sheet(u);detail_sheet(u)

def media_units():
    changed=[]
    for uid in ['TV-01','TV-02']:
        u=copy.deepcopy(next(x for x in D['units'] if x['id']==uid))
        u['id']=uid+'-R04A';u['full_height_front']=True
        u['visual_status']='A választott médiafalhoz igazított frontjavaslat; felület és működés mintára, árra és felmérésre vár.'
        if uid=='TV-01':
            u['front_modules']=[700];u['front']='sötét grafit ásványi hatás + tusnyomat; nem kréta'
            u['hardware']='Egy 697×2327 mm névleges front [J], belül két polcos rekesz. Pántszám, nyitási oldal, merevítés és vasalat gyártói méretezésre vár. 19 mm MDF, 750 kg/m³ számítási sűrűséggel kb. 23,1 kg bevonat nélkül; nem mért ajtótömeg.'
            u['notes']='A képi cél miatt az eddigi két felső front helyett egy folytonos ajtó. A belső középosztó és polcok megmaradnak. Oldható polc és külön toronyrögzítés.'
        else:
            u['modules']=[700,650,650,650,650];u['front_modules']=u['modules'][:]
            off=0
            for i,b in enumerate(u['cp3_bays']):
                mw=u['modules'][i];b.update(id=u['id']+f'-B{i+1:02}',module_w=mw,clear_w=mw-36,offset=off)
                b['shelf_m2']=len(b['shelves_mm'])*(mw-36)*b['clear_d']/1e6;off+=mw
            u['notes']='700 + 4×650 mm alsó modul; első front a toronyhoz igazítva. Az AV-gép mérete, ajtónyitás és szellőzőnyílás még egyeztetendő. Játékdoboz a jobb két rekeszben.'
        u['capacity']={k:round(sum(b[k] for b in u['cp3_bays']),3) for k in ['rail_m','shelf_m2','drawer_l']}
        changed.append(u);cabinet_sheet(u);detail_sheet(u)
    (O/'data/TV_R04A_frontjavaslat.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2))


def use_schedule():
    # Every bay remains traceable; geometric volumes are not assumed contents.
    d=json.loads((O/'data/design_R04.json').read_text());rows=[]
    for u in d['units']:
        for b in u['cp3_bays']:
            q=f"{b['rail_m']:.2f} m rúd; {b['shelf_m2']:.2f} m² polc; {b['drawers']} fiók / {b['drawer_l']:.1f} l"
            rows.append({'unit':u['id'],'bay':b['id'],'use':b['purpose'],'width_mm':b['clear_w'],'depth_mm':b['clear_d'],'capacity':q,'basis':'CP3 rekeszadat, R04 tisztázott felirat; felszerelés és használati hézag még levonandó'})
    with (O/'data/Mit_hova_rekeszenkent.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
    groups=[('Master háló', ['WN-01','WS-01','NT-L','NT-R']),('05.2 és 05.3', ['W52-01','W53-01']),('Konyha', ['K-01','K-02','K-03','K-05','K-06','K-07']),('Nappali, előtér és fürdők', ['TV-01','TV-02','ENT-01','B62-01','B62-02','B61-01','WC-01','NT-64','NT-76'])]
    for idx,(name,ids) in enumerate(groups):
        selected=[r for r in rows if r['unit'] in ids]
        # Two sheets if needed, no tiny typography to squeeze content.
        for pi in range(0,len(selected),10):
            code=f'U{idx+1:02}-{pi//10+1}'
            doc,g=sheet('Mit hová? / '+name,'Rekeszenkénti használati jegyzék - a javasolt új WN/B62 változat külön lapján szerepel.','táblázat',code)
            yy=251
            for r in selected[pi:pi+10]:
                txt(g,14,yy,r['bay'],3,True);txt(g,99,yy,r['use'],2.9,True)
                txt(g,99,yy-6,f"Szabad szélesség × mélység: {r['width_mm']}×{r['depth_mm']} mm. {r['capacity']}",2.8)
                line(g,14,yy-10,403,yy-10,GREY,.1);yy-=20
            wrap(g,14,37,'A liter a tervezett fiókbelső téglatestének térfogata, nem behelyezhető tárgyak száma. A polcfelület nem a padlóval összeadható terület. A készülékes és szifonos rekeszekből a gép és a szerelés helyét le kell vonni.',390,2.8,4)
            save(doc,code+'_hasznalat',name,'rekeszenkénti használati jegyzék')
    # Concrete quantities with stated example dimensions and no double counting.
    items=[
    ['WN-01-R04A','Hosszú ruhák','897 mm rúd','9–13 db','50–70 mm / ruha; 25% üres hely'],
    ['WN-01-R04A','Rövid ruhák','2453 mm rúd','30–52 db','35–60 mm / ruha; 25% üres hely'],
    ['WS-01-B01/B02','Cipők','15 megadott polclap, 559 mm széles','22 pár tervezett','2×250 mm/párhely/polc; 30 elméleti hely, 25% tartalék. A legfelső lapot nem számoljuk cipőpolcnak: ebből további 4 hely levonandó, így 19 pár célszám.'],
    ['WS-01-B03','Táskák','alsó négy magasabb polczóna','3–6 db','250×180×280 mm próbatáska, állítva; nagy táska 1 hely / szint. Fiókokban kiegészítők.'],
    ['WS-01-B04','Porszívó / vasalódeszka','559×423×1780 mm célrekesz','1 + 1','250×250×1250 és 350×100×1500 mm; a deszka hátul, a porszívó előtte. Eléréshez ki kell venni a gépet.'],
    ['W52-01','Extra akasztós ruhák','1,437 m rúd összesen','17–30 db','35–60 mm átlag; 25% üres hely. Hosszú/rövid vegyes ruhánál külön újraszámolandó.'],
    ['W52-01-B04','Játékdoboz','két alsó, elérhető polczóna','2–4 doboz','250×350×250 mm; két hely / zóna; a szekrény alja és az első polc vizsgálandó.'],
    ['W53-01-B02','A4 iratok','5 magas polcköz, 564 mm szélesség','26 széles mappa','80 mm mappagerinc; 7/polc×5=35 elméleti, 25% tartalék. 143 mm-es legfelső résbe nem fér álló A4.'],
    ['K-05','Evőeszköz / edény','3×464×450×170 mm fiók','egy evőeszköz tálca + 2 edényfiók','400×400 mm próbatálca. 280 mm edény két darabja egymás mellé nem fér; egymásba rakás csak valódi készlettel.'],
    ['K-06','Élelmiszer / előkészítés','6×364×450×170 mm fiók','legfeljebb 6 alacsony rendszerező','300×400×140 mm példadoboz; ez a fiók teljes helyét foglalja, nem azon felüli kapacitás.'],
    ['AT8-01','Tartalék készlet','8×800×380 mm polc névlegesen','12 próbadoboz','350×300 mm alapterület; 16 helyből 25% szabad. Ritka gép ugyanezekből a helyekből foglal.'],
    ['AT-FR','Második fagyasztó','597×675×1455 mm gépjelölt','1 készülék','Belső liter / fiókszám nem igazolt; pontos SKU és kézikönyv szükséges.'],
    ['T-0-26','Bőrönd','2 alsó, magas polcrekesz','3 próbabőrönd','350×500×700 mm; 4 helyből 25% üres. Teljes külső méret kerékkel és fogantyúval.'],
    ['T-0-26','Szezonális doboz','6 felső polcszint','9 próbadoboz','350×500 mm alapterület; 12 helyből 25% szabad. A magasság a polcszintekhez igazítandó.'],
    ['T-0-26','Kerékpár','700×1150 mm helyfoglalás, 2000 mm magas','1 felnőtt bicikli','Függőlegesen a déli fal jobb sarkán; tartó SKU, ajtó és kiemelés még nyitott.']]
    # Shoe calculation excludes the two top reserve shelves explicitly.
    items[2][3]='19 pár';items[2][4]='13 tényleges cipőszint ×2 pár=26 hely; 25% üresen: 19 pár. A felső két tartalékpolc nem számít cipőhelynek. 300 mm széles párnál csak 1 pár/szint.'
    for pi in range(0,len(items),6):
        code=f'U05-{pi//6+1}';doc,g=sheet('Mennyit tehetünk bele? / méretpéldák','Tervezési forgatókönyv; nem tulajdonosi leltár és nem garantált termékbeférés.','méret és használati példa',code)
        yy=250
        for loc,what,dim,count,calc in items[pi:pi+6]:
            txt(g,14,yy,loc+' / '+what,3.3,True);txt(g,403,yy,count,3.3,True,anchor='end')
            txt(g,14,yy-7,dim,2.9);wrap(g,14,yy-14,calc,385,2.9,4.2)
            line(g,14,yy-28,403,yy-28,GREY,.1);yy-=35
        save(doc,code+'_mennyiseg','lakás + két tároló','tárgyak és férőhelyek')
    (O/'data/Targyak_es_ferohelyek.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))

if __name__=='__main__':
    bath_option();media_units();finish_cards();use_schedule()
    (O/'data/supplement_index.json').write_text(json.dumps(SHEETS,ensure_ascii=False,indent=2))
    w=PdfWriter()
    for s in SHEETS:w.append(str(O/s['pdf']))
    w.compress_identical_objects(remove_identicals=True,remove_orphans=True)
    w.write(str(O/'materials/A902_R04_Kulso_anyag_hasznalat.pdf'))
    print('Kiegészítő lapok:',len(SHEETS))

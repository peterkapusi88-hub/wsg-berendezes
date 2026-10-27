from r04_drawing_book import *
from PIL import Image as PILImage
import csv

ST=json.loads((CP/'data/storage_CP3.json').read_text())
GUIDE=[]

def room_plan(g,st,x,y,s,bike=False):
    w,h=st['w']*s,st['d']*s
    rect(g,x,y,w,h,HexColor('#f4f1e9'),INK,.7)
    if st['pillar']:
        a,b,c,e=st['pillar'];rect(g,x+a*s,y+b*s,c*s,e*s,GRAPHITE)
    for it in st['items']:
        if bike and it['id']=='T-LUG':continue
        item_x=900 if bike and it['id']=='T-R2' else it['x']
        xx=x+item_x*s;yy=y+it['y']*s;ww=it['w']*s;hh=it['d']*s
        rect(g,xx,yy,ww,hh,HexColor('#c7d5ce') if it['kind']=='freezer' else EDGE)
        txt(g,xx+ww/2,yy+hh/2,it['id'],2.7,True,anchor='middle')
        if it['kind']=='freezer':
            rect(g,xx,yy+hh,ww,600*s,None,RED,.25)
            txt(g,xx+ww/2,yy+hh+300*s,'600 nyitás [J]',2.2,c=RED,anchor='middle')
    if bike:
        # Bicycle vertically stored: footprint is a design envelope, not an actual rack SKU.
        xx=x+1750*s;yy=y+50*s
        rect(g,xx,yy,700*s,1150*s,None,RED,.45)
        line(g,xx,yy,xx+700*s,yy+1150*s,RED,.15,[1,1]);line(g,xx,yy+1150*s,xx+700*s,yy,RED,.15,[1,1])
        txt(g,xx+350*s,yy+575*s,'bicikli [J]',2.6,True,c=RED,anchor='middle')
        txt(g,x+420*s,y+600*s,'ki- / beemelés',2.5,anchor='middle')
        txt(g,x+420*s,y+470*s,'szabad helye',2.5,anchor='middle')
    # Unknown door: show a dashed access zone, not a fabricated built opening.
    ax=x+w-750*s if st['id']=='AT8-01' else x+100*s
    ay=y+h if st['id']=='AT8-01' else y
    line(g,ax,ay,ax+750*s,ay,RED,.8,[2,1]);txt(g,ax+375*s,ay+(4 if st['id']=='AT8-01' else -5),'ajtó helye / nyitása [H]',2.3,c=RED,anchor='middle')
    hd(g,x,x+w,y-12,y,str(st['w'])+' [J]');vd(g,y,y+h,x-8,x,str(st['d'])+' [J]')

def rack_elev(g,x,y,width,height,levels,labels,s=1/20,colour=white):
    rect(g,x,y,width*s,height*s,None)
    rect(g,x,y,20*s,height*s,colour);rect(g,x+(width-20)*s,y,20*s,height*s,colour)
    for i,z in enumerate(levels):
        rect(g,x,y+z*s,width*s,20*s,colour)
        if i<len(labels):wrap(g,x+2,y+(z+90)*s,labels[i],width*s-4,2.4,3.2)
    hd(g,x,x+width*s,y-8,y,str(width));vd(g,y,y+height*s,x-7,x,str(height))

def storage_sheets():
    for st in ST:
        isat=st['id']=='AT8-01'
        d,g=sheet(st['id']+' / tároló és használati hely','A kész belméretek és a nyílások felmérésre várnak. A terület nem kész szélesség/hossz.','alaprajz 1:20 / nézet 1:20',st['id']+'/01')
        txt(g,25,253,'BERENDEZÉSI ALAPRAJZ [J]',3.2,True);room_plan(g,st,28,135,.05)
        txt(g,210,253,'POLCKIOSZTÁS / HASZNÁLAT',3.2,True)
        if isat:
            rack_elev(g,224,150,800,1600,[100,590,1080,1570],['ital / nehéz készlet','konzerv / liszt','zárt élelmiszer','könnyű tartalék'])
            rack_elev(g,298,150,800,1600,[100,590,1080,1570],['ritka kisgépek','konyhai tartalék','dobozok','könnyű kellék'])
            notes=[
            '2× JONAXEL 504.199.72, 800×380×1600 mm; négy gyári polcszint. A rajzi polcszintek közelítő elhelyezések, a gyári szerelési rajz dönt.',
            'Középen a második fagyasztó tervezett helye: 597×675×1455 mm. FNd 4625 / GN46Vd25 névütközés: pontos EAN és kézikönyv még szükséges.',
            '600 mm nyitási próbaborítékkal a szemközti szabad sáv 545 mm. Ez nem teljes használati PASS; a valódi ajtó/fiók és a kezelő helyét együtt kell ellenőrizni.',
            'Vegyszer nem kerül az élelmiszer fölé. A napi tisztítószer a lakásban marad. A tároló klímáját és a fagyasztó szellőzését helyszínen kell ellenőrizni.',
            'Polconként 25 kg a gyártói érték; a falrögzítés külön helyszíni feladat. 2×23 000 Ft webshopár, szállítás és rögzítés nélkül. Ellenőrzés: 2026-10-27.'
            ]
        else:
            rack_elev(g,224,145,850,1900,[100,850,1300,1850],['bőrönd / nehéz holmi','szezonális doboz','sport / tartalék','könnyű textil'],colour=GRAPHITE)
            rack_elev(g,298,145,850,1900,[100,850,1300,1850],['bőrönd / nehéz holmi','ritka kisgépek','kültéri kellék','könnyű textil'],colour=GRAPHITE)
            notes=[
            'A korábbi változat két BROR elemet és külön bőröndhelyet tartalmaz. Bicikli ebben még nem volt elhelyezve.',
            '2× BROR 596.194.05, 850×550×1900 mm, elemenként 4 polc. Állítható polcszintek; a legalsó szabad rekesz nagy bőröndnek készül.',
            'A tényleges ajtóhely ismeretlen, ezért a berendezés feltételes. A déli nyílás csak rajzi hozzáférési feltételezés.',
            'A biciklis változat a 02 lapon látható: mindkét polc megmarad, a külön padlón álló bőröndhely átkerül az alsó polcokra. A fordulás és ajtóhely ellenőrzendő.',
            'Gyártói ár 47 500 Ft / elem, 4 polccal; a gyártó 130 kg/polc értéket ad. A falrögzítés, összeépítés és tényleges padlóterhelés külön ellenőrzendő.'
            ]
        yy=111
        for n in notes:yy=wrap(g,18,yy,n,385,2.8,4.0)-4
        save(d,st['id']+'_01',st['id'],'tároló alaprajz és falnézet')
    st=ST[1]
    d,g=sheet('T-0-26 / bicikli és nagy holmik','Kapacitást őrző elrendezési javaslat - ajtó, kiemelés és rögzítés ellenőrzendő.','1:20 / szemléltetés','T-0-26/02')
    room_plan(g,st,30,134,.05,True)
    txt(g,28,250,'1 BICIKLI + 2 BROR / FELTÉTELES VÁLTOZAT',3.2,True)
    txt(g,210,250,'BICIKLI FÜGGŐLEGES TÁROLÁSA [J]',3.2,True)
    # Front elevation of a vertical bicycle including wheels, handlebar envelope.
    x=247;y=134;s=.05
    for z in [350,1550]:g.add(Circle(x,y+z*s,350*s,fillColor=None,strokeColor=INK,strokeWidth=.35))
    line(g,x,y+350*s,x+12,y+850*s,INK,.45);line(g,x+12,y+850*s,x,y+1550*s,INK,.45);line(g,x,y+350*s,x,y+1050*s,INK,.45)
    line(g,x-17.5,y+1450*s,x+17.5,y+1450*s,INK,.5)
    vd(g,y,y+2000*s,x-30,x,'2000 [J]');hd(g,x-17.5,x+17.5,y-10,y,'700 [J]')
    yy=111
    for n in [
    'Tervezési példa: 1 felnőtt bicikli 2000×700×1200 mm tárgybefoglalóval; falon állítva 1150×700 mm helyfoglalási próbával. Nem a tulajdonos lemért biciklije.',
    'A bicikli a déli fal jobb sarkán, 700×1150 mm alaprajzi borítékban áll; az eredeti próbához képest 90°-kal fordítva. Az ajtó és teljes kiemelési/fordulási út még nem igazolt.',
    'Mindkét BROR megmarad: T-R2 50 mm-rel balra kerül, a polcok összeérnek. A külön T-LUG padlóhely megszűnik: a bőröndök az alsó magas polcrekeszekbe kerülnek, dobozhelyet foglalva.',
    'A 8 gyári polc 8×840×540 mm névleges felülete 3,629 m². A bicikli és a T-R2 tervezési borítéka érinti egymást, nincs tartalékhézag. Szerelvény, belméret vagy mozgástér miatt módosítás kellhet; ez nem PASS.',
    'Kerékpártartó SKU, kerék/gumi-kompatibilitás, tömeg, falanyag és rögzítés még nyitott. A tartó + szerelés külön árazandó; nettó megtakarítás jelenleg nem állítható.'
    ]: yy=wrap(g,18,yy,n,385,2.8,4.1)-4
    save(d,'T-0-26_02_bicikli','T-0-26','biciklis alternatíva')

def guide_page(number,title,subtitle):
    d=Drawing(210*MM,297*MM);g=Group();g.scale(MM,MM);d.add(g)
    rect(g,0,0,210,297,HexColor('#faf8f3'),None)
    txt(g,15,280,'KYOTO INK / A-902',3.2,True,c=GREY)
    txt(g,15,268,title,6.2,True);wrap(g,15,258,subtitle,180,3.2,4.5)
    line(g,15,20,195,20,GREY,.13);txt(g,15,13,'R04 / 2026-10-27 - tervezési útmutató, nem rendelési lista',2.6)
    txt(g,195,13,str(number)+' / 5',2.8,anchor='end');return d,g
def card(g,x,y,w,title,body):
    txt(g,x,y,title,3.7,True);return wrap(g,x,y-7,body,w,3.1,4.4)-7
def pic(g,path,x,y,w):
    im=PILImage.open(path);hh=w*im.height/im.width;g.add(Image(x,y,w,hh,str(reference_preview(path))));return hh
def guide_save(d,i):
    f=O/'owner'/('oldal_'+str(i));renderPDF.drawToFile(d,str(f.with_suffix('.pdf')));renderSVG.drawToFile(d,str(f.with_suffix('.svg')));GUIDE.append(f.with_suffix('.pdf'))

def owner_guide():
    d,g=guide_page(1,'Szép kívül. Használható belül.','A választott látványt bútorra, anyagra és mindennapi használatra fordítjuk le.')
    photo=CP/'reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png'
    pic(g,photo,15,133,180)
    yy=124
    yy=card(g,15,yy,180,'Mi lesz benne különleges?','Az összefüggő tusmotívumos médiafal, a csendes grafit–greige felületek és a rétegzett fény. A működő tárolást a nyugodt külső mögé rejtjük. A kép hangulatcél; az összes részlet még nem kivitelezésre lezárt.')
    yy=card(g,15,yy,180,'Mennyibe kerülhet és miért?','A teljes lakás, kültér és két tároló CP3 előirányzata 23,25 M Ft. Az új R04 változat külön becslése 23,79 M Ft, kb. 20,14–31,86 M Ft sávval: 5,79 M Ft-tal a 18 M keret felett. A 2 M tartalék érintetlen. A CP3-ban 2,35 M Ft webshopár és 0 Ft írásos ajánlat van; az R04 felárai döntően becslések. Az Excelben még a CP3 van kiválasztva.')
    card(g,15,yy,180,'Megéri?','A napi használatot javító szekrénybelső és javítható szerkezet értékes. A drágább felület felárát 1:1 minta és ajánlat alapján érdemes eldönteni. Ingatlanérték-növekedést vagy biztos megtérülést a terv nem igazol.')
    guide_save(d,1)

    d,g=guide_page(2,'Ruhák, cipők, táskák','A napi holmik a lakásban maradnak. A két külön tároló a tartalékoké és a ritkábban használt tárgyaké.')
    u=json.loads((O/'data/WN-01_R04A_alternative.json').read_text())
    elevation(g,u,53,141,.035,True);txt(g,18,130,'Master WN-01-R04A: külön vizsgált új belső, még nem kiválasztott.',2.6,c=RED)
    yy=120
    yy=card(g,15,yy,180,'Master: mi hová kerül?','Balra hosszú ruhák és 2 lapos fiók; középen dupla akasztás, felül lift; jobbra 6 fiók és rövid ruhák liften. Az új változatban 3,35 m hasznos rúd és kb. 437 liter fiók van. A régi WN-01: 3,03 m és 310 liter. A polcfelület viszont 3,39-ről 2,04 m²-re csökken; ez látható kompromisszum.')
    yy=card(g,15,yy,180,'Ez körülbelül mennyi ruha?','25% szabad helyet hagyva a javasolt WN-01-R04A kb. 9–13 hosszú és 30–52 rövid akasztós ruhának ad helyet. Számítás: hosszú ruhánál 50–70 mm, rövidnél 35–60 mm vállfahely. Vastag kabáttal kevesebb fér el; ez tervezési példa, nem leltár.')
    card(g,15,yy,180,'A többi szekrény feladata','WS-01: cipők, táskák és napi takarítóeszközök. 05.2: extra ruhák, négy fiók, alul játékdobozok, később áthelyezhető gyerekrúd. 05.3: vendégruha, iratok és irodaszerek; a jelenlegi ágy–szék ütközés még nyitott. A részletes rekeszméretek az asztalos lapokon vannak.')
    guide_save(d,2)

    d,g=guide_page(3,'A hétköznapi dolgok helye','A tárgyakat használat szerint csoportosítjuk; a látható polc nem jelent automatikusan szabad tárolóhelyet.')
    entries=[
    ('Porszívó + vasalódeszka','WS-01/B04, 559×423 mm alapterület, kb. 1780 mm magas szabad hely. Próbatárgyak: állóporszívó 250×250×1250; összecsukott deszka 350×100×1500 mm. A konkrét géppel ellenőrizendő.'),
    ('Takarítószerek','WS-01/B04 felső, zárható rekeszében, kivehető cseppfogó tálcán. Élelmiszertől és textiltől elkülönítve. Nedves felmosó előbb száradjon ki; nem zárt ruhásszekrényben szárítjuk.'),
    ('Napi kávé, pirító, vízforraló','A konyhában kijelölt kb. 600 mm pultsávon. Nem biztos, hogy mindhárom egyszerre elfér: 3×200 mm gépszélesség már kitölti a sávot, szellőzés nélkül. Gépméret és fedélnyitás alapján választandó kiosztás.'),
    ('Edények, evőeszköz, ritka gépek','K-05/K-06 fiókjaiban főzéshez és előkészítéshez közel. Nehéz dagasztó a lakásban alsó tárolóban, a ritka tartalékgép AT8-01 alsó polcán. A kért nagy kamraszekrény még pultveszteséggel járna.'),
    ('Hajszárító, kefék, kozmetikum','B62-01: a szifon terét levonva kell a fiókot osztani. A képhez igazított R04A két egymás melletti fiókot mutat. A régi két egymás fölötti fiók összehasonlításként maradt meg. A fiókdugalj gyártói/villamos egyeztetést igényel.'),
    ('Cipő, kutyás felszerelés, játék','Előtér: napi kabát, cipő, póráz és tiszta törlő. WS-01 cipős polcán 559 mm szélességre két 250 mm-es párhely tervezhető; csizmához külön magas rekesz. Játék: W52-B04 és a médiafal alsó tárolója, kivehető könnyű dobozokban.')]
    yy=239
    for h,b in entries:yy=card(g,15,yy,180,h,b)
    guide_save(d,3)

    d,g=guide_page(4,'AT8-01: tartalék és fagyasztó','A 8. emeleti, dokumentáltan 4,57 m²-es tároló. A kész méretek és a két tervi dugalj helye ellenőrizendő.')
    room_plan(g,ST[0],25,137,.06)
    yy=118
    yy=card(g,15,yy,180,'Minek van itt helye?','Két fehér JONAXEL polc: összesen 8 polcszint. Balra ital és élelmiszertartalék; jobbra ritkábban használt konyhai gépek, tálak és dobozok. A nehéz dolgok alul, a könnyű tartalék felül. Vegyszer nem kerül az élelmiszer fölé.')
    yy=card(g,15,yy,180,'Mennyit lehet elhelyezni?','A 8×800×380 mm névleges polcfelület felső becslése 2,43 m²; a keretek levonandók. Egy szinten legfeljebb két 350×300 mm-es próbadoboz: 16 helyből 4 maradjon szabadon, tehát 12 ilyen doboz tervezhető. A gépek ugyanebből a helyből foglalnak, nem ezen felül.')
    card(g,15,yy,180,'A második fagyasztó','A középső hely 597×675×1455 mm-es készülékjelölttel szerepel. Pontos típus, szellőzés és ajtónyitás még nincs lezárva. A 600 mm-es nyitási próbában csak 545 mm marad szemben: ezt a tényleges fiókkal és állóhellyel kell ellenőrizni.')
    guide_save(d,4)

    d,g=guide_page(5,'T-0-26: bicikli és szezonális holmik','A garázsszinti tároló 4,00 m². A 2500×1600 mm keret és az ajtó a jelen tervben feltételes.')
    room_plan(g,ST[1],25,144,.06,True)
    yy=125
    yy=card(g,15,yy,180,'A bicikli helyét is megrajzoltuk','A déli fal jobb sarkán 1 függőlegesen tárolt bicikli helye látható. Elfordítottuk a próbát, így mindkét BROR megmarad; a jobb polc 50 mm-rel balra kerül. A bicikli és a polc között nincs tartalékhézag: az ajtóval, falrögzítéssel és kiemeléssel együtt még ellenőrizni kell.')
    yy=card(g,15,yy,180,'Bőröndök és dobozok','A két alsó magas rekeszben összesen 4 darab 350×500×700 mm-es próbabőrönd férőhelye van; 25% tartalékkal 3-mal számoljunk. A felső 6 polcon 12 darab 350×500 mm-es dobozhelyből 9-et töltsünk meg. A bicikli miatt a külön padlón álló bőröndhely megszűnik.')
    yy=card(g,15,yy,180,'Miért tart hónapokig? Mi jöhet közbe?','A felmérés, anyagminta, ajánlat, gyártás és beépítés egymásra épül. A korábbi terv 14–16 hetet irányzott elő a döntésektől; ez nem visszaigazolt határidő. A rossz méret, elhúzódó mintázás vagy későn kiválasztott vasalat újragyártást okozhat.')
    card(g,15,yy,180,'Hogyan lehet gyorsítani?','Egy közös felmérésen rögzítsük a lakást, két tárolót és kiállásokat. A médiafal mintája és a gardrób működési mintája párhuzamosan készüljön. Azonos rajzrevízióra kérjünk összehasonlítható ajánlatokat; rendelés csak a változat, ár és átfutás jóváhagyása után.')
    guide_save(d,5)
    w=PdfWriter()
    for f in GUIDE:w.append(str(f))
    w.write(str(O/'owner/A902_R04_Minek_hol_lesz_helye.pdf'))

if __name__=='__main__':
    storage_sheets();owner_guide()
    (O/'data/storage_drawing_index.json').write_text(json.dumps(SHEETS,ensure_ascii=False,indent=2))
    print('3 tárolólap és 5 tulajdonosi oldal elkészült')

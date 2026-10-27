"""Dimensioned vector drawing revision. Existing CP3 remains an archived input.
No generated drawing is a field survey or a production approval.
"""
from pathlib import Path
import json, math, copy, hashlib, textwrap
from reportlab.graphics.shapes import Drawing, Group, Rect, Line, String, Circle, Polygon, PolyLine, Path as VPath, Image
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

P=Path(__file__).resolve().parents[1]; O=P/'R04'; CP=P/'CP3'
D=json.loads((CP/'data/design_CP3.json').read_text())
L=json.loads((CP/'data/belso_vilagitas.json').read_text())
HARD=json.loads((CP/'data/vasalat.json').read_text())
pdfmetrics.registerFont(TTFont('KI','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('KIB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
MM=72/25.4; INK=HexColor('#252522'); GREY=HexColor('#777772'); RED=HexColor('#b24332')
CREAM=HexColor('#c5bbae'); GRAPHITE=HexColor('#45423e'); CORE=HexColor('#ede9e1'); EDGE=HexColor('#bdb6aa')
SHEETS=[]; BOUNDS=[]

def reference_preview(path):
    # Document embedding format only. The original PNG and its hash are retained.
    from PIL import Image as PI
    dest=O/'qa/previews';dest.mkdir(exist_ok=True)
    out=dest/(hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]+'.jpg')
    if not out.exists():PI.open(path).convert('RGB').save(out,quality=95,subsampling=0)
    return out

def line(g,x,y,X,Y,c=INK,w=.18,dash=None):g.add(Line(x,y,X,Y,strokeColor=c,strokeWidth=w,strokeDashArray=dash))
def rect(g,x,y,w,h,fill=None,c=INK,lw=.18):
    if w<0 or h<0:raise ValueError((x,y,w,h))
    g.add(Rect(x,y,w,h,fillColor=fill,strokeColor=c,strokeWidth=lw))
def txt(g,x,y,s,size=2.6,bold=False,c=INK,anchor='start'):
    g.add(String(x,y,str(s),fontName='KIB' if bold else 'KI',fontSize=size,fillColor=c,textAnchor=anchor))
def wrap(g,x,y,s,width,size=2.6,leading=3.8):
    words=str(s).split(); buf=''
    for word in words:
        test=(buf+' '+word).strip()
        if pdfmetrics.stringWidth(test,'KI',size)>width and buf:
            txt(g,x,y,buf,size);y-=leading;buf=word
        else:buf=test
    if buf:txt(g,x,y,buf,size);y-=leading
    return y
def dot(g,x,y,c=INK):g.add(Circle(x,y,.55,fillColor=c,strokeColor=None))
def leader(g,x,y,X,Y,label,c=INK):
    dot(g,x,y,c);line(g,x,y,X,Y,c,.13);txt(g,X+1,Y+.7,label,2.4,c=c)
def hd(g,x,X,y,objy,label,size=2.4):
    line(g,x,objy,x,y-1,GREY,.08);line(g,X,objy,X,y-1,GREY,.08);line(g,x,y,X,y,INK,.12)
    for a in (x,X):line(g,a-.8,y-.8,a+.8,y+.8,INK,.15)
    txt(g,(x+X)/2,y+1,label,size,anchor='middle')
def vd(g,y,Y,x,objx,label,size=2.3):
    line(g,objx,y,x+1,y,GREY,.08);line(g,objx,Y,x+1,Y,GREY,.08);line(g,x,y,x,Y,INK,.12)
    for a in (y,Y):line(g,x-.8,a-.8,x+.8,a+.8,INK,.15)
    t=Group();t.add(String(0,0,str(label),fontName='KI',fontSize=size,fillColor=INK,textAnchor='middle'));t.transform=(0,1,-1,0,x-1,(y+Y)/2);g.add(t)
def hatch(g,x,y,w,h):
    rect(g,x,y,w,h,CORE)
    # Clipped diagonal hatch within each thin material strip.
    for a in range(int((w+h)/1.8)+1):
        q=a*1.8; x1=max(0,q-h);y1=q-x1;x2=min(w,q);y2=q-x2
        if 0<=y1<=h and 0<=y2<=h:line(g,x+x1,y+y1,x+x2,y+y2,GREY,.07)
def title(g,name,sub,scale,page):
    rect(g,5,5,410,287,None,INK,.2)
    txt(g,12,283,'A-902  /  KYOTO INK',3.4,True)
    txt(g,12,276,name,5,True);txt(g,12,270,sub,2.6)
    line(g,12,265,408,265,GREY,.12)
    rect(g,270,7,138,19,None,INK,.15)
    txt(g,274,21,'KI-R04 / 2026-10-27',2.7,True);txt(g,404,21,page,2.7,True,anchor='end')
    txt(g,274,16,'A3 - 100% nyomtatás - mm - '+scale,2.5)
    txt(g,274,11,'AJÁNLATI / EGYEZTETÉSI TERV - NEM GYÁRTÁSI KIADÁS',2.15,c=RED)
    txt(g,12,17,'[D] korábbi tervadat  [J] új tervezési javaslat  [H] helyszíni / gyártói ellenőrzés',2.3)
    txt(g,12,12,'Szín a képernyőn tájékoztató. Anyag és nyomat fizikai mintával fogadható el.',2.3)
def sheet(name,sub,scale,page):
    d=Drawing(420*MM,297*MM);g=Group();g.scale(MM,MM);d.add(g);title(g,name,sub,scale,page);return d,g
def save(d,name,unit,kind):
    f=O/'drawings'/name;renderPDF.drawToFile(d,str(f.with_suffix('.pdf')));renderSVG.drawToFile(d,str(f.with_suffix('.svg')))
    SHEETS.append({'unit':unit,'kind':kind,'pdf':str(f.with_suffix('.pdf').relative_to(O)),'svg':str(f.with_suffix('.svg').relative_to(O))})
def arc(g,cx,cy,r,a,b,c=GREY):
    pts=[]
    for i in range(25):
        v=math.radians(a+(b-a)*i/24);pts.extend((cx+r*math.cos(v),cy+r*math.sin(v)))
    g.add(PolyLine(pts,strokeColor=c,strokeWidth=.12,strokeDashArray=[1,.8],fillColor=None))

def palette(u):
    s=u['front'].lower()
    if 'kréta/grafit' in s:return CREAM
    return GRAPHITE if any(k in s for k in ['grafit','antracit','sötét']) else CREAM
def coat(g,x,y,w,h):
    # Scale examples, not a claim about actual personal inventory.
    pts=[x+w*.36,y,x+w*.18,y-h*.08,x,y-h*.28,x+w*.14,y-h*.34,x+w*.26,y-h*.20,x+w*.25,y-h,x+w*.75,y-h,x+w*.74,y-h*.20,x+w*.86,y-h*.34,x+w,y-h*.28,x+w*.82,y-h*.08,x+w*.64,y]
    g.add(Polygon(pts,strokeColor=GREY,strokeWidth=.11,fillColor=white));line(g,x+w*.5,y,x+w*.5,y-h, GREY,.09)
def ink_diagram(g,x,y,w,h,mode='wardrobe'):
    # Deliberately tagged as a composition study, not the approved print master.
    p=VPath(fillColor=INK,strokeColor=None)
    if mode=='wall':
        p.moveTo(x+w*.27,y+h*.05);p.lineTo(x+w*.28,y+h*.96);p.lineTo(x+w*.33,y+h*.95);p.lineTo(x+w*.31,y+h*.10);p.closePath()
        q=[x,y+h*.35,x+w*.08,y+h*.42,x+w*.60,y+h*.62,x+w*.62,y+h*.60,x+w*.09,y+h*.38]
    else:
        p.moveTo(x+w*.79,y+h*.10);p.lineTo(x+w*.81,y+h*.90);p.lineTo(x+w*.83,y+h*.93);p.lineTo(x+w*.84,y+h*.08);p.closePath()
        q=[x,y+h*.72,x+w*.12,y+h*.70,x+w,y+h*.45,x+w,y+h*.43,x+w*.12,y+h*.69]
    g.add(p);g.add(Polygon(q,fillColor=INK,strokeColor=None))

def new_data():
    d=copy.deepcopy(D);d['revision']='KI-R04-DRAWING';d['source_commit']='a85802a93d0b9c1d5f46bc798da90e6fdd4bca77'
    d['status']='Részletes rajzi felülvizsgálat; változások még nem zárt Excel–Blender kiadás'
    changes=[]
    for u in d['units']:
        bays=u['cp3_bays'];u['legacy_notes']=u['notes'];u['legacy_interior']=u.get('interior',[])
        if bays:
            u['notes']='; '.join(b['id']+': '+b['purpose'] for b in bays)
            u['drawers']=sum(b['drawers'] for b in bays);u['shelves']=sum(len(b['shelves_mm']) for b in bays)
            u['interior']=[{'bay':b['bay'],'shelves_mm':b['shelves_mm'],'rails_mm':b['rails_mm'],'drawers':b['drawers']} for b in bays]
        u['revision']='KI-R04-DRAWING';u['date']='2026-10-27'
        u['front_modules']=u['modules'][:]
        u['visual_status']='Korábbi méretezett kiosztás; kép szerinti felület, mintajóváhagyás nyitott'
        if u['id'] in ['TV-01','WN-01','WS-01','B62-01']:
            u['visual_status']='KÉP–RAJZ ELTÉRÉS NYITOTT: a részletezett CP3 belső nem tekinthető renderazonos külsőnek'
        if u['kind']=='panel':
            u['hardware']='Oldható függesztősín és kiemelés elleni biztosítás. Falrögzítés [H]. Nincs pánt/fióksín.'
            u['plinth']='Nem releváns';u['handle']='Nem releváns';u['service']='Kábelhez hozzáférő, oldható mező, ahol szükséges.'
        changes.append({'unit':u['id'],'change':'Sablonszöveg és rekeszadat összehangolva; típushelyes nézetek és új rajzi szerkesztés','visual_status':u['visual_status']})
    (O/'data/design_R04.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
    (O/'data/change_log.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
    return d

def elevation(g,u,x,y,s,internal=False):
    w=u['w']*s;h=u['h']*s;cab=u['kind']=='cabinet';bays=u['cp3_bays']
    rect(g,x,y,w,h,white if internal else palette(u))
    if not internal:
        if 'tus' in u['front'].lower():ink_diagram(g,x,y,w,h,'wall' if u['id'].startswith('TV') else 'wardrobe')
        offset=0
        for j,m in enumerate(u['front_modules']):
            bx=x+offset*s;mw=m*s;rect(g,bx+1.5*s,y+1.5*s,mw-3*s,h-3*s,None)
            drawer_front = cab and u['h']<=900 and any(b['drawers'] for b in bays)
            if drawer_front:
                b=bays[min(j,len(bays)-1)]
                n=b['drawers']; bottom=80 if u['id'].startswith('K-') else 0
                top=u['h']-38 if u['id'].startswith('K-') else u['h']
                if n>1:
                    for k in range(1,n):line(g,bx,y+(bottom+(top-bottom)*k/n)*s,bx+mw,y+(bottom+(top-bottom)*k/n)*s,INK,.2)
                if n==1 and b['shelves_mm']:
                    line(g,bx,y+b['shelves_mm'][0]*s,bx+mw,y+b['shelves_mm'][0]*s,INK,.2)
                txt(g,bx+mw/2,y+h/2,'kihúzható',1.8,c=white,anchor='middle')
            elif cab:
                # Door operation line, separate from the face material.
                mid=bx+mw if j%2==0 else bx
                other=bx if j%2==0 else bx+mw
                line(g,other,y+2,mid,y+h/2,GREY,.1,[1,.8]);line(g,mid,y+h/2,other,y+h-2,GREY,.1,[1,.8])
            offset+=m
        if u['h']>2400 and not u.get('full_height_front'):line(g,x,y+2360*s,x+w,y+2360*s,GREY,.15)
        if u['kind']=='upholstery':
            rect(g,x+u['modules'][0]*s,y,u['modules'][-1]*s,h,GRAPHITE)
            for q in range(0,int(w),2):line(g,x+q,y,x+q,y+h,Color(.3,.3,.3,alpha=.13),.07)
        if u['kind']=='table':
            rect(g,x,y,w,h,GRAPHITE)
            if u['id']=='DS52':rect(g,x+18*s,y,(u['w']-36)*s,(u['h']-38)*s,white)
        return
    if not bays:return
    for b in bays:
        bx=x+b['offset']*s;mw=b['module_w'];cw=b['clear_w'];depth=b['clear_d']
        hatch(g,bx,y,18*s,h);hatch(g,bx+(mw-18)*s,y,18*s,h)
        hatch(g,bx+18*s,y,cw*s,18*s);hatch(g,bx+18*s,y+h-18*s,cw*s,18*s)
        for j,z in enumerate(b['shelves_mm']):
            hatch(g,bx+18*s,y+z*s,cw*s,18*s)
            txt(g,bx+20*s,y+z*s+1.5,'P'+str(j+1),1.9,c=GREY)
        for j,z in enumerate(b['rails_mm']):
            lift=z in b['lift_rails_mm'];line(g,bx+38*s,y+z*s,bx+(mw-38)*s,y+z*s,INK,.65)
            txt(g,bx+mw*s/2,y+z*s+1.8,('LIFT' if lift else 'RÚD')+' +'+str(z),2.1,anchor='middle')
            if lift:
                for xx in (bx+45*s,bx+(mw-45)*s):rect(g,xx,y+(z-560)*s,20*s,420*s,EDGE)
                line(g,bx+mw*s/2,y+z*s,bx+mw*s/2,y+(z-750)*s,GREY,.35)
            if u['d']>=550:
                clen=1400 if 'Hosszú' in b['purpose'] else 800
                for k in range(3):coat(g,bx+(60+k*(mw-120)/3)*s,y+(z-65)*s,min(190,(mw-120)/3)*s,clen*s)
            else:
                coat(g,bx+mw*.15*s,y+(z-65)*s,mw*.70*s,min(900,z-100)*s)
                txt(g,bx+mw*s/2,y+(z-350)*s,'előre húzható',1.9,anchor='middle')
        for j,z in enumerate(b['drawer_z']):
            dh=b['drawer_inner_mm'][2];rect(g,bx+30*s,y+z*s,(mw-60)*s,(dh+20)*s,white)
            rect(g,bx+40*s,y+(z+10)*s,(mw-80)*s,dh*s,None,GREY,.1)
            txt(g,bx+mw*s/2,y+(z+dh*.45)*s,'F'+str(j+1),2.1,anchor='middle')
        for z in b['lights_mm']:
            ln=min(u.get('fixture_length',460),cw-50);line(g,bx+(mw-ln)*s/2,y+z*s,bx+(mw+ln)*s/2,y+z*s,RED,.6)
        for z in b['rails_mm']:
            lab=('LIFT' if z in b['lift_rails_mm'] else 'RÚD')+' +'+str(z)
            tw=pdfmetrics.stringWidth(lab,'KI',2.1)
            rect(g,bx+mw*s/2-tw/2-.5,y+z*s+1.4,tw+1,2.8,white,None)
            txt(g,bx+mw*s/2,y+z*s+1.8,lab,2.1,anchor='middle')
        # Clearly identified indicative belongings in open shelf zones.
        if not b['rails_mm'] and not b['drawers']:
            if 'háztart' in b['purpose'].lower():
                rect(g,bx+50*s,y+100*s,200*s,1300*s,None,GREY,.15)
                rect(g,bx+280*s,y+100*s,min(210,cw-300)*s,1550*s,None,GREY,.15)
                txt(g,bx+mw*s/2,y+900*s,'porszívó / deszka',1.8,anchor='middle')
            else:
                for z in b['shelves_mm'][:4]:
                    if z+200<u['h']:rect(g,bx+50*s,y+(z+18)*s,max(60,cw-90)*s,180*s,CORE,GREY,.1)
        txt(g,bx+mw*s/2,y+h+2.8,'B'+str(b['bay']),2.5,True,anchor='middle')
        hd(g,bx+18*s,bx+(mw-18)*s,y-5,y,str(cw),2.1)
    if u['id']=='K-01':
        for z,hh,l in [(600,595,'sütő'),(1280,382,'mikró')]:rect(g,x+18*s,y+z*s,564*s,hh*s,GRAPHITE);txt(g,x+w/2,y+(z+hh/2)*s,l,2.3,c=white,anchor='middle')
    if u['id']=='K-02':rect(g,x+18*s,y+80*s,564*s,1780*s,CORE);txt(g,x+w/2,y+900*s,'hűtőhely',2.5,anchor='middle')
    if u['id']=='K-03':
        rect(g,x+150*s,y+580*s,500*s,240*s,None,RED);line(g,x+400*s,y+600*s,x+400*s,y+250*s,RED,.6)
        txt(g,x+w/2,y+350*s,'szifon + tömlő',2.2,c=RED,anchor='middle')
    if u['id'] in ['B62-01','B61-01']:
        rect(g,x+w*.40,y+u['h']*.45*s,w*.20,u['h']*.55*s,None,RED,.3)
        txt(g,x+w/2,y+h+3,'szifonkivágás: sablon [H]',2.2,c=RED,anchor='middle')

def cabinet_sheet(u):
    # Fixed, actual print scales; large main elevations dominate the page.
    scale=next(n for n in [10,15,20,25,30,40] if u['w']/n<=125 and u['h']/n<=135)
    s=1/scale;w=u['w']*s;h=u['h']*s;x=27;X=192;y=102
    d,g=sheet(u['id']+' / '+u['name'],'Színezett homlokzat - méretezett belső - alaprajz - metszet','1:'+str(scale),u['id']+'/01')
    txt(g,x,255,'A-A ELÖLNÉZET',3.2,True);txt(g,X,255,'A-A BELSŐ / SZERKEZET',3.2,True)
    elevation(g,u,x,y,s);elevation(g,u,X,y,s,True)
    if not u['cp3_bays']:
        # Show construction of non-storage components rather than an empty cabinet.
        if u['kind']=='panel':
            for j,m in enumerate(u['modules']):
                q=sum(u['modules'][:j]);rect(g,X+q*s,y,m*s,h,CORE);txt(g,X+(q+m/2)*s,y+h/2,'P'+str(j+1),3,anchor='middle')
            txt(g,X,y+h+3,'Hordozómezők - grafika külön lapon',2.3)
        elif u['kind'] in ['table','bench','shelf']:
            hatch(g,X,y+h-min(18*s,h),w,min(18*s,h))
            if u['kind']!='shelf':
                hatch(g,X,y,18*s,max(0,h-18*s));hatch(g,X+w-18*s,y,18*s,max(0,h-18*s))
            txt(g,X+2,y+h/2,'Szerkezeti elv [J]',2.6)
        elif u['kind']=='upholstery':
            rect(g,X,y,w,h,CREAM);txt(g,X+3,y+h/2,'Kárpitozott hordozó / rétegrend a 02 lapon',2.3)
        else:txt(g,X+3,y+h/2,'Gyári géphely, nem tárolókapacitás',2.5)
    for xx in (x,X):
        pos=0
        for mw in u['modules']:hd(g,xx+pos*s,xx+(pos+mw)*s,y-11,y,str(mw),2.2);pos+=mw
        hd(g,xx,xx+w,y-18,y,str(u['w'])+' [D]')
    vd(g,y,y+h,x-9,x,str(u['h']))
    # Section, kept inside the right hand column.
    sx=337;sd=u['d']*s
    txt(g,sx,255,'B-B METSZET',2.9,True);rect(g,sx,y,sd,h,None)
    if u['cp3_bays']:
        b=u['cp3_bays'][0];hatch(g,sx,y,19*s,h);hatch(g,sx+sd-38*s,y,8*s,h)
        for z in b['shelves_mm']:hatch(g,sx+19*s,y+z*s,max(0,sd-57*s),18*s)
        for z in b['rails_mm']:g.add(Circle(sx+sd/2,y+z*s,.7,fillColor=INK,strokeColor=None))
        zs=[0]+b['shelves_mm']+[u['h']]
        for lo,hi in zip(zs,zs[1:]):
            if (hi-lo)*s>5:vd(g,y+lo*s,y+hi*s,sx+sd+6,sx+sd,str(hi-lo),2)
    else:hatch(g,sx,y,max(.7,sd),h)
    hd(g,sx,sx+sd,y-11,y,str(u['d']))
    # Top view + true operation arcs. Assumptions explicitly printed.
    ps=min(s,1/25);pw=u['w']*ps
    py=53;ph=u['d']*ps;txt(g,x,81,'ALAPRAJZ / NYITÁS - 1:'+str(round(1/ps)),3,True)
    rect(g,x,py,pw,ph,CORE)
    if u['kind']=='cabinet' and not (u['h']<=900 and any(b['drawers'] for b in u['cp3_bays'])):
        pos=0
        for j,mw in enumerate(u['front_modules']):
            bx=x+pos*ps;rr=mw*ps;hinge=bx if j%2==0 else bx+rr
            arc(g,hinge,py,rr,270,360 if j%2==0 else 180)
            line(g,hinge,py,hinge,py-rr,GREY,.12,[1,.8]);pos+=mw
        txt(g,x+pw+5,py+ph/2,'90° szemléltető nyitás;',2.2)
        txt(g,x+pw+5,py+ph/2-4,'fióknál 155° vizsgálandó.',2.2)
    elif any(b['drawers'] for b in u['cp3_bays']):
        length=max(b['runner_mm'] for b in u['cp3_bays'])*ps
        rect(g,x,py-length,pw,length,None,RED,.15)
        txt(g,x+pw+5,py+ph/2,'Fiók kihúzási helye [J]',2.2)
    hd(g,x,x+pw,py-5,py,str(u['w']))
    txt(g,192,73,'SZÍN ÉS KIVITEL',3,True)
    wrap(g,192,67,u['front']+'. '+u['visual_status'],149,2.6,3.5)
    if 'tus' in u['front'].lower():txt(g,192,49,'A fekete alak kompozíciós jelzés, NEM jóváhagyott nyomat.',2.3,c=RED)
    txt(g,192,36,'A ruhák és tárgyak méretvezető példák; nem valós leltár.',2.3)
    save(d,u['id']+'_01',u['id'],'nézetek')

def detail_sheet(u):
    d,g=sheet(u['id']+' / anyag, belső méret és szerelés','A rajzi kiosztáshoz tartozó előzetes asztalos-specifikáció','részletek 1:2 / jegyzék',u['id']+'/02')
    # Type-specific specification, no cabinet hinge text on artwork or tables.
    edge='Laminált korpusz: látható élen 2 mm ABS, belsőn 1 mm [J]. Festett MDF front: csiszolt és festéssel lezárt él; nem automatikusan ABS. Vizes helyen teljes furat- és éllezárás.' if u['kind']=='cabinet' else u['edge']
    rows=[('Költségsor',', '.join(u['cost'])),('Méretforrás',u['dimension_source']),('Front / felület',u['front']),('Élzárás',edge),('Szerviz',u['service'])]
    if u['kind']=='cabinet':
        rows.insert(2,('Korpusz','18 mm laminált bútorlap; 19 mm MDF front; 8 mm hátlap. Pontos dekor és fronttechnológia mintával.'))
        rows += [('Nyitás / vasalat',u['hardware']),('Rögzítés','Falanyaghoz méretezett bútorfüggesztés / borulásgátlás [H]; rejtett vezetékek bemérése.')]
    elif u['kind']=='panel':
        rows += [('Hordozó','A teljes '+str(u['d'])+' mm befoglaló a hordozóval és tartóval együtt értendő. Rétegrend technológiai döntésre vár; nem 18+19+8 mm.'),('Rögzítés','Rejtett oldható mechanikus sín; nem ragasztjuk lezárt elektromos szerviz elé.'),('Grafika','Kép szerinti kompozíció a cél. A nyomdakész eredeti hiánya nyitott tétel; jelen diagram nem nyomdai master.')]
    elif u['kind']=='upholstery':rows += [('Rétegrend [J]','18 mm hordozó + 30 mm hab + vatelin/textil, a 60 mm befoglalóban; szövet és hab 1:1 mintával.'),('Rögzítés','Levehető kárpitmodulok; fény és kábel a hozzáférhető felső csatlakozásnál.')]
    else:rows += [('Rétegrend [J]','18 mm lapból dobozolt szerkezet; matt grafit bevonat/laminátum. Élfuga és lábazat mintadarabon.'),('Korlát','A kőszerű rendertextúra nem tömörkő-előírás. Kőre váltás külön tömeg- és költségellenőrzés.')]
    yy=252
    for label,value in rows:
        txt(g,12,yy,label,2.8,True);yy=wrap(g,55,yy,value,142,2.6,3.6)-4
    # Enlarged actual section of front, internal space, rear and accessible channel.
    txt(g,235,252,'D1 / RÉTEG ÉS SZERVIZ - 1:2 [J]',3,True)
    if u['kind']=='cabinet':
        xx=241;by=208;hatch(g,xx,by,9.5,29);hatch(g,xx+45,by,4,29)
        rect(g,xx+49,by,15,29,None,GREY)
        hd(g,xx,xx+9.5,by-7,by,'19 front');hd(g,xx+45,xx+49,by-7,by,'8 hát',2.1);hd(g,xx+49,xx+64,by-15,by,'30 kábel [J]')
        txt(g,xx+19,by+14,'belső tér',2.6);leader(g,xx+57,by+25,xx+83,by+32,'levehető fedél')
        wrap(g,235,181,'A metszet részlet, a belső tér megszakítva. A 30 mm szervizsáv a gardróbmélységben van, nem plusz helyiségméret.',169,2.6)
    else:
        rect(g,240,208,20,28,EDGE);rect(g,264,208,9,28,CREAM);line(g,273,208,273,236,RED,.4)
        wrap(g,281,230,'Hordozó / oldható kötés / látható felület. Rétegvastagság a tényleges technológia szerint; ez részletelv.',116,2.7)
    fixtures=u.get('lighting_fixtures',[f for f in L['fixtures'] if f['unit']==u['id']]);drivers=u.get('lighting_drivers',[f for f in L['drivers'] if f['unit']==u['id']])
    txt(g,235,161,'D2 / FÉNY ÉS KAPCSOLÁS',3,True)
    if fixtures:
        for i,(lab,w) in enumerate([('Betáp [H]',28),('Táp / szerviz',38),('Érzékelő + fény',48)]):
            xx=235+i*54;rect(g,xx,142,w,10,CORE);txt(g,xx+2,146,lab,2.4)
            if i<2:line(g,xx+w,147,xx+54,147,RED,.3)
        yy=133
        for v in drivers:yy=wrap(g,235,yy,f"{v['rating_w']} W táp: {v['watts']} W terhelés ({v['load_percent']}%). {v['sku']}",165,2.5,3.5)-2
        yy=wrap(g,235,yy,'Ajtónyitásra önálló belső fény. A Hue hangulatfénytől független működés; közvetlen Hue-párosítás nem igazolt.',165,2.5,3.5)
        txt(g,235,yy-2,str(len(fixtures))+' lámpa; pontos pozíció és cikkszám a fényjegyzékben.',2.5)
    else:wrap(g,235,151,'Ehhez az elemhez nincs külön belső lámpa a CP3 jegyzékben. Külső/dekorfény csak a kapcsolt költségsor és külön szerelési rajz szerint.',165,2.7)
    # Function-driven schedule rather than generic repeated text.
    txt(g,12,108,'REKESZJEGYZÉK / TERVI NETTÓ MÉRETEK',3,True)
    line(g,12,103,404,103,GREY,.15)
    cols=[12,94,134,199,261,340]
    for xx,lab in zip(cols,['Rekesz és funkció','Sz × mély','Polc z (alsó sík)','Rúd z / lift','Fiók belméret / db','Kihúzás']):txt(g,xx,99,lab,2.4,True)
    yy=91
    for b in u['cp3_bays']:
        wrap(g,cols[0],yy,b['id']+' '+b['purpose'],79,2.3,3.2)
        txt(g,cols[1],yy,f"{b['clear_w']}×{b['clear_d']}",2.5)
        wrap(g,cols[2],yy,', '.join(map(str,b['shelves_mm'])) or '-',61,2.3,3.2)
        wrap(g,cols[3],yy,', '.join(map(str,b['rails_mm']))+(' / L '+','.join(map(str,b['lift_rails_mm'])) if b['lift_rails_mm'] else '') or '-',57,2.3,3.2)
        txt(g,cols[4],yy,('×'.join(map(str,b['drawer_inner_mm']))+' / '+str(b['drawers'])) if b['drawers'] else '-',2.4)
        txt(g,cols[5],yy,str(b['runner_mm']) if b['drawers'] else '-',2.4);yy-=12
    if not u['cp3_bays']:wrap(g,12,91,u['notes'],385,2.8)
    txt(g,12,32,'A gyártási méret a kiválasztott vasalat hézagaival, felmérés és mintázás után adható ki.',2.6,c=RED)
    save(d,u['id']+'_02',u['id'],'specifikáció')

def media_wall():
    d,g=sheet('W01 / választott médiafal - teljes kompozíció','A 2026-10-27-én kiválasztott kép alapján. A látható forma megtartandó.','1:20 / vizuális egyeztetés','W01/03')
    x=30;y=83;s=1/20
    # Complete wall, including the former separated tower and floating base.
    rect(g,x,y+150*s,3300*s,400*s,GRAPHITE)
    rect(g,x,y+550*s,700*s,2330*s,GRAPHITE)
    rect(g,x+700*s,y+550*s,2600*s,2330*s,CREAM)
    ink_diagram(g,x,y+550*s,3300*s,2330*s,'wall')
    for z in [700,1350,2000,2650]:line(g,x+z*s,y+150*s,x+z*s,y+550*s,INK,.25)
    for z in [700,1350,2000,2650]:line(g,x+z*s,y+550*s,x+z*s,y+2880*s,GREY,.16)
    rect(g,x+1190*s,y+1050*s,1453*s,834*s,GRAPHITE,black,.35)
    for a,b,c,e in [(700,550,700,2880),(700,2880,3300,2880),(0,150,3300,150)]:line(g,x+a*s,y+b*s,x+c*s,y+e*s,RED,.65)
    hd(g,x,x+3300*s,y-12,y,'3300 [D]');vd(g,y,y+2880*s,x-10,x,'2880 [D]')
    txt(g,x,y-22,'Felső front: egybefüggő megjelenés [J]. Alsó front: 700 + 4×650 [J].',2.7)
    txt(g,x,y-28,'Ez a változat eltér a régi TV-01 kétajtós / TV-02 600–750-es osztásától.',2.7,c=RED)
    txt(g,230,249,'MEGVALÓSÍTÁSI ELV',3.4,True)
    yy=241
    notes=[
    'A 700 mm-es torony összefüggő felső frontja a választott látványt követi. A nyitási mód, ajtótömeg, merevítés és pántkészlet külön gyártói méretezésre vár.',
    'A grafit alsó bútor 150 mm-rel a padló felett lebeg. A torony és a TV saját falrögzítést kap; nem a dekorpanel hordja a televíziót.',
    'A front mögött működő tároló marad. A képen nem látható nyitás és kábelút nem tekinthető a kép által igazoltnak.',
    'Felületjavaslat: merev, sík hordozó; matt ásványi hatású, finom textúrájú bevonat; grafika kontrollált nyomattal vagy sablonos felvitellel. Reliefet a kép alapján nem írunk elő.',
    'A fekete rajz itt kompozíciós tanulmány. A képpel egyező végleges tusgrafika külön grafikai munka és 1:1 részletminta; nincs jóváhagyott nyomdai master.',
    'Kötelező minta: front és panel találkozása, grafika folytonossága, 3 mm fuga, súrolófény. A szín jóváhagyása nappali és esti fényben.',
    'A korábbi médiafal-előirányzatot az új fronttal és bevonattal újra kell árazni. Jelen lap nem állít költségazonosságot vagy gyártási jóváhagyást.'
    ]
    for n in notes:yy=wrap(g,230,yy,n,172,2.8,4.1)-5
    save(d,'W01_03_valasztott_mediafal','W01','választott képhez igazított kompozíció')

def wardrobe_option():
    # A complete internally consistent alternative for narrow full-height fronts.
    u=copy.deepcopy(next(u for u in D['units'] if u['id']=='WN-01'))
    u['id']='WN-01-R04A';u['name']='Master / keskeny, teljes magasságú frontváltozat'
    u['full_height_front']=True;u['modules']=[973,974,973];u['front_modules']=[486.5,486.5,487,487,486.5,486.5]
    u['visual_status']='6 keskeny front [J]; a célkép takart bal széle miatt a frontszám nem felmért adat. Külön összevetendő változat.'
    src=u['cp3_bays'];new=[];offset=0
    specs=[('Hosszú ruhák + 2 fiók',[2360],[2110],[],[100,290],130),('Dupla akasztás / felső lift',[1120,2360],[1040,2160],[2160],[],150),('6 fiók / rövid ruhák liften',[2360],[2160],[2160],[100,290,480,670,860,1050],150)]
    for j,(purpose,sh,ro,li,dz,dh) in enumerate(specs):
        mw=u['modules'][j];cw=mw-36;b=copy.deepcopy(src[0]);b.update(id=f'WN-01-R04A-B{j+1:02}',bay=j+1,offset=offset,module_w=mw,clear_w=cw,purpose=purpose,shelves_mm=sh,rails_mm=ro,lift_rails_mm=li,drawers=len(dz),drawer_z=dz,drawer_inner_mm=[cw-100,450,dh],lights_mm=[z-30 for z in sh]+[2790])
        b['rod_lengths_mm']=[cw-(160 if z in li else 40) for z in ro];b['rail_m']=sum(b['rod_lengths_mm'])/1000;b['shelf_m2']=len(sh)*cw*543/1e6;b['drawer_l']=len(dz)*(cw-100)*450*dh/1e6
        new.append(b);offset+=mw
    u['cp3_bays']=new;u['capacity']={k:round(sum(b[k] for b in new),3) for k in ['rail_m','shelf_m2','drawer_l']};u['notes']='; '.join(b['purpose'] for b in new)
    u['hardware']='CONERO 805–988 mm jelölt a 938/937 mm rekeszhez; 0,5–12 kg régebbi gyártói adat, aktuális készlet és mozgásrajz szükséges. Belső fiók: széles nyitású pánt, két ajtó egyidejű nyitása.'
    u['fixture_length']=710
    u['lighting_fixtures']=[{'id':b['id']+'-L'+str(j+1),'unit':u['id'],'bay':b['id'],'z':z,'length':710,'watts':3.5,'sku':'205.894.85','unit_price_huf':6490,'status':'gyártói termékadat ellenőrizve; egyedi dupla ajtó érzékelése próba'} for b in new for j,z in enumerate(b['lights_mm'])]
    u['lighting_drivers']=[{'rating_w':30,'watts':24.5,'load_percent':81.7,'sku':'TRÅDFRI 603.426.56 + FÖRNIMMA 504.468.81; aktuális elérhetőség ellenőrizendő'}]
    u['lighting_cost_status']='7×6490=45430 Ft lámpa; táp, kábel és szerelés a korábbi csomaggal egyeztetendő, nem teljes beépített ár.'
    (O/'data/WN-01_R04A_alternative.json').write_text(json.dumps(u,ensure_ascii=False,indent=2))
    # Do not silently select this layout or replace current cost/model.
    cabinet_sheet(u);detail_sheet(u)
    return u

def main():
    d=new_data()
    for u in d['units']:cabinet_sheet(u);detail_sheet(u)
    media_wall();a=wardrobe_option()
    (O/'data/drawing_index.json').write_text(json.dumps(SHEETS,ensure_ascii=False,indent=2))
    w=PdfWriter()
    for f in SHEETS:w.append(str(O/f['pdf']))
    w.compress_identical_objects(remove_identicals=True,remove_orphans=True)
    (O/'archive').mkdir(exist_ok=True)
    w.write(str(O/'archive/A902_R04_elozo_kiosztas_osszehasonlitas.pdf'))
    print('Pages',len(SHEETS),'WN alternate capacity',a['capacity'])
if __name__=='__main__':main()

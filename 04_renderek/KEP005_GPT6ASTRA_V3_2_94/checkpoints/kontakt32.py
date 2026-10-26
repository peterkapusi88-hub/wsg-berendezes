"""Stílusonkénti A/B kontaktlap: soronként egy kamera, bal A, jobb B; az elfogadott (legutolsó nem-FAIL) verzió."""
import json,os,re
from PIL import Image,ImageDraw,ImageFont
W='/home/claude/work'; O=W+'/out32/img/'
L=json.load(open(W+'/out32/naplo.json'))
fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
CAMS=['Cam_12','Cam_02','Cam_03','Cam_04','Cam_11','Cam_10']
slots={}
for k,v in L.items():
    m=re.match(r'(\d+)_([AB])(?:_(v\d))?$',k); nr,var,ver=m.group(1),m.group(2),m.group(3) or 'v1'
    if int(nr)>30: continue
    sty=re.search(r'A902_(S1\d)_([A-Za-z]+)',v['kep']); cam=re.search(r'(Cam_\d+)',v['kep']).group(1)
    key=(sty.group(1),sty.group(2),cam,var)
    ok=not v['qa'].startswith(('FAIL','SKIPPED')) and os.path.exists(O+v['kep'])
    prev=slots.get(key)
    if ok and (prev is None or int(ver[1:])>prev[0]): slots[key]=(int(ver[1:]),v['kep'],v['qa'])
    elif key not in slots and not ok: slots.setdefault(('MISS',)+key,(0,None,v['qa']))
styles=sorted({(k[0],k[1]) for k in slots if k[0]!='MISS'})
w=900; h=int(w*992/1586); out=[]
for s,name in styles:
    rows=[c for c in CAMS if any((s,name,c,x) in slots for x in 'AB') or ('MISS',s,name,c,'A') in slots or ('MISS',s,name,c,'B') in slots]
    sheet=Image.new('RGB',(2*w+30,70+len(rows)*(h+40)),'white'); d=ImageDraw.Draw(sheet)
    d.text((10,14),f'A-902 · {s} {name} · V3.2 · A = eredeti Astra | B = profi fotóalapú · KONCEPCIÓ – NEM VALIDÁLT',fill='black',font=fb)
    y=70
    for c in rows:
        for i,var in enumerate('AB'):
            x=10+i*(w+10); sl=slots.get((s,name,c,var))
            if sl:
                im=Image.open(O+sl[1]).convert('RGB').resize((w,h)); sheet.paste(im,(x,y+30))
                d.text((x,y+4),f'{c} · {var} · v{sl[0]}',fill='black',font=fs)
            else:
                d.rectangle([x,y+30,x+w,y+30+h],fill=(235,235,235)); m=slots.get(('MISS',s,name,c,var))
                d.text((x,y+4),f'{c} · {var} · HIÁNYZIK',fill=(170,0,0),font=fs)
                d.text((x+20,y+60),(m[2][:60] if m else 'még nem generált'),fill=(120,0,0),font=fs)
        y+=h+40
    p=f'/mnt/user-data/outputs/V32_{s}_{name}_kontaktlap_AB.jpg'; sheet.save(p,quality=82); out.append(p)
print('\n'.join(out))

"""Extra képek A/B kontaktlapja (X01–X17): soronként egy extra, bal A, jobb B."""
import json,re
from PIL import Image,ImageDraw,ImageFont
W='/home/claude/work'; O=W+'/out32/img/'
L=json.load(open(W+'/out32/naplo.json'))
fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
X=[f'X{i:02d}' for i in range(1,18)]
w=900; out=[]
for part,ids in (('1',X[:9]),('2',X[9:])):
    hs=[]
    for x in ids:
        im=Image.open(O+L[x+'_A']['kep']); hs.append(int(w*im.height/im.width))
    sheet=Image.new('RGB',(2*w+30,70+sum(h+40 for h in hs)),'white'); d=ImageDraw.Draw(sheet)
    d.text((10,14),f'A-902 · V3.2 EXTRÁK {part}/2 · A = eredeti Astra | B = profi fotóalapú · KONCEPCIÓ – NEM VALIDÁLT',fill='black',font=fb)
    y=70
    for x,h in zip(ids,hs):
        for i,v in enumerate('AB'):
            e=L[x+'_'+v]; m=re.search(r'A902_(S1\d)_([A-Za-z]+)_EXTRA_(Cam_[A-Za-z0-9_]+?)_A__',e['kep'])
            im=Image.open(O+e['kep']).convert('RGB').resize((w,h)); sheet.paste(im,(10+i*(w+10),y+30))
            d.text((10+i*(w+10),y+4),f'{x} · {m.group(1)} {m.group(2)} · {m.group(3)} · {v}',fill='black',font=fs)
        y+=h+40
    p=f'/mnt/user-data/outputs/V32_EXTRA_{part}_kontaktlap_AB.jpg'; sheet.save(p,quality=80); out.append(p)
print('\n'.join(out))

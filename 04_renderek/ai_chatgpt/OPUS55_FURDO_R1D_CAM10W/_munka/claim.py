#!/usr/bin/env python3
# claim.py <nr> <statusz> <chat_url> <kuldve> [geometria] [megjegyzes] [verzio]
import sys,os,csv,json,hashlib,shutil
H=os.path.expanduser('~/mnt/Downloads'); D=os.path.join(H,'WSG_FURDO_R1D_RENDEREK')
a=sys.argv; nr,st,url,sent=a[1:5]; geo=a[5] if len(a)>5 else ''; note=a[6] if len(a)>6 else ''; ver=a[7] if len(a)>7 else 'v1'
p=[x for x in json.load(open(os.path.join(D,'plan.json'))) if x['nr']==nr and x['verzio']==ver][0]
fn=p['cel_fajl']; dst=os.path.join(D,fn); res={'nr':nr,'fajl':fn}
if st=='DONE':
    src=os.path.join(H,fn)
    if os.path.exists(dst) and os.path.exists(src): print('HIBA: cel letezik'); sys.exit(2)
    if not os.path.exists(dst):
        if not os.path.exists(src): print('HIBA: nincs letoltes',src); sys.exit(3)
        shutil.move(src,dst)
    from PIL import Image
    im=Image.open(dst); im.verify(); im=Image.open(dst)
    res.update(meret=f'{im.size[0]}x{im.size[1]} {im.format}', sha=hashlib.sha256(open(dst,'rb').read()).hexdigest())
L=os.path.join(D,'GENERALASI_NAPLO.csv')
cols=['nr','kep_id','kamera','verzio','statusz','modell','prompt_forras','csatolmanyok_sorrendben','uzenet','uzenet_sha256','chat_url','kuldve','eredmeny_fajl','meret','sha256','geometria','megjegyzes']
rows=list(csv.reader(open(L),delimiter=';')) if os.path.exists(L) else [cols]
rows=[r for r in rows if not (r[0]==nr and r[3]==ver)]
rows.append([nr,p['kep_id'],p['kamera'],ver,st,p.get('modell',''),p['prompt_forras'],' > '.join(f'{i+1}: _ref/{x}' for i,x in enumerate(p['csatolmanyok'])),'uzenetek/'+p['uzenet'],p['uzenet_sha256'],url,sent,fn if st=='DONE' else '',res.get('meret',''),res.get('sha',''),geo,note])
rows=[rows[0]]+sorted(rows[1:],key=lambda r:(r[0],r[3]))
with open(L,'w',newline='') as f: csv.writer(f,delimiter=';').writerows(rows)
print(json.dumps(res,ensure_ascii=False))

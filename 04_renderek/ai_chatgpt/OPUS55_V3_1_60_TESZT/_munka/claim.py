#!/usr/bin/env python3
# használat: claim.py <nr> <statusz> <chat_url> <kuldve> [geometria] [megjegyzes]
# a ~/Downloads/<cel_fajl> fájlt átmozgatja a WSG_OPUS55_V3_1_RENDEREK mappába (felülírás nélkül), ellenőrzi és naplóz
import sys,os,csv,json,hashlib,shutil,datetime
H=os.path.expanduser('~/mnt/Downloads'); D=os.path.join(H,'WSG_OPUS55_V3_1_RENDEREK')
nr,st,url,sent=sys.argv[1:5]; geo=sys.argv[5] if len(sys.argv)>5 else ''; note=sys.argv[6] if len(sys.argv)>6 else ''
plan={p['nr']:p for p in json.load(open(os.path.join(D,'plan.json')))}
p=plan[nr]; fn=p['cel_fajl']; dst=os.path.join(D,fn); res={'nr':nr}
if st=='DONE':
    src=os.path.join(H,fn)
    if os.path.exists(dst) and not os.path.exists(src):
        pass
    elif os.path.exists(dst):
        print('HIBA: cel mar letezik, nem irom felul'); sys.exit(2)
    elif not os.path.exists(src):
        print('HIBA: nincs letoltott fajl',src); sys.exit(3)
    else:
        shutil.move(src,dst)
    from PIL import Image
    im=Image.open(dst); im.verify(); im=Image.open(dst)
    res.update(meret=f'{im.size[0]}x{im.size[1]} {im.format}', sha=hashlib.sha256(open(dst,'rb').read()).hexdigest(), bytes=os.path.getsize(dst))
rows=list(csv.reader(open(os.path.join(D,'GENERALASI_NAPLO.csv')),delimiter=';'))
hd=rows[0]; ix={c:i for i,c in enumerate(hd)}
for r in rows[1:]:
    if r[0]==nr:
        r[ix['statusz']]=st; r[ix['chat_url']]=url; r[ix['kuldve']]=sent
        if st=='DONE': r[ix['eredmeny_fajl']]=fn; r[ix['meret']]=res['meret']; r[ix['sha256']]=res['sha']
        if geo: r[ix['geometria']]=geo
        if note: r[ix['megjegyzes']]=note
with open(os.path.join(D,'GENERALASI_NAPLO.csv'),'w',newline='') as f: csv.writer(f,delimiter=';').writerows(rows)
print(json.dumps(res))

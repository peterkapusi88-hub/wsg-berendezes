#!/usr/bin/env python3
# claim_v2.py <nr> <statusz> <chat_url> <kuldve> [geometria] [megjegyzes]
import sys,os,csv,json,hashlib,shutil
H=os.path.expanduser('~/mnt/Downloads'); D=os.path.join(H,'WSG_OPUS55_V3_1_RENDEREK')
nr,st,url,sent=sys.argv[1:5]; geo=sys.argv[5] if len(sys.argv)>5 else ''; note=sys.argv[6] if len(sys.argv)>6 else ''
p={x['nr']:x for x in json.load(open(os.path.join(D,'plan_v2.json')))}[nr]
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
L=os.path.join(D,'GENERALASI_NAPLO_v2.csv')
cols=['nr','kep_id','kamera','verzio','statusz','prompt_forras','csatolmanyok_sorrendben','uzenet','uzenet_sha256','chat_url','kuldve','eredmeny_fajl','meret','sha256','geometria','megjegyzes']
rows=list(csv.reader(open(L),delimiter=';')) if os.path.exists(L) else [cols]
rows=[r for r in rows if not (r[0]==nr and r[3]==p['verzio'])]
rows.append([nr,p['kep_id'],p['kamera'],p['verzio'],st,p['prompt_forras'],' > '.join(f'{i+1}: _ref/{a}' for i,a in enumerate(p['csatolmanyok'])),'uzenetek_v2/'+p['uzenet'],p['uzenet_sha256'],url,sent,fn if st=='DONE' else '',res.get('meret',''),res.get('sha',''),geo,note])
with open(L,'w',newline='') as f: csv.writer(f,delimiter=';').writerows(rows)
# fő napló
M=os.path.join(D,'GENERALASI_NAPLO.csv'); r=list(csv.reader(open(M),delimiter=';')); ix={c:i for i,c in enumerate(r[0])}
for x in r[1:]:
    if x[0]==nr:
        if p['verzio']=='v1':
            x[ix['statusz']]=st; x[ix['chat_url']]=url; x[ix['kuldve']]=sent
            if st=='DONE': x[ix['eredmeny_fajl']]=fn; x[ix['meret']]=res['meret']; x[ix['sha256']]=res['sha']
            if geo: x[ix['geometria']]=geo
            x[ix['megjegyzes']]=('javított csomag (Cam_02 KORR alap + 1b, integrátori v1.3 prompt): '+note) if note else 'javított csomag (Cam_02 KORR alap + 1b, integrátori v1.3)'
            x[ix['prompt_forras']]=p['prompt_forras']; x[ix['uzenet']]='uzenetek_v2/'+p['uzenet']; x[ix['uzenet_sha256']]=p['uzenet_sha256']
            x[ix['csatolmanyok_sorrendben']]=' > '.join(f'{i+1}: _ref/{a}' for i,a in enumerate(p['csatolmanyok']))
        else:
            base=x[ix['megjegyzes']].split(' || v2:')[0]
            x[ix['megjegyzes']]=base+f' || v2: {st} {fn if st=="DONE" else ""} – {geo} – {note} ({url})'
with open(M,'w',newline='') as f: csv.writer(f,delimiter=';').writerows(r)
print(json.dumps(res,ensure_ascii=False))

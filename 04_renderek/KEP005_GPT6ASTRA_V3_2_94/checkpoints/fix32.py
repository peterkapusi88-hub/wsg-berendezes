"""fix32.py <seq> <ver> <note> : javítócsomag a V3.2 tervből – a RUN NOTES végére FIX-jegyzet, a brief változatlan."""
import json,sys,os,shutil,hashlib
seq,ver,note=int(sys.argv[1]),sys.argv[2],sys.argv[3]
P=json.load(open('/home/claude/work/v32_plan.json')); p=[x for x in P if x['seq']==seq][0]
src='/home/claude/work/'+p['dir']; msg=open(src+'/_msg.txt',encoding='utf-8').read()
mark='\nCREATIVE BRIEF – GPT-6 Astra V3.2'
assert msg.count(mark)==1
msg=msg.replace(mark,f"\n- FIX {ver} (Claude QA, 2026-10-26): {note}\n"+mark)
extra=os.environ.get('EXTRA')
if extra:
    ep,en,er=extra.split('|',2); k=len(p['csatolmanyok'])+1; en=f'0{k}_image{k}_'+en
    gm='\n\nGEOMETRY LOCK (mandatory)'; assert msg.count(gm)==1
    msg=msg.replace(gm,f"\n- Image {k} ({en}): {er}"+gm)
    import re
    msg=re.sub(r'\(in this order: [^)]*\)',lambda m:'(in this order: '+', '.join('image '+str(i+1) for i in range(k))+')',msg,count=1)
d=src+'_'+ver; os.makedirs(d,exist_ok=True)
for f in os.listdir(src):
    if f!='_msg.txt': shutil.copy(src+'/'+f,d+'/'+f)
if extra: shutil.copy(ep,d+'/'+en)
open(d+'/_msg.txt','w',encoding='utf-8').write(msg)
O='/mnt/user-data/outputs/WSG_ASTRA_V3_2_RENDEREK/prompts_sent/'; name=p['uzenet'].replace('_v1.txt',f'_{ver}.txt'); open(O+name,'w',encoding='utf-8').write(msg)
FP='/home/claude/work/v32_fix_plan.json'; F=json.load(open(FP)) if os.path.exists(FP) else []
e=dict(p); e['csatolmanyok']=list(p['csatolmanyok'])+([dict(sorrend=k,fajl=en,sha256=hashlib.sha256(open(ep,'rb').read()).hexdigest())] if extra else []); e.update(seq=1000+len(F)+1,alap_seq=seq,verzio=ver,fix=note,dir=d.replace('/home/claude/work/',''),uzenet=name,kep_fajl=p['kep_fajl'].replace('_v1.png',f'_{ver}.png'),uzenet_chars=len(msg),uzenet_sha256=hashlib.sha256(msg.encode()).hexdigest())
F=[x for x in F if not (x['alap_seq']==seq and x['verzio']==ver)]+[e]; json.dump(F,open(FP,'w'),ensure_ascii=False,indent=1)
print(e['seq'],e['dir'],e['kep_fajl'])

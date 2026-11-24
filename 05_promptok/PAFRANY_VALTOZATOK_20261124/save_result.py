import json,pathlib,sys,shutil,hashlib,datetime,subprocess,fcntl
p=pathlib.Path(__file__).resolve().parent
lock=open(p/'.save.lock','w');fcntl.flock(lock,fcntl.LOCK_EX)
m=json.loads((p/'MANIFEST.json').read_text());jid,src=sys.argv[1:3];j=next(x for x in m['jobs'] if x['id']==jid)
dest=p/j['output'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
j.update(status='GENERATED_PENDING_VISUAL_QA',source=src,sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
m['completed_images']=sum((p/x['output']).exists() for x in m['jobs']);(p/'MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
(p/'renders'/(jid+'.generation.json')).write_text(json.dumps(j,ensure_ascii=False,indent=2));subprocess.run([sys.executable,str(p/'update_gallery.py')],check=True);print(jid,m['completed_images'],'/',m['expected_images'])

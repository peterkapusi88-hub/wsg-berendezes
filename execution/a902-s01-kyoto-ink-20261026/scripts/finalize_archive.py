from pathlib import Path
import json,hashlib,zipfile
P=Path(__file__).resolve().parents[1];files=[]
for f in sorted(P.rglob('*')):
 if not f.is_file() or f.is_symlink():continue
 rel=f.relative_to(P).as_posix()
 if any(x in rel.split('/') for x in ['node_modules','__pycache__']):continue
 if f.name.startswith(('~$','.')) or f.suffix in ['.blend1','.pyc'] or f.name.endswith('.inspect.ndjson') or rel.startswith('reports/FILE_MANIFEST') or f.name=='A902_R02_teljes_atadas.zip':continue
 b=f.read_bytes();files.append(dict(path='execution/a902-s01-kyoto-ink-20261026/'+rel,project_path=rel,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),text=f.suffix in ['.md','.txt','.json','.csv','.py','.mjs','.svg','.log']))
(P/'reports/FILE_MANIFEST_R02.json').write_text(json.dumps(files,ensure_ascii=False,indent=2));f=P/'reports/FILE_MANIFEST_R02.json';b=f.read_bytes();files.append(dict(path='execution/a902-s01-kyoto-ink-20261026/reports/FILE_MANIFEST_R02.json',project_path='reports/FILE_MANIFEST_R02.json',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),text=True))
Path('/tmp/R02_upload_list.json').write_text(json.dumps(files,ensure_ascii=False));zpath=P/'outputs/A902_R02_teljes_atadas.zip'
with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(P/f['project_path'],arcname='A902_Kyoto_Ink_R02/'+f['project_path'])
with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
print('Files',len(files),'ZIP CRC OK; bytes',zpath.stat().st_size)

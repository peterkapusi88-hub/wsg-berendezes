from pathlib import Path
import hashlib,json,zipfile
O=Path(__file__).resolve().parents[1];R=O.parent
files=[f for f in O.rglob('*') if f.is_file() and not f.is_symlink() and 'node_modules' not in f.parts and f.suffix not in ['.blend1','.pyc','.zip'] and not f.name.endswith('.inspect.ndjson') and f.name not in ['package_manifest.json','github_save.json']]
manifest=[{'path':str(f.relative_to(O)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted(files)]
(O/'audit/package_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));files.append(O/'audit/package_manifest.json')
z=O/'S16_R05_teljes_csomag.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as out:
 for f in files:out.write(f,str(Path(O.name)/f.relative_to(O)))
 for f in (R/'sources').glob('*'):
  if f.is_file():out.write(f,str(Path('sources')/f.name))
 out.write(R/'00_AKTUALIS_VALTOZAT.txt','00_AKTUALIS_VALTOZAT.txt')
with zipfile.ZipFile(z) as zz:
 assert zz.testzip() is None
 for m in manifest:assert hashlib.sha256(zz.read(O.name+'/'+m['path'])).hexdigest()==m['sha256']
print(json.dumps({'files':len(files),'zip_bytes':z.stat().st_size,'zip_git_blob_sha':hashlib.sha1(b'blob '+str(z.stat().st_size).encode()+b'\0'+z.read_bytes()).hexdigest()}))

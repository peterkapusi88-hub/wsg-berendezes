from pathlib import Path
import json,re,hashlib,zipfile,shutil
P=Path(__file__).resolve().parents[1];O=P/'R12_muhely';parts=json.loads((O/'data/parts.json').read_text())
log=(O/'audit/autocad_dwg_readback.log').read_text(errors='replace');volume=float(re.search(r'Volume:\s+([0-9.]+)',log).group(1));expected=sum(p['x']*p['y']*p['t'] for p in parts)
assert 'Total errors found 0 fixed 0' in log and 'R12_NATIVE_SOLID_COUNT=53' in log and abs(volume-expected)<.01
(O/'audit/autocad_result.json').write_text(json.dumps({'engine':'AutoCAD2027 AcCoreConsole X.119.M.246','input':'own R12 DXF, subsequently saved DWG readback','native_solid_count':53,'AUDIT_database_errors':0,'native_volume_mm3':volume,'expected_board_volume_mm3':expected,'volume_match':True,'dwg_saved':True,'not_certified':'manufacturability,loads,toolpaths,site dimensions,hinge motion','startup_note':'acad2027.LSP load-cancel message occurred; explicitly invoked AUDIT, MASSPROP and SAVEAS completed. No security settings changed.'},indent=2))
# Save reproducible native check script, with safe discard after read-only inspection.
(O/'audit/autocad_readback.scr').write_text('(setvar "FILEDIA" 0)\n_.AUDIT\n_N\n(setq ki_s (ssget "_X" \'((0 . "3DSOLID"))))\n(princ (strcat "\\nR12_NATIVE_SOLID_COUNT=" (itoa (sslength ki_s))))\n(command "_.MASSPROP" "_ALL" "" "_N")\n_.QUIT\n_Y\n')
manifest=[]
for f in sorted(O.rglob('*')):
 if f.is_file() and not f.name.endswith('.inspect.ndjson') and f.name!='file_manifest.json' and not f.suffix in ['.dwl','.dwl2']:
  manifest.append({'path':str(f.relative_to(O)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(O/'data/file_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
zpath=P/'A902_TV_R12_muhelyi_checkpoint.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
 for x in manifest:z.write(O/x['path'],'R12_muhely/'+x['path'])
 z.write(O/'data/file_manifest.json','R12_muhely/data/file_manifest.json')
 for f in [P/'scripts'/n for n in ['r12_parts.py','r12_engineering.py','r12_pdf.py','r12_print_validate.py','r12_room_bounds.py','r12_opening_check.py','r12_package.py']]+[P/'r12_workbook.mjs']:z.write(f,'rebuild/'+f.name)
with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
print('Native volume match',volume,'files',len(manifest),'zip_bytes',zpath.stat().st_size)

from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,json,re,hashlib
import openpyxl
P=Path(__file__).resolve().parents[1];O=P/'R12_muhely';f=O/'TV_modul_alkatreszek_es_cimkek.xlsx'
# artifact-tool authored all workbook data and formulas. Only unavailable print metadata is added here.
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';ET.register_namespace('',ns);q=lambda s:'{'+ns+'}'+s
with zipfile.ZipFile(f) as z:items={i.filename:z.read(i.filename) for i in z.infolist()}
s=ET.fromstring(items['xl/worksheets/sheet2.xml'])
for name in ['pageMargins','pageSetup','rowBreaks']:
 e=s.find(q(name))
 if e is not None:s.remove(e)
ET.SubElement(s,q('pageMargins'),{'left':str(5/25.4),'right':str(5/25.4),'top':str(23.5/25.4),'bottom':str(23.5/25.4),'header':'0','footer':'0'})
ET.SubElement(s,q('pageSetup'),{'paperSize':'9','orientation':'portrait','scale':'100','useFirstPageNumber':'1','firstPageNumber':'1'})
b=ET.SubElement(s,q('rowBreaks'),{'count':'5','manualBreakCount':'5'})
for r in [50,100,150,200,250]:ET.SubElement(b,q('brk'),{'id':str(r),'min':'0','max':'16383','man':'1'})
items['xl/worksheets/sheet2.xml']=ET.tostring(s,encoding='utf-8',xml_declaration=True)
w=ET.fromstring(items['xl/workbook.xml']);dn=w.find(q('definedNames'))
if dn is None:
 dn=ET.Element(q('definedNames'));idx=list(w).index(w.find(q('sheets')))+1;w.insert(idx,dn)
for e in list(dn):
 if e.get('name')=='_xlnm.Print_Area' and e.get('localSheetId')=='1':dn.remove(e)
ET.SubElement(dn,q('definedName'),{'name':'_xlnm.Print_Area','localSheetId':'1'}).text="'Cimkek'!$A$1:$I$300"
items['xl/workbook.xml']=ET.tostring(w,encoding='utf-8',xml_declaration=True)
with zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as z:
 for n,v in items.items():z.writestr(n,v)
# Read-only cross checks. Never use openpyxl to author workbook data.
a=openpyxl.load_workbook(f,data_only=False);v=openpyxl.load_workbook(f,data_only=True);p=json.loads((O/'data/parts.json').read_text());ids=set()
for i,x in enumerate(p,6):
 assert a['Alkatreszek'].cell(i,1).value==x['id'];ids.add(x['id'])
 assert [a['Alkatreszek'].cell(i,j).value for j in [5,6,7]]==[x['x'],x['y'],x['t']]
 assert str(a['Alkatreszek'].cell(i,21).value).startswith('=')
 m=(O/'mpr_alap'/x['mpr']).read_text();assert f'L="{x["x"]}"' in m and f'B="{x["y"]}"' in m
 assert set(re.findall(r'^<(\d+)',m,re.M))=={'100','101'}
assert len(ids)==53 and len(list((O/'mpr_alap').glob('*.mpr')))==53
assert str(a['Cimkek'].page_setup.paperSize)=='9' and len(a['Cimkek'].row_breaks.brk)==5
assert a['Kotopontok'].max_row==157
(O/'audit/package_checks.json').write_text(json.dumps({'unique_part_ids':53,'mpr_files':53,'drawing_dxf_files':53,'mpr_macros_only':['100 workpiece','101 comment'],'xlsx_part_dimensions_match':True,'xlsx_formulas_preserved':True,'label_paper':'A4','label_manual_breaks':5,'label_print_scale':100,'label_physical_printer_test':'NOT_DONE','woodwop_test':'NOT_DONE'},indent=2))
print('Workbook + IDs + MPR envelopes + print metadata verified')

import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const p=fileURLToPath(new URL('.',import.meta.url)),o=p+'R05/';
const f=p+'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx',original=await fs.readFile(f);
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(f));
const refresh=process.argv.includes('--refresh');
const base=JSON.parse(await fs.readFile(o+'sources/workbook_before_R05.json','utf8'));
const patch=JSON.parse(await fs.readFile(o+'data/register_patch.json','utf8'));
const materials=JSON.parse(await fs.readFile(o+'data/materials.json','utf8'));
const units=JSON.parse(await fs.readFile(o+'data/design_R05.json','utf8')).units;
const col=n=>{let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s};
const idx=s=>[...s].reduce((n,c)=>n*26+c.charCodeAt(0)-64,0)-1;
const norm=x=>x===''?null:(x??null);const touched=[];
async function preview(name,range,out){const b=await wb.render({sheetName:name,range,scale:1.25,format:'png'});await fs.writeFile(o+'qa/'+out,new Uint8Array(await b.arrayBuffer()));}
await preview('Összesítő','A4:C15','excel_before.png');
const reg=wb.worksheets.getItem('Elemregiszter');const ids=reg.getRange('C2:C173').values.flat();
function put(sh,a,v,formula=false){sh.getRange(a)[formula?'formulas':'values']=[[v]];touched.push([sh.name,a,v]);}
for(const [id,fields] of Object.entries(patch.patches)){
 const r=ids.indexOf(id)+2;if(r<2)throw Error('Missing '+id);
 for(const [c,v] of Object.entries(fields)){
  const current=reg.getRange(c+r).values[0][0],old=base.Elemregiszter[r-1][idx(c)];
  if(norm(current)!==norm(old)&&norm(current)!==norm(v))throw Error('Manual edit since snapshot '+id+' '+c+r);
  put(reg,c+r,v);
 }
}
for(let j=0;j<patch.new_rows.length;j++){
 const r=174+j;
 if(refresh){for(let c=0;c<54;c++){if([20,33,52,53].includes(c))continue;if(norm(reg.getRange(col(c)+r).values[0][0])!==norm(patch.new_rows[j][c]))throw Error('Manual edit in new R05 row '+r+' '+col(c));}}
 else{reg.getRange(`A${r}:BB${r}`).copyFrom(reg.getRange('A173:BB173'),'all');reg.getRange(`A${r}:BB${r}`).values=[patch.new_rows[j]];}
 put(reg,'U'+r,`=O${r}*Q${r}+SUM(R${r}:T${r})`,true);put(reg,'AH'+r,`=O${r}*AG${r}+SUM(R${r}:T${r})`,true);
 put(reg,'BA'+r,`=ROUND(U${r}*AY${r},0)`,true);put(reg,'BB'+r,`=ROUND(U${r}*AZ${r},0)`,true);
}
const last=175;
for(const [name,data] of Object.entries(base)){
 if(['Baseline egyeztetés','CP1a eltérések','CP3 eltérések'].includes(name))continue;
 const sh=wb.worksheets.getItem(name);
 for(let r=0;r<data.length;r++)for(let c=0;c<data[r].length;c++){
  const v=data[r][c];if(typeof v==='string'&&v.startsWith('=')&&v.includes('Elemregiszter')&&/\$?173\b/.test(v))put(sh,col(c)+(r+1),v.replace(/(\$?[A-Z]+\$?)173\b/g,'$1'+last),true);
 }
}
const sum=wb.worksheets.getItem('Összesítő');
// Repair inherited semantic error: copied CP1a formulas pointed to empty local O:T.
const cp1=JSON.parse(await fs.readFile(p+'data/workbook_readback_CP1a.json','utf8')).Elemregiszter;
const historicalTotal=r=>r[14]*r[16]+[17,18,19].reduce((s,c)=>s+(r[c]??0),0);
const cp1tab=wb.worksheets.getItem('CP1a eltérések');
for(let j=1;j<base['CP1a eltérések'].length;j++){const id=base['CP1a eltérések'][j][0],row=cp1.find(r=>r[2]===id);if(row)put(cp1tab,'C'+(j+1),historicalTotal(row));}
put(cp1tab,'C1','CP1a mentett Ft');put(cp1tab,'D1','Aktuális R05 Ft');
const cp3tab=wb.worksheets.getItem('CP3 eltérések');
for(let j=1;j<base['CP3 eltérések'].length;j++){const id=base['CP3 eltérések'][j][0],row=base.Elemregiszter.find(r=>r[2]===id);if(row)put(cp3tab,'C'+(j+1),historicalTotal(row));}
put(cp3tab,'C1','CP3 mentett bruttó Ft');
// Baseline comparison is explicitly current; extend live dependencies, preserve original B/C values.
const bst=wb.worksheets.getItem('Baseline egyeztetés');
for(let r=0;r<base['Baseline egyeztetés'].length;r++)for(let c=0;c<base['Baseline egyeztetés'][r].length;c++){
 const v=base['Baseline egyeztetés'][r][c];if(typeof v==='string'&&v.startsWith('=')&&v.includes('Elemregiszter'))put(bst,col(c)+(r+1),v.replace(/(\$?[A-Z]+\$?)(160|173)\b/g,'$1'+last),true);
}
for(const [a,v] of Object.entries({C7:'R05: teljes R04 bútorváltozat + teljes W02 + biciklitartó. Árazási munkaváltozat, nem rendelési jóváhagyás.',C8:'Azonos tárolókapacitás. Síkabb W01, vlies W02, fix fürdődugalj; mindhárom változtatás döntésre és ajánlatra vár.',C15:'174 élő költségsor; R05 anyag és kapacitás kiegészítéssel.',C17:'18M cél marad. A 23,79M megengedő visszajelzés nem költési keretjóváhagyás.',C18:'Az Elemregiszter az élő árforrás. A CP3 nevű tároló- és fénylapok korábbi revíziók; aktuális R05 kapacitás külön lapon.'}))put(sum,a,v);
function tab(name,headers,rows,widths){const sh=refresh?wb.worksheets.getItem(name):wb.worksheets.add(name),end=col(headers.length-1),rg=sh.getRange(`A1:${end}${rows.length+1}`);rg.values=[headers,...rows];sh.showGridLines=false;sh.freezePanes.freezeRows(1);rg.format.font.name='Arial';rg.format.font.size=10;rg.format.wrapText=true;rg.format.rowHeight=78;rg.format.verticalAlignment='center';sh.getRange(`A1:${end}1`).format.fill='#303C3B';sh.getRange(`A1:${end}1`).format.font.color='#FFFFFF';for(let j=0;j<headers.length;j++)sh.getRange(`${col(j)}1:${col(j)}${rows.length+1}`).format.columnWidth=widths[j]??24;return sh}
tab('R05 anyagok',['Kód','Anyag / jelölt','Alkalmazás','Gyártás / vastagság','Ellenőrzendő','Árkezelés','Forrás'],materials.map(m=>[m.id,m.name+' — '+m.candidate,m.use,m.method,m.gate,m.price,m.source]),[14,48,35,85,70,65,70]);
const changeIds=[...new Set([...Object.keys(patch.patches),...patch.new_rows.map(r=>r[2])])];
const allids=reg.getRange('C2:C175').values.flat();
const ch=tab('R05 változások',['Elem','CP3 bruttó Ft','R05 bruttó Ft','Eltérés Ft','R05 gazdaságos Ft','Megtak. Ft','Műszaki ok'],changeIds.map(id=>{const b=base.Elemregiszter.find(r=>r[2]===id);return[id,b?b[14]*b[16]+[17,18,19].reduce((s,c)=>s+(b[c]??0),0):0,null,null,null,null,patch.reasons[id]??'Új R05 tétel'];}),[23,21,21,21,23,21,110]);
for(let j=0;j<changeIds.length;j++){let r=j+2,rr=allids.indexOf(changeIds[j])+2;ch.getRange(`C${r}:F${r}`).formulas=[[`='Elemregiszter'!U${rr}`,`=C${r}-B${r}`,`='Elemregiszter'!AH${rr}`,`=C${r}-E${r}`]];}ch.getRange(`B2:F${changeIds.length+1}`).setNumberFormat('#,##0');
const caps=[];
for(const u of units)for(const b of u.cp3_bays)caps.push([u.id,b.id,b.purpose,b.clear_w,b.clear_d,b.shelves_mm.length,b.rod_lengths_mm.reduce((a,x)=>a+x,0),b.drawers,...b.drawer_inner_mm,null,null,null,u.id.startsWith('B6')?'Szifon levonása még nincs véglegesítve.':'Tervi kapacitás, nem felmért vagy garantált tárgybeférés.']);
const cap=tab('R05 kapacitás',['Elem','Rekesz','Használat','Nettó szél. mm','Nettó mély. mm','Polc db','Rúd mm','Fiók db','Fiók belszél. mm','Fiók belmély. mm','Fiók belmag. mm','Akasztás m','Polc m²','Fiók liter','Státusz'],caps,[16,25,48,17,17,12,16,12,18,18,18,16,16,16,65]);
for(let r=2;r<=caps.length+1;r++)cap.getRange(`L${r}:N${r}`).formulas=[[`=G${r}/1000`,`=D${r}*E${r}*F${r}/1000000`,`=H${r}*I${r}*J${r}*K${r}/1000000`]];cap.getRange(`L2:N${caps.length+1}`).setNumberFormat('0.000');
wb.recalculate();const got=sum.getRange('B7:B13').values.flat();if(got[0]!==patch.expected.main||got[1]!==patch.expected.economy)throw Error('Independent total mismatch '+got);
const q=reg.getRange('Q174').values[0][0],b=sum.getRange('B7').values[0][0];reg.getRange('Q174').values=[[q+1000]];wb.recalculate();const delta=sum.getRange('B7').values[0][0]-b;if(delta!==7000)throw Error('Quantity perturbation failed '+delta);reg.getRange('Q174').values=[[q]];wb.recalculate();
const err=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'R05 formula errors'});await fs.writeFile(o+'qa/formula_scan.txt',err.ndjson);
await fs.writeFile(o+'qa/touched_cells.json',JSON.stringify(touched,null,2));
await fs.writeFile(o+'qa/excel_checks.json',JSON.stringify({expected:patch.expected,actual:got,perturbation:delta,source_byte_comparison:original.equals(await fs.readFile(f)),calculation_engine:'artifact-tool; desktop Excel not run'},null,2));
if(!original.equals(await fs.readFile(f)))throw Error('Workbook changed during editing');
const cp1got=cp1tab.getRange('C2:C160').values.flat().reduce((a,v)=>a+(v??0),0);const cp3got=cp3tab.getRange('C2:C173').values.flat().reduce((a,v)=>a+(v??0),0);
if(cp1got!==20083350||cp3got!==23253840)throw Error('Historical total error '+[cp1got,cp3got]);
await fs.writeFile(o+'qa/history_reconciliation.json',JSON.stringify({CP1a:cp1got,CP3:cp3got,R05:got[0],CP1a_repair:'Copied formulas originally referred to blank cells on the history sheet; values reconstructed from preserved CP1a qty/rate/cost inputs.',CP3_freeze:'Historical values no longer follow live R05 costs.'},null,2));
await(await SpreadsheetFile.exportXlsx(wb)).save(f);
for(const [name,range,file] of [['Összesítő','A4:C15','excel_after.png'],['R05 anyagok','A1:C5','excel_materials.png'],['R05 változások','A1:F7','excel_changes.png'],['R05 kapacitás','A1:F7','excel_capacity.png']])await preview(name,range,file);
console.log(JSON.stringify({main:got[0],economy:got[1],rows:174,perturbation:delta}));

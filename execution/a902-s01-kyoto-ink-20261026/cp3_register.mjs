import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const p=fileURLToPath(new URL('.',import.meta.url)),o=p+'CP3/';
const file=p+'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx',original=await fs.readFile(file);
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const baseline=JSON.parse(await fs.readFile(p+'data/workbook_readback_before_CP3.json','utf8'));
const patch=JSON.parse(await fs.readFile(o+'data/cost_patch.json','utf8'));
const refresh=process.argv.includes('--refresh');
const prior=refresh?JSON.parse(await fs.readFile(o+'qa/last_applied_patch.json','utf8')):null;
const caps=JSON.parse(await fs.readFile(o+'data/rekesz_kapacitas.json','utf8'));
const lights=JSON.parse(await fs.readFile(o+'data/belso_vilagitas.json','utf8'));
const hw=JSON.parse(await fs.readFile(o+'data/vasalat.json','utf8'));
const snap=JSON.parse(await fs.readFile(o+'data/cost_snapshot_CP3.json','utf8'));
const reg=wb.worksheets.getItem('Elemregiszter');
const col=n=>{let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s};
const idx=c=>[...c].reduce((n,x)=>n*26+x.charCodeAt(0)-64,0)-1;
const ids=reg.getRange('C2:C160').values.flat();
// Compare every intended existing-cell edit with the pre-CP3 readback.
for(const [id,fields] of Object.entries(patch.patches)){
 const r=ids.indexOf(id)+2;if(r<2)throw Error('Missing code '+id);
 for(const [c,v] of Object.entries(fields)){
  const old=baseline.Elemregiszter[r-1][idx(c)],cur=reg.getRange(c+r).values[0][0];
  if((cur??null)!==(old??null)&&cur!==v&&!(refresh&&cur===prior.patches[id]?.[c]))throw Error('Manual change since snapshot at '+id+' '+c+r);
  reg.getRange(c+r).values=[[v]];
 }
}
const last=160+patch.new_rows.length;
for(let j=0;j<patch.new_rows.length;j++){
 if(refresh){const rr=161+j;const norm=x=>x===''?null:(x??null);for(let c=0;c<54;c++){if([20,33,52,53].includes(c))continue;const v=patch.new_rows[j][c],cur=reg.getRange(col(c)+rr).values[0][0],expected=prior.new_rows[j][c];if(norm(cur)!==norm(expected)&&norm(cur)!==norm(v))throw Error('Manual CP3 row edit '+rr+' '+col(c));reg.getRange(col(c)+rr).values=[[v]];}continue;}
 const row=161+j;reg.getRange(`A${row}:BB${row}`).copyFrom(reg.getRange('A160:BB160'),'all');
 reg.getRange(`A${row}:BB${row}`).values=[patch.new_rows[j]];
 reg.getRange('U'+row).formulas=[[`=O${row}*Q${row}+SUM(R${row}:T${row})`]];
 reg.getRange('AH'+row).formulas=[[`=O${row}*AG${row}+SUM(R${row}:T${row})`]];
 reg.getRange(`BA${row}:BB${row}`).formulas=[[`=ROUND(U${row}*AY${row},0)`,`=ROUND(U${row}*AZ${row},0)`]];
}
// Extend only formula dependencies that sum the live register. Baseline snapshots stay unchanged.
for(const [name,data] of Object.entries(baseline)){
 if(name==='CP1a eltérések'||name==='Baseline egyeztetés')continue;
 const sh=wb.worksheets.getItem(name);
 for(let r=0;r<data.length;r++)for(let c=0;c<data[r].length;c++){
  const v=data[r][c];if(typeof v==='string'&&v.startsWith('=')&&v.includes('Elemregiszter')&&/\$?160\b/.test(v))sh.getRange(col(c)+(r+1)).formulas=[[v.replace(/(\$?[A-Z]+\$?)160\b/g,'$1'+last)]];
 }
}
const sum=wb.worksheets.getItem('Összesítő');sum.getRange('C7:C8').values=[['CP3 teljes előirányzat, a második fagyasztóval. Nyitott szakági kapuk és becslések.'],['Tételes cserejavaslatok; csökkentett fiókszám és fix fürdő-dugalj. Nincs elfogadva.']];sum.getRange('B17').values=[['2026-10-27']];sum.getRange('C15').values=[['CP3 sorokkal bővítve; az összesítő képletek tartománya ellenőrizve.']];
sum.getRange('B15').formulas=[[`=COUNTA('Elemregiszter'!C2:C${last})`]];
sum.getRange('A79:C84').values=[['CP3 külön kimutatás','Fő Ft','Megjegyzés'],['AT8-01',null,'Fagyasztóval, polcokkal; közös szerelés külön'],['T-0-26',null,'Polcok; közös szerelés külön'],['AT8-01 / T-0-26',null,'Közös szállítás, rögzítés és dobozok'],['Fagyasztó és kapcsolódó munka',null,'Opcionális beszerzés; a bemutatott fő változat tartalmazza'],['Fő változat fagyasztó nélkül',null,'Nem automatikusan kiválasztott megtakarítás']];
for(let r=80;r<=82;r++)sum.getRange('B'+r).formulas=[[`=SUMIFS('Elemregiszter'!$U$2:$U$${last},'Elemregiszter'!$B$2:$B$${last},A${r})`]];
sum.getRange('B83').formulas=[[`=SUMIFS('Elemregiszter'!$U$2:$U$${last},'Elemregiszter'!$C$2:$C$${last},"KI-CP3-F01")+SUMIFS('Elemregiszter'!$U$2:$U$${last},'Elemregiszter'!$C$2:$C$${last},"KI-CP3-F02")`]];sum.getRange('B84').formulas=[['=B7-B83']];sum.getRange('B80:B84').setNumberFormat('#,##0');
function tab(name,headers,rows,widths){const sh=refresh?wb.worksheets.getItem(name):wb.worksheets.add(name);const end=col(headers.length-1);sh.getRange(`A1:${end}${rows.length+1}`).values=[headers,...rows];sh.showGridLines=false;sh.freezePanes.freezeRows(1);sh.getRange(`A1:${end}${rows.length+1}`).format.font.name='Arial';sh.getRange(`A1:${end}${rows.length+1}`).format.font.size=10;sh.getRange(`A1:${end}${rows.length+1}`).format.wrapText=true;sh.getRange(`A1:${end}${rows.length+1}`).format.verticalAlignment='center';sh.getRange(`A1:${end}${rows.length+1}`).format.rowHeight=48;sh.getRange(`A1:${end}1`).format.fill='#303C3B';sh.getRange(`A1:${end}1`).format.font.color='#FFFFFF';for(let j=0;j<headers.length;j++)sh.getRange(`${col(j)}1:${col(j)}${rows.length+1}`).format.columnWidth=widths[j]??22;return sh}
const ca=tab('CP3 rekeszek',['Elem','Helyiség','Rekesz','Funkció','Nettó szél. mm','Nettó mély. mm','Polc db','Rúd össz. mm','Fiók db','Fiók szél. mm','Fiók mély. mm','Fiók belmag. mm','Szifon levonás l','Akasztás m','Polc m²','Fiók liter','Szabad tartalék','Tervezett feltöltés l','Státusz'],caps.map(b=>{
 let n=b.shelves_mm.length;if(b.unit==='K-01')n=2;if(b.unit==='K-02')n=1;
 const gross=b.drawers*b.drawer_inner_mm.reduce((a,x)=>a*x,1)/1e6;
 return [b.unit,b.room,b.id,b.purpose,b.clear_w,b.clear_d,n,b.rod_lengths_mm.reduce((a,x)=>a+x,0),b.drawers,...b.drawer_inner_mm,Math.max(0,gross-b.drawer_l),null,null,null,.25,null,b.usable_depth_status];}),[15,12,22,48,16,16,12,16,12,16,16,18,18,15,15,16,16,20,45]);
for(let r=2;r<=caps.length+1;r++){ca.getRange(`N${r}:P${r}`).formulas=[[`=H${r}/1000`,`=E${r}*F${r}*G${r}/1000000`,`=I${r}*J${r}*K${r}*L${r}/1000000-M${r}`]];ca.getRange('R'+r).formulas=[[`=P${r}*(1-Q${r})`]];}ca.getRange(`N2:P${caps.length+1}`).setNumberFormat('0.000');ca.getRange(`Q2:Q${caps.length+1}`).setNumberFormat('0%');
const li=tab('CP3 belső fény',['Fénykód','Elem','Rekesz','Magasság mm','Hossz mm','W','SKU','Kelvin / CRI','Kábelút','Vezérlés','Szerviz'],lights.fixtures.map(l=>[l.id,l.unit,l.bay,l.z,l.length,l.watts,l.sku,l.kelvin+' / '+l.cri,l.source,l.scene,l.service]),[31,15,23,16,14,12,45,50,65,55,65]);
const ps=tab('CP3 tápegységek',['Tápegység','Elem','Lámpa db','Terhelés W','Névleges W','Terhelés %','Készlet','Szerviz'],lights.drivers.map(g=>[g.id,g.unit,g.fixture_ids.length,g.watts,g.rating_w,null,g.sku,'Felső, hozzáférhető rekesz; a betáp helyszíni ellenőrzése szükséges.']),[42,16,16,16,16,16,70,70]);for(let r=2;r<=lights.drivers.length+1;r++)ps.getRange('F'+r).formulas=[[`=D${r}/E${r}`]];ps.getRange(`F2:F${lights.drivers.length+1}`).setNumberFormat('0.0%');
tab('CP3 vasalat',['Elem','Rekesz','Típus','Jelölt','Db','Névleges mm','Bizonyíték'],hw.map(h=>[h.unit,h.bay,h.type,h.candidate,h.qty,h.nominal_mm,h.proof]),[16,22,45,70,12,18,75]);
const finalIds=[...ids,...patch.new_rows.map(r=>r[2])];const delta=tab('CP3 eltérések',['Elemkód','R02 bruttó Ft','CP3 bruttó Ft','Változás Ft','Ok / tartalom'],finalIds.map((id,j)=>{
 const b=baseline.Elemregiszter.find(r=>r[2]===id);const v=b?b[14]*b[16]+[17,18,19].reduce((a,c)=>a+(b[c]??0),0):0;
 return [id,v,null,null,patch.patches[id]?.AF??(j>=159?patch.new_rows[j-159][31]:'R02 tartalom megtartva')];}),[23,21,21,21,105]);
for(let r=2;r<=finalIds.length+1;r++)delta.getRange(`C${r}:D${r}`).formulas=[[`='Elemregiszter'!U${r}`,`=C${r}-B${r}`]];delta.getRange(`B2:D${finalIds.length+1}`).setNumberFormat('#,##0');
wb.recalculate();const got=sum.getRange('B7:B8').values.flat();if(Math.abs(got[0]-snap.main)>1||Math.abs(got[1]-snap.economy)>1)throw Error('Independent total mismatch '+got);
const q=reg.getRange('Q161').values[0][0],before=sum.getRange('B7').values[0][0];reg.getRange('Q161').values=[[q+1000]];wb.recalculate();const pert=sum.getRange('B7').values[0][0]-before;if(pert!==patch.new_rows[0][14]*1000)throw Error('Perturbation failed');reg.getRange('Q161').values=[[q]];wb.recalculate();
const err=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:50},summary:'CP3 képlethibák'});await fs.writeFile(o+'qa/excel_formula_scan.txt',err.ndjson);
await fs.writeFile(o+'qa/excel_checks.json',JSON.stringify({expected:snap,actual:got,perturbation_delta:pert,source_rows:159,final_rows:finalIds.length,manual_edits:'Existing target cells checked against pre-CP3 snapshot; unrelated values not rewritten'},null,2));
if(!original.equals(await fs.readFile(file)))throw Error('Live workbook changed during editing');
await(await SpreadsheetFile.exportXlsx(wb)).save(file);
await fs.writeFile(o+'qa/last_applied_patch.json',JSON.stringify(patch,null,2));
for(const [name,range] of [['Összesítő','A4:C15'],['CP3 rekeszek','A1:F6'],['CP3 belső fény','A1:G5'],['CP3 tápegységek','A1:F5'],['CP3 vasalat','A1:E5'],['CP3 eltérések','A48:E54']]){const im=await wb.render({sheetName:name,range,scale:1.3,format:'png'});await fs.writeFile(o+'qa/'+name+'.png',new Uint8Array(await im.arrayBuffer()));}
console.log(JSON.stringify({main:got[0],economy:got[1],rows:finalIds.length,perturbation:pert}));

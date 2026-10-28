import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const p=fileURLToPath(new URL('.',import.meta.url)),o=p+'R10/',f=p+'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx',before=await fs.readFile(f),base=JSON.parse(await fs.readFile(o+'audit/workbook_before.json','utf8'));
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(f)),reg=wb.worksheets.getItem('Elemregiszter');
if(process.argv.includes('--preview')){const b=await wb.render({sheetName:'Összesítő',range:'A5:C9',scale:1.3});await fs.writeFile(o+'audit/excel_before.png',new Uint8Array(await b.arrayBuffer()));process.exit(0);}
const col=n=>{let a='';for(n++;n;n=Math.floor((n-1)/26))a=String.fromCharCode(65+(n-1)%26)+a;return a};
const edits=[];function put(sh,a,v){sh.getRange(a)[typeof v==='string'&&v.startsWith('=')?'formulas':'values']=[[v]];edits.push({sheet:sh.name,cell:a,value:v});}
const changes=[
 ['KI-030',765500,'W01:720mm torony +120mm visszahúzott sáv +4×690mm panel; összes3600mm','720×400×2330 felső torony;2760×36×2330 panel','+75500Ft becslés:0,4194m² többletfelület kb10500Ft; köztes sáv25000; szélek/alkatrész10000; új hordozó/nyomatpróba30000. Nem ajánlat.'],
 ['KI-031',350000,'W01 alsó bútor,5 működő front és120mm süllyesztett szervizbetét','3600×400×400mm;720+120+4×690','+30000Ft:300mm többlet korpusz/top/front, régi320000×3600/3300≈349091Ft,350000Ft becslés.'],
 ['KI-032',135000,'W01 rögzítés, szerviz és köztes sáv szerelése','R10 TV-01/02/03; tervi4m fal','+15000Ft:3óra többlet szerelési előirányzat×5000Ft. Falteher és szolgáltatáskeresés továbbra ellenőrzendő.'],
 ['KI-041',80000,'Magas fali sín, konzolok és oldható szervizrögzítés','4500mm sín; z2840mm javaslat','+15000Ft: magas konzol/oldható elem előirányzat; mennyezeti fúrás nincs jóváhagyva.'],
 ['KI-042',65000,'Méretre varrás és magas függönyszerelés','szabad függés kb2680mm; felmérendő','+10000Ft: magas szerelés/hozzáférés előirányzat; szövetkeret KI-040 változatlan.']
];
for(const[id,q,name,size,note] of changes){const row=base.Elemregiszter.findIndex(r=>r[2]===id)+1;for(const[c,v]of Object.entries({7:name,11:size,16:q,32:q,31:note,40:'R10/drawings/W01_R10.pdf',41:'R10_'+id,21:'előzetes becslés',23:'2026-10-28'}))put(reg,col(+c)+row,v);}
let row=base.Elemregiszter.findIndex(r=>r[2]==='KI-114')+1;put(reg,'L'+row,'Felső2,76m + függőleges2,33m + alsó3,60m=8,69m;10m rendelési keret');
const n=179;reg.getRange(`A${n}:BB${n}`).copyFrom(reg.getRange('A136:BB136'),'all');
const r=[...base.Elemregiszter[135]];r[2]='KI-R10-01';r[6]='Textil';r[7]='3 díszpárna és1 takaró, külön beszerzés';r[8]='választandó';r[9]='PENDING';r[11]='3×kb43×43cm;1 takaró, méret/termék egyeztetendő';r[14]=1;r[16]=45000;r[17]=r[18]=r[19]=0;r[20]='=O179*Q179+SUM(R179:T179)';r[22]='Tervezői becslés:3×8000Ft párna+21000Ft takaró;30000–60000Ft sáv';r[23]='2026-10-28';r[31]='R09 külön deltája most egyszer átvezetve; nem a Lennon gyári tartozéka.';r[32]=45000;r[33]='=O179*AG179+SUM(R179:T179)';r[40]='R10/drawings/W01_R10.pdf';r[41]='R09_cushion_*, R09_grey_throw';r[50]=2/3;r[51]=4/3;r[52]='=ROUND(U179*AY179,0)';r[53]='=ROUND(U179*AZ179,0)';
reg.getRange('A179:BB179').values=[r.map(v=>typeof v==='string'&&v.startsWith('=')?null:v)];for(const c of[20,33,52,53])put(reg,col(c)+n,r[c]);
for(const[name,data]of Object.entries(base)){if(['CP1a eltérések','CP3 eltérések','R05 változások','R06 változások'].includes(name))continue;const sh=wb.worksheets.getItem(name);for(let rr=0;rr<data.length;rr++)for(let c=0;c<data[rr].length;c++){const v=data[rr][c];if(typeof v==='string'&&v.startsWith('=')&&v.includes('Elemregiszter')&&/\$?178\b/.test(v))put(sh,col(c)+(rr+1),v.replace(/(\$?[A-Z]+\$?)178\b/g,'$1179'));}}
const sum=wb.worksheets.getItem('Összesítő');put(sum,'C7','R10:3600mm médiafal,120mm sáv, magas függöny, külön textilek. Becslések, nem jóváhagyott többletkeret.');put(sum,'C15','178 költségsor;2M tartalék érintetlen; R09 45000Ft textildelta már beépítve.');
wb.recalculate();let total=sum.getRange('B7').values[0][0];if(total!==24673390)throw Error('Total mismatch '+total);
const sh=wb.worksheets.add('R10 változások');const data=[['Elem','Előző Ft','R10 Ft','Változás Ft','Indok'],...changes.map(([id,q,name,size,note])=>{let b=base.Elemregiszter.find(r=>r[2]===id);return[id,b[16],q,q-b[16],note]}),['KI-R10-01',0,45000,45000,r[22]]];sh.getRange('A1:E7').values=data;sh.getRange('A1:E7').format.wrapText=true;sh.getRange('A1:D7').format.columnWidth=20;sh.getRange('E1:E7').format.columnWidth=95;sh.getRange('A1:E7').format.rowHeight=65;sh.getRange('A1:E1').format.fill='#303C3B';sh.getRange('A1:E1').format.font.color='#FFFFFF';sh.showGridLines=false;
for(let rr=2;rr<=7;rr++){const id=data[rr-1][0];let target=id==='KI-R10-01'?179:base.Elemregiszter.findIndex(r=>r[2]===id)+1;sh.getRange('C'+rr+':D'+rr).formulas=[[`='Elemregiszter'!U${target}`,`=C${rr}-B${rr}`]];}
put(reg,'Q179',46000);wb.recalculate();if(sum.getRange('B7').values[0][0]!==total+1000)throw Error('Recalc test');put(reg,'Q179',45000);wb.recalculate();
const scan=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!',options:{useRegex:true,maxResults:50}});await fs.writeFile(o+'audit/formula_scan.txt',scan.ndjson);
if(!before.equals(await fs.readFile(f)))throw Error('Workbook changed concurrently');await(await SpreadsheetFile.exportXlsx(wb)).save(f);
const b=await wb.render({sheetName:'R10 változások',range:'A1:D7',scale:1.5});await fs.writeFile(o+'audit/excel_after.png',new Uint8Array(await b.arrayBuffer()));await fs.writeFile(o+'audit/excel_checks.json',JSON.stringify({total,delta:190500,rows:178,recalc_test:true,edits},null,2));console.log(JSON.stringify({total,delta:190500}));

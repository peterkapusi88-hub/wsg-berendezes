import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const dir=fileURLToPath(new URL('.',import.meta.url));
const file=dir+'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx';
const before=await fs.readFile(file);const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(file));
const r=JSON.parse(await fs.readFile(dir+'data/elemek.json','utf8'));
const keys=['lakas','helyiseg','elemkod','render','baseline','kor','szakma','megnevezes','marka','sku','link','meret','szin','anyag','mennyiseg','egyseg','egysegar','szallitas','szereles','egyeb',null,'arstatusz','arforras','datum','atfutas','abc','egyezes','jovahagyas','rendeles','felelos','ellenorzes','megjegyzes','gazdasagos',null,'optimalizalas','garancia','szallithatosag','alt1','alt2'];
const reg=wb.worksheets.getItem('Elemregiszter');
function col(n){let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s}
for(let j=0;j<keys.length;j++)if(keys[j])reg.getRange(`${col(j)}2:${col(j)}${r.length+1}`).values=r.map(x=>[x[keys[j]]??null]);
const sum=wb.worksheets.getItem('Összesítő');sum.getRange('C7').values=[['V3.3 célátvétel: +210 000 Ft; 159 költségsor; minden új ár becslés']];

const extKeys=['szerkezet','rajz','blender_objektum','kesz_egyedi','meret_statusz','penznem','arfolyam','ar_ervenyesseg','felhordas','szakmai_aproanyag','hatarido_het','min_factor','max_factor'];
reg.getRange('AN1').write([['Szerkezet','Rajz','Blender objektum','Kész / egyedi','Méretbizonyíték','Pénznem','Árfolyam','Árérrvényesség','Felhordás','Segédanyag hivatkozás','Döntési hét T0-tól','Alsó szorzó','Felső szorzó','Alsó sáv Ft','Felső sáv Ft'],...r.map(x=>extKeys.map(k=>x[k]??'PENDING'))]);
for(let i=2;i<=r.length+1;i++)reg.getRange(`BA${i}:BB${i}`).formulas=[[`=ROUND(U${i}*AY${i},0)`,`=ROUND(U${i}*AZ${i},0)`]];
reg.getRange('AN1:BB160').format.columnWidth=30;reg.getRange('AN1:BB160').format.wrapText=true;reg.getRange('AN1:BB1').format.fill='#303C3B';reg.getRange('AN1:BB1').format.font.color='#FFFFFF';reg.getRange('BA2:BB160').setNumberFormat('#,##0');
sum.getRange('C7:C8').values=[['R02: teljes lakásra kiterjedő előirányzat; nyitott termékek és becslések'],['Tételes cserejavaslatok; nem elfogadott vagy fix ajánlat. Keret felett marad.']];
sum.getRange('A73:C77').values=[['Bizonytalanság','Ft','Indikatív sáv, nem statisztikai intervallum'],['Alsó sáv',null,'Sorok alsó feltételezéseinek összege'],['Felső sáv',null,'Sorok felső feltételezéseinek összege'],['Tartalék felhasználva',0,'A 2 M Ft továbbra is külön marad'],['Gazdaságos megtakarítás',null,'Bruttó projektkülönbség, változatlan közös logisztikával']];
sum.getRange('B74:B75').formulas=[["=SUM('Elemregiszter'!BA2:BA160)"],["=SUM('Elemregiszter'!BB2:BB160)"]];sum.getRange('B77').formulas=[['=B7-B8']];sum.getRange('B74:B77').setNumberFormat('#,##0');
const tabs=JSON.parse(await fs.readFile(dir+'data/workbook_extension.json','utf8'));
for(const t of tabs){let sh;try{sh=wb.worksheets.getItem(t.name)}catch{};if(!sh)sh=wb.worksheets.add(t.name);sh.getRange('A1').write([t.headers,...t.values]);const used=sh.getUsedRange();used.format.font.name='Arial';used.format.font.size=10;used.format.rowHeight=76;used.format.wrapText=true;used.format.verticalAlignment='center';sh.showGridLines=false;sh.freezePanes.freezeRows(1);for(let j=0;j<t.headers.length;j++)sh.getRange(`${col(j)}1:${col(j)}${t.values.length+1}`).format.columnWidth=t.widths[j]??30;sh.getRange(`A1:${col(t.headers.length-1)}1`).format.fill='#303C3B';sh.getRange(`A1:${col(t.headers.length-1)}1`).format.font.color='#FFFFFF';sh.getRange(`A1:${col(t.headers.length-1)}1`).format.rowHeight=45;
 if(t.name==='CP1a eltérések')for(let i=2;i<=160;i++)sh.getRange(`D${i}:E${i}`).formulas=[[`='Elemregiszter'!U${i}`,`=D${i}-C${i}`]];
 if(t.name==='Felületi mennyiségek')for(let i=2;i<=7;i++){sh.getRange(`D${i}`).formulas=[[`=B${i}*C${i}`]];sh.getRange(`F${i}`).formulas=[[`=D${i}*(1+E${i})`]];}
 if(t.name==='Textilmennyiségek')for(let i=2;i<=5;i++){sh.getRange(`H${i}:I${i}`).formulas=[[`=F${i}*(D${i}+E${i})*1.05`,`=G${i}*(D${i}+E${i})*1.05`]];}
}

wb.recalculate();console.log((await wb.inspect({kind:'table',range:'Összesítő!A5:B15',include:'values',tableMaxRows:11,tableMaxCols:2,maxChars:2200})).ndjson);
const originalQ=reg.getRange('Q2').values[0][0];reg.getRange('Q2').values=[[originalQ+1000]];wb.recalculate();console.log('PERTURBATION',sum.getRange('B7').values);reg.getRange('Q2').values=[[originalQ]];wb.recalculate();
if(!before.equals(await fs.readFile(file)))throw Error('Workbook changed during update; no overwrite');
await (await SpreadsheetFile.exportXlsx(wb)).save(file);
const im=await wb.render({sheetName:'Összesítő',range:'A2:C18',scale:1.3,format:'png'});await fs.writeFile(dir+'outputs/Összesítő.png',new Uint8Array(await im.arrayBuffer()));

for(const t of tabs){const sh=wb.worksheets.getItem(t.name);const im=await wb.render({sheetName:t.name,range:'A1:D4',scale:1.2,format:'png'});await fs.writeFile(dir+'outputs/'+t.name+'.png',new Uint8Array(await im.arrayBuffer()));}

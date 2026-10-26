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
wb.recalculate();console.log((await wb.inspect({kind:'table',range:'Összesítő!A5:B15',include:'values',tableMaxRows:11,tableMaxCols:2,maxChars:2200})).ndjson);
if(!before.equals(await fs.readFile(file)))throw Error('Workbook changed during update; no overwrite');
await (await SpreadsheetFile.exportXlsx(wb)).save(file);
const im=await wb.render({sheetName:'Összesítő',range:'A2:C18',scale:1.3,format:'png'});await fs.writeFile(dir+'outputs/Összesítő.png',new Uint8Array(await im.arrayBuffer()));

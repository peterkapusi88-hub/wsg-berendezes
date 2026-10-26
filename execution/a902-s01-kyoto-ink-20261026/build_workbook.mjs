import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const dir=fileURLToPath(new URL('.',import.meta.url));
const rows=JSON.parse(await fs.readFile(dir+'data/elemek.json','utf8'));
const old=JSON.parse(await fs.readFile(dir+'data/eredeti_S01.json','utf8')).filter(r=>r.osszegezheto==='IGEN');
const wb=Workbook.create();
const products=JSON.parse(await fs.readFile(dir+'data/kiemelt_12_termek.json','utf8'));
const ps=wb.worksheets.add('Kiemelt termékek');
const pk=Object.keys(products[0]);
ps.getRange('A1').write([['ID','Regisztersor','Termék','SKU','Méret cm','Szín','Anyag','Ár','Árstátusz','Terméklink','Rendereltérés','Nyitott kapu','Szállítás','Szerep','Ellenőrzés'],...products.map(p=>pk.map(k=>p[k]))]);
ps.getRange('A1:O13').format.wrapText=true;
ps.getRange('A1:O1').format.fill='#303E3C';ps.getRange('A1:O1').format.font.color='#FFFFFF';
ps.getRange('A1:O13').format.columnWidth=24;ps.getRange('C1:C13').format.columnWidth=38;ps.getRange('J1:L13').format.columnWidth=60;ps.getRange('A2:O13').format.rowHeight=110;ps.getRange('A1:O13').format.verticalAlignment='center';ps.getRange('A1:O13').format.font.size=10;ps.showGridLines=false;ps.freezePanes.freezeRows(1);

const sum=wb.worksheets.add('Összesítő'), reg=wb.worksheets.add('Elemregiszter'), bridge=wb.worksheets.add('Baseline egyeztetés');
const headers=['Lakás','Helyiség','Elemkód','Render','Baseline sor','Fix / stílus','Szakma','Termék / munka','Márka','SKU','Terméklink','Méret','Szín','Anyag','Mennyiség','Egység','Bruttó egységár Ft','Szállítás Ft','Szerelés Ft','Egyéb Ft','Teljes bruttó Ft','Árstátusz','Árforrás','Ellenőrzés dátuma','Átfutás','A/B/C','Render egyezés','Jóváhagyás','Megrendelés','Felelős','Szakmai ellenőrzés','Megjegyzés','Gazdaságos egységár Ft','Gazdaságos teljes Ft','Gazdaságos változtatás','Garancia','HU szállítás / készlet','Alternatíva 1','Alternatíva 2'];
const keys=['lakas','helyiseg','elemkod','render','baseline','kor','szakma','megnevezes','marka','sku','link','meret','szin','anyag','mennyiseg','egyseg','egysegar','szallitas','szereles','egyeb',null,'arstatusz','arforras','datum','atfutas','abc','egyezes','jovahagyas','rendeles','felelos','ellenorzes','megjegyzes','gazdasagos',null,'optimalizalas','garancia','szallithatosag','alt1','alt2'];
const matrix=rows.map(r=>keys.map(k=>k==='gazdasagos'?(r[k]??r.egysegar): k?(r[k]??'PENDING'):null));
reg.getRange('A1').write([headers,...matrix]);const end=rows.length+1;
reg.getRange(`U2:U${end}`).formulas=rows.map((r,i)=>[`=O${i+2}*Q${i+2}+SUM(R${i+2}:T${i+2})`]);
reg.getRange(`AH2:AH${end}`).formulas=rows.map((r,i)=>[`=O${i+2}*AG${i+2}+SUM(R${i+2}:T${i+2})`]);
reg.tables.add(`A1:AM${end}`,true,'Elemek');reg.freezePanes.freezeRows(1);reg.freezePanes.freezeColumns(3);
reg.getRange(`Q2:U${end}`).setNumberFormat('#,##0;(#,##0);"–"');reg.getRange(`AG2:AH${end}`).setNumberFormat('#,##0;(#,##0);"–"');
reg.getRange(`V2:V${end}`).dataValidation={rule:{type:'list',values:['előzetes becslés','ellenőrzött webshopár','beszállítói ajánlat']}};
reg.getRange(`AB2:AB${end}`).dataValidation={rule:{type:'list',values:['PENDING','jóváhagyott','elutasított']}};
reg.getRange(`Q2:T${end}`).format.font.color='#0000FF';reg.getRange(`AG2:AG${end}`).format.font.color='#0000FF';
sum.getRange('A2').values=[['Kyoto Ink S01 – költség és döntések']];sum.getRange('A4:C4').values=[['Mutató','Ft / darab','Értelmezés']];
sum.getRange('A5:C15').values=[['Alapkeret',18000000,'Bruttó, tervezhető'],['Külön tartalék',2000000,'Érintetlen; az előrejelzés nem ebből finanszírozott'],['Fő előrejelzés',null,'Aktuális, teljes tartalom'],['Gazdaságos javaslat',null,'Még nincs optimalizált változat; egyelőre a fővel azonos'],['Fő eltérés a kerettől',null,'Pozitív = túllépés'],['Gazdaságos eltérés',null,'Pozitív = túllépés'],['Ellenőrzött webshopár rész',null,'Termékérték; szállítás/szerelés becslése külön maradhat'],['Beszállítói ajánlat rész',null,'Csak valódi beérkezett ajánlat'],['Még becsült rész',null,'Minden nem igazolt ár'],['Megrendelt érték',null,'Jelenleg rendelés nincs'],['Tételszám',rows.length,'Új sor után a képletek tartományát bővíteni kell']];
sum.getRange('B7:B14').formulas=[[`=SUM('Elemregiszter'!U2:U${end})`],[`=SUM('Elemregiszter'!AH2:AH${end})`],['=B7-B5'],['=B8-B5'],[`=SUMIFS('Elemregiszter'!U2:U${end},'Elemregiszter'!V2:V${end},"ellenőrzött webshopár")`],[`=SUMIFS('Elemregiszter'!U2:U${end},'Elemregiszter'!V2:V${end},"beszállítói ajánlat")`],['=B7-B11-B12'],[`=SUMIFS('Elemregiszter'!U2:U${end},'Elemregiszter'!AC2:AC${end},"megrendelt")`]];
sum.getRange('A17:C18').values=[['Adatállapot','2026-10-26','Folyamatban; teljes műszaki jóváhagyás nincs.'],['Használat','Kék számok szerkeszthetők','Csak az Elemregiszter adatait módosítsd; a kiegészítő exportok pillanatképek.']];
let at=21;
for(const [label,key,col] of [['Helyiségenként','helyiseg','B'],['Szakmánként','szakma','G'],['Fix / stílus','kor','F'],['Megrendelés','rendeles','AC']]){
  sum.getRange(`A${at}:C${at}`).values=[[label,'Fő Ft','Gazdaságos Ft']];at++;
  for(const val of [...new Set(rows.map(r=>r[key]))]){sum.getRange(`A${at}`).values=[[val]];sum.getRange(`B${at}:C${at}`).formulas=[[`=SUMIFS('Elemregiszter'!$U$2:$U$${end},'Elemregiszter'!$${col}$2:$${col}$${end},A${at})`,`=SUMIFS('Elemregiszter'!$AH$2:$AH$${end},'Elemregiszter'!$${col}$2:$${col}$${end},A${at})`]];at++;}at+=2;
}
const fixed=[['01',400000],['02b',1100000],['02c',300000],['05',800000],['06',800000],['08',500000],['09',450000],['13a',1700000],['13b',300000],['13c',600000],['13d',550000],['13e',450000],['14',450000]];
const bs=[...fixed.map(([code,n])=>[code,n,n]),...old.map(r=>[r.koltsegsor,+r.fo_brutto_Ft,+r.gazdasagos_brutto_Ft]),['UJ',0,0]];
bridge.getRange('A1:G1').values=[['Baseline sor','Eredeti fő Ft','Eredeti gazdaságos Ft','Aktuális fő Ft','Gazdaságos javaslat Ft','Eltérés eredeti gazdaságostól Ft','Tartalom']];
for(let i=0;i<bs.length;i++){const n=i+2;bridge.getRange(`A${n}:C${n}`).values=[bs[i]];bridge.getRange(`D${n}:F${n}`).formulas=[[`=SUMIFS('Elemregiszter'!$U$2:$U$${end},'Elemregiszter'!$E$2:$E$${end},A${n})`,`=SUMIFS('Elemregiszter'!$AH$2:$AH$${end},'Elemregiszter'!$E$2:$E$${end},A${n})`,`=E${n}-C${n}`]];bridge.getRange(`G${n}`).values=[[rows.filter(r=>r.baseline===bs[i][0]).map(r=>r.megnevezes).join('; ')]];}
let total=bs.length+2;bridge.getRange(`A${total}`).values=[['Összesen']];bridge.getRange(`B${total}:F${total}`).formulas=[['B','C','D','E','F'].map(c=>`=SUM(${c}2:${c}${total-1})`)];
for(const sh of [sum,reg,bridge]){const used=sh.getUsedRange();used.format.font.name='Arial';used.format.font.size=10;used.format.rowHeight=30;used.format.verticalAlignment='center';sh.showGridLines=false;used.format.columnWidth=22;}
reg.getRange(`H1:N${end}`).format.columnWidth=42;reg.getRange(`W1:AM${end}`).format.columnWidth=42;reg.getRange(`A1:G${end}`).format.columnWidth=18;reg.getRange(`H1:AM${end}`).format.wrapText=true;reg.getRange(`A2:AM${end}`).format.rowHeight=72;
reg.getRange('A1:AM1').format={fill:'#303C3B',font:{color:'#FFFFFF',bold:true},wrapText:true,rowHeight:45};
sum.getRange(`A1:A${at}`).format.columnWidth=45;sum.getRange(`B1:B${at}`).format.columnWidth=22;sum.getRange(`C1:C${at}`).format.columnWidth=90;sum.getRange(`B5:C${at}`).setNumberFormat('#,##0;(#,##0);"–"');sum.getRange('A2').format.font.size=16;sum.getRange('A4:C4').format={fill:'#303C3B',font:{bold:true,color:'#FFFFFF'}};sum.getRange('B5:B6').format.font.color='#0000FF';
bridge.getRange('B2:F'+total).setNumberFormat('#,##0;(#,##0);"–"');bridge.getRange('A1:G1').format={fill:'#303C3B',font:{bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:45};bridge.getRange('G1:G'+total).format.columnWidth=85;bridge.getRange('G2:G'+total).format.wrapText=true;bridge.getRange('A2:G'+total).format.rowHeight=100;
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Összesítő!A5:B15',include:'values,formulas',tableMaxRows:11,tableMaxCols:2,maxChars:2500})).ndjson);
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:20},maxChars:2000})).ndjson);
await fs.mkdir(dir+'outputs',{recursive:true});
await (await SpreadsheetFile.exportXlsx(wb)).save(dir+'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx');
for(const [sheet,range] of [['Kiemelt termékek','C1:F4'],['Összesítő','A2:C18'],['Elemregiszter','A1:H7'],['Baseline egyeztetés','A1:F8']]){const im=await wb.render({sheetName:sheet,range,scale:1.5,format:'png'});await fs.writeFile(dir+'outputs/'+sheet+'.png',new Uint8Array(await im.arrayBuffer()));}

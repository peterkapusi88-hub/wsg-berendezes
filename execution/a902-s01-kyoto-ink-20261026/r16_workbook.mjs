import fs from 'node:fs/promises';
import {SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const base=fileURLToPath(new URL('.',import.meta.url))+'R16_feluletek_fiokok/';
const r=async n=>JSON.parse(await fs.readFile(base+n,'utf8'));
const parts=await r('data/parts.json'),holes=await r('data/holes.json'),ds=await r('data/drawers.json'),cost=await r('data/cost.json'),light=await r('data/lighting.json'),art=await r('data/artwork.json'),materials=await r('data/materials.json'),snap=await r('audit/R15_excel_snapshot.json');
const raw=await fs.readFile(base+'sources/TV_R15_eredeti_munkafuzet.xlsx');
const w=await SpreadsheetFile.importXlsx(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.byteLength));
const s={};
function table(n,title,heads,rows,last){const sh=w.worksheets.add(n);s[n]=sh;sh.showGridLines=false;sh.getRange('A1').values=[[title]];sh.getRange('A1').format.font={name:'Arial',size:16,bold:true};const end=rows.length+5;sh.getRange(`A5:${last}${end}`).format={font:{name:'Arial',size:10},wrapText:true,columnWidth:24,rowHeight:36};sh.getRange(`A5:${last}5`).values=[heads];sh.getRange(`A5:${last}5`).format={fill:'#4e4035',font:{name:'Arial',size:10,bold:true,color:'#ffffff'}};if(rows.length)sh.getRange(`A6:${last}${end}`).values=rows;sh.freezePanes.freezeRows(5);return sh;}
const old=new Map(snap.sheets.Darabok.slice(5).map(x=>[x[0],x]));
table('R16_Attekintes','R16 / ÉRVÉNYES TERVI RE VÍZIÓ /6 magas fiók',['Kérdés','Válasz'],[['Állapot','A régiR15 lapok változatlan archívum. Műhelyi alap: azR16 lapok és azR16 címkék.'],['Alsó sor','720+450+450+1080+450+450mm; mindenfront egy magas fiók.'],['Felső sor','720mm torony +200mm bronzbetét +4x670mm panelosztás.'],['Működés','Blum MOVENTO +TIPONBLUMOTION; hat külön fiókszenzor, két ajtószenzor.'],['Alkatrész',parts.length],['Furat',holes.length],['Fiókok nettó belső tere, liter',null],['Összes fényforrás W',null],['Feltételes projektösszeg Ft',null],['Még nyitott','Felmérés, anyag/nyomatminta, MOVENTO sablonfuratok, gépi próba, asztaleltolás, fal/villamos jóváhagyás.'],['Keret','18M cél +külön2M tartalék. A terv jelenleg nincs18Mkereten belül.']],'B');
s.R16_Attekintes.getRange('A5:B16').format.columnWidth=62;s.R16_Attekintes.getRange('B5:B16').format.columnWidth=110;s.R16_Attekintes.getRange('B12').formulas=[['=SUM(R16_Fiokok!G6:G11)']];s.R16_Attekintes.getRange('B13').formulas=[['=R16_Feny!B20']];s.R16_Attekintes.getRange('B14').formulas=[['=R16_Koltseg!B23']];
table('R16_Darabok','Készméretek / megőrzött kézi éladatok / újraszámolt nyersméret',['ID','Név','Umm','Vmm','tmm','Anyag','E1','E2','E3','E4','Uráhagyás','Vráhagyás','NyersU','NyersV','Ckód','Műhelymegjegyzés','Furat','Revízió'],parts.map(p=>{let a=old.get(p.id);return[p.id,p.name,p.x,p.y,p.t,p.material,...(a?a.slice(6,12):[...p.edge,null,null]),null,null,a?.[15]??'NYITOTT',a?.[16]??'Új alkatrész; műhely ellenőrzi',p.hole_count,'R16:'+p.id]}),'R');
for(let i=6;i<parts.length+6;i++)s.R16_Darabok.getRange(`M${i}:N${i}`).formulas=[[`=IF(COUNT(H${i},J${i},K${i})=3,C${i}-H${i}-J${i}+K${i},"NYITOTT")`,`=IF(COUNT(G${i},I${i},L${i})=3,D${i}-G${i}-I${i}+L${i},"NYITOTT")`]];
s.R16_Darabok.getRange(`G6:L${parts.length+5}`).format.fill='#fff0ca';s.R16_Darabok.getRange(`O6:P${parts.length+5}`).format.fill='#fff0ca';
table('R16_Furatok','Szerkezeti furatok / a külön megjelölt vasalati sablonműveletek nélkül',['ID','Darab','Funkció','U','V','W','IrányU','IrányV','IrányW','Átmérő','Mélység','Forrás'],holes.map(h=>[h.id,h.part,h.kind,...h.local_UVW,...h.local_axis,h.diameter,h.depth,h.source]),'L');s.R16_Furatok.getRange(`L5:L${holes.length+5}`).format.columnWidth=65;
table('R16_Fiokok','Kapacitás és tömeg / a40kg sín nem azonos a TIPON egység20kg határával',['Fiók','Modulmm','Belsőszél','Belsőmély','Belsőmagas','NL','Liter','Üreskg becsült','TIPON','Összkg határ','Hasznoskg becsült','Szinkronmm','Stabilizátormm'],ds.map(d=>[d.id,d.width,...d.inside,d.NL,null,d.empty_mass_estimate_kg,d.motion_unit,d.max_total_kg,null,d.sync_cut_mm,d.stabilizer_cut_mm]),'M');
for(let i=6;i<=11;i++){s.R16_Fiokok.getRange(`G${i}`).formulas=[[`=C${i}*D${i}*E${i}/1000000`]];s.R16_Fiokok.getRange(`K${i}`).formulas=[[`=J${i}-H${i}`]];}s.R16_Fiokok.getRange('G6:K11').setNumberFormat('0.00');
table('R16_Feny','24V / belső fény ajtónként-fiókonként / bronzbetét külön kör',['Ág','LEDmm','W/m','W','A','Vezérlés'],light.circuits.map(q=>[q.id,q.length_mm,q.wpm,null,null,q.control]),'F');
for(let i=6;i<6+light.circuits.length;i++)s.R16_Feny.getRange(`D${i}:E${i}`).formulas=[[`=B${i}/1000*C${i}`,`=D${i}/24`]];
s.R16_Feny.getRange('A20:B23').values=[['ÖsszesW',null],['TápegységW',151.2],['Terhelés',null],['Fizikai ellenőrzés','Nincs beüzemelve; csatlakozó és hőpróba szükséges.']];s.R16_Feny.getRange('B20').formulas=[['=SUM(D6:D16)']];s.R16_Feny.getRange('B22').formulas=[['=B20/B21']];s.R16_Feny.getRange('B22').setNumberFormat('0.0%');
table('R16_Koltseg','R16 változás / minden ár bruttó becslés / teljes régi csomag kiváltása',['ID','Tartalom','Menny','KiváltottFt','AlsóegységFt','VárhatóegységFt','FelsőegységFt','Alsónövekmény','Várhatónövekmény','Felsőnövekmény','Alap'],cost.rows.map(q=>[...q.slice(0,7),null,null,null,q[7]]),'K');
for(let i=6;i<cost.rows.length+6;i++)s.R16_Koltseg.getRange(`H${i}:J${i}`).formulas=[[`=C${i}*E${i}-D${i}`,`=C${i}*F${i}-D${i}`,`=C${i}*G${i}-D${i}`]];
const last=cost.rows.length+5;s.R16_Koltseg.getRange('G18').values=[['NÖVEKMÉNY']];s.R16_Koltseg.getRange('H18:J18').formulas=[[`=SUM(H6:H${last})`,`=SUM(I6:I${last})`,`=SUM(J6:J${last})`]];s.R16_Koltseg.getRange('A21:B27').values=[['R15 feltételes projektösszeg',cost.R15_conditional_total],['Főregiszter R16 előtti összege',cost.master_readback_total],['R16 frissített projektelőirányzat',null],['Eltérés18M-tól',null],['Külön tartalék',2000000],['CsakR16 bizonytalansági sáv alsó',null],['CsakR16 bizonytalansági sáv felső',null]];
for(const [cell,f] of [['B23','=B21+I18'],['B24','=B23-18000000'],['B26','=B21+H18'],['B27','=B21+J18']])s.R16_Koltseg.getRange(cell).formulas=[[f]];
s.R16_Koltseg.getRange('D6:J18').setNumberFormat('#,##0 "Ft"');s.R16_Koltseg.getRange('B21:B27').setNumberFormat('#,##0 "Ft"');s.R16_Koltseg.getRange('B5:B27').format.columnWidth=65;s.R16_Koltseg.getRange('K5:K14').format.columnWidth=70;
table('R16_Feluletek','Tusgrafika közös koordinátán;200mm bronzbetét nincs teleszínezve mintával',['Darab','X','Z','Wmm','Hmm','Nettóm²','Kifutóvalm²','Fájl'],art.panels.map(p=>[p.part,p.X,p.Z,p.W,p.H,null,null,p.TRIM]),'H');for(let i=6;i<=11;i++)s.R16_Feluletek.getRange(`F${i}:G${i}`).formulas=[[`=D${i}*E${i}/1000000`,`=(D${i}+20)*(E${i}+20)/1000000`]];
table('R16_Anyagok','Anyag és technológia / fizikai minta még nem jóváhagyott',['Kód','Rétegrend','Méret/alkalmazás','Próba','Megjegyzés'],materials,'E');s.R16_Anyagok.getRange('B5:E9').format.columnWidth=55;s.R16_Anyagok.getRange('A6:E9').format.rowHeight=100;
w.worksheets.getItem('Attekintes').getRange('A1:B14').values=[['R16 / AKTUÁLIS TERV / 2026.10.29.','A további R15 lapok archív előzmények; az új adatok az R16_ kezdetű lapokon.'],['Lapalkatrész',parts.length],['Szerkezeti furat',holes.length],['Alsó fiókok',6],['Frontok','Minden alsó front egyetlen magas fiók. A magas szekrény ajtós.'],['Bronzbetét','200 mm, önálló panel, a szekrény oldaláról megvilágítva.'],['Projektösszeg',cost.conditional_expected],['Árstátusz','Becslés, nem beszállítói ajánlat.'],['Teljes világítás W',light.power_W],['Fontos','MOVENTO sablonfuratok, falrögzítés, anyagminta és műhelypróba nyitott.'],['Fiók- és ajtófény','8 külön nyitásérzékelő.'],['Kézi adatok','Meglévő él- és műhelyadatok ID szerint megőrizve.'],['Eredeti fájl','sources/TV_R15_eredeti_munkafuzet.xlsx változatlanul megőrizve.'],['Érvényes címke','R16: előtag; R15 programot az új alsó sorhoz ne használj.']];
w.recalculate();if(Math.abs(s.R16_Koltseg.getRange('B23').values[0][0]-cost.conditional_expected)>.01)throw Error('Budget mismatch');
await(await SpreadsheetFile.exportXlsx(w)).save(base+'TV_R16_muhelyi_regiszter.xlsx');
for(const n of ['R16_Attekintes','R16_Fiokok','R16_Feny','R16_Koltseg']){let im=await w.render({sheetName:n,range:n==='R16_Koltseg'?'A21:B27':n==='R16_Attekintes'?'A5:B10':'A5:G11',scale:1});await fs.writeFile(base+'audit/xlsx_'+n+'.png',new Uint8Array(await im.arrayBuffer()));}
console.log(JSON.stringify({total:s.R16_Koltseg.getRange('B23').values,power:s.R16_Feny.getRange('B20').values,originalSheets:'preserved by import'}));
// Update the single live project workbook in place, preserving unrelated cells and all sheets.
const masterRaw=await fs.readFile(base+'sources/A902_elo_regiszter_R16_elott.xlsx');
const master=await SpreadsheetFile.importXlsx(masterRaw.buffer.slice(masterRaw.byteOffset,masterRaw.byteOffset+masterRaw.byteLength));
const e=master.worksheets.getItem('Elemregiszter');
const updates=[
 [31,'KI-030',935500,765500,'720 mm torony +200 mm matt bronzbetét +4×670 mm falburkolati mező','M16-WALL / M16-BRONZE / M16-TOWER','720+200+2680 mm; névleges teljes3600 mm','18 mm hordozó; Bely+Print jelölt; bronzbarna matt felület; látható tusgrafika vektorban.'],
 [32,'KI-031',985000,350000,'Hat magas fiókos alsó médiafal, eltérő frontszélességekkel','M16-DRAWER15 / bronzbarna front','720+450+450+1080+450+450 mm; egy magas fiók frontonként','760H3000S +T51.7601 +TIPONBLUMOTION S0/S1 +ZS7M400MU; sablonműveletek nyitottak.'],
 [33,'KI-032',504800,135000,'W01 rögzítési és műhelyi csomag R15→R16 egyeztetve','Camar807 IN / MF375 / kötőelemek','7 korpuszpár;4 főpanel +bronzbetét','R15 H01–H04,H06,M01–M03:489800 Ft +15000 Ft hetedik Camar pár. Nem adandó újra az R15 összeghez.'],
 [35,'KI-034',32000,30000,'Vogel TVM3605 konzol','Vogel3836050','675×22×428 mm gyári befoglaló','R15 H05 kiváltja a régi30000 Ft-os konzolkeretet. Falhorgony szakági ellenőrzés kell.'],
 [115,'KI-114',512000,150000,'W01 hangulatfény +6fiók és2ajtó nyitásérzékelős belső fénye','24V2700K; LPV15024; Sunricher; Loox5','102,8 W összes;151,2 W tápegység;8 külön szenzor','R15 L01–L07:281000 Ft +196000 Ft belső világítás +35000 Ft szervizáthelyezés. Nem dupla tápegység.']
];
for(const [row,id,price,oldPrice,name,material,dimensions,note] of updates){
 if(e.getRange('C'+row).values[0][0]!==id)throw Error('Master ID mismatch '+id);
 e.getRange('H'+row).values=[[name]];e.getRange('L'+row).values=[[dimensions]];e.getRange('N'+row).values=[[material]];
 e.getRange('D'+row).values=[['R16_feluletek_fiokok/data/handoff_manifest.json']];
 e.getRange('J'+row).values=[[id==='KI-031'?'760H3000S; T51.7601; T60L7040/T60L7140; ZS7M400MU':id==='KI-034'?'3836050 / TVM3605':id==='KI-114'?'LPV-150-24; SR-ZG9101FA-DIM; LED3040 833.76.300; sensor833.89.253':material]];
 e.getRange('K'+row).values=[['R16_feluletek_fiokok/data/sources.json; gyártói adatok, nem kereskedői árforrás']];
 e.getRange('Q'+row).values=[[price]];e.getRange('AG'+row).values=[[price]];
 e.getRange('W'+row).values=[['R16/data/cost.json és R15/data/cost_allowance.json; bruttó tervezői becslés, nem ajánlat']];e.getRange('X'+row).values=[['2026-10-29']];e.getRange('AF'+row).values=[[note]];
 e.getRange('AI'+row).values=[['R16 főtartalom. Ugyanez az előirányzat; új önálló gazdaságos változat nincs igazolva.']];
 e.getRange('AO'+row).values=[['R16_feluletek_fiokok/rajzok/TV_R16_asztalos_tervcsomag.pdf']];e.getRange('AP'+row).values=[['R16_feluletek_fiokok/rajzok/TV_R16_koordinacio.blend; data/parts.json']];
 e.getRange('AR'+row).values=[['Névleges CAD-méret; nem felmérés. Minta, fal és műhelypróba nyitott.']];
}
const change=master.worksheets.add('R16 változások');change.getRange('A1:F6').values=[['Elem','Előző Ft','Új Ft','Különbség Ft','Tartalom','Státusz'],...updates.map(([row,id,price,oldPrice,name])=>[id,oldPrice,price,null,name,'Becslés; nincs megrendelve'])];
for(let i=2;i<=6;i++)change.getRange('D'+i).formulas=[[`=C${i}-B${i}`]];
change.getRange('A1:F6').format={font:{name:'Arial',size:11},columnWidth:28,rowHeight:52,wrapText:true};change.getRange('E1:E6').format.columnWidth=65;
change.getRange('A9:B12').values=[['R16 frissített projektelőirányzat',null],['Külön érintetlen tartalék',2000000],['Kereteltérés',null],['Átfedés megjegyzés','A korábbi csomagárakat kiváltottuk. A további szakági csomagokkal esetleges átfedést beszállítói ajánlattal kell egyeztetni.']];
change.getRange('B9').formulas=[["='Összesítő'!B7"]];change.getRange('B11').formulas=[['=B9-18000000']];
master.recalculate();const total=master.worksheets.getItem('Összesítő').getRange('B7').values[0][0];if(total!==cost.conditional_expected)throw Error('Live total mismatch '+total);
await(await SpreadsheetFile.exportXlsx(master)).save(base+'../outputs/A902_Kyoto_Ink_elo_regiszter.xlsx');
console.log(JSON.stringify({liveProjectTotal:total,updatedRows:updates.map(x=>x[1])}));

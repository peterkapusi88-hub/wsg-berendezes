from pathlib import Path
from openpyxl import load_workbook
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from pypdf import PdfReader,PdfWriter
import json,csv,hashlib
p=Path('execution/a902-s01-kyoto-ink-20261026');o=p/'R10/specifikacio';o.mkdir(exist_ok=True)
f=p/'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx';before=hashlib.sha256(f.read_bytes()).hexdigest();w=load_workbook(f,data_only=True);rows={r[2]:list(r) for r in list(w['Elemregiszter'].values)[1:] if r[2]}
ids=['KI-036','KI-028','KI-029','KI-037','KI-038','KI-039','KI-113','KI-R10-01','KI-135']
with (o/'termekek_arakkal.csv').open('w',encoding='utf-8-sig',newline='') as out:
 c=csv.writer(out,delimiter=';');c.writerow(['Elem','Megnevezés','Márka','SKU','Méret','Mennyiség','Egységár Ft','Összes Ft','Árstátusz','Ellenőrizve','Link','Eltérés']);
 for id in ids:
  r=rows[id];c.writerow([r[i] for i in [2,7,8,9,11,14,16,20,21,23,10,26]])
font='/System/Library/Fonts/Supplemental/';pdfmetrics.registerFont(TTFont('A',font+'Arial.ttf'));pdfmetrics.registerFont(TTFont('AB',font+'Arial Bold.ttf'))
st=getSampleStyleSheet();st.add(ParagraphStyle(name='BodyHU',fontName='A',fontSize=10,leading=14,spaceAfter=8));st.add(ParagraphStyle(name='TitleHU',fontName='AB',fontSize=20,leading=24,spaceAfter=14));st.add(ParagraphStyle(name='HeadHU',fontName='AB',fontSize=12,leading=16,spaceAfter=8));st.add(ParagraphStyle(name='SmallHU',fontName='A',fontSize=8,leading=11))
a=[]
def para(t,style='BodyHU'):a.append(Paragraph(t,st[style]))
def heading(t):para(t,'HeadHU')
def money(v):return f'{v:,.0f}'.replace(',',' ')+' Ft'
para('Kyoto Ink R10 | Mit lehet megépíteni?','TitleHU');para('Asztalos ajánlatkérési kiegészítés és nappali–étkező terméklista | 2026.10.28.')
a.append(Image(str(p/'R10/images/V01_R10_RETRY.png'),width=490,height=307));a.append(Spacer(1,12))
heading('A rövid válasz')
para('A terv méretekkel leírható és beárazható, de a generált kép nem teljesen mérethű gyártási bizonyíték. A műszaki alap az R10 Blender-modell és a mellékelt rajz. A képi felületek, a kanapé részletei és a városkép nem igazolt másolatai a megvalósulásnak.')
para('A médiafal ajánlatkérésre előkészíthető. Gyártás előtt helyszíni méret, falrögzítés, teljes belső kiosztás, vasalatkiválasztás és anyag-/nyomatminta jóváhagyása szükséges. Az itt részletezett belső kiosztás új ajánlati javaslat; az R10 tömör geometriai modellje nem tartalmazza a belső szerkezetet.')
para('Teljes lakás előrejelzése: <b>24 673 390 Ft</b>. A 18 milliós célhoz képest <b>+6 673 390 Ft</b>; a külön 2 millió tartalék érintetlen. Ez tehát jelenleg nem kereten belüli terv. A részösszegek a meglévő Excel sorai, nem hozzáadandó új költségek.')
a.append(PageBreak());para('01 | Készbútorok és mozgatható elemek','TitleHU')
short=['Lennon jobb sarokkanapé','Toni 160 cm étkezőasztal','Eamy szék, 6 db','CF-01 egyedi dohányzóasztal','ST-01 egyedi mellékasztal','Nifelia szőnyeg + alátét keret','Hue Enrave M mennyezeti','3 párna + 1 takaró keret','Kerámia, könyv, kis növény keret']
data=[['Elem / termék','Menny.','Egységár','Összes','Ár alapja']]
for id,n in zip(ids,short):
 r=rows[id];data.append([Paragraph(id+'<br/>'+n,st['SmallHU']),str(r[14]),money(r[16]),money(r[20]),Paragraph(('Webshop '+str(r[23]) if r[21]=='ellenőrzött webshopár' else 'Becslés / előirányzat'),st['SmallHU'])])
t=Table(data,colWidths=[192,35,80,80,105],repeatRows=1);t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'A'),('FONTSIZE',(0,0),(-1,-1),8),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcded5')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,-1),.3,colors.lightgrey)]));a.append(t);a.append(Spacer(1,12))
para('A három konkrét fő készbútor (kanapé + asztal + 6 szék): <b>'+money(sum(rows[i][20] for i in ids[:3]))+'</b>. A fenti teljes lista: <b>'+money(sum(rows[i][20] for i in ids))+'</b>. Nem a teljes nappali vagy lakás ára.')
para('Webshopadatot a korábbi ellenőrzésből vettem át; a mai újralekérés Westwing-elérési hibával és Kave429 korlátozással végződött. Új ár- vagy készletigazolás nincs. Eamy75 180Ft/db tervezési átszámítás, nem fix magyar ajánlat. A 0Ft soronkénti szállítás nem ingyenes szállítás: központi logisztikai kerethez tartozik.')
para('Pontos SKU-k, méretek, terméklinkek és eltérések a csatolt CSV-ben. CF-01/ST-01 egyedi asztalok, nem webshoptermékek. A képen látható extra előtéri sötét tömb darabszámát és szerepét az ST-01 egy darabos regiszterével külön egyeztetni kell; nem igazolt második ingyenes asztal. A függöny és kültér nincs ebben a részösszegben.')
a.append(PageBreak());para('02 | Asztalos ajánlatkérési specifikáció','TitleHU')
heading('W01 külső megjelenés - megőrzendő')
para('3600mm teljes szélesség, a tervi4000mm falon300/100mm végmaradék. Bal torony720mm; süllyesztett szervizsáv120mm; négy690mm panelmező. Alsó bútor3600×400×400mm, alsó él150mm, felső él550mm. Torony felső rész720×400×2330mm, teteje2880mm. Felső két front névleges360mm; a rajz szerinti hézaggal kb357×2327mm. A méretek ajánlati, nem felmért gyártási méretek.')
heading('Belső szerkezet - ajánlati javaslat, külön gyártmánytervvel')
para('18mm korpusz/front,8mm hátfal, látható éleken1mm ABS. Torony két egymás melletti függőleges rekesz középosztóval: elméleti tiszta szélesség (720−3×18)/2=333mm; 5 állítható polc rekeszenként, összes10. Polc névleges333mm helyett kb331mm,320mm mélységű javaslat, végleges hátfal-/pánthely szerint. 6 szint/rekesz, kb370–380mm közökkel; összes kb3,31 folyóméter polc, 1,06m² felület a10 polcon. Pántszámot a2327mm magas front tömege alapján a vasalatgyártó méretezi.')
para('Alsó bútor:1×720 és4×690mm modul; 120mm betét nem tároló. Belső névleges szélességek684 és654mm, magasság364mm. Modulonként1 kivehető polc, kb320mm mélységgel; egyik690mm modul szellőző, szerszámmal oldható elektromos szervizrekesz. Ott nem számolható teljes polckapacitás. Oldalra nyíló front/pánt javaslat, nem lehajló ajtóként véglegesítve; a nyitási ívet a kanapéval ellenőrizni kell. Hosszú frontok vetemedési kockázatát gyártó ellenőrizze.')
heading('Felület, grafika, csatlakozás')
para('Grafit jelölt EGGER U961 ST7; TV-mező18mm stabil lap +18mm szerelőlégrés. Matt nyomat, mintázandó finoman texturált hordozón; nem kő és nem relief. Tusgrafika az R06 master maszkról, egy közös koordinátarendszerből panelenként kivágva. Ajtóréseken nem hidalható át. Szín és textúra nappali/2700K mintapróba után rögzíthető. Sáv, panelek, LED és tápegység szerelhető/bontható legyen.')
para('Fényprofil2,76+2,33+3,60=8,69m,10m rendelési kerettel. 9,6W/m feltételezéssel83,424W; az örökölt körszámítás még régi hosszakra utal, villamos aktualizálás kell. Falteher, rejtett konzolok, TV/VESA és vezetékezés szakági ellenőrzést igényel.')
para('Árkeret: KI-030765500 + KI-031350000 + KI-032135000 = <b>1 250 500Ft</b>, fény150000Ft külön KI-114. CF-01 700×450×350mm105000Ft; ST-01 300×300×450mm55000Ft,18mm dobozszerkezet, matt grafit lap, rejtett talp: ajánlati javaslat. Belsők, pántok, minták, felhordás és rögzítés tartalmát a kivitelező tételesen igazolja; ezek a keretek nem elfogadott ajánlatok.')
para('Az Excel tárgyhivatkozásai részben elavultak: KI-031 helyes R10_TV02_*, a panel R10_TV03_*. Ez a kiegészítés tisztázza; az élő munkafüzetet ebben a körben nem módosítottam. A modell tömör testei nem szabáslisták. Következő két oldal: meglévő R10 méretezett rajz és anyaglap.','SmallHU')
SimpleDocTemplate('/tmp/r10_spec_core.pdf',pagesize=(595,842),rightMargin=50,leftMargin=50,topMargin=36,bottomMargin=36).build(a)
wr=PdfWriter();
for fp in ['/tmp/r10_spec_core.pdf',str(p/'R10/drawings/W01_R10.pdf')]:
 for page in PdfReader(fp).pages:wr.add_page(page)
with (o/'R10_asztalos_es_termekarak.pdf').open('wb') as q:wr.write(q)
assert hashlib.sha256(f.read_bytes()).hexdigest()==before
(o/'ellenorzes.json').write_text(json.dumps({'source_workbook_sha256':before,'workbook_unchanged':True,'core_pages':len(PdfReader('/tmp/r10_spec_core.pdf').pages),'total_pages':len(wr.pages),'main_furniture_total':sum(rows[i][20] for i in ids[:3]),'listed_items_total':sum(rows[i][20] for i in ids),'project_total':w['Összesítő']['B7'].value,'price_recheck':'failed; dated register evidence preserved'},indent=2))
print((o/'ellenorzes.json').read_text())

"""Dimensioned technical drawing book; nominal construction, not shop approval."""
from pathlib import Path
src=(Path(__file__).parent/'r13_documents.py').read_text()
prefix=src.split("hdr('Az asztalosnak")[0].replace('R13','R14')
exec(compile(prefix,__file__+':helpers','exec'))
sections=json.loads((O/'data/sections.json').read_text());cost=json.loads((O/'data/cost_allowance.json').read_text());tip=json.loads((O/'data/tipon.json').read_text());service=json.loads((O/'data/lighting_service.json').read_text())
hdr('A rejtett szerkezetek kidolgozása','75 alkatrész | 579 tényleges CAD-furat | 69 aktív MPR-tervezet | 138 új párosított kötés')
img('belso.png',40,160,770,540)
y=700
for title,body in [('Ami elkészült','14 bükk rögzítőléc,7 hátsó merevítő,6 hátlap illesztési hézaga. Öt TIP-ON adapter tíz rögzítőfurata. Minden új alkatrész saját azonosítót és rajzlapot kapott.'),('Amit megtartottunk','A látható frontosztás, a3600mm-es szélesség és a2880mm-es tervezett magasság változatlan. Ezek még nem új helyszíni felmérésből származó méretek.'),('A kép jelentése','A megmunkált natív AutoCAD-testekből készült ellenőrzőkép. A színek anyagcsoportok; nem elfogadott felületminták. A kiemelt3–4.front nem valós nyitási helyzet.'),('Amit még nem bizonyít','Falrögzítési teherbírás, tényleges pántkinematika, woodWOP5 elfogadás és gépi szimuláció. A rajzadatbázis hibamentessége ezekre nem ad PASS-t.')]:
 txt(835,y,title,13,True);y=wrap(835,y-22,body,310,12)-22
wrap(45,111,'Kezdés az asztalosnak: TV_R14_belso.dwg + ez a rajzkönyv + az Excel Darabok/Furatok/Kötések lapja. A kész tervméret és a nyers szabásméret külön adat; a nyersméret csak a műhely élzárási és ráhagyási szabályával zárható le.',1090,11)
c.showPage()
hdr('Három tényleges metszet a CAD koordinátáiból','D01–D03 / bal szélső alsó korpusz / XY vízszintes metszetek / mm')
notes=[('Z=210 / léc az oldalhoz','4x30 csavar: Ø4 átmenő a18mm bükk lécben, Ø2,5x12 előfurat a korpuszban. A csavar feje belül van.'),('Z=225 / hátlap a léchez','3,5x20 csavar: Ø3,5 átmenő a8mm hátlapban, Ø2,5x12 a lécben. A két csavarirány15mm-rel eltolt.'),('Z=452 / hátsó merevítő','Ø8x30 csap:22mm a merevítő élében +12mm az oldalban. A7 merevítő összesen42 új csapot kap.')]
for i,(sec,(title,note)) in enumerate(zip(sections,notes)):
 ox=60+i*380;oy=310;s=3.5
 txt(ox,706,sec['id'],14,True);txt(ox,680,title,12,True)
 for r in sec['rectangles']:
  x,y,w,h=r['box'];c.setFillColor('#cbb991' if r['part'].startswith('KI14-BAT') else '#b2c2bd' if r['part'].startswith('KI14-RAIL') else '#d8d8cf');c.setStrokeColor('#33433e');c.rect(ox+x*s,oy+(y-320)*s,w*s,h*s,fill=1)
 for r in sec['bores']:
  x,y,w,h=r['box'];c.setFillColor('#fff4ee');c.setStrokeColor('#b74930');c.rect(ox+x*s,oy+(y-320)*s,w*s,h*s,fill=1)
 dim((ox,oy-20),(ox+18*s,oy-20),'18')
 dim((ox+27*s,oy+36*s),(ox+27*s,oy+54*s),'18')
 dim((ox+65*s,oy+54*s),(ox+65*s,oy+62*s),'8')
 wrap(ox,258,note,330,12)
 y=185
 for r in sec['rectangles']:
  txt(ox,y,r['part'],10);y-=17
wrap(55,90,'A piros körvonal a valódi furat metszete. Az oldalsó és hátsó csavar nem találkozik. A fúróátmérő/próbafúrás tervezői előírás; a konkrét lapanyag és csavar szerint próbadarabon ellenőrizendő. Szerkeszthető1:1DXF-ek: D01, D02, D03.',1080,11)
c.showPage()
hdr('Hátlap, rejtett betét és merevítés','Hézag, kötés, sorrend és hozzáférés – a látható frontfelület változtatása nélkül')
img('hatlap_reszlet.png',45,300,540,400)
txt(45,275,'Részlet kiemelt hátlappal és oldallappal; az eltolás csak szemléltetés.',10)
ys=700
for a,b in [('Hátlapok','Körben1mm tervezett illesztési hézag. Torony:2292x682x8; alsó1.:682x362x8; alsó2–5.:652x362x8. Az oldalankénti bükk léc18x18, a hátlap belső síkja Y374.'),('Lécek','Torony:2x2254mm. Alsó modulok:10x324mm. A köztes betéthez2x320mm. Összes nettó léchossz8,388m; a rendelési előirányzat20% tartalékkal10,066m.'),('Hátsó merevítők','Alul1x684x100x18 és4x654x100x18; fent2x333x100x18. Anyag:18mm rétegelt lemez, fafaj/minőség még mintázandó. A középosztó két oldalán a csaptengelyek10mm-rel eltoltak.'),('Rejtett alsó betét','A117x380x18 grafit betét hátulról kap rögzítést. Két18x18x320 léc, összesen8db4x30 csavar. A betéten6mm névleges anyag marad a12mm vakfurat előtt.'),('Szerelési sorrend','Száraz korpuszpróba → merevítők ragasztása és derékszögellenőrzés → lécek → hátlapok hátulról → alsó betét → pántok és TIP-ON → falrögzítés lezárása után helyszíni szerelés.'),('Szervizkorlát','A hátlap hátulról csavarozott: beépítés után csak a korpusz kiemelésével bontható. A tápegységhez/vezérlőhöz ezért elölről kivehető tálcát javaslunk. A hátlap nem szerelőajtó és nem teherhordó függesztő.')]:
 txt(620,ys,a,12,True);ys=wrap(620,ys-20,b,520,11)-16
wrap(45,215,'A falhoz rögzítés még külön tervezési feladat. Az új keresztlécek javítják a korpusz kialakítását és szerelhetőségét, de a falhorgonyok, fali sín és függesztő teherbírása nincs igazolva. Ezek furatait nem találjuk ki a fal ismerete nélkül.',520,12)
c.showPage()
hdr('Nyomásra nyitás: gyári adapterkiosztás','2 hosszú +3 rövid TIP-ON / 10 új adapterfurat / a két vitatott alsó front nélkül')
for i,(title,span,length) in enumerate([('Torony / 956A1004 +956A1201',32,79),('Alsó1,2,5 / 956.1004 +956.1201',17,53)]):
 ox=70+i*560;oy=450;s=4
 txt(ox,700,title,14,True);c.setFillColor('#deded7');c.setStrokeColor('#465854');c.rect(ox,oy,360,100,fill=1)
 line(ox,oy-20,ox,oy+125,'#ad5032',1.5)
 for yy in [20,20+span]:c.setStrokeColor('#a64632');c.circle(ox+yy*s,oy+50,2.5*s/2)
 dim((ox,oy+120),(ox+20*s,oy+120),'20');dim((ox+20*s,oy+145),(ox+(20+span)*s,oy+145),str(span))
 txt(ox,oy-55,'Korpusz első élétől mért gyári furathelyek',11);txt(ox,oy-80,'Ø2,5x10 előfurat: tervezői próbaérték',11)
y=310
for t in tip:
 txt(65,y,t['front'],11,True);txt(280,y,t['adapter']+' / '+t['support'],11);txt(690,y,'XYZ első furat: '+str(t['position'])+' mm',11);y-=27
wrap(65,143,'Gyári öntapadó ellenlemezt tervezünk: helyét a ténylegesen felszerelt nyitóval kell átjelölni. A ragasztás a választott belső felületen próbálandó. A3mm névleges nyomási hézag már a modellben van; a teljes fronttömeg és a nyitóerő működési próbája szükséges.',1070,11)
wrap(65,87,'Gyári forrás: Blum LIT.HNG4700.06.17,2.oldal; sources/Blum_TIPON_gyari_szereles.pdf. A rögzítési geometria gyári, a2,5mm pilotfurat nem minden lapra jóváhagyott gyári érték.',1070,10)
c.showPage()
hdr('Világítás és hozzáférhető szerelőtér','Méretezett helyfoglalási javaslat / nem villamos kiviteli kiadás')
ox,oy,s=65,250,.16
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm'];c.setStrokeColor('#a5aca6');c.setFillColor('#e5e6df');c.rect(ox+x*s,oy+z*s,w*s,h*s,fill=0)
for q in service['circuits']:
 a,b=q['polyline_mm'];line(ox+a[0]*s,oy+a[2]*s,ox+b[0]*s,oy+b[2]*s,'#ca8f20',3);txt(ox+a[0]*s+7,oy+a[2]*s+12,q['id'],11,True)
x,y,z,w,d,h=service['access_box_mm'];c.setFillColor('#bfdbcb');c.rect(ox+x*s,oy+z*s,w*s,h*s,fill=1);txt(ox+170,oy-30,'430x240x150mm szerviz-helyfoglalás',11)
y=700
for a,b in [('Fényágak','L01:3,60m /34,56W. L02:2,76m /26,50W. L03:2,33m /22,37W. Összesen8,69m és83,424W a feltételezett9,6W/m szalaggal.'),('Profil és fényforrás','KLUS PDS-4-ALU B1718 család:16x12mm, belső szélesség11,2mm. Legfeljebb10mm széles24V/2700K/CRI90 szalag javasolt. Pontos szalag-SKU, diffúzor, vágásosztás és színhűségi minta még nyitott.'),('Tápegység-jelölt','MEAN WELL LPV-150-24:191x63x37,5mm,151,2W. A tervezett szalagterhelés55,2%. Ez nem hőtechnikai vagy villamos jóváhagyás; a gyári hőmérsékleti korlátozásokat ellenőrizni kell.'),('Kábelút és szerviz','Kiállás azonosítása → elkülönített230V → elölről kivehető tálca → külön biztosított24V ágak. Az AV-rekeszben nincs polc. A három nyomvonal és a szerviztér a külön DXF-ben méretezett koordinátával szerepel.'),('Vezérlés és nyitott feltételek','3 külön dimmelhető ág. Hue-vezérlő még nincs kiválasztva/tesztelve. Vezetékméret, védelem, szellőzés, profilrögzítés és plafonhézag szakági ellenőrzést igényel. A panel mögötti helyfoglalás nem kész gyártási furat.')]:
 txt(760,y,a,12,True);y=wrap(760,y-20,b,380,11)-17
wrap(65,112,'Gyári méretforrások: KLUS PDS-4-ALU adatlap és MEAN WELL LPV,LPVL-150-SPEC2024-12-12. A teljes linkek a data/lighting_service.json állományban. A9,6W/m szalag tervezési paraméter; az ábrán nem bizonyított, kész fénytechnikai hatás látható.',1080,10)
c.showPage()
# Carry the genuinely dimensioned S10 alternative, explicitly outside the main model.
alternative=src.split("hdr('Alsó 3-4. rekesz:")[1].split("hdr('Műhelyi adatkapcsolat")[0]
exec(compile("hdr('Alsó 3-4. rekesz:"+alternative.replace('R13','R14'),__file__+':S10','exec'))
hdr('Költséghatás és a gyártási lezárás feltételei','A rejtett szerkezeti kiegészítés becslése / nem új teljes lakásköltségvetés')
cols=[55,135,670,760,880,1010]
for x,t in zip(cols,['Tétel','Tartalom','Mennyiség','Alsó Ft','Várható Ft','Felső Ft']):txt(x,710,t,11,True)
y=680
for r in cost:
 txt(cols[0],y,r[0],10);wrap(cols[1],y,r[1],500,10);txt(cols[2],y,f'{r[2]:g} {r[3]}',10)
 for x,price in zip(cols[3:],r[4:7]):txt(x,y,f'{r[2]*price:,.0f}'.replace(',',' '),11)
 line(50,y-29,1135,y-29,'#d5ded8');y-=51
tot=[sum(r[2]*r[i] for r in cost) for i in [4,5,6]]
txt(55,185,'Bruttó előirányzat:',13,True)
for x,v in zip(cols[3:],tot):txt(x,185,f'{v:,.0f}'.replace(',',' '),13,True)
wrap(55,151,'Ez a kiegészítés önálló, mennyiségi alapon készített becslése. Nem adjuk automatikusan a meglévő asztaloscsomaghoz: az ajánlatból először ki kell derülnie, mely kötéseket tartalmazta már. Nincs új fix beszállítói ár; a18milliós teljes keret teljesülését ez a csomag nem igazolja.',1080,11)
wrap(55,88,'Nyitott: helyszíni felmérés és anyagminta; falfüggesztési rendszer és terhelés; alsó3–4.front megoldása; teljes fényrendszer; gépi szerszámadatbázis, ütköző és elsődarab. A konkrét CAD-munkát ezek mellett elvégeztük, de a nyitott pontokat nem nevezzük jóváhagyottnak.',1080,10)
c.showPage()
hdr('Műhelyi átadás és elsődarab-ellenőrzés','Aktív programtervezet / a helyi címke–rajz–program kapcsolat ellenőrizhető')
y=705
for a,b in [('01 / Helyes revízió','A címke kulcsa R14:darabID. A kereső csakR14-et fogad el, majd ellenőrzi a fájlok SHA-256 hashét. Hiányzó vagy módosult fájlnál nem ad ki programútvonalat. Semmit nem indít a gépen.'),('02 / Kész és nyers méret','75 alkatrész, minden készméret az Excelben. Az élvastagság, ráhagyás ésC műhelykód kézi mezői az aktuálisR13-ból átvéve. A gyári lapszabászat/élzárás szabálya hiányában a nyersméret NYITOTT marad.'),('03 / Befogás','A/B rajzi koordinátarendszer, nem igazolt gépi ütköző. B oldal: U körüli fordítás. Azonosítani kell a gép ténylegesX/Y irányát, felső felületét, ütközőit, leszorítóit és a legkisebb biztonságosan befogható18x18léceket.'),('04 / Program','69 aktív MPR,579 fúrási művelet. Saját szöveges visszaolvasás megtörtént. A F_=STANDARD a műhely adatbázisára támaszkodik; nincs igazolt woodWOP5 megnyitás vagy gépi szimuláció.'),('05 / Próbadarab','Elsőként egy darabazonosítóval együtt próbálni kell a kétoldali furatot, a csap12/22mm párját, a csészét és az adaptert. Ellenőrizendő: tényleges furatpozíció, mélység, illesztés, áttörés, kiszakadás és felületjelölés.'),('06 / Nem CNC-maráspálya','AØ60AV átvezetés megmunkálási módját és szerszámát a műhelynek kell kijelölnie; a makró jelenleg átmérő szerinti fúrási tervezet. Nincs kitalált marószerszám, fordulatszám, ráállás vagy leszorítóhely.'),('07 / Mit nem helyettesít','A helyi SQLite-címkekereső nem Livewood-adatbázisba telepített integráció. A gépi elfogadást és elsődarabot a műhely rögzíti. Sem az AI, sem egy hibátlan DWG nem teszi feleslegessé a gyártási ellenőrzést.')]:
 txt(55,y,a,12,True);y=wrap(290,y,b,830,12)-27
c.showPage()
# Existing per-part drawing layout, now populated from the complete R14 model.
tail='# Part sheets:'+src.split('# Part sheets:')[1]
tail=tail.replace('R13','R14').replace('Pánt/polctartó/csap és AV funkció','Pánt/polctartó/csap/TIP-ON/léc/hátlap és AV funkció')
old_manual={r[0]:r for r in json.loads((O/'audit/R13_excel_snapshot.json').read_text())['sheets']['Darabok'][5:] if r[0]}
tail=tail.replace("'C élkód: NYITOTT'","'C élkód: '+str(old_manual.get(p['id'], ['']*16)[15] or 'NYITOTT')")
exec(compile(tail,__file__+':part_sheets','exec'))

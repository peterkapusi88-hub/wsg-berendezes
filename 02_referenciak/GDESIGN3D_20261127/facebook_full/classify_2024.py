from pathlib import Path
import json
p=Path(__file__).resolve().parent
D={
59:('lakás','nappali, konyha, előtér',['konyha','nappali','nappali_konyha','folyoso','eloter'],'Sötét dió, grafit és fekete üveg, finom rejtett fények, szobrászati kárpit.',None),
60:('lakás','nappali, folyosó',['nappali','nappali','nappali','folyoso','nappali'],'Világos taupe, kerekített fapanelek, fehér erezett kő és krémszínű kárpit.','calm'),
61:('lakás','konyha, étkező, szépítkező',['konyha','etkezo','konyha_etkezo','szepitkezo'],'A Calm nappalihoz tartozó fehér kősziget, körasztal és keskeny világított tároló.','calm'),
62:('lakóház','gardrób, háló, fürdő',['gardrob','halo','halo_media','furdo','furdo'],'Sötét dió, markáns fekete-fehér kő, füstüveg gardrób.','slender'),
63:('lakóház','garázs, wellness, szauna',['garazs','garazs','wellness','wellness','zuhany','szauna'],'Sötét dió és strukturált kő; autókiállítás és spa. Külön funkció, nem lakásba másolandó tér.','slender'),
64:('lakóház','nappali, konyha, lépcső',['nappali','nappali','nappali','lepcso','konyha','konyha'],'Kétszintes nappali, bordázott szürke kanapé, erezett kő és sötét fa.','slender'),
66:('lakóház','konyha, étkező',['etkezo','konyha','konyha','konyha'],'Bézs és bronz konyha, kontrasztos fehér kősziget.','proud'),
67:('lakóház','háló, gardrób, lépcső',['halo','halo_gardrob','gardrob','halo_kad','lepcso'],'Rozsdabarna ágy, sötétfa gardrób, sziklaszerű kőfal, motoros lépcsőtér.',None),
68:('lakóház','nappali, étkező',['nappali','nappali','nappali','etkezo'],'Világos széles kanapé, taupe faburkolat, fekete-fehér kő és hullámos függőlámpa.',None),
70:('lakóház','előszoba, folyosó',['eloter','folyoso','eloter'],'Karcsú kapszula alakú világító tükrök és dióhatású gardrób.',None),
73:('lakás','fürdő',['furdo_mosdo','furdo_kad','furdo'],'Bézs travertinhatás, sötét bordázott mosdóbútor és széles megvilágított tükör.',None),
74:('lakóház','nappali',['nappali','nappali','nappali'],'Lágy taupe moduláris ülőbútorok, világos kanapé, vékony vonallámpás csillár.',None),
75:('lakóház','nappali TV-fal',['nappali_tv','nappali','nappali_tv','nappali'],'Bronz panel, világított texturált kőkeret, szobrászati fotel.','proud'),
76:('lakóház','lépcső',['lepcso','lepcso'],'Világos kőlépcső, sötét fa és visszafogott alsó világítás.',None),
77:('lakóház','előszoba',['eloter','eloter','eloter'],'Taupe falpanel, keskeny konzol, világos kőbetét és ülőpuff.',None),
78:('lakóház','fürdő',['furdo_kad','furdo_mosdo','furdo','furdo_zuhany'],'Fehér-barnán erezett brecciahatású kő, függőleges tükrök, bézs kád.','proud'),
79:('lakás','háló, szépítkező',['szepitkezo','halo','halo','halo','halo_szepitkezo'],'Világos szürke kárpit, füstszínű panelek, nagy köralakú világító tükör.',None),
81:('lakóház','fürdő',['furdo_mosdo','furdo_reszlet','furdo_zuhany'],'Szélesen erezett bézs-fehér kő, dupla köralakú tükör.','proud'),
83:('lakóház','háló',['halo_fejveg','halo','halo','halo','halo_media'],'Bronz paneles, texturált kőbetétes fejvég és meleg rétegzett világítás.','proud'),
84:('kültér','villa, kert, medence',['kulter_villa','kulter_medence','kulter_villa'],'Teraszos villa és kültéri medence. Archiválva, külön kezelendő, nem beltéri stílus.',None),
86:('lakóház','bab aszoba',['babaszoba','babaszoba','babaszoba'],'Taupe és olíva fiókfrontok, lágy organikus világítás, tetőtéri babaszoba.',None),
87:('lakóház','háló, gardrób',['halo','gardrob','halo_gardrob','gardrob','szepitkezo'],'Sötét tetőtéri háló, fekete textúrák, bronz/füstölt üveg, cipős vitrinek.',None),
88:('lakóház','fürdő, WC',['furdo_mosdo','furdo','furdo_kad','wc'],'Sötét kőhatás, világos szabadonálló kád, köralakú tükrök és rejtett világítás.',None),
89:('lakóház','nappali, konyha',['konyha_etkezo','nappali','nappali_konyha','konyha'],'Grafit konyha, sötét kősziget, bronzos vitrinfal és mélyszürke kárpit.',None),
90:('lakóház','fürdő',['furdo_mosdo','furdo_kad','furdo','furdo'],'Sötét dió, bézs kő, világos szabadonálló kád, gömblámpák.','confident'),
91:('lakóház','fürdő',['furdo_mosdo','furdo_kad','furdo','furdo_zuhany'],'Dió és karakteres barnás kő, fehér erezett zuhanyfal, széles megvilágított tükör.','confident'),
92:('lakóház','háló, gardrób',['gardrob','halo','halo','halo_media','halo_media'],'Lekerekített végű üveges gardrób, bronzbarna falpanelek, kőbetétes ágyfal.','confident'),
93:('lakóház','nappali, étkező, előtér',['etkezo','nappali','nappali','nappali_konyha','lepcso','eloter','bar'],'Alacsony krém kanapé, sötét dió és durva kőfelület, íves függőlámpa.','confident'),
94:('lakóház','háló, fürdő, gyerekszoba',['halo','folyoso','furdo_mosdo','furdo_zuhany','gyerekszoba_dolgozo','gyerekszoba'],'Kékes ágyfal és dolgozórészletek, dió és világos kő; több helyiség egy csomagban.',None),
95:('lakóház','konyha, étkező, előtér',['etkezo','konyha_etkezo','eloter_lepcso','etkezo','konyha','konyha'],'Világos fa, fehér erezett kő, kék étkező- és bárszékek, függőleges fekete fényrudak.',None),
96:('lakóház','háló, szépítkező',['halo_media','szepitkezo','halo_media','halo'],'Mélyzöld/fekete panelek, lágy szögletes fényvonalak és fehér erezett kő.','handsome'),
97:('lakóház','bár, garázs, mozi',['bar_mozi','garazs','bar','mozi','bar'],'Sötét dió és bronz, vörös mozifotelek, megvilágított üvegpolcos bár. Külön funkció.','handsome'),
98:('lakóház','konyha, étkező, előtér',['eloter_lepcso','konyha','konyha_etkezo','eloter','konyha','etkezo'],'Dió és bronz, fehér márványhatású sziget, lekerekített kárpitozott bárszékek.','handsome'),
99:('lakóház','fürdő, mosókonyha',['furdo_mosdo','furdo','furdo_kad','furdo_kad','mosokonyha'],'Kapszula alakú tükrök, fehér márványhatás, rézszínű kád és diópanelek.','handsome')}
rows=[]
for n,(category,rooms,tags,desc,match) in D.items():
 id=f'GD{n:03}';d=p/id;m=json.loads((d/'MANIFEST.json').read_text());assert len(tags)==len(m['images'])
 for im,tag in zip(m['images'],tags): im['room_type_visual']=tag
 c={'id':id,'category_visual':category,'rooms_hu':rooms.replace('bab aszoba','babaszoba'),'character_hu':desc,'official_portfolio_visual_match':match,'match_basis':'Same rendered scene visibly present in official portfolio; project label inferred from visual match, not FBcaption.' if match else 'No confirmed official portfolio match.'}
 m['classification']=c;(d/'MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2));rows.append(c)
result={'year':2024,'albums':34,'images':150,'full_cycles':34,'failures_remaining':0,'scope':'All nonempty album_id records GD059–GD099 in parent ALBUM_INDEX.tsv; 7 non-photo records handled by parent.','classification_method':'Visual review of every downloaded image on labeled contact sheets; exact source material SKUs are not inferred.','items':rows}
(p/'2024_CLASSIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('34album150imageclassified;allmanifestsstable')

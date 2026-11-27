from pathlib import Path
from PIL import Image,ImageDraw
import json,math,csv
p=Path(__file__).resolve().parent
idx=[r for r in csv.DictReader((p/'ALBUM_INDEX.tsv').open(),delimiter='\t') if r['date'].startswith('2024') and r['album_id']]
for start in range(0,len(idx),6):
 batch=idx[start:start+6];sheet=Image.new('RGB',(1440,260*len(batch)),(245,242,235));dr=ImageDraw.Draw(sheet)
 for y,r in enumerate(batch):
  d=p/r['id'];m=json.loads((d/'MANIFEST.json').read_text());dr.text((8,y*260+4),r['id']+' '+r['date']+' '+str(m['downloaded_count'])+' images',fill='black')
  for i,row in enumerate(m['images']):
   im=Image.open(row['path']).convert('RGB');im.thumbnail((195,215));sheet.paste(im,(i*205,y*260+23));dr.text((i*205,y*260+240),str(i+1),fill='black')
 sheet.save(p/('2024_CONTACT_'+str(start//6+1)+'.jpg'),quality=88)
print('sheets',math.ceil(len(idx)/6),'albums',len(idx))

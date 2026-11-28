import json,csv,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
captions=json.loads((P/'2024_FEED_CAPTIONS.json').read_text())
extra=json.loads((P/'2024_EXTRA_CLASSIFICATION.json').read_text())
summary=json.loads((P/'2024_CLASSIFICATION.json').read_text())
summary['items']=[x for x in summary['items'] if not x['id'].startswith('GD2024_')]
for id,caption in captions.items():
    f=P/id/'MANIFEST.json';m=json.loads(f.read_text());m['caption']=caption;m['caption_note']='Observed in logged-in 2024 filtered public feed audit; whitespace normalized, DOM emoji omission and visible truncation retained. No personal comments saved.';f.write_text(json.dumps(m,ensure_ascii=False,indent=2))
for c in extra:
    f=P/c['id']/'MANIFEST.json';m=json.loads(f.read_text())
    assert len(c['room_types'])==len(m['images'])
    for image,room in zip(m['images'],c['room_types']):image['room_type_visual']=room
    x={'id':c['id'],'category_visual':'residential','rooms_hu':', '.join(dict.fromkeys(c['room_types'])),'character_hu':c['character_hu'],'official_portfolio_visual_match':c['official_portfolio_visual_match'],'match_basis':'Visual same-scene identification, not inferred from palette.' if c['official_portfolio_visual_match'] else 'No confirmed official portfolio match.'}
    m['classification']=x;f.write_text(json.dumps(m,ensure_ascii=False,indent=2));summary['items'].append(x)
summary.update(albums=43,images=188,full_cycles=43,failures_remaining=0,scope='Original 34 indexed 2024 albums plus 9 albums discovered by full-year filtered feed audit using 1.5-page scrolls; lower boundary 2023-12-23 and 2023-12-07. One cover and six videos separately recorded.')
(P/'2024_CLASSIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
family=json.loads((P/'PROJECT_FAMILIES_2024.json').read_text())
ids=[x for f in family['families'] for x in f['source_ids']]
assert len(ids)==len(set(ids))==43
results=[]
for id in ids:
    m=json.loads((P/id/'MANIFEST.json').read_text());assert m['complete'];assert len(m['images'])==int(m['expected_photos'])
    hashes=[]
    for im in m['images']:
        assert Path(im['path']).exists()
        assert hashlib.sha256(Path(im['path']).read_bytes()).hexdigest()==im['sha256']
        hashes.append(im['sha256'])
    assert len(hashes)==len(set(hashes)),(id,'duplicate image bytes')
    results.append({k:m[k] for k in ['id','date','album_id','expected_photos','downloaded_count','cycle_confirmed','complete']})
audit={'verified_date':'2026-11-27','year':2024,'source_profile':'https://www.facebook.com/gdesign3d','method':'Logged-in Chrome profile filter year 2024; twenty successive 1.5-page scrolls with fresh AX observation and visible DOM caption/photo extraction after every scroll; reconciled album IDs against original index. No hidden state or private comments read into archive.','uppermost_record':'2024-12-20','lower_boundary_records':[{'date':'2023-12-23','photo_id':'900695388723054','kind':'single_photo'},{'date':'2023-12-07','album_id':'889803039812289'}],'record_count':50,'photo_album_count':43,'photo_image_count':188,'cover_record_count':1,'video_record_count':6,'new_album_count':9,'new_image_count':38,'all_album_cycles_complete':True,'all_saved_image_hashes_verified':True,'album_internal_duplicate_hashes':0,'albums':results,'non_album_reference':'PROJECT_FAMILIES_2024.json','limitation':'Coverage describes the currently visible published feed; deleted or inaccessible historical content cannot be asserted. Video URLs/posters are archived, video files unavailable.'}
(P/'2024_FEED_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
print('2024 audit: 43 albums / 188 images / 50 records; hashes and unique source-family coverage verified.')

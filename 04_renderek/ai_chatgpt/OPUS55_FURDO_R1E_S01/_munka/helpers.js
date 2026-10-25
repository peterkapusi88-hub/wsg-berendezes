window.opusSuffix='__FURDO_R1C__';
window.opusEd=()=>[...document.querySelectorAll('div.ProseMirror')].find(e=>e.offsetParent);
window.opusNew=()=>{let i=document.getElementById('opus-src'); if(!i){i=document.createElement('input');i.type='file';i.multiple=true;i.id='opus-src';i.setAttribute('aria-label','OPUS-SRC forrasfajlok');i.style.cssText='position:fixed;left:0;top:0;width:40px;height:20px;opacity:0.01;z-index:99999';document.body.appendChild(i);} i.value=''; return 'ok'};
window.opusName=(fn)=>{const m=fn.match(/^\d+_(.+?)(?:__(v\d+))?\.txt$/); return m[1]+window.opusSuffix+(m[2]||'v1')+'.png'};
window.opusImgTiles=()=>{const f=opusEd().closest('form')||document;return [...f.querySelectorAll('img')].filter(e=>e.offsetParent).map(e=>e.alt.replace(/\([\d-]+\)(\.\w+)$/,'$1'))};
window.opusWatch=(NAME,sent)=>{const st={NAME,state:'sent',sent}; window.__opus=st; const seen=new Set([...document.querySelectorAll('img')].map(i=>i.src)); let last='',same=0,t0=Date.now();
 const iv=setInterval(async()=>{try{
  if(st.state!=='sent'){clearInterval(iv);return}
  if(Date.now()-t0>9*60e3){st.state='timeout';clearInterval(iv);return}
  const txt=document.querySelector('main')?.innerText||'';
  if(/Képgenerálás sikertelen|nem sikerült létrehozni/i.test(txt)) st.fail=true;
  const cand=[...document.querySelectorAll('main img')].filter(i=>i.offsetParent&&!seen.has(i.src)&&!/csatolm/i.test(i.alt)&&!i.closest('form')&&i.naturalWidth>=1000&&i.complete);
  const stop=document.querySelector('[data-testid="stop-button"],button[aria-label*="Leállítás"],button[aria-label*="leállítása"],button[aria-label*="Stop"]');
  st.cands=cand.map(i=>i.alt+'|'+i.naturalWidth+'x'+i.naturalHeight); st.stop=!!stop;
  if(!cand.length){ if(st.fail&&!stop){st.state='failed';clearInterval(iv)} return}
  const im=cand[cand.length-1]; const key=im.src+im.naturalWidth;
  if(key===last&&!stop){same++}else{same=0;last=key}
  if(same>=3){st.state='downloading';clearInterval(iv);
    const r=await fetch(im.src,{credentials:'include'}); const b=await r.blob(); st.type=b.type; st.size=b.size; st.w=im.naturalWidth; st.h=im.naturalHeight; st.alt=im.alt; st.ncand=cand.length;
    const a=document.createElement('a'); a.href=URL.createObjectURL(b); a.download=NAME; document.body.appendChild(a); a.click(); a.remove(); st.state='downloaded'}
 }catch(e){st.err=String(e)}},3000)};
window.opusSend=async(NAME,msg)=>{const ed=opusEd(); ed.focus(); const sel=window.getSelection(); sel.selectAllChildren(ed); sel.collapseToEnd();
 document.execCommand('insertText',false,msg); await new Promise(r=>setTimeout(r,1500));
 const norm=s=>s.replace(/\s+/g,' ').trim(); const ok=norm(ed.innerText).endsWith(norm(msg)); const extra=ed.innerText.length-msg.length;
 if(!ok) return {ok:false,why:'text mismatch',extra,head:ed.innerText.slice(0,80)};
 const btn=document.querySelector('form button[aria-label="Küldés"],[data-testid="send-button"]'); if(!btn||btn.disabled) return {ok:false,why:'no send btn'};
 btn.click(); const sent=new Date().toISOString(); opusWatch(NAME,sent); return {ok:true,NAME,extra,sent}};
window.opusRun=async()=>{const fs=[...document.getElementById('opus-src').files]; const txt=fs.find(f=>f.name.endsWith('.txt')); const imgs=fs.filter(f=>!f.name.endsWith('.txt'));
 const NAME=opusName(txt.name); const msg=(await txt.text()).replace(/\n+$/,'');
 if(opusImgTiles().length===0){const ed=opusEd(); ed.focus(); const dt=new DataTransfer(); imgs.forEach(f=>dt.items.add(f)); ed.dispatchEvent(new ClipboardEvent('paste',{clipboardData:dt,bubbles:true,cancelable:true}));}
 for(let k=0;k<20&&opusImgTiles().length<imgs.length;k++) await new Promise(r=>setTimeout(r,500));
 const busyN=()=>[...(opusEd().closest('form')).querySelectorAll('[role="progressbar"],svg circle[stroke-dasharray]')].length;
 let waited=0; await new Promise(r=>setTimeout(r,2500)); while(busyN()>0&&waited<30){await new Promise(r=>setTimeout(r,1000));waited++}
 const tiles=opusImgTiles(); const want=imgs.map(f=>f.name); if(JSON.stringify(tiles)!==JSON.stringify(want)) return {ok:false,why:'tile order',tiles,want};
 const r=await opusSend(NAME,msg); r.tiles=tiles; r.busyAtSend=busyN(); r.waited=waited; return r};
'helpers ok'

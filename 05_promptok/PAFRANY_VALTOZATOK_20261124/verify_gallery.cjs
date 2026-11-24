const {chromium}=require('/Users/peterkapusi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path=require('path'),fs=require('fs');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const root=__dirname, page=await browser.newPage();const results=[];
 for(const [name,width,height] of [['desktop',1440,1050],['mobile',390,844]]){
  await page.setViewportSize({width,height});await page.goto('file://'+path.join(root,'00_KEPES_ATTEKINTO.html'));
  await page.evaluate(async()=>{for(const im of document.images){im.loading='eager';await im.decode().catch(()=>{});}});
  const state=await page.evaluate(()=>({title:document.title,imageCount:document.images.length,brokenImages:[...document.images].filter(x=>!x.naturalWidth).map(x=>x.src),overflow:document.documentElement.scrollWidth>innerWidth,articles:document.querySelectorAll('article').length,links:[...document.querySelectorAll('a[href]')].map(a=>a.href)}));
  const missing=state.links.filter(x=>x.startsWith('file:')&&!x.includes('#')).filter(x=>!fs.existsSync(decodeURIComponent(new URL(x).pathname)));
  const invalidAnchors=await page.evaluate(()=>[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.getAttribute('href').slice(1))).map(a=>a.href));
  delete state.links;results.push({viewport:name,...state,missing,invalidAnchors});
  await page.screenshot({path:'/private/tmp/pafrany-'+name+'.png'});
 }
 fs.writeFileSync(path.join(root,'92_GALLERY_QA.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});

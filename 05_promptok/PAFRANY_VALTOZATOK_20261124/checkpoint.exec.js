
const repo="peterkapusi88-hub/wsg-berendezes", branch="competition/s18-lake-forest-plus-20261123";
const get=async url=>JSON.parse((await tools.mcp__codex_apps__github_fetch({url})).structuredContent.content);
const head=(await get("https://api.github.com/repos/"+repo+"/git/ref/heads/"+branch)).object.sha;
const base=(await get("https://api.github.com/repos/"+repo+"/git/commits/"+head)).tree.sha;
const remote=await get("https://api.github.com/repos/"+repo+"/git/trees/"+base+"?recursive=1");
const map=new Map(remote.tree.map(x=>[x.path,x.sha]));
const f=await tools.exec_command({cmd:"python3 - <<'PY'\nimport pathlib,json,hashlib\np=pathlib.Path('05_promptok/PAFRANY_VALTOZATOK_20261124');print(json.dumps([{'path':str(f),'size':f.stat().st_size,'sha':hashlib.sha1(b'blob '+str(f.stat().st_size).encode()+b'\\0'+f.read_bytes()).hexdigest()} for f in sorted(p.rglob('*')) if f.is_file() and '__pycache__' not in str(f)]))\nPY",max_output_tokens:25000});
const files=JSON.parse(f.output),changed=files.filter(x=>map.get(x.path)!==x.sha), entries=[];
const q=s=>"'"+s.replace(/'/g,"'\\''")+"'";
let tree=base;
for(const file of changed){
 if(file.path.endsWith('.png')){
  let b64="";
  for(let offset=0;offset<file.size;offset+=300000){
   const r=await tools.exec_command({cmd:"python3 -c "+q("import pathlib,base64;print(base64.b64encode(pathlib.Path("+JSON.stringify(file.path)+").read_bytes()["+offset+":"+Math.min(offset+300000,file.size)+"]).decode())"),max_output_tokens:200000});
   b64+=r.output.trim();
  }
  const r=await tools.mcp__codex_apps__github_create_blob({repository_full_name:repo,encoding:"base64",content:b64});
  if(r.structuredContent?.sha!==file.sha)throw Error("Upload SHA mismatch "+file.path+" "+JSON.stringify(r).slice(0,400));
  entries.push({path:file.path,mode:"100644",type:"blob",sha:file.sha});notify("GitHub-kép mentve: "+file.path.split('/').pop());
 }else{
  const r=await tools.exec_command({cmd:"cat "+q(file.path),max_output_tokens:150000});
  entries.push({path:file.path,mode:"100644",type:"blob",content:r.output});
 }
}
for(let i=0;i<entries.length;i+=20){
 const r=await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:tree,tree_elements:entries.slice(i,i+20)});
 if(!r.structuredContent?.sha)throw Error(JSON.stringify(r));tree=r.structuredContent.sha;
}
const commit=(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:head,tree_sha:tree,message:"Páfrány checkpoint: saved generated concepts, reference links and full pending camera queue"})).structuredContent.sha;
const u=await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:branch,expected_sha:head,sha:commit});if(!u.structuredContent?.success)throw Error("Ref not updated");
const verify=await get("https://api.github.com/repos/"+repo+"/git/trees/"+tree+"?recursive=1"),vm=new Map(verify.tree.map(x=>[x.path,x.sha]));
const bad=files.filter(x=>vm.get(x.path)!==x.sha);if(bad.length)throw Error("Remote differs "+JSON.stringify(bad.map(x=>x.path)));
store('pfLatestCommit',commit);text({commit,verified_files:files.length,changed:changed.length});
await tools.exec_command({cmd:"python3 - <<'PY'\nimport json,pathlib\np=pathlib.Path('05_promptok/PAFRANY_VALTOZATOK_20261124/90_CHECKPOINTS.json');d=json.loads(p.read_text());d.append({'commit':'"+commit+"','status':'ALL_FILE_GIT_SHA_VERIFIED','files':"+files.length+"});p.write_text(json.dumps(d,indent=2))\nPY",max_output_tokens:1000});


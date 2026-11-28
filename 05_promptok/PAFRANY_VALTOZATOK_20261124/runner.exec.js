const rr=await tools.exec_command({cmd:"python3 '05_promptok/PAFRANY_VALTOZATOK_20261124/select_jobs.py'",max_output_tokens:30000});
const jobs=JSON.parse(rr.output);
const results=await Promise.allSettled(jobs.map(async j=>({j,r:await tools.image_gen__imagegen({prompt:j.prompt_text,referenced_image_paths:j.inputs,transparent_background:false})})));
for(const entry of results){
 if(entry.status!=="fulfilled"){text({error:String(entry.reason)});continue;}
 const {j,r}=entry.value,src=r.output_hint?.match(/as (\/.*?\.png) by default/)?.[1];if(!src)throw Error("No result path "+j.id);
 const q=s=>"'"+s.replace(/'/g,"'\\''")+"'";
 const save=await tools.exec_command({cmd:"python3 '05_promptok/PAFRANY_VALTOZATOK_20261124/save_result.py' "+q(j.id)+" "+q(src),max_output_tokens:1000});
 const meta=JSON.stringify({id:j.id,actual_inputs:j.inputs,actual_prompt:j.prompt_text,source:src});
 await tools.apply_patch("*** Begin Patch\n*** Add File: 05_promptok/PAFRANY_VALTOZATOK_20261124/renders/"+j.id+".execution.json\n+"+meta+"\n*** End Patch");
 generatedImage(r);text(save.output);
}

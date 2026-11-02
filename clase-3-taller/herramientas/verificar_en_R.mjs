import { pathToFileURL, fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
const { WebR } = await import(process.env.WEBR_MODULE ? pathToFileURL(process.env.WEBR_MODULE).href : 'webr');
import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const webR=new WebR();await webR.init();
await webR.FS.mkdir('/work');await webR.FS.mkdir('/work/datos');
for(const file of ['wage1.csv','wage2.csv'])await webR.FS.writeFile('/work/datos/'+file,await fs.readFile(path.join(root,'datos',file)));
await webR.evalRVoid('setwd("/work");pdf("verificacion-graficos.pdf", width=8, height=5)');
const content=JSON.parse(await fs.readFile(path.join(root,'contenido-clase-3.json'),'utf8'));
const outputs={};
for(const a of content.bloques.flatMap(b=>b.laminas)){
 console.log('Ejecutando',a.id);
 if(a.codigo_inicial)await webR.evalRVoid(a.codigo_inicial);
 outputs[a.id]=await webR.evalRString(`paste(capture.output({${a.codigo}\n}),collapse="\\n")`);
 for (const item of a.explicaciones||[]) {
  if(item.length>2)await webR.evalRVoid('eval(parse(text='+JSON.stringify(item[2])+'), envir=new.env(parent=as.environment("package:stats")))');
 }
 if(a.reto_codigo)await webR.evalRVoid('eval(parse(text='+JSON.stringify(a.reto_codigo)+'), envir=new.env(parent=as.environment("package:stats")))');
 if(['C3-02','C3-03','C3-04','C3-05','C3-06','C3-07'].includes(a.id)) {
  await webR.evalRVoid('eval(parse(text='+JSON.stringify(a.codigo)+'), envir=new.env(parent=as.environment("package:stats")))');
 }

}
await webR.evalRVoid(`
stopifnot(nrow(salarios)==526,nrow(trabajo)==935,ATE==17,ATT==20,brecha==50,seleccion==30)
stopifnot(isTRUE(all.equal(b_corta,b1_mas_b2_delta <- unname(coef(larga)["x1"] + coef(larga)["x2"] * coef(auxiliar)["x1"]))))
stopifnot(coef(sin_edad)["fumar"]<0,coef(con_edad)["fumar"]>0)
stopifnot(sd(pendientes[,2])>sd(pendientes[,1]))
stopifnot(coef(modelo_corto)["educ"]>coef(modelo_control)["educ"])
write.csv(personas,"personas.csv",row.names=FALSE)
write.csv(data.frame(habilidad,Y_NT,Y_T,T_auto,T_azar,Y_auto,Y_azar),"asignacion.csv",row.names=FALSE)
write.csv(data.frame(estimacion=estimaciones),"sorteos.csv",row.names=FALSE)
write.csv(data.frame(x1,v,u,x2=sim_ov$x2,y=sim_ov$y),"omision.csv",row.names=FALSE)
write.csv(casos,"signos.csv",row.names=FALSE)
write.csv(fumar_datos,"fumar.csv",row.names=FALSE)
write.csv(pendientes,"irrelevantes.csv",row.names=FALSE)
write.csv(trabajo,"trabajo.csv",row.names=FALSE)
dev.off()
`);
const data={};
for(const name of ['personas','asignacion','sorteos','omision','signos','fumar','irrelevantes','trabajo']){
 const csv=new TextDecoder().decode(await webR.FS.readFile('/work/'+name+'.csv'));
 const lines=csv.trim().split('\n');const keys=lines.shift().split(',').map(x=>x.replace(/^"|"$/g,''));
 data[name]=lines.map(row=>Object.fromEntries(row.split(',').map((v,i)=>[keys[i],isNaN(Number(v))?v.replace(/^"|"$/g,''):Number(v)])));
}
data.salarios=await webR.evalRString('paste(capture.output(write.csv(salarios[,c("wage","educ")],row.names=FALSE)),collapse="\\n")');
const sl=data.salarios.trim().split('\n');sl.shift();data.salarios=sl.map(row=>{const [wage,educ]=row.split(',').map(Number);return {wage,educ};});
await fs.writeFile(path.join(root,'datos/resultados-interactivos.json'),JSON.stringify(data));
await fs.writeFile(path.join(root,'datos/salidas-verificadas-r.json'),JSON.stringify(outputs,null,2)+'\n');
// Los gráficos se generan en el sistema de archivos temporal de R durante esta comprobación.
const acts=content.bloques.flatMap(b=>b.laminas);
const code=acts.map(a=>a.id+'\n'+(a.codigo_inicial||'')+'\n'+a.codigo+'\n'+(a.reto_codigo||'')+'\n'+(a.explicaciones||[]).filter(x=>x.length>2).map(x=>x[2]).join('\n')).join('\n\n');
await fs.writeFile(path.join(root,'datos/verificacion.json'),JSON.stringify({codigo_sha256:createHash('sha256').update(code).digest('hex'),motor:'webR 0.6.0',ejemplos_ejecutados:acts.length},null,2)+'\n');
console.log('Todos los ejemplos R ejecutados y comprobados.');
await webR.close();

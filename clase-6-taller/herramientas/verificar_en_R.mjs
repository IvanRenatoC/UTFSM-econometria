import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const {WebR}=await import(process.env.WEBR_MODULE ? pathToFileURL(process.env.WEBR_MODULE).href : 'webr');
const content=JSON.parse(await fs.readFile(path.join(root,'contenido-clase-6.json'),'utf8'));
const r=new WebR();
await r.init();
await r.installPackages(["wooldridge"]);
try {
 await r.FS.mkdir('/work'); await r.FS.mkdir('/work/datos');
 await r.FS.writeFile('/work/datos/wage1.csv',await fs.readFile(path.join(root,'datos/wage1.csv')));
 await r.evalRVoid('setwd("/work"); pdf("graficos.pdf", width=9, height=5)');
 const outputs={};
 for(const a of content.laminas){
  console.log('Verificando',a.id);
  outputs[a.id]={
   ejemplo:await r.evalRString('paste(capture.output({'+a.codigo+'\n}),collapse="\n")'),
   solucion:await r.evalRString('paste(capture.output({'+a.solucion+'\n}),collapse="\n")')
  };
 }
 await r.evalRVoid(`
 stopifnot(nrow(datos)==526, nrow(datos_log)==524)
 stopifnot(all.equal(fitted(modelo_pesos)/1000,fitted(modelo_nivel))==TRUE)
 stopifnot(all.equal(fitted(modelo_meses),fitted(modelo_nivel))==TRUE)
 stopifnot(all.equal(unname(coef(modelo_tenure_meses)[2]*12),unname(bt))==TRUE)
 stopifnot(all.equal(unname(p[2]-p[1]),unname(bi["educ"]+bi["educ:exper"]*35))==TRUE)

 modelo_I <- lm(wage ~ exper + I(exper^2), data=datos)
 stopifnot(isTRUE(all.equal(fitted(modelo_I), fitted(modelo_cuad))))
 write.csv(datos[,c("wage","educ","exper")],"puntos.csv",row.names=FALSE)
 write.csv(data.frame(x=6:18,y=predict(modelo_log,newdata=data.frame(educ=6:18))),"lognivel.csv",row.names=FALSE)
 elog <- seq(log(min(datos_log$educ)), log(max(datos_log$educ)), length.out=100)
 write.csv(data.frame(x=elog,y=predict(modelo_log_log,newdata=data.frame(educ=exp(elog)))),"loglog.csv",row.names=FALSE)

 edu <- seq(6,18,length.out=100)
 write.csv(data.frame(x=edu,y=exp(predict(modelo_log,newdata=data.frame(educ=edu)))),"log.csv",row.names=FALSE)
 ex <- seq(min(datos$exper),max(datos$exper),length.out=100)
 write.csv(data.frame(x=ex,y=predict(modelo_cuad,newdata=data.frame(exper=ex,exper2=ex^2))),"cuad.csv",row.names=FALSE)
 for(e in c(5,20,35)) {
  write.csv(data.frame(x=edu,y=predict(modelo_int,newdata=data.frame(educ=edu,exper=e))),
            paste0("int",e,".csv"),row.names=FALSE)
 }
 write.csv(data.frame(x=edu,y=predict(modelo_nivel,newdata=data.frame(educ=edu))),"nivel.csv",row.names=FALSE)
 dev.off()
 `);
 const graphs={};
 for(const name of ['puntos','log','cuad','int5','int20','int35','nivel','lognivel','loglog']){
  const lines=new TextDecoder().decode(await r.FS.readFile('/work/'+name+'.csv')).trim().split('\n');
  const keys=lines.shift().split(',').map(x=>x.replaceAll('"',''));
  graphs[name]=lines.map(line=>Object.fromEntries(line.split(',').map((v,i)=>[keys[i],Number(v)])));
 }
 await fs.writeFile(path.join(root,'datos/resultados-interactivos.json'),JSON.stringify(graphs)+'\n');
 await fs.writeFile(path.join(root,'datos/salidas-verificadas-r.json'),JSON.stringify(outputs,null,2)+'\n');
 await fs.writeFile(path.join(root,'datos/verificacion.json'),JSON.stringify({
  codigo_sha256:createHash('sha256').update(JSON.stringify(content)).digest('hex'),
  ejemplos:9,soluciones:9,motor:'webR',pruebas:['526 personas con salarios positivos','524 personas con educación positiva','Predicciones invariantes al reescalar','Pendiente por mes igual a pendiente anual / 12','Interacción igual a diferencia predicha']
 },null,2)+'\n');
} finally { await r.close(); }

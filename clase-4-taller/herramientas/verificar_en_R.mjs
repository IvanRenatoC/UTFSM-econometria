import {pathToFileURL,fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import fs from 'node:fs/promises';
import path from 'node:path';
const {WebR}=await import(process.env.WEBR_MODULE?pathToFileURL(process.env.WEBR_MODULE).href:'webr');
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const content=JSON.parse(await fs.readFile(path.join(root,'contenido-clase-4.json'),'utf8'));
const r=new WebR();await r.init();await r.FS.mkdir('/work');await r.FS.mkdir('/work/datos');
await r.FS.writeFile('/work/datos/wage2.csv',await fs.readFile(path.join(root,'datos/wage2.csv')));
await r.evalRVoid('setwd("/work");pdf("graficos.pdf",width=8,height=5)');
const outputs={};
for(const a of content.laminas){console.log('Ejecutando',a.id);outputs[a.id]=await r.evalRString(`paste(capture.output({${a.codigo}\n}),collapse="\\n")`);}
await r.evalRVoid(`
stopifnot(nrow(datos)==935,all(complete.cases(datos)))
stopifnot(isTRUE(all.equal(as.numeric(beta_sistema),unname(coef(modelo5)))))
stopifnot(max(abs(t(X)%*%u_hat))<1e-6, abs(mean(y)-mean(y_ajustado))<1e-7)
stopifnot(abs(determinante-34276)<1e-5, max(abs(A%*%inversa-diag(3)))<1e-7)
stopifnot(all(diff(trayectoria$R2)> -1e-12))
write.csv(data.frame(datos),"wage.csv",row.names=FALSE)
write.csv(data.frame(ejemplo[,1:4],predicho=fitted(modelo5),residuo=resid(modelo5)),"cinco.csv",row.names=FALSE)
write.csv(trayectoria,"ruido.csv",row.names=FALSE)
write.csv(data.frame(modelo=c("simple","multiple"),b0=c(coef(simple)[1],coef(multiple)[1]),b1=c(coef(simple)[2],coef(multiple)[2]),b2=c(0,coef(multiple)[3]),R2=c(summary(simple)$r.squared,summary(multiple)$r.squared),R2aj=c(summary(simple)$adj.r.squared,summary(multiple)$adj.r.squared)),"modelos.csv",row.names=FALSE)
write.csv(data.frame(beta=as.numeric(coef(modelo5))),"beta5.csv",row.names=FALSE)
write.csv(data.frame(coef=rownames(summary(modelo5)$coefficients),summary(modelo5)$coefficients,check.names=FALSE),"summary.csv",row.names=FALSE)
write.csv(data.frame(fuente=rownames(anova(modelo5)),anova(modelo5),check.names=FALSE),"anova.csv",row.names=FALSE)
dev.off()
`);
const data={};
// Las tablas exportadas no contienen comas dentro de sus campos.
for(const name of ['wage','cinco','ruido','modelos','beta5','summary','anova']){
 const lines=new TextDecoder().decode(await r.FS.readFile('/work/'+name+'.csv')).trim().split('\n');
 const keys=lines.shift().split(',').map(x=>x.replace(/^"|"$/g,''));
 data[name]=lines.map(l=>Object.fromEntries(l.split(',').map((v,i)=>[keys[i],v==='NA'?null:isNaN(Number(v))?v.replace(/^"|"$/g,''):Number(v)])));
}
await fs.writeFile(path.join(root,'datos/resultados-interactivos.json'),JSON.stringify(data)+'\n');
await fs.writeFile(path.join(root,'datos/salidas-verificadas-r.json'),JSON.stringify(outputs,null,2)+'\n');
await fs.writeFile(path.join(root,'datos/verificacion.json'),JSON.stringify({codigo_sha256:createHash('sha256').update(content.laminas.map(a=>a.id+'\n'+a.codigo).join('\n\n')).digest('hex'),ejemplos_ejecutados:content.laminas.length,motor:'webR 0.6.0',pruebas:['Muestra común de 935 observaciones','lm coincide con cálculo matricial','Ortogonalidad de residuos','Determinante 34276','Inversa por cofactores e identidad','R² no decrece en modelos anidados']},null,2)+'\n');
await r.close();console.log('Todos los ejemplos y comprobaciones pasaron.');

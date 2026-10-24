(() => {
const D = window.datosTaller;
const cases = {positive:['educ','wage','Educación (años)','Salario (USD/h de 1976)'],negative:['exper','educ','Experiencia potencial (años)','Educación (años)'],flat:['numdep','wage','Número de dependientes','Salario (USD/h de 1976)']};
const fit = (x,y) => {let mx=x.reduce((a,b)=>a+b)/x.length,my=y.reduce((a,b)=>a+b)/y.length;let b=x.reduce((s,v,i)=>s+(v-mx)*(y[i]-my),0)/x.reduce((s,v)=>s+(v-mx)**2,0);let a=my-b*mx,sst=y.reduce((s,v)=>s+(v-my)**2,0),ssr=y.reduce((s,v,i)=>s+(v-a-b*x[i])**2,0);return {a,b,ssr,r2:1-ssr/sst,my};};
const node=(tag,attrs={})=>{const n=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,v));return n;};
document.querySelectorAll('.lab').forEach((lab,index)=>{
let kind=lab.dataset.kind,selected=['positive','negative','flat'].includes(kind)?kind:'positive',animate=0,frame=0;
lab.innerHTML='<div class="lab-controls"></div><svg viewBox="0 0 760 420" role="img"></svg><p class="lab-result" aria-live="polite"></p>';
const controls=lab.querySelector('.lab-controls'),svg=lab.querySelector('svg'),out=lab.querySelector('.lab-result');
const button=(label,fn)=>{let b=document.createElement('button');b.type='button';b.textContent=label;b.addEventListener('click',fn);controls.append(b);return b;};
let reveal=!['cases','explore-positive'].includes(kind),manual=kind==='fit';
if(['cases','variance'].includes(kind)) Object.entries({positive:'Pendiente positiva',negative:'Pendiente negativa',flat:'No significativa'}).forEach(([k,label])=>{let b=button(label,()=>{selected=k;controls.querySelectorAll('button[data-case]').forEach(t=>t.setAttribute('aria-pressed',String(t===b)));draw();});b.dataset.case=k;b.setAttribute('aria-pressed',String(k===selected));});
if(['cases','explore-positive'].includes(kind))button('Mostrar / ocultar recta',()=>{reveal=!reveal;draw();});
let intercept,slope;
if(manual){const slider=(label,min,max,step,value)=>{let l=document.createElement('label');l.textContent=label+' ';let i=document.createElement('input');i.type='range';Object.assign(i,{min,max,step,value});l.append(i);controls.append(l);i.addEventListener('input',draw);return i;};intercept=slider('Intercepto',-8,10,.000001,0);slope=slider('Pendiente',-.5,1.5,.000001,.5);button('Ajustar con MCO',()=>{let f=fit(D.map(d=>d.educ),D.map(d=>d.wage));intercept.value=f.a;slope.value=f.b;draw();});}
if(kind==='residuals')button('Animar residuos / reiniciar',()=>{cancelAnimationFrame(frame);animate=0;const start=performance.now();const tick=t=>{animate=Math.min(1,(t-start)/2400);draw();if(animate<1)frame=requestAnimationFrame(tick);};frame=requestAnimationFrame(tick);});
function draw(){svg.replaceChildren();let [xx,yy,xlabel,ylabel]=cases[selected],x=D.map(d=>d[xx]),y=D.map(d=>d[yy]),f=fit(x,y);let a=manual?+intercept.value:f.a,b=manual?+slope.value:f.b;let xmin=Math.min(...x),xmax=Math.max(...x),ymin=Math.min(0,...y),ymax=Math.max(...y)*1.06;let X=v=>65+(v-xmin)/(xmax-xmin)*655,Y=v=>350-(v-ymin)/(ymax-ymin)*305;
svg.append(node('title',{}));svg.firstChild.textContent=xlabel+' frente a '+ylabel;
const text=(str,px,py,attrs={})=>{let t=node('text',{x:px,y:py,fill:'currentColor','font-size':14,...attrs});t.textContent=str;svg.append(t);};
if(kind==='variance'){let w=650*f.r2;svg.append(node('rect',{x:65,y:130,width:w,height:65,fill:'#D6A600'}),node('rect',{x:65+w,y:130,width:650-w,height:65,fill:'#005E90'}));text('Fracción de la variación total: SST = 100 %',65,100);text('Dorado: explicada (SSE) · Azul: residual (SSR)',65,235);out.textContent=`R² = ${(100*f.r2).toFixed(2)} %. Residual = ${(100*(1-f.r2)).toFixed(2)} %. ${ylabel} es la respuesta.`;return;}
for(let i=0;i<=5;i++){let xv=xmin+(xmax-xmin)*i/5,yv=ymin+(ymax-ymin)*i/5;svg.append(node('line',{x1:65,y1:Y(yv),x2:720,y2:Y(yv),stroke:'#99a8b5','stroke-opacity':.25}));text(xv.toFixed(1),X(xv),373,{'text-anchor':'middle'});text(yv.toFixed(1),55,Y(yv)+4,{'text-anchor':'end'});}
svg.append(node('path',{d:'M65 40V350H720',fill:'none',stroke:'currentColor'}));text(xlabel,390,407,{'text-anchor':'middle'});text(ylabel,65,22);
// Clip fitted lines to the plotting region.
let defs=node('defs'),clip=node('clipPath',{id:'clip-'+index});clip.append(node('rect',{x:65,y:40,width:655,height:310}));defs.append(clip);svg.append(defs);let g=node('g',{'clip-path':`url(#clip-${index})`});svg.append(g);
x.forEach((v,i)=>{g.append(node('circle',{cx:X(v),cy:Y(y[i]),r:3.1,fill:'#005E90','fill-opacity':.4}));if(kind==='residuals'&&i<x.length*animate)g.append(node('line',{x1:X(v),x2:X(v),y1:Y(a+b*v),y2:Y(y[i]),stroke:'#D6A600','stroke-opacity':.55}));});
if(kind==='means'){let groups={};x.forEach((v,i)=>{(groups[v]??=[]).push(y[i]);});Object.entries(groups).forEach(([v,ys])=>g.append(node('circle',{cx:X(+v),cy:Y(ys.reduce((a,b)=>a+b)/ys.length),r:6,fill:'#D6A600'})));g.append(node('line',{x1:65,x2:720,y1:Y(f.my),y2:Y(f.my),stroke:'currentColor','stroke-dasharray':'5 5'}));out.textContent=`Promedio total: ${f.my.toFixed(3)} USD/h. Los puntos dorados son promedios por nivel educativo.`;return;}
if(reveal)g.append(node('line',{x1:X(xmin),x2:X(xmax),y1:Y(a+b*xmin),y2:Y(a+b*xmax),stroke:'#D6A600','stroke-width':3,class:'fitted-line'}));
let ssr=y.reduce((s,v,i)=>s+(v-a-b*x[i])**2,0);out.textContent=reveal?`ŷ = ${a.toFixed(3)} ${b<0?'−':'+'} ${Math.abs(b).toFixed(3)} x; SSR = ${ssr.toFixed(2)}${manual?'. Compara con el mínimo MCO.':`; R² = ${f.r2.toFixed(4)}`}`:'¿Qué signo anticipas? Muestra la recta después de mirar la nube.';
}
draw();
});
})();

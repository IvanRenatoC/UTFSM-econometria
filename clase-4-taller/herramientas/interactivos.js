(()=>{'use strict';
const D=window.datosC4,N='#1b2a5e',B='#005f96',G='#d6a600',R='#b93e42';
const f=(x,n=3)=>Number(x).toLocaleString('es-CL',{minimumFractionDigits:n,maximumFractionDigits:n});
const model=D.modelos[1],beta=D.beta5.map(x=>x.beta),X=D.cinco.map(p=>[1,p.experiencia,p.educacion]);
const A=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>X.reduce((s,row)=>s+row[i]*row[j],0)));
const table=(headers,rows,cls='')=>'<div class="table-wrap"><table><thead><tr>'+headers.map(h=>'<th scope="col">'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.map((r,i)=>'<tr '+(cls===String(i)?'class="selected"':'')+'>'+r.map((x,j)=>`<${j?'td':'th scope="row"'}>${x}</${j?'td':'th'}>`).join('')+'</tr>').join('')+'</tbody></table></div>';
function axes(xmin,xmax,ymin,ymax,xlabel,ylabel){const px=x=>65+(x-xmin)/(xmax-xmin)*610,py=y=>295-(y-ymin)/(ymax-ymin)*240;let body='';for(let i=0;i<=5;i++){let x=xmin+(xmax-xmin)*i/5,z=ymin+(ymax-ymin)*i/5;body+=`<line x1="65" x2="675" y1="${py(z)}" y2="${py(z)}" stroke="#dce2ea"/><text x="55" y="${py(z)+4}" text-anchor="end">${f(z,0)}</text><text x="${px(x)}" y="316" text-anchor="middle">${f(x,0)}</text>`;}body+=`<line x1="65" y1="55" x2="65" y2="295" stroke="${N}"/><line x1="65" y1="295" x2="675" y2="295" stroke="${N}"/><text x="370" y="343" text-anchor="middle">${xlabel}</text><text x="65" y="25">${ylabel}</text>`;return{px,py,body};}
function chart(body,label){return `<svg viewBox="0 0 720 355" role="img" aria-label="${label}" style="font:12px sans-serif;fill:${N}">${body}</svg>`;}
const line=(x1,y1,x2,y2,color,width=3)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}"/>`;
function controls(l,html){l.innerHTML='<div class="controls">'+html+'</div><div class="viz"></div><div class="result" role="status" aria-live="polite"></div>';return{v:l.querySelector('.viz'),r:l.querySelector('.result')};}
function btn(text,value){return `<button type="button" data-value="${value}" aria-pressed="false">${text}</button>`;}
for(const lab of document.querySelectorAll('.lab')){
 const kind=lab.dataset.kind;
 if(kind==='comparar'){
  const o=controls(lab,'');
  const simple=D.modelos[0],iq=100;
  const ax=axes(8,18,0,3100,'Educación (años)','Salario mensual (USD)');
  let b=ax.body;
  b+=D.wage.map(p=>`<circle cx="${ax.px(p.educ)}" cy="${ax.py(Math.min(p.wage,3100))}" r="2" fill="${B}" opacity=".25"><title>Educación ${p.educ}; salario ${p.wage}; IQ ${p.IQ}</title></circle>`).join('');
  b+=line(ax.px(8),ax.py(simple.b0+simple.b1*8),ax.px(18),ax.py(simple.b0+simple.b1*18),G);
  const inicio=model.b0+model.b1*8+model.b2*iq;
  const fin=model.b0+model.b1*18+model.b2*iq;
  b+=`<line x1="${ax.px(8)}" y1="${ax.py(inicio)}" x2="${ax.px(18)}" y2="${ax.py(fin)}" stroke="${R}" stroke-width="3" stroke-dasharray="8 5"/>`;
  o.r.textContent=`a) Dorada continua, solo educación. Pendiente de USD ${f(simple.b1,2)} por año. b) Roja discontinua, educación e IQ fijo en 100. Pendiente de USD ${f(model.b1,2)} por año. Ambas rectas se muestran sobre la misma nube de puntos.`;
  o.v.innerHTML=chart(b,'Salario y educación con las rectas de ambos modelos');
 }
 else if(kind==='geometria'){
  const o=controls(lab,btn('Plano de predicción (variables)',0)+btn('Proyección MCO (observaciones)',1));
  function draw(j){lab.querySelectorAll('button').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===j)));
   if(j===0){o.v.innerHTML=chart(`<polygon points="140,240 470,175 630,90 300,155" fill="#005f96" opacity=".15"/><line x1="110" y1="290" x2="650" y2="290" stroke="${N}" stroke-width="2"/><line x1="110" y1="290" x2="310" y2="95" stroke="${N}" stroke-width="2"/><line x1="110" y1="290" x2="110" y2="35" stroke="${N}" stroke-width="2"/><text x="570" y="315">Educación</text><text x="285" y="80">IQ</text><text x="120" y="45">Salario predicho</text><line x1="185" y1="215" x2="535" y2="145" stroke="${G}" stroke-width="5"/><text x="310" y="155" fill="${N}">Corte: IQ fijo</text><line x1="185" y1="215" x2="185" y2="290" stroke="${G}" stroke-dasharray="5 5"/><line x1="535" y1="145" x2="535" y2="290" stroke="${G}" stroke-dasharray="5 5"/><text x="350" y="340" text-anchor="middle">Esquema conceptual: no representa datos ni escalas numéricas.</text>`,'Plano de predicción y corte con IQ fijo');o.r.textContent='Dos regresores y una respuesta requieren tres ejes. La línea dorada es un corte del plano con IQ fijo. En la siguiente actividad veremos ese corte de frente, con educación y salario en los dos ejes.';}
   else{o.v.innerHTML=chart(`<polygon points="85,280 520,280 650,125 215,125" fill="#005f96" opacity=".2"/><text x="115" y="263">Col(X)</text><line x1="210" y1="240" x2="395" y2="55" stroke="${N}" stroke-width="3"/><text x="402" y="50">Y</text><line x1="210" y1="240" x2="395" y2="225" stroke="${B}" stroke-width="3"/><text x="400" y="247">Ŷ</text><line x1="395" y1="55" x2="395" y2="225" stroke="${G}" stroke-width="4"/><text x="407" y="135">û = Y − Ŷ</text><line x1="395" y1="55" x2="515" y2="250" stroke="${R}" stroke-width="2" stroke-dasharray="6 4"/><line x1="210" y1="240" x2="515" y2="250" stroke="${N}" stroke-width="2"/><text x="523" y="258">v</text><text x="520" y="155">Y − v</text><path d="M 395 211 L 381 212 L 381 226" fill="none" stroke="${B}" stroke-width="2"/><text x="190" y="260">0</text><text x="355" y="325" text-anchor="middle">La distancia mínima a Col(X) se alcanza en Ŷ.</text>`,'Proyección ortogonal de Y sobre el espacio de columnas de X');o.r.textContent='Y contiene las n respuestas observadas y Ŷ es su proyección sobre Col(X), el espacio generado por las columnas de X. El residuo û es perpendicular a ese espacio. Otra predicción v dentro de Col(X) queda más lejos de Y.';}
  }lab.querySelectorAll('button').forEach(b=>b.onclick=()=>draw(+b.dataset.value));draw(0);
 }
 else if(kind==='residuos'){
  const o=controls(lab,'<label>Desplazar el intercepto <input type="range" min="-200" max="200" step="10" value="0" aria-label="Cambio en el intercepto"></label>'+btn('Restablecer MCO',0));
  function draw(){const d=+lab.querySelector('input').value,ax=axes(1,5,400,1100,'Persona (orden de la tabla)','Salario del ejemplo');let b=ax.body,ss=0;
   D.cinco.forEach((p,i)=>{const v=p.predicho+d;ss+=(p.salario-v)**2;b+=`<line class="residual-line" x1="${ax.px(i+1)}" x2="${ax.px(i+1)}" y1="${ax.py(p.salario)}" y2="${ax.py(v)}" stroke="${G}" stroke-width="3"/><circle cx="${ax.px(i+1)}" cy="${ax.py(p.salario)}" r="5" fill="${B}"/><rect x="${ax.px(i+1)-4}" y="${ax.py(v)-4}" width="8" height="8" fill="${R}"/>`;});o.v.innerHTML=chart(b,'Residuos de las cinco observaciones');o.r.textContent=`Cambio en intercepto: ${d}; suma de residuos al cuadrado = ${f(ss,2)}. Puntos azules: observado; cuadrados rojos: ajustado. Manteniendo pendientes MCO, desplazar el intercepto aumenta SSR.`;}
  lab.querySelector('input').oninput=draw;lab.querySelector('button').onclick=()=>{lab.querySelector('input').value=0;draw();};draw();
 }
 else if(kind==='matriz'){
  const o=controls(lab,'<label>Persona <select aria-label="Persona del ejemplo">'+D.cinco.map((p,i)=>`<option value="${i}">${p.persona}</option>`).join('')+'</select></label>');
  function draw(){const i=+lab.querySelector('select').value,p=D.cinco[i];o.v.innerHTML=table(['Persona','Unos','Experiencia','Educación','Salario'],D.cinco.map(p=>[p.persona,1,p.experiencia,p.educacion,p.salario]),String(i));o.r.textContent=`Fila ${i+1}: [1, ${p.experiencia}, ${p.educacion}]. Predicción = ${f(beta[0])} + (${f(beta[1])}) × ${p.experiencia} + ${f(beta[2])} × ${p.educacion} = ${f(p.predicho)}. Salario observado: ${p.salario}.`;}
  lab.querySelector('select').onchange=draw;draw();
 }
 else if(kind==='producto'){
  const o=controls(lab,'<p>Selecciona una de las nueve celdas.</p>');let i=0,j=0;
  function draw(){o.v.innerHTML='<h4>A = XᵀX</h4><div class="table-wrap"><table><tbody>'+A.map((row,r)=>'<tr>'+row.map((v,c)=>`<td class="${r===i&&c===j?'selected':''}"><button type="button" aria-label="Fila ${r+1}, columna ${c+1}: ${v}" data-r="${r}" data-c="${c}">${v}</button></td>`).join('')+'</tr>').join('')+'</tbody></table></div>';
   const terms=X.map(row=>row[i]*row[j]);o.r.textContent=`Celda (${i+1},${j+1}): ${X.map(row=>row[i]+' × '+row[j]).join(' + ')} = ${terms.reduce((a,b)=>a+b,0)}. Se multiplican las columnas ${i+1} y ${j+1} de X y se suman los cinco productos.`;
   o.v.querySelectorAll('button').forEach(b=>b.onclick=()=>{i=+b.dataset.r;j=+b.dataset.c;draw();});
  }draw();
 }
 else if(kind==='anova_wage'){
  lab.innerHTML=table(['Fuente','gl','Suma de cuadrados','Cuadrado medio','F','Valor p'],D.anova_wage.map(p=>[
   p.fuente==='Residuals'?'Residuos':p.fuente,
   p.Df,f(p['Sum Sq'],2),f(p['Mean Sq'],2),
   p['F value']===null?'—':f(p['F value'],2),
   p['Pr(>F)']===null?'—':p['Pr(>F)'].toExponential(3)
  ]));
 }
}
})();

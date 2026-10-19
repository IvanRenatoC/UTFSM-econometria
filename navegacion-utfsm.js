// Navegación de clase; los cálculos y ejemplos siguen exclusivamente en R.
const searchInput=document.querySelector('#class-search');
const results=document.querySelector('#search-results');
const normalizeText=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const searchEntries=[...document.querySelectorAll('.slide')].map(slide=>({id:slide.id,title:slide.dataset.title,text:normalizeText(slide.textContent)}));
searchInput.addEventListener('input',()=>{
  results.replaceChildren();const query=normalizeText(searchInput.value.trim());
  if(!query){results.hidden=true;return;}
  const terms=query.split(/\s+/);const matches=searchEntries.filter(x=>terms.every(term=>x.text.includes(term)));
  const intro=document.createElement('p');intro.textContent=`${matches.length} lámina${matches.length===1?'':'s'} encontrada${matches.length===1?'':'s'}`;results.append(intro);
  for(const hit of matches.slice(0,20)){
    const link=document.createElement('a');link.href=`#${hit.id}`;link.textContent=hit.title;
    link.addEventListener('click',()=>{
      if(document.body.classList.contains('presenting'))document.querySelector('#present').click();
      results.hidden=true;searchInput.value='';
    });results.append(link);
  }results.hidden=false;
});
searchInput.addEventListener('keydown',event=>{if(event.key==='Escape'){results.hidden=true;searchInput.blur();}if(event.key==='Enter'){const link=results.querySelector('a');if(link){event.preventDefault();link.click();}}});
document.addEventListener('click',event=>{if(!event.target.closest('.search-wrap'))results.hidden=true;});
const themeButton=document.querySelector('#theme-toggle');
themeButton.addEventListener('click',()=>{const dark=document.body.classList.toggle('dark');themeButton.setAttribute('aria-pressed',String(dark));themeButton.setAttribute('aria-label',dark?'Cambiar a modo claro':'Cambiar a modo oscuro');});
const contentsLinks=[...document.querySelectorAll('.contents-sidebar a')];
const observer=new IntersectionObserver(entries=>{for(const entry of entries){if(!entry.isIntersecting)continue;for(const link of contentsLinks){const active=link.getAttribute('href')===`#${entry.target.id}`;link.classList.toggle('is-active',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');}}},{rootMargin:'-120px 0px -65% 0px'});
document.querySelectorAll('section[id],article.slide').forEach(node=>observer.observe(node));

// Controles de la ilustración; ambas orientaciones comparten el mismo ciclo.
for(const demo of document.querySelectorAll('.vector-demo')){
  const pause=demo.querySelector('.vector-pause');
  pause.addEventListener('click',()=>{
    const paused=demo.classList.toggle('is-paused');
    pause.setAttribute('aria-pressed',String(paused));
    pause.textContent=paused?'Continuar animación':'Pausar animación';
  });
  demo.querySelector('.vector-replay').addEventListener('click',()=>{
    demo.classList.add('is-started');demo.classList.remove('is-paused');pause.setAttribute('aria-pressed','false');pause.textContent='Pausar animación';
    const dots=demo.querySelectorAll('.vector-dot, .matrix-dot, .stair-animated');
    for(const dot of dots)dot.style.animation='none';
    void demo.offsetWidth;
    for(const dot of dots)dot.style.animation='';
  });
}

// La escena de dos recorridos empieza cuando el alumno llega a ella.
const stairStartObserver=new IntersectionObserver(entries=>{
  for(const entry of entries){
    if(entry.isIntersecting){entry.target.classList.add('is-started');stairStartObserver.unobserve(entry.target);}
  }
},{threshold:0.25});
document.querySelectorAll('.staircase-demo').forEach(demo=>stairStartObserver.observe(demo));

// Plegar cada lámina conserva el estado de sus ejercicios interiores.
function expandSlide(slide){
  if(!slide)return;
  slide.querySelector('.slide-toggle').setAttribute('aria-expanded','true');
  slide.querySelector('.slide-body').hidden=false;
}
for(const button of document.querySelectorAll('.slide-toggle')){
  button.addEventListener('click',()=>{
    const expanded=button.getAttribute('aria-expanded')==='true';
    button.setAttribute('aria-expanded',String(!expanded));
    document.getElementById(button.getAttribute('aria-controls')).hidden=expanded;
  });
}
function expandLinkedSlide(){
  const target=document.getElementById(location.hash.slice(1));
  expandSlide(target?.closest('.slide'));
}
window.addEventListener('hashchange',expandLinkedSlide);
document.addEventListener('click',event=>{
  const link=event.target.closest('a[href^="#"]');
  if(link)expandSlide(document.getElementById(link.getAttribute('href').slice(1))?.closest('.slide'));
});
document.querySelector('#present').addEventListener('click',()=>{
  if(document.body.classList.contains('presenting'))document.querySelectorAll('.slide').forEach(expandSlide);
});

// Cada botonera muestra un solo gráfico o argumento a la vez.
for(const explorer of document.querySelectorAll('.wage-explorer, .reason-explorer')){
  const choices=[...explorer.querySelectorAll('.chart-choice')];
  for(const choice of choices){
    choice.addEventListener('click',()=>{
      for(const button of choices)button.setAttribute('aria-pressed',String(button===choice));
      for(const panel of explorer.querySelectorAll('.chart-panel'))panel.hidden=panel.id!==choice.getAttribute('aria-controls');
      explorer.querySelector('.chart-status').textContent=`Mostrando ${choice.dataset.variable}.`;
    });
  }
}

// Video de datasets: capítulos, respuesta razonada y pausa al plegar.
for(const lesson of document.querySelectorAll('.dataset-lesson')){
  const video=lesson.querySelector('video');
  const chapters=[...lesson.querySelectorAll('.dataset-chapter')];
  for(const chapter of chapters){
    chapter.addEventListener('click',()=>{
      video.currentTime=Number(chapter.dataset.start);
      video.play().catch(()=>{lesson.querySelector('.dataset-status').textContent='Pulsa reproducir en los controles del video.';});
    });
  }
  video.addEventListener('timeupdate',()=>{
    const current=chapters.filter(button=>Number(button.dataset.start)<=video.currentTime).at(-1);
    for(const button of chapters)button.setAttribute('aria-pressed',String(button===current));
  });
  lesson.closest('.slide').querySelector('.slide-toggle').addEventListener('click',()=>{
    if(lesson.closest('.slide-body').hidden)video.pause();
  });
  document.addEventListener('visibilitychange',()=>{if(document.hidden)video.pause();});
  const slide=lesson.closest('.slide');
  new MutationObserver(()=>{if(document.body.classList.contains('presenting')&&!slide.classList.contains('active'))video.pause();}).observe(slide,{attributes:true,attributeFilter:['class']});
  for(const answer of lesson.querySelectorAll('[data-answer]')){
    answer.addEventListener('click',()=>{
      const correct=answer.dataset.answer==='panel';
      lesson.querySelector('.dataset-feedback').textContent=correct?'Correcto: son datos de panel. Seguimos a las mismas personas en varios períodos.':'Observa que se repiten las mismas personas A, B y C en varios años. Cada punto combina persona y período: son datos de panel.';
      for(const button of lesson.querySelectorAll('[data-answer]'))button.setAttribute('aria-pressed',String(button===answer));
    });
  }
}

// Salarios por estado civil: mostrar un grupo sin perder la comparación global.
for(const summary of document.querySelectorAll('.salary-summary')){
  for(const button of summary.querySelectorAll('.salary-group')){
    button.addEventListener('click',()=>{
      for(const choice of summary.querySelectorAll('.salary-group'))choice.setAttribute('aria-pressed',String(choice===button));
      for(const panel of summary.querySelectorAll('.salary-panel'))panel.hidden=panel.id!==button.getAttribute('aria-controls');
    });
  }
}

for(const demo of document.querySelectorAll('.variance-demo')){
 const slider=demo.querySelector('.variance-scale'),button=demo.querySelector('.variance-play');let playing=false,start=0;
 function update(){const s=Number(slider.value);for(const dot of demo.querySelectorAll('.variance-point'))dot.setAttribute('cx',String(365+s*Number(dot.dataset.z)*30));demo.querySelector('.variance-reading').textContent=`Desviación = ${s.toFixed(2)} · Varianza = ${(s*s).toFixed(2)}`;}
 function stop(){playing=false;button.setAttribute('aria-pressed','false');button.textContent='Animar aumento de varianza';}
 slider.addEventListener('input',()=>{stop();update();});
 function tick(t){if(!playing)return;if(demo.closest('.slide-body').hidden){stop();return;}if(!start)start=t;const p=Math.min(1,(t-start)/6500);slider.value=String(.2+2.3*p);update();if(p<1)requestAnimationFrame(tick);else stop();}
 button.addEventListener('click',()=>{if(playing){stop();return;}playing=true;start=0;slider.value='.2';update();button.setAttribute('aria-pressed','true');button.textContent='Pausar animación';requestAnimationFrame(tick);});
 update();
}

// Cinco figuras de inferencia. Los parámetros se reflejan en el código R visible.
for(const demo of document.querySelectorAll('.inference-demo')){
 const svg=demo.querySelector('.inf-plot'),reading=demo.querySelector('.inf-reading'),code=demo.querySelector('.inf-r-code');
 const template=code.textContent;let zDemo=demo.dataset.zs?JSON.parse(demo.dataset.zs):[];
 const zcrit=c=>c===.90?1.64485362695147:c===.99?2.5758293035489:1.95996398454005;
 const fmt=(v,d=2)=>Number(v).toLocaleString('es-CL',{maximumFractionDigits:d});
 function draw(){
  const p={};for(const control of demo.querySelectorAll('.inf-control')){p[control.dataset.key]=Number(control.value);const output=control.parentElement.querySelector('output');if(output)output.textContent=control.value;}
  if(p.exitos!==undefined){const control=demo.querySelector('[data-key="exitos"]');control.max=String(p.n-1);if(p.exitos>=p.n){p.exitos=p.n-1;control.value=String(p.exitos);control.parentElement.querySelector('output').textContent=control.value;}}
  let rCode=template;for(const [key,value] of Object.entries(p))rCode=rCode.replace(new RegExp('^'+key+' <- .*$', 'm'),`${key} <- ${value}`);
  if(zDemo.length)rCode=rCode.replace(/^z_demo <- .*$/m,`z_demo <- c(${zDemo.join(', ')})`);code.textContent=rCode;
  let html='',map;
  function axis(lo,hi,title){if(lo===hi){lo-=1;hi+=1;}const pad=(hi-lo)*.08;lo-=pad;hi+=pad;map=x=>85+(x-lo)/(hi-lo)*570;html+=`<line x1="85" y1="335" x2="655" y2="335" stroke="#8294a7"/>`;for(let i=0;i<=4;i++){const value=lo+(hi-lo)*i/4;html+=`<text x="${85+570*i/4}" y="356" text-anchor="middle">${fmt(value,2)}</text>`;}html+=`<text x="350" y="378" text-anchor="middle">${title}</text>`;}
  function reference(value,top=35,bottom=320){html+=`<line x1="${map(value)}" x2="${map(value)}" y1="${top}" y2="${bottom}" stroke="#1b2a5e" stroke-dasharray="5 5"/>`;}
  function band(lower,upper,center,y,color='#0160a0'){html+=`<line x1="${map(lower)}" x2="${map(upper)}" y1="${y}" y2="${y}" stroke="${color}" stroke-width="4"/><circle cx="${map(center)}" cy="${y}" r="4" fill="${color}"/>`;}
  const kind=demo.dataset.kind;
  if(kind==='tcl'){
   const mu=Number(demo.dataset.mu),sigma=Number(demo.dataset.sigma),se=sigma/Math.sqrt(p.n),se5=sigma/Math.sqrt(5);
   axis(mu-4*se5,mu+4*se5,'Promedio salarial (USD/h de 1976)');reference(mu);
   const peak=1/(sigma/Math.sqrt(200)*Math.sqrt(2*Math.PI));
   for(const [error,color] of [[se5,'#a0aab8'],[se,'#0160a0']]){let path='';for(let i=0;i<=220;i++){const x=mu-4*se5+8*se5*i/220;const density=Math.exp(-.5*((x-mu)/error)**2)/(error*Math.sqrt(2*Math.PI));path+=`${i?'L':'M'}${map(x)},${320-270*density/peak} `;}html+=`<path d="${path}" fill="none" stroke="${color}" stroke-width="3"/>`;}
   html+=`<text x="105" y="24">Azul: n = ${p.n} · Gris: n = 5 · Media fija μ = ${fmt(mu,3)}</text>`;
   reading.textContent=`Error estándar = ${fmt(se,3)} USD/h · Varianza de la media = ${fmt(se*se,3)}. Al aumentar n, la distribución de las medias se concentra. La curva normal es una aproximación del TCL.`;
  }else if(kind==='media'){
   const se=60/Math.sqrt(p.n),z=zcrit(p.confianza),margin=z*se,lower=200-margin,upper=200+margin;
   const means=zDemo.map(x=>200+x*se),low=means.map(x=>x-margin),high=means.map(x=>x+margin);axis(Math.min(lower,...low),Math.max(upper,...high),'Media de ventas');reference(200);
   band(lower,upper,200,45);html+='<text x="95" y="24">IC del ejemplo · línea vertical: μ = 200 en la ilustración</text>';
   let cover=0;for(let i=0;i<20;i++){const yes=low[i]<=200&&high[i]>=200;if(yes)cover++;band(low[i],high[i],means[i],90+i*11,yes?'#0160a0':'#e12523');}
   reading.textContent=`IC ${100*p.confianza}%: (${fmt(lower)}; ${fmt(upper)}) · margen = ${fmt(margin)}. En estas 20 repeticiones, ${cover} intervalos contienen μ = 200. El porcentaje observado fluctúa; la confianza describe el procedimiento repetido.`;
  }else if(kind==='precision'){
   const se=60/Math.sqrt(p.n),levels=[.90,.95,.99],margins=levels.map(c=>zcrit(c)*se);axis(200-Math.max(...margins),200+Math.max(...margins),'Media de ventas');reference(200);
   levels.forEach((level,i)=>{const y=85+i*85;band(200-margins[i],200+margins[i],200,y,['#00875a','#0160a0','#e12523'][i]);html+=`<text x="10" y="${y+4}">${100*level}%</text>`;});
   const required=Math.ceil((zcrit(p.confianza)*60/p.E)**2);
   reading.textContent=`Con n = ${p.n}, margen al ${100*p.confianza}% = ${fmt(zcrit(p.confianza)*se)}. Para un margen E = ${fmt(p.E)} al ${100*p.confianza}%, se requieren ${required} observaciones (redondeo hacia arriba). Mayor confianza ensancha; mayor n estrecha.`;
  }else if(kind==='proporcion'){
   const phat=p.exitos/p.n,z=zcrit(p.confianza),required=Math.ceil(z*z*p.p_previa*(1-p.p_previa)/(p.E*p.E));
   if(p.exitos>5&&p.n-p.exitos>5&&p.n>=30){const se=Math.sqrt(phat*(1-phat)/p.n),lower=phat-z*se,upper=phat+z*se;axis(Math.min(0,lower),Math.max(.20,upper+.03),'Proporción de defectuosos');reference(.05);band(lower,upper,phat,175);html+='<text x="95" y="35">Referencia del proveedor: p = 0,05</text>';const contains=lower<=.05&&upper>=.05;
    reading.textContent=`p̂ = ${fmt(phat,3)} · IC ${100*p.confianza}%: (${fmt(lower,4)}; ${fmt(upper,4)}). ${contains?'Incluye':'No incluye'} 0,05. Planificación: p* = ${fmt(p.p_previa)}, E = ${fmt(p.E,3)} → n = ${required}; largo deseado = ${fmt(2*p.E,3)}.`;
   }else{html='<text x="60" y="150">No se cumplen las condiciones de la aproximación normal.</text>';reading.textContent=`Se exige n ≥ 30, éxitos > 5 y fracasos > 5. No interpretamos un IC normal aquí. Planificación con p* y E indicados: n = ${required}.`;}
  }else{
   const difference=p.xbarra-680000,se=Math.sqrt(60000**2/p.nx+50000**2/p.ny),margin=zcrit(p.confianza)*se,lower=difference-margin,upper=difference+margin;
   axis(Math.min(0,lower),Math.max(0,upper),'Diferencia de medias (pesos del ejemplo)');reference(0);band(lower,upper,difference,180);html+='<text x="95" y="35">Ingeniería menos arquitectura · referencia: diferencia cero</text>';
   reading.textContent=`Diferencia = ${fmt(difference,0)} · IC ${100*p.confianza}%: (${fmt(lower,0)}; ${fmt(upper,0)}). ${lower<=0&&upper>=0?'Incluye cero: no se detecta diferencia al nivel elegido.':'Excluye cero: hay evidencia de diferencia entre las medias.'} Esto no identifica un efecto causal de la carrera.`;
  }
  svg.innerHTML=html;
 }
 for(const control of demo.querySelectorAll('.inf-control'))control.addEventListener('input',draw);
 const repeat=demo.querySelector('.inf-repeat');if(repeat)repeat.addEventListener('click',()=>{zDemo=Array.from({length:20},()=>Number((Math.sqrt(-2*Math.log(Math.max(Number.MIN_VALUE,Math.random())))*Math.cos(2*Math.PI*Math.random())).toFixed(6)));draw();});
 draw();
}

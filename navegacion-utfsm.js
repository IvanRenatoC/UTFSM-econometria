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

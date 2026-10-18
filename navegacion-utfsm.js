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

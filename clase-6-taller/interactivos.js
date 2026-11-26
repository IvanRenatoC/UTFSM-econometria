// Las curvas proceden de predict() ejecutado en R y exportado con el taller.
const format = value => Number(value).toLocaleString('es-CL', {maximumFractionDigits: 3});
for (const button of document.querySelectorAll('.copy')) {
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(button.parentElement.nextElementSibling.textContent);
      button.textContent = 'Copiado';
      setTimeout(() => { button.textContent = 'Copiar código'; }, 1800);
    } catch {
      button.textContent = 'Selecciona el código para copiarlo';
    }
  });
}
function openAnchor() {
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  const details = target?.querySelector('details');
  if (details) details.open = true;
}
window.addEventListener('hashchange', openAnchor);
openAnchor();

async function initializeGraphs() {
  const response = await fetch('datos/resultados-interactivos.json');
  if (!response.ok) throw new Error('No se pudieron cargar los datos de los gráficos.');
  const data = await response.json();
  for (const demo of document.querySelectorAll('.demo')) {
    const canvas = demo.querySelector('canvas');
    const ctx = canvas.getContext('2d');
    const control = demo.querySelector('input,select');
    const plotType = demo.dataset.plot;
    let frame = 0;
    let progress = 1;
    const defaultValue = control.value;
    function draw() {
      const review = plotType === 'repaso';
      const type = review ? control.value : plotType;
      const logged = type === 'lognivel' || type === 'loglog';
      const explanation = {
        lognivel: 'Log-nivel · Eje Y en logaritmos y educación en años. La pendiente multiplicada por 100 aproxima el cambio porcentual por un año adicional.',
        loglog: 'Log-log · Ambos ejes en logaritmos. La pendiente es la elasticidad, el cambio porcentual aproximado del salario por 1% más de educación.',
        cuad: 'Cuadrática · wage = b0 + b1·exper + b2·exper². La pendiente b1 + 2·b2·exper cambia a medida que avanzamos por la misma curva.',
        int: demo.dataset.interactionDescription
      };
      if (review) {
        demo.querySelector('.review-explanation').textContent = explanation[type];
        for (const button of demo.querySelectorAll('[data-model]')) {
          button.setAttribute('aria-pressed', String(button.dataset.model === type));
        }
      }
      const unit = type === 'escala' ? control.value : 'usd';
      const fx = unit === 'meses' ? 12 : 1;
      const fy = unit === 'pesos' ? 1000 : 1;
      const key = type === 'int' ? 'int' + (review ? '35' : control.value) : type === 'escala' ? 'nivel' : type;
      const curve = data[key];
      const points = data.puntos.filter(p => type !== 'loglog' || p.educ > 0).map(p => ({
        x: (type === 'cuad' ? p.exper : type === 'loglog' ? Math.log(p.educ) : p.educ) * fx,
        y: (logged ? Math.log(p.wage) : p.wage) * fy
      }));
      const line = curve.map(p => ({x: p.x * fx, y: p.y * fy}));
      const xMax = Math.max(...points.map(p => p.x));
      const yMin = Math.min(0, ...line.map(p => p.y), ...points.map(p => p.y));
      const yMax = Math.max(...points.map(p => p.y)) * 1.04;
      const left = 90, right = 868, top = 28, bottom = 385;
      const x = v => left + v / xMax * (right - left);
      const y = v => bottom - (v - yMin) / (yMax - yMin) * (bottom - top);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'white'; ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.font = '14px sans-serif'; ctx.lineWidth = 1;
      for (let i = 0; i <= 5; i++) {
        const value = yMin + i * (yMax - yMin) / 5;
        ctx.strokeStyle = '#dce3ec'; ctx.beginPath();
        ctx.moveTo(left, y(value)); ctx.lineTo(right, y(value)); ctx.stroke();
        ctx.fillStyle = '#253047'; ctx.textAlign = 'right';
        ctx.fillText(format(value), left - 10, y(value) + 5);
        const xv = i * xMax / 5;
        ctx.textAlign = 'center'; ctx.fillText(format(xv), x(xv), bottom + 24);
      }
      ctx.strokeStyle = '#253047'; ctx.beginPath(); ctx.moveTo(left, top);
      ctx.lineTo(left, bottom); ctx.lineTo(right, bottom); ctx.stroke();
      ctx.fillStyle = '#005f9648';
      for (const p of points) {
        ctx.beginPath(); ctx.arc(x(p.x), y(p.y), 3, 0, Math.PI * 2); ctx.fill();
      }
      ctx.strokeStyle = '#D6A600'; ctx.lineWidth = 4; ctx.beginPath();
      const count = Math.max(1, Math.ceil(line.length * progress));
      line.slice(0, count).forEach((p, i) => {
        if (i === 0) ctx.moveTo(x(p.x), y(p.y));
        else ctx.lineTo(x(p.x), y(p.y));
      });
      ctx.stroke();
      if (review && type === 'int') {
        ctx.strokeStyle = '#005F96'; ctx.beginPath();
        data.int5.slice(0,count).forEach((p,i) => {
          if (i === 0) ctx.moveTo(x(p.x),y(p.y)); else ctx.lineTo(x(p.x),y(p.y));
        });
        ctx.stroke();
      }
      ctx.fillStyle = '#253047'; ctx.textAlign = 'center';
      const xLabel = type === 'loglog' ? 'Logaritmo de educación (años)' : type === 'cuad' ? 'Experiencia potencial (años)' : unit === 'meses' ? 'Educación (meses)' : 'Educación (años)';
      ctx.fillText(xLabel, (left + right) / 2, 440);
      ctx.save(); ctx.translate(20, 220); ctx.rotate(-Math.PI / 2);
      ctx.fillText(logged ? 'Logaritmo del salario (USD/h)' : unit === 'pesos' ? 'Salario (pesos/h, TC hipotético)' : 'Salario (USD/h de 1976)', 0, 0); ctx.restore();
      let message = type === 'int' ? 'Experiencia fija en ' + control.value + ' años.' : type === 'escala' ? 'Mismas personas y mismo ajuste económico, con unidades ' + unit + '.' : '';
      if (!review && ['log', 'cuad', 'lognivel', 'loglog'].includes(type)) {
        const target = type === 'loglog' ? Math.log(Number(control.value)) : Number(control.value);
        const chosen = line.reduce((best, p) => Math.abs(p.x - target) < Math.abs(best.x - target) ? p : best);
        ctx.fillStyle = '#B2292E'; ctx.beginPath();
        ctx.arc(x(chosen.x), y(chosen.y), 7, 0, Math.PI * 2); ctx.fill();
        message = xLabel + ' = ' + target + '. ' + (type === 'log' ? 'Curva exp de log ajustado' : logged ? 'Logaritmo del salario ajustado' : 'Salario ajustado') + ' ≈ ' + format(chosen.y) + (logged ? ' en escala logarítmica.' : ' USD/h.');
      }
      demo.querySelector('output').textContent = review ? '' : message;
      const table = document.createElement('table');
      table.innerHTML = '<thead><tr><th>' + xLabel + '</th><th>Valor de la curva</th></tr></thead>';
      const body = document.createElement('tbody');
      for (const p of line) {
        const row = document.createElement('tr');
        for (const value of [p.x, p.y]) {
          const cell = document.createElement('td'); cell.textContent = format(value); row.append(cell);
        }
        body.append(row);
      }
      table.append(body); demo.querySelector('.curve-table').replaceChildren(table);
    }
    for (const button of demo.querySelectorAll('[data-model]')) {
      button.addEventListener('click', () => {
        control.value = button.dataset.model;
        demo.querySelector('.animate').click();
      });
    }
    control.addEventListener('input', () => { cancelAnimationFrame(frame); progress = 1; draw(); });
    demo.querySelector('.reset').addEventListener('click', () => {
      cancelAnimationFrame(frame); control.value = defaultValue; progress = 1; draw();
    });
    demo.querySelector('.animate').addEventListener('click', () => {
      cancelAnimationFrame(frame);
      const start = performance.now();
      function tick(now) {
        progress = matchMedia('(prefers-reduced-motion: reduce)').matches ? 1 : Math.min(1, (now - start) / 1500); draw();
        if (progress < 1) frame = requestAnimationFrame(tick);
      }
      frame = requestAnimationFrame(tick);
    });
    draw();
  }
}
initializeGraphs().catch(error => {
  for (const demo of document.querySelectorAll('.demo')) {
    demo.querySelector('output').textContent = error.message + ' Abre la página publicada o usa un servidor local. El código y los resultados de R siguen disponibles debajo.';
  }
});

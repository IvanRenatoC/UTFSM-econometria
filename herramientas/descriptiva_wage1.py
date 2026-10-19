"""Resumen salarial calculado del CSV, reproducible con el código R de la lámina."""
from html import escape as e
from collections import Counter
from statistics import mean,median,variance,stdev
import csv,json,math

def quantile(x,p):
 x=sorted(x);position=(len(x)-1)*p;lo=math.floor(position);hi=math.ceil(position)
 return x[lo]+(x[hi]-x[lo])*(position-lo)

def wage_groups(root):
 rows=list(csv.DictReader((root/'datos/wage1.csv').open()))
 groups=[('total','Total',[float(r['wage']) for r in rows]),('no','No casados (married = 0)',[float(r['wage']) for r in rows if r['married']=='0']),('si','Casados (married = 1)',[float(r['wage']) for r in rows if r['married']=='1'])]
 result=[]
 for key,label,x in groups:
  counts=Counter(x);modes=sorted(v for v,n in counts.items() if n==max(counts.values()))
  result.append(dict(key=key,label=label,n=len(x),promedio=mean(x),mediana=median(x),moda='; '.join(f'{v:g}' for v in modes),P24=quantile(x,.24),P50=quantile(x,.5),P75=quantile(x,.75),varianza=variance(x),desviacion=stdev(x),rango=max(x)-min(x),riq=quantile(x,.75)-quantile(x,.25)))
 return result

def render_descriptiva(root):
 groups=wage_groups(root)
 buttons=''.join(f'<button type="button" class="salary-group" data-group="{g["key"]}" aria-controls="salary-{g["key"]}" aria-pressed="{str(i==0).lower()}">{e(g["label"])}</button>' for i,g in enumerate(groups))
 panels=''
 for i,g in enumerate(groups):
  cards=''.join(f'<div><span>{label}</span><strong>{e(g[metric]) if metric=="moda" else format(g[metric],".3f")}</strong></div>' for metric,label in [('promedio','Promedio'),('mediana','Mediana'),('moda','Moda'),('P24','Percentil 24'),('P50','Percentil 50'),('P75','Percentil 75')])
  panels+=f'<section class="salary-panel" id="salary-{g["key"]}"'+(' hidden' if i else '')+f'><p><strong>{e(g["label"])} · n = {g["n"]}</strong></p><div class="salary-cards">{cards}</div></section>'
 rows=''.join('<tr><th scope="row">'+e(g['label'])+'</th><td>'+str(g['n'])+'</td>'+''.join('<td>'+str(g[m] if m=='moda' else f'{g[m]:.3f}')+'</td>' for m in ['promedio','mediana','moda','P24','P50','P75'])+'</tr>' for g in groups)
 graph='<svg viewBox="0 0 700 270" class="wage-chart salary-comparison" role="img" aria-label="Promedio salarial total, no casados y casados">'
 maximum=max(g['promedio'] for g in groups)*1.2
 for i,g in enumerate(groups):
  height=170*g['promedio']/maximum;x=130+i*210;color=['#00875A','#0160A0','#F8C751'][i]
  graph+=f'<rect x="{x-48}" y="{205-height}" width="96" height="{height}" fill="{color}"/><text x="{x}" y="{193-height}" text-anchor="middle">{g["promedio"]:.3f}</text><text x="{x}" y="230" text-anchor="middle">{["Total","No casados","Casados"][i]}</text>'
 graph+='<text x="350" y="260" text-anchor="middle">Salario promedio por hora (USD de 1976)</text></svg>'
 return '<div class="salary-summary"><p>Comparamos el salario de todas las personas y de los grupos definidos por <code>married</code>. <strong>married = 0 significa no casado/a; no permite identificar solamente a los solteros.</strong></p><div class="salary-choices" role="group" aria-label="Grupo salarial">'+buttons+'</div>'+panels+graph+'<details class="check"><summary>Ver los tres grupos juntos</summary><div class="chart-table-wrap"><table class="schedule"><thead><tr><th>Grupo</th><th>n</th><th>Promedio</th><th>Mediana</th><th>Moda</th><th>P24</th><th>P50</th><th>P75</th></tr></thead><tbody>'+rows+'</tbody></table></div></details><p>La media usa todos los salarios y es sensible a extremos. La mediana es el valor central y coincide con P50. La moda es el salario más frecuente. P24 y P75 señalan posiciones de la distribución; se usa la interpolación <code>type = 7</code> de R.</p><p class="data-note">526 personas de wage1 · CPS de Estados Unidos, 1976 · salarios en USD por hora de ese período. Comparar estos grupos no demuestra un efecto causal del estado civil.</p></div>'


def render_dispersion(root):
 import random
 from statistics import mean,stdev
 rng=random.Random(39);raw=[rng.gauss(0,1) for _ in range(30)];z=raw+[-x for x in raw];scale=stdev(z);z=[x/scale for x in z]
 svg='<svg class="wage-chart variance-cloud" viewBox="0 0 700 300" role="img" aria-label="Nube artificial: media fija 10 y varianza creciente"><line x1="65" y1="240" x2="665" y2="240" stroke="#8294a7"/><line x1="365" y1="45" x2="365" y2="240" stroke="#1b2a5e" stroke-dasharray="5 5"/>'
 for value in range(0,21,2):svg+=f'<text x="{65+value*30}" y="263" text-anchor="middle">{value}</text>'
 for i,value in enumerate(z):
  y=75+rng.random()*135
  svg+=f'<circle class="variance-point" data-z="{value:.15g}" cx="{365+.2*value*30:.3f}" cy="{y:.3f}" r="5" fill="#0160a0" fill-opacity=".7"/>'
 svg+='<text x="350" y="292" text-anchor="middle">Valor artificial · media fija = 10</text></svg>'
 body=''.join('<tr><th scope="row">'+e(g['label'])+'</th>'+''.join('<td>'+f'{g[k]:.3f}'+'</td>' for k in ['varianza','desviacion','rango','riq'])+'<td>'+f'{100*g["desviacion"]/g["promedio"]:.2f} %'+'</td></tr>' for g in wage_groups(root))
 return '<div class="variance-demo"><p><strong>La media permanece en 10.</strong> Mueve el control o reproduce la animación: cuando aumenta la desviación estándar, los mismos puntos se alejan del centro y crece la varianza.</p>'+svg+'<label>Desviación estándar: <input class="variance-scale" type="range" min="0.2" max="2.5" step="0.01" value="0.2"></label><p class="variance-reading" role="status">Desviación = 0,20 · Varianza = 0,04</p><button class="variance-play chart-choice" type="button" aria-pressed="false">Animar aumento de varianza</button><p class="data-note">Ilustración artificial. La altura solo separa visualmente los puntos; la dispersión que medimos es horizontal. Varianza = desviación estándar².</p></div><h4>Indicadores reales del salario</h4><div class="chart-table-wrap"><table class="schedule"><thead><tr><th>Grupo</th><th>Varianza</th><th>Desv. estándar</th><th>Rango</th><th>RIQ</th><th>CV</th></tr></thead><tbody>'+body+'</tbody></table></div><p>La varianza está en (USD/h)²; la desviación estándar y el RIQ, en USD/h. El RIQ mide P75 − P25 y es menos sensible a extremos que la varianza. El CV expresa la desviación como porcentaje de la media. Los cálculos corresponden a las 526 personas de wage1 y a cada grupo de estado civil.</p>'

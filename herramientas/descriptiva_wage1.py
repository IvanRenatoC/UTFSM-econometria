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

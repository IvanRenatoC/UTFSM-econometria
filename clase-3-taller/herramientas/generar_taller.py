"""Genera notebook, script y guía desde el contenido común de la clase 3."""
from pathlib import Path
import json, hashlib
ROOT = Path(__file__).resolve().parent.parent

def generar():
    contenido = json.loads((ROOT / 'contenido-clase-3.json').read_text())
    acts = [a for b in contenido['bloques'] for a in b['laminas']]
    code = '\n\n'.join(a['id']+'\n'+a.get('codigo_inicial','')+'\n'+a['codigo']+'\n'+a.get('reto_codigo','')+'\n'+'\n'.join(x[2] for x in a.get('explicaciones',[]) if len(x)>2) for a in acts)
    verification = json.loads((ROOT / 'datos/verificacion.json').read_text())
    if hashlib.sha256(code.encode()).hexdigest() != verification['codigo_sha256']:
        raise ValueError('El código cambió: ejecutar verificar_en_R.mjs antes de regenerar las salidas.')
    outputs = json.loads((ROOT / 'datos/salidas-verificadas-r.json').read_text())
    for a in acts:
        a['salidas_r'] = [['Salida del ejemplo ejecutado en R', outputs[a['id']]]]
    cells = []
    guia = []
    script = ['# Taller 3: ejecutar desde clase-3-taller/.\n']
    def md(texto, id):
        cells.append({'cell_type': 'markdown', 'id': id, 'metadata': {}, 'source': (texto+'\n').splitlines(True)})
        guia.append(texto)
    def r(codigo, id):
        cells.append({'cell_type': 'code', 'id': id, 'metadata': {}, 'source': (codigo+'\n').splitlines(True), 'outputs': [], 'execution_count': None})
        script.append(codigo+'\n\n')
        guia.append('```r\n'+codigo+'\n```')
    def teaching(lamina):
        key = lamina['id'].lower()
        if lamina.get('proposito'):
            md('**Propósito del ejemplo**\n\n'+lamina['proposito'], key+'-proposito')
        if lamina.get('definiciones'):
            md('\n\n'.join('**'+t+'**\n\n'+x for t,x in lamina['definiciones']),key+'-definiciones')
        for i,t in enumerate(lamina.get('tablas_didacticas',[])):
            cols=t['columnas']
            md('**'+t['titulo']+'**\n\n| '+' | '.join(cols)+' |\n| '+' | '.join('---' for _ in cols)+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in t['filas']),key+'-tabla-'+str(i))
        if lamina.get('pizarra'):
            md('**Para desarrollar en la pizarra**\n\n'+'\n\n'.join('**'+f['titulo']+'**\n\n$$'+f['latex']+'$$' for f in lamina['pizarra']),key+'-pizarra')
        if lamina.get('desarrollo'):
            md('\n\n'.join('**'+t+'**\n\n'+x for t,x in lamina['desarrollo']),key+'-desarrollo')
    def steps(lamina, suffix, title):
        key=lamina['id'].lower()
        md('**'+title+'**',key+suffix)
        for i,item in enumerate(lamina['explicaciones'],1):
            md('**'+item[0]+'**\n\n'+item[1],key+suffix+'-'+str(i))
            if len(item)>2:
                r(item[2],key+suffix+'-'+str(i)+'-r')
    md('# '+contenido['titulo']+'\n\n'+contenido['estado']+'\n\nDocente: '+contenido['docente']+'\n\nEjecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.', 'inicio')
    md('## Agenda\n\n'+'\n'.join('- '+hora+': '+tema for hora,tema,_ in contenido['agenda']), 'agenda')
    for bloque in contenido['bloques']:
        md('## '+bloque['etiqueta']+' · '+bloque['titulo'], bloque['id'].lower())
        for lamina in bloque['laminas']:
            md('### '+lamina['titulo']+'\n\n'+lamina['texto'], lamina['id'].lower()+'-consigna')
            teaching(lamina)
            md('**Referencia en la cátedra:** '+lamina.get('referencia',''), lamina['id'].lower()+'-referencia')
            if lamina.get('explicaciones_al_inicio'):
                steps(lamina,'-ejercicio-guiado','Ejercicio guiado')
            if lamina.get('codigo_inicial'):
                md('**Preparar los datos: ejecuta sólo este bloque**', lamina['id'].lower()+'-preparar-datos')
                r(lamina['codigo_inicial'], lamina['id'].lower()+'-carga-r')
                md(lamina['lectura_codigo_inicial'], lamina['id'].lower()+'-carga-lectura')
            if lamina.get('sintaxis'):
                md('**Firma de '+lamina.get('nombre_funcion','lm()')+' - referencia, no ejecutar como llamada completa**\n\n```r\n'+lamina['sintaxis']+'\n```\n\n[Documentación oficial de R]('+lamina.get('fuente_sintaxis','https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html')+')', lamina['id'].lower()+'-sintaxis')
            if lamina.get('codigo'):
                r(lamina['codigo'], lamina['id'].lower()+'-r')
            if lamina.get('despues_codigo'):
                md('\n\n'.join('**'+t+'**\n\n'+d for t,d in lamina['despues_codigo']), lamina['id'].lower()+'-despues-codigo')
            for index, block in enumerate(lamina.get('bloques_codigo', []), 1):
                md('**'+block['titulo']+'**', lamina['id'].lower()+'-ejercicio-'+str(index))
                r(block['codigo'], lamina['id'].lower()+'-ejercicio-'+str(index)+'-r')
                md(block['lectura'], lamina['id'].lower()+'-ejercicio-'+str(index)+'-lectura')
            if lamina.get('tablas_anova'):
                table_text = []
                for t in lamina['tablas_anova']:
                    table_text.append('**'+t['titulo']+' · '+t['modelo']+' · n = '+str(t['n'])+'**\n\n| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |\n|---|---:|---:|---:|---:|---:|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in t['filas']))
                md('\n\n'.join(table_text)+'\n\n'+lamina['nota_anova'], lamina['id'].lower()+'-anova')
            if lamina.get('salidas_r'):
                md('**Resultados de referencia calculados en R**\n\n'+'\n\n'.join('**'+t+'**\n\n```text\n'+out+'\n```' for t,out in lamina['salidas_r']), lamina['id'].lower()+'-salidas')
            if lamina.get('explicaciones') and not lamina.get('explicaciones_al_inicio'):
                steps(lamina,'-explicaciones','El código, paso a paso')
            md('**Lectura del resultado:** '+lamina['lectura'], lamina['id'].lower()+'-lectura')
            if lamina.get('reto_codigo'):
                md('**Reto adicional: cambiar solo a Juan**',lamina['id'].lower()+'-reto')
                r(lamina['reto_codigo'],lamina['id'].lower()+'-reto-r')
            if lamina.get('despues_lectura'):
                md('\n\n'.join('**'+t+'**\n\n'+d for t,d in lamina['despues_lectura']), lamina['id'].lower()+'-despues-lectura')
            if lamina.get('quiz'):
                md('**Autoevaluación**\n\n'+'\n\n'.join(q+'\n\n'+'\n'.join(str(i+1)+'. '+v for i,v in enumerate(opts))+'\n\nRespuesta: '+opts[correct]+' '+reason for q,opts,correct,reason in lamina['quiz']),lamina['id'].lower()+'-quiz')
    nb = {'nbformat': 4, 'nbformat_minor': 5, 'metadata': {'kernelspec': {'display_name': 'R', 'language': 'R', 'name': 'ir'}, 'language_info': {'name': 'R', 'file_extension': '.r', 'mimetype': 'text/x-r-source'}}, 'cells': cells}
    (ROOT / 'clase-taller-3.ipynb').write_text(json.dumps(nb, ensure_ascii=False, indent=1)+'\n')
    (ROOT / 'clase-taller-3.R').write_text(''.join(script).rstrip()+'\n')
    (ROOT / 'guia-actividades-taller-3.md').write_text('\n'.join(line.rstrip() for line in '\n\n'.join(guia).splitlines())+'\n')
    return contenido

if __name__ == '__main__':
    generar()
    print('Notebook, script y guía de clase 3 generados; sin ejecución R.')

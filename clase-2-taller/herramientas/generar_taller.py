"""Genera notebook, script y guía desde el contenido común de la clase 2."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parent.parent

def generar():
    contenido = json.loads((ROOT / 'contenido-clase-2.json').read_text())
    cells = []
    guia = []
    script = ['# Taller 2: ejecutar desde clase-2-taller/.\n']
    def md(texto, id):
        cells.append({'cell_type': 'markdown', 'id': id, 'metadata': {}, 'source': (texto+'\n').splitlines(True)})
        guia.append(texto)
    def r(codigo, id):
        cells.append({'cell_type': 'code', 'id': id, 'metadata': {}, 'source': (codigo+'\n').splitlines(True), 'outputs': [], 'execution_count': None})
        script.append(codigo+'\n\n')
        guia.append('```r\n'+codigo+'\n```')
    md('# '+contenido['titulo']+'\n\n'+contenido['estado']+'\n\nDocente: '+contenido['docente']+'\n\nEjecuta las celdas en orden con kernel R. En Colab selecciona R en el tipo de entorno; no uses %%R ni rpy2.', 'inicio')
    md('## Agenda\n\n'+'\n'.join('- '+hora+': '+tema for hora,tema,_ in contenido['agenda']), 'agenda')
    for bloque in contenido['bloques']:
        md('## '+bloque['etiqueta']+' · '+bloque['titulo'], bloque['id'].lower())
        for lamina in bloque['laminas']:
            md('### '+lamina['titulo']+'\n\n'+lamina['texto'], lamina['id'].lower()+'-consigna')
            if lamina.get('sintaxis'):
                md('**Firma oficial de lm() — referencia, no ejecutar como llamada completa**\n\n```r\n'+lamina['sintaxis']+'\n```\n\n[Documentación oficial de R](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html)', lamina['id'].lower()+'-sintaxis')
            r(lamina['codigo'], lamina['id'].lower()+'-r')
            if lamina.get('tablas_anova'):
                table_text = []
                for t in lamina['tablas_anova']:
                    table_text.append('**'+t['titulo']+' · '+t['modelo']+' · n = '+str(t['n'])+'**\n\n| Fuente de variación | Suma de cuadrados | Grados de libertad | Cuadrado medio | F | p-valor |\n|---|---:|---:|---:|---:|---:|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in t['filas']))
                md('\n\n'.join(table_text)+'\n\n'+lamina['nota_anova'], lamina['id'].lower()+'-anova')
            if lamina.get('salidas_r'):
                md('**Resultados de referencia calculados en R**\n\n'+'\n\n'.join('**'+t+'**\n\n```text\n'+out+'\n```' for t,out in lamina['salidas_r']), lamina['id'].lower()+'-salidas')
            if lamina.get('explicaciones'):
                md('**El código, paso a paso**\n\n'+'\n\n'.join('**'+t+'**\n\n'+d for t,d in lamina['explicaciones']), lamina['id'].lower()+'-explicaciones')
            md('**Lectura del resultado:** '+lamina['lectura'], lamina['id'].lower()+'-lectura')
    nb = {'nbformat': 4, 'nbformat_minor': 5, 'metadata': {'kernelspec': {'display_name': 'R', 'language': 'R', 'name': 'ir'}, 'language_info': {'name': 'R', 'file_extension': '.r', 'mimetype': 'text/x-r-source'}}, 'cells': cells}
    (ROOT / 'clase-taller-2.ipynb').write_text(json.dumps(nb, ensure_ascii=False, indent=1)+'\n')
    (ROOT / 'clase-taller-2.R').write_text(''.join(script).rstrip()+'\n')
    (ROOT / 'guia-actividades-taller-2.md').write_text('\n\n'.join(guia)+'\n')
    return contenido

if __name__ == '__main__':
    generar()
    print('Notebook, script y guía de clase 2 generados; sin ejecución R.')

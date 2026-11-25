# Clase 6 · Interpretación de modelos en R

Taller de 110 minutos basado en la cátedra 6, con 8 láminas en el orden de sus cuatro temas.
Los tiempos son transcurridos desde el comienzo y suman 110 minutos de actividades.

- Fuente teórica https://hizocar.github.io/econometria-usm/clases/clase6/
- Base wage1 de Wooldridge, copia local en datos/wage1.csv. La columna rownames proviene de la exportación y no se usa como regresor.
- Documentación https://justinmshea.github.io/wooldridge/reference/wage1.html
- Notebook con kernel R en clase-taller-6.ipynb.
- Página en index.html y script en clase-taller-6.R.
- contenido-clase-6.json es la fuente de ejemplos, ejercicios, explicaciones y soluciones.
- Verificación ejecutada con webR. Las salidas y curvas exportadas están en datos/.
- Todas las curvas de la página se calcularon con predict() en R.

Para regenerar después de editar el contenido, ejecuta desde la raíz del repositorio:

    WEBR_MODULE=/ruta/a/webr/dist/webr.mjs node clase-6-taller/herramientas/verificar_en_R.mjs
    python3 clase-6-taller/herramientas/generar_web.py

El módulo también puede resolverse desde una instalación local de webr mediante Node.
La carga de datos usa la copia local si está disponible y el paquete wooldridge en Colab.
El notebook tiene las mismas 16 celdas de código que los 8 ejemplos y sus 8 soluciones de la página.

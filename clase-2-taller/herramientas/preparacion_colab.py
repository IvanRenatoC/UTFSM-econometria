"""Guía visual de acceso a Colab, exclusiva de la página web."""
from html import escape
from pathlib import Path
import struct

def render_preparacion(root: Path):
 pasos = [
  ('Abre Google Drive', 'Inicia sesión con tu cuenta de Google. Abre el menú de aplicaciones y selecciona Drive.', 'Menú de aplicaciones de Google con el acceso a Drive.'),
  ('Busca las aplicaciones disponibles', 'Si todavía no tienes Colaboratory conectado, en Drive selecciona Nuevo → Más → Conectar más aplicaciones. También puedes abrir Más apps de Google Workspace Marketplace desde el menú de aplicaciones, como muestra esta imagen.', 'Menú de Google con Más apps de Google Workspace Marketplace resaltado.'),
  ('Conecta Google Colaboratory', 'Busca Google Colab o Colaboratory y elige la aplicación Colaboratory, del equipo Colaboratory team. Pulsa Instalar y sigue los pasos de conexión a tu cuenta.', 'Resultados de Marketplace con la aplicación oficial Colaboratory y su botón Instalar resaltados.'),
  ('Comprueba el acceso desde Drive', 'Vuelve a Drive: en Nuevo → Más debe aparecer Google Colaboratory. Si ya lo tienes disponible, puedes omitir la instalación y comenzar directamente.', 'Menú Más de Google Drive con Google Colaboratory señalado con una flecha.'),
  ('Abre la configuración del entorno', 'Con el notebook abierto en Colab, ve a Entorno de ejecución → Cambiar tipo de entorno de ejecución. Allí puedes seleccionar el lenguaje que ejecutará las celdas.', 'Menú Entorno de ejecución de Colab con Cambiar tipo de entorno de ejecución señalado.'),
  ('Selecciona R y guarda', 'En Tipo de entorno de ejecución, selecciona R y pulsa Guardar. Para este taller ejecutaremos R directamente: no necesitas %load_ext rpy2.ipython ni escribir %%R al inicio de cada celda. Si ya aparece R, conserva esa selección.', 'Ventana de configuración de Colab con R seleccionado y el botón Guardar visible.')
 ]
 figuras=[]
 for n,(title,text,alt) in enumerate(pasos,1):
  archivo=f'colab-{n}.png'
  with (root/archivo).open('rb') as f:
   ancho,alto=struct.unpack('>II',f.read(24)[16:24])
  figuras.append(f'<figure class="colab-step'+(' colab-wide' if n>2 else '')+f'" id="colab-paso-{n}"><figcaption><h4>{n}. {escape(title)}</h4><p>{escape(text)}</p></figcaption><a href="{archivo}" target="_blank" rel="noopener" aria-label="Ampliar imagen del paso {n}"><img src="{archivo}" alt="{escape(alt)}" width="{ancho}" height="{alto}" loading="lazy"></a></figure>')
 return '''<section class="brief colab-preparation" id="preparar-colab" aria-labelledby="titulo-preparar-colab">
<style>.colab-preparation .colab-steps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.5rem}.colab-preparation .colab-step{margin:0;padding:1rem;border:1px solid #dce3ec;border-radius:12px;background:#f7f9fc}.colab-preparation .colab-wide{grid-column:1/-1}.colab-preparation h4{margin-top:0;color:#1b2a5e}.colab-preparation img{display:block;width:auto;max-width:100%;height:auto;max-height:420px;margin:1rem auto 0;border-radius:8px}.colab-preparation .colab-wide img{width:100%;max-height:none}.colab-preparation a:focus-visible{outline:3px solid #e5b300;outline-offset:4px}@media(max-width:640px){.colab-preparation .colab-steps{grid-template-columns:1fr}}</style>
<h3 id="titulo-preparar-colab">Antes de programar: prepara Google Colaboratory</h3>
<p>Antes de comenzar el taller, debes poder acceder a <strong>Google Colaboratory (Colab)</strong> con tu cuenta de Google. Lo utilizaremos para abrir y ejecutar el notebook desde el navegador. Comprueba que esté disponible en las opciones de Google Drive; si todavía no aparece, conéctalo siguiendo estos pasos.</p>
<div class="colab-steps">'''+''.join(figuras)+'''</div>
<p>Puedes pulsar cada imagen para verla en tamaño completo. Después, descarga el <a href="clase-taller-2.ipynb" download>notebook del taller</a> y ábrelo desde <a href="https://colab.research.google.com/">Google Colab</a> mediante Archivo → Subir notebook. El archivo del curso está preparado para trabajar directamente en R.</p>
<p class="data-note">Aplicación oficial: <a href="https://workspace.google.com/marketplace/app/colaboratory/1014160490159">Colaboratory en Google Workspace Marketplace</a>.</p></section>'''

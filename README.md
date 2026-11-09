# Econometría UTFSM

Material del taller de Econometría ICS-294.

## Clase 1

Todo el material específico de la primera clase está en [clase-1-taller/](clase-1-taller/).

- [Abrir la clase](clase-1-taller/index.html)
- [Notebook completo en R](clase-1-taller/clase-taller-1.ipynb)
- [Guía del material](clase-1-taller/README.md)
- [Ejercicios en PDF](clase-1-taller/ejercicios-econometria-taller-1.pdf)
- [Respuestas en PDF](clase-1-taller/respuestas-ejercicios-econometria-taller-1.pdf)

Para ejecutar el notebook o el script R, utiliza `clase-1-taller/` como directorio de trabajo, junto a su carpeta `datos/`.

Para regenerar la web desde la raíz:

```sh
python3 clase-1-taller/herramientas/generar_web.py
```

## Clase 2

Base de trabajo preparada en [clase-2-taller/](clase-2-taller/).

- [Plantilla web](clase-2-taller/index.html)
- [Notebook de R](clase-2-taller/clase-taller-2.ipynb)
- [Instrucciones para desarrollar la clase](clase-2-taller/instruccion-clase-taller-2.md)

## Clase 3

Taller de causalidad y variable omitida, con 16 láminas y notebook sincronizado.

- [Página de la clase](clase-3-taller/index.html)
- [Notebook de R](clase-3-taller/clase-taller-3.ipynb)
- [Guía docente](clase-3-taller/guia-docente-taller-3.md)
- [Guía del material](clase-3-taller/README.md)

## Clase 4

Regresión lineal múltiple, 18 láminas en el orden de la cátedra y notebook R sincronizado.

- [Página de la clase](clase-4-taller/index.html)
- [Notebook R](clase-4-taller/clase-taller-4.ipynb)
- [Guía del material](clase-4-taller/README.md)

## Recursos compartidos del curso

El logo `Logo_UTFSM.png`, los estilos `identidad-utfsm.css`, la navegación `navegacion-utfsm.js`, la especificación `IDENTIDAD-VISUAL.md` y el documento general `Econometria_USM_2026_3.pdf` permanecen en la raíz.

El archivo `index.html` de la raíz es el menú del curso. Cada clase se publica en su propia ruta:

- Portada: https://ivanrenatoc.github.io/UTFSM-econometria/
- Clase 1: https://ivanrenatoc.github.io/UTFSM-econometria/clase-1-taller/
- Clase 2: https://ivanrenatoc.github.io/UTFSM-econometria/clase-2-taller/
- Clase 3: https://ivanrenatoc.github.io/UTFSM-econometria/clase-3-taller/
- Clase 4: https://ivanrenatoc.github.io/UTFSM-econometria/clase-4-taller/

Los enlaces antiguos a láminas de la clase 1 conservan su destino mediante redirección desde la portada. El antiguo `#clase-2` abre ahora la página independiente de la clase 2. El enlace `#clase-3` abre la página independiente del taller 3.


## Sincronización con GitHub

Esta carpeta está vinculada al repositorio `IvanRenatoC/UTFSM-econometria`. Después de editar una clase, ejecuta su generador, revisa los cambios con `git status` y utiliza una rama y un pull request para incorporarlos a `main`. GitHub Pages publica desde `main`, en la raíz del repositorio.

Los archivos temporales de LaTeX y las cachés de Python se excluyen mediante `.gitignore`; los PDF finales, notebooks, fuentes y recursos de las clases forman parte del material versionado.

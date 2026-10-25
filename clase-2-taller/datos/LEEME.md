# Datos del taller

`wage1.csv`: copia obtenida el 17 de octubre de 2026 de [Rdatasets](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/wooldridge/wage1.csv), distribución de la base del paquete wooldridge. [Documentación original](https://justinmshea.github.io/wooldridge/reference/wage1.html).

526 filas; 24 variables más el índice de distribución `rownames`, eliminado al cargar. No se modificaron valores. País y año: Estados Unidos, 1976; fuente CPS. Salarios en USD nominales por hora. No se afirma representatividad bajo los submuestreos docentes.

SHA-256: `3c60871a79f29417895a164ef7f9ef284065357b216e6b478aa71e2bfd86f38c`.


## Uso en la clase 2

Copia de apoyo de la clase 1. La selección definitiva de la base para las actividades de clase 2 queda pendiente de revisar la cátedra.


## mtcars

Copia de `datasets::mtcars` exportada directamente desde R. Datos de Motor Trend (1974), 32 automóviles de modelos 1973–1974; sin observaciones eliminadas ni simuladas. Fuente: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html . La web usa qsec (segundos para recorrer 1/4 de milla), hp (potencia bruta) y drat (relación de transmisión del eje trasero). El notebook usa `autos <- datasets::mtcars`, sin instalación adicional.


## ceosal1

Copia íntegra exportada a CSV desde https://raw.githubusercontent.com/JustinMShea/wooldridge/master/data/ceosal1.RData . 209 filas y 12 variables, sin filtros ni datos simulados. Documentación: https://justinmshea.github.io/wooldridge/reference/ceosal1.html . La práctica ajusta salary ~ roe; el código utiliza la copia local o carga el paquete oficial wooldridge desde CRAN si no está disponible.

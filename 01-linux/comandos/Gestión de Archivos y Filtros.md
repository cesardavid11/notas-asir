# [Gestión de Archivos y Filtros]

**Fecha:** 2026-08-30
**Categoría:** (Linux)

# Comandos de Visualización y Lectura de Texto

## cat (concatenate)
Muestra todo el contenido de uno o varios archivos de golpe en la consola.

Uso principal: Archivos pequeños o concatenar archivos.

Ejemplo: cat archivo.txt


## less 
Abre un paginador interactivo que permite navegar por el archivo con las flechas, buscar 
palabras (/palabra) y salir con q.

Uso principal: Archivos grandes donde no quieres que la pantalla se llene de texto.

Ejemplo: less /var/log/syslog


## head 
Muestra por defecto las primeras 10 líneas de un archivo.

Uso principal: Ver la estructura o el encabezado de un fichero.

Ejemplo: head -n 20 archivo.txt (muestra 20 líneas).


## tail 
Muestra por defecto las últimas 10 líneas de un archivo.

El parámetro clave: -f (follow) mantiene el comando abierto esperando nuevas líneas en tiempo real.

Uso principal: Monitorear registros/logs en vivo mientras ocurren eventos en el sistema.

Ejemplo: tail -f /var/log/syslog


# Filtrado y Métricas

##grep 
Busca patrones o palabras dentro del texto e imprime solo las líneas coincidentes.

-i: Ignora mayúsculas/minúsculas.

-v: Invierte la búsqueda (muestra las líneas que no coinciden).

-E: Permite expresiones regulares avanzadas.

Ejemplo: grep -i "error" /var/log/syslog


## wc (Word Count) 
Cuenta líneas, palabras o bytes de una entrada.

-l: Cuenta únicamente el número de líneas.

Ejemplo: wc -l lista.txt


# Operadores de Redirección

Por defecto, los comandos leen de la entrada estándar (teclado) y escriben en la salida 
estándar (pantalla). Las redirecciones cambian este flujo hacia o desde archivos.

## > (Redirección destructiva/Sobrescritura) 
Envía la salida de un comando a un archivo. Si el archivo existe, borra su contenido 
y escribe el nuevo.

Ejemplo: echo "Hola Mundo" > mensaje.txt

## >> (Redirección acumulativa/Anexión) 
Envía la salida de un comando al final de un archivo sin borrar lo que ya contiene.

Ejemplo: echo "Nueva línea" >> mensaje.txt


#El Tubo o Pipe (|)

El carácter tubería | toma la salida estándar del comando a su izquierda y la convierte 
directamente en la entrada estándar del comando a su derecha. Te permite encadenar utilidades 
simples para crear procesamiento complejo.

Comando A (genera texto)  --->  |  --->  Comando B (filtra/procesa)
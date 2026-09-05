# Comando awk

**Fecha:** 2026-09-05
**Categoría:** (Linux)

---

## ¿Que es awk?

awk es un lenguaje de programación y herramienta de línea de comandos en Linux diseñado principalmente para procesar, filtrar y analizar texto estructurado por columnas o campos (como archivos CSV, logs del sistema o salidas de otros comandos)

A diferencia de comandos como grep (que busca líneas completas) o sed (que modifica texto), awk comprende la estructura del texto por columnas y te permite realizar operaciones lógicas, cálculos matemáticos y formateo de reportes.

---

## Concepto clave de awk

### Campos (Columnas): 
awk divide cada línea en columnas usando espacios o tabulaciones por defecto.

* **$0:** Representa la línea completa.

* **$1, $2, $3:** Representan la primera, segunda y tercera columna, respectivamente.

* **$NF:** Representa la última columna.

### Separador de campos (-F):
Define qué carácter separa las columnas (por ejemplo, -F',' para archivos CSV).

### Variables internas útiles:

* NR: Número de registro o fila actual (Number of Record).

* NF: Número total de campos o columnas en la fila actual (Number of Fields).

**Sintaxis básica:**

```
awk -F'separador' 'patrón { acción }' archivo
```

--- 

## Ejemplos prácticos

1. Imprimir columnas específicas
Dado un comando que muestra archivos, si solo quieres ver el tamaño (columna 5) y el nombre (columna 9):

```
ls -l | awk '{print $5, $9}'
```

2. Usar un separador personalizado (/etc/passwd)
El archivo /etc/passwd usa : como separador. Para listar solo los usuarios (columna 1) y sus shells (columna 7):

```
awk -F':' '{print $1, $7}' /etc/passwd
```

3. Filtrar datos con condiciones
Mostrar las líneas del archivo /etc/passwd donde el UID (columna 3) sea mayor o igual a 1000:

```
awk -F':' '$3 >= 1000 {print $1, $3}' /etc/passwd
```

4. Filtrar por coincidencia de texto (Patrón)
Imprimir las líneas que contengan la palabra "Error" en un archivo de registros:

```
awk '/Error/ {print $0}' /var/log/syslog
```

5. Realizar cálculos (Sumar una columna)
Sumar el tamaño total de todos los archivos listados por ls -l:

```
ls -l | awk '{sum += $5} END {print "Total bytes:", sum}'
```

6. Usar los bloques BEGIN y END
BEGIN se ejecuta antes de procesar el archivo y END se ejecuta después de terminar.

```
awk 'BEGIN {print "--- INICIO DEL REPORTE ---"} {print $1, $3} END {print "--- FIN DEL REPORTE ---"}' datos.txt
```


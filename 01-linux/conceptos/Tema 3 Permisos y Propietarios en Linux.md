# Permisos y Propietarios

**Fecha:** 2026-08-30
**Categoría:** (Linux)

---

## ¿Qué son los  Permisos y Propiedades?

En Linux y sistemas Unix, los permisos determinan qué acciones puede realizar 
un usuario sobre un archivo o directorio. Para representarlos de forma clara y 
precisa, se utilizan dos formatos equivalentes: la notación simbólica (rwx) y 
la notación octal o numérica (4-2-1).

## La Notación Simbólica (rwx)

| Notación Simbólica | Operación / Suma | Valor Octal | Descripción de Permisos |
| :---: | :---: | :---: | :--- |
| `---` | 0 + 0 + 0 | **0** | Sin ningún permiso |
| `--x` | 0 + 0 + 1 | **1** | Solo ejecución |
| `-w-` | 0 + 2 + 0 | **2** | Solo escritura |
| `-wx` | 0 + 2 + 1 | **3** | Escritura y ejecución |
| `r--` | 4 + 0 + 0 | **4** | Solo lectura |
| `r-x` | 4 + 0 + 1 | **5** | Lectura y ejecución |
| `rw-` | 4 + 2 + 0 | **6** | Lectura y escritura |
| `rwx` | 4 + 2 + 1 | **7** | Lectura, escritura y ejecución (Acceso total) |


## Las Tres Capas de Usuarios
Cada archivo o directorio asigna estos permisos a tres conjuntos de usuarios 
distintos, siempre en este orden exacto:

* u (User/Owner): El usuario propietario del archivo.

* g (Group): Los usuarios que pertenecen al grupo propietario del archivo.

* o (Others): Cualquier otro usuario del sistema.

* Si ejecutas el comando ls -l en la terminal, verás un bloque de 10 caracteres.


## La Notación Octal o Numérica (4-2-1)
La notación numérica convierte las letras rwx en un sistema binario 
(donde 1 significa concedido y 0 denegado). Cada letra tiene asignado 
un valor numérico equivalente en base octal:

* Lectura (r) = 4  (Binario: 100)

* Escritura (w) = 2  (Binario: 010)

* Ejecución (x) = 1  (Binario: 001)

Para calcular el permiso de cada grupo (Propietario, Grupo, Otros), 
simplemente sumas los valores:

| Notación Simbólica | Binario | Operación / Suma | Valor Octal | Descripción de Permisos |
| :---: | :---: | :---: | :---: | :--- |
| `---` | `000` | 0 + 0 + 0 | **0** | Sin ningún permiso concedido |
| `--x` | `001` | 0 + 0 + 1 | **1** | Solo ejecución / acceso a directorio |
| `-w-` | `010` | 0 + 2 + 0 | **2** | Solo escritura / modificación |
| `-wx` | `011` | 0 + 2 + 1 | **3** | Escritura y ejecución |
| `r--` | `100` | 4 + 0 + 0 | **4** | Solo lectura / visualización |
| `r-x` | `101` | 4 + 0 + 1 | **5** | Lectura y ejecución (Estándar scripts/programas) |
| `rw-` | `110` | 4 + 2 + 0 | **6** | Lectura y escritura (Estándar documentos) |
| `rwx` | `111` | 4 + 2 + 1 | **7** | Lectura, escritura y ejecución (Acceso total) |

---

## Comandos de Modificacion de permisos

### Comando chmod: Modificación de Permisos
El comando chmod (change mode) permite alterar los permisos de lectura (r), escritura
(w) y ejecución (x) asignados al propietario (u), al grupo (g) y a otros usuarios (o).

Cambia los permisos asignando valores numéricos exactos para cada entidad: [Propietario][Grupo][Otros].

Ejemplos: 

* Establece los permisos de lectura, escritura y ejecucuion al propietario, y solo de 
lectura y ejecucion al grupo  y otros

chmod 755 archivo.sh

* Otorga permisos de ejecución (+x) únicamente al propietario (u)

chmod u+x script.sh

* Quita el permiso de escritura (-w) tanto al grupo como a otros usuarios

chmod go-w documento.docx


### Comando chown (Change Owner)
El comando chown cambia el usuario propietario y, opcionalmente, el grupo propietario de 
un archivo o directorio. Por razones de seguridad, esta operación generalmente requiere 
privilegios de superusuario (sudo).

Ejemplos: 

* Cambia solo el usuario propietario a "carlos"

sudo chown carlos documento.pdf

* Cambia el usuario propietario a "carlos" y el grupo a "desarrollo" al mismo tiempo

sudo chown carlos:desarrollo proyecto/

* Cambia recursivamente (-R) el propietario y grupo de un directorio y todo su contenido

sudo chown -R carlos:desarrollo /var/www/html/


### Comando chgrp (Change Group)
El comando chgrp está dedicado exclusivamente a modificar el grupo propietario. Puede 
ser utilizado por el propietario del archivo si este pertenece al grupo de destino, o 
por el administrador.

Ejemplos:

* Cambia el grupo propietario a "analytics"

chgrp analytics datos.csv

* Cambia el grupo de forma recursiva en todo un directorio

chgrp -R analytics /datos/reportes/

---

### La Máscara de Permisos: umask
Cuando se crea un archivo o directorio nuevo, el sistema operativo le asigna permisos 
predeterminados. El comando umask (user file-creation mode mask) define qué permisos 
se deben sustraer o bloquear a partir del permiso máximo base del sistema.
 

### Permisos Máximos Base del Sistema
Por razones de seguridad, el núcleo de Linux nunca otorga permisos de ejecución (x)
por defecto a archivos de texto o datos ordinarios:

Permiso base máximo para Archivos: 666 (rw-rw-rw-)

Permiso base máximo para Directorios: 777 (rwxrwxrwx) (requiere ejecución 'x' 
para permitir navegación interna)
 

### Cálculo del Permiso Efectivo
La fórmula para calcular los permisos finales de un elemento nuevo es la resta lógica 
entre el permiso base y el valor de la umask:

Permiso Final = Permiso Base - Valor de umask

A continuación se analiza un ejemplo común con una máscara umask 022:

| Tipo de Elemento | Permiso Base | Máscara (umask) | Permiso Resultante | Representación Simbólica |
| :--- | :--- | :--- | :--- | :--- |
| **Archivo nuevo** | 666 | 022 | **644** | `rw- r-- r--` |
| **Directorio nuevo** | 777 | 022 | **755** | `rwx r-x r-x` |


Otro caso práctico: Si se configura una máscara restrictiva umask 077 (privacidad total):

Archivos nuevos: 666 - 077 = 600 (rw-------) - Lectura/Escritura solo para el dueño.

Directorios nuevos: 777 - 077 = 700 (rwx------) - Acceso total solo para el dueño.


### Uso del comando umask en la Terminal

* Consultar el valor actual de umask

umask

* Establecer temporalmente una nueva máscara

umask 027

* Consultar la máscara en notación simbólica (muestra los permisos permitidos)

umask -S


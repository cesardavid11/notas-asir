# [Permisos y Propietarios]

**Fecha:** 2026-08-30
**Categoría:** (Linux)

## ¿Qué es?

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

u (User/Owner): El usuario propietario del archivo.

g (Group): Los usuarios que pertenecen al grupo propietario del archivo.

o (Others): Cualquier otro usuario del sistema.

Si ejecutas el comando ls -l en la terminal, verás un bloque de 10 caracteres como este:


- r w x r - x r - -
│ └──┬──┘ └──┬──┘ └──┬──┘
│    │       │       └ Others (Otros): r-- (Solo lectura)
│    │       └──────── Group (Grupo): r-x (Lectura y ejecución)
│    └──────────────── Owner (Propietario): rwx (Todos los permisos)
└───────────────────── Tipo de nodo (- para archivo, d para directorio)


## La Notación Octal o Numérica (4-2-1)
La notación numérica convierte las letras rwx en un sistema binario 
(donde 1 significa concedido y 0 denegado). Cada letra tiene asignado 
un valor numérico equivalente en base octal:

Lectura (r) = 4  (Binario: 100)

Escritura (w) = 2  (Binario: 010)

Ejecución (x) = 1  (Binario: 001)

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


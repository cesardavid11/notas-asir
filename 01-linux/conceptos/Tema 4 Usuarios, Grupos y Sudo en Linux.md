# Usuarios, Grupos y Sudo

**Fecha:** 2026-08-30
**Categoría:** (Linux)

---

## Usuario (User)
En los sistemas operativos tipo Unix y Linux, un usuario es una entidad lógica creada para representar a un individuo, un servicio o un proceso informático dentro del sistema. Los usuarios son la base del modelo de seguridad y control de acceso del sistema operativo.

Identificación del Sistema: Cada usuario cuenta con un nombre único (username) para los humanos, pero internamente el sistema operativo lo identifica mediante un número entero denominado UID (User ID). El usuario superadministrador (root) siempre tiene el UID 0.

Mecanismo de Aislamiento: Los usuarios garantizan que un proceso o persona no pueda alterar, leer ni borrar los archivos de otros usuarios sin una autorización explícita.

### Tipos de Usuarios:

* Usuario Root (root): Tiene acceso absoluto y sin restricciones a todos los archivos, comandos y configuraciones del sistema.

* Usuarios Regulares: Cuentan con un directorio personal (/home/usuario), donde pueden crear y editar archivos. Tienen permisos limitados para modificar la configuración global del sistema o los archivos de otros usuarios.

* Usuarios de Sistema (Servicios): Cuentan con UID bajos (habitualmente entre 1 y 999) y se utilizan para ejecutar servicios o demonios en segundo plano (como nginx, mysql o sshd) sin otorgarles acceso a un intérprete de comandos interactivo (shell), minimizando así el impacto en caso de una brecha de seguridad.

## Grupo (Group)
Un grupo es una unidad organizativa que agrupa a múltiples usuarios bajo un mismo conjunto de permisos de acceso sobre archivos, directorios o recursos del sistema.

Gestión Eficiente: En lugar de asignar permisos individuales archivo por archivo a cada usuario, el administrador del sistema asigna permisos a un grupo determinado y luego añade los usuarios necesarios a dicho grupo.

Identificador de Grupo (GID): Al igual que los usuarios con el UID, cada grupo posee un número de identificación único llamado GID (Group ID).

### Tipos de Membresía de Grupo:

* Grupo Primario: Cada usuario pertenece obligatoriamente a un grupo primario, definido al momento de crear la cuenta. Todos los archivos nuevos que cree el usuario pertenecerán por defecto a este grupo. En la mayoría de las distribuciones modernas, al crear un usuario se crea automáticamente un grupo primario con su mismo nombre (modelo Private Group Scheme).

* Grupos Secundarios (o Complementarios): Un usuario puede pertenecer a múltiples grupos secundarios adicionales. Esto le otorga permisos de lectura, escritura o ejecución sobre los recursos compartidos pertenecientes a esos grupos (por ejemplo, el grupo docker, audio, video o sudo).


## Sudo (Superuser Do)
sudo es una utilidad de seguridad de software que permite a un usuario del sistema ejecutar programas o comandos con los privilegios de seguridad de otro usuario (por defecto, los del superadministrador root), de forma controlada y auditable.

El Principio del Menor Privilegio: Permite a los administradores trabajar en el día a día con cuentas de usuario normales de bajo riesgo, escalando privilegios a nivel de root únicamente durante los segundos o minutos que toma ejecutar una tarea específica. Esto previene errores destructivos accidentales que podrían ocurrir al estar permanentemente autenticado como root.

Mecanismo de Autenticación: A diferencia del comando su (switch user), que requiere conocer la contraseña de la cuenta destino (normalmente la contraseña del propio root), sudo requiere que el usuario introduzca su propia contraseña personal. Esto garantiza la trazabilidad y evita tener que compartir la contraseña maestra entre varios administradores.

Control Fino y Registro (Logging): Mediante la regla de configuración en /etc/sudoers, es posible restringir exactamente qué comandos o scripts específicos puede ejecutar un usuario determinado mediante sudo. Además, cada intento de ejecución de sudo (sea exitoso o fallido) queda registrado en los archivos de registro del sistema (/var/log/auth.log o /var/log/secure), generando un historial completo de auditoría.

---

## Comandos de Gestión

### useradd: 
Crea un usuario nuevo en el sistema 

(ej. sudo useradd -m username para crear también su carpeta personal /home).


### passwd:
Establece o cambia la contraseña de un usuario 

(ej. sudo passwd username).


### groupadd: 
Crea un nuevo grupo en el sistema 

(ej. sudo groupadd nombre_grupo).

### /etc/sudoers:
Archivo de configuración que define quién puede usar sudo y qué comandos puede ejecutar. Para editarlo de forma segura sin romper la sintaxis del sistema, se debe usar siempre el comando visudo.
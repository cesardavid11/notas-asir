# Estructura del Sistema de Archivos

**Fecha:** 2026-08-29
**Categoría:** (Linux)

---

## ¿Qué es la Estructura del sistema de Archivos?

En Linux, la estructura del sistema de archivos se organiza como un único árbol invertido jerárquico
que parte de una raíz principal llamada / (root). A diferencia de Windows (donde existen letras de
unidad como C:, D:), en Linux todos los discos, particiones y dispositivos se montan en algún punto
dentro de esta única jerarquía. Esta organización está estandarizada bajo el patrón FHS (Filesystem
Hierarchy Standard).

### bin (Enlace simbólico a usr/bin) 

Contiene los ejecutables y comandos esenciales del sistema que pueden usar todos los usuarios (ej. ls, cd, cp, mv).


### boot
Guarda todos los archivos necesarios para el arranque del sistema operativo, incluyendo el kernel de Linux (vmlinuz) 
y los archivos de imagen del disco RAM inicial (initrd.img).


### dev (devices)
Aloja los archivos especiales de dispositivos. En Linux todo se trata como un archivo; aquí se representan discos duros
(sda, nvme), teclados, ratones, /dev/null, etc.


### etc
Almacena todos los archivos de configuración global del sistema operativo y de los programas instalados 
(ej. configuración de red, usuarios /etc/passwd, servicios web).


### home 
Contiene los directorios personales de los usuarios del sistema (excepto el administrador). Por ejemplo: /home/cesar.
Aquí guardas tus descargas, documentos y configuraciones personales.


### lib / lib64 (Enlaces simbólicos a usr/lib y usr/lib64) 
Contienen las librerías compartidas necesarias para que se ejecuten los binarios del sistema (equivalentes a los 
archivos .dll en Windows) y los módulos del kernel.


### lost+found 
Directorio de recuperación utilizado por la herramienta fsck para guardar fragmentos de archivos recuperados tras
un apague repentino o fallo en el sistema de archivos.


### media 
Punto de montaje automático para medios extraíbles que conecta el usuario (pendrives USB, unidades de CD/DVD, discos 
externos).


### mnt (mount) 
Punto de montaje temporal donde los administradores pueden montar manualmente sistemas de archivos o particiones 
adicionales.


### opt (optional) 
Destinado a la instalación de paquetes de software de terceros o aplicaciones independientes que no siguen la estructura
estándar (ej. Google Chrome, paquetes de software empresarial).


### proc 
Sistema de archivos virtual (existente solo en memoria RAM) que contiene información en tiempo real sobre los procesos
en ejecución y los recursos del kernel.


### root 
El directorio personal del usuario administrador (root). Se mantiene separado de /home para asegurar que se pueda
acceder a él aunque /home esté montado en una partición distinta que falle.


### run 
Almacena datos temporales sobre el estado del sistema desde el último arranque (ID de procesos en ejecución PIDs,
sockets, variables de entorno de tiempo de ejecución).


### sbin (Enlace simbólico a usr/sbin) 
Contiene binarios y herramientas de administración del sistema reservadas principalmente para el superusuario root
(ej. fdisk, iptables, reboot).


## #srv (service) 
Aloja datos específicos de servicios que ofrece el sistema, como directorios de un servidor web (/srv/www) o un
servidor FTP.


### sys 
Sistema de archivos virtual similar a /proc que expone información estructurada del kernel sobre los dispositivos 
de hardware, controladores y configuración del bus del sistema.


### tmp (temporary) 
Espacio para archivos temporales creados por programas o por el usuario. Generalmente se limpia automáticamente 
al reiniciar el sistema.


### usr (User System Resources) 
Contiene la mayoría de las aplicaciones y utilidades del sistema de lectura solo para los usuarios. Es una 
sub-jerarquía que incluye sus propios directorios /usr/bin, /usr/lib, /usr/share, etc.


### var (variable) 
Guarda archivos de contenido variable y cambiante a lo largo del tiempo, como archivos de registro (logs en /var/log),
colas de impresión, bases de datos o correo local.
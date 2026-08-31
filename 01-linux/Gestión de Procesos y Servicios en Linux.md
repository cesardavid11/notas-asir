# [Gestión de Procesos y Servicios]

**Fecha:** 2026-08-30
**Categoría:** (Linux)

# Monitorización de Procesos
Un proceso es cualquier programa o tarea en ejecución. En Linux, cada proceso 
tiene un identificador único denominado PID (Process ID).


## ps aux (Snapshot / Foto fija) 
Muestra una lista detallada de todos los procesos en ejecución en el sistema 
en un instante específico.

a: Muestra procesos de todos los usuarios.

u: Muestra información detallada del usuario (CPU, Memoria, PID).

x: Incluye procesos sin terminal (procesos en segundo plano o del sistema).

Ejemplos:

 Ver todos los procesos en el sistema
ps aux

 Filtrar un proceso específico usando grep (ej. buscar el navegador Firefox)
ps aux | grep firefox


## top (Monitor interactivo básico) 
Muestra en tiempo real el consumo de CPU, memoria y los procesos más pesados del sistema.

Ejecución: top

Comandos útiles dentro de top: 
Presiona q para salir k para matar un proceso, o P para ordenar por consumo de CPU.


## htop (Monitor interactivo avanzado) 
Una versión mejorada y visual de top con barras de colores, soporte para ratón y árbol 
de procesos. (Puede requerir instalación: sudo apt install htop o sudo dnf install htop).

Ejecución: htop

Comandos útiles: 
Usa las teclas F1 a F10 (por ejemplo, F9 para enviar señales/matar procesos o F3 para buscar).


# Finalización de Procesos (kill)
Cuando un proceso no responde o se necesita detener, se envía una señal del sistema para 
finalizarlo.

## kill 
Detiene un proceso individual especificando su número de PID.

SIGTERM (señal 15 por defecto): Solicita la finalización ordenada del proceso.

SIGKILL (señal 9): Forzado inmediato. Se usa cuando el proceso está colgado.

Ejemplo:

 Terminar un proceso de forma suave (PID: 1234)
kill 1234

 Forzar la finalización inmediata de un proceso (PID: 1234)
kill -9 1234


## killall 
Detiene todos los procesos que coincidan con un nombre de programa, en lugar 
de usar su PID.

Ejemplo:

 Cierra todas las instancias abiertas del proceso "nginx"
killall nginx

 Forzar el cierre de todas las instancias de "firefox"
killall -9 firefox


# Control de Servicios con systemctl
Un servicio (o demonio) es un proceso que se ejecuta en segundo plano sin intervención 
directa del usuario (por ejemplo, un servidor web o de base de datos). En la mayoría 
de distros modernas se gestionan con systemd mediante la orden systemctl.


## status 
Muestra si el servicio está activo (running), detenido o con errores.

Ejemplo:

sudo systemctl status nginx


## start 
Inicia un servicio que está detenido (solo para la sesión actual).

Ejemplo:

sudo systemctl start nginx


## stop 
Detiene un servicio en ejecución.

Ejemplo:

sudo systemctl stop nginx


## restart 
Reinicia el servicio (útil tras aplicar cambios en un archivo 
de configuración).

Ejemplo:

sudo systemctl restart nginx


## enable 
Configura el servicio para que se inicie automáticamente cuando 
arranque el sistema.

Ejemplo:

sudo systemctl enable nginx


## disable 
Evita que el servicio se inicie automáticamente en el arranque.

Ejemplo:

sudo systemctl disable nginx
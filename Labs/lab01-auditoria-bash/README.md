# 🛡️ Lab 01: Script de Auditoria del Sistema en Bash

> **Proyecto de Automatizacion en Linux / SysAdmin**

> Scrip en Bash diseñado para analizar la seguridad, recursos y logs de un servidor Linux, gererando un reporte tecnico detallado en un archivo de texto.

---

## 🚀 Funcionalidades

El script realiza de forma automatica las siguientes comprobaciones:

* **Gestion de Usuarios:** Filtra y muestra los usuarios locales con shell interactiva activa ('/etc/passwd').
* **Auditoria de Red:** Lista todos los puertos TCP y UDP en escucha pasiva ('ss')
* **Estado de Disco:** Analiza el porcentaje de uso de la particion raiz ('/') e incluye logica condicional que emite una aleta si se supera el 85% de capacidad.
* **Registro de Seguridad (SSH):** Extrae los Ultimos 5 intentos fallidos de autenticacion en el servicio SSH mediante 'journalctl' o '/var/log/auth.log'.
* **Monitoreo de Memoria:** Muestra el espacio de memoria RAM disponible en Gigabytes (GB) calculando con 'awk'

---

## 💻 Requisitos Previos

* **Sistema Operativo:** GNU/LINUX (Probando en Debian 12 / Ubuntu)
* **Interprete:** Bash Shell
* **Permisos:** Se requiere acceso con privilegios de administrador ('sudo') para la lectura de eventos del sistema mediante 'journalctl'.

---

## ⚙️ Instalacion y Ejecucion 

1. **Clonar el repositorio o descargar el script:**

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio/Labs/Lab01-auditoria-bash

2. **Otorgar permisos de ejecucion al archivo:**

chmod +x auditoria.sh

3. **Ejecutar el script con privilegios de administrador:**

sudo ./auditoria.sh

---

## 📊 Ejemplo de Salida Generada

El script genera de manera autónoma el archivo reporte_auditoria.txt. A continuación se muestra un fragmento del informe obtenido:

```
========================================
  REPORTE DE AUDITORÍA DE SISTEMA
  Fecha: 2026-09-03 19:21:03
========================================

[1] USUARIOS CON SHELL ACTIVA
root
cesar
guerra

[2] PUERTOS TCP/UDP ABIERTOS (LISTEN)
127.0.0.1:631
0.0.0.0:22
0.0.0.0:53

[3] ESTADO DEL DISCO PRINCIPAL (/)
Uso actual del disco: 38%
Estado del disco dentro de los límites normales.

[4] ÚLTIMOS INTENTOS FALLIDOS DE ACCESO SSH
Sep 01 16:54:29 debian sshd-session[13591]: Failed password for invalid user cesaar from 172.24.128.242 port 37516 ssh2

[5] MEMORIA RAM LIBRE
Espacio de RAM Libre: 2.55 GB
```

## 👤 Autor

* Cesar-Preparacion Grado Superior ASIR
* GitHub: @cesarguerra11
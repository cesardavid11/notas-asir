# Puertos, Sockets y Servicios

**Fecha:** 2026-09-02
**Categoría:** (Redes)

---

## Conceptos fundamentales: Puerto, Socket y Servicio
Para entender cómo se comunican las aplicaciones en red, imagina un edificio de oficinas:

* Dirección IP: Es la dirección postal del edificio. Identifica de forma única a una máquina en la red.

* Puerto: Es el número de oficina dentro del edificio. Un número entre 1 y 65535 que permite a la red saber a qué aplicación concreta va dirigida la información.

* Socket: Es la combinación de una Dirección IP y un Puerto (por ejemplo, 192.168.1.50:80). Representa el punto final exacto de una conexión de red entre dos aplicaciones.

* Servicio (o Demonio): Es el programa o proceso que está ejecutándose en segundo plano dentro del sistema (como Apache, Nginx o SSH) y que se queda "escuchando" en un puerto específico a la espera de peticiones.


## Puertos bien conocidos y esenciales

Los puertos se dividen en rangos definidos por la IANA (Internet Assigned Numbers Authority). Los puertos bien conocidos van del 0 al 1023 y requieren privilegios de superusuario (root) para abrirse.

**Puertos solicitados:**

* 21 (FTP): Transferencia de archivos sin cifrar.

* 22 (SSH): Acceso remoto seguro mediante consola encriptada y SFTP.

* 53 (DNS): Resolución de nombres de dominio a direcciones IP (opera principalmente en UDP).

* 80 (HTTP): Tráfico web estándar sin cifrar.

* 443 (HTTPS): Tráfico web seguro cifrado mediante SSL/TLS.


**Tabla de puertos esenciales en la administración de sistemas:**

| Puerto | Protocolo | Servicio / Software Común | Descripción y Uso Principal |
| :---: | :---: | :--- | :--- |
| **20 / 21** | TCP | FTP (*File Transfer Protocol*) | Transferencia de archivos entre cliente y servidor (Canal de datos/control). |
| **22** | TCP | SSH (*Secure Shell*) / SFTP | Administración remota segura vía CLI y transferencia cifrada de archivos. |
| **23** | TCP | Telnet | Administración remota en texto plano (en desuso por falta de seguridad). |
| **25** | TCP | SMTP (*Simple Mail Transfer Protocol*) | Envío de correo electrónico entre servidores de correo. |
| **53** | UDP/TCP | DNS (*Domain Name System*) | Resolución de nombres de dominio a direcciones IP (UDP para consultas, TCP para transferencias de zona). |
| **67 / 68** | UDP | DHCP (*Dynamic Host Configuration Protocol*) | Asignación dinámica de direcciones IP en la red local (67: Servidor, 68: Cliente). |
| **80** | TCP | HTTP (*Hypertext Transfer Protocol*) | Tráfico web estándar sin cifrado. |
| **110** | TCP | POP3 (*Post Office Protocol v3*) | Descarga e inspección de correos electrónicos desde un cliente local. |
| **123** | UDP | NTP (*Network Time Protocol*) / Chrony | Sincronización precisa de la hora e intervalo del sistema. |
| **143** | TCP | IMAP (*Internet Message Access Protocol*) | Gestión y lectura de correo directamente en el servidor. |
| **161 / 162** | UDP | SNMP (*Simple Network Management Protocol*) | Monitoreo y gestión de dispositivos de red (161: Consultas, 162: Traps/Alertas). |
| **389** | TCP/UDP | LDAP (*Lightweight Directory Access Protocol*) | Servicio de directorio para autenticación centralizada de usuarios. |
| **443** | TCP | HTTPS (*HTTP Secure / SSL-TLS*) | Tráfico web cifrado y seguro mediante certificados SSL/TLS. |
| **465 / 587** | TCP | SMTPS / SMTP Submission | Envío seguro de correos cifrados por parte de clientes de correo. |
| **636** | TCP | LDAPS (*LDAP Secure*) | Servicio de directorio seguro cifrado mediante SSL/TLS. |
| **993** | TCP | IMAPS (*IMAP Secure*) | Recuperación y gestión de correo electrónico mediante conexión cifrada. |
| **995** | TCP | POP3S (*POP3 Secure*) | Descarga de correo de forma cifrada mediante SSL/TLS. |

---

## Análisis de puertos y conexiones con ss y netstat
Aunque históricamente se usaba netstat, actualmente está obsoleto (deprecated) en la mayoría de distribuciones Linux. La herramienta moderna y rápida para esta función es ss (Socket Statistics).

### El comando ss -tulpn
Es el comando estándar para ver qué puertos están abiertos y escuchando en el sistema:

sudo ss -tulpn

**Desglose de las opciones:**

* -t (TCP): Muestra sockets TCP.

* -u (UDP): Muestra sockets UDP.

* -l (Listening): Muestra únicamente los puertos que están en modo escucha (abiertos a conexiones).

* -p (Processes): Muestra el proceso y PID al que pertenece cada socket (requiere sudo).

* -n (Numeric): Muestra números de puertos e IP directos en lugar de intentar resolver los nombres de los servicios (hace el comando instantáneo).

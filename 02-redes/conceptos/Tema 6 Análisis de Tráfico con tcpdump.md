# Servicios Fundamentales DHCP y DNS

**Fecha:** 2026-09-03
**Categoría:** (Redes)

Para capturar tráfico en servidores sin interfaz gráfica, tcpdump es la herramienta estándar. Requiere permisos de superusuario (sudo).

---

## Comandos esenciales

* Listar interfaces disponibles:

sudo tcpdump -D

* Capturar en una interfaz específica:

sudo tcpdump -i eth0

* Capturar por IP de origen o destino:

sudo tcpdump -i eth0 host 192.168.1.50

* Capturar por puerto (ej. HTTP/HTTPS o SSH):

sudo tcpdump -i eth0 port 80
sudo tcpdump -i eth0 port 443

* Guardar la captura en un archivo .pcap (para analizar luego con Wireshark):

sudo tcpdump -i eth0 -w captura.pcap

* Leer un archivo .pcap previamente guardado:

tcpdump -r captura.pcap

## Flags útiles de visualización

* -n	No resuelve nombres de dominio/IPs (muestra números, acelera la captura).

* -nn	No resuelve nombres de dominio ni nombres de puertos (ej. muestra 80 en lugar de http).

* -v / -vv	Muestra información más detallada (verbose).

* -A	Muestra el contenido del paquete en texto ASCII (útil para inspeccionar tráfico HTTP no cifrado).

* -X	Muestra el contenido en Hexadecimal y ASCII.

* -c N	Detiene la captura automáticamente tras recibir N paquetes (ej. tcpdump -c 10).


**Ejemplo combinado de diagnóstico rápido**
Capturar 20 paquetes del puerto 80 sin resolver nombres y mostrando el contenido ASCII:

sudo tcpdump -i eth0 -nn -A port 80 -c 20
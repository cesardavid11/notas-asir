# Comandos de Diagnóstico de Red

**Fecha:** 2026-09-01
**Categoría:** (Redes)

---

Las herramientas de diagnóstico de red permiten aislar la capa del modelo OSI donde ocurre una falla, dividiéndose principalmente en dos grupos: conectividad/ruta (Capas 3 y 4) y resolución de nombres (DNS / Capa 7).

## Comandos de Conectividad y Ruta

### ping
Mide la alcanzabilidad de un host y el tiempo de ida y vuelta de los paquetes (RTT - Round Trip Time) mediante mensajes ICMP Echo Request y Echo Reply.

Uso básico: ping google.com o ping 8.8.8.8

**Lectura clave:**

* RTT (ms): Latencia actual. Un valor muy alto indica congestión en la red.

* Pérdida de paquetes (% loss): Señal directa de problemas físicos, saturación de canal o descarte por firewall.

* TTL (Time to Live): Contador decreciente por cada router que atraviesa. Ayuda a deducir el sistema operativo de destino (Linux suele salir con 64/128, Windows con 128/256).


### traceroute / tracepath
Mapean la ruta que siguen los paquetes desde el origen hasta el destino identificando cada router (salto).

Mecanismo: Incrementan el valor TTL de los paquetes a partir de 1. Cuando el TTL de un paquete llega a 0, el router intermedio lo descarta y devuelve un mensaje ICMP Time Exceeded, revelando su IP.

traceroute vs tracepath: traceroute utiliza UDP/ICMP/TCP y puede requerir permisos de superusuario (sudo). tracepath no requiere privilegios elevados y calcula además el MTU (Maximum Transmission Unit) a lo largo de la ruta.

---

## Comandos de Resolución DNS

### nslookup
Herramienta interactiva y multiplataforma clásica para consultar servidores DNS.

Ejemplo: nslookup dominio.com o especificando un DNS particular: nslookup dominio.com 1.1.1.1

Cuándo usarlo: Consultas rápidas para verificar qué IP devuelve un nombre de dominio.

### dig (Domain Information Groper)
Herramienta avanzada en sistemas UNIX/Linux que devuelve la respuesta cruda enviada por los servidores DNS con metadatos extendidos.

Ejemplo: dig @8.8.8.8 dominio.com MX

Lectura clave: Muestra las secciones QUESTION, ANSWER, AUTHORITY y el QUERY TIME (milisegundos que tarda la consulta DNS en responder).

Útil para: Verificar registros específicos (A, AAAA, MX, CNAME, TXT, NS), probar zonas y diagnosticar propagaciones DNS lentas.

### host
Alternativa rápida para búsquedas DNS orientadas a scripts o verificaciones legibles por humanos.

Ejemplo: host -t AAAA dominio.com (consulta directa de registro IPv6) o host 8.8.8.8 (búsqueda inversa PTR).

---

## Troubleshooting de Red

| Síntoma / Fallo detectado | Comando Principal (Linux) | Comando Secundario / Comprobación | Diagnóstico Esperado |
| :--- | :--- | :--- | :--- |
| **No navega por nombre, pero responde el ping a la IP (`8.8.8.8`)** | `dig google.com` | `cat /etc/resolv.conf`<br>o `resolvectl status` | **Fallo de DNS.** Servidor DNS no responde, timeout en la consulta o archivo de resolución mal configurado. |
| **Sin conectividad en la red local ni a la puerta de enlace** | `ping -c 4 127.0.0.1` | `ping -c 4 $(ip route show default \| awk '{print $3}')` | Si falla `127.0.0.1`, la pila TCP/IP local no responde. Si falla el gateway, hay un problema físico, interfaz caída (`ip link`) o falla de DHCP. |
| **Conexión intermitente o lentitud hacia un servidor específico** | `ping -c 50 <IP_Destino>` | `mtr <IP_Destino>` | Muestra porcentaje de paquetes perdidos y variaciones en la latencia (jitter) en tiempo real. |
| **El tráfico se interrumpe antes de llegar al destino** | `tracepath <IP_Destino>` | `traceroute <IP_Destino>` | Muestra en qué salto (router intermedio) se cortan los paquetes o dónde se dispara el tiempo de respuesta. |
| **Registros DNS desactualizados o incoherentes** | `dig +trace <dominio>` | `host -t A <dominio>` | Rastrea la jerarquía DNS desde los Root Servers para diagnosticar propagación o errores en registros específicos. |
| **Servicio/aplicación inaccesible en un puerto específico (ej. 80, 443, 22)** | `nc -zv <IP_Destino> <Puerto>` | `traceroute -T -p <Puerto> <IP_Destino>` | `nc` comprueba si el socket TCP/UDP responde. `traceroute -T` envía SYN de TCP para evaluar si un firewall bloquea la ruta a ese puerto. |
| **Verificación de la tarjeta de red o configuración IP local** | `ip a` (o `ip addr`) | `ip route` | Permite verificar si la interfaz tiene asignada la dirección IP correcta, si está en estado `UP` y cuál es la tabla de ruteo por defecto. |
# [Modelo OSI vs TCP/IP y Direccionamiento]

**Fecha:** 2026-09-01
**Categoría:** (Redes)

# Modelo OSI vs. TCP/IP
El Modelo OSI es una referencia teórica de 7 capas creada por la ISO para estandarizar 
la comunicación en redes, mientras que TCP/IP es la pila práctica de 4 o 5 capas 
utilizada realmente en Internet.

La principal diferencia radica en su enfoque: OSI separa estrictamente la preparación 
de datos (Presentación) y la gestión de sesiones (Sesión) de las aplicaciones, mientras 
que TCP/IP condensa todo ese trabajo directamente en la Capa de Aplicación.

| Característica | Modelo OSI | Modelo TCP/IP (Actual/Híbrido) |
| :--- | :--- | :--- |
| **Nivel** | Teórico / Conceptual | Práctico / Estándar real de Internet |
| **Nº de Capas** | 7 capas | 4 (original) o 5 (modelo de estudio) |
| **Tratamiento de Datos** | Separa Aplicación, Presentación y Sesión | Fusiona las capas 5, 6 y 7 en Aplicación |
| **Desarrollo** | Independiente de los protocolos | Diseñado a la par de los protocolos TCP e IP |


# Direccionamiento y Protocolos por Capa (TCP/IP de 5 Capas)

## 5. Capa de Aplicación
Función: Proporcionar la interfaz de red para las aplicaciones del usuario final.

Tipo de Direccionamiento: Nombres de Dominio (FQDN) y URLs (ej. [www.ejemplo.com](https://www.ejemplo.com)).

PDU: Datos / Mensaje.

Protocolos: HTTP, HTTPS, DNS, DHCP, FTP, SSH, Telnet, SMTP, POP3, IMAP.

Comandos y Herramientas:

curl / wget (peticiones HTTP)

nslookup / dig / host (consultas DNS)

ssh (conexión remota)

## 4. Capa de Transporte
Función: Comunicación extremo a extremo (end-to-end), control de flujo y multiplexación.

Tipo de Direccionamiento: Puertos (0 a 65535, ej. Puerto 80 para HTTP, 443 para HTTPS).

PDU: Segmento (TCP) / Datagrama (UDP).

Protocolos: TCP (orientado a conexión, confiable) y UDP (no orientado a conexión, rápido).

Comandos y Herramientas:

netstat / ss (listar puertos abiertos y conexiones activas)

nc / netcat (auditar o abrir conexiones por puerto)

## 3. Capa de Red (o Internet)
Función: Enrutamiento de paquetes a través de diferentes redes para llegar al destino.

Tipo de Direccionamiento: Direcciones IP (IPv4: 192.168.1.1, IPv6: fe80::1).

PDU: Paquete.

Protocolos: IP (IPv4/IPv6), ICMP (mensajes de control y error), IPsec, IGMP.

Comandos y Herramientas:

ping (diagnóstico de conectividad con ICMP)

traceroute (Linux) / tracert (Windows) (rastreo de saltos IP)

route / ip route (tabla de enrutamiento)

2. Capa de Enlace de Datos
Función: Transmisión de tramas entre nodos dentro de la misma red local (LAN) y control de acceso al medio.

Tipo de Direccionamiento: Dirección MAC (Física/Hardware, ej. 00:1A:2B:3C:4D:5E).

PDU: Trama (Frame).

Protocolos: Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), ARP (resolución de IP a MAC), PPP, VLAN (802.1Q).

Comandos y Herramientas:

arp -a (muestra la tabla ARP que mapea IP con MAC)

ip link / ifconfig (ver la MAC física del adaptador)

1. Capa Física
Función: Transmisión de bits puros sobre el medio físico (cables, ondas de radio, fibra).

Tipo de Direccionamiento: Ninguno (señales eléctricas, ópticas o de radio).

PDU: Bits.

Protocolos/Estándares: 1000BASE-T, DSL, Señales de Radio RF, Conectores RJ-45, Especificaciones de Fibra Óptica.

Comandos y Herramientas:

ethtool (en Linux, para comprobar velocidad del cable, full-duplex, estado físico del puerto).


# ¿Qué es una dirección IP y para que sirve?

Una **dirección de protocolo de Internet (IP)** es el número de identificación único asignado a cada dispositivo conectado a Internet. Una definición de dirección IP es una etiqueta numérica asignada a dispositivos que utilizan Internet para comunicarse. Las computadoras que se comunican a través de Internet o a través de redes locales comparten información a una ubicación específica utilizando direcciones IP.

Las direcciones IP tienen dos versiones o estándares distintos. La dirección del protocolo de Internet versión 4 (IPv4) es la más antigua de las dos, que tiene espacio para hasta 4 mil millones de direcciones IP y está asignada a todas las computadoras. La versión 6 del protocolo de Internet (IPv6) más reciente tiene espacio para billones de direcciones IP, lo que representa la nueva clase de dispositivos además de las computadoras. También hay varios tipos de direcciones IP, incluidas las direcciones IP públicas, privadas, estáticas y dinámicas.

Cada dispositivo con conexión a Internet tiene una dirección IP, ya sea una computadora, computadora portátil, dispositivo IoT o incluso juguetes.  Las direcciones IP permiten la transferencia eficiente de datos entre dos dispositivos conectados, lo que permite que las máquinas en diferentes redes se comuniquen entre sí.


Una dirección IP ayuda a su dispositivo, sea cual sea el acceso a Internet, a encontrar cualquier dato o contenido que se encuentre para permitir su recuperación. 

Las tareas comunes para una dirección IP incluyen la identificación de un host o una red, o la identificación de la ubicación de un dispositivo. Una dirección IP no es aleatoria. La creación de una dirección IP tiene la base de las matemáticas.  La Autoridad de números asignados por Internet (IANA) asigna la dirección IP y su creación. La gama completa de direcciones IP puede ir de 0.0.0.0 a 255.255.255.255.  

Con la asignación matemática de una dirección IP, se puede realizar la identificación única para hacer una conexión a un destino.


## Dirección IP pública

Una dirección IP pública, o dirección IP externa, se aplica al dispositivo principal que las personas utilizan para conectar su red de Internet comercial o doméstica a su proveedor de servicios de Internet (ISP). En la mayoría de los casos, este será el enrutador. Todos los dispositivos que se conectan a un enrutador se comunican con otras direcciones IP utilizando la dirección IP del enrutador.

Conocer una dirección IP externa es crucial para que las personas abran puertos utilizados para juegos en línea, servidores web y de correo electrónico, transmisión de medios y creación de conexiones remotas.  

## Dirección IP privada

Una dirección IP privada, o dirección IP interna, es asignada por una oficina o intranet doméstica (o red de área local) a dispositivos, o por el proveedor de servicios de Internet (ISP). El enrutador de la casa/oficina administra las direcciones IP privadas a los dispositivos que se conectan desde esa red local. Por lo tanto, el enrutador asigna los dispositivos de red de sus direcciones IP privadas a direcciones IP públicas.

Las direcciones IP privadas se reutilizan en múltiples redes, preservando así el valioso espacio de direcciones IPv4 y extendiendo la direccionalidad más allá del límite simple de direccionamiento IPv4 (4,294,967,296 o 2^32).

En el esquema de direccionamiento IPv6, cada dispositivo posible tiene su propio identificador único asignado por el ISP o la organización de red principal, que tiene un prefijo único. El direccionamiento privado es posible en IPv6 y, cuando se utiliza, se denomina direccionamiento local único (ULA).

[ Dispositivo Local ] --(IP Privada: 192.168.1.15)--> [ Router / NAT ] --(IP Pública: 80.34.12.5)--> [ Internet ]

## Dirección IP estática

Todas las direcciones públicas y privadas se definen como estáticas o dinámicas. Una dirección IP que una persona configura y corrige manualmente en la red de su dispositivo se denomina dirección IP estática. Una dirección IP estática no se puede cambiar automáticamente. Un proveedor de servicios de Internet puede asignar una dirección IP estática a una cuenta de usuario. Se asignará la misma dirección IP a ese usuario para cada sesión.

## Dirección IP dinámica

Una dirección IP dinámica se asigna automáticamente a una red cuando se configura un enrutador. E protocolo  de configuración dinámica de host (DHCP) asigna la distribución de este conjunto dinámico de direcciones IP. El DHCP puede ser el enrutador que proporciona direcciones IP a redes a través de una casa u organización.

Cada vez que un usuario inicia sesión en la red, se asigna una nueva dirección IP del grupo de direcciones IP disponibles (actualmente no asignadas). Un usuario puede alternar aleatoriamente entre varias direcciones IP en múltiples sesiones.


## Formato de IPv4

Las direcciones IPv4 son básicamente números binarios de 32 bits que consisten en las dos subdirecciones (identificadores) mencionadas anteriormente que identifican la red y el _host_ a la red, respectivamente, con un límite imaginario que los separa. Una dirección IP, como tal, generalmente se muestra como 4 octetos de números, del 0 al 255, representados en forma decimal en lugar de binaria.

Por ejemplo, la dirección **168.212.226.204** representa el número binario de 32 bits 10101000.11010100.11100010.11001100.

El número binario es importante, porque es lo que determinará a qué clase de red pertenece una dirección IP.

Una dirección IPv4 se expresa típicamente en notación decimal con puntos, representando cada ocho bits (octetos) mediante un número del 1 al 255, separando cada octeto por un punto. Un ejemplo de dirección IPv4 sería así:

|192.168.17.43|
|---|

Las direcciones IPv4 están compuestas de dos partes. Los primeros números de la dirección indican la red, mientras que los últimos especifican el _host_ concreto. La máscara de subred es lo que indica qué parte de una dirección es la de la red y qué parte se refiere al _host_ específico.

Un paquete con una dirección de destino que no se encuentre en la misma red que la dirección de origen se reenviará o enrutará a la red apropiada. Una vez que se encuentre en la red correcta, la parte del _host_ de la dirección determinará a qué interfaz se entrega el paquete.


## Clases de direcciones IP (contexto histórico)


Esto es el sistema **classful** que se usó antes de CIDR (Classless Inter-Domain Routing), que es lo que se usa hoy en día. Aun así, sigue apareciendo en exámenes de certificaciones (Security+, Network+, CCNA) porque ayuda a entender los rangos "por defecto".

| Clase | Rango del primer octeto | Máscara por defecto | Uso principal | Equipos por red (*hosts*) |
| :--- | :--- | :--- | :--- | :--- |
| **A** | `1.0.0.0` a `126.255.255.255` | `255.0.0.0` (`/8`) | Redes extremadamente grandes (gobiernos, multinacionales) | ~$16.7$ millones |
| **B** | `128.0.0.0` a `191.255.255.255` | `255.255.0.0` (`/16`) | Redes medianas (universidades, grandes empresas) | ~$65.535$ |
| **C** | `192.0.0.0` a `223.255.255.255` | `255.255.255.0` (`/24`) | Redes pequeñas (hogares, PYMEs) | $254$ |
| **D** | `224.0.0.0` a `239.255.255.255` | N/A | Reservado para **Multicast** (transmisión a múltiples equipos) | N/A |
| **E** | `240.0.0.0` a `254.255.255.255` | N/A | Reservado para **Investigación y Pruebas** | N/A |

### Nota: La dirección 127.x.x.x no pertenece a ninguna clase útil comercialmente; está reservada para Loopback/localhost (la propia máquina).

Actualmente, las clases están obsoletas y se utiliza CIDR (Classless Inter-Domain Routing, ej. /24, /16), lo que permite subdividir redes (subnetting) con mayor flexibilidad.

El problema del sistema classful es que desperdiciaba direcciones brutalmente. Si una empresa necesitaba 300 IPs, no le servía una clase C (256 direcciones máx), así que le daban una clase B entera (65,536 direcciones) y sobraban casi todas. Por eso en 1993 se introdujo **CIDR**, que permite máscaras arbitrarias (`/25`, `/27`, etc.) para ajustar el tamaño de la subred a lo que realmente se necesita, sin desperdiciar rangos.

## Por qué esto quedó obsoleto


Hoy en día, cuando ves una IP, lo que importa es la máscara/prefijo que la acompaña (`/24`, `/16`...), no la "clase" a la que pertenecería por su primer octeto — pero conviene sabérselo porque los exámenes de certificación aún preguntan por ello, y ayuda a entender por qué `/24` es tan común como "red de casa".

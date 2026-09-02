# Servicios Fundamentales DHCP y DNS

**Fecha:** 2026-09-02
**Categoría:** (Redes)

---

## Conceptos Fundamentales: DHCP y DNS
Son los dos pilares que permiten la comunicación en cualquier red IP sin necesidad de configurar manualmente cada dispositivo:

### DHCP (Dynamic Host Configuration Protocol): 
Protocolo del nivel de aplicación que asigna automáticamente parámetros de red a los clientes (dirección IP, máscara de red, puerta de enlace/gateway y servidores DNS). Trabaja bajo el modelo cliente-servidor mediante el proceso DORA (Discover, Offer, Request, Acknowledge).

### DNS (Domain Name System): 
Sistema de base de datos distribuida y jerárquica que traduce nombres de dominio legibles por humanos (ejemplo.com) en direcciones IP numéricas (192.0.2.1) que los enrutadores entienden.

---

## Flujo Paso a Paso de una Consulta DNS

**Explicación de las Etapas**

* Búsqueda Local (Caché): El navegador o sistema operativo comprueba su caché interna. Si no existe la entrada, envía una consulta recursiva al DNS Resolver (configurado vía DHCP, p. ej. 1.1.1.1 o el router local).

* Servidor Raíz (Root Server .): El Resolver consulta a uno de los 13 grupos de servidores raíz mundiales. El servidor raíz responde con la ubicación del servidor de nivel superior (TLD) correspondiente (.com, .es, .org).

* Servidor TLD (Top-Level Domain): El Resolver pregunta al servidor TLD. Este responde con la IP del servidor autoritativo responsable del dominio específico (ejemplo.com).

* Servidor Autoritativo: Es la fuente definitiva de la zona. Contiene el registro A o AAAA final y devuelve la IP pública real.

* Respuesta y Caché: El Resolver guarda el resultado en su caché local respetando el tiempo de vida (TTL) y entrega la IP al cliente para iniciar la conexión HTTP/TCP.

---

## Despliegue de un Servidor DNS / DHCP Local (dnsmasq)

1. Instalar el servicio en Linux

sudo apt update && sudo apt install dnsmasq -y

Desactiva el resolvedor por defecto de la distribución (systemd-resolved) si está ocupando el puerto 53:

sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved

2. Configurar /etc/dnsmasq.conf

Edita el archivo /etc/dnsmasq.conf con los parámetros esenciales para DNS y DHCP:

```ini
# Interfaz de red donde escuchará dnsmasq
interface=enp0s3

# --- CONFIGURACIÓN DNS ---
# Redirige peticiones no locales a servidores DNS upstream (Cloudflare)
server=1.1.1.1
server=1.0.0.1
# Dominio local predeterminado
domain=lab.local

# --- CONFIGURACIÓN DHCP ---
# Rango de IPs a repartir, máscara de red y tiempo de concesión (lease)
dhcp-range=192.168.1.100,192.168.1.200,255.255.255.0,12h
# Puerta de enlace enviada a los clientes
dhcp-option=option:router,192.168.1.1
# Servidor DNS enviado a los clientes (esta misma máquina)
dhcp-option=option:dns-server,192.168.1.139
```

3. Mapear dominios locales y reiniciar

Agrega registros DNS locales directamente en el archivo /etc/hosts del servidor:

192.168.1.5    servidor.lab.local
192.168.1.50   router.lab.local

Aplica los cambios reiniciando el servicio:

sudo systemctl restart dnsmasq
sudo systemctl status dnsmasq

4. Validar resoluciones con dig y nslookup

Comprueba la resolución de un dominio local configurado:

dig @127.0.0.1 servidor.lab.local +short
Resultado esperado: 192.168.1.139

Comprueba el reenvío recursivo hacia un dominio público externo:

dig @127.0.0.1 google.com
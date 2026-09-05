# Paso 1: Configurar la IP Estática en el Servidor

## Opción A: Desde la Interfaz Gráfica (GUI)

1. Presiona Win + R, escribe ncpa.cpl y pulsa Enter.

![Paso 1](../img/ip-gui-paso1.png)

2. Clic derecho en la tarjeta de red > Propiedades.

![Paso 2](../img/ip-gui-paso2.png)

3. Selecciona Protocolo de Internet versión 4 (TCP/IPv4) > Propiedades.

![Paso 3](../img/ip-gui-paso3.png)

4. Selecciona "Usar la siguiente dirección IP":


* IP: 192.168.10.10

* Máscara: 255.255.255.0

* DNS: 127.0.0.1 (o 192.168.10.10)

![Paso 4](../img/ip-gui-paso4.png)

---

## Opción B: Desde PowerShell (Como Administrador)

```
# Obtener el índice o nombre de la interfaz de red
Get-NetAdapter

# Asignar IP estática y Máscara de subred (cambia 'Ethernet' por el nombre de tu tarjeta)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress "192.168.10.10" -PrefixLength 24

# Configurar el servidor DNS hacia sí mismo
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "127.0.0.1"
```

![alt text](<Configurar la IP Estática en el Servidor desde PowerShell. paso 1.png>)

![alt text](<Configurar la IP Estática en el Servidor desde PowerShell. paso 2.png>)

![alt text](<Configurar la IP Estática en el Servidor desde PowerShell. paso 3.png>)

![alt text](<Configurar la IP Estática en el Servidor desde PowerShell. paso 4 Resultado.png>)
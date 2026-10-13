# Paso 5: Configurar la IP y Unir el Cliente (Windows 10 Pro) al Dominio

## Opción A: Desde la Interfaz Gráfica (GUI) en Windows 10 Pro

1. Asigna IP 192.168.10.20 y DNS 192.168.10.10 en ncpa.cpl.

![Paso 1](../img/cliente-paso1.png)

2. Presiona Win + R, escribe sysdm.cpl (Propiedades del sistema).

![Paso 2](../img/cliente-paso2.png)


3. Pestaña Nombre del equipo > Clic en Cambiar....


4. En Miembro del, selecciona Dominio e ingresa MIDOMINIO.local.

![Paso 4](../img/cliente-paso4.png)


5. Introduce las credenciales del Administrador del Dominio (MIDOMINIO\Administrator) y reinicia.

---

## Opción B: Desde PowerShell en Windows 10 Pro (Ejecutado como Administrador)

```
# 1. Configurar IP y DNS
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress "192.168.10.20" -PrefixLength 24
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.10.10"

# 2. Comprobar conectividad con el dominio
Test-Connection MIDOMINIO.local

# 3. Unir al dominio (Pedirá credenciales de administrador)
Add-Computer -DomainName "MIDOMINIO.local" -Restart
```
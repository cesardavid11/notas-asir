# Lab: Promoción de Windows Server a Domain Controller

**Fecha:** 2026-08-22 (reconstruida)
**Entorno:** VirtualBox, Windows Server, red interna con IP estática

## Contexto

Antes de promover a DC, la VM necesitaba IP estática (no DHCP) porque un DC no puede depender de una IP que cambie. Tuve problemas iniciales con el adaptador NAT de VirtualBox — lo cambié a **bridged** (o red interna con dos adaptadores) para que el cliente Windows 10 pudiera resolver el DNS del DC.

## Pasos

1. Configurar IP estática en el adaptador de red del futuro DC (IPv4 manual, DNS apuntando a sí mismo: 127.0.0.1 o su propia IP).
2. Instalar el rol AD DS:
   ```powershell
   Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
   ```
3. Promocionar el servidor a controlador de un nuevo bosque:
   ```powershell
   Install-ADDSForest -DomainName "midominio.local" -InstallDns
   ```
4. Reinicio automático tras la promoción.
5. Verificar con `dsa.msc` (Active Directory Users and Computers) que el dominio se creó correctamente.

## Troubleshooting

- **Problema**: el cliente no encontraba el dominio al intentar unirse.
  **Causa**: adaptador NAT no permite comunicación DC↔cliente en la misma red interna.
  **Solución**: cambiar a adaptador bridged (o red interna VirtualBox) en ambas VMs y fijar IPs del mismo segmento.

## Qué aprendí

Siempre revisar la red (tipo de adaptador + IP estática + DNS) ANTES de tocar roles de AD — el 80% de los problemas de "no puedo unir el cliente al dominio" son de red, no de configuración de AD en sí.

# 🖥️ Lab: Administración de Windows Server y Active Directory

Este repositorio contiene una guía paso a paso para desplegar y configurar un entorno de red basado en **Windows Server** y un cliente **Windows 10 Pro**, documentando cada procedimiento tanto desde la **Interfaz Gráfica (GUI)** como mediante **PowerShell**.

---

## 📐 Esquema de Red y Entorno

* **Hipervisor:** VMware / VirtualBox / Hyper-V
* **Servidor (DC):** Windows Server (IP: `192.168.10.10/24` | DNS: `127.0.0.1`)
* **Cliente:** Windows 10 Pro (IP: `192.168.10.20/24` | DNS: `192.168.10.10`)
* **Nombre de Dominio:** `MIDOMINIO.local`

---

## 🛠️ Contenido del Laboratorio

La documentación detallada se encuentra en la carpeta [`docs/`](./docs/):

1. 📌 **[Paso 1: Configurar la IP Estática en el Servidor](./docs/Paso%201%20Configurar%20la%20IP%20Est%C3%A1tica%20en%20el%20Servidor.md)**
   * Configuración de interfaz de red mediante GUI y `Set-DnsClientServerAddress` / `New-NetIPAddress`.

2. 🏰 **[Paso 2: Instalar Active Directory y Promover el Servidor](./docs/Paso%202%20Instalar%20Active%20Directory%20y%20Promover%20el%20Servidor.md)**
   * Instalación del rol AD DS y creación del nuevo bosque `labasir.local`.

3. 👥 **[Paso 3: Estructura de Active Directory (OUs, Grupos y Usuarios)](./docs/Paso%203%20Estructura%20de%20Active%20Directory%20(OUs,%20Grupos%20y%20Usuarios).md)**
   * Creación de Unidad Organizativa (`OU_Sistemas`), grupo de seguridad (`GRP_Sistemas_RW`) y usuario (`jperez`).

4. 📂 **[Paso 4: Carpeta Compartida y Permisos NTFS](./docs/Paso%204%20Carpeta%20Compartida%20y%20Permisos.md)**
   * Recursos compartidos en red, gestión de permisos mediante `icacls` y ruptura de herencia.

5. 💻 **[Paso 5: Configurar IP e Unir Cliente Windows 10 al Dominio](./docs/Paso%205%20Configurar%20la%20IP%20y%20Unir%20el%20Cliente%20(Windows%2010%20Pro)%20al%20Dominio.md)**
   * Conectividad cliente-servidor y unión al dominio mediante `Add-Computer`.

---

## 🚀 Tecnologías y Comandos Utilizados

* **Active Directory Domain Services (AD DS)**
* **PowerShell Cmdlets:** `New-ADOrganizationalUnit`, `New-ADGroup`, `New-ADUser`, `Add-ADGroupMember`, `Add-Computer`
* **Gestión de Red y Permisos:** `icacls`, `New-SmbShare`, `New-NetIPAddress`
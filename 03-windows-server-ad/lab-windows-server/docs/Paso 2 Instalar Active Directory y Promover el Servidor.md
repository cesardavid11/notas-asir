# Paso 2: Instalar Active Directory y Promover el Servidor

## Opción A: Desde la Interfaz Gráfica (GUI)

1. Abre Administrador del Servidor > Agregar roles y características.

![Paso 1](../img/install-ad-paso1.png)

2. Avanza hasta Roles de servidor y marca Servicios de dominio de Active Directory. Instala.

![Paso 2](../img/install-ad-paso2.png)


3. Al finalizar, haz clic en el ícono de la bandera (arriba a la derecha) > Promover este servidor a controlador de dominio.

![Paso 3](../img/install-ad-paso3.png)

![Paso 3.1](../img/install-ad-paso4.png)



4. Selecciona Agregar un nuevo bosque, asigna el nombre MIDOMINIO.local, escribe la contraseña DSRM y completa el asistente. Se reiniciará solo.

![Paso 4](../img/install-ad-paso5.png)

---

## Opción B: Desde PowerShell (Como Administrador)

```
# 1. Instalar la característica de Active Directory con sus herramientas
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# 2. Promover a Controlador de Dominio y crear el bosque (te pedirá la contraseña DSRM)
Install-ADDSForest -DomainName "MIDOMINIO.local" -InstallDns:$true -Force
```




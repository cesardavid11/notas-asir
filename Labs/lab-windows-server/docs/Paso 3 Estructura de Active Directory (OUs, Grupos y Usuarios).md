# Paso 3: Estructura de Active Directory (OUs, Grupos y Usuarios)

## Opción A: Desde la Interfaz Gráfica (GUI)

1. Abre Usuarios y equipos de Active Directory (dsa.msc).

![Paso 1](../img/estruc-ad-paso1.png)

2. Clic derecho en labasir.local > Nuevo > Unidad Organizativa (Nombre: OU_Sistemas).

![Paso 2](../img/estruc-ad-paso2.png)

3. Clic derecho dentro de OU_Sistemas > Nuevo > Grupo (Nombre: GRP_Sistemas_RW).

![Paso 3](../img/estruc-ad-paso3.png)


4. Clic derecho dentro de OU_Sistemas > Nuevo > Usuario (Nombre: Juan Pérez, Login: jperez). Asigna contraseña.

![Paso 4](../img/estruc-ad-paso4.png)

![Paso 4.1](../img/estruc-ad-paso5.png)


5. Abre las propiedades del usuario jperez > Pestaña Miembro de > Agrega el grupo GRP_Sistemas_RW.

![Paso 5](../img/estruc-ad-paso6.png)

---

## Opción B: Desde PowerShell (Como Administrador)

```
# 1. Crear Unidad Organizativa
New-ADOrganizationalUnit -Name "OU_Sistemas" -Path "DC=MIDOMINIO,DC=local"

# 2. Crear Grupo de Seguridad
New-ADGroup -Name "GRP_Sistemas_RW" -GroupScope Global -GroupCategory Security -Path "OU=OU_Sistemas,DC=MIDOMINIO,DC=local"

# 3. Crear Usuario (encriptando la contraseña previamente)
$Password = ConvertTo-SecureString "P@ssw0rd2026!" -AsPlainText -Force
New-ADUser -Name "Juan Perez" -GivenName "Juan" -Surname "Perez" `
           -SamAccountName "jperez" -UserPrincipalName "jperez@labasir.local" `
           -Path "OU=OU_Sistemas,DC=labasir,DC=local" `
           -AccountPassword $Password -Enabled $true

# 4. Añadir Usuario al Grupo
Add-ADGroupMember -Identity "GRP_Sistemas_RW" -Members "jperez"
```
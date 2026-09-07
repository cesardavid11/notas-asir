# Paso 4: Carpetas Compartidas y Permisos

## Opción A: Desde la Interfaz Gráfica (GUI)

1. En C:\, crea la carpeta Sistemas.

![Paso 1](../img/permisos-paso1.png)

2. Clic derecho > Propiedades > Pestaña Compartir > Compartir avanzado.

![Paso 2](../img/permisos-paso1.png)

* Marca Compartir esta carpeta. Permisos: Control Total a Todos.

![Paso 2.1](../img/permisos-paso2.png)


3. Pestaña Seguridad (Permisos NTFS):

![Paso 3](../img/permisos-paso3.png)

* Clic en Opciones avanzadas > Deshabilitar herencia (Convertir permisos heredados en explícitos).

![Paso 3.1](../img/permisos-paso4.png)

* Elimina permisos innecesarios y añade el grupo GRP_Sistemas_RW con permisos de Modificar/Escritura.

![Paso 3.2](../img/permisos-paso5.png)

---

## Opción B: Desde PowerShell / CMD

```
# 1. Crear la carpeta
New-Item -Path "C:\Sistemas" -ItemType Directory

# 2. Compartir la carpeta en red
New-SmbShare -Name "Sistemas" -Path "C:\Sistemas" -FullAccess "Everyone"

# 3. Configurar Permisos NTFS usando icacls
icacls "C:\Sistemas" /inheritance:d
icacls "C:\Sistemas" /grant "labasir\GRP_Sistemas_RW:(OI)(CI)M"
```
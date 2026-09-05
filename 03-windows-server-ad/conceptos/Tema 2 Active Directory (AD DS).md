# Active Directory (AD DS)

**Fecha:** 2026-09-05
**Categoría:** (Windows Server)

Active Directory (AD) es el servicio de directorio de Microsoft que actúa como la base de datos centralizada de identidades y permisos de una red empresarial.

Imagina Active Directory como la "agenda digital inteligente" o el "libro de registro" de la compañía: almacena la información de todos los usuarios, ordenadores, impresoras y carpetas compartidas, y controla exactamente quién tiene acceso a qué recurso.

---

## ¿Cómo funciona en la práctica?

Sin Active Directory, un administrador tendría que configurar manualmente cada ordenador de la empresa para crear las cuentas de usuario y asignar permisos uno por uno.

Con Active Directory, todo se gestiona desde un único servidor (llamado Controlador de Dominio):

* **Autenticación (Inicio de sesión único):** Un empleado puede sentarse en cualquier ordenador de la oficina conectada a la red, ingresar sus credenciales (usuario y contraseña) y el sistema lo reconocerá al instante cargando sus permisos.

* **Autorización:** Define qué puede o no hacer cada usuario. Por ejemplo, el departamento de Finanzas puede acceder a la carpeta de contabilidad, pero el departamento de Marketing no.

* **Políticas de Grupo** (GPO): Permite aplicar reglas de seguridad de forma masiva a cientos de ordenadores a la vez (como obligar el cambio de contraseña cada 90 días, bloquear el uso de memorias USB o instalar un software automáticamente).

---

## La estructura lógica de Active Directory

Para mantener el orden, Active Directory organiza sus elementos de forma jerárquica:

1. **Objetos:** Cada elemento individual de la red (un usuario, una impresora, un equipo).

2. **Unidades Organizativas (OU):** Carpetas lógicas dentro de AD para agrupar objetos por departamentos o sedes (ej. "Ventas", "Recursos Humanos").

3 **Dominio:** La frontera principal de gestión. Es el espacio donde residen todos los objetos bajo una misma administración y nombre (ej. empresa.local).

4. **Árboles y Bosques:** Agrupaciones de uno o varios dominios que comparten la misma estructura de datos y relaciones de confianza.
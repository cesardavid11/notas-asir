# Dominio

**Fecha:** 2026-09-05
**Categoría:** (Windows Server)

Un Dominio en el entorno de Windows Server es el límite administrativo y de seguridad principal dentro de una red empresarial.

Si Active Directory es la base de datos de la empresa, el Dominio es la frontera o el "territorio digital" que delimita qué equipos y usuarios comparten esa misma base de datos, reglas de seguridad y administración centralizada.

Se identifica mediante un nombre de red con formato similar a una página web (por ejemplo, miempresa.com o empresa.local)

---

## ¿Para qué sirve un Dominio?

1. **Centralización de credenciales:** Un usuario creado en el dominio puede iniciar sesión en cualquier ordenador conectado a ese mismo dominio sin necesidad de crear una cuenta local en cada máquina.

2. **Administración unificada:** Si cambias la contraseña de un usuario o modificas sus permisos en el servidor principal, el cambio se aplica al instante en toda la red.

3 **Límite de seguridad:** Todo lo que ocurre dentro del dominio sigue las mismas políticas. Un usuario de un dominio exterior no puede acceder a los recursos del tuyo a menos que se establezca una relación explícita de confianza.

---

### Conceptos clave relacionados con el Dominio

- **Controlador de Dominio (Domain Controller / DC):** Es el servidor físico o virtual que ejecuta Active Directory. Es el "jefe" del dominio; responde a las peticiones de inicio de sesión, verifica las contraseñas y aplica las directivas de seguridad.

- **Unirse al Dominio (Domain Join):** Es el proceso mediante el cual añades un equipo (con Windows 10/11 Pro o Enterprise) al dominio. A partir de ese momento, el equipo pasa a ser administrado centralmente por el servidor.

- **Relaciones de Confianza (Trusts):** Permiten que dos dominios distintos (por ejemplo, tras la fusión de dos empresas) compartan recursos para que los usuarios de un dominio puedan acceder a los servicios del otro.
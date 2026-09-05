# DNS (Domain Name System)

**Fecha:** 2026-09-05
**Categoría:** (Windows Server)

El DNS (Sistema de Nombres de Dominio) es el servicio encargado de traducir los nombres legibles para las personas en direcciones IP numéricas que entienden los ordenadores.

Funciona como la "lista de contactos" de la red: los humanos recuerdan nombres (como google.com o servidor-archivos), mientras que los equipos necesitan conectarse a través de direcciones de red (como 192.168.1.50).

---

## ¿Por qué DNS es importante en Windows Server?

En una red empresarial con Active Directory, DNS no es solo un servicio secundario para salir a Internet; es absolutamente indispensable para que la red funcione.

Sin un servidor DNS bien configurado, Active Directory deja de funcionar por completo. Esto se debe a varias razones clave:

1. **Localización de servicios (Registros SRV):** Cuando un usuario intenta iniciar sesión, su equipo no sabe dónde está el Controlador de Dominio. Le pregunta a DNS: "¿Quién es el Controlador de Dominio de empresa.local?", y DNS le devuelve la IP exacta del DC.

2. **Nombres de equipos:** Permite que los usuarios accedan a carpetas compartidas o impresoras usando nombres sencillos (ejemplo: \\servidor-fotos\ventas) en lugar de memorizar números de IP.

3. **Navegación externa e interna:** Resuelve tanto las direcciones internas de la oficina como las peticiones de páginas web en Internet (google.com, microsoft.com).
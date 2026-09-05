# Controlador de Dominio (DC)

**Fecha:** 2026-09-05
**Categoría:** (Windows Server)

El Controlador de Dominio (o DC, por sus siglas en inglés: Domain Controller) es el servidor que tiene instalado Active Directory y se encarga de dirigir toda la seguridad y el acceso dentro del dominio.

Si el Dominio es el territorio y Active Directory es la base de datos, el Controlador de Dominio es el guardián y cerebro del sistema.

---

## ¿Qué hace exactamente un Controlador de Dominio?

* **Autenticación de usuarios (El "portero"):**
Cuando un empleado enciende su ordenador e introduce su usuario y contraseña, el equipo no verifica los datos localmente, sino que le pregunta al Controlador de Dominio: "¿Es correcta esta contraseña?". El DC la comprueba y le da acceso.

* **Replicación (Sincronización):**
En empresas medianas o grandes suele haber varios Controladores de Dominio para que, si uno falla o se apaga, la red siga funcionando sin interrupciones. Los DCs se comunican entre sí mediante un proceso llamado replicación para mantener la base de datos idéntica en todos ellos.

* **Búsqueda de recursos (Servidor de Catálogo Global):**
Mantiene un índice de todos los objetos de la red. Si un usuario busca una impresora en la oficina o la dirección de correo de un compañero, el DC le dice dónde encontrarlo.

**Aplicación de Políticas (GPO):**
Cada vez que un equipo o usuario inicia sesión, el DC le envía las reglas de configuración vigentes (por ejemplo: cambiar el fondo de pantalla, bloquear el Panel de Control o forzar la actualización del antivirus).

---

## Los roles FSMO (Funciones especiales del DC)

Aunque la mayoría de los trabajos dentro de Active Directory se reparten por igual entre todos los DCs, hay 5 tareas críticas llamadas funciones FSMO (Flexible Single Master Operation) que solo un DC específico gestiona a la vez para evitar conflictos:

* **Esquema (Schema Master):** Define las reglas del tipo de datos que se pueden guardar en Active Directory.

* **Nombres de Dominio (Domain Naming Master):** Controla que no se añadan dominios con nombres duplicados en el bosque.

* **PIDC (PDC Emulator):** Maneja la sincronización de la hora de todos los ordenadores de la red (crucial para la seguridad) y los cambios de contraseña inmediatos.

* **RID (RID Master):** Asigna identificadores únicos a cada usuario o equipo nuevo que se crea.

* **Infraestructura (Infrastructure Master):** Traduce las referencias a objetos cuando hay múltiples dominios interactuando.
# Kerberos (autenticación en Active Directory)

**Fecha:** 2026-08-22 (reconstruida)
**Categoría:** Windows-AD / Seguridad

## ¿Qué es?

Protocolo de autenticación que usa AD por defecto. En vez de mandar contraseñas por la red, usa "tickets" cifrados que demuestran que ya te autenticaste, sin repetir credenciales en cada servicio.

## ¿Para qué sirve? (contexto real)

Permite Single Sign-On dentro del dominio: te logueas una vez y accedes a recursos (archivos, impresoras, otros servicios) sin volver a meter la contraseña.

## Cómo funciona (paso a paso)

1. **AS-REQ**: el cliente pide un TGT (Ticket Granting Ticket) al KDC (el propio DC), mandando su usuario cifrado con su hash de contraseña.
2. **AS-REP**: el KDC responde con un TGT cifrado con la clave del `krbtgt` (cuenta especial del dominio).
3. **TGS-REQ**: cuando el cliente quiere acceder a un servicio, manda el TGT al KDC pidiendo un ticket específico para ese servicio.
4. **TGS-REP**: el KDC entrega un Service Ticket cifrado con la clave del servicio destino.
5. **AP-REQ**: el cliente presenta ese Service Ticket directamente al servicio, que lo valida sin necesidad de contactar al KDC.

```
Cliente --AS-REQ--> KDC (DC)
Cliente <--AS-REP-- KDC   (TGT)
Cliente --TGS-REQ-> KDC
Cliente <--TGS-REP-- KDC  (Service Ticket)
Cliente --AP-REQ---> Servicio
```

## Ejemplo práctico

En mi lab `midominio.local`, al hacer login con `ana.perez` en el cliente Windows 10 unido al dominio, Wireshark filtrado por `kerberos` muestra el AS-REQ/AS-REP nada más loguear, y el TGS-REQ/TGS-REP al acceder a un recurso compartido (`\\dc01\ventas`).

## Relación con seguridad

- **Kerberoasting**: pedir Service Tickets para cuentas de servicio y crackear el hash offline, porque parte del ticket va cifrado con el hash de la contraseña del servicio.
- **Golden Ticket**: si un atacante roba el hash de `krbtgt`, puede forjar TGTs válidos para cualquier usuario, sin pasar por el KDC real.
- Mitigación básica: contraseñas largas/aleatorias en cuentas de servicio, rotación de `krbtgt`, monitorizar TGS-REQ inusuales.

## Fuentes / referencias

- Sesión de estudio propia + labs en VirtualBox (dominio midominio.local)

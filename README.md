# 📚 Notas ASIR — Cesar

Repositorio de notas técnicas del ciclo ASIR (IES Doctor Fleming, Oviedo), enfocado en administración de sistemas y camino hacia ciberseguridad (SOC / pentesting).

## ¿Por qué este repo?

No tomé notas mientras aprendía por vagancia 😅. Este repo es la reconstrucción documentada de esos conocimientos, hecha bien desde ahora en adelante. Sirve como:
- Portfolio demostrable para entrevistas de FCT
- Referencia rápida para no repetir errores ya resueltos
- Evidencia de progreso real, no solo "vi un curso"

## Estructura

```
01-linux/              → Permisos, ACLs, procesos, systemd, cron
02-redes/               → OSI/TCP-IP, subnetting, Wireshark, routing (OSPF/BGP)
03-windows-server-ad/   → AD DS, DNS, Kerberos, GPOs
04-seguridad/           → Security+, conceptos, roadmap de certificaciones
05-ctf-writeups/        → OverTheWire Bandit y futuros CTFs
06-scripting/           → Bash, PowerShell
00-templates/           → Plantillas para nuevas notas (usar SIEMPRE una de estas)
```

Cada tema tiene dos tipos de nota posibles:
- **conceptos/** → teoría explicada con tus propias palabras + diagramas/ejemplos
- **labs/** o **comandos/** → paso a paso reproducible de algo que hiciste

## Cómo se escribe cada nota

1. Copia la plantilla correspondiente de `00-templates/`
2. Rellena el contexto: ¿qué problema resolvías o qué querías lograr?
3. Pasos numerados, con el comando exacto usado
4. Errores que cometiste y cómo los arreglaste (sección "Troubleshooting")
5. Commit con mensaje descriptivo: `git commit -m "docs: nota sobre Kerberoasting"`

## Estado del repo

- [x] Estructura base
- [ ] Migrar notas de AD DS (promoción DC, OUs, GPOs)
- [ ] Migrar notas de Kerberos + ataques
- [ ] Migrar notas de subnetting/VLSM
- [ ] Migrar writeups de Bandit
- [ ] Migrar roadmap Security+

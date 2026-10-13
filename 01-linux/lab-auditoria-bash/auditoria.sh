#!/bin/bash

# SCRIPT DE AUDITORIA DE SISTEMA - LAB 1


# Definicion del archivo de salida

log_file="reporte_auditoria.txt"
fecha=$(date "+%Y-%m-%d %H:%M:%S")

echo "=================================" >> $log_file
echo " REPORTE DE AUDITORIA DE SISTEMA " >> $log_file
echo " Fecha: $fecha" >> $log_file
echo "=================================" >> $log_file
echo "" >> $log_file


# INFORMACION DE USUARIOS

echo "[1] USUARIOS CON SHELL ACTIVA" >> $log_file
grep -E '/bin/bash|/bin/zsh' /etc/passwd | cut -d ':' -f1 >> $log_file
echo "" >> $log_file


# PUERTOS EN ESCUCHA

echo "[2] PUERTOS TCP/UDP ABIERTOS (LISTEN)" >> $log_file
ss -tulpn | grep LISTEN | awk '{print $5}' >> $log_file
echo "" >> $log_file


# VERIFICACION DE ESPACIO EN DISCO

echo "[3] ESTADO DEL DISCO PRINCIPAL (/)" >> $log_file
uso_disco=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
echo "Uso actual del disco: ${uso_disco}%" >> $log_file

if [ "$uso_disco" -ge 85 ]; then
    echo "ALERTA: El espacio en disco ha superado el 85%" >> $log_file
else
    echo "Estado del disco dentro de los limites normales." >> $log_file
fi
echo "" >> $log_file


# INTENTOS FALLIDOS DE ACCESO SSH (ultimos 5)

echo "[4] ULTIMOS FALLIDOS DE ACCESO SSH" >> $log_file

if [ -f /var/log/uath.log ]; then
    grep "Failed password" /var/log/auth.log | tail -n 5 >> $log_file
else
    # Para sistemas Debian/Ubuntu
    journalctl _SYSTEMD_UNIT=ssh.service | grep "Failed password" | tail -n 5 >> $log_file
fi
echo "" >> $log_file

# VERIFICACION DE RAM LIBRE

echo "[5] MEMORIA RAM LIBRE" >> $log_file
ram_libre=$(free -m | awk 'NR==2 {printf "%.2f", $7/1024}')
echo "Espacio de RAM Libre: ${ram_libre} GB" >> $log_file
echo "" >> $log_file


echo "Auditoria completada. Guardando en $log_file" 
# Empaquetado, Compresión y SSH

**Fecha:** 2026-08-30
**Categoría:** (Linux)

---

## Conceptos Importantes 

### Empaquetado (Archivado): 
Agrupa múltiples archivos y directorios en un único archivo (un contenedor), conservando
permisos, estructura de carpetas y metadatos. No reduce el tamaño.

### Compresión: 
Aplica algoritmos matemáticos para reducir el espacio ocupado por un archivo o empaquetado.

### SSH (Secure Shell): 
Protocolo de red cifrado que permite administrar y transferir archivos entre máquinas remotas 
de forma segura.

---

## Uso de tar (Empaquetado y Compresión)
tar (Tape Archive). El formato comprimido más común combina tar con el compresor gzip, generando 
archivos con extensión .tar.gz o .tgz.

Desglose de Flags de tar

* -c (create): Crea un nuevo archivo.

* -x (extract): Extrae el contenido de un archivo.

* -z (gzip): Filtra el archivo mediante el algoritmo de compresión gzip.

* -v (verbose): Muestra los archivos procesados en la terminal.

* -f (file): Especifica el nombre del archivo destino/origen. (Debe ser el último flag antes del nombre).


## Crear un tarball comprimido (tar -czvf)
Para empaquetar y comprimir el directorio mi_carpeta en un archivo llamado archivo.tar.gz:

tar -czvf archivo.tar.gz /ruta/a/mi_carpeta


## Extraer un tarball (tar -xzvf)
Para descomprimir y extraer el contenido en el directorio actual:

tar -xzvf archivo.tar.gz


Para extraer el contenido en una carpeta específica (ej. /tmp):

tar -xzvf archivo.tar.gz -C /tmp

---
 
## Configuración del Servidor SSH (openssh-server)

1. Instalar el servidor SSH

sudo apt update
sudo apt install openssh-server -y

2. Iniciar y habilitar el servicio
sudo systemctl enable ssh

3. Verificar el estado del servicio:

sudo systemctl status ssh

4. Obtener la IP de la máquina servidor:

ip a


## Conexión inicial por contraseña desde la máquina cliente
En tu máquina cliente, conéctate con la IP obtenida:

ssh usuario_remoto@192.168.1.50


# Autenticación por Claves SSH (Pública y Privada)
La autenticación mediante par de claves elimina la necesidad de escribir la contraseña y proporciona mayor seguridad criptográfica.


1. Generar el par de claves en el cliente:
Ejecuta esto en tu máquina local (cliente):

ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"

resiona Enter para guardar en la ruta por defecto (~/.ssh/id_ed25519). Opcionalmente, puedes añadir una contraseña de paso (passphrase).


2. Copiar la clave pública al servidor remoto:
Transfiere tu clave pública (id_ed25519.pub) al servidor con la herramienta automatizada:

ssh-copy-id usuario_remoto@192.168.1.50


3. Conectarse sin contraseña:
A partir de ahora, el servidor autenticará la clave privada local contra la clave pública almacenada en ~/.ssh/authorized_keys del servidor:

ssh usuario_remoto@192.168.1.50


4. Desactivar la autenticación por contraseña (Opcional - Mayor Seguridad):
En el servidor, edita el archivo /etc/ssh/sshd_config:

sudo nano /etc/ssh/sshd_config

Cambia o añade la línea:

PasswordAuthentication no

Reinicia el servicio para aplicar cambios:

sudo systemctl restart ssh


# Subnetting Básico y CIDR

**Fecha:** 2026-09-01
**Categoría:** (Redes)

Entender Subnetting y CIDR consiste en aprender a dividir una red grande en subredes pequeñas para optimizar el tráfico, mejorar la seguridad y no desperdiciar direcciones IP.

---

## Conceptos Fundamentales
Una dirección IPv4 tiene 32 bits en total. Se divide en dos partes:

Porción de Red: Identifica a la red a la que pertenece la IP.

Porción de Host: Identifica al dispositivo específico dentro de esa red.

## 3. Mascara de subred:

Cada dirección IP identifica una red y una interfaz única en la misma. También se puede escribir la máscara de subred en notación decimal, con puntos, y determina dónde termina la parte de la red y dónde comienza la parte del _host_ de la dirección IP.

Cuando se expresa en binario, cualquier bit puesto a uno significa que el correspondiente bit en la dirección IP es parte de la dirección de red. Los bits puestos a cero indican los bits correspondientes a parte de la dirección del _host_ en la dirección IP.

Los bits que marcan la máscara de subred deben ser unos consecutivos. La mayoría de las máscaras de subred comienzan con 255. y continúan hasta que finaliza la máscara de red. Por ejemplo, una máscara de subred de clase C sería 255.255.255.0.


Mediante la máscara de red, un sistema (ordenador, puerta de enlace, enrutador, etc.) podrá saber si debe enviar un paquete dentro o fuera de la subred en la que está conectado. Por ejemplo, si el enrutador tiene la dirección IP 192.168.1.1 y máscara de red 255.255.255.0, entiende que todo lo que se envía a una dirección IP con formato 192.168.1.X, se envía hacia la red local, mientras que direcciones con distinto formato de dirección IP serán enviadas hacia afuera (Internet, otra red local mayor, entre otros). También, es muy común encontrar variaciones de la misma.

 Ejemplo:

Suponiendo que tenemos un rango de direcciones IP desde 10.0.0.0 hasta 10.255.255.255, y si todas ellas forman parte de la misma red, su máscara de red sería 255.0.0.0, que también se puede expresar como 10.0.0.0/8

Una máscara de red representada en binario son 4 octetos de bits:

`11111111.11111111.11111111.11111111`

La representación utilizada se define colocando en 1 todos los bits de red (máscara natural) y en el caso de subredes, se coloca en 1 los bits de red y 0 los bits de host usados por las subredes. Así, en esta forma de representación (10.0.0.0/8) el 8 sería la cantidad de bits puestos a 1 que contiene la máscara en binario, comenzando desde la izquierda. Para el ejemplo dado (/8), sería:

`11111111.00000000.00000000.00000000`

y en su representación en decimal sería 255.0.0.0.


## ¿Cómo funciona el CIDR?

El CIDR se basa en el concepto de las máscaras de subred. Una máscara se superpone a una dirección IP creando así una red se­cu­n­da­ria su­pe­di­ta­da a Internet. Esta **máscara de subred** señala al router qué porción de la dirección IP se reserva a los hosts (a cada in­te­gra­n­te de la red) y qué parte ide­n­ti­fi­ca a la red.

Pero, si en lugar de añadir una máscara de subred, se integra en la dirección IP una es­pe­ci­fi­ca­ción o un **sufijo con CIDR**, no solo se gana vi­sua­l­me­n­te: además de subredes (_su­b­ne­t­ti­ng_), el CIDR también permite crear su­per­re­des (_su­pe­r­ne­t­ti­ng_). Esto quiere decir que las redes pueden tanto su­b­di­vi­di­r­se como agruparse.

El _su­pe­r­ne­t­ti­ng_ podría interesar, por ejemplo, a empresas con varias filiales que quieren mantener todos los or­de­na­do­res en la misma red, porque con esta técnica, también conocida como **_route ag­gre­ga­tion_** (agru­pa­ción de rutas) podrían agrupar varias redes en una sola ruta. Con ello los paquetes de datos solo se enviarían a un destino, sin importar dónde estuviera situado el host fí­si­ca­me­n­te.

 Hecho

Un elemento central del CIDR es la **VSLM**: la **_variable length subnet mask_** (máscara de subred de longitud variable) permite que también puedan im­ple­me­n­tar­se redes con lo­n­gi­tu­des variables y no solo según las ca­te­go­rías es­ta­ble­ci­das de las clases de redes


## La notación CIDR

Antes podía deducirse de una dirección IP a qué clase pe­r­te­ne­cía. Las redes de la clase C, por ejemplo, ocupaban el espacio de di­re­c­cio­nes de 192.0.0.0 a 223.255.255.255. La máscara de subred (como 255.255.255.0, p. ej.) **se superpone a la dirección IP** y determina cuántos hosts puede alojar. En el formato CIDR esta in­fo­r­ma­ción ya está integrada en la misma dirección IP como sufijo, aunque el principio de base sigue siendo el mismo: este sufijo indica qué po­si­cio­nes (o bits) de la dirección IP ide­n­ti­fi­can a la red (Network ID) y au­to­má­ti­ca­me­n­te qué bits co­n­s­ti­tu­yen el área del host ID. Para en­te­n­de­r­lo, ob­se­r­ve­mos una máscara de subred en formato binario:

255.255.255.0 ≙ **11111111 11111111 11111111** 00000000

En la notación CIDR, esta máscara de subred (de clase C) equi­va­l­dría al sufijo /24, ya que los primeros 24 bits (en negrita) ide­n­ti­fi­can la porción de la red de la dirección IP (en la clase C los tres primeros octetos ide­n­ti­fi­can a la red). Pero la notación CIDR no solo admite bloques de unos o ceros: gracias a la VLSM también es posible crear **subredes más flexibles**. La máscara /25 equivale en formato binario a 11111111 11111111 11111111 **1**000000, por ejemplo, y en formato decimal a 255.255.255.128.

> **Nota:** También con CIDR y VLSM los bits de las máscaras de subred se agregan siempre de izquierda a derecha y cada octeto solo puede incluir ceros o unos, si bien no de forma aleatoria (00110000 10101000 no sería posible).


## Qué son los bloques CIDR

Una dirección IPv4 se compone de 32 bits, lo que se ve mucho más claro si se calcula el **equi­va­le­n­te binario** desde la notación decimal:

201.105.7.34 equivale a 11001001 01101001 00000111 00100010.

La notación binaria de una dirección IP, que es el lenguaje con el que operan los or­de­na­do­res, está formada por 32 po­si­cio­nes que solo pueden ocuparse con unos o ceros, esto es, 32 bits. Por eso en la notación CIDR los sufijos posibles también abarcan del 0 al 32.

En la creación de subredes se trata de **lograr puntos en común**. 201.105.7.34/24 y 201.105.7.1/24 están, así, en la misma red. El sufijo indica que los primeros 24 bits se emplean para ide­n­ti­fi­car a la red, de modo que, si pe­r­te­ne­cen a la misma red, estos han de ser iguales. Los bits restantes están re­se­r­va­dos para de­te­r­mi­nar los hosts. El número de bits que en formato CIDR se encuentra tras la barra señala el número de po­si­cio­nes (de izquierda a derecha) o bits que pe­r­te­ne­cen a la parte de la red de la dirección IP. La tabla a co­n­ti­nua­ción muestra a qué máscaras de subred equivale la notación CIDR y cuántas di­re­c­cio­nes (o dominios) libres ofrece cada una.

| **Sufijo CIDR** | **Máscara de subred** (decimal) | **Máscara de subred** (binario)     | **Di­re­c­cio­nes libres** |     |
| --------------- | ------------------------------- | ----------------------------------- | -------------------------- | --- |
| /0              | 0.0.0.0                         | 00000000.00000000.00000000.00000000 | 4.294.967.296              | 232 |
| /1              | 128.0.0.0                       | 10000000.00000000.00000000.00000000 | 2.147.483.648              | 231 |
| /2              | 192.0.0.0                       | 11000000.00000000.00000000.00000000 | 1.073.741.824              | 230 |
| /3              | 224.0.0.0                       | 11100000.00000000.00000000.00000000 | 536.870.912                | 229 |
| /4              | 240.0.0.0                       | 11110000.00000000.00000000.00000000 | 268.435.456                | 228 |
| /5              | 248.0.0.0                       | 11111000.00000000.00000000.00000000 | 134.217.728                | 227 |
| /6              | 252.0.0.0                       | 11111100.00000000.00000000.00000000 | 67.108.864                 | 226 |
| /7              | 254.0.0.0                       | 11111110.00000000.00000000.00000000 | 33.554.432                 | 225 |
| /8              | 255.0.0.0                       | 11111111.00000000.00000000.00000000 | 16.777.216                 | 224 |
| /9              | 255.128.0.0                     | 11111111.10000000.00000000.00000000 | 8.388.608                  | 223 |
| /10             | 255.192.0.0                     | 11111111.11000000.00000000.00000000 | 4.194.304                  | 222 |
| /11             | 255.224.0.0                     | 11111111.11100000.00000000.00000000 | 2.097.152                  | 221 |
| /12             | 255.240.0.0                     | 11111111.11110000.00000000.00000000 | 1.048.576                  | 220 |
| /13             | 255.248.0.0                     | 11111111.11111000.00000000.00000000 | 524.288                    | 219 |
| /14             | 255.252.0.0                     | 11111111.11111100.00000000.00000000 | 262.144                    | 218 |
| /15             | 255.254.0.0                     | 11111111.11111110.00000000.00000000 | 131.072                    | 217 |
| /16             | 255.255.0.0                     | 11111111.11111111.00000000.00000000 | 65.536                     | 216 |
| /17             | 255.255.128.0                   | 11111111.11111111.10000000.00000000 | 32.768                     | 215 |
| /18             | 255.255.192.0                   | 11111111.11111111.11000000.00000000 | 16.384                     | 214 |
| /19             | 255.255.224.0                   | 11111111.11111111.11100000.00000000 | 8.192                      | 213 |
| /20             | 255.255.240.0                   | 11111111.11111111.11110000.00000000 | 4.096                      | 212 |
| /21             | 255.255.248.0                   | 11111111.11111111.11111000.00000000 | 2.048                      | 211 |
| /22             | 255.255.252.0                   | 11111111.11111111.11111100.00000000 | 1.024                      | 210 |
| /23             | 255.255.254.0                   | 11111111.11111111.11111110.00000000 | 512                        | 29  |
| /24             | 255.255.255.0                   | 11111111.11111111.11111111.00000000 | 256                        | 28  |
| /25             | 255.255.255.128                 | 11111111.11111111.11111111.10000000 | 128                        | 27  |
| /26             | 255.255.255.192                 | 11111111.11111111.11111111.11000000 | 64                         | 26  |
| /27             | 255.255.255.224                 | 11111111.11111111.11111111.11100000 | 32                         | 25  |
| /28             | 255.255.255.240                 | 11111111.11111111.11111111.11110000 | 16                         | 24  |
| /29             | 255.255.255.248                 | 11111111.11111111.11111111.11111000 | 8                          | 23  |
| /30             | 255.255.255.252                 | 11111111.11111111.11111111.11111100 | 4                          | 22  |
| /31             | 255.255.255.254                 | 11111111.11111111.11111111.11111110 | 2                          | 21  |
| /32             | 255.255.255.255                 | 11111111.11111111.11111111.11111111 | 1                          | 20  |

---

## Cómo calcular cualquier IP a mano

Imagina que te dan la IP 172.16.10.70/27 y te piden hallar su Red, Broadcast y Rango útil:

1. Calcula los ceros y el tamaño del salto

Ceros de host: 32 - 27 = 5 ceros.

Hosts totales por bloque 2^5 = 32.

El salto de red es 32.

2. Calcula la máscara decimal

256 - 32 = 224.

La máscara es 255.255.255.224.

3. Encuentra el bloque al que pertenece el valor (.70)

Como los saltos van de 32 en 32 en el último octeto:

Subred 0: 0

Subred 1: 32

Subred 2: 64S

ubred 3: 96

El número 70 cae en el rango entre 64 y 96.

4. Determina la IP de Red, Broadcast y Rango

IP de Red: 172.16.10.64 (El inicio de ese bloque).

IP de Broadcast: 172.16.10.95 (El número justo antes del siguiente salto, 96 - 1).

Rango Útil: 172.16.10.65 hasta 172.16.10.94.
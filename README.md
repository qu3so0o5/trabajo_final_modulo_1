<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:8A2BE2,50:B84DFF,100:00D9FF&height=220&section=header&text=SISTEMA%20DE%20INVENTARIO&fontSize=42&fontColor=FFFFFF&fontAlignY=42&animation=twinkling&desc=Gestión%20de%20productos%20desde%20la%20terminal&descSize=16&descAlignY=62&descColor=E6E6FA"/><br><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=B84DFF&center=true&vCenter=true&width=700&lines=Python+%7C+CLI+%7C+CSV;Gestión+de+productos+y+stock;Registro+de+ventas;Construido+desde+cero" alt="Typing SVG"/><br><br>

<img src="https://img.shields.io/badge/Python-3.x-8A2BE2?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CSV-Storage-00BFFF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/CLI-Terminal-B84DFF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-En%20desarrollo-FF69B4?style=for-the-badge"/></div><br>---

<div align="center">Una aplicación de inventario construida desde cero con Python

Sistema de línea de comandos para crear, consultar, modificar y eliminar productos, controlar existencias y registrar ventas utilizando archivos CSV como almacenamiento local.

</div><br>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

01 / DESCRIPCIÓN

Este proyecto nace como una implementación práctica de un sistema de inventario utilizando únicamente Python y su biblioteca estándar.

La aplicación funciona directamente desde la terminal y utiliza archivos ".csv" para conservar los datos, evitando depender de una base de datos externa.

                         SISTEMA DE INVENTARIO
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
          PRODUCTOS             STOCK              VENTAS
              │                   │                   │
        ┌─────┼─────┐             │             ┌─────┴─────┐
        │     │     │             │             │           │
      Crear  Ver  Editar       Añadir        Registrar   Reportar
        │     │     │          cantidad          │
        └─────┼─────┘             │             │
              │                   └──────┬──────┘
              │                          │
              └──────────────────────────┘
                         │
                         ▼
                       CSV

---

02 / FUNCIONALIDADES

GESTIÓN DE PRODUCTOS

<table>
<tr>
<td width="50%">Crear

- Registrar productos
- Generar ID único
- Definir nombre
- Establecer precio de compra
- Establecer precio de venta
- Definir stock inicial

</td>
<td width="50%">Administrar

- Mostrar inventario
- Buscar por ID
- Actualizar información
- Eliminar productos
- Consultar existencias

</td>
</tr>
</table><br>CONTROL DE INVENTARIO

El stock puede incrementarse directamente desde el menú:

                    STOCK ACTUAL

                         25
                          │
                          │
                       + 10
                          │
                          ▼
                         35

                   unidades disponibles

El sistema actualiza la cantidad almacenada del producto.

<br>REGISTRO DE VENTAS

Una venta sigue un proceso de validación antes de modificar el inventario:

                         PRODUCTO
                             │
                             ▼
                       BUSCAR POR ID
                             │
                             ▼
                     ¿PRODUCTO EXISTE?
                       ╱           ╲
                     NO             SÍ
                     │               │
                     ▼               ▼
                   ERROR        SOLICITAR
                                CANTIDAD
                                    │
                                    ▼
                              COMPROBAR STOCK
                               ╱           ╲
                             NO             SÍ
                             │               │
                             ▼               ▼
                           ERROR       DESCONTAR STOCK
                                             │
                                             ▼
                                      REGISTRAR VENTA

---

03 / MENÚ

La aplicación cuenta con un menú interactivo ejecutado directamente desde la terminal.

╭──────────────────────────────────────────────────╮
│                                                  │
│              SISTEMA DE INVENTARIO               │
│                                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  01    Añadir producto                           │
│  02    Mostrar productos                         │
│  03    Buscar producto por ID                    │
│  04    Actualizar producto                       │
│  05    Eliminar producto                         │
│  06    Añadir stock                              │
│  07    Registrar venta                           │
│  08    Salir                                     │
│                                                  │
╰──────────────────────────────────────────────────╯

La interfaz utiliza colores ANSI para diferenciar información, advertencias, errores y datos del inventario.

---

04 / ESTRUCTURA DE DATOS

Los productos se almacenan en:

data.csv

Formato:

id,nombre,p_compra,p_venta,stock

Ejemplo:

1,Teclado_Mecanico,80,120,15
2,Mouse_Gamer,40,70,20
3,Auriculares,60,95,10

Las operaciones de venta se almacenan en:

reporte_venta.csv

De esta forma, el proyecto mantiene separados los datos del inventario y el historial de ventas.

---

05 / ARQUITECTURA

.
├── main.py
│
│   ├── comprobando_existencia_de_archivos()
│   ├── agregar_producto()
│   ├── mostrar_productos()
│   ├── mostrar_producto_id()
│   ├── actulizar_producto()
│   ├── eliminar_producto()
│   ├── añadir_stock()
│   ├── venta_de_producto()
│   └── generar_reporte()
│
├── modulo_constantes.py
│
│   ├── Colores ANSI
│   ├── Negrita
│   ├── Reset
│   ├── Banner
│   └── Menús
│
├── data.csv
├── reporte_venta.csv
└── README.md

"main.py"

Contiene la lógica principal del sistema y las operaciones relacionadas con productos, inventario y ventas.

"modulo_constantes.py"

Centraliza los elementos visuales utilizados por la terminal.

Esto permite mantener separadas progresivamente la lógica y la presentación.

---

06 / TECNOLOGÍAS

<div align="center"><img src="https://img.shields.io/badge/Python-B84DFF?style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/CSV-00D9FF?style=for-the-badge"/><img src="https://img.shields.io/badge/Terminal-8A2BE2?style=for-the-badge"/></div><br>Python

El proyecto utiliza Python y módulos de su biblioteca estándar:

import csv
import time

from modulo_constantes import *

CSV

Los datos se gestionan mediante:

csv.reader()
csv.DictReader()
csv.DictWriter()

Esto permite trabajar tanto con filas como con registros representados mediante diccionarios.

---

07 / CONCEPTOS DE PROGRAMACIÓN

┌──────────────────────────────┐
│       ENTRADA / SALIDA       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       CONDICIONALES          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           BUCLES             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         FUNCIONES            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     MANEJO DE EXCEPCIONES    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      ARCHIVOS + CSV          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     LISTAS + DICCIONARIOS    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│            CRUD              │
└──────────────────────────────┘

También se practican:

- Lectura y escritura de archivos
- Conversión de tipos
- Validación de entradas
- "FileNotFoundError"
- "ValueError"
- "KeyboardInterrupt"
- Manipulación de listas
- Manipulación de diccionarios

---

08 / INTERFAZ DE TERMINAL

Una parte importante del proyecto es su identidad visual.

La interfaz utiliza colores ANSI y un banner personalizado para diferenciar los distintos tipos de información mostrados al usuario.

███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝

La intención es que el sistema no sea solamente funcional, sino que tenga una experiencia visual propia desde la terminal.

---

09 / INSTALACIÓN

Clonar

git clone <URL_DEL_REPOSITORIO>

Entrar al proyecto

cd <NOMBRE_DEL_REPOSITORIO>

Ejecutar

python main.py

También:

python3 main.py

No se requieren paquetes externos para las funcionalidades actuales.

---

10 / REQUISITOS

Python 3
   │
   ▼
Terminal compatible con ANSI
   │
   ▼
Sistema de archivos
   │
   ▼
CSV como almacenamiento

El proyecto no requiere:

- Base de datos externa
- Framework
- Librerías de terceros
- Servidor

---

11 / ESTADO

<div align="center"><img src="https://img.shields.io/badge/STATUS-EN%20DESARROLLO-B84DFF?style=for-the-badge"/><br><br>

████████████████░░░░   80%

</div>Las operaciones principales del sistema ya están implementadas y el proyecto continúa en proceso de mejora.

Próximas mejoras

[ ] Generación completa de reportes
[ ] Validaciones más robustas
[ ] Mejor manejo de errores
[ ] Mejor presentación de tablas
[ ] Validación de cantidades y precios
[ ] Optimización de la estructura
[ ] Separación entre lógica, datos e interfaz

---

12 / OBJETIVO

El objetivo es construir progresivamente un sistema de inventario funcional utilizando Python desde cero.

El proyecto parte de una aplicación de terminal sencilla y evoluciona incorporando nuevas funcionalidades mientras se refuerzan conceptos fundamentales de programación.

                       PYTHON
                          │
                          ▼
                    TERMINAL CLI
                          │
                          ▼
                     INVENTARIO
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
             CRUD                    CSV
              │                       │
              └───────────┬───────────┘
                          │
                          ▼
                        VENTAS
                          │
                          ▼
                       REPORTES

---

<div align="center"><br><img src="https://capsule-render.vercel.app/api?type=waving&color=0:00D9FF,50:B84DFF,100:8A2BE2&height=120&section=footer&animation=twinkling"/>SISTEMA DE INVENTARIO

Python · Terminal · CSV

</div>

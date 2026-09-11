<div align="center">SISTEMA DE INVENTARIO

Sistema de gestión de productos desde la terminal

Un proyecto de línea de comandos desarrollado en Python para administrar productos, controlar stock y registrar ventas utilizando archivos CSV como almacenamiento.

<br>"Python" (https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
"CSV" (https://img.shields.io/badge/Storage-CSV-6B7280?style=for-the-badge)
"CLI" (https://img.shields.io/badge/Interface-CLI-8B5CF6?style=for-the-badge)
"Status" (https://img.shields.io/badge/Status-In%20Development-F59E0B?style=for-the-badge)

</div>---

Vista general

Este proyecto es un sistema de inventario diseñado para ejecutarse directamente desde la terminal.

La aplicación permite crear productos, consultar información, modificar registros, eliminar productos, aumentar el stock y registrar ventas.

El proyecto utiliza archivos ".csv" para almacenar la información, evitando la necesidad de una base de datos externa.

              SISTEMA DE INVENTARIO
                       |
          +------------+------------+
          |            |            |
       PRODUCTOS     STOCK        VENTAS
          |            |            |
      Crear / Ver   Añadir      Registrar
      Buscar        cantidad    venta
      Editar                    |
      Eliminar                  v
                              REPORTE

---

Funcionalidades

Gestión de productos

- Añadir nuevos productos.
- Asignar un ID único.
- Registrar nombre.
- Registrar precio de compra.
- Registrar precio de venta.
- Registrar stock inicial.
- Mostrar todos los productos.
- Buscar productos mediante su ID.
- Actualizar información existente.
- Eliminar productos.

Control de inventario

El sistema permite incrementar el stock de un producto existente.

Stock actual
     |
     v
   25 unidades
     |
     + 10 ingresadas
     |
     v
   35 unidades

Registro de ventas

Al realizar una venta:

1. Se busca el producto mediante su ID.
2. Se solicita la cantidad.
3. Se comprueba el stock disponible.
4. Se descuenta la cantidad vendida.
5. Se registra la operación en el archivo de ventas.

---

Menú

La aplicación cuenta con un menú interactivo desde la terminal:

===============              MENU               ===============

1.- Añadir producto.
2.- Mostrar productos (Tabla).
3.- Buscar producto por (id).
4.- Actualizar producto (Sub menu).
5.- Eliminar producto.
6.- Añadir stock.
7.- Venta producto.
8.- Salir.

===============================================================

La interfaz utiliza colores ANSI para diferenciar información, advertencias, errores y datos del inventario.

---

Estructura de datos

Los productos se almacenan en:

data.csv

Cada producto contiene:

id,nombre,p_compra,p_venta,stock

Ejemplo:

1,Teclado_Mecanico,80,120,15
2,Mouse_Gamer,40,70,20
3,Auriculares,60,95,10

Las operaciones de venta se registran en:

reporte_venta.csv

---

Estructura del proyecto

.
├── modulo_constantes.py
├── main.py
├── data.csv
├── reporte_venta.csv
└── README.md

"main.py"

Contiene la lógica principal del sistema:

comprobando_existencia_de_archivos()
        |
        +-- Verificación de archivos

agregar_producto()
        |
        +-- Creación de productos

mostrar_productos()
        |
        +-- Visualización del inventario

mostrar_producto_id()
        |
        +-- Búsqueda por ID

actulizar_producto()
        |
        +-- Modificación de productos

eliminar_producto()
        |
        +-- Eliminación

añadir_stock()
        |
        +-- Incremento de inventario

venta_de_producto()
        |
        +-- Registro de ventas

generar_reporte()
        |
        +-- Reportes

"modulo_constantes.py"

Contiene las constantes utilizadas para la interfaz de terminal:

- Colores ANSI.
- Negrita.
- Reset de colores.
- Banner principal.
- Menús secundarios.

Esto permite mantener separada la parte visual de la lógica del programa.

---

Tecnologías utilizadas

Python

El proyecto está construido utilizando Python y diferentes herramientas de su biblioteca estándar.

import csv
import time
from modulo_constantes import *

CSV

El módulo "csv" permite trabajar con los archivos de inventario utilizando:

csv.reader()
csv.DictReader()
csv.DictWriter()

Esto permite trabajar tanto con filas como con registros representados mediante diccionarios.

---

Flujo de una venta

                  ID DEL PRODUCTO
                         |
                         v
                 Buscar producto
                         |
                         v
                  ¿Existe el ID?
                    /        \
                  NO          SÍ
                  |            |
                  v            v
               Error       Solicitar
                           cantidad
                              |
                              v
                       Comprobar stock
                         /         \
                       NO           SÍ
                       |             |
                       v             v
                    Error       Descontar
                                  stock
                                    |
                                    v
                            Registrar venta

---

Interfaz

El proyecto intenta mantener una experiencia visual clara dentro de una terminal, utilizando una combinación de colores pastel y un banner ASCII.

███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝

La idea es que el programa no sea solamente funcional, sino que también tenga una identidad visual propia desde la terminal.

---

Instalación

Clona el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>

No requiere instalar paquetes externos para utilizar las funcionalidades mostradas en el proyecto.

Ejecuta:

python main.py

o, dependiendo de tu instalación:

python3 main.py

---

Requisitos

Python 3
Terminal compatible con colores ANSI

El sistema utiliza archivos locales ".csv", por lo que no necesita una base de datos para funcionar.

---

Conceptos utilizados

Este proyecto sirve como práctica de varios conceptos fundamentales de Python:

Entrada / salida
       |
       v
Condicionales
       |
       v
Bucles
       |
       v
Funciones
       |
       v
Manejo de excepciones
       |
       v
Archivos
       |
       v
CSV
       |
       v
Diccionarios
       |
       v
CRUD

También se trabaja con operaciones como:

- Lectura y escritura de archivos.
- "csv.reader".
- "csv.DictReader".
- "csv.DictWriter".
- Listas.
- Diccionarios.
- Conversión de tipos.
- Validación de entradas.
- Manejo de "FileNotFoundError".
- Manejo de "ValueError".
- Manejo de "KeyboardInterrupt".

---

Estado del proyecto

[████████████████░░░░]  En desarrollo

El sistema ya cuenta con las operaciones principales de inventario y se encuentra en proceso de mejora.

Próximas mejoras

- Generación completa de reportes.
- Validaciones más robustas.
- Mejor manejo de errores.
- Mejoras en la presentación de las tablas.
- Validación de cantidades y precios.
- Optimización de la estructura del código.
- Separación progresiva entre lógica, datos e interfaz.

---

Objetivo

El objetivo del proyecto es construir progresivamente un sistema de inventario funcional desde cero, utilizando Python y herramientas de su biblioteca estándar.

Más que depender de una interfaz gráfica o una base de datos externa, el proyecto parte de una aplicación sencilla de terminal y evoluciona incorporando nuevas funcionalidades.

         PYTHON
            |
            v
       TERMINAL CLI
            |
            v
        INVENTARIO
            |
       +----+----+
       |         |
      CSV       CRUD
       |         |
       +----+----+
            |
            v
          VENTAS
            |
            v
         REPORTES

---

<div align="center">Sistema de Inventario

Desarrollado con Python desde la terminal.

</div>

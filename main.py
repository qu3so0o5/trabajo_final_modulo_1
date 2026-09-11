from modulo_constantes import *
import csv
import time

# Funcion para comprobar existenci del  archivo "data.csv"
def comprobando_existencia_de_archivos():
    nombre_archivo:list = ["./data.csv","./reporte_venta.csv","./reporte_venta.csv"]
    for i in nombre_archivo:
        try:
            with open(i,'r',encoding="utf-8") as arch:
                pass
        except FileNotFoundError:
            print(f"{ROJO_PASTEL}ERROR archivo {i} no encontrado...{RESET}")
# Parte visual para mostrar todo en una tambla
# Funcion para optener el maximo numero de caracteres de la columna "nombre"
def optener_maximo_num_caracteres_nombre():
    try:
        # Abrimos el archivo solo en modo lectura
        with open("./data.csv","r",encoding="utf-8") as arch:

            # Obteniendo objeto iterrable con arrays o listas de las filas del archivo 
            read_csv = csv.reader(arch)
            # Iniciando contador del maximo nro caracteres de la colunma name
            max_character:int = 0
            # Usando el objeto iterrable para onbtener los diccionarios

            for i in read_csv: # => en este caso i es un array o lista
                # Condicion para encontrar el valor de la columna "nombre" con mas caracteres
                if max_character < len(i[1]):
                    max_character:int = len(i[1])
            return max_character
    except:
        print("ERROR...")

#funcion para agregar producto
def agregar_producto():
    id_s = []
    with open("./data.csv",'r',encoding="utf-8") as arch:
            csv_reader = csv.reader(arch)
            for i in csv_reader:
                id_s.append(i[0])

    print(f"{NARANJA_CORAL}Recomendacion continuar la mumeracion de id {NEGRITA}{CELESTE_CIELO}(ultima ID = {id_s[-1]}){RESET}")
    while True:
        id_producto = input("Ingrese el id de tu producto: ")
        if not id_producto:
            print(f"{ROJO_PASTEL}El id no puede estar vacio...{RESET}")
            continue
        if id_producto in id_s:
            print(f"{ROJO_PASTEL}ID repetida, ingrese otra...{RESET}")
        else:
            break # ID válido, salimos del bucle

    nombre = input("Ingrese el nombre del producto: ")
    nombre = nombre.replace(" ","_")
    while True:
        precio_compra = input("Ingrese el precio de compra de produto: ")
        if precio_compra.isnumeric():
            break
        else:
            print(f"{ROJO_PASTEL}DATO INCORRECTO INTENTE DE NUEVO...{RESET}")

    while True:
        precio_venta =  input("Ingrese el precio de venta de produto: ")
        if precio_venta.isnumeric():
            break
        else:
            print(f"{ROJO_PASTEL}DATO INCORRECTO INTENTE DE NUEVO...{RESET}")

    while True:
        stock = input("Ingrese el stock del producto: ")
        if precio_venta.isnumeric():
            break
        else:
            print(f"{ROJO_PASTEL}DATO INCORRECTO INTENTE DE NUEVO...{RESET}")
    with open("./data.csv",'a',encoding="utf-8") as arch:
        arch.write(f"{id_producto},{nombre},{precio_compra},{precio_venta},{stock}\n")

# Funcion para mostrar visualmente mejor en forma de tabla los datos del archivo csv
def mostrar_productos():
    try:    
        # Abrimos el archivo solo en modo lectura
        with open("./data.csv",'r',encoding="utf-8") as arch:
            read_csv = csv.reader(arch)
            # Variable q indica el numero de tabulaciones por hacer dependiendo del numero de caracteres de la colunma "nombre"
            tab:int = 0
            # Obteniendo el maximo nro de caracteresd de la columna "nombre"
            max_character = optener_maximo_num_caracteres_nombre()

            # Imprimiendo los datos en forma de tabla
            print(f"{NARANJA_CORAL}=" * (24 + ((max_character // 8) + 3 ) * 8) + "=")
            for i in read_csv:
                if len(i[1]) < max_character:
                    tab = (max_character // 8) - (len(i[1]) // 8) + 1
                    print(f'{NARANJA_CORAL}|{RESET}{i[0]}',end="")
                    if len(i[1]) == 15:
                        print(f'\t{NARANJA_CORAL}|{CELESTE_CIELO}{i[1]}{RESET}{"\t"*(tab-1)}',end="")
                    else:
                        print(f'\t{NARANJA_CORAL}|{CELESTE_CIELO}{i[1]}{RESET}{"\t"*tab}',end="")
                    print(f'\t{NARANJA_CORAL}|{VERDE_MENTA}{i[2]}{RESET}',end="")
                    print(f'\t{NARANJA_CORAL}|{VERDE_MENTA}{i[3]}{RESET}',end="")
                    print(f'\t{NARANJA_CORAL}|{ROSA_PASTEL}{i[4]}\t{NARANJA_CORAL}|{RESET}',end="\n")
                    print(f"{NARANJA_CORAL}=" * (24 + ((max_character // 8) + 3 ) * 8) + "=")

    except:
        print("ERROR...")

# funcion para mostar datos por id
def mostrar_producto_id(id_producto:str):
     # Abrimos el archivo solo en modo lectura
    with open("./data.csv",'r',encoding="utf-8") as arch:
        read_csv = csv.reader(arch)
        # Variable q indica el numero de tabulaciones
        tab:int = 0
        # Obteniendo el maximo nro de caracteresd de la columna "nombre"
        max_character = optener_maximo_num_caracteres_nombre()
        for i in read_csv:
            if i[0] == id_producto:
                tab = (max_character // 8) - (len(i[1]) // 8) + 1
                print(f"\n",f"{NARANJA_CORAL}=" * (24 + ((max_character // 8) + 2 ) * 8) + "=",sep="")
                print(f'{NARANJA_CORAL}|{RESET}{i[0]}',end="")
                if len(i[1]) == 15:
                    print(f'\t{NARANJA_CORAL}|{CELESTE_CIELO}{i[1]}{RESET}{"\t"*(tab-1)}',end="")
                else:
                    print(f'\t{NARANJA_CORAL}|{CELESTE_CIELO}{i[1]}{RESET}{"\t"*tab}',end="")
                    print(f'\t{NARANJA_CORAL}|{VERDE_MENTA}{i[2]}{RESET}',end="")
                    print(f'\t{NARANJA_CORAL}|{VERDE_MENTA}{i[3]}{RESET}',end="")
                    print(f'\t{NARANJA_CORAL}|{ROSA_PASTEL}{i[4]}\t{NARANJA_CORAL}|{RESET}',end="\n")
                print(f"{NARANJA_CORAL}=" * (24 + ((max_character // 8) + 2 ) * 8) + "=\n")

def actulizar_producto(id_modificar:str):
    # Definiendo columnas, son las keys de los diccionarios :D
    columnas = ["id","nombre","p_compra","p_venta","stock"]
    # Lista vacia a la q se añade el diccionario modificado y los demas diccionarios
    new_csv = []
    
    # Opteneiendo todos los valores del csv en forma de diccionario y modificando el valor de stock del id especifico
    with open("./data.csv","r",encoding="utf-8",newline="") as arch:
        dict_csv = csv.DictReader(arch)

        for i in dict_csv:
            if i["id"] == id_modificar:
                print(MENU_2)
                campo = int(input("Ingrese la opcion del campo q decea modificar: "))
                if campo == 1:
                    i['nombre'] = input("Ingrese el nuevo nombre del producto: ").replace(" ","_")
                elif campo == 2:
                    i['p_compra'] = input("Ingrese el nuevo precio del producto: ").replace(" ","")
                elif campo == 3:
                    i['p_venta'] = input("Ingrese el nuevo precio del producto: ").replace(" ","")
                elif campo == 4:
                    i["stock"] = input("Ingrese el nuevo stcko del producto: ").replace(" ","")
                else:
                    print(f"{ROJO_PASTEL}Opcion invalida{RESET}")
            new_csv.append(i)
    
     # Escribiendo los datos modificados
    with open("./data.csv","w",encoding="utf-8",newline="") as arch:
        escritor = csv.DictWriter(arch,fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(new_csv)

def eliminar_producto(id_eliminar):
    
    # Definiendo columnas, son las keys de los diccionarios :D
    columnas = ["id","nombre","p_compra","p_venta","stock"]
    # Lista vacia a la q se añade el diccionario modificado y los demas diccionarios
    new_csv = []

    # Opteneiendo todos los valores del csv en forma de diccionario y modificando el valor de stock del id especifico
    with open("./data.csv","r",encoding="utf-8",newline="") as arch:
        dict_csv = csv.DictReader(arch)
        for i in dict_csv:
            if i["id"] == id_eliminar:
                print("ELIMINANDO PRODUCTO...")
            else:
                new_csv.append(i)

    # Escribiendo los datos modificados
    with open("./data.csv","w",encoding="utf-8",newline="") as arch:
        escritor = csv.DictWriter(arch,fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(new_csv)


# Modificar datos 

def añadir_stock(id_modificar:str):

    # Definiendo columnas, son las keys de los diccionarios :D
    columnas = ["id","nombre","p_compra","p_venta","stock"]
    # Lista vacia a la q se añade el diccionario modificado y los demas diccionarios
    new_csv = []

    # Opteneiendo todos los valores del csv en forma de diccionario y modificando el valor de stock del id especifico
    with open("./data.csv","r",encoding="utf-8",newline="") as arch:
        dict_csv = csv.DictReader(arch)
        for i in dict_csv:
            if i["id"] == id_modificar:
                cantidad = int(input("Ingrese la cantidad del producto que ingreso: "))
                i["stock"] = str(cantidad + int(i["stock"]))
            new_csv.append(i)

    # Escribiendo los datos modificados
    with open("./data.csv","w",encoding="utf-8",newline="") as arch:
        escritor = csv.DictWriter(arch,fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(new_csv)

def venta_de_producto(id_venta:int):
    
    # Definiendo columnas, son las keys de los diccionarios :D
    columnas = ["id","nombre","p_compra","p_venta","stock"]
    # Lista vacia a la q se añade el diccionario modificado y los demas diccionarios
    new_csv = []

    # Opteneiendo todos los valores del csv en forma de diccionario y modificando el valor de stock del id especifico
    with open("./data.csv","r",encoding="utf-8",newline="") as file:
        dict_csv = csv.DictReader(file)
        for i in dict_csv:
            if i["id"] == id_venta:
                cantidad:int = int(input("Ingrese la cantidad del producto que se vende: "))
                if int(i["stock"]) > cantidad:
                    i["stock"] = str(int(i["stock"]) - cantidad)
                    with open("./reporte_venta.csv","a",encoding="utf-8") as arch:
                        arch.write(f"{cantidad},{i['nombre']},{i['precio']}\n")
                else:
                    print(f"{ROJO_PASTEL}Ese numero excede la cantidad del stock...{RESET}")
            new_csv.append(i)

    # Escribiendo los datos modificados
    with open("./data.csv","w",encoding="utf-8",newline="") as arch:
        escritor = csv.DictWriter(arch,fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(new_csv)
def generar_reporte():
    pass
# Menu colorido         
def menu():
    while True:
        print(f'''
{BANER}{MORADO_SUAVE}{NEGRITA}
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
        {RESET}''')
        # Manejo de excepción por si el valor no es el correcto 
        try:
            opcion:int = int(input("Ingrese la opcion deceada: "))
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                mostrar_productos()
            elif opcion == 3:
                mostrar_producto_id(input("Ingrese el id del producto: "))
            elif opcion == 4:
                actulizar_producto(input("Ingrese el id del producto q decea actulizar: "))
            elif opcion == 5:
                eliminar_producto(input("Id del producto a eliminar: "))   
            elif opcion == 6:
                añadir_stock(input("Ingrese el id del producto: "))
            elif opcion == 7:
                venta_de_producto(input("Ingrese el id del producto: "))
            elif opcion == 8:
                print(f"salida con exito{"\n"*2}{VERDE_MENTA}··················")
                print(f"{VERDE_MENTA}··GRACIAS!!!!!!!··")
                print(f"{VERDE_MENTA}··················{RESET}{"\n"*2}")
                break
            else:
                print("opcion invalida...")
        except ValueError:
            print(f"{ROJO_PASTEL}ERROR DATO INVALIDO (ingrese un numero)...{RESET}")
# Manejo de error por si interrrupcion del usuario
try:
    menu()
except KeyboardInterrupt:
    print(f"\n{NEGRITA}{ROJO_PASTEL}Forzaste la salida del programas {CELESTE_CIELO}{NEGRITA}(ctrl + c)\n{RESET}")
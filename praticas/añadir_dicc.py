import os
os.system("cls")
from datos_rest import menu_total, menu_almuerzos
#from generar_cuentas import 

"""
Programa para solicitar al usuario elegir los platos del menu
Seleccionar que tipo de menu desea ver (Almuerzos o bebidas)
Ingresar 
""" 


def imprimir_productos(productos, titulo):
    """
    Imprime una lista de productos
    """
    print(f"\n=== {titulo} ===")

    for codigo, info in productos.items():
        nombre = info["nombre"].title()
        precio = info["precio"]
        print(f"{codigo:4} {nombre:25} ${precio:,}")


def opcion_menu(menu, categoria):
    """
    Permite al usuario seleccionar el menú que desea ver
    """
    if categoria == "1":
        imprimir_productos(menu["almuerzos"], "Almuerzos")

    elif categoria == "2":
        imprimir_productos(menu["bebidas"], "Bebidas")

    elif categoria == "3":
        for nombre_categoria, productos in menu.items():
            titulo = nombre_categoria.replace("_", " ").title()
            imprimir_productos(productos, titulo)

    else:
        print("Opción no válida")


opcion_cliente = input(
    "\nSeleccione el item del menu que desea conocer:\n"
    "1. Almuerzos\n"
    "2. Bebidas\n"
    "3. Ver todo el menu\n"
    "Opción: "
)

opcion_menu(menu_total, opcion_cliente)


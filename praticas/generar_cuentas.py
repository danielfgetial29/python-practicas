import os
os.system("cls")

# NOTAS DEL EJERCICIO 
"""
Una cuenta se genera apartir de varias cosas.
    1. items consumidos en el restaurante✅✅
    2. Sumar el valor de todos los items consumidos que sera la cuenta 
    3. Si el cliente desea añadir la propina a la cuenta con el porcentaje que el desee
Proceso que debe seguir el programa
    1. El usuario debe ingresar los items consumidos y cantidad ingresando su item para evitar erroes,
        las opciones se deben ver reflejadas en la consola
    2. el usuario debe elegir si/no si desea añadir propina a su cuenta
    3. se debe imprimir por consola la cuenta al usuario con los items que el selecciono
        , su precio individual y total 
    4. se debe ver el valor total de todos los items sin la propina, ver el valor unitario de la propina dependiendo del porcentaje
        y ver el valor con la propina 
    5. mensaje de gracias por su compra y despedida
""" 

# diccionarios
menu_almuerzos = {
    "A1": {"nombre": "pollo campesino", "precio": 42000},
    "A2": {"nombre": "sancocho de gallina", "precio": 38000},
    "A3": {"nombre": "chuleton de cerdo", "precio": 45000},
    "A4": {"nombre": "costilla san luis", "precio": 48000},
    "A5": {"nombre": "costillon montañero", "precio": 50000},
    "A6": {"nombre": "sancocho trifasico", "precio": 52000},
    "A7": {"nombre": "tilapia a la parrilla", "precio": 40000},
    "A9": {"nombre": "tilapia frita", "precio": 38000},
    "A10": {"nombre": "salmon", "precio": 60000}
}

menu_bebidas = {
    "B1": {"nombre": "limonada natural", "precio": 8000},
    "B2": {"nombre": "limonada de coco", "precio": 10000},
    "B3": {"nombre": "limonada de kiwi", "precio": 11000},
    "B4": {"nombre": "limonada cerezada", "precio": 10000},
    "B5": {"nombre": "jarra de mandarina", "precio": 15000},
    "B6": {"nombre": "jarra de coco", "precio": 18000},
    "B7": {"nombre": "jarra de jugo natural", "precio": 14000},
    "B8": {"nombre": "gaseosa personal", "precio": 5000},
    "B9": {"nombre": "gaseosa 1.5", "precio": 8000},
    "B10": {"nombre": "botella aguardiente", "precio": 90000}
}

def show_menu(menu,titulo):
    """
    muestra el menu al usuario
    """
    print(f"\n === {titulo} ===")
    for key, valor in menu.items():
        print(f"{key}. {valor["nombre"]}")

    

show_menu(menu_almuerzos, "Almuerzos")
show_menu(menu_bebidas, "BEBIDAS")

def choose_disk(almuerzos, bebidas, seleccion):
    """
    selecciona los platos consumidos y se guarda
    """
    items = seleccion.split(",")
    items_guardados = []

    for item in items:
        item = item.strip()

        if item in almuerzos:
            items_guardados.append(almuerzos[item])
        elif item in bebidas:
            items_guardados.append(bebidas[item])

    return items_guardados

def valor_cuenta(platos):
    """
    Calcula la suma de todos los items seleccionados 
    """
    cuenta = float(sum(item['precio'] for item in platos))
    return cuenta

def calcular_valor_propina (cuenta, porcentaje, propina):
    """
    Calcula el valor de la cuenta con la propina 
    """
    if propina == "SI":
        tip = float(cuenta * porcentaje ) / 100
        total_cuenta = float(cuenta + tip)
    else:
        tip = 0
        total_cuenta = cuenta
    
    return tip, total_cuenta

def show_check (platos):
    """
    Muestra al usuario por consola lo que selecciono
    """
    contador = 0

    for item in platos:
        contador += 1
        print(f"{contador}. {item['nombre']} - ${item['precio']}")
    
while True:

    # Mensajes en la consola

    print("=== GENERADORA DE CUENTAS DE UN RESTAURANTE ===")

    # Funcion de mostrar el menu 
    show_menu(menu_almuerzos, "Almuerzos")
    show_menu(menu_bebidas, "BEBIDAS")

    # Funcion de selecionar los platos 
    print("\nPOR FAVOR SELECCIONE LOS INSUMOS QUE CONSUMIO")

    seleccion = input("Selecciona los items de los alimentos y bebidas que consumiste\nseparados por comas (1,2,3...): ").upper()
    platos_seleccionados = choose_disk(menu_almuerzos, menu_bebidas, seleccion)

    # Mostrar factura con el valor y propina (si es el caso)
    print("\n === FACTURA ===")
    show_check(platos_seleccionados)
    cuenta = valor_cuenta(platos_seleccionados)
    print(f"Valor de la cuenta es: $ {cuenta:.2f}")

    propina = input("¿Desea agregar propina? (SI/NO): ").upper()

    if propina == "SI":
        porcentaje = float(input("Ingrese el porcentaje que desea \n añadir a su propina: %  "))
    else:
        porcentaje = 0

    valor_propina, valor_total = calcular_valor_propina(cuenta, porcentaje, propina)

    # Validador si el usuario ingresa la propina
    if propina == "SI":
        print(f"Valor propina: $ {valor_propina:.2f}")
        print(f"El valor total de su factura es: $ {valor_total:.2f}")
    else:
        print(f"El valor de su cuenta es: $ {cuenta:.2f}")

    # Respuesta para continuar o salir del ciclo 
    continuar = input("\nDesea hacer generar otra factura? (SI/NO): ").upper()

    if continuar != "SI":
        print("Gracias por su compra, vuelva pronto 👋")
        break
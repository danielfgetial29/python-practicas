import os
os.system("cls")

print("=== CALCULADORA DE PROPINAS ===")

def calcular_tip(cuenta_pagar, porcentaje):
    """
    Calcula el valor de la propina de una cuenta dependiendo de su porcentaje.
    """
    tip = (cuenta_pagar * porcentaje) / 100
    total = cuenta_pagar + tip
    return total, tip

while True:
    entrada = input("\nIngrese el valor a pagar (o escriba 'salir'): ")

    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break

    cuenta_pagar = float(entrada)
    porcentaje = float(input("Ingrese el porcentaje de propina: % "))

    valor_con_propina, propina = calcular_tip(cuenta_pagar, porcentaje)

    print(f"\nPropina: ${propina:.2f}")
    print(f"Total a pagar: ${valor_con_propina:.2f}")

import os
os.system("cls")

def calcular_media(a, b, par=None):
    """
    Calcula la media del rango [a, b].
    Si 'par' es 'si', solo considera números pares.
    Si 'par' es 'no', solo considera números impares.
    """
    if par == "si":
        numeros = [n for n in range(a, b + 1) if n % 2 == 0]
    elif par == "no":
        numeros = [n for n in range(a, b + 1) if n % 2 != 0]
    else:
        numeros = list(range(a, b + 1))

    if not numeros:
        return None
    return sum(numeros) // len(numeros)


def adivinar(a, b, par=None):
    """
    Función recursiva que adivina el número dentro del rango [a, b],
    usando pistas de paridad y mayor/menor.
    """
    intento = calcular_media(a, b, par)
    if intento is None:
        print("🤔 Parece que no hay números posibles con estas pistas.")
        return

    respuesta = input(f"\n¿Tu número es {intento}? (si/no): ").lower()

    if respuesta == "si":
        print("🎉 ¡He adivinado tu número!")
        return
    elif respuesta == "no":
        mayor_menor = input(f"¿Es mayor o menor que {intento}?: ").lower()
        par = input("¿Es par? (si/no): ").lower()

        # Reducimos el rango según la respuesta mayor/menor
        if mayor_menor == "mayor":
            nuevo_a = intento + 1
            nuevo_b = b
        elif mayor_menor == "menor":
            nuevo_a = a
            nuevo_b = intento - 1
        else:
            print("Respuesta inválida. Intentemos de nuevo.")
            nuevo_a, nuevo_b = a, b

        # Llamada recursiva con el nuevo rango y la paridad
        adivinar(nuevo_a, nuevo_b, par)
    else:
        print("Respuesta inválida. Intenta de nuevo.")
        adivinar(a, b, par)


# --- Flujo principal ---
print("=== ADIVINAR UN NÚMERO ===")
a, b = map(int, input("Introduce el rango (ej: 1 100): ").split())

adivinar(a, b)
import random

"""
Juego de piedra, papel o tijera
"""

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]


def opcion_maquina():
    """
    Genera aleatoriamente la elección de la máquina.
    """
    return random.choice(opciones)


def obtener_opcion_usuario():
    """
    Solicita al usuario una opción válida.
    Repite la pregunta hasta que la opción sea correcta.
    """

    while True:
        usuario = input(
            "Elige piedra, papel o tijera: "
        ).lower().strip()

        if usuario in opciones:
            return usuario

        print(
            "La opción ingresada es incorrecta. "
            "Intenta nuevamente.\n"
        )


def determinar_ganador(usuario, maquina):
    """
    Determina quién gana la partida.
    """

    victorias = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }

    print(f"\nLa computadora eligió: {maquina}")
    print(f"Tú elegiste: {usuario}")

    if usuario == maquina:
        print("¡Empate!")

    elif victorias[usuario] == maquina:
        print("¡Ganaste!")

    else:
        print("¡Perdiste!")


# Programa principal

jugador = obtener_opcion_usuario()

maquina = opcion_maquina()

determinar_ganador(jugador, maquina)
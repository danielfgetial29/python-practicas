try:
    # Solicitamos el valor por consola
    num = int(input("Ingrese un numero entero\n"))


    # verificamos que sea positivo
    if num > 0:
        print(f"{num} es POSITIVO")

    # verificamos que sea negativo
    elif num < 0:
        print(f"{num} es NEGATIVO")

    # si no es ni positivo ni negativo entonces es Cero
    else:
        print(f"El numero ingresado es {num}")

    # Lanzamos mensaje de error por consola para notificar al usuario que el numero
    # ingresado no es un entero
except ValueError:
    print("El numero ingresado no es un ENTERO")
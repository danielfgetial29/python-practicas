# algoritmo para analizar si un numero es 
# negativo o positivo

try:
    num = int(input("Por favor ingrese un valor ENTERO\n"))

    if num >= 0:
        print("El valor ingresado es POSITIVO")
    else:
        print("El valor ingresado es NEGATIVO")
except ValueError:
    print("El valor ingresado no es un entero, por favor diigtar de nuevo")


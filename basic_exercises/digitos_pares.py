## Leer un numero entero de dos dígitos y determinar si ambos dígitos son pares

num = int(input("Digite un numero entero de SOLO DOS CIFRAS\n"))

num_positivo = abs(num)

if 10 <= num_positivo <= 99:
    primerNumero = num_positivo // 10
    segundoNumero = num_positivo % 10

    if primerNumero % 2 == 0 and segundoNumero % 2 == 0:
        print(f"Los dos numeros de {num} son pares")

    else:
        print("Los dos numeros NO SON PARES")
else:
    print("El numero ingresado NO tiene DOS cifras")
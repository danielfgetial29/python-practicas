## algoritmo para verificar si el
# el ultimo numero es 4

num = int(input("Digite un número:\n "))
num2 = 4

    # validar si son positivos
if num < 0:
        num = num * -1

    # obtener ultimo digito atravez del residuo
ud = num % 10

if ud == num2:
        print(f"El ultimo digito de {num} es igual a {num2}")
else: 
    print("Los numeros no son iguales")

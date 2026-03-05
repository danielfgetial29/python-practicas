# algoritmo que identifica si un entero esta conformado por 
# 3 digitos 

num = int(input("Ingrese un entero\n"))

# Convertir a positivo
#if num < 0:
#    num = num * -1

cd = 0  # contador de dígitos

# caso que el entero ingresado sea un cero
if num == 0:
    cd = 1
else:
    # comienza el ciclo hasta que num no sea 0
    while num != 0: # compara que num sea diferente de 0 para realizar la instruccion
        num = num // 10 # la divide entre 10 y guarda el valor restante en num
        cd += 1 # al mismo tiempo suma 1 unidad a cd para llevar el contador de num

if cd == 3:
    print("El entero ingresado SÍ tiene 3 dígitos")
else:
    print("El entero ingresado NO tiene 3 dígitos")



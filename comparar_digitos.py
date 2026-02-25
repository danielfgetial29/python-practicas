# Inicializar las variables 
"""""
num1 = 187
num2 = 195

# verificar que no sean negativos y si lo son convertir a positivos
if num1 < 0:
    num1 = num1 * -1

if num2 < 0:
    num2 = num2 * -1

# Obtener el ultimo digito atravez del residuo 
ud1 = num1 % 10
ud2 = num2 % 10

# Comparamos si son o no iguales y mostramos el mensaje en la pantalla 
if ud1 == ud2:
    print("Los ultimos digitos son iguales")
else:
    print("Los ultimos digitnos no son iguales")
    """
respuesta = 176 % 10 
print(respuesta)
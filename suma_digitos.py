num = int(input("Por favor ingrese un número ENTERO de dos cifras\n"))

# Convertir a positivo
num_abs = abs(num)

# Verificar que tenga dos dígitos

"""""
En este bloque de codigo lo que haces es verficiar que el numero si tenga dos digitos
y eso lo hacemos verificando que el num_abs que es el numero ya positivo
sea menor o igual (<=) a 10, esto porque si es menor de 10 tendria solo un digito a menos que tenga un 0 delante
ej. 08. Tambien verificamos que sea menor o igual a 99 ya que si es mayor tendria tres digitos
99..,100, y asi verificariamos si el numero tiene las dos cifras que necesitamos

Seguido de eso si el numero cumple la condición entonces lo que haces es extraer su 
ultimo numero (decena) y guardarlo en una variable, esto lo hacemos dividendo el entero en 10
y para obtener el primer digito y con el  residuo % obtenemos el ultimo y tambien lo guardamos en 
una variable.
Seguido de eso ya pomos realizar la suma y mostramos el valor por consola 

"""""
if 10 <= num_abs <= 99:
    primerNumero = num_abs // 10 # decenas
    ultimoNumero = num_abs % 10 # unidades
    suma = primerNumero + ultimoNumero

    print(f"La suma de los dígitos de {num} es {suma}")
else:
    print("El número ingresado NO tiene dos cifras")
import os 
os.system("cls")
"""
CALCULADORA UTILIZANDO POO
"""

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    # Metodos
    def sumar(self):
        """
        Metodo para sumar los valores ingresados
        """
        return self.numero1 + self.numero2

    def restar(self):
        """
        Metodo de resta para los valores ingresados
        """        
        return self.numero1 - self.numero2


print("## CALCULADORA ## ")

#Valores a operar
num1 = int(input("Ingrese el primero valor:\n"))
num2 = int(input("Ingrese el segundo valor:\n"))

operacion = Calculadora(num1, num2)

#Operacion a realizar 
print("--- MENÚ DE OPCIONES ---")
print("1. SUMAR")
print("2. RESTAR")


while True:
    eleccion = int(input("Eliga que operacion realizar (1 / 2):\n"))


    if eleccion == 1:
        resultado = operacion.sumar()
        break

    elif eleccion == 2:
        resultado = operacion.restar()
        break

    else:
        print("Operacion no valida")

print(f"""
        CALCULADORA:\n
        Primer numero ingresado: {operacion.numero1}\n
        Segundo numero ingresado: {operacion.numero2}\n\n
        RESULTADO = {resultado}
        """)


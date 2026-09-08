import subprocess
subprocess.run("cls", shell=True)
# Probar lso atributos privados en Python por medio de un 
# ejercicio de un cajero automatico para que el usuario no 
# pueda manipular si valor, sin o el propio sistema 


class Cuentas:
    def __init__(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("INGRESE VALOR POSITIVO")

    def depositar(self, cantidad):
        """
        Decidir cuanto dinero se depositara
        """
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        """
        Ingresar la cantidad a retirar 
        """
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("No tienes suficiente dinero para retirar esa cantidad") 

micuenta_banco = Cuentas(2)

micuenta_banco.depositar(1)

micuenta_banco.retirar(1)


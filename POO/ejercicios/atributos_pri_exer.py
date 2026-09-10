import subprocess
subprocess.run("cls", shell=True)

class Cuenta:
    def __init__(self, titular, saldo):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self.__saldo = saldo

    def __monto_valido(self, cantidad):
        """Consulta internamente el saldo actual y 
            validar que no sea un valor negativo
        """
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return False
        return True
    # si es correcta el metodo se convierte en True, como aceptado
        
    def mostrar_saldo(self):
        """Muestra el saldo al usuario."""
        if self.__saldo > 0:
            print(f"Su saldo actual es: $ {self.__saldo:,}")
        else:
            print("No tiene dinero en la cuenta")

    def depositar(self, cantidad):
        """Realiza un depósito."""
        if not self.__monto_valido(cantidad): # y aqui lo que hacemos es que negamos el metodo privado
            return                            # para que no entre en este if de validacion, ya que si fue aceptado  
                                              # con el if not se negara y no entrara en este if, saltando a la siguiente   
        self.__saldo += cantidad              # linea de mi codigo  
        print(f"Depósito realizado correctamente: ${cantidad:,}")
        self.mostrar_saldo()

    def retirar(self, cantidad):
        """Realiza un retiro."""
        if not self.__monto_valido(cantidad):
            return

        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
            return
        self.__saldo -= cantidad
        print(f"Retiro realizado correctamente: ${cantidad:,}")
        self.mostrar_saldo()


# Crear cuenta
usuario = input("Por favor ingrese su nombre: ")
saldo_inicial = int(input("Ingrese el saldo inicial: "))

try:
    mi_cuenta = Cuenta(usuario, saldo_inicial)
except ValueError as e:
    print(e)
    exit()


while True:
    print("""
    ===== CAJERO AUTOMÁTICO =====

    1. Depositar
    2. Retirar
    3. Consultar saldo
    4. Salir
    """)

    try:
        eleccion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número.")
        continue

    if eleccion == 1:
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        mi_cuenta.depositar(cantidad)

    elif eleccion == 2:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        mi_cuenta.retirar(cantidad)

    elif eleccion == 3:
        mi_cuenta.mostrar_saldo()

    elif eleccion == 4:
        print("Gracias por utilizar el cajero.")
        break

    else:
        print("Opción no válida.")
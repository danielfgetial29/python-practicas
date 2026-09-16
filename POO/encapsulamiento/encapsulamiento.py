# Encapsulamiento\
import subprocess
subprocess.run("cls", shell = True)

class Clase:
    def __init__(self):
        self._atributo_privado = "Valor1"
        self.__atributo_super_privado= "Valor2"

miclase = Clase()
print(miclase.__atributo_super_privado)

class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!


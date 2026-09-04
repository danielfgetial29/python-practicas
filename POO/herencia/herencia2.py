import os
os.system("cls")

## HERENCIA

# Definimos una clase Padre
class Animal:
    pass

#Clase hija que hereda de la padre 
class Perro(Animal):
    pass

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        # return print(f"El {self.especie} {sonido}")
        pass

    def moverse(self):
        pass

    def descripcion(self):
        print("Soy un animal del tipo", type(self).__name__)
        #type(self).__name__ Obtiene el nombre de la clase que pertence el objeto

# class Perro(Animal):
#     pass

# mi_perro = Perro("Mamifero", 6)
# mi_perro.descripcion()

class Perro(Animal):
    def hablar(self):
        print("Guauu!!")

    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuuuu")

    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz")

    def moverse(self):
        print("Volando")

    # Nuevo metodo propio de esta clase Hija
    def defensa(self):
        print("Picar!")

class Serpiente(Animal):
    def hablar(self):
        print("Ssssss")

    def moverse(self):
        print("Arrastrandose")


mi_perro = Perro("Mamifero", 10)
mi_vaca = Vaca("Mamifero", 11)
mi_abeja = Abeja("Insecto", 2)
mi_serpiente = Serpiente("Rectil", 4)

mi_perro.hablar()
mi_vaca.hablar()
mi_abeja.hablar()
mi_serpiente.hablar()

mi_perro.descripcion()
mi_serpiente.descripcion()
mi_vaca.descripcion()
mi_abeja.descripcion()

mi_abeja.defensa()
# mi_vaca.defensa()
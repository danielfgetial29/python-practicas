import subprocess
subprocess.run("cls", shell=True)

"""
EJERCICIO DE HERENCIA MULTIPLE Y MRO

Crear tres clases Animal, Mamifero y Ave. La clase animal debe tener un metodo llamado
ciner, La clase Mamifero debe tener un metodo llamad amamantar y la clase Ave un metodo volar

tambien crear una clase Muercielago que herede de Mamifero y Ave, en ese orden y por lo tanto
debe poder utilizar sus metodos y ademas de comer

"""

#Clases Padre
class Animal():
    def comer(self):
        print("Todos los animales pueden comer")

# clases hijas
class Mamifero(Animal):
    def amamantar(self):
        print("Los mamiferos amamantan a sus crias")

class Ave(Animal):
    def volar(self):
        print("La mayoria de aves pueden volar")

#clase con herencia multiple
class Muercielago(Mamifero, Ave):
    pass

animal = Muercielago()
# animal.volar()
# animal.comer()
# animal.amamantar()

Muercielago.volar(animal)

print(Muercielago.mro())
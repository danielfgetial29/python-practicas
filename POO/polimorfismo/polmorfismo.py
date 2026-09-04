import subprocess
subprocess.run("cls", shell=True)

# Polimorfismo

class Gato():
    def sonido(self):
        print("Mia Miauuu")

class Perro():
    def sonido(self):
        print("Gua Guaaauu\n")

perro = Perro()
gato = Gato()

# Ejecuanto el mismo metodo pero con objetos diferentes
print("## EJECUTANDO LA CLASE PERRO")
perro.sonido()
print("## EJECUTANDO LA CLASE GATO")
gato.sonido()

#Polimorfismo de funcion
def sonido_perro():
    print("Guauu")

def sonido_gato():
    print("Miauu")

def sonido_vaca():
    print("Muuuuu")

def sonido_animales(animal):
    animal()

sonido_animales(sonido_perro)
sonido_animales(sonido_gato)
sonido_animales(sonido_vaca)

#ejemplo con clases
class Gato():
    def sonido(self):
        print("Mia Miauuu")

class Perro():
    def sonido(self):
        print("Gua Guaaauu\n")


def hacer_sonidos(animal):
    animal.sonido()

perro = Perro()
gato = Gato()
hacer_sonidos(perro)

#En un ciclo for
for animal in Perro(), Gato():
    animal.sonido()
    
# En una lista con las clases
animales = [Gato(), Perro()]
for animal in animales:
    animal.sonido()
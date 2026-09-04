import os
os.system("cls")
## HERENCIA MULTIPLE

# primera clase
class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_nacionalidad(self):
        return (f"Mi nacionalidad es {self.nacionalidad}")

#segunda clase
class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f"Mi habilidad es {self.habilidad}")

#clase que hereda las otras dos clases

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad,salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    #super(). para llamar el metodo directamente de la clase
    def llamar_nacionalidad(self):
        print(super().mostrar_nacionalidad())

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y trabajo en {self.empresa}\ny tengo un salario de {self.salario}")


daniel = EmpleadoArtista("Daniel", 25, "Colombiano","Jugar futbol",5000000.00,"Google")
daniel.presentarse()

daniel.mostrar_habilidad()
daniel.llamar_nacionalidad()

## DATOS A TENER EN CUENTA 
# Se recomienda seguir el orden logico de como se llaman las clases para que asi el 
#codigo sea facil de entender para cualquiera que lo vea
# class Padre():
#     pass

# class Madre():
#     pass

# class Hija(Padre, Madre):
#     def __init__(self):
#         Padre.__init__()
#         Madre.__init__()
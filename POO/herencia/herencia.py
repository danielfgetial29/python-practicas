import os
os.system("cls")

## HERENCIA

# Clase padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablandoooo")

class Empleado(Persona): 
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario): # dos parametros propios de esta clase hija
        super().__init__(nombre, edad, nacionalidad) # parametros heredados de la clase padre
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, carrera, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.notas = notas
        self.universidad = universidad

    def informacion(self):
        return (f"Hola soy {self.nombre} y tengo {self.edad} años\n",
            f"Actualmente estudio la carrera de {self.carrera} en la {self.universidad}\n",
            f"Y mi promedio de notas es de {self.notas}")

daniel = Empleado("Daniel", 25, "Colombiano", "Programador", 800000000)
daniel.hablar()

#clase estudiante (objetos)
mi_estudiante = Estudiante("Daniel", 25, "Colombiano", "Desarrollador", 5.0, "Universidad del Valle")
mi_estudiante.informacion()


# para poder ver de que clase es hija una clase 
print(Empleado.__bases__)

# Ver que clase descienden de una
print(Persona.__subclasses__())

# class Padre:
#     def __init__(self, atributoPadre1, atributoPadre2):
#         self.nombre_atributo1 = atributoPadre1
#         self.nombre_atributo2 = atributoPadre2

# class Hija(Padre):
#     def __init__(self, atributoPadre1, atributoPadre2, atributoNuevo_Hija):
#         super().__init__(atributoPadre1, atributoPadre2)
#         self.nomre_atributo_hija = atributoNuevo_Hija
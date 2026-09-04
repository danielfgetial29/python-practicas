import os, inspect
os.system("cls")

"""
EJERCICIO DE HERENCIA Y USO DE SUPER

Crear un sistema para una escuela. En este sistema debemos tener dos clases principales
Persona y Estudiante. La clase Peresona tendra los atributos de nombre y edad y un metodo 
que imprima el nombre y la edad de la pesona. La clase Estudiante heredara de la clase Persona 
y tambien tendra un atributo adicional: grado y un metodo que imprima el grado del estudiante


"""

#Clase Padre
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def show_datos(self):
        """
        Muestra el nombre y la edad de la persona 
        """    
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años👋"

#Clase Hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def show_grado(self):
        """
        Imprime el grado del estudiante
        """
        return f"Estoy en grado {self.grado}"

#Instancia
estudiante1 = Estudiante("Daniel", 25, "once")
print(inspect.cleandoc(f"""
        ## PRESENTACION DEL ESTUDIANTE\n
        {estudiante1.show_datos()}
        {estudiante1.show_grado()}
    """))
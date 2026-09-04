#Clases en POO
#Clase vacia 
class Perro:
    pass

#Objeto para la clase Perro
mi_perro = Perro()

#Atributos de instancia 
class Perro:
    #El metodo __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza

mi_perro = Perro("Sasha", "Criolla")
print(type(mi_perro))
#Acceder a los atributos
print(mi_perro.nombre)
print(mi_perro.raza)

#Atributos de clase
class Perro:
    #Atributo de clase
    especie = "mamifero"
    
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza
mi_perro2 = Perro("Negra", "Pitbull")
print(mi_perro2.especie)

mi_perro2.especie

class Perro:
    #Atributo de clase
    especie = "mamifero"
    
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        #Atributos de instancia 
        self.nombre = nombre
        self.raza = raza

    #Metodos 
    def ladrar(self):
        print("Gua Guaauuuuu...")

    def caminar(self, pasos):
        print(f"El perro camino {pasos} pasos")


mi_perro2 = Perro("Negra", "Pitbull")
mi_perro2.ladrar() #metodo sin parametros
mi_perro2.caminar(15) # metodo con parametros
print(mi_perro2.especie)
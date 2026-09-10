import subprocess
subprocess.run("cls", shell=True)

# Getters y Setters

class Persona():
    def __init__(self, nombre = "Lucas", edad = 23):
        self._nombre = nombre
        self._edad = edad

    # Getter
    def get_nombre(self):
        return self._nombre

    # Setters
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    # Getter 
    def get_edad(self):
        return self._edad

    # Setter
    def set_edad(self, new_edad):
        self._edad = new_edad

persona = Persona()
# print(persona._nombre)
persona.set_nombre("Daniel Felipe")
persona.set_edad(25)
nombre = persona.get_nombre()
edad = persona.get_edad()
print(nombre, edad)

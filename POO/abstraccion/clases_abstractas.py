import subprocess
subprocess.run("cls", shell=True)

from abc import ABC, abstractmethod
# clase abstracta usando el moduo abc

# clase molde, guia o abstracta 
class Saludar(ABC):

    @abstractmethod  
    def saludar_usuario(self):
        pass # debe ser pass ya que no haremos ninguna accion aqui

# clase que hereda la clase abstracta
class English(Saludar):

    def saludar_usuario(self):
        return "Hello everybody..."

class Spanish(Saludar):

    def saludar_usuario(self):
        return "Hola como estas..."

class French(Saludar):
    def saludar_usuario(self):
        return "Salut comment vas-tu"

saludo_en_ingles = English()
print(saludo_en_ingles.saludar_usuario())

saludar_en_frances = French()
print(saludar_en_frances.saludar_usuario())

saludar_en_espanol = Spanish()
print(saludar_en_espanol.saludar_usuario())
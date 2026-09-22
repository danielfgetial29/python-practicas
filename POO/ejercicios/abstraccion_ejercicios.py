import subprocess
subprocess.run("cls", shell=True)

from abc import ABC, abstractmethod

#Clase abstracta
class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        """
        Metodo abstracto que definiremos segun sea 
        necesario
        """
        pass

# Clases hijas
class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        """
        Calcula el area de un rectangulo
        """
        area = self.base * self.altura
        return area
        
class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self, pi):
        """
        Calcula el area de un circulo
        """
        area = pi * self.radio**2 
        return area

PI = 3.1416

#Instancias 
rectangulo = Rectangulo(10,6)
circulo =Circulo(4)



print(f"El area del rectangulo es: {rectangulo.calcular_area()}")
print(f"El area del circulo es  es: {circulo.calcular_area(PI):.2f}")
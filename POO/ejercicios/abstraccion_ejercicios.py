import subprocess, math
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

    def calcular_area(self):
        """
        Calcula el area de un circulo
        """
        area = math.pi * (self.radio**2)
        return area

# PI = 3.1416

#Instancias 
rectangulo = Rectangulo(10,6)
circulo =Circulo(4)

print("=== Primer Ejercicio === \n")

print(f"El area del rectangulo es: {rectangulo.calcular_area()}")
print(f"El area del circulo es  es: {circulo.calcular_area():.2f}")



class ServicioEnvio(ABC):

    @property
    @abstractmethod
    def costo_base(self):
        pass

    @abstractmethod
    def enviar(self):
        pass


# clase hija 
class EnvioNacional(ServicioEnvio):
    def __init__(self, destino, costo_base):
        self.destino = destino
        self._costo_base = costo_base

    @property
    def costo_base(self):
        return self._costo_base

    def enviar(self):
        return f"Enviado a {self.destino} por correo terrestre"

class EnvioInternacional(ServicioEnvio):
    def __init__(self, destino, costo_base):
        self.destino = destino
        self._costo_base = costo_base

    @property
    def costo_base(self):
        return self._costo_base

    
    def enviar(self):
        return f"Envio a {self.destino} por vía aérea"

# instancias 
envio_cali = EnvioNacional("Cali", 5.00)
envio_usa = EnvioInternacional("USA", 2.000)

print("\n=== Segundo Ejercicio === \n")

print(f"El costo para un envio en la ciudad de {envio_cali.destino} es de ${envio_cali.costo_base:.2f}")

print(f"El costo para un envio en la ciudad de {envio_usa.destino} es de ${envio_usa.costo_base:.2f}")
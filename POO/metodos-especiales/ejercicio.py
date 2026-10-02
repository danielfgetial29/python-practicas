# Crear un juego de fusion
# El jeugo consiste en crear personajes de un jeugo y que esos personajes
# se puedan fusionar para formar personajkes mas poderoos y que tengan mas poder
# 
# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando
# los personajes se fusionen, salgan un nuevo personaje con habilidades mejoradas
# 
# Un posible formula es: El promedio de las habilidades de ambos, al cuadrado
# 
# 

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):  
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} Fuerza: {self.fuerza} y velocidad {self.velocidad}"

    def __add__(self, other_pj):
        nuevo_nombre = self.nombre + "-" + other_pj.nombre
        new_strong = round(((self.fuerza + other_pj.fuerza)/2)**2) # promedio y lo elevo al cuadrado
        new_fast = round(((self.velocidad + other_pj.velocidad)/2)**2)
        return Personaje(nuevo_nombre, new_strong, new_fast)

goku = Personaje("Goku", 100, 100)
vegeta  = Personaje("Vegeta", 90, 190)

fusion = goku + vegeta
print(fusion)

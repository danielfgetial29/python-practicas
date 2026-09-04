import os
os.system("cls")

## TIPOS DE HERENCIA

## Herencia Multiple
# clase con varias clases al mismo tiempo
class Clase1:
    pass

class Clase2:
    pass

class Clase3(Clase1, Clase2):
    pass

#  MRO o Method Order Resolution
print(Clase3.__mro__)

#Heredar una clase atravez de otra clase
class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
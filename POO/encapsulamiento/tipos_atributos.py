import subprocess
subprocess.run("cls", shell=True)

#Tipos de atributos

#Publicos
class Ejemplos_Atributos:
    def __init__(self, atributo_publico):
        self.atributo_publico = atributo_publico

miclase = Ejemplos_Atributos("Publico") 
print(miclase.atributo_publico)

#Atributos Protegidos:
class Ejemplos_Atributos:
    def __init__(self, atributo_protegido):
        self._atributo_protegido = atributo_protegido

miclase = Ejemplos_Atributos("Atributo Protegido") 
print(miclase._atributo_protegido)

# Atributos Privados
class Ejemplos_Atributos:
    def __init__(self, atributo_privado):
        self.__atributo_privado = atributo_privado

miclase = Ejemplos_Atributos("Atributo Privado🔑") 
print(miclase.__atributo_privado)
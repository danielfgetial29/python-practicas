import subprocess
subprocess.run("cls", shell=True)

# Decoradores @property

class Clase():
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo
    
# try:
#     mi_clase = Clase("Hola atributo")
#     print(mi_clase.mi_atributo()) # llamo a .mi_atributo como si fuera un metodo
# except TypeError as e:             # para probrar capturar su error
#     print(f"Error de tipo {e}")

try:
    mi_clase = Clase("Hola atributo")
    print(mi_clase.mi_atributo)
except TypeError as e:
    print(f"Error de tipo {e}")
import subprocess
subprocess.run("cls", shell=True)

# Decoradores @property

class Clase():
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        # El acceso se realiza a través de este "método" y
        # podría contener código extra y no un simple retorn
        return self.__mi_atributo

    @mi_atributo.setter
    def mi_nuevo_atributo(self, new_atributo):
        self.__mi_atributo = new_atributo
        return self.mi_atributo
# try:
#     mi_clase = Clase("Hola atributo")
#     print(mi_clase.mi_atributo()) # llamo a .mi_atributo como si fuera un metodo
# except TypeError as e:             # para probrar capturar su error
#     print(f"Error de tipo {e}")

try:
    # usando el getter *@property se lee directamente sin ()
    mi_clase = Clase("Hola atributo")
    print(mi_clase.mi_atributo) 
    
    # usando setter cambiamos asignamos el valor directamente como una varaible
    mi_clase.mi_nuevo_atributo = "Hola nuevo atributo"
    print(mi_clase.mi_nuevo_atributo)
    
except TypeError as e:
    print(f"Error de tipo {e}")
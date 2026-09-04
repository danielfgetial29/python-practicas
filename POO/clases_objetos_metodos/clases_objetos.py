import os
os.system("cls")
# class NombreClase():
#     propiedad_1 = "Valor 1"
#     propiedad_2 = "Valor 2"
#     propiedad_3 = "Valor 3"
# # %%
# class Celular():
#     marca = "Iphone"
#     modelo = "17"
#     camara = "48MP"

# celular1 = Celular()
# print(celular1.marca)               

# class NombreClase:
#     def __init__(self, parametro1, parametro2, parametro_n...):
#         self.nombre_atributo1 = parametro1  # Dato recibido del parametro1
#         self.nombre_atributo2 = parametro2  # Dato recibido del parametro1
#         self.nombre_atributoN - parametro_n # Dato recibido del parametro_n

# objeto_de_la_clase = NombreClase("Argumento1", "Argumento2", "Argumento_n...")

# class NombreClase:
#     def __init__(self):
#         pass
#%%
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.marca} {self.modelo}...")

    
    def colgar(self):
        print(f"Colgaste la llamada desde un telefono {self.marca} {self.modelo}")

celular1 = Celular("Iphone", "17 Pro", "48MP")   
#print(celular1.camara)

celular1.llamar()
celular1.colgar()
# %%


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

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Ipohne", "17 Pro", "48MP")   

print(celular1.camara)


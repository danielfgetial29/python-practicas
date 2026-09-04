# Ejercicio con clases de animales utilizando la herencia multiple

class Animal():
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_especie(self):
        """
        Metodo que permitira mostrar la especie del animal
        """
        return (f"Esta especie es un: {self.especie}")

class Mascota():
    def __init__(self, nombre_dueno, tipo_mascota):
        self.nombre_dueno = nombre_dueno
        self.tipo_mascota = tipo_mascota

    def mostrar_tipo(self):
        """
        Metodo que permite mostrar el tipo de mascota
        """
        return (f"es de tipo {self.tipo_mascota}")

class AnimalDomestico(Animal, Mascota):
    def __init__(self, nombre, edad, especie,nombre_dueno, tipo_mascota, peso, nombre_clinica):
        Animal.__init__(self,nombre, edad, especie)
        Mascota.__init__(self, nombre_dueno, tipo_mascota)
        self.peso = peso
        self.nombre_clinica = nombre_clinica

    def presentacion(self):
        """
        Metodo que describe todas las cualidades del animal
        """
        # print(f"El nombre de esta mascota es {self.nombre}\n,{super().mostrar_especie()}, y {super().mostrar_especie()}")
        print(f"""
            El nombre de esta mascota es {self.nombre}\n     
            Tiene una edad de {self.edad} años\n
            {super().mostrar_especie()}  y {super().mostrar_tipo()}.\n
            Aparte su dueño se llama {self.nombre_dueno}\n
            Su peso es de {self.peso} kg y lo atienden en {self.nombre_clinica}
                """)

mascota1 = AnimalDomestico("Max", 5, "Perro", "Daniel", "Domestico", 20, "Veterinaria Central")

mascota1.presentacion()
print("==== Usando .mro() ===")
print(AnimalDomestico.mro())
print("==== Usando .__mro__ ===")
print(AnimalDomestico.__mro__)
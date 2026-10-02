import os
os.system("cls")


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # # Metodo especial para volver algo un str
    def __str__(self):
        return f'Persona(nombre = "{self.nombre}", edad ={self.edad})'

    # Similar al metodo __str__ pero es para reprentar a la clase, debe 
    # repr() para envolver la instancia y eval() si queremos acceder o mostrar a sus propiedades
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'

    # Sobre carga de operadores
    # Me permite poder decidir que sucede si agrego un dato mas a mi clase
    # puedo aplicar los signos aritmeticos para operar con ellos
    def __add__(self, other):
        # En este ejemplo defino un nuevo dato para poder sumar los atibutos de una 
        # o mas instancias 
        nuevo_valor = self.edad + other.edad
        
        return Persona(self.nombre + other.nombre, nuevo_valor)

daniel = Persona("Daniel", 25)
felipe = Persona("Felipe", 10)

nuevo_dato = daniel + felipe
print(nuevo_dato.nombre)
# print(daniel)

# repre = repr(daniel)
# # print(repre)

# resultado = eval(repre)
# print(resultado.nombre)
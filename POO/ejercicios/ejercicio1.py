import os
os.system("cls")
"""
EJERCICIO 1
crear una clase estudiante que tenga los atributos nombre, edad y grado
Ademas agregar un metodo que se llame estudiar que imprima "el estudiante {nombre} esta estudiando
crear un objeto estudiante y usar el metodo estudiar()


"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        """
        Imprime mensaje informativo del estudiante
        """
        print(f"El estudiante {self.nombre} esta estudiando el grado {self.grado} en este momento 📖")

#Lista de grados válidos en letras 
grados_validos = ["primero", "segundo", "tercero", "cuarto", "quinto", 
                  "sexto", "séptimo", "octavo", "noveno", "décimo", "once"]

# Variables que recibe el objeto estudiante()
nombre = input("Por favor ingrese su nombre:\n")
edad = input("Por favor ingrese su apellido: ")

#Ciclo para que ingrese la respuesta correcta nuevamente en caso de ValueError
while True:
    #Manejo de excepciones para verificar que ingrese dato dentro de la lista de grados
    try:
        grado = input("Ingrese el año que se encuentra cursando: ").lower().strip()

        # Condicion que verifica que el dato este en la lista
        if grado not in grados_validos:
            raise ValueError

        # salir del bucle al momento que todo este correcto
        break

    except ValueError:
        print("Error al ingresar el año cursado ")

estudiante = Estudiante(nombre.capitalize(), edad, grado)
estudiante.estudiar()

print(f"""
        DATOS DEL ESTUDIANTE:\n
        Nombre: {estudiante.nombre}\n
        Edad: {estudiante.edad}\n
        Grado: {estudiante.grado}
        """)

# #Tipos de Metodos
# Metodos de instancia normales como metodo()
# DE clase usando el decorador @classmethod
# Y  estaticos usando el decorador staticmethod

class Clase:
    def metodo(self):
        return 'Metodo Normal', self

    @classmethod
    def metodo_clase(cls):
        return 'Metodo de Clase', cls

    @staticmethod
    def metodo_estatico():
        return "Metodo Estatico"

# Metodo de instacia 
class Clase:
    def metodo(self, arg1, arg2):
        return 'Metodo normal', self # self representa la instancia misma del objeto (mi_clase)

mi_clase = Clase()
mi_clase.metodo(1, 2)


#Metodos de clase
class Clase:
    @classmethod
    def metodo_clase(cls):
        return 'Metodo de Clase', cls

#Se puede llamar sobre la clase
Clase.metodo_clase()

# Y tambien sobre el objeto
mi_clase = Clase()
mi_clase.metodo_clase()


#Metodos estaticos (staticmethod)
class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"
mi_clase = Clase()
Clase.metodoestatico()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'
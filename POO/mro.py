import os
os.system("cls")

#MRO

class E():
    pass

class A():
    # def hablar(self):
    #     print("Saludo desde A..")
    pass
class B(E):
    def hablar(self):
        print("Saludo desde B..")

class C(A):
    # def hablar(self):
    #     print("Saludo desde C..")
    pass
class D(C,B):
    pass
    # def hablar(self):
    #     print("Saludo desde D..")

prueba_mro = D()

prueba_mro.hablar()

#.mro() Metodo que devuelve una lista
print(D.mro())

#.__mro__  Atributo que devuelve una tupla
print(D.__mro__)

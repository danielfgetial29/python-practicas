import os
os.system("cls")

#MRO

class A():
    def hablar(self):
        print("Hola desde A...")

class C(A):
    def hablar(self):
        print("Hola desde C...")

class B(C):
    def hablar(self):
        print("Hola desde B...")

class D(B):
    def hablar(self):
        print("Hola desde D...")

class F(D):
    def hablar(self):
        print("Hola desde F...")

mro = F()
print(F.mro())
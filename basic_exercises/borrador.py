import os
os.system("cls")

a, b = map(int, input("Ingrese dos numeros enteros separados por espacio: ").split())

mi_lista = []

for i in range(a, b + 1):
    mi_lista.append(i)

print(mi_lista)
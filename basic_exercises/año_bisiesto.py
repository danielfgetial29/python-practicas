# Calculadora de años Bisiestos

year = int(input("Ingrese un año:\n"))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0) :
    print(f"El año {year} es Bisiesto")
else:
    print(f"{year} No es un año Bisiesto")
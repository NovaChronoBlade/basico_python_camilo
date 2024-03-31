# 5. *Generador de Tablas de Multiplicar:*
#    - Desarrolla un programa que genere la tabla de multiplicar de un número ingresado por el usuario utilizando repeticiones y operadores aritméticos.


# numero = int(input("Ingresa el nunmero del cual quieres las tablas: "))

numero = 5


for i in range(1, 11):

    print(f"{numero} x {i} = {numero * i}")
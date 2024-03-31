# 8. *Simulador de Cuenta Regresiva:*
#    - Desarrolla un programa que simule una cuenta regresiva con diferentes decrementos a partir de entradas ingresadas por el usuario, utilizando repeticiones y operadores aritméticos.


# base = int(input("Ingrese el numero del conteo: "))
# decremento = int(input("Ingrese el numero del decremento: "))


base = 10
decremento = 2

while base > 0:
    
    print(f"Cuenta regresiva: {base}")
    base = base - decremento

    if base <= 0:
        print(f"Cuenta regresiva: {base}")
        print("Go!!!")
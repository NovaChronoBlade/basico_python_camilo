# 2. *Adivina el Número:*
#    - Desarrolla un juego en el que el programa elige un número aleatorio y el usuario debe adivinarlo. El programa proporciona pistas (mayor/menor) para ayudar al usuario a encontrar el número.


import random

number = random.randint(1, 20)

print(number)


nose = False

while nose != True:

    try:
        
        nr = int(input("Dame un numero un numero: "))
        
        if nr == number:
            print("Haz adivinado el numero")
            nose = True

                        
        elif nr > number:
            print("El numero no es correcto es menor")
                        
        elif nr <  number:
            print( "El numero no es correcto es mayor")
                        
    except Exception as e:
        print("Valor incorrecto")



        





#Hecho por Camilo Mosquera
# 1. *Simulador de Juego de Dados:*
#    - Crea un programa que simule un juego de dados en el que el usuario apuesta a un número. El programa debe generar dos números aleatorios y determinar si el usuario gana o pierde según su elección.

import random

def dados_game(numero):

    try: 

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        print(d1)
        print(d2)

        numero = int(numero)

        if numero == d1 or numero == d2:
            return "Haz ganado la apuesta"
        else:
            return "Intentalo de nuevo"

    except Exception as e:
        return "Ingresaste un valor incorrecto"
    

apuesta = 1

juego = dados_game(apuesta)

print(juego)


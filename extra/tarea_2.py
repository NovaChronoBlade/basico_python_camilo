# 2. *Contador de Vocales:*
#    - Desarrolla un programa que cuente la cantidad de vocales (a, e, i, o, u) en una palabra ingresada por el usuario. Utiliza condicionales y repeticiones para realizar el conteo y muestra el resultado.


def contador_vocales(palabra):

    vocales = ["a", "e", "i", "o", "u"]

    n_vocales = 0


    for i in range(0, len(palabra)):
        if palabra[i] in vocales:
            n_vocales = n_vocales + 1


    print(f"Hay en total: {n_vocales} vocales")


contador_vocales("camilo")

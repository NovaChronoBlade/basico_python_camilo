# Comparaciones de Edades: Crea un programa que compare tres edades para determinar quién es el más viejo y quién es el más joven. Usa declaraciones if/elif/else
# para realizar las comparaciones.

def comparacion_edades(edad,edad_2,edad_3):
    if edad >= edad_2 and edad >= edad_3:
        mayor = "La primera persona es la más vieja."
    elif edad_2 >= edad and edad_2 >= edad_3:
        mayor = "La segunda persona es la más vieja."
    else:
        mayor = "La tercera persona es la más vieja."

    return mayor


resultado = comparacion_edades(25, 12, 50)
print(resultado)
# Ejercicio 3:
# Crea un programa que imprima la siguiente suma en la pantalla:


def x_spaces(string, n):
    return f"{string:>{n}}"


print(x_spaces("1", 6) + "\n" + x_spaces("20", 6) + "\n" + x_spaces("300", 6) + "\n" + "+ " + x_spaces("4000", 3) + "\n" + "-"*6 + "\n" + x_spaces("4321", 6)) 
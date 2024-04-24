# Calculadora de Calificaciones: Crea un programa que calcule y muestre la calificación
# en letra basada en una calificación numérica dada. Usa declaraciones if/elif/else
# para asignar la calificación en letra apropiada


def calcular_calificacion(calificacion):
    if 4.5 <= calificacion <= 5.0:
        return "A"
    elif 4.0 <= calificacion < 4.5:
        return "B"
    elif 3.5 <= calificacion < 4.0:
        return "C"
    elif 3.0 <= calificacion < 3.5:
        return "D"
    elif 2.0 <= calificacion < 3.0:
        return "E"
    elif 1.0 <= calificacion < 2.0:
        return "F"
    else:
        return "Calificación fuera de rango"
calificacion = 60

print(calcular_calificacion(calificacion))


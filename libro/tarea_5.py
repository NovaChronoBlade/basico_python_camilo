# Recomendador de Música según Grupo de Edad: Escribe un programa que clasifique
# a una persona en diferentes grupos de edad según su edad y recomiende bandas
# de música apropiadas. Usa declaraciones if/elif/else para categorizar el grupo de
# edad.


def recomendar_musica(edad):
    if 10 <= edad <= 19:
        return "Para adolescentes entre 10 y 19 años, recomendamos artistas como Billie Eilish, Peso Pluma y BTS."
    elif 20 <= edad <= 29:
        return "Para jóvenes adultos entre 20 y 29 años, recomendamos artistas como Dua Lipa, The Weeknd y Travis Scott."
    elif 30 <= edad <= 39:
        return "Para adultos entre 30 y 39 años, recomendamos bandas como Shakira, rihanna y Adele."
    elif 40 <= edad <= 49:
        return "Para quienes están entre 40 y 49 años, recomendamos clásicos como U2, Juan Gabriel y Luis Miguel."
    elif 50 <= edad <= 59:
        return "Para personas entre 50 y 59 años, recomendamos artistas como Bruce Springsteen, Madonna y The Cure."
    elif 60 <= edad <= 69:
        return "Para personas entre 60 y 69 años, recomendamos a The Rolling Stones, Fleetwood Mac y Elton John."
    elif 70 <= edad <= 80:
        return "Para personas entre 70 y 80 años, recomendamos clásicos como Frank Sinatra, The Beatles y Aretha Franklin."
    else:
        return "La edad proporcionada no está en el rango válido (10-80 años). Por favor, ingresa una edad dentro del rango permitido."

edad_usuario = 25
recomendacion = recomendar_musica(edad_usuario)
print(recomendacion)

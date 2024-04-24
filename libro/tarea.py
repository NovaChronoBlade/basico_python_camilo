# Traductor de Emojis: Escribe un programa que traduzca un emoticón de texto a
# su significado correspondiente. Usa una sentencia match/case para determinar los
# significados.


def traducir_emoticon(emoticon):
    match emoticon:
        case ":)":
            return "Carita feliz"
        case ":v":
            return "Pac Man grasa"
        case ":(":
            return "Carita triste"
        case ":D":
            return "Carita sonriente"
        case "XD":
            return "Xddddd"
        case ":P":
            return "Sacando la lengua"
        case ";)":
            return "Guiñando un ojo"
        case _:
            return "Emoticón desconocido"

emoticon = ":v"
resultado = traducir_emoticon(emoticon)
print(resultado)

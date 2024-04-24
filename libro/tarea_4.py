# Juego de Piedra, Papel o Tĳera: Implementa un sencillo juego de piedra, papel o
# tĳera por consola. Usa declaraciones match/case para determinar el ganador según las
# elecciones de los jugadores.
import random

def piedra_papel_tijeras(mano):
    mano = mano.lower()
    tipos = ['piedra', 'papel', 'tijeras']
    bot = random.choice(tipos)

    if mano not in tipos:
        return "Entrada no válida. Por favor elige entre 'piedra', 'papel' o 'tijeras'"

    match mano:
        case "piedra":
            match bot:
                case "piedra":
                    return "Es un empate."
                case "papel":
                    return "Tu eliges piedra y el bot elige papel. Lo siento, perdiste."
                case "tijeras":
                    return "Tu eliges piedra y el bot elige tijeras. ¡Ganaste!"
        case "papel":
            match bot:
                case "piedra":
                    return "Tu eliges papel y el bot elige piedra. ¡Ganaste!"
                case "papel":
                    return "Es un empate."
                case "tijeras":
                    return "Tu eliges papel y el bot elige tijeras. Lo siento, perdiste."
        case "tijeras":
            match bot:
                case "piedra":
                    return "Tu eliges tijeras y el bot elige piedra. Lo siento, perdiste."
                case "papel":
                    return "Tu eliges tijeras y el bot elige papel. ¡Ganaste!"
                case "tijeras":
                    return "Es un empate."

mano = "papel"

juego = piedra_papel_tijeras(mano)

print(juego)
# 4. *Conversor de Temperatura:*
#    - Crea un programa que convierta la temperatura de grados Celsius a Fahrenheit o viceversa, según la elección del usuario.

def conversor(temperatura, de_tipo, a_tipo):

    if de_tipo == a_tipo:
        return "Ingresaste la misma conversion"
    
    if de_tipo == "1":
        if a_tipo == "2":
            return f"La temperatura esta en: {(temperatura * 9/5) + 32}°F"
        elif a_tipo == "3":
            return f"La temperatura esta en: {temperatura + 273.15}K"
    elif de_tipo == "2":
        if a_tipo == "1":
            return f"La temperatura esta en: {(temperatura - 32) * 5/9}°C"
        elif a_tipo == "3":
            return f"La temperatura esta en: {(temperatura + 459.67) * 5/9}K"
    elif de_tipo == "3":
        if a_tipo == "1":
            return f"La temperatura esta en: {temperatura - 273.15}°C"
        elif a_tipo == "2":
            return f"La temperatura esta en: {temperatura * 9/5 - 459.67}°F"


# temperatura = int(input("Ingrese la temperatura: "))

# menu = '''
# Tu temperatura esta en:
# 1. Celsius
# 2. Fahrenheit
# 3. Kelvin'''

# print(menu)

# tipo = input("Ingrese el valor: ")

# menu_2 = '''
# La temperatura lo pasas a:
# 1. Celsius
# 2. Fahrenheit
# 3. Kelvin'''

# print(menu_2)

# a_tipo = input("Ingrese el valor: ")
        
# print(conversor(temperatura, tipo, a_tipo))


# base = 100  #temperatura
# celsius = "1"
# fahrenheit = "2"

# print(conversor(base, celsius, fahrenheit))






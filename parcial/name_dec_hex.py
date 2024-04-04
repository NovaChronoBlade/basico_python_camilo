import math

def dec_to_bin(decimal):
    binario = []

    while decimal > 0:
        binario.append(str(decimal % 2))
        decimal = math.floor(decimal / 2)

    binario.reverse()
    return "".join(binario)

def name_to_bin(full_name):
    words = []

    for i in range(len(full_name)):
        if full_name[i] != ' ':
            words.append(dec_to_bin(ord(full_name[i])))

    return words

def dec_to_hex(numero):
    hex_diccionario = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    result = []
    
    while numero > 0:
        residuo = numero % 16
        
        if residuo >= 10:
            result.append(hex_diccionario[residuo])
        else:
            result.append(str(residuo))
        
        numero //= 16
    
    result.reverse()
    
    numero_hexadecimal = ''.join(result)
    
    return numero_hexadecimal


def name_hex(full_name):
    words = []

    for i in range(len(full_name)):
        if full_name[i] != ' ':
            words.append(dec_to_hex(ord(full_name[i])))

    return words

nombre = "Juan Camilo Mosquera Palomino"

print(name_to_bin(nombre))
print(name_hex(nombre))





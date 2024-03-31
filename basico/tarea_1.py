# 1. *Calculadora Simple:*
#    - Crea un programa que solicite al usuario dos números y realice operaciones aritméticas básicas (suma, resta, multiplicación, división) con ellos.


def aritmetica(valor, n1, n2):

    try: 
        if valor == 1:
            result = n1 + n2
            return f"La suma de: {n1} + {n2} = {result}"
        
        elif valor == 2:
            result = n1 - n2
            return f"La resta de: {n1} - {n2} = {result}"
        
        elif valor == 3:
            result = n1 * n2
            
            return f"La multiplicacion de: {n1} x {n2} = {result}"
        
        elif valor == 4:
            result = n1 / n2
            return f"La division de: {n1} / {n2} = {int(result)}"
        
    except Exception as e:
        return "Ha ingresado un valor incorrecto."

# menu = '''
# 1. Suma
# 2. Resta
# 3. Multiplicacion
# 4. Dvision'''

# print(menu)

# valor = int(input("Ingrese el valor aritmetico que quiere usar: "))

# n1 = int(input("Ingrese el primer numero: "))
# n2 = int(input("Ingrese el segundo numero: "))


n1 = 2
n2 = 4
valor = 3


resultado = aritmetica(valor, n1, n2)

print(resultado)






#Hecho por Camilo Mosquera
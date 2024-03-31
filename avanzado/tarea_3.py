# 3. *Verificador de Palíndromos:*
#    - Escribe un programa que verifique si una palabra o frase ingresada por el usuario es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda, utilizando condicionales y repeticiones.

def palindromo(palabra):
    

    reserva = len(palabra)

    original = []
    comparacion = []

    for i in range(0, reserva):
        original.append(palabra[i])

    base = len(original) - 1
   
    while base > -1:
        comparacion.append(original[base])
        base = base - 1

    for i in range(0, reserva):
        if original[i] != comparacion[i]:
            return print("No es")
              
    print("Es un palindromo")        


palabra = "reconocer"

palindromo(palabra)


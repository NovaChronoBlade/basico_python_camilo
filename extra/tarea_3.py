# 3. *Reverso de Palabra:*
#    - Escribe un programa que reciba una palabra y muestre su reverso. Utiliza la manipulación de strings para lograr este resultado.


def reversa(palabra):
    

    reserva = len(palabra)

    original = []
    comparacion = []

    for i in range(0, reserva):
        original.append(palabra[i])

    base = len(original) - 1
   
    while base > -1:
        comparacion.append(original[base])
        base = base - 1


              
    print("".join(comparacion))


reversa("camilo")



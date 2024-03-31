# 7. *Calculadora de IMC (Índice de Masa Corporal):*
#    - Crea un programa que calcule el IMC a partir del peso y la altura ingresados por el usuario, y luego indique en qué rango se encuentra el IMC calculado.


# peso = int(input("Ingrese el peso en kg: "))
# altura = int(input("Ingrese la altura en cm: "))


def IMC(peso, altura):

    altura = altura / 100

    imc = round(peso / (altura)**2, 1)

    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc <= 24.9: 
        return "Normal"
    elif 25 <= imc <= 29.9:  
        return "Sobrepeso"
    else:  
        return "Obeso"
    


peso = 120
altura = 170
estado = IMC(peso, altura)
print(f"Su estado actual es: {estado}")
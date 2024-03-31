# 10. *Calculadora de Descuentos:*
#     - Crea un programa que calcule el precio final de un producto considerando un descuento ingresado por el usuario, utilizando operadores aritméticos y condicionales.


def calcular(original, descuento):
    
    descuento = (original * descuento) / 100
    
    final = original - descuento
    
    return final

# original = float(input("Ingrese el precio original: "))
# descuento = float(input("Ingrese el descuento: "))

original = float(20000)
descuento = float(50)

final = calcular(original, descuento)

print(f"El precio final con el descuento {descuento}% es: {round(final)}")


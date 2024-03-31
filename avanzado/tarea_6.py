# 6. *Calculadora de Ecuaciones Cuadráticas:*
#    - Escribe un programa que resuelva ecuaciones cuadráticas a partir de los coeficientes ingresados por el usuario, utilizando condicionales, operadores aritméticos y la fórmula cuadrática.

import math

print('teniendo en cuenta la ecuacion ax^2+bx+c=0')
print('-'*70)
# a = int(input('Introduce el valor de a: '))
# b = int(input('Introduce el valor de b: '))
# c = int(input('Introduce el valor de c: '))

a = 5
b = 23
c = 12

print('-'*70)
#calculo extra
d = (b**2)-4*a*c

#mas calculos

if d < 0:
    print('No hay solucion posible')

x1 = (-b+math.sqrt(d))/(2*a) 
x2 = (-b-math.sqrt(d))/(2*a)
 
print('-----Soluciones-----')
print('Solucion x1', x1)
print('Solucion x2', x2)
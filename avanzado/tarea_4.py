# 4. *Generador de Secuencias de Fibonacci:*
#    - Crea un programa que genere los primeros n números de la secuencia de Fibonacci, donde cada número es la suma de los dos anteriores, utilizando repeticiones y variables.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_veces = 5
for i in range(n_veces):
    print(fibonacci(i))






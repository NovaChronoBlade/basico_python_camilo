# 6. *Verificador de Números Primos:*
#    - Escribe un programa que verifique si un número ingresado por el usuario es primo o no, utilizando condicionales y repeticiones.


def n_primos(numero):
    if numero <= 1:
        return False  
    for i in range(2, numero):
        if numero % i == 0:
            return False  
    return True  

numero = 100

if n_primos(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

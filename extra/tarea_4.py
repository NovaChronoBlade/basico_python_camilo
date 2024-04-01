# 4. *Contador de Palabras:*
#    - Desarrolla un programa que cuente la cantidad de palabras en una frase ingresada por el usuario. Utiliza la manipulación de strings para realizar el conteo y muestra el resultado.
import re
nombre_completo = "Juan*Camilo.. Mosqura Pal-omino"

def contador(texto):
  palabra = re.findall(r'\b\w+(?:-\w+)*\b', texto)
  numero = len(palabra)
  return palabra

print(contador(nombre_completo))

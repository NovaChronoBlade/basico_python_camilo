# 1. *Formateo de Nombres:*
#    - Crea un programa que reciba el nombre completo de una persona y lo formatee en el estilo "Apellido, Nombre(s)". Utiliza la manipulación de strings para lograr este formato y muestra el resultado.


nombre_completo = "Juan Camilo Mosqura Palomino"

divsion = nombre_completo.split(" ")

no_1 = divsion[0]
no2 = divsion[1]
ap_1 = divsion[2]
ap_2 = divsion[3]

nombre_format = f"{ap_1} {ap_2} {no_1} {no2}"

print(nombre_format)

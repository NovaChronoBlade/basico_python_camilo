# 2. *Calculadora de Intereses Compuestos:*
#    - Desarrolla un programa que calcule el monto final de una inversión a interés compuesto, considerando el capital inicial, la tasa de interés y el tiempo, utilizando operadores aritméticos y repeticiones.

def interes_compuesto(capital_inical, tasa_de_interes, perido_de_ahorro):
    monto_final = capital_inical * (1 + tasa_de_interes/100)**perido_de_ahorro
    return monto_final


capital_inical = float(1000)
tasa_de_interes = float(10)
perido_de_ahorro = int(1)


resultado = interes_compuesto(capital_inical, tasa_de_interes, perido_de_ahorro)

print(resultado)



# Ejercicio 1:
# Imprime un recibo de compra como el que se muestra a continuación.

recibo = "RECIBO"
recibo = f"|{recibo:^35}|"

articulo = "ARTICULO"
articulo = f"| {articulo:<14}"

cantidad = "CANTIDAD"
cantidad = f"| {cantidad} | "

precio = "PRECIO"
precio = f"{precio} |"

def store(fruta, cantidad, precio):
    return f"| {fruta:<13} | {cantidad:<8} | ${precio:<5} |"

manzanas = store("Manzanas", "3", "1.50")
bananas = store("Bananas", "2", "0.80")
naranjas = store("Naranjas", "4", "2.00")
 
print("-"*37,  recibo, articulo + cantidad + precio, "|" + "-"*15 + "|" + "-"*10 + "|" + "-"*8 + "|", manzanas, bananas, naranjas, "-"*37, sep="\n")

# Pedido de Pizza: Escribe un programa que tome la entrada del usuario para el
# tamaño y los ingredientes de una pizza y calcule el costo total. Usa declaraciones if/
# elif/else y el operador in para determinar el costo según el tamaño y los ingredientes.

def calcular_costo_pizza(tamano, tipo_pizza):
    tamano = tamano.lower()
    tipo_pizza = tipo_pizza.lower()

    if tamano == "pequeño":
        precios_tamano = 10
    elif tamano == "mediano":
        precios_tamano = 20
    elif tamano == "grande":
        precios_tamano = 30
    else:
        return "Tamaño no válido"

    menu_pizzas = {
        "hawaiana": {"precio_base": 10, "ingredientes": ["piña", "jamón", "extra queso"]},
        "carnívora": {"precio_base": 12, "ingredientes": ["pepperoni", "salchicha", "tocino", "jamón"]},
        "vegetariana": {"precio_base": 9, "ingredientes": ["pimiento", "champiñones", "aceitunas", "cebolla"]}
    }

    if tipo_pizza not in menu_pizzas:
        return "Tipo de pizza no válido"

    precio_base = menu_pizzas[tipo_pizza]["precio_base"]
    factor_tamano = precios_tamano
    costo_total = precio_base * factor_tamano

    return f"Costo total: ${costo_total:.2f} (incluye ingredientes como {', '.join(menu_pizzas[tipo_pizza]['ingredientes'])})"

tamano_pizza = "grande"
tipo_pizza = "vegetariana"

resultado = calcular_costo_pizza(tamano_pizza, tipo_pizza)
print(resultado)

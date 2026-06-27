productos = [
    {"nombre": "Harina", "precio": 2.50, "cantidad": 2},
    {"nombre": "Tomate", "precio": 1.80, "cantidad": 3},
    {"nombre": "Queso", "precio": 4.00, "cantidad": 1}
]

def resumen_compra(productos):
    precio_compra = 0
    unidades = 0

    for producto in productos:
        precio_producto = producto["precio"] * producto["cantidad"]
        precio_compra += precio_producto
        unidades += producto["cantidad"]

    ticket = {
        "Precio_compra": precio_compra,
        "Unidades": unidades
    }
    return ticket


"""
print("El precio total de la compra es: ", precio_compra, "Euros")
print("La cantidad de articulos en la cesta es: ", unidades)
"""
print(resumen_compra(productos))

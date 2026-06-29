productos = [
    {"nombre": "Teclado", "precio": 45, "cantidad": 2},
    {"nombre": "Raton", "precio": 25, "cantidad": 1},
    {"nombre": "Cable", "precio": 8, "cantidad": 2}
]
def calculador_pedidos (productos):
    unidades = 0
    subtotal = 0
    precio_mas_caro = 0
    producto_mas_caro = ""
    for producto in productos:
        
        unidades += producto["cantidad"]
        subtotal +=  (producto["cantidad"] * producto["precio"])
        if producto["cantidad"] * producto["precio"] > precio_mas_caro:
            precio_mas_caro = producto["cantidad"] * producto["precio"]
            producto_mas_caro = producto["nombre"]
        
    if subtotal >= 100:
        descuento = subtotal * 0.1
    else:
        descuento = 0
    
    total_pedido = subtotal - descuento

        
    resultado = {
        "Subtotal": subtotal,
        "Unidades": unidades,
        "Producto con mayor importe": producto_mas_caro,
        "Mayor importe": precio_mas_caro,
        "Descuento": round(descuento, 2),
        "Total": total_pedido
    }

    return resultado

print(calculador_pedidos (productos))
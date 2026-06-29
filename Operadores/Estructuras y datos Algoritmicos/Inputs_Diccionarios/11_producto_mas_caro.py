productos = [
    {"nombre": "Harina", "precio": 2.50, "cantidad": 2},
    {"nombre": "Tomate", "precio": 1.80, "cantidad": 3},
    {"nombre": "Queso", "precio": 4.00, "cantidad": 1}
]

def revisar_mayor_importe(productos):
    producto_mas_caro = ""
    importe_mas_caro = 0
    
    for producto in productos:
        importe = producto["precio"] * producto["cantidad"]
        if importe > importe_mas_caro:
            importe_mas_caro =  importe
            producto_mas_caro = producto["nombre"]
    return producto_mas_caro, importe_mas_caro
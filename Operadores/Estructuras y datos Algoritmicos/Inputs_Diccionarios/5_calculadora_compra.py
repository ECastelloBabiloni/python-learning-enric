def calculadora(precio, cantidad, descuento):
    subtotal = precio * cantidad
    importe_descontado = descuento * subtotal
    precio_final = subtotal - importe_descontado

    return subtotal, importe_descontado, precio_final

precio = float(input("Precio del articulo: "))
cantidad = int(input("Unidades: "))
rebaja = input("Descuento aplicado [0%]: ")

if rebaja == (""):
    descuento = 0
else:
    descuento = float(rebaja) / 100

subtotal, importe_descontado, precio_final = calculadora(precio, cantidad, descuento)



print("Subtotal: ", round(subtotal,2))
print("Importe descontado: ", round(importe_descontado, 2))
print("Total: ", round(precio_final, 2))
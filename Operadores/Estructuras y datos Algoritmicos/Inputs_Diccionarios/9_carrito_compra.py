
lista = [25, 40, 50]

def lista_compra(lista):
    
    suma = 0
    descuento = 10
    for numero in lista:
        suma += numero

    if suma >= 100:
        importe_descuento = suma * descuento / 100
    else:
        importe_descuento = 0

    importe_total = suma - importe_descuento
    
    return suma, importe_descuento, importe_total

print(lista_compra(lista))

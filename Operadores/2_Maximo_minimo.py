def analizar_precios(lista_precios):
    if not lista_precios:
        return "Precios no disponibles"
    precio_alto = lista_precios[0]
    precio_bajo = lista_precios[0]

    for precio in lista_precios[1:]:
        if precio >= precio_alto:
            precio_alto = precio
        elif precio <= precio_bajo:
            precio_bajo = precio
    
    return precio_bajo, precio_alto
    

lista_precios = [1.32, 50.05, 32.5, 60, 10.85, 2.15]

print(analizar_precios(lista_precios))

5.32, 50.05, 32.5, 6, 10.85, 24.15
5, 50, 32, 6, 10, 24
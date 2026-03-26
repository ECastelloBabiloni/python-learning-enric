def segundo_mas_grande(lista):
    if not lista or len(lista) < 2:
        return "Lista no disponible"
    valor_alto = lista[0]
    segundo_valor_alto = None

    for valor in lista[1:]:
        if valor == valor_alto or valor == segundo_valor_alto:
            continue
        if valor > valor_alto:
            segundo_valor_alto = valor_alto
            valor_alto = valor
        elif segundo_valor_alto is None or valor > segundo_valor_alto:
            segundo_valor_alto = valor
    
    
    return segundo_valor_alto
    

lista = [1.32, 60, 50.05, 5.32, 32.5, 60, 10.85, 2.15, 24.15, 55]

print(segundo_mas_grande(lista))


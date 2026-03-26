def valores_unicos(lista):
    if not lista:
        return "No hay lista"
    sin_duplicados = []
    for numero in lista:
        if numero not in sin_duplicados: 
            sin_duplicados.append(numero)

    return sin_duplicados

lista = [1, 60, 50, 5, 5, 60, 10, 2, 24, 55, 2]
print(valores_unicos(lista))
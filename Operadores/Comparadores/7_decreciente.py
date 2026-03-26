def es_decreciente(lista):
    if len(lista) < 2:
        return "No hay lista"

    for i in range(len(lista)-1):
        if lista[i] < lista[i + 1]:
            return False
    return True

lista = [5, 3, 3, 2, 0]
print(es_decreciente(lista))    
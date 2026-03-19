def hay_duplicados(lista):
    if len(lista) < 2:
        return "No hay lista"
    for i in lista:
        for j in lista:
            if i == j :
                continue
            if lista[j] == lista[i]:
                return True
    return False
            
lista= [1, 2, 5, 1, 3]
print(hay_duplicados(lista))
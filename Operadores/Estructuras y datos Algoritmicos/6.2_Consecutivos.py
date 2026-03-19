def hay_consecutivos(lista):
    if len(lista) < 2:
        return "No hay lista o lista corta"
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            return True
    return False 

lista = [1, 2, 3, 7, 5]
print(hay_consecutivos(lista))
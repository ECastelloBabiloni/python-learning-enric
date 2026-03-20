def hay_duplicados(lista):
    if len(lista) < 2:
        return "No hay lista"
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            
            if lista[j] == lista[i]:
                return True
    return False
            
lista= [1, 2, 5, 3, 3]
print(hay_duplicados(lista))
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def sumar_matriz(matriz):
    total_suma = 0
    for fila in matriz:
        for numero in fila:
            total_suma += numero
    return total_suma
    

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

    
mostrar_matriz(matriz)
print(sumar_matriz(matriz))


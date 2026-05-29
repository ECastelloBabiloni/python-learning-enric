def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def sumar_matriz(matriz):
    total_suma = 0
    for fila in matriz:
        for numero in fila:
            total_suma += numero
    return total_suma

def sumar_filas(matriz):
    resultados = []
    for fila in matriz:
        suma_fila = 0

        for numero in fila:
            suma_fila += numero

        resultados.append(suma_fila)
    return resultados

def sumar_columnas(matriz):
    
    suma_col_0 = 0
    suma_col_1 = 0
    suma_col_2 = 0

    for fila in matriz:
           
        suma_col_0 += fila[0]      
        suma_col_1 += fila[1]
        suma_col_2 += fila[2]
   
    return [suma_col_0, suma_col_1, suma_col_2]


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

    
mostrar_matriz(matriz)
print("sumar matriz",sumar_matriz(matriz))
print("sumar filas",sumar_filas(matriz))
print("sumar columnas", sumar_columnas(matriz))

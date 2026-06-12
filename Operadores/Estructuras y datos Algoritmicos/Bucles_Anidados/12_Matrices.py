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


def primer_elemento(matriz):
    if not matriz or not matriz[0]:
        return None
    
    return matriz[0][0]
    

print("primer elemento", primer_elemento(matriz))  # 1

def elemento_central(matriz):
    if not matriz or not matriz[0]:
        return None
    return matriz[1][1]


print("elemento central", elemento_central(matriz))

def contar_elementos(matriz):
    if not matriz or not matriz[0]:
        return None
    contador = 0

    for fila in matriz:
        for numero in fila:
            contador += 1
    return contador
     

print("contar elementos", contar_elementos(matriz))

def contar_pares(matriz):
    if not matriz or not matriz[0]:
        return 0
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                contador = contador + 1
    return contador

print("contar pares", contar_pares(matriz))


def contar_impares(matriz):
    if not matriz or not matriz[0]:
        return 0
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 != 0:
                contador = contador + 1
    return contador
print("contar impares", contar_impares(matriz))


def sumar_pares(matriz):
    if not matriz or not matriz[0]:
        return 0
    suma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                suma += matriz[i][j]
    return suma

print("sumar pares", sumar_pares(matriz))
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

def sumar_impares(matriz):
    if not matriz or not matriz[0]:
        return 0
    suma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 != 0:
                suma += matriz[i][j]
    return suma


print("sumar impares", sumar_impares(matriz))

def contar_mayores_5(matriz):
    if not matriz or not matriz[0]:
        return 0
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 5:
                contador = contador +1
    return contador

print("cuenta mayores de 5: ", contar_mayores_5(matriz))

def contar_menores_5(matriz):
    if not matriz or not matriz[0]:
        return 0
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 5:
                contador = contador +1
    return contador

print("contar menores de 5: ", contar_menores_5(matriz))

def sumar_mayores_5(matriz):
    if not matriz or not matriz[0]:
        return 0
    suma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 5:
                suma += matriz[i][j]
    return suma

print("sumar mayores de 5: ", sumar_mayores_5(matriz))

def contar_multiplos_3(matriz):
    if not matriz or not matriz[0]:
        return 0
    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 3 == 0:
                contador = contador+1
    return contador

print("contar multiplos de 3: ", contar_multiplos_3(matriz))

def existe_numero(matriz, objetivo):
    if not matriz or not matriz[0]:
        return False
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                return True
    return False


print("¿existe el numero 5? ", existe_numero(matriz, 5))
print("¿existe el numero 20? ", existe_numero(matriz,20))

def posicion_numero(matriz, objetivo):
    if not matriz or not matriz[0]:
        return None
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == objetivo:
                return i, j
    return None

print("posicion 5:", posicion_numero(matriz, 5))    # (1, 1)
print("posicion 9:", posicion_numero(matriz, 9))    # (2, 2)
print("posicion 20:", posicion_numero(matriz, 20))  # None

def posicion_primer_par(matriz):
    if not matriz or not matriz[0]:
        return None
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                return i, j
    return None

print("posicion primer numero par: ", posicion_primer_par(matriz))

def posicion_primer_mayor_que(matriz, limite):
    if not matriz or not matriz[0]:
        return None
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > limite:
                return i, j
    return None


print("posicion primer numero mayor de 5: ", posicion_primer_mayor_que(matriz, 5))

def posiciones_pares(matriz):
    if not matriz or not matriz[0]:
        return None
    
    posiciones = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                posiciones.append((i, j))
    return posiciones


print("posiciones de los pares: ", posiciones_pares(matriz))

def posiciones_mayores_5(matriz):
    if not matriz or not matriz[0]:
        return []
    posiciones = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 5:
                posiciones.append((i, j))
    return posiciones

print("posiciones mayores de 5: ", posiciones_mayores_5(matriz))

def posiciones_multiplo_3(matriz):
    if not matriz or not matriz[0]:
        return []
    posiciones = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 3 == 0:
                posiciones.append((i, j))
    return posiciones

print("Posiciones multiplos de 3: ", posiciones_multiplo_3(matriz))

def valores_pares(matriz):
    if not matriz or not matriz[0]:
        return []
    pares = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                pares.append(matriz[i][j])
    return pares

print("lista de numeros pares: ", valores_pares(matriz))

def valores_mayores_5(matriz):
    if not matriz or not matriz[0]:
        return []
    mayores_5 = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 5:
                mayores_5.append(matriz[i][j])
    return mayores_5

print("lista mayores de 5: ", valores_mayores_5(matriz))

def valores_multiplos_3(matriz):
    if not matriz or not matriz[0]:
        return []
    multiplos_3 = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 3 == 0:
                multiplos_3.append(matriz[i][j])
    return multiplos_3

print("lista multiplos de 3: ", valores_multiplos_3(matriz))

def encontrar_maximo(matriz):
    if not matriz or not matriz[0]:
        return []
    maximo = matriz[0][0]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
    return maximo

print("numero maximo: ", encontrar_maximo(matriz))

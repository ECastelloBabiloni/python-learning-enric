def esta_ordenada(lista):
    # 1. Cláusula de guarda (Fail Fast)
    if len(lista) < 2:
        return True
    
    # 2. El vigilante (Bucle controlado por rango)
    for i in range(len(lista) - 1):
        
        # 3. La comparación de vecinos
        if lista[i] > lista[i + 1]:
            return False # Se detectó un error, cortamos de inmediato
            
    # 4. Confirmación final
    return True

# Pruebas
print(esta_ordenada([5-7])) # True
print(esta_ordenada([5-7])) # False


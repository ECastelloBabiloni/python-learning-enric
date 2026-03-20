"""
Ejercicio de Fase 2: "El Terreno Común" (Intersección de Listas)
Tarea: Escribe una función llamada elementos_comunes(lista_a, lista_b) que reciba dos listas de números y devuelva una nueva lista que contenga únicamente los números que aparecen en ambas colecciones.
Lo que debes aplicar para consolidar:
Estructura de Bucle Anidado: Necesitas un bucle exterior (i) para recorrer la lista_a y un bucle interior (j) para recorrer la lista_b.
Comparación Total: Por cada elemento de la primera lista, debes preguntar si existe en la segunda.
Gestión de Resultados: Deberás crear una lista vacía al principio (resultado = []) y usar el método .append() para ir guardando los hallazgos.
Criterio Senior (El Reto): Para que tu código sea profesional, asegúrate de que si un número está repetido en ambas listas, solo se añada una vez a tu lista de resultados (puedes usar el operador in solo para esta comprobación antes de añadir).
"""


def elementos_comunes(lista_a, lista_b):
    if len(lista_a) <2 or len(lista_b)<2:
        return "no hay listas"
    comunes = []
    for i in lista_a:
        if i in comunes:
            continue
        for j in lista_b:
            if j in comunes:
                continue
            if i == j:
                comunes.append(j)
    return comunes


lista_a = [ 5, 8, 9]
lista_b = [0,3,6,1,3]
print(elementos_comunes(lista_a, lista_b))
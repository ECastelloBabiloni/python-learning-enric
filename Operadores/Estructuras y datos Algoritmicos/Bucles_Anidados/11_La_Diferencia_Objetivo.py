""" 
Reto Final: "La Diferencia Objetivo"
Tarea: Escribe una función llamada existe_diferencia(lista, d) que reciba una lista de números y un valor de diferencia d. La función debe devolver True si existen dos números cualesquiera en la lista cuya resta (el mayor menos el menor) sea exactamente igual a d. Si no existen, debe devolver False.
Lo que debes aplicar (sin mirar apuntes si es posible):
Cláusula de Guarda: Ataca el problema de listas vacías o con un solo elemento (principio Fail Fast)
.
Bucle Exterior (i): Recorre hasta el penúltimo elemento
.
Bucle Interior Optimizado (j): Usa el patrón que aprendimos el último día: empezar justo después de i para no repetir comparaciones ni restarte a ti mismo
.
Lógica de Valor Absoluto: Para que no importe el orden de la resta, puedes usar la función integrada abs(lista[i] - lista[j]) o simplemente restar el mayor del menor si lo prefieres
.
Complejidad: Recuerda que este algoritmo seguirá siendo O(n 
2
 ) (cuadrático) porque estamos agotando todas las parejas posibles
.
Ejemplo:
lista =
d = 5
Proceso: El código comparará 10 con 15. Como 15 - 10 = 5, devuelve True inmediatamente.
"""

def existe_diferencia(lista, d):
    if len(lista) < 2:
        return "No hay lista"
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] - lista[j] == d:
                return lista[i], lista[j]
    return None

lista = [8,5,3,1]
d = 4
print(existe_diferencia(lista, d))
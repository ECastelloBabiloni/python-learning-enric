"""
Reto de Refresh: "La Pareja Perfecta"
Tarea: Escribe una función llamada busca_suma(lista, objetivo) que reciba una lista de números y un número llamado objetivo. La función debe encontrar los dos primeros números de la lista que, al sumarse, den exactamente el valor del objetivo.
Lo que debes aplicar para consolidar:
Estructura de Bucle Anidado: Necesitas un bucle exterior que seleccione un número y uno interior que busque a su "pareja" en el resto de la lista.
Optimización de Índices: Aplica el range(i + 1, len(lista)) que descubrimos en el ejercicio de duplicados. Esto garantiza que no compares un número consigo mismo y que el algoritmo sea más eficiente al no repetir parejas ya revisadas
.
Principio Fail Fast: En cuanto la suma sea igual al objetivo, devuelve la pareja (puede ser como una pequeña lista o tupla) para cerrar la función de inmediato
.
Confirmación Final: Si los bucles agotan todas las vueltas y nadie suma el objetivo, devuelve None fuera de los bucles.
Ejemplo de flujo esperado:
Entrada: lista =
, objetivo = 5
Proceso:
¿1 + 4 == 5? Sí.
Salida: (1, 4)
"""

def busca_suma(lista, objetivo):
    if len(lista) < 2:
        return "No hay lista"
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                return lista[i],lista[j] 
    return None

lista = [1,3,5,8]
objetivo = 8
print(busca_suma(lista, objetivo))
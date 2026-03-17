def elementos_comunes(lista_a, lista_b):
    if not lista_a or lista_b:
        return "No hay lista"
    comunes = []
    for numero in lista_a:
       if numero in lista_b:
           comunes.append(numero)

lista_a = [1, 60, 50, 5, 5, 60, 10, 2, 24, 55, 2]
lista_b = [ 7, 8, 10, 50, 5, 18, 24] 
print(elementos_comunes(lista_a, lista_b))
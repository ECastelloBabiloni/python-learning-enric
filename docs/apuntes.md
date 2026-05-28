# Apuntes de Python y logica

Este documento guarda conceptos importantes aprendidos durante los ejercicios.

## Clausula de guarda

Una clausula de guarda es una comprobacion al principio de una funcion para cortar rapido si los datos no permiten resolver el problema.

Ejemplo:

```python
def segundo_mas_grande(lista):
    if len(lista) < 2:
        return None
```

Sirve para evitar errores y para que el resto de la funcion trabaje con datos validos.

## Retorno temprano

El retorno temprano consiste en devolver la respuesta en cuanto se encuentra, sin seguir recorriendo datos innecesariamente.

Ejemplo:

```python
def contiene_duplicados(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False
```

## Bucles anidados

Un bucle anidado es un bucle dentro de otro. Se usa cuando necesitas comparar combinaciones de elementos.

Patron recomendado para comparar parejas sin repetir:

```python
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        print(lista[i], lista[j])
```

Ventajas:

- No compara un elemento consigo mismo.
- No repite parejas ya revisadas.
- Hace el codigo mas claro.

## Complejidad O(n^2)

Cuando hay dos bucles anidados que recorren una lista, normalmente la solucion es cuadratica: `O(n^2)`.

Esto significa que si la lista crece mucho, el numero de comparaciones crece muy rapido.

No siempre esta mal. Para aprender logica, primero es importante escribir una solucion correcta y clara. Luego se puede buscar una version mas eficiente.

## Valores booleanos

Si el enunciado pide responder si algo existe o no existe, lo normal es devolver `True` o `False`.

Ejemplo:

```python
def existe_valor(lista, objetivo):
    for valor in lista:
        if valor == objetivo:
            return True
    return False
```

## Separar logica y pruebas

Es recomendable que la funcion solo resuelva el problema, y que las pruebas manuales esten debajo de:

```python
if __name__ == "__main__":
    print(mi_funcion([1, 2, 3]))
```

Esto permite importar la funcion desde otro archivo sin ejecutar automaticamente las pruebas.

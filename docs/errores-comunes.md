# Errores comunes

Este documento registra fallos habituales para convertirlos en aprendizaje.

## 1. Devolver algo distinto a lo que pide el enunciado

Ejemplo: si el enunciado pide devolver `True` o `False`, no conviene devolver una pareja de numeros o `None`.

Antes de programar, escribir claramente:

- Entrada: que recibe la funcion.
- Salida: que debe devolver.

## 2. Mezclar mensajes de texto con datos logicos

Si una funcion normalmente devuelve numeros, listas, tuplas o booleanos, conviene evitar devolver textos como `"No hay lista"`.

Mejor:

```python
return None
```

o:

```python
return False
```

Depende de lo que pida el ejercicio.

## 3. No probar casos limite

Casos que suelen romper soluciones:

- Lista vacia.
- Lista con un solo elemento.
- Valores repetidos.
- Numeros negativos.
- Objetivo imposible.
- Lista ya ordenada.
- Lista desordenada.

## 4. Comparar parejas repetidas

Si se comparan todos contra todos, es facil repetir trabajo.

Menos recomendable:

```python
for i in range(len(lista)):
    for j in range(len(lista)):
        ...
```

Mejor para parejas:

```python
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        ...
```

## 5. Confundir diferencia directa con diferencia absoluta

Si el problema dice "la diferencia entre dos numeros", muchas veces no importa el orden.

Ejemplo:

```python
abs(8 - 3) == 5
abs(3 - 8) == 5
```

Usar `abs()` evita depender de si el numero grande aparece antes o despues.

## 6. Pruebas que no prueban lo que dicen

Un comentario como `# False` debe coincidir con el resultado esperado.

Ejemplo:

```python
print(esta_ordenada([1, 2, 3]))  # True
print(esta_ordenada([3, 2, 1]))  # False
```

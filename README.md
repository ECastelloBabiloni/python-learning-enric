# Python Learning Enric

Repositorio personal para practicar Python, logica de programacion y pensamiento algoritmico.

El objetivo no es solo acumular ejercicios resueltos, sino aprender a razonar como programador: entender el problema, dividirlo en pasos, detectar casos especiales, escribir codigo claro y explicar las decisiones.

## Objetivos del repositorio

- Practicar fundamentos de Python.
- Mejorar la logica de programacion paso a paso.
- Documentar ejercicios, errores y aprendizajes.
- Construir una base visible de progreso para GitHub.
- Evolucionar desde soluciones funcionales hacia soluciones mas limpias, testeables y mantenibles.

## Estructura actual

```text
Operadores/
  Casa/
    Primeros ejercicios y pruebas iniciales.

  Comparadores/
    Ejercicios sobre maximos, minimos, orden, valores unicos y comparacion de listas.

  Estructuras y datos Algoritmicos/
    Bucles_Anidados/
      Ejercicios de duplicados, elementos comunes, parejas con suma objetivo y diferencia objetivo.

docs/
  apuntes.md
  errores-comunes.md
  progreso.md
```

## Ruta de aprendizaje

### 1. Fundamentos

- Variables.
- Tipos de datos.
- Operadores.
- Condiciones.
- Funciones.
- Listas.

### 2. Logica con colecciones

- Recorrer listas.
- Comparar elementos vecinos.
- Buscar maximos y minimos.
- Detectar duplicados.
- Encontrar elementos comunes.
- Trabajar con indices.

### 3. Pensamiento algoritmico

- Clausulas de guarda.
- Retorno temprano.
- Bucles anidados.
- Evitar comparaciones repetidas.
- Analizar la complejidad de una solucion.

### 4. Calidad de codigo

- Nombres claros.
- Funciones con una responsabilidad concreta.
- Separar la logica de las pruebas manuales.
- Devolver valores consistentes.
- Cubrir casos limite.

## Como revisar cada ejercicio

Para cada ejercicio conviene responder estas preguntas:

1. Que problema resuelve?
2. Que datos recibe la funcion?
3. Que debe devolver exactamente?
4. Que casos especiales existen?
5. La solucion corta pronto cuando ya tiene respuesta?
6. Hay una forma mas clara o mas eficiente?
7. Que pruebas demuestran que funciona?

## Estado actual

Nivel estimado: inicial / inicial-medio.

Fortalezas detectadas:

- Ya usas funciones para encapsular soluciones.
- Empiezas a aplicar clausulas de guarda.
- Usas bucles con indices.
- Estas practicando comparaciones entre elementos.
- Has empezado con problemas de parejas y bucles anidados.

Puntos a trabajar:

- Alinear mejor lo que pide el enunciado con lo que devuelve la funcion.
- Usar retornos consistentes, por ejemplo `True`/`False` si el ejercicio pide booleanos.
- Separar codigo de solucion y pruebas.
- Agregar mas casos de prueba por ejercicio.
- Cuidar la codificacion de caracteres en textos con acentos.

## Proximos pasos recomendados

1. Normalizar la documentacion del repo.
2. Revisar ejercicio por ejercicio.
3. Crear pruebas simples para validar cada funcion.
4. Mejorar nombres y retornos.
5. Crear una segunda version optimizada de algunos ejercicios.

## Convencion sugerida para nuevos ejercicios

Cada archivo nuevo puede seguir esta estructura:

```python
"""
Enunciado:
Explicacion breve del problema.

Entrada:
Que datos recibe.

Salida:
Que debe devolver.

Casos especiales:
Lista vacia, un solo elemento, duplicados, etc.
"""


def nombre_de_la_funcion(datos):
    # Solucion
    pass


if __name__ == "__main__":
    # Pruebas manuales
    print(nombre_de_la_funcion([]))
```

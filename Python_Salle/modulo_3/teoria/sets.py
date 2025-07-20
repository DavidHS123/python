# Los sets (o conjuntos) son una estructura de datos en Python que permite almacenar colecciones de elementos !!!únicos!!! y no ordenados. Son útiles cuando necesitas realizar operaciones matemáticas como uniones, intersecciones o diferencias entre conjuntos.
# Los valores que se repitan en un set se eliminan automáticamente, lo que significa que cada elemento en un set es único. Hay que tener en cuenta, que hay valores que para Python son considerados iguales, como por ejemplo `1` y `True`, o `"hola"` y `"Hola"`. Por lo tanto, si intentas añadir un elemento que ya existe en el set, no se añadirá de nuevo.

# Los sets se definen utilizando llaves `{}` o la función `set()`. A continuación, se presentan algunas características y ejemplos de uso de los sets en Python:
# 1. **Creación de un set**:

frutas = {"manzana", "plátano", "naranja"}

# 2. **Acceso a los elementos**: A diferencia de las listas, los sets no permiten acceder a los elementos por índice, ya que no están ordenados. Sin embargo, puedes iterar sobre ellos.
for fruta in frutas:
    print(fruta)
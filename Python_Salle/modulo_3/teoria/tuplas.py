# Las tuplas son estructuras de datos que permiten almacenar múltiples elementos en un solo objeto, similar a las listas. Sin embargo, a diferencia de las listas, las tuplas son inmutables, lo que significa que no puedes modificar su contenido una vez que han sido creadas. Esto las hace útiles para almacenar datos que no deben cambiar.

# Las tuplas se definen utilizando paréntesis `()` y los elementos se separan por comas. A continuación, se presentan algunas características y ejemplos de uso de las tuplas en Python:

# 1. **Creación de una tupla**:
frutas = ("manzana", "plátano", "naranja")

# 2. **Acceso a los elementos**: Puedes acceder a los elementos de una tupla utilizando índices, al igual que con las listas.
print(frutas[0])  # Imprime: manzana
print(frutas[1])  # Imprime: plátano
print(frutas[2])  # Imprime: naranja

# 3. **Longitud de una tupla**: Puedes obtener la cantidad de elementos en una tupla utilizando la función `len()`.
print(len(frutas))  # Imprime: 3

# 4. **Iteración sobre una tupla**: Puedes iterar sobre los elementos de una tupla utilizando un bucle `for`.
for fruta in frutas:
    print(fruta)
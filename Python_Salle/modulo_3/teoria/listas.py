# Las listas son estructuras de datos que permiten almacenar múltiples elementos en un solo objeto. Son mutables, lo que significa que puedes modificar su contenido después de haberlas creado. Las listas se definen utilizando corchetes `[]` y los elementos se separan por comas.
# Ejemplo de una lista simple:
frutas = ["manzana", "plátano", "naranja"]
# Acceder a los elementos de una lista utilizando índices (empezando desde 0):
print(frutas[0])  # Imprime: manzana
print(frutas[1])  # Imprime: plátano
print(frutas[2])  # Imprime: naranja
# Puedes modificar los elementos de una lista asignando un nuevo valor a un índice específico:
frutas[0] = "pera"
print(frutas)  # Imprime: ['pera', 'plátano', 'naranja']
# En este ejercicio, buscaremos todas las apariciones de un elemento en una lista y devolveremos sus índices.
# En este código, buscamos todas las apariciones de la palabra "dolor" en el texto lorem y mostramos sus índices.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Definimos una función que le pasamos una lista y un elemento como parámetros.
def buscar_apariciones(lista, elemento):
    # Inicializamos variables
    string = lista
    index = 0
    indexTotal = 0

    # Bucle para buscar todas las apariciones del elemento en la cadena
    # Utilizamos string.find() para encontrar el índice de la primera aparición del elemento
    while string.find(elemento) >= 0:
        # Si el elemento no se encuentra, salimos del bucle
        index = string.find(elemento)
        indexTotal += index
        print(indexTotal)
        
        string = string[index + len(elemento):]
        indexTotal += index + len(elemento)
        # Actualizamos la cadena para buscar la siguiente aparición del elemento

buscar_apariciones(text, "dolor")
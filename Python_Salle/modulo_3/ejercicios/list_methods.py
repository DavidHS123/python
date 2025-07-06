# En este ejecicio, vamos a trabajar con métodos de listas en Python.
# Metodos existentes(https://www.w3schools.com/python/python_lists_methods.asp):
    # append()    Adds an element at the end of the list
    # clear()     Removes all the elements from the list
    # copy()      Returns a copy of the list
    # count()     Returns the number of elements with the specified value
    # extend()    Add the elements of a list (or any iterable), to the end of the current list
    # index()     Returns the index of the first element with the specified value
    # insert()    Adds an element at the specified position
    # pop()       Removes the element at the specified position
    # remove()    Removes the item with the specified value
    # reverse()   Reverses the order of the list
    # sort()      Sorts the list

# Vamos a crear una lista con diferentes elementos (numeros, listas, diccionarios, cadenas de texto, etc.) y jugaremos con los métodos de listas para manipularla.

# Creamos una lista con diferentes tipos de elementos

mi_lista = [1, 2, 3, "hola", [4, 5], {"clave": "valor"}, 6.7]

# Imprimimos la lista original
print("Lista original:", mi_lista)

# Añadimos un elemento al final de la lista
mi_lista.append("nuevo elemento")

# Imprimimos la lista después de añadir un elemento
print("Lista después de añadir un elemento:", mi_lista)

# Insertamos un elemento en una posición específica (índice 2)
mi_lista.insert(2, "insertado en el índice 2")

# Imprimimos la lista después de insertar un elemento
print("Lista después de insertar un elemento en el índice 2:", mi_lista)

# Eliminamos un elemento específico (la cadena "hola")
mi_lista.remove("hola")

# Imprimimos la lista después de eliminar un elemento
print("Lista después de eliminar 'hola':", mi_lista)

# Añadimos un elemento a la lista interna (índice 4)
mi_lista[4].append(6)

# Imprimimos la lista después de añadir un elemento a la lista interna
print("Lista después de añadir un elemento a la lista interna:", mi_lista)
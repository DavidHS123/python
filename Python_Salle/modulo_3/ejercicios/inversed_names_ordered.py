# En este ejercicio, invertiremos el orden de los nombres de una lista y los ordenaremos alfabéticamente.

alumnes = ["Francisco", "Antonio", "Eliel", "Walter", "Maria", "Ana", "Ivan"]

def reverseNames(names):
    reversed_names = []
    for name in names:
        reversed_names.append(name[::-1])
    reversed_names.sort()
    return reversed_names

print(reverseNames(alumnes))
# Muestra por consola el resultado de una función que devuelva "hola" y el nombre del usuario introducido en un input:
def saludo():
    nombre = input("Introduce tu nombre: ")
    nombre = "Hola " + nombre
    return nombre
print(saludo())
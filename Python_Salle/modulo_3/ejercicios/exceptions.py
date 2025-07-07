# En este ejercicio vamos a practicar el manejo de excepciones en Python.
#1. Crea una funcion que valide una lista de nombres de alumnos. Lanza una excepcion si el nombre no es una cadena de texto o si la cadena esta vacia.
print("Ejercicio 1: Validación de nombres de alumnos")

def validar_nombres(nombres):
    for nombre in nombres:
        if not isinstance(nombre, str):
            raise TypeError(f"El nombre '{nombre}' no es una cadena de texto.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
    return True
alumnos = ["Juan", "Ana", "", 123, "Pedro"]

try:
    validar_nombres(alumnos)
except TypeError as e:
    print(f"Error de tipo: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
else:
    print("Todos los nombres son válidos.")

#2.Crea una funcion que abra un archivo que lea su contenido y muestre el numero de lineas que contiene. Lanza una excepcion personalizada si el archivo no existe o si esta vacio.

print("\nEjercicio 2: Lectura de archivo y conteo de líneas")

class ArxiuNoTrobatError(Exception):
    pass

class ArxiuBuitError(Exception):
    pass

def mostrar_arxiu(path):
    try:
        with open(path, 'r') as f:
            contingut = f.readlines()
            if not contingut:
                raise ArxiuBuitError("L'arxiu està buit.")
            print("Contingut de l'arxiu:")
            for linia in contingut:
                print(linia, end='')
            print(f"\n\nNúmero de línies: {len(contingut)}")
    except FileNotFoundError:
        raise ArxiuNoTrobatError(f"L'arxiu '{path}' no existeix.")

# Exemple d’ús:
try:
    mostrar_arxiu("exemple.txt")
except ArxiuNoTrobatError as e:
    print(f"Error: {e}")
except ArxiuBuitError as e:
    print(f"Error: {e}")

#3. Crea un registro de estudiante (lista de diccionarios que contengan: nombre, año, nota y comentarios) y una función que le permite agregar estudiantes a la lista con entradas. Administra todos los errores posibles

print("\nEjercicio 3: Registro de estudiantes")

alumnes = []

def afegirAlumne():
    try:
        nom = input("Introduce el nombre del estudiante: ")
        if not nom:
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(nom, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        
        anyo = int(input("Introduce el año de ingreso: ").strip())
        if not isinstance(anyo, int):
            raise TypeError("El año debe ser un número entero.")
        if anyo < 1900 or anyo > 2025:
            raise ValueError("El año debe estar entre 1900 y 2025.")
        
        nota = float(input("Introduce la nota del estudiante: "))
        if not isinstance(nota, float):
            raise TypeError("La nota debe ser un número.")
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        
        comentarios = input("Introduce comentarios (opcional): ")

        alumno = {
            "nombre": nom,
            "año": anyo,
            "nota": nota,
            "comentarios": comentarios
        }
        alumnes.append(alumno)
        print(f"Estudiante {nom} agregado exitosamente.")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except TypeError as te:
        print(f"Error de tipo: {te}")

# Bucle para agregar estudiantes
while True:
    afegirAlumne()
    continuar = input("¿Deseas agregar otro estudiante? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Mostrar todos los estudiantes registrados
print("\nRegistro de estudiantes:") 
for alumno in alumnes:
    print(alumno)

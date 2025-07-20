# En Python, una de las cosas que hace más potente este lenguaje es su capacidad de importar módulos. Los módulos son archivos que contienen código Python y pueden ser reutilizados en otros programas. Esto permite organizar el código de manera más eficiente y facilita la reutilización de funciones y clases.

# Un módulo puede contener funciones, clases y variables que pueden ser importadas en otros archivos Python. Para importar un módulo, se utiliza la palabra clave `import` seguida del nombre del módulo. Por ejemplo, para importar el módulo `math`, se puede hacer de la siguiente manera:

import math # Importa el módulo math, se puede utilizar un alias con `imporas m` para abreviart math 

# import math as m # Importa el módulo math con un alias

# Ejemplo de uso del módulo math
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)
# Ejemplo de uso
print(f"El área de un círculo con radio 5 es: {calcular_area_circulo(5)}")

# También se pueden importar funciones específicas de un módulo utilizando la sintaxis `from nombre_modulo import funcion`. Por ejemplo, para importar la función `sqrt` del módulo `math`, se puede hacer de la siguiente manera:
from math import sqrt

# Ejemplo de uso de la función sqrt
def calcular_raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número."""
    return sqrt(numero)
# Ejemplo de uso
print(f"La raíz cuadrada de 16 es: {calcular_raiz_cuadrada(16)}")

# Además, se pueden crear módulos personalizados. Para ello, simplemente se crea un archivo Python con las funciones y clases que se deseen incluir. Luego, se puede importar este módulo en otros archivos Python de la misma manera que se importan los módulos estándar de Python.

# Por ejemplo, si se crea un archivo llamado `mi_modulo.py` con el siguiente contenido:

# ```python
# def saludar(nombre):
#     """Saluda a una persona por su nombre."""
#     return f"Hola, {nombre}!"
# ```
# Se puede importar y utilizar la función `saludar` en otro archivo Python de la siguiente manera:
from mi_modulo import saludar

# Ejemplo de uso de la función saludar del módulo personalizado
def saludar_persona(nombre):
    """Saluda a una persona utilizando la función del módulo personalizado."""
    return saludar(nombre)
# Ejemplo de uso
print(saludar_persona("David"))
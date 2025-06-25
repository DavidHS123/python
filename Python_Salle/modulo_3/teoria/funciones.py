# En Python tenemos muchas funciones predefinidas, como `print()`, `len()`, `type()`, entre otras. Estas funciones son parte de la biblioteca estándar de Python y se pueden utilizar directamente sin necesidad de importarlas.
# Sin embargo, también podemos crear nuestras propias funciones para organizar y reutilizar el código de manera más eficiente.

# 1. Definición de funciones:
# Las funciones en Python se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden contener parámetros.

def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    print(f"Hola, {nombre}!")
# Esta función toma un parámetro `nombre` y muestra un saludo personalizado.

# Ejemplo de uso:
saludar("Juan")
# Salida: Hola, Juan!

# 2. Parámetros y argumentos:
# Las funciones pueden aceptar parámetros, que son variables que se pasan a la función cuando se llama. Los argumentos son los valores reales que se pasan a esos parámetros.
def sumar(a, b):
    """Función que suma dos números."""
    return a + b

# Esta función toma dos parámetros `a` y `b`, y devuelve su suma.

# Ejemplo de uso:
resultado = sumar(3, 5)
print(f"La suma es: {resultado}")
# Salida: La suma es: 8

# 3. Funciones con valores por defecto:
def saludar_con_saludo(nombre, saludo="Hola"):
    """Función que saluda a una persona con un saludo personalizado."""
    print(f"{saludo}, {nombre}!")

# Esta función tiene un parámetro `saludo` con un valor por defecto "Hola". Si no se proporciona un saludo al llamar a la función, se utilizará el valor por defecto.
# Ejemplo de uso:

saludar_con_saludo("Ana")
# Salida: Hola, Ana!

saludar_con_saludo("Pedro", "Buenos días")
# Salida: Buenos días, Pedro!
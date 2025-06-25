# Los bloques `try` y `except` en Python se utilizan para manejar excepciones, que son errores que pueden ocurrir durante la ejecución de un programa. Estos bloques permiten que el programa continúe ejecutándose incluso si ocurre un error, en lugar de detenerse abruptamente.

# Permite manejar errores de manera controlada, evitando que el programa se detenga abruptamente.
print("Ejemplo de manejo de excepciones:")

dividendo = 4  # Cambia este valor para probar diferentes escenarios, por ejemplo, si fuese una cadena saltaria un TypeError.
divisor = 0  # Cambia este valor para probar diferentes escenarios, por ejemplo, si fuese 2 no habría error.

# Intentamos realizar una división y capturamos posibles errores.
try:
    resultado = dividendo / divisor  # Intenta realizar una división
    # print(f"Resultado de la división: {resultado}") 
    # En vez de usar este print aquí, se usará el else para comprobar que no ha habido errores.

# En este ejemplo, se intenta realizar una división por cero, lo que generará un error. El bloque `except` captura el error y permite manejarlo de manera controlada, imprimiendo un mensaje en lugar de detener el programa.
except ZeroDivisionError:  # Captura el error de división por cero
    if divisor == 0:
        print("Error: No se puede dividir por cero.")

# Este excepto captura errores de tipo, como intentar dividir un número por una cadena, y permite manejarlo de manera controlada.
except TypeError:  # Captura errores de tipo, como intentar dividir un número por una cadena
    print("Error: Tipo de dato no válido para la división.")

else:
    # Si no hubo errores, se ejecuta este bloque.
    print(f"Resultado de la división: {resultado}")

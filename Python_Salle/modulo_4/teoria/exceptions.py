# Manejo de excepciones en Python
# En Python se pueden manejar excepciones utilizando bloques try-except. Esto permite capturar errores y manejar situaciones excepcionales sin que el programa se detenga abruptamente.

# Ejemplo básico de manejo de excepciones
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero.")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    else:
        return resultado
    
# Ejemplo de uso
print(dividir(10, 2))  # Salida: 5.0
dividir(10, 0)  # Salida: Error: División por cero.
dividir(10, "a")  # Salida: Error: Tipo de dato

# En Python, también se pueden definir excepciones personalizadas creando una clase que herede de la clase base Exception. Esto permite crear errores específicos para situaciones particulares en el código.
class MiExcepcion(Exception):
    pass
# Ejemplo de excepción personalizada

def funcion_con_error():
    raise MiExcepcion("Ocurrió un error personalizado.")

# Manejo de la excepción personalizada
try:
    funcion_con_error()
except MiExcepcion as e:
    print(f"Excepción capturada: {e}")
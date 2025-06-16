# Python usa tipado dinámico, lo que significa que no es necesario declarar el tipo de variable al crearla.

# Ejemplo de variables
variable_int = 4
print(type(variable_int)) # Imprime el tipo de la variable, que es int de manera dinámica.

variable_float = 3.14
print(type(variable_float)) # Imprime el tipo de la variable, que es float de manera dinámica.

variable_str = "Hola, Python"
print(type(variable_str)) # Imprime el tipo de la variable, que es str de manera dinámica.

variable_bool = True
print(type(variable_bool)) # Imprime el tipo de la variable, que es bool de manera dinámica.

# Python permite convertir entre tipos de datos de manera sencilla.

# Si tienes un entero y quieres convertirlo a un flotante, puedes hacerlo con la función float()
# Ejemplo de conversión de tipos de datos

variable_int_a_float = float(variable_int)  # Convierte int a float
print(variable_int_a_float)  # Imprime: 4.0
variable_float_a_int = int(variable_float)  # Convierte float a int
print(variable_float_a_int)  # Imprime: 3

# Así con otros tipos de datos.
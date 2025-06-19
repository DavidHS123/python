# Para entrar datos por teclado, se utiliza la función input(). Esta función devuelve un string, por lo que si se necesita otro tipo de dato, es necesario convertirlo.
# Ejemplo de entrada de datos por teclado
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))  # Convertimos la entrada a entero
print(f"Hola, {nombre}. Tienes {edad} años.")
# Si queremos comprobar el tipo de dato introducido, podemos utilizar la función type().
print(f"El tipo de dato de 'nombre' es: {type(nombre)}") # Esto imprimirá <class 'str'> porque input() devuelve un string
print(f"El tipo de dato de 'edad' es: {type(edad)}")  # Esto imprimirá <class 'int'> si la conversión fue exitosa

# Ejemplo de uso: /ejercicios/calculadora_salario.py
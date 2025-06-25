# Las estructuras de control en Python son fundamentales para dirigir el flujo de ejecución del programa. Permiten tomar decisiones, repetir acciones y manejar excepciones. A continuación, se describen las principales estructuras de control:

# 1. Condicionales (`if`, `elif`, `else`):

# Permiten ejecutar bloques de código basados en condiciones.
# Donde if evalúa una condición, y si es verdadera, ejecuta el bloque de código correspondiente. `elif` permite evaluar múltiples condiciones, y `else` se ejecuta si ninguna de las condiciones anteriores es verdadera.

print("Ejemplo de condicionales:")

if True:
    print("Esto se ejecuta si la condición es verdadera.")

elif False:
    print("Esto se ejecuta si la condición anterior es falsa y esta es verdadera.")

else:
    print("Esto se ejecuta si todas las condiciones anteriores son falsas.")

# En las condicionales, los valores que devuelven los operadores de comparación son booleanos (`True` o `False`) y dependiendo de su valor, se ejecutará un bloque de código o no, y saltara al siguiente paso.

# 2. Bucles while:

# Permiten repetir un bloque de código mientras una condición sea verdadera.
print("Ejemplo de bucle while:")

contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador en 1

# El bucle `while` continuará ejecutándose hasta que la condición `contador < 5` sea falsa. En este caso, se imprimirá el valor del contador y luego se incrementará en 1 en cada iteración.
# Ejemplo de uso: /ejercicios/tabla_multiplicar.py

# Con el bucle while y la condición true, el bloque de código se ejecutará indefinidamente.
##  while True:
##      print("Este bucle se ejecuta indefinidamente. Presiona Ctrl+C para detenerlo.")
# Ejemplo de uso: /ejercicios/inicio_session.py


# 3. Bucles for:

# Permiten iterar sobre una secuencia (como una lista, tupla o cadena de texto).

print("Ejemplo de bucle for:")

for i in range(5):
    print(f"Iteración: {i}")

# El bucle `for` itera sobre un rango de números del 0 al 4, imprimiendo el valor de `i` en cada iteración.
# Ejemplo de uso: /ejercicios/lista_prendas.py


# 4. Sentencias de control de flujo (`break`, `continue`, `pass`):

# - `break`: Termina el bucle actual y sale de él.
print("Ejemplo de break:")

for i in range(5):
    if i == 3:
        break  # Sale del bucle cuando i es igual a 3
    print(f"Valor de i: {i}")

# - `continue`: Salta a la siguiente iteración del bucle.
print("Ejemplo de continue:")

for i in range(5):
    if i == 2:
        continue  # Salta a la siguiente iteración cuando i es igual a 2
    print(f"Valor de i: {i}")

# - `pass`: No hace nada, se utiliza como un marcador de posición.
print("Ejemplo de pass:")

for i in range(5):
    if i == 2:
        pass  # No hace nada, pero permite que el bucle continúe
    print(f"Valor de i: {i}")

# Estas estructuras de control son esenciales para crear programas que puedan tomar decisiones, repetir acciones y manejar errores de manera efectiva. Su comprensión y uso adecuado son fundamentales para cualquier programador en Python.
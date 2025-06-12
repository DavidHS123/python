# Las variables en Python son espacios en memoria que almacenan datos.

# Los nombres de variables deben comenzar con una letra o guion bajo, y pueden contener letras, números y guiones bajos. SIEMPRE deben comenzar con una letra o guion bajo, no con un número.

# Ejemplos de nombres de variables válidos e inválidos
variable_1 = "Esto es una variable válida"
# 1variable = "Esto no es una variable válida" 
# Esto generará un error de sintaxis

# Por otra parte, las variables son sensibles a mayúsculas y minúsculas, lo que significa que `variable` y `Variable` son dos variables diferentes.
variable = "Esto es una variable"
Variable = "Esto es otra variable"
print(variable)  # Imprime: Esto es una variable
print(Variable)  # Imprime: Esto es otra variable

# Python no permite nombres de variables que sean palabras reservadas del lenguaje, como `if`, `else`, `while`, `for`, etc.
# A continuación, se muestra una lista de las palabras reservadas en Python:
import keyword # Importa el módulo keyword para acceder a las palabras reservadas
# Imprime las palabras reservadas en Python
print("Palabras reservadas en Python:")
for palabra in keyword.kwlist:
    print(palabra)
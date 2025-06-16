# Orden de evaulución de los operadores en Python:
# 1. Operadores de paréntesis ()
# 2. Operadores de exponenciación (**)
# 4. Operadores de multiplicación, división, división entera y módulo (*, /, //, %)
# 5. Operadores de suma y resta (+, -)
# 6. Orden de evaluación en caso de igualdad, de izquierda a derecha.


# En este ejemplo, se evalúa la expresión 1 + 2 * 3 - 4 / 5 ** 6 siguiendo el orden de precedencia de los operadores:
# 1. Primero se evalúa la exponenciación: 5 ** 6 = 15625
# 2. Luego se evalúa la división: 4 / 15625 = 0.000256
# 3. Después se evalúa la multiplicación: 2 * 3 = 6
# 4. Finalmente, se evalúan la suma y la resta: 1 + 6 - 0.000256 = 6.999744
x = 1 + 2 * 3 - 4 / 5 ** 6
print(x)
# Resultado: 6.999744

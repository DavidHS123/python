# Un operador es un elemento del lenguaje que realiza una acción sobre uno o más operandos. Los operadores son fundamentales en la programación, ya que permiten realizar cálculos, comparaciones y manipulación de datos.

# En Python, existen varios tipos de operadores, cada uno con su propia funcionalidad. A continuación, se describen los principales tipos de operadores en Python:

# 1. Operadores Aritméticos: Realizan operaciones matemáticas básicas.
operador_suma = 5 + 3  # Suma
operador_resta = 5 - 3  # Resta
operador_multiplicacion = 5 * 3  # Multiplicación
operador_exponente = 5 ** 3  # Exponente (potencia)
operador_division = 5 / 3  # División
operador_division_entera = 5 // 3  # División entera
operador_modulo = 5 % 3  # Módulo (resto de la división)

# Tambien se pueden utilizar los operadores entre variables con la misma funcionalidad, llamados operadores de asignación.
variable_a = 5
variable_b = 3
variable_a += variable_b  # Suma y asigna (equivalente a variable_a = variable_a + variable_b)
variable_a -= variable_b  # Resta y asigna (equivalente a variable_a = variable_a - variable_b)
# También se pueden utilizar otros operadores de asignación como *=, **=, /=, //=, %=, etc.

# 2. Operadores de Comparación: Comparan dos valores y devuelven un valor booleano (True o False).
operador_igual = (5 == 3)  # Igualdad (mismo VALOR, no confundir con identidad)
operador_diferente = (5 != 3)  # Diferente
operador_mayor_que = (5 > 3)  # Mayor que
operador_menor_que = (5 < 3)  # Menor que
operador_mayor_igual = (5 >= 3)  # Mayor o igual que
operador_menor_igual = (5 <= 3)  # Menor o igual que

# 3. Operadores de cadena de texto: Realizan operaciones sobre cadenas de texto.
operador_concatenacion = "Hola, " + "Python"  # Concatenación de cadenas
operador_repeticion = "Python" * 3  # Repetición de cadena

# 4. Operadores Lógicos: Realizan operaciones lógicas y devuelven un valor booleano.
operador_and = True and False  # AND lógico
operador_or = True or False  # OR lógico
operador_not = not True  # NOT lógico

# En Python, los operadores lógicos devuelven el primer valor que determina el resultado lógico, no necesariamente un valor booleano.

# Evaluación paso a paso:
# 1. El operador 'and' tiene mayor prioridad que 'or'.
# 2. Se evalúa 2 and 3: ambos son verdaderos (no cero), así que devuelve el último valor, 3.
# 3. Ahora la expresión es: 0 or 3 or 4
# 4. Se evalúa 0 or 3: 0 es falso, así que devuelve 3.
# 5. Finalmente, 3 or 4: 3 es verdadero, así que devuelve 3.

resultado = 0 or 2 and 3 or 4  # El resultado será 3

print("El resultado de '0 or 2 and 3 or 4' es:", resultado)

# 5. Operadores de Identidad: Verifican si dos variables son el mismo objeto en memoria (mismo id()).
operador_is = (variable_a is variable_b)  # Verifica si son el mismo objeto
operador_is_not = (variable_a is not variable_b)  # Verifica si no son el mismo objeto

# 6. Operadores de Pertenencia: Verifican si un valor pertenece a una secuencia (como una lista o una cadena).
operador_in = 5 in [1, 2, 3, 4, 5]  # Verifica si el valor está en la lista
operador_not_in = 6 not in [1, 2, 3, 4, 5]  # Verifica si el valor no está en la lista

# 7. Operadores Bit a Bit: Realizan operaciones a nivel de bits.
operador_and_bit = 5 & 3  # AND bit a bit
operador_or_bit = 5 | 3  # OR bit a bit
operador_xor_bit = 5 ^ 3  # XOR bit a bit
operador_desplazamiento_izquierda = 5 << 1  # Desplazamiento a la izquierda
operador_desplazamiento_derecha = 5 >> 1  # Desplazamiento a la derecha
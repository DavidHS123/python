# Las estructuras de control en Python son fundamentales para dirigir el flujo de ejecución del programa. Permiten tomar decisiones, repetir acciones y manejar excepciones. A continuación, se describen las principales estructuras de control:
# 1. Condicionales (`if`, `elif`, `else`):
# Permiten ejecutar bloques de código basados en condiciones.
# Donde if evalúa una condición, y si es verdadera, ejecuta el bloque de código correspondiente. `elif` permite evaluar múltiples condiciones, y `else` se ejecuta si ninguna de las condiciones anteriores es verdadera.
if True:
    print("Esto se ejecuta si la condición es verdadera.")
elif False:
    print("Esto se ejecuta si la condición anterior es falsa y esta es verdadera.")
else:
    print("Esto se ejecuta si todas las condiciones anteriores son falsas.")

# En las condicionales, los valores que devuelven los operadores de comparación son booleanos (`True` o `False`) y dependiendo de su valor, se ejecutará un bloque de código o no, y saltara al siguiente paso.
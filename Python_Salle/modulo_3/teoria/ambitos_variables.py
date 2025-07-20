# Ámbitos de variables en Python (LEGB: Local, Enclosing, Global, Built-in)

# 1. Ámbito Local: Variable definida dentro de una función, solo accesible ahí.
def ejemplo_local():
    x = "local"
    print(x)  # Imprime 'local'

# 2. Ámbito Enclosing: Variable definida en una función externa, accesible en funciones internas.
def funcion_externa():
    y = "enclosing"
    def funcion_interna():
        print(y)  # Imprime 'enclosing'
    funcion_interna()

# 3. Ámbito Global: Variable definida fuera de funciones, accesible en todo el archivo.
z = "global"
def ejemplo_global():
    global z
    z = "modificado"
    print(z)  # Imprime 'modificado'

# 4. Ámbito Built-in: Funciones y nombres predefinidos de Python.
def ejemplo_builtin():
    print(len("Python"))  # Usa la función incorporada 'len'
    print(type(123))      # Usa la función incorporada 'type'

# Ejemplo de uso:
ejemplo_local()
funcion_externa()
ejemplo_global()
ejemplo_builtin()
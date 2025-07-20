# En Python, un docstring (document string) es una cadena de texto que se coloca justo después de la definición de una función, clase o módulo.
# Sirve para documentar el propósito y el uso del bloque de código al que acompaña.
# Los docstrings se escriben entre comillas triples (""") y pueden ser accedidos mediante la propiedad __doc__ del objeto.

def ejemplo_funcion(parametro):
    """
    Esta es una función de ejemplo que muestra cómo usar un docstring.
    
    Parámetros:
        parametro (str): Un texto que será mostrado por pantalla.
    
    Retorna:
        None
    """
    print(parametro)

# Puedes acceder al docstring así:
print(ejemplo_funcion.__doc__)

# Ventajas de usar docstrings:
# - Facilitan la comprensión del código por otros desarrolladores (o por ti mismo en el futuro).
# - Herramientas como help() y generadores de documentación los utilizan para mostrar información sobre funciones, clases y módulos.
# - Permiten mantener un código más limpio y organizado al documentar directamente en el lugar donde se define la función o clase.
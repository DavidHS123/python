# En este programa, haremos un convertidor de pisos europeos al sistema de pisos estadounidense, donde practicaremos el uso de variables, entrada de datos y conversión de tipos.
# En Europa, el primer piso es el piso 0, mientras que en Estados Unidos, el primer piso es el piso 1.
# # Ejemplo:
# # - Si el usuario introduce 0, el programa debe mostrar 1.
# # - Si el usuario introduce 1, el programa debe mostrar 2.
piso_europeo = int(input("Introduce el número de piso europeo: "))
# Convertimos el número de piso europeo al sistema estadounidense
piso_estadounidense = piso_europeo + 1
# Mostramos el resultado
print(f"El número de piso estadounidense es: {piso_estadounidense}")

# Este programa es un ejemplo simple de cómo convertir un número de piso de un sistema a otro.
# Podemos ampliarlo para incluir más funcionalidades, como manejar errores de entrada o permitir al usuario elegir entre diferentes sistemas de numeración de pisos.
# Este es el primer programa de Python que ejecuto en el curso.
# Es un programa en el que imprimiremos preguntas de python y esperaremos la respuesta del usuario.
# Si la respuesta es correcta, imprimiremos un mensaje de éxito, si no, un mensaje de error.
# Tambien tendremos un contador de aciertos y fallos.

# Importando la libreria os para limpiar la pantalla
import os

aciertos = 0
fallos = 0

print("Bienvenidos al Test 1 de Python")
print("Responde las siguientes preguntas correctamente para demostrar tus conocimientos.")
print("Cada respuesta correcta suma un punto, cada respuesta incorrecta resta un punto.")
print("Al final del test, se mostrará tu puntuación total.")
print("Las respuestas deben ser introducidas en minúsculas (a, b, c, d).")
print("Si estas preparado, pulsa Enter para comenzar...")
# Esperamos a que el usuario pulse Enter para comenzar
input()
# Limpiamos la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Preguntas del test
print("1. ¿Cuál es el objetivo principal de aprender a programar?")

print("a) Memorizar comandos")
print("b) Dar instrucciones a una computadora para resolver problemas")
print("c) Usar la computadora solo para tareas básicas")
print("d) Aprender a usar programas de Office")

# Esperamos la respuesta del usuario ý la convertimos a minúsculas para facilitar la comparación
respuesta = input("Tu respuesta: ").lower()

# Verificamos la respuesta
if respuesta == "b":
    print("¡Correcto! Has acertado.")
    aciertos += 1
else:
    print("Incorrecto. La respuesta correcta es la b.")
    fallos += 1
input("Pulsa Enter para continuar...")
# Limpiamos la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

print("2. ¿Qué es un lenguaje de programación?")
print("a) Un conjunto de instrucciones que una computadora puede entender y ejecutar")
print("b) Un software para escribir documentos")
print("c) Un dispositivo de entrada de datos")
print("d) Un sistema operativo")

respuesta = input("Tu respuesta: ").lower()

if respuesta == "a":
    print("¡Correcto! Has acertado.")
    aciertos += 1
else:
    print("Incorrecto. La respuesta correcta es la a.")
    fallos += 1
input("Pulsa Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')


# En este programa, usaremos un bucle for para iterar sobre una lista de prendas e imprimiremos una frase con cada elemento de la lista.

print("Ejemplo de iteración sobre una lista de prendas:")

# Definimos una lista de prendas
prendas = ["camisa", "gorra", "chaqueta", "bufanda"]

# Iteramos sobre la lista de prendas
for prenda in prendas:

    # Imprimimos una frase con cada prenda
    print(f"Hoy llevo puesta una {prenda}.")

# Imprimimos un mensaje final
print("¡Lista de prendas procesada con éxito!")
print("") # Línea en blanco para mejorar la legibilidad

# Este programa imprimirá una frase para cada prenda en la lista, indicando que se lleva puesta esa prenda.
# Puedes modificar la lista de prendas para incluir las que desees.

# También puedes usar un diccionario si quieres asociar cada prenda con un color o una talla, por ejemplo:
print("Ejemplo de iteración sobre un diccionario de prendas y colores:")

prendas_colores = {
    "camisa": "azul",
    "gorra": "roja",
    "chaqueta": "negra",
    "bufanda": "verde"
}

# Iteramos sobre el diccionario de prendas y colores
for prenda, color in prendas_colores.items():
    
    # Imprimimos una frase con cada prenda y su color
    print(f"La {prenda} es de color {color}.")

# Imprimimos un mensaje final
print("¡Lista de prendas y colores procesada con éxito!")
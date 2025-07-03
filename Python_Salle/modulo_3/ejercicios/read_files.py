# Este ejercicio lee un archivo de texto y muestra su contenido
archivo = open("text1.txt", "r")
contenido = archivo.read()
archivo.close()

print("Contenido del archivo:")
print(contenido)
# En este ejercicio, trataremos de leer una cadena de texto con formato CSV y la convertiremos en una lista de diccionarios.


# Esta cadena de texto esta harcodeada, pero en un caso real, podría provenir de un archivo o una API.
datos = """Marca,Modelo,Año
            Seat,Leon,2010
            Chevrolet,Camaro,1968
            Land Rover,Uno,1945"""

def csv_a_diccionario(csv_string):
    # Dividir la cadena en líneas
    lineas = csv_string.strip().split('\n')
    
    # Obtener las cabeceras de las columnas
    cabeceras = lineas[0].split(',')
    
    # Crear una lista para almacenar los diccionarios
    coches = []
    
    # Recorrer las líneas restantes y crear un diccionario por cada línea
    for linea in lineas[1:]:
        valores = linea.split(',')
        coche = {cabecera.strip(): valor.strip() for cabecera, valor in zip(cabeceras, valores)}
        coches.append(coche)   
            
# Imprimir la lista de diccionarios
    print(coches)

csv_a_diccionario(datos)
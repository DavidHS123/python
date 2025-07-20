# Gestionar CSV en Python

import csv
# Crear archivo CSV
with open('datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Edad', 'Ciudad'])
    writer.writerow(['David', 19, 'Barcelona'])
    writer.writerow(['Ana', 22, 'Madrid'])
    writer.writerow(['Luis', 25, 'Valencia'])
# Leer archivo CSV

with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    print("Contenido del archivo CSV:")
    for row in reader:
        print(row)
        
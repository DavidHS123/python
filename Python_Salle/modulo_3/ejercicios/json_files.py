# Gestionar archivos JSON en Python

import json

# Crear archivo JSON
with open('datos.json', 'w') as file:
    data = {
        "nombre": "David",
        "edad": 19,
        "ciudad": "Barcelona"
    }
    json.dump(data, file)

# Leer archivo JSON
with open('datos.json', 'r') as file:
    data = json.load(file)
    print("Contenido del archivo JSON:")
    print(data)

# Actualizar archivo JSON
data['edad'] = 20   # Cambiar la edad
with open('datos.json', 'w') as file:
    json.dump(data, file)

# Leer archivo JSON actualizado
with open('datos.json', 'r') as file:
    data = json.load(file)
    print("Contenido del archivo JSON actualizado:")
    print(data)

# Este ejercicio ordena las notas de los alumnos de mayor a menor por cada assignatura.
alumnes = [
    {
        "nom": "Rossana",
        "notes": [
            ("matemàtiques", [8, 9, 7]),
            ("ciències", [7, 8, 7, 7.2]),
            ("música", [10, 9, 9, 8, 9, 9.5])
        ]
    },
    {
        "nom": "Lluis",
        "notes": [
            ("matemàtiques", [8, 9, 9.5]),
            ("ciències", [6, 8, 7, 5.4]),
            ("català", [10, 8, 9])
        ]
    },
    {
        "nom": "Ruben",
        "notes": [
            ("matemàtiques", [6, 5.5, 7]),
            ("català", [9, 8, 7]),
            ("música", [8, 9, 7, 6, 5, 7.5])
        ]
    }
]

# Diccionario para almacenar las notas finales de cada asignatura
notes_finals = {
    "matemàtiques": [],
    "ciències": [],
    "música": [],
    "català": []
}

def calcular_nota_final(notas):
    """
    Calcula la nota final a partir de una lista de notas.
    
    Parámetros:
        notas (list): Lista de notas numéricas.
        
    Retorna:
        float: La nota final calculada como el promedio de las notas.
    """
    return round(sum(notas) / len(notas), 1) if notas else 0

for alumne in alumnes:
    for materia, notes in alumne["notes"]:
        # Calcular la nota final para cada asignatura
        nota_final = calcular_nota_final(notes)
        # Añadir la nota final al diccionario
        notes_finals[materia].append((alumne["nom"], nota_final))
        

# Ordenar las notas de cada asignatura de mayor a menor
for materia in notes_finals:
    # Ordenar la lista de tuplas por la nota final (índice 1) en orden descendente
    notes_finals[materia].sort(key=lambda alumne: alumne[1], reverse=True)
    # Variable para almacenar el texto de salida
    text = f"Notas de {materia}:"
    # Concatenar los nombres y notas finales en el texto
    for alumne in notes_finals[materia]:
        nom, nota_final = alumne
        # si es el ultimo elemento de la lista
        if alumne == notes_finals[materia][-1]:
            text += f" {nom} {nota_final}"
        else:
            text += f" {nom} {nota_final},"
        
    print(text)
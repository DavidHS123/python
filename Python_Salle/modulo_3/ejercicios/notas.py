# Este ejercicio calcula las notas finales de todos los estudiantes y muestra por la consola en el formato "Omar ha sacado un 7.3 en la assignatura "matemáticas"".

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

def calcular_nota_final(notas):
    """
    Calcula la nota final a partir de una lista de notas.
    
    Parámetros:
        notas (list): Lista de notas numéricas.
        
    Retorna:
        float: La nota final calculada como el promedio de las notas.
    """
    return sum(notas) / len(notas) if notas else 0

def mostrar_notas(alumnes):
    """
    Muestra las notas finales de todos los estudiantes en el formato especificado.
    
    Parámetros:
        alumnes (list): Lista de diccionarios con la información de los estudiantes y sus notas.
    """
    for alumne in alumnes:
        nom = alumne["nom"]
        for materia, notes in alumne["notes"]:
            nota_final = calcular_nota_final(notes)
            print(f"{nom} ha sacado un {nota_final:.1f} en la assignatura \"{materia}\"")

mostrar_notas(alumnes)
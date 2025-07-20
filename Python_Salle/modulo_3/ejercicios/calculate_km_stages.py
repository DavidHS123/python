''' Exercici:
      - Crear una llista d'etapes d'una ruta de muntanya que tingui: número d'etapa, lloc d'origen, lloc de destí, distància i desnivell acumulat
      - Fer una funció que rebi dos números d'etapa com a paràmetres i retorni en un diccionari l'inici, el final i els kilómetres i el desnivell totals
      - Obligatori usar filter i reduce, com a mínim '''

etapes = [
    {"etapa": 1, "origen": "Barcelona", "desti": "Manresa", "distancia": 80, "desnivell": 500},
    {"etapa": 3, "origen": "Berga", "desti": "Solsona", "distancia": 60, "desnivell": 300},
    {"etapa": 2, "origen": "Manresa", "desti": "Berga", "distancia": 40, "desnivell": 700},
    {"etapa": 4, "origen": "Solsona", "desti": "Lleida", "distancia": 50, "desnivell": 200},
    {"etapa": 5, "origen": "Lleida", "desti": "Sort", "distancia": 70, "desnivell": 800},
    {"etapa": 7, "origen": "Vielha", "desti": "Benasque", "distancia": 110, "desnivell": 1500},
    {"etapa": 6, "origen": "Sort", "desti": "Vielha", "distancia": 90, "desnivell": 1200},
    {"etapa": 8, "origen": "Benasque", "desti": "Ainsa", "distancia": 30, "desnivell": 400}
]

'''
- definir una función 
- filtrar etapas incluidas 
- guardar en variables inicio y final 
- sumar quilometros 
- sumar desniveles 
- devolver inicio, final, km y desnivel 
- probar la función (con casos extremos)  '''

from functools import reduce

def calcular_etapes(etapa_inicial, etapa_final):
    numero_etapes = list(map(lambda x: x['etapa'], etapes))
    if etapa_inicial not in numero_etapes or etapa_final not in numero_etapes:
        return "Etapa no encontrada"
    
    if etapa_inicial == etapa_inicial:
        lista_etapas = list(filter(lambda x: etapa_inicial <= x['etapa'] <= etapa_final, etapes))
        etapa= lista_etapas[0]
        return {
            "inici": etapa['origen'],
            "final": etapa['desti'],
            "km": reduce(lambda x, y: x + y['distancia'], lista_etapas, 0),
            "desnivell": reduce(lambda x, y: x + y['desnivell'], lista_etapas, 0)
        }
    comprovacio = []
    comprovacio.extends = list(filter(lambda x: x['etapa'] == etapa_inicial or x['etapa'] == etapa_final, etapes))
    if len(comprovacio) != 2:
        return "Etapa no encontrada"
    
    llista_etapes = list(filter(lambda x: etapa_inicial <= x['etapa'] <= etapa_final, etapes))

    llista_etapes.sort(key=lambda x: x['etapa'])
    etapa_inici = llista_etapes[0]["origen"]
    etapa_final = llista_etapes[-1]["desti"]

    km_total = reduce(lambda x, y: x + y['distancia'], llista_etapes, 0)
    desnivell_total = reduce(lambda x, y: x + y['desnivell'], llista_etapes, 0)

    return {
        "inici": etapa_inici,
        "final": etapa_final,
        "km": km_total,
        "desnivell": desnivell_total
    }

# Proves de la funció
print(calcular_etapes(1, 3))  # Etapa 1 a 3
print(calcular_etapes(2, 5))  # Etapa 2 a 5
print(calcular_etapes(6, 8))  # Etapa 6 a 8
print(calcular_etapes(1, 8))  # Etapa 1 a 8
print(calcular_etapes(3, 7))  # Etapa 3 a
print(calcular_etapes(1, 10))  # Etapa 1 a 10 (no existeix)
print(calcular_etapes(0, 2))  # Etapa 0 a 2 (no existeix)
print(calcular_etapes(2, 2))  # Etapa 2 a 2 (cas extrem)
print("---------------------")
print(calcular_etapes(2,4))  # correcte
print(calcular_etapes(0,0))  # zero
print(calcular_etapes(5,5))  # només una etapa
print(calcular_etapes(15,18))  # etapes fora de rang
print(calcular_etapes(1,18))   # una etapa fora de rang
    


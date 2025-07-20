# En este programa, simularemos un combate donde se enfrentan dos Pokémon. Cada pokémon tiene un tipo, nivel y un ataque.

# Exemple de combat:
# Combat Pokémon:

# Pikachu (nivell 13) ha llençat l'atac Impactrueno ⚡
# Squirtle s'ha defensat de l'atac

# Squirtle (nivell 17) ha llençat l'atac Pistola agua 💧
# Pikachu s'ha defensat de l'atac


from pokemon import dades, combat

def combat_pokemon(nom_pokemon1, nom_pokemon2):
    pokemon1 = dades.pokedex[nom_pokemon1]
    pokemon2 = dades.pokedex[nom_pokemon2]
    
    print(combat.atacar(nom_pokemon1, pokemon1['nivell'], pokemon1['atac'], pokemon1['tipus']))
    print(combat.defensa(nom_pokemon2))
    print(combat.atacar(nom_pokemon2, pokemon2['nivell'], pokemon2['atac'], pokemon2['tipus']))
    print(combat.defensa(nom_pokemon1))

combat_pokemon('Pikachu', 'Squirtle')
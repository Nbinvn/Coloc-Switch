# config.py
# Configuration globale, constantes et données de base pour MK8 et FC26

APP_PASSWORD = "coloc2026"  # Mot de passe commun

DEFAULT_ROOMMATES = ["Coloc 1", "Coloc 2", "Coloc 3"]

# Mario Kart 8 Deluxe - Circuits avec niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile)
MK8_TRACKS = {
    # Coupe Champignon
    "Champidrome": {"cup": "Champignon", "difficulty": 1},
    "Voie Lagon": {"cup": "Champignon", "difficulty": 1},
    "Aéroport Azur": {"cup": "Champignon", "difficulty": 2},
    "Aux Délices Sucrés": {"cup": "Champignon", "difficulty": 1},
    # Coupe Fleur
    "Thomp Docks": {"cup": "Fleur", "difficulty": 2},
    "Circuit Mario": {"cup": "Fleur", "difficulty": 1},
    "Piste aux Delices": {"cup": "Fleur", "difficulty": 2},
    "Manoir de Tremplin": {"cup": "Fleur", "difficulty": 2},
    # Coupe Étoile
    "Aéroport Soleil": {"cup": "Étoile", "difficulty": 2},
    "Dauphin Dolfino": {"cup": "Étoile", "difficulty": 2},
    "Electrodrome": {"cup": "Étoile", "difficulty": 2},
    "Mont Enneigé": {"cup": "Étoile", "difficulty": 3},
    # Coupe Spéciale
    "Voie Céleste": {"cup": "Spéciale", "difficulty": 3},
    "Désert Bone-Dry": {"cup": "Spéciale", "difficulty": 3},
    "Château de Bowser": {"cup": "Spéciale", "difficulty": 3},
    "Route Arc-en-ciel (Wii/Switch)": {"cup": "Spéciale", "difficulty": 3},
    # DLC Pass Extra
    "Promenade à Paris": {"cup": "Pass DLC", "difficulty": 1},
    "Circuit Choco 3": {"cup": "Pass DLC", "difficulty": 2},
    "Supermarché Cocon": {"cup": "Pass DLC", "difficulty": 2},
    "Odyssée à la Cité": {"cup": "Pass DLC", "difficulty": 3},
    "Piste Corniche": {"cup": "Pass DLC", "difficulty": 3},
}

MK8_CHARACTERS = [
    "Mario", "Luigi", "Peach", "Daisy", "Rosalina", "Yoshi", "Toad", "Koopa",
    "Shy Guy", "Wario", "Waluigi", "Bowser", "Donkey Kong", "Link", "Isabelle",
    "Inkling", "Funky Kong", "Peachette", "Pauline", "Kamek"
]

# FC26 Équipes par défaut
FC26_DEFAULT_TEAMS = {
    "Real Madrid": 5.0,
    "Manchester City": 5.0,
    "Paris Saint-Germain": 5.0,
    "Bayern Munich": 5.0,
    "Arsenal": 4.5,
    "FC Barcelone": 4.5,
    "Inter Milan": 4.5,
    "Bayer Leverkusen": 4.5,
    "Olympique de Marseille": 4.0,
    "Olympique Lyonnais": 3.5,
    "AS Monaco": 4.0,
    "Équipe Nationale de France": 5.0,
}
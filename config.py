# config.py

APP_PASSWORD = "coloc2026"

DEFAULT_ROOMMATES = ["Coloc 1", "Coloc 2", "Coloc 3"]

# URL générique pour les circuits sans image spécifique
DEFAULT_MK_IMG = "https://upload.wikimedia.org/wikipedia/fr/a/a9/Mario_Kart_8_logo.png"

MK8_TRACKS = {
    "Champidrome": {"cup": "Champignon", "difficulty": 1, "image": DEFAULT_MK_IMG},
    "Voie Lagon": {"cup": "Champignon", "difficulty": 1, "image": DEFAULT_MK_IMG},
    "Aéroport Azur": {"cup": "Champignon", "difficulty": 2, "image": DEFAULT_MK_IMG},
    "Aux Délices Sucrés": {"cup": "Champignon", "difficulty": 1, "image": DEFAULT_MK_IMG},
    "Thomp Docks": {"cup": "Fleur", "difficulty": 2, "image": DEFAULT_MK_IMG},
    "Circuit Mario": {"cup": "Fleur", "difficulty": 1, "image": DEFAULT_MK_IMG},
    "Mont Enneigé": {"cup": "Étoile", "difficulty": 3, "image": DEFAULT_MK_IMG},
    "Route Arc-en-ciel": {"cup": "Spéciale", "difficulty": 3, "image": "https://mario.wiki.gallery/images/thumb/3/36/MK8_Rainbow_Road_Course_Icon.png/250px-MK8_Rainbow_Road_Course_Icon.png"},
    "Promenade à Paris": {"cup": "Pass DLC", "difficulty": 1, "image": DEFAULT_MK_IMG},
    "Odyssée à la Cité": {"cup": "Pass DLC", "difficulty": 3, "image": DEFAULT_MK_IMG},
}

MK8_CHARACTERS = [
    "Mario", "Luigi", "Peach", "Daisy", "Rosalina", "Yoshi", "Toad", "Bowser", "Donkey Kong", "Link"
]

FC26_DEFAULT_TEAMS = {
    "Real Madrid": 5.0,
    "Manchester City": 5.0,
    "Paris Saint-Germain": 5.0,
    "Arsenal": 4.5,
    "Olympique de Marseille": 4.0,
    "Olympique Lyonnais": 3.5,
}

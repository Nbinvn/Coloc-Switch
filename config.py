# config.py

APP_PASSWORD = "coloc2026"
DEFAULT_ROOMMATES = ["Coloc 1", "Coloc 2", "Coloc 3"]

DEFAULT_LOGO = "https://cdn-icons-png.flaticon.com/512/564/564419.png" # Ballon générique
DEFAULT_MK_TRACK_IMG = "https://upload.wikimedia.org/wikipedia/fr/a/a9/Mario_Kart_8_logo.png"

# ==========================================
# MARIO KART 8 DELUXE - PERSONNAGES (50)
# ==========================================
MK8_CHARACTERS = {
    # Super Mario
    "Mario": {"image": "https://mario.wiki.gallery/images/3/3e/Mario_-_Mario_Kart_8.png"},
    "Luigi": {"image": "https://mario.wiki.gallery/images/6/6f/Luigi_-_Mario_Kart_8.png"},
    "Peach": {"image": "https://mario.wiki.gallery/images/3/30/Peach_-_Mario_Kart_8.png"},
    "Daisy": {"image": "https://mario.wiki.gallery/images/5/52/Daisy_-_Mario_Kart_8.png"},
    "Rosalina": {"image": "https://mario.wiki.gallery/images/f/fc/Rosalina_-_Mario_Kart_8.png"},
    "Mario de Métal": {"image": "https://mario.wiki.gallery/images/7/7b/Metal_Mario_-_Mario_Kart_8.png"},
    "Peach d'Or Rose": {"image": "https://mario.wiki.gallery/images/a/ab/Pink_Gold_Peach_-_Mario_Kart_8.png"},
    "Yoshi": {"image": "https://mario.wiki.gallery/images/2/23/Yoshi_-_Mario_Kart_8.png"},
    "Toad": {"image": "https://mario.wiki.gallery/images/f/f6/Toad_-_Mario_Kart_8.png"},
    "Toadette": {"image": "https://mario.wiki.gallery/images/c/cb/Toadette_-_Mario_Kart_8.png"},
    "Koopa Troopa": {"image": "https://mario.wiki.gallery/images/4/4e/Koopa_Troopa_-_Mario_Kart_8.png"},
    "Maskass": {"image": "https://mario.wiki.gallery/images/6/62/Shy_Guy_-_Mario_Kart_8.png"},
    "Lakitu": {"image": "https://mario.wiki.gallery/images/1/13/Lakitu_-_Mario_Kart_8.png"},
    "Wario": {"image": "https://mario.wiki.gallery/images/6/68/Wario_-_Mario_Kart_8.png"},
    "Waluigi": {"image": "https://mario.wiki.gallery/images/5/5e/Waluigi_-_Mario_Kart_8.png"},
    "Donkey Kong": {"image": "https://mario.wiki.gallery/images/0/07/Donkey_Kong_-_Mario_Kart_8.png"},
    "Bowser": {"image": "https://mario.wiki.gallery/images/1/14/Bowser_-_Mario_Kart_8.png"},
    "Skelerex": {"image": "https://mario.wiki.gallery/images/f/fb/Dry_Bones_-_Mario_Kart_8_Deluxe.png"},
    "Bowser Jr.": {"image": "https://mario.wiki.gallery/images/d/df/Bowser_Jr._-_Mario_Kart_8_Deluxe.png"},
    "Bowser Skelet": {"image": "https://mario.wiki.gallery/images/8/86/Dry_Bowser_-_Mario_Kart_8.png"},
    "Roi Boo": {"image": "https://mario.wiki.gallery/images/a/a2/King_Boo_-_Mario_Kart_8_Deluxe.png"},
    # Bébés
    "Bébé Mario": {"image": "https://mario.wiki.gallery/images/8/87/Baby_Mario_-_Mario_Kart_8.png"},
    "Bébé Luigi": {"image": "https://mario.wiki.gallery/images/4/42/Baby_Luigi_-_Mario_Kart_8.png"},
    "Bébé Peach": {"image": "https://mario.wiki.gallery/images/7/7b/Baby_Peach_-_Mario_Kart_8.png"},
    "Bébé Daisy": {"image": "https://mario.wiki.gallery/images/2/2f/Baby_Daisy_-_Mario_Kart_8.png"},
    "Bébé Harmonie": {"image": "https://mario.wiki.gallery/images/2/29/Baby_Rosalina_-_Mario_Kart_8.png"},
    # Koopalings
    "Lemmy": {"image": "https://mario.wiki.gallery/images/9/90/Lemmy_Koopa_-_Mario_Kart_8.png"},
    "Larry": {"image": "https://mario.wiki.gallery/images/4/41/Larry_Koopa_-_Mario_Kart_8.png"},
    "Wendy": {"image": "https://mario.wiki.gallery/images/b/bd/Wendy_O._Koopa_-_Mario_Kart_8.png"},
    "Ludwig": {"image": "https://mario.wiki.gallery/images/9/96/Ludwig_von_Koopa_-_Mario_Kart_8.png"},
    "Iggy": {"image": "https://mario.wiki.gallery/images/6/64/Iggy_Koopa_-_Mario_Kart_8.png"},
    "Roy": {"image": "https://mario.wiki.gallery/images/e/ef/Roy_Koopa_-_Mario_Kart_8.png"},
    "Morton": {"image": "https://mario.wiki.gallery/images/c/c5/Morton_Koopa_Jr._-_Mario_Kart_8.png"},
    # Crossovers & Variants
    "Link": {"image": "https://mario.wiki.gallery/images/1/18/Link_-_Mario_Kart_8.png"},
    "Villageois (Garçon)": {"image": "https://mario.wiki.gallery/images/a/a8/VillagerBoy_-_Mario_Kart_8.png"},
    "Villageoise (Fille)": {"image": "https://mario.wiki.gallery/images/d/da/VillagerGirl_-_Mario_Kart_8.png"},
    "Marie": {"image": "https://mario.wiki.gallery/images/b/b3/Isabelle_-_Mario_Kart_8.png"},
    "Inkling Garçon": {"image": "https://mario.wiki.gallery/images/7/79/InklingBoy_-_Mario_Kart_8_Deluxe.png"},
    "Inkling Fille": {"image": "https://mario.wiki.gallery/images/7/77/InklingGirl_-_Mario_Kart_8_Deluxe.png"},
    "Mario Tanooki": {"image": "https://mario.wiki.gallery/images/c/cb/Tanooki_Mario_-_Mario_Kart_8.png"},
    "Peach Chat": {"image": "https://mario.wiki.gallery/images/2/29/Cat_Peach_-_Mario_Kart_8.png"},
    # DLC BCP
    "Birdo": {"image": "https://mario.wiki.gallery/images/3/39/Birdo_-_Mario_Kart_8_Deluxe.png"},
    "Flora Piranha": {"image": "https://mario.wiki.gallery/images/2/2d/Petey_Piranha_-_Mario_Kart_8_Deluxe.png"},
    "Wiggler": {"image": "https://mario.wiki.gallery/images/f/f6/Wiggler_-_Mario_Kart_8_Deluxe.png"},
    "Kamek": {"image": "https://mario.wiki.gallery/images/9/90/Kamek_-_Mario_Kart_8_Deluxe.png"},
    "Pauline": {"image": "https://mario.wiki.gallery/images/2/2b/Pauline_-_Mario_Kart_8_Deluxe.png"},
    "Diddy Kong": {"image": "https://mario.wiki.gallery/images/e/e9/Diddy_Kong_-_Mario_Kart_8_Deluxe.png"},
    "Funky Kong": {"image": "https://mario.wiki.gallery/images/e/e8/Funky_Kong_-_Mario_Kart_8_Deluxe.png"},
    "Peachette": {"image": "https://mario.wiki.gallery/images/0/03/Peachette_-_Mario_Kart_8_Deluxe.png"},
}

# ==========================================
# MARIO KART 8 DELUXE - CIRCUITS (96)
# (Difficulté 1 = Facile, 2 = Moyen, 3 = Difficile)
# ==========================================
MK8_TRACKS = {
    # Coupe Champignon
    "Champidrome": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Parc Glougloop": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Piste aux délices": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Temple Thwomp": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Fleur
    "Circuit Mario": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Promenade Toad": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Manoir englouti": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Cascades Maskass": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Étoile
    "Aéroport Azur": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Lagon Dauphin": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Électrodrome": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Mont Éboulis": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Spéciale
    "Voie Céleste": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Désert Toussec": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Château de Bowser": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Route Arc-en-ciel": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Carapace
    "Wii Prairie Meuh Meuh": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Circuit Mario": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "DS Plage Cheep Cheep": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Autoroute Toad": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Banane
    "GCN Désert Sec Sec": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "SNES Plaine Beigne 3": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Vallée Yoshi": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Autodrome Mario": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Feuille
    "DS Horloge Tic-Tac": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Égout Piranha": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Volcan Grondant": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Train Kalimari": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Éclair
    "DS Stade Wario": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GCN Royaume Sorbet": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Piste Musicale": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Route Arc-en-ciel": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Œuf
    "GCN Circuit Yoshi": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Arène d'Excitebike": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Route du Dragon": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Mute City": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Triforce
    "Wii Mine Wario": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "SNES Route Arc-en-ciel": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Station Glagla": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Circuit Hyrule": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Crossing
    "GCN Parc Baby": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Pays Fromage": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Passage Feuillage": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Animal Crossing": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    # Coupe Clochette
    "3DS Koopapolis": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Route Ruban": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Métro Turbo": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Big Blue": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    # --- PASS CIRCUITS ADDITIONNELS (Vagues 1 à 6) ---
    "Tour Promenade à Paris": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Circuit Toad": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Montagne Choco": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Supermarché Coco": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Traversée de Tokyo": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "DS Corniche Champignon": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Jardin Volant": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Dojo Ninja": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Escapade New-Yorkaise": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "SNES Circuit Mario 3": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "N64 Désert Kalimari": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "DS Flipper Waluigi": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Sprint à Sydney": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Pays Neigeux": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Gorge Champignon": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Cité Sorbet": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Détour à Londres": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Lac Boo": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Mont Éboulis": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Bois Vermeil": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Balade Berlinoise": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "DS Jardins Peach": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Mont Brumeux": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Route Arc-en-ciel": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Virée à Amsterdam": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Riverside Parc": {"difficulty": 1, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Pic DK": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Île de Yoshi": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Bousculade à Bangkok": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "DS Circuit Mario": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GCN Stade Waluigi": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Poursuite à Singapour": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Athènes Antique": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "GCN Paquebot Daisy": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Route Clair de Lune": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Course à la Propreté": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Los Angeles de nuit": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "GBA Pays Crépuscule": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Cap Koopa": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Virages à Vancouver": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Rome Romantique": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "GCN Montagne DK": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Circuit Daisy": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "Piranha Plant Cove": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Tour Madrid Drive": {"difficulty": 2, "image": DEFAULT_MK_TRACK_IMG},
    "3DS Rosalina's Ice World": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "SNES Bowser Castle 3": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
    "Wii Route Arc-en-ciel": {"difficulty": 3, "image": DEFAULT_MK_TRACK_IMG},
}

# ==========================================
# FC 26 - ÉQUIPES
# Structure : { "Ligue": { "Équipe": {"stars": x, "logo": url} } }
# Ce format permet le double menu déroulant "Ligue" -> "Équipe".
# NOTE : la base de données réelle du jeu FC 26 contient plusieurs
# centaines de clubs sous licence. Il n'est pas réaliste de tous les
# lister ici de façon fiable, donc cette liste couvre un très large
# éventail de championnats + les équipes nationales. Tu peux en ajouter
# d'autres à tout moment via "Créer une équipe personnalisée" dans l'appli.
# ==========================================
FC26_TEAMS = {
    "Premier League": {
        "Arsenal": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"},
        "Aston Villa": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f9/Aston_Villa_FC_crest_%282016%29.svg"},
        "Bournemouth": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Brentford": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Brighton": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Chelsea": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"},
        "Crystal Palace": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Everton": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Fulham": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Liverpool": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg"},
        "Manchester City": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"},
        "Manchester United": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg"},
        "Newcastle United": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg"},
        "Nottingham Forest": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Tottenham Hotspur": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"},
        "West Ham United": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Wolverhampton": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "La Liga": {
        "Athletic Bilbao": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Atlético Madrid": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg"},
        "FC Barcelone": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg"},
        "Girona FC": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/9/90/Girona_FC_logo.svg"},
        "Real Betis": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Real Madrid": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"},
        "Real Sociedad": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f1/Real_Sociedad_logo.svg"},
        "Sevilla FC": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Valence CF": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Villarreal CF": {"stars": 4.0, "logo": DEFAULT_LOGO},
    },
    "Ligue 1": {
        "AS Monaco": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/b/ba/AS_Monaco_FC.svg"},
        "FC Nantes": {"stars": 3.0, "logo": DEFAULT_LOGO},
        "Lille OSC": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3f/Lille_OSC_2018_logo.svg"},
        "Olympique de Marseille": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/fr/4/43/Logo_Olympique_de_Marseille.svg"},
        "Olympique Lyonnais": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c6/Olympique_Lyonnais.svg"},
        "Paris Saint-Germain": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"},
        "RC Lens": {"stars": 4.0, "logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/RC_Lens_logo.svg"},
        "RC Strasbourg": {"stars": 3.0, "logo": DEFAULT_LOGO},
        "Stade Rennais": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Toulouse FC": {"stars": 3.0, "logo": DEFAULT_LOGO},
    },
    "Serie A": {
        "AC Milan": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg"},
        "AS Roma": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f7/AS_Roma_logo_%282017%29.svg"},
        "Atalanta": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Bologne": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Fiorentina": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Inter Milan": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/commons/0/05/FC_Internazionale_Milano_2021.svg"},
        "Juventus": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Juventus_FC_2017_icon_%28black%29.svg"},
        "Lazio": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Napoli": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/commons/2/28/S.S.C._Napoli_logo.svg"},
        "Torino": {"stars": 3.0, "logo": DEFAULT_LOGO},
    },
    "Bundesliga": {
        "Bayer Leverkusen": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/5/59/Bayer_04_Leverkusen_logo.svg"},
        "Bayern Munich": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/FC_Bayern_M%C3%BCnchen_logo_%282017%29.svg"},
        "Borussia Dortmund": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/commons/6/67/Borussia_Dortmund_logo.svg"},
        "Eintracht Francfort": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "RB Leipzig": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/0/04/RB_Leipzig_2014_logo.svg"},
        "SC Fribourg": {"stars": 3.0, "logo": DEFAULT_LOGO},
        "VfB Stuttgart": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "VfL Wolfsburg": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "Liga Portugal": {
        "Benfica": {"stars": 4.5, "logo": DEFAULT_LOGO},
        "FC Porto": {"stars": 4.5, "logo": DEFAULT_LOGO},
        "Sporting CP": {"stars": 4.5, "logo": DEFAULT_LOGO},
        "SC Braga": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "Eredivisie": {
        "Ajax": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Feyenoord": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "PSV Eindhoven": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "AZ Alkmaar": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "Süper Lig": {
        "Galatasaray": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Fenerbahçe": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Besiktas": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "Brasileirão": {
        "Flamengo": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Palmeiras": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "São Paulo FC": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "Corinthians": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "MLS": {
        "Inter Miami": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "LA Galaxy": {"stars": 3.5, "logo": DEFAULT_LOGO},
        "LAFC": {"stars": 3.5, "logo": DEFAULT_LOGO},
    },
    "Équipes Nationales": {
        "Allemagne": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e3/DFB_Logo_1995.svg"},
        "Angleterre": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/7/7b/England_national_football_team_crest.svg"},
        "Argentine": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/4/47/Argentine_Football_Association_logo.svg"},
        "Belgique": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/4/43/Royal_Belgian_FA_logo_2019.svg"},
        "Brésil": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/c/cb/Confedera%C3%A7%C3%A3o_Brasileira_de_Futebol_%28CBF%29_logo.svg"},
        "Croatie": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Espagne": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/3/31/Spain_National_Football_Team_badge.svg"},
        "France": {"stars": 5.0, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f9/French_Football_Federation_logo.svg"},
        "Italie": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/3/30/Italian_Football_Federation_logo.svg"},
        "Maroc": {"stars": 4.0, "logo": DEFAULT_LOGO},
        "Pays-Bas": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/7/78/Netherlands_national_football_team_logo.svg"},
        "Portugal": {"stars": 4.5, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3d/Portuguese_Football_Federation.svg"},
    },
}

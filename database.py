# database.py

import sqlite3
import json
from typing import List, Dict, Any
from config import DEFAULT_ROOMMATES, FC26_TEAMS, DEFAULT_LOGO
from config import DEFAULT_ROOMMATES, FC26_TEAMS_MEN, FC26_TEAMS_WOMEN
from placeholders import DEFAULT_PLAYER_AVATAR

DB_FILE = "app_data.db"
DEFAULT_AVATAR = "https://cdn-icons-png.flaticon.com/512/149/149071.png"
DEFAULT_AVATAR = DEFAULT_PLAYER_AVATAR  # image générée localement, ne casse jamais

def get_connection():
    conn = sqlite3.connect(DB_FILE)
@@ -30,7 +31,8 @@ def init_db():
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                stars REAL NOT NULL,
                logo TEXT DEFAULT ''
                logo TEXT DEFAULT '',
                gender TEXT NOT NULL DEFAULT 'Masculin'
            )
        """)
        cursor.execute("""
@@ -48,6 +50,8 @@ def init_db():
        except: pass 
        try: cursor.execute("ALTER TABLE custom_teams ADD COLUMN logo TEXT DEFAULT ''")
        except: pass
        try: cursor.execute("ALTER TABLE custom_teams ADD COLUMN gender TEXT NOT NULL DEFAULT 'Masculin'")
        except: pass

        for roomie in DEFAULT_ROOMMATES:
            cursor.execute("INSERT OR IGNORE INTO players (name, is_guest, elo, avatar) VALUES (?, 0, 1000.0, ?)", (roomie, DEFAULT_AVATAR))
@@ -82,23 +86,34 @@ def update_player_elo(name: str, delta: float):
        cursor.execute("UPDATE players SET elo = elo + ? WHERE name = ?", (delta, name))
        conn.commit()

def get_fc26_teams() -> Dict[str, dict]:
    teams = FC26_TEAMS.copy()
CUSTOM_LEAGUE_NAME = "Équipes Personnalisées"

def get_fc26_teams(gender: str = "Masculin") -> Dict[str, Dict[str, dict]]:
    """Retourne les équipes FC26 groupées par ligue, filtrées par genre :
    { "Nom de la ligue": { "Nom de l'équipe": {"stars": x, "logo": url} } }
    """
    base = FC26_TEAMS_MEN if gender == "Masculin" else FC26_TEAMS_WOMEN
    teams = {league: dict(clubs) for league, clubs in base.items()}
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, stars, logo FROM custom_teams")
        for row in cursor.fetchall():
            teams[row["name"]] = {
                "stars": row["stars"], 
                "logo": row["logo"] if row["logo"] else DEFAULT_LOGO
            }
        cursor.execute("SELECT name, stars, logo FROM custom_teams WHERE gender = ?", (gender,))
        rows = cursor.fetchall()
        if rows:
            teams.setdefault(CUSTOM_LEAGUE_NAME, {})
            for row in rows:
                teams[CUSTOM_LEAGUE_NAME][row["name"]] = {
                    "stars": row["stars"],
                    "logo": row["logo"] or ""
                }
    return teams

def add_custom_team(name: str, stars: float, logo: str):
    final_logo = logo if logo.strip() != "" else DEFAULT_LOGO
def add_custom_team(name: str, stars: float, logo: str, gender: str = "Masculin"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO custom_teams (name, stars, logo) VALUES (?, ?, ?)", (name.strip(), stars, final_logo))
        cursor.execute(
            "INSERT OR REPLACE INTO custom_teams (name, stars, logo, gender) VALUES (?, ?, ?, ?)",
            (name.strip(), stars, logo.strip(), gender)
        )
        conn.commit()

def save_match(game: str, is_official: bool, details: dict, elo_changes: dict):

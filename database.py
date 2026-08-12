# database.py

import sqlite3
import json
from typing import List, Dict, Any
from config import DEFAULT_ROOMMATES, FC26_TEAMS_MEN, FC26_TEAMS_WOMEN
from placeholders import DEFAULT_PLAYER_AVATAR

DB_FILE = "app_data.db"
DEFAULT_AVATAR = DEFAULT_PLAYER_AVATAR  # image générée localement, ne casse jamais

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                is_guest INTEGER NOT NULL DEFAULT 0,
                elo REAL NOT NULL DEFAULT 1000.0,
                avatar TEXT DEFAULT ''
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS custom_teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                stars REAL NOT NULL,
                logo TEXT DEFAULT '',
                gender TEXT NOT NULL DEFAULT 'Masculin'
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                game TEXT NOT NULL,
                is_official INTEGER NOT NULL,
                details_json TEXT NOT NULL,
                elo_changes_json TEXT NOT NULL
            )
        """)
        # Mises à jour silencieuses pour DB existantes
        try: cursor.execute("ALTER TABLE players ADD COLUMN avatar TEXT DEFAULT ''")
        except: pass 
        try: cursor.execute("ALTER TABLE custom_teams ADD COLUMN logo TEXT DEFAULT ''")
        except: pass
        try: cursor.execute("ALTER TABLE custom_teams ADD COLUMN gender TEXT NOT NULL DEFAULT 'Masculin'")
        except: pass

        for roomie in DEFAULT_ROOMMATES:
            cursor.execute("INSERT OR IGNORE INTO players (name, is_guest, elo, avatar) VALUES (?, 0, 1000.0, ?)", (roomie, DEFAULT_AVATAR))
        conn.commit()

def get_all_players() -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players ORDER BY elo DESC")
        return [dict(row) for row in cursor.fetchall()]

def add_guest_player(name: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO players (name, is_guest, elo, avatar) VALUES (?, 1, 1000.0, ?)", (name.strip(), DEFAULT_AVATAR))
        conn.commit()

def update_player_profile(old_name: str, new_name: str, avatar_b64: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET name = ?, avatar = ? WHERE name = ?", (new_name.strip(), avatar_b64, old_name))
        cursor.execute("SELECT id, details_json, elo_changes_json FROM matches")
        for row in cursor.fetchall():
            new_details = row["details_json"].replace(f'"{old_name}"', f'"{new_name}"')
            new_elo = row["elo_changes_json"].replace(f'"{old_name}"', f'"{new_name}"')
            cursor.execute("UPDATE matches SET details_json = ?, elo_changes_json = ? WHERE id = ?", (new_details, new_elo, row["id"]))
        conn.commit()

def update_player_elo(name: str, delta: float):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET elo = elo + ? WHERE name = ?", (delta, name))
        conn.commit()

CUSTOM_LEAGUE_NAME = "Équipes Personnalisées"

def get_fc26_teams(gender: str = "Masculin") -> Dict[str, Dict[str, dict]]:
    """Retourne les équipes FC26 groupées par ligue, filtrées par genre de façon sécurisée."""
    base = FC26_TEAMS_MEN if gender == "Masculin" else FC26_TEAMS_WOMEN
    
    # S'assure de copier proprement la structure de base
    teams = {}
    if isinstance(base, dict):
        for league, clubs in base.items():
            if isinstance(clubs, dict):
                teams[league] = dict(clubs)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, stars, logo FROM custom_teams WHERE gender = ?", (gender,))
        rows = cursor.fetchall()
        if rows:
            teams.setdefault(CUSTOM_LEAGUE_NAME, {})
            for row in rows:
                teams[CUSTOM_LEAGUE_NAME][row["name"]] = {
                    "stars": row["stars"],
                    "logo": row["logo"] or ""
                }
                
    # Sécurité ultime : si le dictionnaire est vide, on renvoie au moins une structure minimale pour éviter le crash
    if not teams:
        teams = {"Ligues par défaut": {"Équipe par défaut": {"stars": 3.0, "logo": ""}}}
        
    return teams

def add_custom_team(name: str, stars: float, logo: str, gender: str = "Masculin"):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO custom_teams (name, stars, logo, gender) VALUES (?, ?, ?, ?)",
            (name.strip(), stars, logo.strip(), gender)
        )
        conn.commit()

def save_match(game: str, is_official: bool, details: dict, elo_changes: dict):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO matches (game, is_official, details_json, elo_changes_json) VALUES (?, ?, ?, ?)",
            (game, 1 if is_official else 0, json.dumps(details), json.dumps(elo_changes)))
        conn.commit()

def get_match_history() -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM matches ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["details"] = json.loads(d["details_json"])
            d["elo_changes"] = json.loads(d["elo_changes_json"])
            result.append(d)
        return result

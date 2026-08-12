# database.py
# Gestion de la persistance SQLite (Joueurs, Équipes perso, Historique)

import sqlite3
import json
from typing import List, Dict, Any, Tuple
from config import DEFAULT_ROOMMATES, FC26_DEFAULT_TEAMS

DB_FILE = "app_data.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Table Joueurs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                is_guest INTEGER NOT NULL DEFAULT 0,
                elo REAL NOT NULL DEFAULT 1000.0
            )
        """)
        
        # Table Équipes Personnalisées FC26
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS custom_teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                stars REAL NOT NULL
            )
        """)
        
        # Table Matchs
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
        
        # Initialisation des 3 colocataires si non existants
        for roomie in DEFAULT_ROOMMATES:
            cursor.execute("INSERT OR IGNORE INTO players (name, is_guest, elo) VALUES (?, 0, 1000.0)", (roomie,))
            
        conn.commit()

def get_all_players() -> List[Dict[str, Any]]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players ORDER BY elo DESC")
        return [dict(row) for row in cursor.fetchall()]

def add_guest_player(name: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO players (name, is_guest, elo) VALUES (?, 1, 1000.0)", (name.strip(),))
        conn.commit()

def update_player_elo(name: str, delta: float):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE players SET elo = elo + ? WHERE name = ?", (delta, name))
        conn.commit()

def get_fc26_teams() -> Dict[str, float]:
    teams = FC26_DEFAULT_TEAMS.copy()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, stars FROM custom_teams")
        for row in cursor.fetchall():
            teams[row["name"]] = row["stars"]
    return teams

def add_custom_team(name: str, stars: float):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO custom_teams (name, stars) VALUES (?, ?)", (name.strip(), stars))
        conn.commit()

def save_match(game: str, is_official: bool, details: dict, elo_changes: dict):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO matches (game, is_official, details_json, elo_changes_json) VALUES (?, ?, ?, ?)",
            (game, 1 if is_official else 0, json.dumps(details), json.dumps(elo_changes))
        )
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

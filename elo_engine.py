# elo_engine.py
# Moteur de calcul ELO modulaire pour MK8, FC26 et futurs jeux

from typing import List, Dict, Tuple
from config import DEFAULT_ROOMMATES, MK8_TRACKS

K_FACTOR = 32.0

def check_is_official(participating_players: List[str]) -> bool:
    """Vérifie si au moins 2 colocataires participent au match."""
    roommate_count = sum(1 for p in participating_players if p in DEFAULT_ROOMMATES)
    return roommate_count >= 2

def calculate_fc26_elo(
    team1_players: List[str],
    team2_players: List[str],
    team1_stars: float,
    team2_stars: float,
    score1: int,
    score2: int,
    players_elo: Dict[str, float]
) -> Tuple[Dict[str, float], bool]:
    
    all_players = team1_players + team2_players
    is_official = check_is_official(all_players)
    elo_changes = {p: 0.0 for p in all_players}
    
    if not is_official:
        return elo_changes, False

    # Moyenne ELO des équipes
    avg_elo_t1 = sum(players_elo[p] for p in team1_players) / len(team1_players)
    avg_elo_t2 = sum(players_elo[p] for p in team2_players) / len(team2_players)

    # Ajustement selon les étoiles
    adj_elo_t1 = avg_elo_t1 + (team2_stars - team1_stars) * 40.0
    adj_elo_t2 = avg_elo_t2 + (team1_stars - team2_stars) * 40.0

    # Espérances
    expected1 = 1.0 / (1.0 + 10.0 ** ((adj_elo_t2 - adj_elo_t1) / 400.0))
    expected2 = 1.0 - expected1

    # Ratios de score (Victoire = 1, Nul = 0.5, Défaite = 0)
    if score1 > score2:
        actual1, actual2 = 1.0, 0.0
    elif score2 > score1:
        actual1, actual2 = 0.0, 1.0
    else:
        actual1, actual2 = 0.5, 0.5

    delta1 = K_FACTOR * (actual1 - expected1)
    delta2 = K_FACTOR * (actual2 - expected2)

    for p in team1_players:
        elo_changes[p] = round(delta1, 2)
    for p in team2_players:
        elo_changes[p] = round(delta2, 2)

    return elo_changes, True


def calculate_mk8_elo(
    rankings: List[str],  # Liste ordonnée des joueurs (du 1er au dernier)
    selected_tracks: List[str],
    players_elo: Dict[str, float]
) -> Tuple[Dict[str, float], bool]:
    
    is_official = check_is_official(rankings)
    elo_changes = {p: 0.0 for p in rankings}
    
    if not is_official:
        return elo_changes, False

    # Difficulté moyenne des circuits joués
    diff_sum = sum(MK8_TRACKS[t]["difficulty"] for t in selected_tracks if t in MK8_TRACKS)
    avg_diff = diff_sum / max(len(selected_tracks), 1)
    
    # Facteur K effectif ajusté
    k_eff = K_FACTOR * (0.8 + 0.2 * avg_diff)
    n = len(rankings)

    # Pairwise comparison entre chaque joueur
    for i in range(n):
        p_i = rankings[i]
        r_i = players_elo[p_i]
        
        for j in range(n):
            if i == j:
                continue
            p_j = rankings[j]
            r_j = players_elo[p_j]

            expected_i = 1.0 / (1.0 + 10.0 ** ((r_j - r_i) / 400.0))
            actual_i = 1.0 if i < j else (0.5 if i == j else 0.0)

            elo_changes[p_i] += (k_eff / (n - 1)) * (actual_i - expected_i)

    for p in elo_changes:
        elo_changes[p] = round(elo_changes[p], 2)

    return elo_changes, True

# elo_engine.py

from typing import List, Dict, Tuple
from config import DEFAULT_ROOMMATES, MK8_TRACKS
import database as db

K_FACTOR = 32.0

def get_current_roommates():
    players = db.get_all_players()
    return [p["name"] for p in players if not p["is_guest"]]

def check_is_official(participating_players: List[str]) -> bool:
    roommates = get_current_roommates()
    roommate_count = sum(1 for p in participating_players if p in roommates)
    return roommate_count >= 2

def calculate_fc26_elo(
    team1_players: List[str], team2_players: List[str], team1_stars: float,
    team2_stars: float, score1: int, score2: int, players_elo: Dict[str, float]
) -> Tuple[Dict[str, float], bool]:
    
    all_players = team1_players + team2_players
    is_official = check_is_official(all_players)
    elo_changes = {p: 0.0 for p in all_players}
    
    if not is_official: return elo_changes, False

    avg_elo_t1 = sum(players_elo[p] for p in team1_players) / len(team1_players)
    avg_elo_t2 = sum(players_elo[p] for p in team2_players) / len(team2_players)

    adj_elo_t1 = avg_elo_t1 + (team2_stars - team1_stars) * 40.0
    adj_elo_t2 = avg_elo_t2 + (team1_stars - team2_stars) * 40.0

    expected1 = 1.0 / (1.0 + 10.0 ** ((adj_elo_t2 - adj_elo_t1) / 400.0))
    expected2 = 1.0 - expected1

    if score1 > score2: actual1, actual2 = 1.0, 0.0
    elif score2 > score1: actual1, actual2 = 0.0, 1.0
    else: actual1, actual2 = 0.5, 0.5

    delta1 = K_FACTOR * (actual1 - expected1)
    delta2 = K_FACTOR * (actual2 - expected2)

    for p in team1_players: elo_changes[p] = round(delta1, 2)
    for p in team2_players: elo_changes[p] = round(delta2, 2)

    return elo_changes, True


def calculate_mk8_elo(
    rankings_with_pos: List[Tuple[str, int]], 
    selected_tracks: List[str],
    players_elo: Dict[str, float]
) -> Tuple[Dict[str, float], bool]:
    
    players = [p[0] for p in rankings_with_pos]
    is_official = check_is_official(players)
    elo_changes = {p: 0.0 for p in players}
    
    if not is_official: return elo_changes, False

    diff_sum = sum(MK8_TRACKS[t]["difficulty"] for t in selected_tracks if t in MK8_TRACKS)
    avg_diff = diff_sum / max(len(selected_tracks), 1)
    k_eff = K_FACTOR * (0.8 + 0.2 * avg_diff)
    n = len(rankings_with_pos)

    # 1. Comparaison entre joueurs humains (Relatif)
    for i in range(n):
        p_i, pos_i = rankings_with_pos[i]
        r_i = players_elo[p_i]
        
        for j in range(n):
            if i == j: continue
            p_j, pos_j = rankings_with_pos[j]
            r_j = players_elo[p_j]

            expected_i = 1.0 / (1.0 + 10.0 ** ((r_j - r_i) / 400.0))
            actual_i = 1.0 if pos_i < pos_j else (0.5 if pos_i == pos_j else 0.0)
            elo_changes[p_i] += (k_eff / (n - 1)) * (actual_i - expected_i)

    # 2. Modificateur absolu face aux Bots (1 à 12)
    for p, pos in rankings_with_pos:
        # 6.5 est la position moyenne (entre 1 et 12). 
        # Bonus si < 6.5, Malus si > 6.5. Multiplié par la difficulté.
        absolute_bonus = (6.5 - pos) * 2.5 * avg_diff
        elo_changes[p] += absolute_bonus

    for p in elo_changes:
        elo_changes[p] = round(elo_changes[p], 2)

    return elo_changes, True

# app.py
# Interface principale Streamlit - Dashboard, Modules de Jeux, Statistiques

import streamlit as st
import pandas as pd
import database as db
import elo_engine as elo
from config import APP_PASSWORD, DEFAULT_ROOMMATES, MK8_TRACKS, MK8_CHARACTERS

# Configuration de la page
st.set_page_config(page_title="Coloc Game Tracker", page_icon="🎮", layout="wide")

# Initialisation DB
db.init_db()

# --- AUTHENTIFICATION ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 Accès Réservé - Coloc Game Tracker")
    pwd = st.text_input("Saisir le mot de passe commun :", type="password")
    if st.button("Se connecter"):
        if pwd == APP_PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Mot de passe incorrect !")
    st.stop()

# --- NAVBAR / NAVIGATION ---
st.sidebar.title("🎮 Naviguer")
menu = st.sidebar.radio(
    "Menu",
    ["📊 Classement & Stats", "🏎️ Mario Kart 8", "⚽ FC 26", "👥 Joueurs & Équipes", "📜 Historique"]
)

players_data = db.get_all_players()
players_dict = {p["name"]: p["elo"] for p in players_data}

# -----------------------------------------------------------------------------
# 1. CLASSEMENT & STATISTIQUES
# -----------------------------------------------------------------------------
if menu == "📊 Classement & Stats":
    st.title("📊 Tableau de Bord & Classements ELO")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Classement Officiel (Colocataires)")
        coloc_df = pd.DataFrame([p for p in players_data if not p["is_guest"]])
        if not coloc_df.empty:
            coloc_df = coloc_df[["name", "elo"]].reset_index(drop=True)
            coloc_df.columns = ["Colocataire", "Score ELO"]
            st.dataframe(coloc_df, use_container_width=True)

    with col2:
        st.subheader("🌟 Classement Général (Inclus Invités)")
        all_df = pd.DataFrame(players_data)
        if not all_df.empty:
            all_df["Statut"] = all_df["is_guest"].apply(lambda x: "Invité" if x else "Coloc")
            all_df = all_df[["name", "Statut", "elo"]].reset_index(drop=True)
            all_df.columns = ["Joueur", "Statut", "Score ELO"]
            st.dataframe(all_df, use_container_width=True)

    st.markdown("---")
    st.subheader("📈 Statistiques par Jeu")
    history = db.get_match_history()
    
    if history:
        df_hist = pd.DataFrame(history)
        mk8_count = len(df_hist[df_hist["game"] == "Mario Kart 8"])
        fc_count = len(df_hist[df_hist["game"] == "FC26"])
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total des Matchs", len(history))
        m2.metric("Parties de MK8", mk8_count)
        m3.metric("Matchs de FC26", fc_count)
    else:
        st.info("Aucun match enregistré pour le moment.")

# -----------------------------------------------------------------------------
# 2. MODULE MARIO KART 8
# -----------------------------------------------------------------------------
elif menu == "🏎️ Mario Kart 8":
    st.title("🏎️ Session Mario Kart 8 Deluxe")
    
    available_players = list(players_dict.keys())
    selected_players = st.multiselect("Sélectionner les joueurs (2 à 4) :", available_players, max_selections=4)
    
    if len(selected_players) >= 2:
        st.subheader("1. Paramètres de la session")
        session_type = st.radio("Format :", ["Course unique", "Grand Prix"])
        
        all_tracks = list(MK8_TRACKS.keys())
        tracks_played = st.multiselect("Circuits joués :", all_tracks)
        
        st.subheader("2. Choix des personnages")
        chars = {}
        cols = st.columns(len(selected_players))
        for idx, p in enumerate(selected_players):
            with cols[idx]:
                chars[p] = st.selectbox(f"Perso de {p}", MK8_CHARACTERS, key=f"char_{p}")
                
        st.subheader("3. Classement Final de la Session")
        st.caption("Faites glisser ou numérotez les joueurs du 1er au dernier")
        
        rankings = []
        cols_rank = st.columns(len(selected_players))
        for idx, p in enumerate(selected_players):
            with cols_rank[idx]:
                rank = st.number_input(f"Position de {p}", min_value=1, max_value=len(selected_players), value=idx+1)
                rankings.append((p, rank))
                
        # Trier les joueurs selon la position saisie
        rankings.sort(key=lambda x: x[1])
        ordered_players = [p[0] for p in rankings]

        if st.button("💾 Enregistrer la session MK8"):
            if not tracks_played:
                st.error("Veuillez sélectionner au moins un circuit.")
            else:
                elo_changes, is_official = elo.calculate_mk8_elo(ordered_players, tracks_played, players_dict)
                
                # Appliquer changements ELO
                for p, delta in elo_changes.items():
                    db.update_player_elo(p, delta)
                    
                details = {
                    "session_type": session_type,
                    "tracks": tracks_played,
                    "characters": chars,
                    "rankings": ordered_players
                }
                
                db.save_match("Mario Kart 8", is_official, details, elo_changes)
                
                if is_official:
                    st.success("Session enregistrée ! L'ELO des colocataires a été mis à jour.")
                else:
                    st.warning("Session enregistrée en mode Amical (moins de 2 colocataires) : aucun impact sur l'ELO Officiel.")
                st.rerun()

# -----------------------------------------------------------------------------
# 3. MODULE FC 26
# -----------------------------------------------------------------------------
elif menu == "⚽ FC 26":
    st.title("⚽ Match FC 26")
    
    all_teams = db.get_fc26_teams()
    available_players = list(players_dict.keys())
    
    st.subheader("1. Composition des équipes")
    format_match = st.selectbox("Format :", ["1v1", "2v1", "2v2"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Équipe 1")
        if format_match == "1v1":
            t1_p = [st.selectbox("Joueur Équipe 1", available_players, key="t1p1")]
        elif format_match == "2v1":
            t1_p = st.multiselect("Joueurs Équipe 1 (2 joueurs)", available_players, max_selections=2, key="t1p2")
        else:
            t1_p = st.multiselect("Joueurs Équipe 1 (2 joueurs)", available_players, max_selections=2, key="t1p22")
            
        t1_team = st.selectbox("Équipe FC26 (1) :", list(all_teams.keys()), key="t1_team")
        score1 = st.number_input("Score Équipe 1 :", min_value=0, value=0)

    with col2:
        st.markdown("### Équipe 2")
        p2_avail = [p for p in available_players if p not in t1_p]
        
        if format_match in ["1v1", "2v1"]:
            t2_p = [st.selectbox("Joueur Équipe 2", p2_avail, key="t2p1")]
        else:
            t2_p = st.multiselect("Joueurs Équipe 2 (2 joueurs)", p2_avail, max_selections=2, key="t2p2")
            
        t2_team = st.selectbox("Équipe FC26 (2) :", list(all_teams.keys()), key="t2_team")
        score2 = st.number_input("Score Équipe 2 :", min_value=0, value=0)

    if st.button("💾 Enregistrer le match FC26"):
        if not t1_p or not t2_p:
            st.error("Veuillez sélectionner correctement les joueurs pour chaque équipe.")
        else:
            elo_changes, is_official = elo.calculate_fc26_elo(
                t1_p, t2_p, all_teams[t1_team], all_teams[t2_team], score1, score2, players_dict
            )
            
            for p, delta in elo_changes.items():
                db.update_player_elo(p, delta)
                
            details = {
                "team1_players": t1_p,
                "team2_players": t2_p,
                "team1_name": t1_team,
                "team2_name": t2_team,
                "score1": score1,
                "score2": score2
            }
            
            db.save_match("FC26", is_official, details, elo_changes)
            
            if is_official:
                st.success("Match enregistré avec mise à jour ELO !")
            else:
                st.warning("Match enregistré (non officiel : moins de 2 colocataires).")
            st.rerun()

# -----------------------------------------------------------------------------
# 4. GESTION DES JOUEURS ET ÉQUIPES
# -----------------------------------------------------------------------------
elif menu == "👥 Joueurs & Équipes":
    st.title("👥 Gestion des Invités et Équipes Personnalisées")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("➕ Ajouter un Invité")
        guest_name = st.text_input("Prénom de l'invité :")
        if st.button("Ajouter l'invité"):
            if guest_name:
                db.add_guest_player(guest_name)
                st.success(f"Invité {guest_name} ajouté !")
                st.rerun()

    with col2:
        st.subheader("⚽ Ajouter une Équipe Personnalisée FC26")
        custom_team_name = st.text_input("Nom de l'équipe :")
        stars = st.slider("Étoiles (1.0 à 5.0) :", min_value=1.0, max_value=5.0, step=0.5, value=4.0)
        if st.button("Sauvegarder l'équipe"):
            if custom_team_name:
                db.add_custom_team(custom_team_name, stars)
                st.success(f"Équipe {custom_team_name} ({stars}⭐) sauvegardée !")
                st.rerun()

# -----------------------------------------------------------------------------
# 5. HISTORIQUE DES MATCHS
# -----------------------------------------------------------------------------
elif menu == "📜 Historique":
    st.title("📜 Historique des Matchs")
    
    history = db.get_match_history()
    for m in history:
        status = "🟢 Officiel" if m["is_official"] else "⚪ Amical"
        with st.expander(f"{m['timestamp']} - {m['game']} ({status})"):
            st.json(m["details"])
            st.write("**Variations ELO :**", m["elo_changes"])
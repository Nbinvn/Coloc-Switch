# app.py

import streamlit as st
import pandas as pd
import base64
import database as db
import elo_engine as elo
from config import APP_PASSWORD, MK8_TRACKS, MK8_CHARACTERS

st.set_page_config(page_title="Coloc Game Tracker", page_icon="🎮", layout="wide")
db.init_db()

# --- AUTHENTIFICATION ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 Accès Réservé - Coloc Game Tracker")
    pwd = st.text_input("Saisir le mot de passe :", type="password")
    if st.button("Se connecter"):
        if pwd == APP_PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Mot de passe incorrect !")
    st.stop()

# --- REQUÊTES GLOBALES ---
players_data = db.get_all_players()
players_dict = {p["name"]: p["elo"] for p in players_data}
available_players = list(players_dict.keys())

# --- NAVBAR ---
st.sidebar.title("🎮 Menu")
menu = st.sidebar.radio("Navigation", ["📊 Classement", "🏎️ Mario Kart 8", "⚽ FC 26", "⚙️ Gestion Profils", "📜 Historique"])

# -----------------------------------------------------------------------------
# 1. CLASSEMENT & STATS
# -----------------------------------------------------------------------------
if menu == "📊 Classement":
    st.title("📊 Tableau de Bord")
    
    df = pd.DataFrame(players_data)
    if not df.empty:
        df["Avatar"] = df["avatar"]
        coloc_df = df[df["is_guest"] == 0][["Avatar", "name", "elo"]].reset_index(drop=True)
        guest_df = df[df["is_guest"] == 1][["Avatar", "name", "elo"]].reset_index(drop=True)
        
        st.subheader("🏆 Classement Officiel (Colocataires)")
        st.dataframe(
            coloc_df,
            column_config={
                "Avatar": st.column_config.ImageColumn("Avatar", help="Photo"),
                "name": "Joueur", "elo": "Score ELO"
            },
            use_container_width=True
        )
        
        st.subheader("🌟 Classement Invités")
        st.dataframe(
            guest_df,
            column_config={
                "Avatar": st.column_config.ImageColumn("Avatar", help="Photo"),
                "name": "Invité", "elo": "Score ELO"
            },
            use_container_width=True
        )

# -----------------------------------------------------------------------------
# 2. MARIO KART 8
# -----------------------------------------------------------------------------
elif menu == "🏎️ Mario Kart 8":
    st.title("🏎️ Session Mario Kart 8 Deluxe")
    
    with st.expander("➕ Ajouter un invité rapidement"):
        guest_name = st.text_input("Prénom de l'invité (MK8) :")
        if st.button("Ajouter", key="add_guest_mk8"):
            db.add_guest_player(guest_name)
            st.success("Invité ajouté ! Recharge la page.")
            st.rerun()

    selected_players = st.multiselect("Sélectionner les joueurs présents :", available_players, max_selections=4)
    
    if len(selected_players) >= 2:
        st.subheader("1. Paramètres")
        
        def format_track(t):
            return f"{t} ({'🌶️' * MK8_TRACKS[t]['difficulty']})"
            
        tracks_played = st.multiselect("Circuits joués (Difficulté indiquée par 🌶️) :", list(MK8_TRACKS.keys()), format_func=format_track)
        
        if tracks_played:
            st.write("**Aperçu des circuits :**")
            cols = st.columns(len(tracks_played))
            for i, t in enumerate(tracks_played):
                with cols[i]:
                    st.image(MK8_TRACKS[t]["image"], width=120)
                    st.caption(t)

        st.subheader("2. Classement Absolu (contre les Bots)")
        st.caption("Indiquez la position exacte (1 à 12) de chaque joueur à l'issue de la course/du Grand Prix.")
        
        rankings_with_pos = []
        cols_rank = st.columns(len(selected_players))
        for idx, p in enumerate(selected_players):
            with cols_rank[idx]:
                pos = st.number_input(f"Place de {p}", min_value=1, max_value=12, value=idx+1)
                rankings_with_pos.append((p, pos))

        if st.button("💾 Enregistrer la session MK8"):
            if not tracks_played:
                st.error("Sélectionnez au moins un circuit.")
            else:
                elo_changes, is_off = elo.calculate_mk8_elo(rankings_with_pos, tracks_played, players_dict)
                for p, delta in elo_changes.items(): db.update_player_elo(p, delta)
                db.save_match("Mario Kart 8", is_off, {"tracks": tracks_played, "rankings": rankings_with_pos}, elo_changes)
                st.success("Session enregistrée !")
                st.rerun()

# -----------------------------------------------------------------------------
# 3. FC 26
# -----------------------------------------------------------------------------
elif menu == "⚽ FC 26":
    st.title("⚽ Match FC 26")
    
    col_exp1, col_exp2 = st.columns(2)
    with col_exp1:
        with st.expander("➕ Ajouter un invité"):
            guest_name = st.text_input("Prénom de l'invité (FC26) :")
            if st.button("Ajouter", key="add_guest_fc"):
                db.add_guest_player(guest_name)
                st.rerun()
    with col_exp2:
        with st.expander("⚙️ Créer une équipe personnalisée"):
            c_name = st.text_input("Nom de l'équipe :")
            c_stars = st.slider("Niveau :", 1.0, 5.0, 4.0, 0.5)
            if st.button("Sauvegarder l'équipe"):
                db.add_custom_team(c_name, c_stars)
                st.rerun()

    all_teams = db.get_fc26_teams()
    def format_team(t_name):
            stars = all_teams.get(t_name, 0)
            star_str = '⭐' * int(stars)
            if stars % 1 != 0: star_str += '✨' # ✨ = Demi-étoile
            return f"{t_name} ({star_str})"

    format_match = st.selectbox("Format :", ["1v1", "2v1", "2v2"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Équipe 1")
        t1_p = st.multiselect("Joueurs (Eq.1)", available_players, max_selections=2 if "2" in format_match else 1, key="t1p")
        t1_team = st.selectbox("Équipe (Eq.1) :", list(all_teams.keys()), format_func=format_team, key="t1_team")
        score1 = st.number_input("Score Eq.1 :", min_value=0, value=0)

    with col2:
        st.markdown("### Équipe 2")
        p2_avail = [p for p in available_players if p not in t1_p]
        t2_p = st.multiselect("Joueurs (Eq.2)", p2_avail, max_selections=2 if "2v2" == format_match else 1, key="t2p")
        t2_team = st.selectbox("Équipe (Eq.2) :", list(all_teams.keys()), format_func=format_team, key="t2_team")
        score2 = st.number_input("Score Eq.2 :", min_value=0, value=0)

    if st.button("💾 Enregistrer le match FC26"):
        if not t1_p or not t2_p: st.error("Sélectionnez les joueurs.")
        else:
            elo_changes, is_off = elo.calculate_fc26_elo(t1_p, t2_p, all_teams[t1_team], all_teams[t2_team], score1, score2, players_dict)
            for p, delta in elo_changes.items(): db.update_player_elo(p, delta)
            db.save_match("FC26", is_off, {"team1_players": t1_p, "team2_players": t2_p, "score1": score1, "score2": score2}, elo_changes)
            st.success("Match enregistré !")
            st.rerun()

# -----------------------------------------------------------------------------
# 4. GESTION DES PROFILS (Nom & Photo)
# -----------------------------------------------------------------------------
elif menu == "⚙️ Gestion Profils":
    st.title("⚙️ Modifier les Profils")
    
    selected_player = st.selectbox("Choisir le joueur à modifier :", available_players)
    player_info = next(p for p in players_data if p["name"] == selected_player)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(player_info.get("avatar") or "https://cdn-icons-png.flaticon.com/512/149/149071.png", width=150)
    
    with col2:
        new_name = st.text_input("Modifier le nom :", value=player_info["name"])
        avatar_file = st.file_uploader("Nouvelle photo (PNG/JPG) :", type=["png", "jpg", "jpeg"])
        
        if st.button("💾 Enregistrer les modifications"):
            final_avatar = player_info.get("avatar")
            if avatar_file:
                # Encode l'image en texte Base64 pour l'enregistrer dans SQLite facilement
                final_avatar = "data:image/png;base64," + base64.b64encode(avatar_file.read()).decode()
            
            db.update_player_profile(player_info["name"], new_name, final_avatar)
            st.success(f"Profil de {new_name} mis à jour avec succès !")
            st.rerun()

# -----------------------------------------------------------------------------
# 5. HISTORIQUE
# -----------------------------------------------------------------------------
elif menu == "📜 Historique":
    st.title("📜 Historique des Matchs")
    for m in db.get_match_history():
        with st.expander(f"{m['timestamp']} - {m['game']} ({'🟢 Officiel' if m['is_official'] else '⚪ Amical'})"):
            st.json(m["details"])
            st.write("**Variations ELO :**", m["elo_changes"])

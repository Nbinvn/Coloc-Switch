# app.py

import streamlit as st
import pandas as pd
import base64
import database as db
import elo_engine as elo
from config import APP_PASSWORD, MK8_TRACKS, MK8_CHARACTERS
from placeholders import avatar_circle, logo_shield, track_banner, DEFAULT_PLAYER_AVATAR

st.set_page_config(page_title="Coloc Game Tracker", page_icon="🎮", layout="wide")
db.init_db()

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

players_data = db.get_all_players()
players_dict = {p["name"]: p["elo"] for p in players_data}
available_players = sorted(players_dict.keys())  # Ordre alphabétique

st.sidebar.title("🎮 Menu")
menu = st.sidebar.radio("Navigation", ["📊 Classement", "🏎️ Mario Kart 8", "⚽ FC 26", "⚙️ Gestion Profils", "📜 Historique"])

# --- FONCTIONS VISUELLES ---
# Toutes les images sont générées localement (data URI) : elles ne dépendent
# d'aucun serveur externe et ne peuvent donc jamais s'afficher "cassées",
# contrairement aux liens hotlinkés (wikis, flaticon...) qui peuvent bloquer
# le hotlinking à tout moment sans prévenir.

def display_mk8_track(track_name):
    t = MK8_TRACKS[track_name]
    img = track_banner(track_name, t["difficulty"])
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap:15px; background-color:#1e1e2e; padding:10px; border-radius:10px; margin-bottom:10px;">
            <img src="{img}" width="80" style="border-radius:5px;">
            <div>
                <strong style="font-size:1.1em;">{track_name}</strong><br>
                <span>Difficulté : {'🌶️' * t['difficulty']}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def display_mk8_character(char_name, player_name):
    img = avatar_circle(char_name)
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap:10px; padding:5px;">
            <img src="{img}" width="40" style="border-radius:50px;">
            <span><b>{player_name}</b> joue <i>{char_name}</i></span>
        </div>
    """, unsafe_allow_html=True)

def display_fc_team(league_name, team_name, all_teams_dict):
    data = all_teams_dict.get(league_name, {}).get(team_name, {"stars": 1.0, "logo": ""})
    stars = data["stars"]
    star_str = '⭐' * int(stars) + ('✨' if stars % 1 != 0 else '')
    real_logo = data.get("logo") or ""
    fallback = logo_shield(team_name)
    src = real_logo if real_logo else fallback
    onerror = f"this.onerror=null;this.src='{fallback}';" if real_logo else ""
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap:15px; background-color:#173620; padding:10px; border-radius:10px; margin-bottom:15px; border: 1px solid #2d663b;">
            <img src="{src}" width="50" onerror="{onerror}">
            <div>
                <strong style="font-size:1.2em;">{team_name}</strong><br>
                <span>Niveau : {star_str} ({stars})</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. CLASSEMENT
# -----------------------------------------------------------------------------
if menu == "📊 Classement":
    st.title("📊 Tableau de Bord")
    
    df = pd.DataFrame(players_data)
    if not df.empty:
        if "avatar" not in df.columns:
            df["avatar"] = DEFAULT_PLAYER_AVATAR
        else:
            df["avatar"] = df["avatar"].fillna(DEFAULT_PLAYER_AVATAR)
            df.loc[df["avatar"] == "", "avatar"] = DEFAULT_PLAYER_AVATAR
        
        coloc_df = df[df["is_guest"] == 0][["avatar", "name", "elo"]].sort_values("elo", ascending=False).reset_index(drop=True)
        guest_df = df[df["is_guest"] == 1][["avatar", "name", "elo"]].sort_values("elo", ascending=False).reset_index(drop=True)
        
        st.subheader("🏆 Classement Officiel (Colocataires)")
        st.dataframe(
            coloc_df,
            column_config={
                "avatar": st.column_config.ImageColumn("Avatar", help="Photo"),
                "name": "Joueur", 
                "elo": "Score ELO"
            },
            width="stretch"
        )
        
        st.subheader("🌟 Classement Invités")
        st.dataframe(
            guest_df,
            column_config={
                "avatar": st.column_config.ImageColumn("Avatar", help="Photo"),
                "name": "Invité", 
                "elo": "Score ELO"
            },
            width="stretch"
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
        st.subheader("1. Paramètres & Personnages")
        
        chars = {}
        cols_char = st.columns(len(selected_players))
        for idx, p in enumerate(selected_players):
            with cols_char[idx]:
                chars[p] = st.selectbox(f"Personnage pour {p}", sorted(MK8_CHARACTERS.keys()), key=f"char_{p}")
                display_mk8_character(chars[p], p)
                
        st.markdown("---")
        tracks_played = st.multiselect("Circuits joués :", sorted(MK8_TRACKS.keys()))
        
        if tracks_played:
            st.write("**Aperçu des circuits sélectionnés :**")
            cols_tracks = st.columns(min(len(tracks_played), 4))
            for i, t in enumerate(tracks_played):
                with cols_tracks[i % 4]:
                    display_mk8_track(t)

        st.subheader("2. Classement Absolu (contre les Bots)")
        rankings_with_pos = []
        cols_rank = st.columns(len(selected_players))
        for idx, p in enumerate(selected_players):
            with cols_rank[idx]:
                pos = st.number_input(f"Place de {p}", min_value=1, max_value=12, value=idx+1, key=f"pos_{p}")
                rankings_with_pos.append((p, pos))

        # Deux joueurs ne peuvent pas finir à la même place
        positions_used = [pos for _, pos in rankings_with_pos]
        has_duplicate_positions = len(positions_used) != len(set(positions_used))
        if has_duplicate_positions:
            st.error("🚫 Deux joueurs ne peuvent pas terminer à la même place ! Merci d'attribuer une place unique à chaque joueur.")

        if st.button("💾 Enregistrer la session MK8", disabled=has_duplicate_positions):
            if not tracks_played:
                st.error("Sélectionnez au moins un circuit.")
            else:
                elo_changes, is_off = elo.calculate_mk8_elo(rankings_with_pos, tracks_played, players_dict)
                for p, delta in elo_changes.items(): db.update_player_elo(p, delta)
                db.save_match("Mario Kart 8", is_off, {"tracks": tracks_played, "characters": chars, "rankings": rankings_with_pos}, elo_changes)
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
            c_gender = st.selectbox("Genre :", sorted(["Masculin", "Féminin"]), key="c_gender")
            c_logo = st.text_input("URL du logo (optionnel, sinon un écusson est généré automatiquement) :")
            if st.button("Sauvegarder l'équipe"):
                if c_name.strip():
                    db.add_custom_team(c_name, c_stars, c_logo, c_gender)
                    st.success("Équipe personnalisée créée !")
                    st.rerun()
                else:
                    st.error("Merci de donner un nom à l'équipe.")

    # Genre de la confrontation : détermine quelles ligues sont proposées
    match_gender = st.selectbox("👤 Confrontation :", sorted(["Masculin", "Féminin"]), key="match_gender")
    all_teams = db.get_fc26_teams(match_gender)
    leagues_sorted = sorted(all_teams.keys())
    format_match = st.selectbox("Format :", sorted(["1v1", "2v1", "2v2"]))
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Équipe Domicile")
        t1_p = st.multiselect("Joueurs (Dom)", available_players, max_selections=2 if "2" in format_match else 1, key="t1p")
        t1_league = st.selectbox("Ligue (Dom) :", leagues_sorted, key="t1_league")
        t1_team = st.selectbox("Équipe (Dom) :", sorted(all_teams[t1_league].keys()), key="t1_team")
        display_fc_team(t1_league, t1_team, all_teams)
        score1 = st.number_input("Score Dom :", min_value=0, value=0)

    with col2:
        st.markdown("### Équipe Extérieur")
        p2_avail = [p for p in available_players if p not in t1_p]
        t2_p = st.multiselect("Joueurs (Ext)", p2_avail, max_selections=2 if "2v2" == format_match else 1, key="t2p")
        t2_league = st.selectbox("Ligue (Ext) :", leagues_sorted, key="t2_league")
        t2_team = st.selectbox("Équipe (Ext) :", sorted(all_teams[t2_league].keys()), key="t2_team")
        display_fc_team(t2_league, t2_team, all_teams)
        score2 = st.number_input("Score Ext :", min_value=0, value=0)

    if st.button("💾 Enregistrer le match FC26"):
        if not t1_p or not t2_p: st.error("Sélectionnez les joueurs.")
        else:
            t1_data, t2_data = all_teams[t1_league][t1_team], all_teams[t2_league][t2_team]
            elo_changes, is_off = elo.calculate_fc26_elo(t1_p, t2_p, t1_data["stars"], t2_data["stars"], score1, score2, players_dict)
            for p, delta in elo_changes.items(): db.update_player_elo(p, delta)
            db.save_match("FC26", is_off, {
                "gender": match_gender,
                "team1_players": t1_p, "team2_players": t2_p,
                "team1": f"{t1_league} - {t1_team}", "team2": f"{t2_league} - {t2_team}",
                "score1": score1, "score2": score2
            }, elo_changes)
            st.success("Match enregistré !")
            st.rerun()

# -----------------------------------------------------------------------------
# 4. GESTION DES PROFILS & 5. HISTORIQUE
# -----------------------------------------------------------------------------
elif menu == "⚙️ Gestion Profils":
    st.title("⚙️ Modifier les Profils")
    selected_player = st.selectbox("Choisir le joueur :", available_players)
    player_info = next(p for p in players_data if p["name"] == selected_player)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(player_info.get("avatar") or DEFAULT_PLAYER_AVATAR, width=150)
    with col2:
        new_name = st.text_input("Modifier le nom :", value=player_info["name"])
        avatar_file = st.file_uploader("Nouvelle photo (PNG/JPG) :", type=["png", "jpg", "jpeg"])
        if st.button("💾 Enregistrer"):
            final_avatar = player_info.get("avatar")
            if avatar_file:
                final_avatar = "data:image/png;base64," + base64.b64encode(avatar_file.read()).decode()
            db.update_player_profile(player_info["name"], new_name, final_avatar)
            st.success(f"Profil mis à jour !")
            st.rerun()

elif menu == "📜 Historique":
    st.title("📜 Historique des Matchs")
    for m in db.get_match_history():
        with st.expander(f"{m['timestamp']} - {m['game']} ({'🟢 Officiel' if m['is_official'] else '⚪ Amical'})"):
            st.json(m["details"])
            st.write("**Variations ELO :**", m["elo_changes"])

import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Pour ma chérie ❤️", page_icon="🌹")

# Initialiser l'état de l'application
if 'empezar' not in st.session_state:
    st.session_state.empezar = False
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0

# Style personnalisé
st.markdown("""
    <style>
    .main { background-color: #fff0f3; }
    .titulo-gigante {
        color: #800f2f;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-size: 50px;
        font-weight: bold;
        margin-top: 20%;
    }
    div.stButton > button:first-child {
        background-color: #ff4d6d;
        color: white;
        border-radius: 20px;
        border: none;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# PANTALLA 1: Bienvenida
if not st.session_state.empezar:
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Clique ici mon amour ✨"):
            st.session_state.empezar = True
            st.rerun()

# PANTALLA 2: La pregunta (Solo sale después de hacer clic)
else:
    st.title("Veux-tu être ma Valentine ? 🌹")

    # Tu GIF
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZqZzRyeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/c76IJLufpNwSULPk77/giphy.gif")

    # Calcul de la taille du bouton OUI
    taille_oui = 18 + (st.session_state.intentos * 20)

    col1, col2 = st.columns([1, 1])

    with col1:
        estilo_oui = f"""
            <style>
            button[kind="primary"] {{
                font-size: {taille_oui}px !important;
                padding: {10 + st.session_state.intentos*5}px !important;
                width: 100%;
            }}
            </style>
        """
        st.markdown(estilo_oui, unsafe_allow_html=True)
        if st.button("OUI ! ❤️", type="primary"):
            st.balloons()
            st.success("Dimanche a 20h soit prete")
            st.write("### Prépare-toi pour une journée inoubliable... 🥰")

    with col2:
        if st.button("Non 😢"):
            st.session_state.intentos += 1
            st.rerun()

    # Messages de persuasion
    messages = [
        "Tu es sûre ? 🤔",
        "Réfléchis encore... 🥺",
        "Le bouton OUI est plus joli, non ? ✨",
        "Tu vas vraiment me dire non ? 💔",
        "Je vais pleurer... 😭",
        "Regarde comme le bouton OUI est grand maintenant ! 😉"
    ]

    if st.session_state.intentos > 0:
        msg_index = min(st.session_state.intentos - 1, len(messages) - 1)
        st.info(messages[msg_index])

import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Pour ma femme boostee, l'amour de ma vie ❤️", page_icon="🌹")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4d6d;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        color: white;
    }
    h1 {
        color: #800f2f;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("J'ai une question tres importante pour toi... 🌹")

# Imagen o GIF romántico
st.image("https://i.pinimg.com/originals/f1/09/3d/f1093dd6dce5892d2b74c6e8d8c1c909.gif")

st.write("### Voudrais-tu être mon Saint Valentin?")

col1, col2 = st.columns(2)

with col1:
    if st.button("OUI❤️"):
        st.balloons()
        st.success("¡ME HACES EL MÁS FELIZ DEL MUNDO! 💍✨")
        st.write("Prometo que será un día increíble. ¡Te amo!")

with col2:
    # Un poco de humor: el botón de "No" que es difícil de clickear (opcional)
    no_button = st.button("Non 😢")
    if no_button:
        st.warning("Option pas disponible. Essaye encore une fois 😉")

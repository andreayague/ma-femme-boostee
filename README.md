# ma-femme-boostee
mi amor
import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Para mi niña ❤️", page_icon="🌹")

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

st.title("Tengo una pregunta muy importante... 🌹")

# Imagen o GIF romántico
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZqZzRyeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/c76IJLufpNwSULPk77/giphy.gif")

st.write("### Llevo tiempo pensando en esto y quería decírtelo de una forma especial:")

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ! ❤️"):
        st.balloons()
        st.success("¡ME HACES EL MÁS FELIZ DEL MUNDO! 💍✨")
        st.write("Prometo que será un día increíble. ¡Te amo!")

with col2:
    # Un poco de humor: el botón de "No" que es difícil de clickear (opcional)
    no_button = st.button("No 😢")
    if no_button:
        st.warning("Esa opción no está disponible en este momento. Intenta de nuevo. 😉")

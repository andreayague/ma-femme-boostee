import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial
st.set_page_config(page_title="Pour ma chérie ❤️", page_icon="🌹")

# Inicializar estados de memoria
if 'empezar' not in st.session_state:
    st.session_state.empezar = False
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0
if 'mostrar_final' not in st.session_state:
    st.session_state.mostrar_final = False

# Estilo visual
st.markdown("""
    <style>
    .main { background-color: #fff0f3; }
    .titulo-gigante {
        color: #800f2f;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-size: 45px;
        font-weight: bold;
        padding-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIÓN DE AUDIO ---
def reproducir_musica():
    try:
        with open("These_Eyes_KLICKAUD.mp3", "rb") as f:
            data = f.read()
            st.audio(data, format="audio/mp3", autoplay=True, loop=True)
    except:
        pass

# PANTALLA 1: Bienvenida
if not st.session_state.empezar:
    reproducir_musica()
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Clique ici mon amour ✨", use_container_width=True):
        st.session_state.empezar = True
        st.rerun()

# PANTALLA FINAL
elif st.session_state.mostrar_final:
    st.balloons()
    st.title("OUI ! ❤️")
    
    try:
        st.image("IMG_1950.jpg", use_container_width=True)
    except:
        st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")
    
    st.success("Je t'aime !")
    st.markdown("""
    ### Je t'aime. 
    ### Sois prête le dimanche 15 janvier à 20h. 
    ### Habille-toi très jolie, même s'il me semble impossible que tu sois plus belle que tu ne l'es déjà. ❤️
    """)

# PANTALLA 2: La pregunta
else:
    reproducir_musica()
    st.title("Veux-tu être ma Valentine ? 🌹")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")

    if st.session_state.intentos < 3:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("OUI ! ❤️", type="primary", use_container_width=True):
                st.session_state.mostrar_final = True
                st

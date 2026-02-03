import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial
st.set_page_config(page_title="Pour ma femme ❤️", page_icon="🌹")

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
    div.stButton > button:first-child {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MÚSICA ---
try:
    with open("These_Eyes_KLICKAUD.mp3", "rb") as f:
        st.audio(f.read(), format="audio/mp3", autoplay=True, loop=True)
except:
    pass

# PANTALLA 1: BIENVENIDA
if not st.session_state.empezar:
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Clique ici mon amour ✨"):
        st.session_state.empezar = True
        st.rerun()

# PANTALLA FINAL (Cuando dice OUI)
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

# PANTALLA 2: LA PREGUNTA
else:
    st.title("Veux-tu être ma Valentine ? 🌹")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")

    # Tamaño del botón OUI
    tamano_si = 18 + (st.session_state.intentos * 12)
    st.markdown(f"<style>button[kind='primary'] {{ font-size: {tamano_si}px !important; }}</style>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("OUI ! ❤️", type="primary", key="principal_oui"):
            st.session_state.mostrar_final = True
            st.rerun()
            
    with col2:
        # Solo mostramos el botón "Non" real los primeros 3 intentos
        if st.session_state.intentos < 3:
            if st.button("Non 😢", key="boton_no_estatico"):
                st.session_state.intentos += 1
                st.rerun()
        else:
            st.write(" ") # Espacio vacío si ya está el modo "esquivar" activo

    # Mensajes y modo esquivar
    if st.session_state.intentos > 0:
        mensajes = [
            "Tu es sûre ? 🤔", 
            "Réfléchis encore... 🥺", 
            "Le botón OUI est plus joli, non ? ✨",
            "Attention... le bouton va commencer à bouger ! 🏃‍♂️"
        ]
        msg_idx = min(st.session_state.intentos - 1, len(mensajes) - 1)
        st.info(mensajes[msg_idx])

    # A partir del 4º intento, sale el botón que huye
    if st.session_state.intentos >= 3:
        valentine_js = """
        <div id="container" style="height: 150px; width: 100%; position: relative;">
            <button id="noBtn" onmouseover="moveButton()" style="
                background-color: #808080; color: white; border: none;
                padding: 10px 20px; font-size: 18px; border-radius: 15px;
                position: absolute; left: 40%; top: 20px; transition: 0.1s;
                cursor: pointer;
            ">Non 😢</button>
        </div>
        <script>
            function moveButton() {
                var btn = document.getElementById('noBtn');
                btn.style.left = Math.random() * 80 + '%';
                btn.style.top = Math.random() * 100 + 'px';
            }
        </script>
        """
        components.html(valentine_js, height=200)
        
        # Botón extra para forzar el crecimiento si ella es muy terca jaja
        if st.button("Toujours Non ? 🙄", key="retry"):
            st.session_state.intentos += 1
            st.rerun()

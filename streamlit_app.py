import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Pour ma chérie ❤️", page_icon="🌹")

# Inicializar estados
if 'empezar' not in st.session_state:
    st.session_state.empezar = False
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0
if 'mostrar_final' not in st.session_state:
    st.session_state.mostrar_final = False

# Estilo y Música (Autoplay)
st.markdown("""
    <style>
    .main { background-color: #fff0f3; }
    .titulo-gigante {
        color: #800f2f;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-size: 50px;
        font-weight: bold;
        margin-top: 15%;
    }
    /* Estilo para los globos y éxito */
    .stSuccess { font-size: 24px !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- MÚSICA ---
# Puedes cambiar el link de YouTube por cualquier canción romántica
st.write(f'<iframe width="0" height="0" src="https://www.youtube.com/embed/LjhCEhWiKXk?autoplay=1&loop=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)

# PANTALLA 1: BIENVENIDA
if not st.session_state.empezar:
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Clique ici mon amour ✨"):
            st.session_state.empezar = True
            st.rerun()

# PANTALLA FINAL (Cuando dice OUI)
elif st.session_state.mostrar_final:
    st.balloons()
    st.title("OUI ! ❤️")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif") # Tu GIF de Pinterest
    st.success("Je t'aime !")
    st.markdown("""
    ### Je t'aime. 
    ### Sois prête le dimanche 15 février à 20h. 
    ### Habille-toi très jolie, même s'il me semble impossible que tu sois plus belle que tu ne l'es déjà. ❤️
    """)
    # Nota: Puse 15 de febrero porque San Valentín es en febrero, cámbialo a enero en el código si prefieres.

# PANTALLA 2: EL JUEGO
else:
    st.title("Veux-tu être ma Valentine ? 🌹")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")

    # Mensajes de persuasión
    messages = [
        "Tu es sûre ? 🤔",
        "Réfléchis encore... 🥺",
        "Le bouton OUI est plus joli, non ? ✨",
        "Attention... le bouton va commencer à bouger ! 🏃‍♂️"
    ]

    # Lógica de los botones
    if st.session_state.intentos < 3:
        # Botones estáticos (Primeros 3 intentos)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("OUI ! ❤️", key="btn_si_estatico"):
                st.session_state.mostrar_final = True
                st.rerun()
        with col2:
            if st.button("Non 😢", key="btn_no_estatico"):
                st.session_state.intentos += 1
                st.rerun()
        
        if st.session_state.intentos > 0:
            st.info(messages[st.session_state.intentos - 1])

    else:
        # Botones dinámicos (A partir del 4º intento)
        st.info(messages[3])
        
        # HTML/JS para movimiento y crecimiento
        valentine_js = f"""
        <div id="container" style="height: 300px; width: 100%; position: relative; text-align: center;">
            <button id="siBtn" onclick="parent.postMessage('si_clicked', '*')" style="
                background-color: #ff4d6d; color: white; border: none;
                padding: 15px 32px; font-size: {20 + (st.session_state.intentos * 5)}px;
                border-radius: 20px; cursor: pointer; position: absolute;
                left: 10%; top: 50px; transition: 0.3s;
            ">OUI ! ❤️</button>

            <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()" style="
                background-color: #808080; color: white; border: none;
                padding: 15px 32px; font-size: 20px; border-radius: 20px;
                position: absolute; left: 60%; top: 50px; transition: 0.1s;
            ">Non 😢</button>
        </div>

        <script>
            function moveButton() {{
                var btn = document.getElementById('noBtn');
                var x = Math.random() * (window.innerWidth - btn.offsetWidth - 50);
                var y = Math.random() * (250);
                btn.style.left = x + 'px';
                btn.style.top = y + 'px';
            }}
        </script>
        """
        components.html(valentine_js, height=350)
        
        # Escuchar el click del JS
        # Como los componentes de Streamlit son aislados, usamos un pequeño truco de botón invisible o check
        if st.button("Confirmer le OUI ! ❤️ (clique ici si le bouton rose est trop gros)"):
            st.session_state.mostrar_final = True
            st.rerun()

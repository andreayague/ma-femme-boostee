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
import streamlit as st
import streamlit.components.v1 as components





# PANTALLA 1: Bienvenida
if not st.session_state.empezar:
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Clique ici mon amour ✨"):
            st.session_state.empezar = True
            st.rerun()

# PANTALLA FINAL
elif st.session_state.mostrar_final:
    st.balloons()
    st.title("OUI ! ❤️")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")
    st.success("Je t'aime !")
    st.markdown(f"""
    ### Je t'aime. 
    ### Sois prête le dimanche 15 janvier à 20h. 
    ### Habille-toi très jolie, même s'il me semble impossible que tu sois plus belle que tu ne l'es déjà. ❤️
    """)

# PANTALLA 2: La pregunta
else:
    st.title("Veux-tu être ma Valentine ? 🌹")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")

    # Lógica de intentos
    if st.session_state.intentos < 3:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("OUI ! ❤️", type="primary"):
                st.session_state.mostrar_final = True
                st.rerun()
        with col2:
            if st.button("Non 😢"):
                st.session_state.intentos += 1
                st.rerun()
        
        if st.session_state.intentos > 0:
            mensajes = ["Tu es sûre ? 🤔", "Réfléchis encore... 🥺", "Le bouton OUI est plus joli, non ? ✨"]
            st.info(mensajes[st.session_state.intentos - 1])

    else:
        # A partir del 4to intento: Botón "OUI" gigante de Streamlit y "NON" falso que huye
        st.warning("Attention... le bouton va commencer à bouger ! 🏃‍♂️")
        
        # Botón OUI real de Streamlit (Para que funcione el clic)
        # El tamaño aumenta con st.session_state.intentos
        tamano = 20 + (st.session_state.intentos * 10)
        st.markdown(f"<style>div.stButton > button:first-child {{ font-size: {tamano}px !important; width: 100%; }}</style>", unsafe_allow_html=True)
        
        if st.button("OUI ! ❤️", key="boton_gigante", type="primary"):
            st.session_state.mostrar_final = True
            st.rerun()

        # Botón NON que huye (HTML/JS)
        # Este botón es solo visual para "engañarla", al pasar el mouse se mueve
        valentine_js = """
        <div id="container" style="height: 200px; width: 100%; position: relative;">
            <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()" style="
                background-color: #808080; color: white; border: none;
                padding: 10px 20px; font-size: 18px; border-radius: 15px;
                position: absolute; left: 45%; top: 20px; transition: 0.1s;
                cursor: pointer;
            ">Non 😢</button>
        </div>
        <script>
            function moveButton() {
                var btn = document.getElementById('noBtn');
                var x = Math.random() * (window.innerWidth - 100);
                var y = Math.random() * 150;
                btn.style.left = x + 'px';
                btn.style.top = y + 'px';
            }
        </script>
        """
        components.html(valentine_js, height=250)
        
        # Un botón invisible para aumentar el contador si logra clicar el "No" (opcional)
        if st.button("J'insiste, c'est NON !", key="retry"):
            st.session_state.intentos += 1
            st.rerun()

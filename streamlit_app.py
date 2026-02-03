import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial
st.set_page_config(page_title="Pour ma chérie ❤️", page_icon="🌹")

# URL de la música (puedes cambiar este link .mp3 por otro si quieres)
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

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

# PANTALLA 1: Bienvenida
if not st.session_state.empezar:
    # Reproductor de audio invisible (se activa tras el primer clic)
    st.markdown(f'<audio autoplay loop><source src="{audio_url}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Clique ici mon amour ✨", use_container_width=True):
        st.session_state.empezar = True
        st.rerun()

# PANTALLA FINAL
elif st.session_state.mostrar_final:
    st.balloons()
    st.title("OUI ! ❤️")
    
    # Intenta cargar tu foto de GitHub (asegúrate de que se llame mi_foto.jpg)
    try:
        st.image("mi_foto.jpg", use_container_width=True)
    except:
        st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")
    
    st.success("Je t'aime !")
    st.markdown("""
    ### Je t'aime. 
    ### Sois prête le dimanche 15 janvier à 20h. 
    ### Habille-toi très jolie, même s'il me semble impossible que tu sois plus belle que tu ne l'es déjà. ❤️
    """)
    st.audio(audio_url)

# PANTALLA 2: La pregunta
else:
    st.title("Veux-tu être ma Valentine ? 🌹")
    st.image("https://i.pinimg.com/originals/81/15/44/8115442566c727a2024b33878b66f212.gif")

    if st.session_state.intentos < 3:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("OUI ! ❤️", type="primary", use_container_width=True):
                st.session_state.mostrar_final = True
                st.rerun()
        with col2:
            if st.button("Non 😢", use_container_width=True):
                st.session_state.intentos += 1
                st.rerun()
        
        if st.session_state.intentos > 0:
            mensajes = ["Tu es sûre ? 🤔", "Réfléchis encore... 🥺", "Le bouton OUI est plus joli, non ? ✨"]
            st.info(mensajes[st.session_state.intentos - 1])

    else:
        st.warning("Attention... le bouton va commencer à bouger ! 🏃‍♂️")
        tamano = 20 + (st.session_state.intentos * 10)
        st.markdown(f"<style>button[kind='primary'] {{ font-size: {tamano}px !important; }}</style>", unsafe_allow_html=True)
        
        if st.button("OUI ! ❤️", type="primary", use_container_width=True):
            st.session_state.mostrar_final = True
            st.rerun()

        valentine_js = """
        <div id="container" style="height: 150px; width: 100%; position: relative;">
            <button id="noBtn" onmouseover="moveButton()" style="
                background-color: #808080; color: white; border: none;
                padding: 10px 20px; font-size: 18px; border-radius: 15px;
                position: absolute; left: 40%; top: 20px; transition: 0.1s;
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

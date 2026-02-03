import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="Pour ma chérie ❤️", page_icon="🌹")

# Estado de la aplicación
if 'empezar' not in st.session_state:
    st.session_state.empezar = False

# Estilo General
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
    </style>
    """, unsafe_allow_html=True)

# PANTALLA 1: Bienvenida
if not st.session_state.empezar:
    st.markdown('<p class="titulo-gigante">Coucou ma femme boostée ! ❤️</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        if st.button("Clique ici mon amour ✨"):
            st.session_state.empezar = True
            st.rerun()

# PANTALLA 2: La pregunta con el botón esquivo
else:
    st.title("Veux-tu être ma Valentine ? 🌹")
    
    # Tu GIF
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZqZzRyeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/c76IJLufpNwSULPk77/giphy.gif")

    # HTML y JavaScript para los botones
    # El botón "Non" se mueve a una posición aleatoria al pasar el mouse (onmouseover)
    valentine_html = """
    <div id="container" style="height: 400px; width: 100%; position: relative; text-align: center;">
        <button id="siBtn" onclick="onSi()" style="
            background-color: #ff4d6d;
            color: white;
            border: none;
            padding: 15px 32px;
            font-size: 20px;
            border-radius: 20px;
            cursor: pointer;
            transition: 0.3s;
            position: absolute;
            left: 20%;
            top: 50px;
            z-index: 1000;
        ">OUI ! ❤️</button>

        <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()" style="
            background-color: #808080;
            color: white;
            border: none;
            padding: 15px 32px;
            font-size: 20px;
            border-radius: 20px;
            position: absolute;
            left: 60%;
            top: 50px;
            transition: 0.1s;
        ">Non 😢</button>
    </div>

    <script>
        function moveButton() {
            var btn = document.getElementById('noBtn');
            var siBtn = document.getElementById('siBtn');
            
            // Hacer el botón SI más grande cada vez que intentan darle al NO
            var currentSize = parseFloat(window.getComputedStyle(siBtn).fontSize);
            siBtn.style.fontSize = (currentSize + 5) + 'px';
            siBtn.style.padding = (currentSize + 2) + 'px';

            // Mover el botón NO a una posición aleatoria
            var x = Math.random() * (window.innerWidth - btn.offsetWidth - 50);
            var y = Math.random() * (300); // Rango de altura dentro del container
            
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }

        function onSi() {
            parent.postMessage({type: 'streamlit:setComponentValue', value: 'si_clicked'}, '*');
            alert("JE T'AIME ! Tu me rends le plus heureux du monde ! ❤️✨");
        }
    </script>
    """
    
    # Renderizar el componente
    components.html(valentine_html, height=500)

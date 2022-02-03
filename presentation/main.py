import streamlit as st
from phases import phase1
from phases import phase2
from phases import phase3
from phases import phase4
from phases import phase5

st.set_page_config(page_title='MOVIE EDA', page_icon='/img/eda.png', layout='wide')

st.sidebar.image('/img/eda.jpg')

st.sidebar.markdown("""
                ## <br/><div style="text-align: center">ANÁLISIS EXPLORATORIO CON HISTÓRICO DE PELÍCULAS</div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("""***""")

selectedPhase = st.sidebar.selectbox('Fase', [
    '1. Introducción',
    '2. Elección de la fuente',
    '3. Extracción de los datos',
    '4. Limpieza y preparación de los datos',
    '5. Análisis exploratorio'
])

if selectedPhase == '1. Introducción':
    phase1.phase1()
elif selectedPhase == '2. Elección de la fuente':
    phase2.phase2()
elif selectedPhase == '3. Extracción de los datos':
    phase3.phase3()
elif selectedPhase == '4. Limpieza y preparación de los datos':
    phase4.phase4()
elif selectedPhase == '5. Análisis exploratorio':
    phase5.phase5()

st.sidebar.markdown("""
    ***
    **Daniel Vivas - Enero 2022**
    contacto@danielvivas.com
""")
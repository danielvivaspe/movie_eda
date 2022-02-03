import streamlit as st

import pandas as pd

def phase4():
    st.markdown("""
            # Fase 4: Limpieza y preparación de los datos
            #### Una vez descargados todos los datos, hay que prepararlos para su análisis.
            ***
            ##### Partimos del siguiente dataframe:
            """)
    st.text('')

    df = pd.read_csv('src/data/all_data.csv', nrows=1000)
    st.dataframe(df)

    st.text('')
    st.text('')
    st.markdown("""
                ##### Hemos trabajado con las siguientes columnas:
                """)

    with st.expander('Presupuesto'):
        st.markdown("""
            - Registros sin presupuesto
            - Presupuesto menor de 1000
        """)

    with st.expander('Ingresos'):
        st.markdown("""
            - Registros sin beneficio
        """)

    with st.expander('Genero'):
        st.markdown("""
            - Registros sin género
        """)

    with st.expander('Estado'):
        st.markdown("""
            - Se filtra por películas ya publicadas
            - Después de filtrar, se borra la columna
        """)

    with st.expander('Fecha'):
        st.markdown("""
            - Se filtra por películas publicadas en el 2022
            - Se eliminan los registros sin fecha
        """)

    with st.expander('Nuevas columnas'):
        st.markdown("""
            - Beneficio
            - Año
            - Mes
            - Return Of Investment (%)
            - Media bayesiana de votos
        """)

    st.markdown("""
            ### <br/><div style="text-align: center">Pasamos de un dataframe con 669 410 registros a tener 9007 registros</div>
        """, unsafe_allow_html=True)

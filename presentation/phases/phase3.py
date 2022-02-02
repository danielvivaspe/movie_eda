import streamlit as st

import urllib.request, json
import pandas as pd

def phase3():
    st.markdown("""
            # Fase 3: Extracción de los datos
            #### Proceso de extracción de los datos desde la API de The Movie Database.
            ***
            """)


    st.markdown("""
        ## TMDB ofrece un listado diario de todos los IDs y otros datos que se encuentran en su plataforma con casi 700 000 registros:
        """)

    df = pd.read_json('../src/data/tmdb-ids.json', lines=True, nrows=1000)
    st.dataframe(df)

    st.text('')

    st.markdown("""
        ***
        ##### Es necesario analizar el formato en el que la API devuelve los datos:
    """)

    id = st.text_input('ID de la película')

    searchButton = st.button('Buscar')

    if searchButton:
        jsonData = fetchData(id)
        st.header(jsonData['original_title'])
        st.json(jsonData)


    st.markdown("""
        ***
        ## Para conseguir todos los datos, los pasos que se han realizado son:
        
        #### 1. Crear dataframe vacío y desechar el resto de las columnas
        #### 2. Trocear el dataframe
        #### 3. Atacar la API para rellenar el dataframe con los datos de las películas
        #### 4. Unir los ficheros con los datos
    """)



def fetchData(id):
    apikey = '199c618826a0a7286c6bef47d076a144'
    link = f'https://api.themoviedb.org/3/movie/{id}?api_key={apikey}'
    with urllib.request.urlopen(link) as url:
        return json.loads(url.read().decode())
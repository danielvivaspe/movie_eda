import streamlit as st

def phase2():

    st.markdown("""
        # Fase 2: Recopilación de datos
        #### Una vez decidido la temática de nuestro análisis, la siguiente decisión a tomar es la fuente de datos.
        ***
        ##### Se han considerado varias fuentes para este proyecto:
        """)
    st.text('')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image('./img/omdb.png', use_column_width='auto')
        st.text('')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">API oficial de IMDb, probablemente la API más conocida. En su versión básica es gratuita y tiene límite de uso.</div>
            """, unsafe_allow_html=True)

    with col2:
        st.image('./img/imdb.png', use_column_width='auto')
        st.text('')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">Orientada a proyectos más profesionales, hay que rellenar un formulario para su uso</div>
            """, unsafe_allow_html=True)

    with col3:
        st.image('./img/kaggle.png', use_column_width='auto')
        st.text('')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">Contiene datasets muy completos listos para su análisis. No contiene datos actualizados.</div>
            """, unsafe_allow_html=True)

    with col4:
        st.image('./img/tmdb.png', use_column_width='auto')
        st.text('')
        st.markdown("""
                    ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">Contiene datos bastante completos con un catálogo de más de 700 000 registros entre películas y otro contenido multimedia. Contiene información acerca del presupuesto y de los ingresos conseguidos.</div>
                    """, unsafe_allow_html=True)

    st.text('')
    st.text('')
    st.markdown("""
        #### <br/><div style="text-align: center">Nos decantamos por esta última puesto que tiene datos actualizados así como las variables que queremos estudiar</div>
    """, unsafe_allow_html=True)

def foward():
    pass
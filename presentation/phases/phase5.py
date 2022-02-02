import streamlit as st

import pandas as pd
import plotly.express as px


def removeOutliers(dtf, *columns):
    for i in range(len(columns)):
        q_low = dtf[columns[i]].quantile(0.01)
        q_hi = dtf[columns[i]].quantile(0.99)
        dtf = dtf[(dtf[columns[i]] < q_hi) & (dtf[columns[i]] > q_low)]
    return dtf


def graph1(data):
    fig = px.scatter(
        data,
        x="budget",
        y='profit',
        height=650,
        width=900
    )

    fig.update_xaxes(range=[-2000000, 190000000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph2(data):
    fig = px.scatter(
        data,
        x=data["budget"],
        y=data['profit'],
        height=650,
        width=900
    )
    fig.add_shape(type='line',
                  x0=0,
                  y0=0,
                  x1=200000000,
                  y1=0,
                  line=dict(color='Yellow'))
    fig.update_xaxes(range=[-2000000, 190000000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph3(data):
    fig = px.scatter(
        data,
        x="budget",
        y='ROI',
        height=650,
        width=900
    )
    fig.update_xaxes(range=[-2000000, 190000000], row=1, col=1)
    fig.update_yaxes(range=[-200, 7000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph4(data, en):
    if en:
        data = data[data['original_language'] == 'en']
    else:
        data = data[data['original_language'] != 'en']

    fig = px.scatter(
        data,
        x="budget",
        y='ROI',
        height=650,
        width=900
    )
    fig.update_xaxes(range=[-2000000, 190000000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph5(data, sum):
    if sum:
        data = data.groupby('year').sum().reset_index()
    else:
        data = data.groupby('year').mean().reset_index()

    fig = px.line(data, x="year", y="budget", width=1000)
    fig.update_xaxes(range=[1913, 2022], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph6(data):
    fig = px.histogram(
        data,
        x="runtime",
        y='profit',
        height=650,
        width=900,
        # nbins=80,
        labels={
            'profit': 'Total profit',
            'runtime': 'Duration'
        }
    )
    fig.update_yaxes(range=[-100000000, 14000000000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph7(data):
    fig = px.scatter(
        data,
        x="popularity",
        y='budget',
        height=650,
        width=900
    )
    fig.update_xaxes(range=[-1, 250], row=1, col=1)
    fig.update_yaxes(range=[-6000000, 400000000], row=1, col=1)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph8(data, order):
    yaxis = ''

    if order == 'Presupuesto':
        yaxis = 'budget'
        data = data.groupby('genre').sum().sort_values(yaxis, ascending=False).reset_index()

    elif order == 'Popularidad':
        yaxis = 'popularity'
        data = data.groupby('genre').sum().sort_values(yaxis, ascending=False).reset_index()

    elif order == 'Ingresos':
        yaxis = 'revenue'
        data = data.groupby('genre').sum().sort_values(yaxis, ascending=False).reset_index()

    elif order == 'Media bayesiana de votos':
        yaxis = 'bayesAVG'
        data = data.groupby('genre').mean().sort_values(yaxis, ascending=False).reset_index()


    fig = px.bar(
        data,
        x='genre',
        y=yaxis
    )

    if order == 'Media bayesiana de votos':
        fig.update_yaxes(range=[6, 7], row=1, col=1)

    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def graph9(data):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data['month'] = pd.Categorical(data['month'], categories=months, ordered=True)
    data.sort_values('month', inplace=True)

    fig = px.line(
        data.groupby('month').sum().reset_index(),
        x='month',
        y='revenue',
        width=1000,
        height=600
    )
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

def phase5():
    st.markdown("""
                # Fase 5: Análisis exploratorio
                #### Llegamos a la fase final del EDA. Una vez tenemos los datos consolidados, es hora de analizarlos
                ***
                ##### Partimos del siguiente dataframe:
                """)
    st.text('')

    df = pd.read_csv('../data/clean_data.csv', index_col='tmdb_id')
    df['year'] = df['year'].astype('Int32')

    st.dataframe(df)

    st.markdown("""
        ***
        ### Distribución de la relación entre el presupuesto y el beneficio
        #### *Cuanto más invierta más beneficio obtendré, ¿no?*
    """)

    with st.expander('Desplegar'):

        data = removeOutliers(df, 'budget', 'profit')
        graph1(data)

        st.markdown("""
                ##### Nos fijamos en los valores del beneficio por debajo de 0:
            """)

        data = removeOutliers(df, 'budget', 'profit')
        graph2(data)


    st.markdown("""
            ***
            ### Distribución de la relación entre el presupuesto y el ROI
        """)

    with st.expander('Desplegar'):

        data = removeOutliers(df, 'budget', 'ROI')
        graph3(data)

        st.markdown("""
                        ##### ¿Y si discriminamos por el lenguaje original?
                    """)

        language = st.radio(
            "Filtrado por idioma original",
            ('Habla inglesa', 'Habla no inglesa'))

        if language == 'Habla inglesa':
            graph4(data, True)
        else:
            graph4(data, False)

    st.markdown("""
                ***
                ### Evolución del presupuesto a lo largo del tiempo
                #### *¿Se invierte cada vez más en la producción de las películas?*
            """)

    with st.expander('Desplegar'):
        budget = st.radio(
            "Analizar presupuesto:",
            ('Total', 'Medio'))

        if budget == 'Total':
            graph5(df, True)
        else:
            graph5(df, False)

    st.markdown("""
        ***
        ### Beneficio en función de la duración
        #### *¿Influye la duración en los beneficios generados?*
    """)

    with st.expander('Desplegar'):
        data = removeOutliers(df, 'runtime', 'profit')
        graph6(data)

    st.markdown("""
        ***
        ### Popularidad en función del presupuesto
        #### *"Las películas con más presupuesto son más conocidas porque pueden invertir más en publicidad"*
    """)

    with st.expander('Desplegar'):
        data = removeOutliers(df, 'popularity')
        graph7(data)


    st.markdown("""
                ***
                ### Ingresos por meses
                #### *En épocas de vacaciones seguro que se generan más ingresos*
            """)

    with st.expander('Desplegar'):
        graph9(data)

    st.markdown("""
                ***
                ### Popularidad, ingresos y media bayesiana de votos por géneros
                #### *¿Que géneros lideran los rankings?*
            """)

    with st.expander('Desplegar'):

        order = st.radio(
            "Ordenar por",
            ('Popularidad', 'Presupuesto', 'Ingresos', 'Media bayesiana de votos'))

        graph8(data, order)

        st.markdown("""
                        ##### Si son más populares, más gente irá a verlas e ingresarán más dinero, ¿verdad?
                    """)

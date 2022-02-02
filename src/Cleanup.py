import pandas as pd

def run():
    # Leo el dataframe
    data = pd.read_csv('data/all_data.csv', index_col='tmdb_id')

    # Descarto registros sin presupuesto
    data = data[data['budget'] != 0]

    # Descarto presupuestos por debajo de 1000
    data = data[data['budget'] >= 1000]

    # Descarto registros sin beneficio
    data = data[data['revenue'] != 0]

    # Descarto registros sin género principal
    data = data[data['genre'] != '0']

    # Descarto registros de películas que no estén publicadas
    data = data[data['status'] == 'Released']

    # Ya no necesito la columna status puesto que ya he filtrado por ella
    data.drop(columns=['status'], inplace=True)

    # Añado una columna de ingresos
    data['profit'] = data['revenue'] - data['budget']

    # Retiro los registros sin fecha
    data.dropna(subset=['release_date'], how='all', inplace=True)

    # Añado una columna con el año
    data['year'] = data['release_date'].str[:4]

    # Añado otra columna con el mes
    months = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec',
    }
    data['month'] = data['release_date'].apply(lambda x: months[x[5:7]])

    # Borro los registros del 2022
    data = data[data['year'] != '2022']

    # Creo una columna con el ROI
    data['ROI'] = ((data['revenue'] - data['budget']) / data['budget']) * 100

    # Añado una columna con la media bayesiana de la valoración
    # https://www.algolia.com/doc/guides/solutions/ecommerce/relevance-optimization/tutorials/bayesian-average/
    confidence = 50
    votes_avg = 6.1757
    data['bayesAVG'] = ((data['vote_average'] * data['vote_count']) + (confidence * votes_avg)) / (
                data['vote_count'] + confidence)

    data.to_csv('data/clean_data.csv')
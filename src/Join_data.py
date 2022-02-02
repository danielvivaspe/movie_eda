import pandas as pd

def run():
    # Leo el primer trozo como base
    data = pd.read_csv('data/sliced_files/data_1_filled.csv', index_col='tmdb_id')

    # Uno a uno voy uniendo los siguientes trozos
    for i in range(2, 68):
        df = pd.read_csv(f'data/sliced_files/data_{i}_filled.csv', index_col='tmdb_id')
        data = pd.concat([data, df])

        # Guardo el dataframe consolidado
        data.to_csv('data/all_data.csv')

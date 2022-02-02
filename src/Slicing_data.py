import pandas as pd
import urllib.request, json

def run():
    # Leo la lista de ids con el resto de datos
    data = pd.read_json('data/tmdb-ids.json', lines=True)

    # Solo me interesan los ids, por lo que deshecho el resto de columnas
    data.drop(columns=['adult', 'original_title', 'popularity', 'video'], inplace=True)

    # Renombro la columna de id
    data.rename(columns={"id": "tmdb_id"}, inplace=True)

    # Creo las columnas de datos que me interesa tener
    data = data.reindex(columns=[
        'tmdb_id', 'adult', 'budget', 'genre', 'original_language',
        'original_title', 'overview', 'popularity', 'poster_path',
        'release_date', 'revenue', 'runtime', 'status', 'tagline',
        'title', 'vote_average', 'vote_count'], fill_value=0)

    # Defino el tipo de datos del dataframe
    data = data.astype({
        'adult': bool, 'budget': int, 'genre': str, 'original_language': str,
        'original_title': str, 'overview': str, 'popularity': float, 'poster_path': str,
        'release_date': str, 'revenue': int, 'runtime': int, 'status': str, 'tagline': str,
        'title': str, 'vote_average': float, 'vote_count': int
    })

    # Defino el índice
    data.set_index('tmdb_id', inplace=True)

    # El dataset es enorme, lo divido en trozos de 10000 registros
    size = 10000

    for i in range(1, 68):
        inicio = size * (i - 1)
        fin = (size * i) - 1
        trozo = data[inicio:fin]
        trozo.to_csv(f'data/sliced_files/data_{i}.csv')
import pandas as pd
import urllib.request, json
import sys
import os
from termcolor import colored, cprint

file_num = sys.argv[1]

def getMovieData(movie, df):
    print(movie)
    apikey = '199c618826a0a7286c6bef47d076a144'
    link = f'https://api.themoviedb.org/3/movie/{movie}?api_key={apikey}'

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        print(data)

        df.loc[movie, 'adult']              = data['adult']
        df.loc[movie, 'budget']             = data['budget']
        if len(data['genres']) > 0:
            df.loc[movie, 'genre']          = data['genres'][0]['name']
        df.loc[movie, 'original_language']  = data['original_language']
        df.loc[movie, 'original_title']     = data['original_title']
        df.loc[movie, 'overview']           = data['overview']
        df.loc[movie, 'popularity']         = data['popularity']
        df.loc[movie, 'poster_path']        = data['poster_path']
        df.loc[movie, 'release_date']       = data['release_date']
        df.loc[movie, 'revenue']            = data['revenue']
        df.loc[movie, 'runtime']            = data['runtime']
        df.loc[movie, 'status']             = data['status']
        df.loc[movie, 'tagline']            = data['tagline']
        df.loc[movie, 'title']              = data['title']
        df.loc[movie, 'vote_average']       = data['vote_average']
        df.loc[movie, 'vote_count']         = data['vote_count']

        print(f"Added {movie} - {data['original_title']}")
        cprint(f"Added {movie} - {data['original_title']}", 'white', 'on_green')
        print()

        return df


if os.path.isfile(f'src/data/sliced_files/data_{file_num}_filled.csv'):
    data = pd.read_csv(f'src/data/sliced_files/data_{file_num}_filled.csv', sep=',', index_col='tmdb_id')
else:
    data = pd.read_csv(f'src/data/sliced_files/data_{file_num}.csv', sep=',', index_col='tmdb_id')

count = 0

total = data.shape[0]
pending = data[data['original_title'] == 0].shape[0]
filled = data[data['original_title'] != 0].shape[0]

print(f'Pending: {pending} | filled: {filled}')

if(input('Press y to continue ') == 'y'):

    for row in data[data['original_title'] == 0].itertuples():
        try :
            data = getMovieData(row.Index, data)
            pending -= 1
            filled +=1
            if count == 50:
                data.to_csv(f'data_{file_num}_filled.csv')
                print('Guardando...')
                count = 0
                    
            count += 1
            print(f'Pending: {pending} | filled: {filled}')
            cprint(f'Pending: {pending} | filled: {filled}', 'white', 'on_yellow')
        except:
            print(f'Movie fetch {row.Index} failed')
            cprint(f'Movie fetch {row.Index} failed', 'white', 'on_red')



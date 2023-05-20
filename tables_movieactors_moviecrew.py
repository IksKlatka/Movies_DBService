"""
Collecting data to tables:
- movie_actors
- movie_crew
"""
import pandas as pd
import json
from model import *

pd.set_option('display.max_columns', None)

def get_cast(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_id=index, **d)
        entries.append(entry)

    return entries

def get_crew(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CrewEntry(movie_index=index, **d)
        entries.append(entry)

    return entries



def create_movie_actors_table(df: pd.DataFrame):

    # list of cast (individually)
    all_cast_entries = []
    for i, movie in enumerate(df['cast']):
        entries = get_cast(i, movie)
        for e in entries:
            all_cast_entries.append(e)

    # renaming columns
    movieactor_entries = pd.DataFrame(all_cast_entries)
    movieactor_entries.rename(columns={'order': 'orders', 'keyword_id': 'actor_id'},
                         inplace=True)

    # changing order of columns
    movieactor_entries = movieactor_entries.set_index(['movie_index'])
    movieactor_entries = movieactor_entries[['actor_id', 'cast_id',
                                   'character', 'credit_id', 'gender', 'orders']]

    # adding extra column necessary in the table
    movieactor_entries['movie_index'] = mdf['keyword_id']
    movieactor_entries.insert(0, 'movie_index', movieactor_entries.pop('movie_index'))
    # movieactor_entries.info()

    #reset index (from movie_index) & set it to credit_id
    movieactor_entries = movieactor_entries.reset_index(drop=True)
    # movieactor_entries = movieactor_entries.set_index('credit_id')

    return movieactor_entries #

def create_movie_crew_table(df: pd.DataFrame):

    # list of crew (individually)
    all_crew_entries = []
    for i, movie in enumerate(df['crew']):
        entries = get_crew(i, movie)
        for e in entries:
            all_crew_entries.append(e)

    moviecrew_table = pd.DataFrame(all_crew_entries)

    #enable inserting valid movie_index by setting index = movie_index
    moviecrew_table = moviecrew_table.set_index(['movie_index'])
    moviecrew_table['movie_index'] = cdf['movie_index']

    #placing movie_index column on the right place in DF
    moviecrew_table.insert(2, 'movie_index', moviecrew_table.pop('movie_index'))

    #renaming column and changing their order in DF
    moviecrew_table = moviecrew_table.rename(columns={'keyword_id': 'person_id'})
    moviecrew_table = moviecrew_table[['credit_id', 'movie_index', 'person_id',
                             'job', 'department', 'gender']]

    moviecrew_table = moviecrew_table.reset_index(drop= True)
    moviecrew_table = moviecrew_table.set_index('credit_id')

    return  moviecrew_table
    # save_to_file(moviecrew_table, 'table_moviecrew.csv')

def save_to_file(dataframe: pd.DataFrame, filename: str):
    dataframe.to_csv(rf'C:/Users/igakl/Desktop/MOVIES/datas/{filename}',
                     sep=';')


if __name__ == '__main__':
    credits = pd.read_csv('./datas/tmdb_5000_credits.csv')
    movies = pd.read_csv('./datas/tmdb_5000_movies.csv')
    mdf = pd.DataFrame(movies)
    cdf = pd.DataFrame(credits)

    movieactors = create_movie_actors_table(cdf)
    moviecrew = create_movie_crew_table(cdf)

    # movieactors.info()
    # print('movie actors table: ')
    # movieactors.info()
    # print('---'*15, '\nmovie crew table: ')
    # moviecrew.info()

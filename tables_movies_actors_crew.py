"""
Collecting data to tables:
- movies
- actors
- crew
"""

import pandas as pd
import json
from functions import get_crew_of_movie
from model import CastEntry

def get_cast(index: int, cast_field: str):
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_id=index, **d)
        entries.append(entry)

    return entries

def create_table_actors(df: pd.DataFrame):

    #extracting data from object 'cast'
    entries = []
    for i, movie in enumerate(df['cast']):
        entry = get_cast(i, movie)
        for e in entry:
            entries.append(e)

    #creating DF from extracted data
    actors = pd.DataFrame(entries)
    actors = actors.rename(columns={'keyword_id': 'actor_id'})
    #extracting keyword_id and name of an actor from DF above
    actors_table = actors[['name', 'actor_id']]
    actors_table = actors_table.drop_duplicates('name')

    return actors_table
    # save_to_file(actors_table, 'table_actors.csv')

def create_table_movies(df: pd.DataFrame):

    # creating new DF containing movies keyword_id and title
    movies_table = df[['keyword_id', 'title']]
    # movies_table = movies_table.set_index('keyword_id')
    movies_table = movies_table.drop_duplicates('title')
    # save_to_file(movies_table, 'table_movies.csv')
    return movies_table

def create_table_crew(df: pd.DataFrame):
    # TABLE CREW
    # list of crew (individually)
    all_crew_entries = []
    for i, movie in enumerate(df['crew']):
        entry = get_crew_of_movie(i, movie)
        for e in entry:
            all_crew_entries.append(e)

    crew = pd.DataFrame(all_crew_entries)
    crew_table = crew[['keyword_id', 'name']]
    crew_table = crew_table.drop_duplicates('name')
    # crew_table = crew_table.set_index('name')

    # save_to_file(crew_table, 'table_crew.csv')
    return crew_table

def save_to_file(df: pd.DataFrame, filename: str):
    df.to_csv(path_or_buf=fr'C:/Users/igakl/Desktop/MOVIES/datas/{filename}',
              sep=';')


if __name__ == "__main__":

    # importing csv files
    c = pd.read_csv('./datas/tmdb_5000_credits.csv')
    m = pd.read_csv('./datas/tmdb_5000_movies.csv')
    # creating DataFrames from csv files
    mdf, cdf = pd.DataFrame(m), pd.DataFrame(c)

    crew_tbl = create_table_crew(cdf)
    actors_tbl = create_table_actors(cdf)
    movies_tbl = create_table_movies(mdf)

    print('crew: ') #52234
    crew_tbl.info()
    print('----'*15,'\nactors: ') #54201
    actors_tbl.info()
    print('----'*15,'\nmovies: ') #4802
    movies_tbl.info()

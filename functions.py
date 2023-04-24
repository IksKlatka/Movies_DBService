import json
from collections import defaultdict
from collections.abc import Iterable
import pandas as pd
from model import *

pd.options.display.max_rows = 10

# ACTORS ----------------
def get_cast_of_movie(movie_id: int, cast_field: str) -> list[CastEntry]:
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_id=movie_id, **d)
        entries.append(entry)
    return entries

def get_cast():
    casts_ = list(df('cast'))
    return casts_

def get_actors(casts: list[str]) -> Iterable[Actor]:
    actors = []
    for a, movie in enumerate(casts):
        entries = get_cast_of_movie(a, movie)
        actors.extend([(c.id, c.name) for c in entries])
    actors = set(actors)
    return actors

def check_unique_cast_credit_id(casts: list[str]):
    credit_ids = []
    for i, movie in enumerate(casts):
        entries = get_cast_of_movie(i, movie)
        credit_ids.extend([c.credit_id for c in entries])

    unique = (len(credit_ids) == len(set(credit_ids)))
    print(f'{unique=}')

def check_assignment_cast(cast: list[str]):

    name_id_pairs = []

    for i, movie in enumerate(cast):
        entries = get_cast_of_movie(i, movie)
        for e in entries:
            print(e)
        name_id_pairs.extend([(c.id, c.name) for c in entries])

    unique_pairs = set(name_id_pairs)
    n_pairs = len(unique_pairs)
    n_names = len(set([c for i, c in unique_pairs]))  # unique names
    n_ids = len(set([i for i, c in unique_pairs]))  # unique id's

    print(f'{n_pairs=}')
    print(f'{n_ids=}')
    print(f'{n_names=}')

    def find_duplicates_cast(casts: list[str]):
        name_id_pairs = []
        for i, movie in enumerate(casts):
            entries = get_cast_of_movie(i, movie)
            name_id_pairs.extend([(c.id, c.name) for c in entries])

        unique_pairs = set(name_id_pairs)
        id_to_name = defaultdict(lambda: set())
        for (id, name) in unique_pairs:
            id_to_name[id].add(name)

        for (k, v) in id_to_name.items():
            if len(v) > 1:
                print('id->names ', k, v)

        # -----
        name_to_id = defaultdict(lambda: set())
        for (id, name) in unique_pairs:
            name_to_id[name].add(id)

        for (k, v) in name_to_id.items():
            if len(v) > 4:
                print('name->ids ', k, v)


# CREW ----------------
def get_crew_of_movie(index: int, crew_field: str) -> list[CrewEntry]:
    dicts = json.loads(crew_field)
    entries = []
    for d in dicts:
        entry = CrewEntry(movie_index=index, **d)
        entries.append(entry)
    return entries

def check_assignment_crew(crew: list[str]):

    name_id_pairs = []


    for i, movie in enumerate(crew):
        entries = get_crew_of_movie(i, movie)
        for e in entries:
            print(e)
        name_id_pairs.extend([(c.id, c.name) for c in entries])

    unique_pairs = set(name_id_pairs)
    n_pairs = len(unique_pairs)
    n_names = len(set([c for i, c in unique_pairs]))  # unique names
    n_ids = len(set([i for i, c in unique_pairs]))  # unique id's

    print(f'{n_pairs=}')
    print(f'{n_ids=}')
    print(f'{n_names=}')

def find_duplicates_crew(crews: list[str]):
    name_id_pairs =[]
    for i, movie in enumerate(crews):
        entries = get_crew_of_movie(i, movie)
        name_id_pairs.extend([(c.id, c.name) for c in entries]) #comprehension

    unique_pairs = set(name_id_pairs)
    id_to_name = defaultdict(lambda : set())
    for (id, name) in unique_pairs:
        id_to_name[id].add(name)

    for (k, v) in id_to_name.items():
        if len(v) > 1:
            print('name -> ids: ', k, v)

    # -----
    name_to_id = defaultdict(lambda : set())
    for (id, name) in unique_pairs:
        name_to_id[name].add(id)

    for (k,v) in name_to_id.items():
        if len(v) > 4:
            print('name -> ids: ', k, v)


#MOVIES ----------------

def to_movie_actor(cast_entry: CastEntry) -> MovieActor:
    """Create MovieActor object from CastEntry object"""
    elem = cast_entry
    return MovieActor(movie_id=elem.movie_id, actor_id=elem.id, cast_id=elem.cast_id,
                      character=elem.character, credit_id=elem.credit_id, gender=elem.gender,
                      orders=elem.order)

def get_movies(filename: str) -> Iterable[Movie]:
    """Get movies from CSV"""
    df = pd.read_csv(filename)
    subframe = df.loc[:, ['id', 'title']]
    subframe_as_dict = subframe.to_dict(orient='records')
    #comprehension: creating list[object] of Movies
    movies = [Movie(movie_id=d['id'], title=d['title']) for d in subframe_as_dict]
    return movies

def get_movie_actors(filename: str) -> Iterable[MovieActor]:
    """Correctly assigning actors to movies"""
    df = pd.read_csv(filename)
    subframe = df.loc[:, ['movie_id', 'cast']]
    subframe_as_dict = subframe.to_dict(orient='records')
    result = []
    for row in subframe_as_dict:
        movie_id = row['movie_id']
        cast_string = row['cast']
        all_casts = get_cast_of_movie(movie_id, cast_string)
        all_casts = [to_movie_actor(ac) for ac in all_casts]
        result.extend(all_casts)
    return result


if __name__ == '__main__':
    df = pd.read_csv('./datas/tmdb_5000_credits.csv')
    casts_ = list(df['cast'])  # list[str]
    crew_ = list(df['crew'])


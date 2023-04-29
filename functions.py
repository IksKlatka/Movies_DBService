import json
from collections.abc import Iterable
import pandas as pd
from model import *

pd.options.display.max_rows = 10

# ACTORS ----------------
def get_cast():
    df = pd.read_csv('./datas/tmdb_5000_credits.csv')
    casts_ = list(df['cast'])
    return casts_

def get_cast_of_movie(movie_id: int, cast_field: str) -> list[CastEntry]:
    dicts = json.loads(cast_field)
    entries = []
    for d in dicts:
        entry = CastEntry(movie_id=movie_id, **d)
        entries.append(entry)
    return entries
    # print(entries)

def get_actors_of_movie(casts: list[str]) -> Iterable[Actor]:
    """returns id:name pairs"""
    actors = []
    for a, movie in enumerate(casts):
        entries = get_cast_of_movie(a, movie)
        actors.extend([(e.id, e.name) for e in entries])
    actors = set(actors)
    return actors




# CREW ----------------
def get_crew():
    df = pd.read_csv('datas/tmdb_5000_credits.csv')
    crew_ = list(df['crew'])
    return crew_

def get_crew_of_movie(index: int, crew_field: str) -> list[CrewEntry]:
    dicts = json.loads(crew_field)
    entries = []
    for d in dicts:
        entry = CrewEntry(movie_index=index, **d)
        entries.append(entry)
    return entries

def get_crew_people(crews: list) -> Iterable[CrewPerson]:
    """returns id:name pairs"""
    people = []
    for c, movie in enumerate(crews):
        entries = get_crew_of_movie(c, movie)
        people.extend([(e.id, e.name) for e in entries])
    people = set(people)
    return people
    # print(people)

def to_movie_crew(crew_entry: CrewEntry) -> MovieCrew:

    c = crew_entry
    return MovieCrew(movie_id=c.movie_index, person_id=c.id, credit_id=c.credit_id,
                     department=c.department, gender=c.gender, job=c.job)



#MOVIES ----------------
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

def to_movie_actor(cast_entry: CastEntry) -> MovieActor:
    """Create MovieActor object from CastEntry object"""
    c = cast_entry
    return MovieActor(movie_id=c.movie_id, actor_id=c.id, cast_id=c.cast_id,
                      character=c.character, credit_id=c.credit_id, gender=c.gender,
                      orders=c.order)

def get_movie_crew(filename: str) -> Iterable[MovieCrew]:
    """Correctly assigning crew people to movies"""
    df = pd.read_csv(filename)
    subframe = df.loc[:, ['movie_index', 'crew']]
    subframe_as_dict = subframe.to_dict(orient='records')
    result=[]
    for row in subframe_as_dict:
        movie_id = row['movie_index']
        crew = row['crew']
        all_crew = get_crew_of_movie(movie_id, crew)
        all_crew = [to_movie_crew(ac) for ac in all_crew]
        result.extend(all_crew)

    return result


# LANGUAGES ----------------
def get_spoken_langs(filename: str):
    """
    all spoken languages with iso code
    at the same time => filling for languages table
    """
    df = pd.read_csv(filename)
    spoken_langs = list(df['spoken_languages'])
    entries = []
    for spoken in spoken_langs:
        dicts = json.loads(spoken)
        for d in dicts:
            entry = Language(lang_id=d['iso_639_1'], lang=d['name'])
            if entry not in entries:
                entries.append(entry)

    return entries

def get_movie_lang(filename: str):

    df = pd.read_csv(filename) #movies.csv
    subframe = df.loc[:, ['id', 'original_language']]
    subframe_as_dict = subframe.to_dict(orient='records')
    movie_lang = [MovieLanguage(movie_id=d['id'], lang_id=d['original_language'])\
              for d in subframe_as_dict]

    return(movie_lang)


# PRODUCTION COMPANIES --------------

def get_companies() -> list[Company]:
    """COMPANY object"""
    df= pd.read_csv('datas/tmdb_5000_movies.csv')
    comps = df['production_companies']
    entries = []
    for c in comps:
        dicts = json.loads(c)
        for d in dicts:
            entry = Company(**d)
            if entry not in entries:
                entries.append(entry)

    return entries

def companies_for_movie(index: int, company_field: str):
    """COMPANY ENTRY object"""
    dicts = json.loads(company_field)
    comps = []
    for d in dicts:
        company = CompanyEntry(index, **d)
        comps.append(company)

    return comps

def get_company_of_movie() -> list[MovieCompany]:

    df= pd.read_csv('datas/tmdb_5000_movies.csv')
    subframe = df.loc[:, ['id', 'production_companies']]
    subframe_as_dict = subframe.to_dict(orient='records')

    result = []
    for r, row in enumerate(subframe_as_dict):
        movie_id = row['id']
        comps = row['production_companies']
        all_comps = companies_for_movie(movie_id, comps)
        mov_comp = [to_moviecompany(ac) for ac in all_comps]
        result.extend(mov_comp)

    return result

def to_moviecompany(company_entry: CompanyEntry) -> MovieCompany:
    ce = company_entry
    return MovieCompany(movie_id=ce.movie_index, company_id=ce.id)

# COUNTRIES -------------------------
def get_countries(filename: str) -> list[Country]:

    df = pd.read_csv(filename)
    prod_count = list(df['production_countries'])
    entries = []
    for count in prod_count:
        dicts = json.loads(count)
        for d in dicts:
            entry = Country(country_id=d['iso_3166_1'], name=d['name'])
            if entry not in entries:
                entries.append(entry)

    return entries

def get_countries_of_movie(index: int, country_field: str):
    dicts = json.loads(country_field)
    countries = []
    for d in dicts:
        d['country_id'] = d['iso_3166_1']
        del d['iso_3166_1']
        country = CountryEntry(index, **d)
        countries.append(country)

    return countries

def get_movie_country(filename: str):

    df = pd.read_csv(filename)
    subframe = df.loc[:, ['id', 'production_countries']]
    subframe_as_dict = subframe.to_dict(orient='records')
    result = []
    for row in subframe_as_dict:
        movie_id = row['id']
        countries = row['production_countries']
        all_countries = get_countries_of_movie(movie_id, countries)
        movie_country = [to_moviecountry(mc) for mc in all_countries]
        result.extend(movie_country)

    return result

def to_moviecountry(country_entry: CountryEntry) -> MovieCountry:
    ce = country_entry
    return MovieCountry(movie_id=ce.movie_index, country_id=ce.country_id)

# GENRES ------------------------------------
def get_genres(filename):
    df = pd.read_csv(filename)
    genres = list(df['genres'])  # list[str]
    entries = []
    for genre in genres:
        dicts = json.loads(genre)
        for d in dicts:
            entry = Genre(genre_id=d['id'], name=d['name'])
            if entry not in entries:
                entries.append(entry)
    return entries

def get_movie_genres(filename):
    df = pd.read_csv(filename)
    df_sub = df.loc[:, ['id', 'genres']]  # wycinek tabel
    df_as_dict = df_sub.to_dict(orient='records')
    entries = []
    for movie in df_as_dict:
        genres = json.loads(movie.get('genres'))
        for genre in genres:
            entry = MovieGenre(movie_id=movie.get('id'), genre_id=genre['id'])
            entries.append(entry)

    return entries

# KEYWORDS -----------------------------------------------
def get_keywords(filename):

    df = pd.read_csv(filename)
    keywords = df['keywords']

    entries = []
    for kwd in keywords:
        dicts = json.loads(kwd)
        for d in dicts:
            entry = Keyword(id=d['id'], name=d['name'])
            if entry not in entries:
                entries.append(entry)

    return entries

def get_keywords_from_movie(index: int, kwd_field: str):
    dicts = json.loads(kwd_field)
    keywords = []
    for d in dicts:
        kwd = KeywordEntry(index, **d)
        keywords.append(kwd)

    return keywords

def get_movie_keywords(filename: str):

    df = pd.read_csv(filename)
    subframe = df.loc[:, ['id', 'keywords']]
    subframe_as_dict = subframe.to_dict(orient='records')
    result = []
    for row in subframe_as_dict:
        movie_id = row['id']
        keywords = row['keywords']
        all_kwords = get_keywords_from_movie(movie_id, keywords)
        movie_kwords = [to_moviekeyword(mk) for mk in all_kwords]
        result.extend(movie_kwords)

    return result

def to_moviekeyword(kwd_entry: KeywordEntry) -> MovieKeyword:
    ke = kwd_entry
    return MovieKeyword(movie_id=ke.movie_index, keyword_id=ke.id)

if __name__ == '__main__':
    df = pd.read_csv('./datas/tmdb_5000_credits.csv')
    filename = './datas/tmdb_5000_credits.csv'
    casts_ = list(df['cast'])  # list[str]

    res_actors = get_movie_actors(filename)
    res_crew = get_movie_crew(filename)
    print(type(res_actors))
    crew_ppl = get_crew_people(list(df['crew']))
    actors = get_actors_of_movie(list(df['cast']))
    print(type(crew_ppl))
    print(actors)
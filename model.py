from dataclasses import dataclass
from datetime import date


@dataclass
class CastEntry:
    #QA_IDs --> movie_index: int
    movie_id: int
    id: int  # actor
    cast_id: int
    character: str
    credit_id: str
    gender: int
    name: str
    order: int

@dataclass
class Actor:
    actor_id: int
    name: str

@dataclass
class MovieActor:
    movie_id: int
    actor_id: int  # keyword_id of the actor
    cast_id: int
    character: str
    credit_id: str
    gender: int
    orders: int

@dataclass
class CrewEntry:
    movie_index: int
    # movie_index: int
    credit_id: int
    department: str
    gender: int
    id: int
    job: str
    name: str

@dataclass
class CrewPerson:
    person_id: int
    name: str

@dataclass
class MovieCrew:
    movie_id: int
    person_id: int
    credit_id: int
    department: str
    job: str
    gender: int


@dataclass
class Movie:
    movie_id: int
    title: str
    budget: int
    popularity: float
    release_date: date
    revenue: int

@dataclass
class Language:
    lang_id: int
    lang: str

@dataclass
class MovieLanguage:
    movie_id: int
    lang_id: int

@dataclass
class CompanyEntry:
    movie_index: int
    id: int #company
    name: str

@dataclass
class Company:
    id: int
    name: str

@dataclass
class Pcompany:
    company_id: int
    name: str

@dataclass
class MovieCompany:
    movie_id: int
    company_id: int

@dataclass
class Country:
    country_id: str
    name: str

@dataclass
class CountryEntry:
    movie_index: int
    country_id: str
    name: str
@dataclass
class MovieCountry:
    movie_id: int
    country_id: str

@dataclass
class Genre:
    genre_id: int
    name: str

@dataclass
class MovieGenre:
    movie_id: int
    genre_id: int

@dataclass
class Keyword:
    keyword_id: int
    name: str

@dataclass
class KeywordEntry:
    movie_index: int
    id: int
    name: str

@dataclass
class MovieKeyword:
    movie_id: int
    keyword_id: int


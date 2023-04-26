from dataclasses import dataclass

@dataclass
class CastEntry:
    movie_id: int  # dodane... rząd w csv-ie
    id: int  # id of the actor
    cast_id: int
    character: str
    credit_id: str
    gender: int
    name: str
    order: int # !!!!!!

@dataclass
class Actor:
    actor_id: int
    name: str

@dataclass
class MovieActor:
    movie_id: int  # dodane... rząd w csv-ie
    actor_id: int  # id of the actor
    cast_id: int
    character: str
    credit_id: str
    gender: int
    orders: int

@dataclass
class CrewEntry:
    movie_index: int
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
    movie_index: int
    credit_id: int
    department: str
    gender: int
    id: int
    job: str
    name: str

@dataclass
class Movie:
    movie_id: int
    title: str



@dataclass
class Language:
    lang_id: int
    lang: str

@dataclass
class MovieLanguage:
    movie_id: int
    lang_id: int




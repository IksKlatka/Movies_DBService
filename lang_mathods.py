import json
import pandas as pd
from model import *

def get_spoken_langs():
    """all spoken languages with iso code"""
    entries = []
    for spoken in spoken_langs:
        dicts = json.loads(spoken)
        for d in dicts:
            entry = Language(lang_id=d['iso_639_1'], lang=d['name'])
            if entry not in entries:
                entries.append(entry)

    return entries

def check_if_got_all_langs():
    """all main langs to check if there r any missing in spoken_langs"""
    spoken = get_spoken_langs()
    entries = []
    for origin in origin_langs:
        if origin not in entries:
            entries.append(origin)

    lang_ids = list(map(lambda x: x.lang_id, spoken))
    missing = [entry for entry in entries if entry not in lang_ids]
    # print(missing)

    """
    missing = 'nb' (code for Norwegian Bokmål),
    therefore I count it as 'no' (code for Norwegian)
    """


if __name__ == "__main__":

    df = pd.read_csv('datas/tmdb_5000_movies.csv')
    origin_langs = df['original_language']
    spoken_langs = list(df['spoken_languages'])


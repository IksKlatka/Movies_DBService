from asyncio import run, create_task, gather, sleep
from functions import get_spoken_langs, get_movie_lang
from db_service import DbService
from model import Language, MovieLanguage

#ONLY LANGUAGES ---------------
async def create_languages():
    db = DbService()
    await db.initialize()

    langs = get_spoken_langs('../datas/tmdb_5000_movies.csv')

    for l, lang in enumerate(langs):
        await db.upsert_language(lang)
        if l%100 == 0:
            print(f'import languages in {l/ len(langs)*100:.1f}% done')

    await sleep(1)

async def add_missing_to_langs():
    db = DbService()
    await db.initialize()

    tasks =[]
    lang = Language(lang_id='nb', lang='Norwegian Bokmål')
    tasks.append(create_task(db.upsert_language(lang)))
    await gather(*tasks)
    print('done')

#MOVIE LANGUAGES ---------------
async def create_movie_languages():
    db = DbService()
    await db.initialize()

    movie_langs = get_movie_lang('../datas/tmdb_5000_movies.csv')

    for ml, mlang in enumerate(movie_langs):
        await  db.upsert_movie_language(MovieLanguage(movie_id=mlang.movie_id,
                                                      lang_id=mlang.lang_id))
        if ml%100 == 0:
            print(f'import movie languages in {ml / len(movie_langs) * 100:.1f}% done')



if __name__ == "__main__":
    run(create_languages())
    run(create_movie_languages())
    # run(add_missing_to_langs())

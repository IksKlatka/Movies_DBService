from asyncio import run, sleep
from functions import get_keywords, get_movie_keywords
from db_service import DbService

filename = 'datas/tmdb_5000_movies.csv'
async def create_keywords():

    db = DbService()
    await db.initialize()  # tu łączymy się z bazą danych

    keywords = get_keywords(filename)

    for k, kword in enumerate(keywords):
        await db.upsert_genre(kword)
        if k % 100 == 0:
            print(f'import in {k / len(keywords) * 100:.1f}% done')

    await sleep(1)

async def create_movie_keywords():
    db = DbService()
    await db.initialize()

    movie_kwords = get_movie_keywords(filename)

    for k, kword in enumerate(movie_kwords):
        await db.upsert_movie_genre(kword.keyword_id, kword.movie_id)
        if k % 100 == 0:
            print(f'import in {k / len(movie_kwords) * 100:.1f}% done')

    await sleep(1)


if __name__ == "__main__":
    run(create_keywords())

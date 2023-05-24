from asyncio import run, sleep
from functions import get_genres, get_movie_genres
from db_service import DbService

filename = '../datas/tmdb_5000_movies.csv'
async def create_genres():

    db = DbService()
    await db.initialize()  # tu łączymy się z bazą danych

    genres = get_genres(filename)

    for i, genre in enumerate(genres):
        await db.upsert_genre(genre)
        if i % 100 == 0:
            print(f'import in {i / len(genres) * 100:.1f}% done')

    await sleep(1)

async def create_movie_genres():
    db = DbService()
    await db.initialize()

    genres = get_movie_genres('../datas/tmdb_5000_movies.csv')

    for i, genre in enumerate(genres):
        await db.upsert_movie_genre(genre.genre_id, genre.movie_id)
        if i % 100 == 0:
            print(f'import in {i / len(genres) * 100:.1f}% done')

    await sleep(1)


if __name__ == "__main__":
    run(create_genres())
    run(create_movie_genres())

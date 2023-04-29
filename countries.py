from asyncio import run, sleep
from functions import get_countries, get_movie_country
from db_service import DbService
from model import Country, MovieCountry

filename = './datas/tmdb_5000_movies.csv'


#ONLY LANGUAGES ---------------
async def create_counties():
    db = DbService()
    await db.initialize()

    countries = get_countries(filename)

    for c, country in enumerate(countries):
        await db.upsert_country(country)
        if c%100 == 0:
            print(f'import countries in {c/ len(countries)*100:.1f}% done')

    await sleep(1)

#MOVIE LANGUAGES ---------------
async def create_movie_country():
    db = DbService()
    await db.initialize()

    movie_countries = get_movie_country(filename)

    for mc, mcountry in enumerate(movie_countries):
        await  db.upsert_movie_country(MovieCountry(movie_id=mcountry.movie_id,
                                                      country_id=mcountry.country_id))
        if mc%100 == 0:
            print(f'import movie_countries in {mc / len(movie_countries) * 100:.1f}% done')



if __name__ == "__main__":
    # run(create_counties())
    run(create_movie_country())

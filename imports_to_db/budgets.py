from asyncio import run, create_task, gather

from functions import *
from db_service import DbService
from model import MovieBudget


async def create_movie_budgets():
    db = DbService()
    await db.initialize()

    filename = ('../datas/tmdb_5000_movies.csv')
    movbud = get_movie_budget(filename)

    for mi, mb in enumerate(movbud):
        await db.upsert_movie_budget(MovieBudget(movie_id=mb.movie_id,
                                                 budget=mb.budget))

        if mi % 100 == 0:
            print(f'import movie budgets in {mi / len(movbud) * 100:.1f}% done')


if __name__ == '__main__':
    run(create_movie_budgets())
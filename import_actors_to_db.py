from asyncio import run, sleep
from functions import get_cast, get_actors
from db_service import DbService
from model import Actor


#ONLY ACTORS -------------------
async def create_actors():
    db = DbService()
    await db.initialize() # == establishing connection

    casts_ = get_cast()
    actors = get_actors(casts_)
    actors = [Actor(*a) for a in actors]

    for a, actor in enumerate(actors):
        await db.upsert_actor(actor)
        if a%100 == 0:
            print(f'import actors in {a/ len(actors)*100:.1f}% done')

    await sleep(1)

#MOVIE ACTORS -------------------
async def create_movie_actors():
    db = DbService()
    await db.initialize() # == establishing connection





if __name__ == "__main__":
    run(create_actors())


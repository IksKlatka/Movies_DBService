from asyncio import run
from functions import get_cast, get_actors
from db_service import DbService
from model import Actor


async def create_actors():
    db = DbService()
    await db.initialize() # == establishing connection

    casts_ = get_cast()
    actors = get_actors(casts_)
    actors = [Actor(*a) for a in actors]

    for a in actors:
        await db.upsert_actor(a)

if __name__ == "__main__":
    run(create_actors())


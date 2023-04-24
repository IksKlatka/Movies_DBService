from asyncio import run
from functions import get_crew, get_persons
from db_service import DbService
from model import CrewPerson

async def create_crew():
    db = DbService()
    await db.initialize()

    crew_ = get_crew()
    people = get_persons(crew_)
    people = [CrewPerson(*p) for p in people]

    for p in people:
        await db.upsert_person(p)

if __name__ == "__main__":
    run(create_crew())
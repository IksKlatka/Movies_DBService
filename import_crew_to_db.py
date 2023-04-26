from asyncio import run, sleep
from functions import get_crew, get_people
from db_service import DbService
from model import CrewPerson

async def create_crew():
    db = DbService()
    await db.initialize()

    crew_ = get_crew()
    people = get_people(crew_)
    people = [CrewPerson(*p) for p in people]

    for p, person in enumerate(people):
        await db.upsert_person(person)
        if p%100 == 0:
            print(f'import crew people in {p/len(people) *100:.1f}% done')

    await sleep(1)

if __name__ == "__main__":
    run(create_crew())
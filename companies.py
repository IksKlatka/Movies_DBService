from asyncio import run, sleep
from functions import get_companies
from db_service import DbService
from model import Company

# ONLY COMPANIES ----------------

async def create_companies():
    db = DbService()
    await db.initialize()

    companies = get_companies()

    for c, comp in enumerate(companies):
        await db.upsert_prod_company(comp)
        if c% 100== 0:
            print(f'import companies in {c/len(companies) *100:.1f}% done')

    await sleep(1)

# MOVIE COMPANIES -------------------
async def create_movie_companies():
    db = DbService()
    await db.initialize()


if __name__ == "__main__":
    run(create_companies())
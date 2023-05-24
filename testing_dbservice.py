from db_service import *
from asyncio import run


async def main_():
    db = DbService()
    await db.initialize()


    actor_del = await db.delete_actor(actor_id=1286878)
    print(actor_del)

if __name__ == "__main__":
    run(main_())
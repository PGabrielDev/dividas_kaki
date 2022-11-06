import  core.database as db
from src.dividas.entities import Devedor
import sqlalchemy as sa
import asyncio

async def select():
    async with await db.create_session() as session:

        select = sa.select(Devedor)
        devedores = await session.execute(select)
        print("Antes")
        for i in devedores:
            print(i)
        print("depois")

async def insert():
    async with await db.create_session() as session:
        devedor = Devedor(name="Gabriel")
        session.add(devedor)
        await session.commit()
        print("teminei de executar")
        await select()


asyncio.run(insert())



import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, dotenv_values
from src.dividas.entities import Devedor
import sqlalchemy as sa


#create engine
async def create_engine() -> AsyncEngine:

    envs = dotenv_values()
    url = f"postgresql+asyncpg://{envs['DB_USER']}:{envs['DB_PASSWORD']}@{envs['DB_HOST']}:{envs['DB_PORT']}/{envs['DB_NAME']}"
    print(url)
    engine = create_async_engine(
        url=url,
        echo=True
    )
    return engine

#create session
async def create_session() -> AsyncSession:
    async_session = sessionmaker(
     await create_engine(),
     class_= AsyncSession, 
     expire_on_commit=False
    )
    session: AsyncSession = async_session()
    return session

#Base
Base = declarative_base()


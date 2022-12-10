import asyncio

import dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from src.core.get_env import GetEnvOrDefault

#create engine
async def create_engine() -> AsyncEngine:
    envs = GetEnvOrDefault(os)
    DB_USER = envs.get_env('DB_USER')
    DB_PASSWORD = envs.get_env('DB_PASSWORD')
    DB_PORT = envs.get_env('DB_PORT')
    DB_NAME = envs.get_env('DB_NAME')
    DB_HOST = envs.get_env('DB_HOST')
    url = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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


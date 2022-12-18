
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.core.settings import settings


#create engine
async def create_engine() -> AsyncEngine:

    engine = create_async_engine(
        url=settings.DB_URL,
        echo=True
    )
    return engine

#create session
async def create_session() -> AsyncSession:
    async_session = sessionmaker(
     bind=await create_engine(),
     class_= AsyncSession,
     expire_on_commit=False,
     autocommit=False,
     autoflush=False
    )
    session: AsyncSession = async_session()
    return session



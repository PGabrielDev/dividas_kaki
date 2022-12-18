from pydantic import BaseModel



from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import  declarative_base
import os
from src.core.get_env import GetEnvOrDefault

envs = GetEnvOrDefault(os)
DB_USER = envs.get_env('DB_USER')
DB_PASSWORD = envs.get_env('DB_PASSWORD')
DB_PORT = envs.get_env('DB_PORT')
DB_NAME = envs.get_env('DB_NAME')
DB_HOST = envs.get_env('DB_HOST')
url = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Settings(BaseSettings):
    API_V1_STR: str = 'api/v1'
    DB_URL: str = url
    DBBase_model = declarative_base()
    Model = BaseModel

    JWT_SECRET: str = 'yEjQ7SFsASUIaFxc7drq7J_monHO2KoNSQKKuVspgBs'
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()
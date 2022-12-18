from typing import  Optional, List
from pydantic import EmailStr
from datetime import datetime,timedelta
from pytz import timezone
from fastapi.security import OAuth2PasswordBearer


from sqlalchemy.future import  select
from sqlalchemy.ext.asyncio import AsyncSession
from src.usuario import  entities

from jose import jwt

from src.core.settings import settings
from src.core.security import verify_password

oauth_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def auth(email: EmailStr, password: str, db:AsyncSession) -> Optional[entities.Usuario]:
    async  with db as session:
        query = select(entities.Usuario).filter(entities.Usuario.email == email)
        result = await session.execute(query)
        usuario: entities.Usuario = result.scalars().unique().one_or_none()

        if not usuario:
            return None
        if not verify_password(password, usuario.password):
            return None

        return usuario

def _create_token(type_token: str, life_time: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + life_time
    payload["type"] = type_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload,settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:
    return _create_token(
        type_token='access_token',
        life_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )



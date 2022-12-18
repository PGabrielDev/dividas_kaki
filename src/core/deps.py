from typing import Generator , Optional
from fastapi import Depends , HTTPException , status
from jose import jwt , JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.usuario import entities


from src.core.settings import settings
from src.core.database import create_session
from src.core import  auth

class TokenData(settings.Model):
    username: Optional[str] = None


async  def get_session() -> Generator:
    session: AsyncSession = await create_session()

    try:
        yield session
    finally:
        await session.close()

async def get_current_user(db: AsyncSession = Depends(get_session), token: str = Depends(auth.oauth_schema)) -> entities.Usuario:
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='not possible authenticated', headers={"WWW-Authenticate":"Bearer"})
    try:
        payload = jwt.decode(token,settings.JWT_SECRET,algorithms=[settings.ALGORITHM], options={"verify_aud":False})
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        credential_exception

    async with db as session:
        query = select(entities.Usuario).filter(entities.Usuario.id == int(token_data.username))
        result = await session.execute(query)
        usuario = result.scalars().unique().one_or_none()

        if usuario is None:
            return credential_exception

        return  usuario
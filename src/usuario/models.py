from src.core.settings import settings
from typing import Optional
from pydantic import EmailStr

class UsuarioModel(settings.Model):
    id: Optional[int]
    nome: str
    sobre_nome: str
    email: EmailStr
    class Config:
        orm_mode = True

class UsuarioModelCreate(UsuarioModel):
    senha: str
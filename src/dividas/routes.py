from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from src.dividas import models
from src.dividas import  use_cases
from src.core import  deps
from typing import List
from src.usuario.entities import Usuario
from src.usuario.models import UsuarioModel,UsuarioModelCreate
from src.core.security import generate_hash
from src.core import auth


dividas_router = APIRouter()

@dividas_router.post("/devedor", response_model=models.DevedorResponse)
async def create_devedor(
    request: models.DevedorCreateRequest,
    usuario: Usuario = Depends(deps.get_current_user)
):
    return await use_cases.CreateDevedorUseCase(request,usuario.id).execute()

@dividas_router.post("/divida", response_model=models.DividasResponse)
async def create_divida(
    request: models.DividasCreateRequest
):
    return await use_cases.CreateDividaUseCase(request).execute()


@dividas_router.get("/{id}", response_model=models.DevedorDividasResponse)
async def list_debts_by_devedor(
        id: int,
        name: models.nameQuery = Depends(models.nameQuery),
):
    return await use_cases.ListDebtsByDevedorUseCase(id,name.name).execute()

@dividas_router.get("/devedores/", response_model=List[models.DevedorResponse])
async def list_devedores(usuario: Usuario = Depends(deps.get_current_user)):
    return await use_cases.ListDevedorUseCase(usuario.id).execute()

@dividas_router.post("dividas/quitar", response_model=None, status_code=204)
async def quitar_dividas(request: List[models.DividasRequestId], usuario: Usuario = Depends(deps.get_current_user), session = Depends(deps.get_session)):
    async with session as _session:
        await use_cases.QuitarDividasUseCase(request, _session).execute()


@dividas_router.post("/signup", response_model=UsuarioModel)
async def create_user(usuario_create: UsuarioModelCreate, db = Depends(deps.get_session)):
    new_user = Usuario(
        nome=usuario_create.nome,
        sobre_nome=usuario_create.sobre_nome,
        email=usuario_create.email,
        password=generate_hash(usuario_create.senha)
    )

    async with db as session:
        session.add(new_user)
        await session.commit()

    return new_user

@dividas_router.post("/signin")
async  def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(deps.get_session)):
    user = await auth.auth(form_data.username,form_data.password,db)
    if not user:
        HTTPException(status_code=400,detail='Dados de acesso incorretos')
    return JSONResponse(content={"access_token":auth.criar_token_acesso(sub=user.id), "token_type": "bearer"}, status_code=200)
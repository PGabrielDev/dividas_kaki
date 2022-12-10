from fastapi import APIRouter, Depends
from src.dividas import models
from src.dividas import  use_cases


dividas_router = APIRouter()

@dividas_router.post("devedor", response_model=models.DevedorResponse)
async def create_devedor(
    request: models.DevedorCreateRequest
):
    return await use_cases.CreateDevedorUseCase(request).execute()

@dividas_router.post("divida", response_model=models.DividasResponse)
async def create_divida(
    request: models.DividasCreateRequest
):
    return await use_cases.CreateDividaUseCase(request).execute()


@dividas_router.get("/{id}")
async def listDebtsbyDevedor(
        id: int,
        name: models.nameQuery = Depends(models.nameQuery),
):
    return await use_cases.ListDebtsByDevedorUseCase(id,name.name).execute()
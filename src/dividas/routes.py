from fastapi import APIRouter, Depends
from src.dividas import models
from src.dividas import  use_cases
from typing import List

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


@dividas_router.get("/{id}", response_model=models.DevedorDividasResponse)
async def list_debts_by_devedor(
        id: int,
        name: models.nameQuery = Depends(models.nameQuery),
):
    return await use_cases.ListDebtsByDevedorUseCase(id,name.name).execute()

@dividas_router.get("devedores", response_model=List[models.DevedorResponse])
async def list_devedores():
    return await use_cases.ListDevedorUseCase().execute()

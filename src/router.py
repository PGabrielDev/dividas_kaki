from fastapi import APIRouter
from src.dividas.routes import  dividas_router

router = APIRouter()

router.include_router(prefix="/dividas_kaki/v1", tags=["dividas, devedor"] , router=dividas_router)

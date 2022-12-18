import datetime
from decimal import Decimal
from src.core.settings import settings
from typing import  List


class DevedorCreateRequest(settings.Model):
    name: str


class DevedorResponse(settings.Model):
    id: int
    name: str


class DividasCreateRequest(settings.Model):
    data_divida: datetime.date
    valor: Decimal
    descricao: str
    vencimento: datetime.date
    devedor_id: int


class DividasResponse(settings.Model):
    id: int
    data_divida: datetime.date
    valor: Decimal
    descricao: str
    vencimento: datetime.date
    status: bool
    devedor_id: int

class DevedorDividasResponse(settings.Model):
    devedor: DevedorResponse
    dividas: List[DividasResponse]
class nameQuery(settings.Model):
    name: str = None
import datetime
from decimal import Decimal
from src.core.settings import Model
from typing import  List


class DevedorCreateRequest(Model):
    name: str


class DevedorResponse(Model):
    id: int
    name: str


class DividasCreateRequest(Model):
    data_divida: datetime.date
    valor: Decimal
    descricao: str
    vencimento: datetime.date
    devedor_id: int


class DividasResponse(Model):
    id: int
    data_divida: datetime.date
    valor: Decimal
    descricao: str
    vencimento: datetime.date
    status: bool
    devedor_id: int

class DevedorDividasResponse(Model):
    devedor: DevedorResponse
    dividas: List[DividasResponse]
class nameQuery(Model):
    name: str = None
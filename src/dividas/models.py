import datetime
from decimal import Decimal
from src.core.settings import Model


class DevedorCreateRequest(Model):
    name: str


class DevedorResponse(Model):
    id: int
    name: str


class DividasCreateRequest(Model):
    data_divida: datetime.datetime
    valor: Decimal
    descricao: str
    vencimento: datetime.datetime
    devedor_id: int


class DividasResponse(Model):
    id: int
    data_divida: datetime.datetime
    valor: Decimal
    descricao: str
    vencimento: datetime.datetime
    status: bool
    devedor_id: int

import src.core.database as db
from src.dividas import models
from src.dividas import entities
class DividasReposiry:

    def __init__(self):
        self._session = None


    async def create_devedor(self, devedor_create: models.DevedorCreateRequest) -> models.DevedorResponse:
        if not self._session:
            self._session = await db.create_session()
        devedor = entities.Devedor(
            name=devedor_create.name
        )
        self._session.add(devedor)
        await self._session.commit()
        return models.DevedorResponse(
            id=devedor.id,
            name=devedor.name
        )
    async def create_divida(self, divida_create: models.DividasCreateRequest) -> models.DividasResponse:
        if not self._session:
            self._session = await db.create_session()
        print("teste")
        divida = entities.Divida(
            valor=divida_create.valor,
            descricao=divida_create.descricao,
            vencimento=divida_create.vencimento,
            devedor_id=divida_create.devedor_id,
            data_divida=divida_create.data_divida
        )
        self._session.add(divida)
        await self._session.commit()
        return models.DividasResponse(
            id=divida.id,
            data_divida= divida.data_divida,
            valor = divida.valor,
            descricao = divida.descricao,
            vencimento = divida.vencimento,
            status = divida.status,
            devedor_id = divida.devedor_id,
        )
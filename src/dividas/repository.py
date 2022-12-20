import src.core.database as db
from src.dividas import models
from src.dividas import entities
import sqlalchemy as sa

def create_response_devedor_divida(dict):
    devedor = models.DevedorResponse(id=dict[0]["Devedor"].id, name=dict[0]["Devedor"].name)
    debts = []
    for debt in dict:
        debt = debt["Divida"]
        debts.append(
            models.DividasResponse(
                id=debt.id,
                descricao=debt.descricao,
                status=debt.status,
                valor=debt.valor,
                vencimento=debt.vencimento,
                data_divida=debt.data_divida,
                devedor_id=debt.devedor_id,
            )
        )
        return  models.DevedorDividasResponse(
            devedor=devedor,
            dividas=debts
        )



class DividasReposiry:

    def __init__(self):
        self._session = None


    async def create_devedor(self, devedor_create: models.DevedorCreateRequest, user_id: int) -> models.DevedorResponse:
        if not self._session:
            self._session = await db.create_session()
        devedor = entities.Devedor(
            name=devedor_create.name,
            user_id=user_id
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

    async def listDebs(self, id_devedor: int, name: str= ""):
        if not self._session:
            self._session = await db.create_session()
        _select = (sa.select(
            entities.Devedor,
            entities.Divida
        ).join(
            entities.Divida,
            entities.Divida.devedor_id == entities.Devedor.id
        ).filter(
            entities.Divida.devedor_id == id_devedor
        ))
        if name:
            _select = _select.filter(
                sa.and_(
                    entities.Devedor.name.ilike(name)
                )
            )
        result = await self._session.execute(_select)
        debts = result.mappings().all()
        return create_response_devedor_divida(debts)

    async def list_devedores(self, user_id: int):
        if not self._session:
            self._session = await db.create_session()
        result = await self._session.execute(sa.select(entities.Devedor).filter(entities.Devedor.user_id == user_id))

        devedores_entity = result.mappings().all()
        devedores = []
        for devedor in devedores_entity:
            devedor = devedor["Devedor"]
            devedores.append(
                models.DevedorResponse(
                    id=devedor.id,
                    name=devedor.name
                )
            )
        return devedores
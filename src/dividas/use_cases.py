from src.dividas import  models
from src.dividas.repository import DividasReposiry

class CreateDevedorUseCase:
    def __init__(self, devedor: models.DevedorCreateRequest, user_id):
        self._devedor = devedor
        self._dividas_repository = DividasReposiry()
        self._id = user_id


    async def execute(self):
        return await self._create_devedor()


    async def _create_devedor(self):
        devedor = await self._dividas_repository.create_devedor(self._devedor,self._id)
        return  devedor

class CreateDividaUseCase:
    def __init__(self, divida: models.DividasCreateRequest):
        self._divida = divida
        self._dividas_repository = DividasReposiry()

    async def execute(self):
        return await self._create_divida()

    async def _create_divida(self):
        return await self._dividas_repository.create_divida(self._divida)



class ListDevedorUseCase:
    def __init__(self, id):
        self._id = id
        self._dividas_repository = DividasReposiry()

    async def execute(self):
        return await self._list_devedores()
    async def _list_devedores(self):
        return  await self._dividas_repository.list_devedores(self._id)


class ListDebtsByDevedorUseCase:

    def __init__(self, id_devedor: int, devedor: str = ""):
        self._devedor = devedor
        self._dividas_repository = DividasReposiry()
        self._id_devedor = id_devedor

    async def execute(self):
        return await self._list_debts()
    async def _list_debts(self):
        return  await self._dividas_repository.listDebs(self._id_devedor,self._devedor)





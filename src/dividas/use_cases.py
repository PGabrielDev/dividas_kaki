from src.dividas import  models
from src.dividas.repository import DividasReposiry

class CreateDevedorUseCase:
    def __init__(self, devedor: models.DevedorCreateRequest):
        self.devedor = devedor
        self.dividas_repository = DividasReposiry()


    async def execute(self):
        return await self._create_devedor()


    async def _create_devedor(self):
        devedor = await self.dividas_repository.create_devedor(self.devedor)
        return  devedor

class CreateDividaUseCase:
    def __init__(self, divida: models.DividasCreateRequest):
        self.divida = divida
        self.dividas_repository = DividasReposiry()

    async def execute(self):
        return await self._create_divida()

    async def _create_divida(self):
        return await self.dividas_repository.create_divida(self.divida)
from datetime import datetime
from src.core.settings import settings
import sqlalchemy as sa



class Devedor(settings.DBBase_model):
    __tablename__: str = "devedor"
    id = sa.Column(sa.BigInteger, primary_key= True)
    name = sa.Column(sa.TEXT, nullable=False)
    user_id = sa.Column(sa.Integer,sa.ForeignKey('usuario.id'))

    def __repr__(self):
        return f"nome:{self.name}"



class Divida(settings.DBBase_model):
    __tablename__: str = "divida"
    id = sa.Column(sa.BigInteger, primary_key= True)
    data_divida = sa.Column(sa.Date)
    valor = sa.Column(sa.DECIMAL(8,2), nullable=False)
    descricao = sa.Column(sa.TEXT, nullable=False)
    vencimento = sa.Column(sa.Date)
    status = sa.Column(sa.Boolean, default=lambda _: False)
    devedor_id = sa.Column(sa.Integer, sa.ForeignKey('devedor.id'))






    
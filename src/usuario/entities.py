from src.core.settings import settings
import  sqlalchemy as sa


class Usuario(settings.DBBase_model):
    __tablename__ = 'usuario'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.TEXT, nullable=False)
    sobre_nome = sa.Column(sa.TEXT, nullable=False)
    email = sa.Column(sa.TEXT, nullable=False, index=True, unique=True)
    password = sa.Column(sa.TEXT, nullable=False)



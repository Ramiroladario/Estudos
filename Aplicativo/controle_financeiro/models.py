from sqlmodel import Field, SQLModel, create_engine, Relationship
from enum import Enum
from datetime import date

class Bancos(Enum):
    BANCO_DO_BRASIL = 'Banco do Brasil'
    CAIXA_ECONOMICA = 'Caixa Econômica Federal'
    ITAU = 'Itaú'
    SANTANDER = 'Santander'
    INTER = 'Inter'
    BRADESCO = 'Bradesco'
    BRB = 'Brb'

class Status(Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'

class Tipos(Enum):
    Entrada = 'Entrada'
    Saida = 'Saida'

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    banco: Bancos = Field(default=Bancos.BANCO_DO_BRASIL)
    status: Status = Field(default=Status.ATIVO)
    valor: float

class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    id_conta: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.Entrada)
    valor: float
    data: date

sqlite_file_name = 'database.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
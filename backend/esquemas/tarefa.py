from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class TarefaEntrada(BaseModel):
    titulo: str = Field(max_length=100)
    descricao: str = Field(max_length=500)
    prazo: date
    situacao: str = Field(max_length=20)
    itens_feitos: int
    solicitante_id: int


class TarefaSaida(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    descricao: str
    prazo: date
    situacao: str
    itens_feitos: int
    solicitante_id: int

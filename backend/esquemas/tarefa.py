from datetime import date

from pydantic import BaseModel, ConfigDict


class TarefaSaida(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    descricao: str
    prazo: date
    situacao: str
    itens_feitos: int
    solicitante_id: int

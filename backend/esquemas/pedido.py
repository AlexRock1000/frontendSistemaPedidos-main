from pydantic import BaseModel


class PedidoSaida(BaseModel):
    id: int
    cliente: str
    status: str
    total: float

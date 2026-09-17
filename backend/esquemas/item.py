from pydantic import BaseModel


class ItemSaida(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ItemPedidoEntrada(BaseModel):
    produtoId: int = Field(gt=0)
    quantidade: int = Field(gt=0, le=99)


class ItemPedidoSaida(ItemPedidoEntrada):
    nome: str
    precoUnitario: float


class PedidoEntrada(BaseModel):
    cliente: str = Field(min_length=2, max_length=80)
    tipo: Literal["local", "viagem"]
    observacao: str = Field(default="", max_length=140)
    itens: list[ItemPedidoEntrada] = Field(min_length=1)


class PedidoSaida(BaseModel):
    id: int
    numero: int
    cliente: str
    tipo: Literal["local", "viagem"]
    observacao: str
    itens: list[ItemPedidoSaida]
    criadoEm: datetime
    atualizadoEm: datetime
    status: str
    total: float

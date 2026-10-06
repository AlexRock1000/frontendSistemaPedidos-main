from fastapi import APIRouter, status

from esquemas.pedido import PedidoEntrada, PedidoSaida
from servicos import pedido as servico_pedido

router = APIRouter()


@router.get("/", response_model=list[PedidoSaida])
def listar_pedidos():
	return servico_pedido.listar_pedidos()


@router.post("/", response_model=PedidoSaida, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoEntrada):
	return servico_pedido.criar_pedido(pedido)


@router.get("/status")
def listar_status():
	return servico_pedido.listar_status()


@router.patch("/{pedido_id}", response_model=PedidoSaida)
def atualizar_status(pedido_id: int, dados: dict):
	return servico_pedido.atualizar_status(pedido_id, dados)

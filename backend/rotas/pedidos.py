from fastapi import APIRouter, HTTPException, status

from esquemas.pedido import PedidoEntrada, PedidoSaida
from servicos import pedido as servico_pedido

router = APIRouter()


@router.get("/", response_model=list[PedidoSaida])
def listar_pedidos():
	return servico_pedido.listar_pedidos()


@router.post("/", response_model=PedidoSaida, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoEntrada):
	novo_pedido = servico_pedido.criar_pedido(pedido)
	if novo_pedido is None:
		raise HTTPException(status_code=404, detail="Produto não encontrado")
	return novo_pedido


@router.get("/status")
def listar_status():
	return servico_pedido.listar_status()


@router.patch("/{pedido_id}", response_model=PedidoSaida)
def atualizar_status(pedido_id: int, dados: dict):
	resultado = servico_pedido.atualizar_status(pedido_id, dados)
	if resultado is None:
		raise HTTPException(status_code=404, detail="Pedido não encontrado")
	if resultado is False:
		raise HTTPException(status_code=422, detail="Status inválido")
	return resultado

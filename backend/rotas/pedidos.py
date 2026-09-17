from fastapi import APIRouter
from esquemas.pedido import PedidoSaida

router = APIRouter()

pedidos = [
	{
		"id": 1,
		"cliente": "Marina",
		"status": "recebido",
		"total": 78.70,
	},
	{
		"id": 2,
		"cliente": "Carlos",
		"status": "entregue",
		"total": 67.80,
	},
]


@router.get("/", response_model=list[PedidoSaida])
def listar_pedidos():
	return pedidos

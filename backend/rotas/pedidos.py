from fastapi import APIRouter

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


@router.get("/")
def listar_pedidos():
	return pedidos

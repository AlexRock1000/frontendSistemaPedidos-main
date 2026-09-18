from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

from esquemas.pedido import PedidoEntrada, PedidoSaida

router = APIRouter()

pedidos = [
	{
		"id": 1,
		"numero": 101,
		"cliente": "Marina",
		"tipo": "local",
		"observacao": "",
		"itens": [],
		"status": "recebido",
		"total": 78.70,
		"criadoEm": "2026-09-10T21:05:00Z",
		"atualizadoEm": "2026-09-10T21:05:00Z",
	},
	{
		"id": 2,
		"numero": 102,
		"cliente": "Carlos",
		"tipo": "viagem",
		"observacao": "",
		"itens": [],
		"status": "entregue",
		"total": 67.80,
		"criadoEm": "2026-09-10T21:12:00Z",
		"atualizadoEm": "2026-09-10T21:12:00Z",
	},
]

cardapio = [
	{"id": 1, "nome": "Pizza Marguerita", "preco": 39.90},
	{"id": 2, "nome": "Suco de Laranja", "preco": 12.50},
]


@router.get("/", response_model=list[PedidoSaida])
def listar_pedidos():
	return sorted(pedidos, key=lambda pedido: pedido["criadoEm"], reverse=True)


@router.post("/", response_model=PedidoSaida, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoEntrada):
	itens_pedido = []
	for item in pedido.itens:
		produto = next((produto for produto in cardapio if produto["id"] == item.produtoId), None)
		if produto is None:
			raise HTTPException(status_code=404, detail="Produto não encontrado")
		itens_pedido.append({
			"produtoId": produto["id"],
			"nome": produto["nome"],
			"precoUnitario": produto["preco"],
			"quantidade": item.quantidade,
		})

	agora = datetime.now(timezone.utc).isoformat()
	novo_pedido = {
		"id": max((pedido["id"] for pedido in pedidos), default=0) + 1,
		"numero": max((pedido["numero"] for pedido in pedidos), default=100) + 1,
		"cliente": pedido.cliente.strip(),
		"tipo": pedido.tipo,
		"observacao": pedido.observacao.strip(),
		"itens": itens_pedido,
		"status": "recebido",
		"total": round(sum(item["precoUnitario"] * item["quantidade"] for item in itens_pedido), 2),
		"criadoEm": agora,
		"atualizadoEm": agora,
	}
	pedidos.append(novo_pedido)
	return novo_pedido


@router.get("/status")
def listar_status():
	return [
		{"id": "recebido", "nome": "Recebido", "finalizado": False},
		{"id": "entregue", "nome": "Entregue", "finalizado": True},
	]


@router.patch("/{pedido_id}", response_model=PedidoSaida)
def atualizar_status(pedido_id: int, dados: dict):
	pedido = next((pedido for pedido in pedidos if pedido["id"] == pedido_id), None)
	if pedido is None:
		raise HTTPException(status_code=404, detail="Pedido não encontrado")
	if dados.get("status") not in {"recebido", "entregue"}:
		raise HTTPException(status_code=422, detail="Status inválido")
	pedido["status"] = dados["status"]
	pedido["atualizadoEm"] = datetime.now(timezone.utc).isoformat()
	return pedido

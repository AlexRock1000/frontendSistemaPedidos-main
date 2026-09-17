from fastapi import APIRouter, HTTPException
from esquemas.item import ItemSaida

router = APIRouter()

cardapio = [
	{"id": 1, "nome": "Pizza Marguerita", "preco": 39.90, "categoria": "prato"},
	{"id": 2, "nome": "Suco de Laranja", "preco": 12.50, "categoria": "bebida"},
]


@router.get("/", response_model=list[ItemSaida])
def listar_itens(categoria: str | None = None):
	if categoria is None:
		return cardapio
	return [item for item in cardapio if item["categoria"] == categoria]


@router.get("/{item_id}", response_model=ItemSaida)
def obter_item(item_id: int):
	for item in cardapio:
		if item["id"] == item_id:
			return item
	raise HTTPException(status_code=404, detail="Item não encontrado")

from fastapi import APIRouter, HTTPException
from esquemas.item import ItemSaida
from servicos import item as servico_item

router = APIRouter()


@router.get("/", response_model=list[ItemSaida])
def listar_itens(categoria: str | None = None):
	return servico_item.listar_itens(categoria)


@router.get("/{item_id}", response_model=ItemSaida)
def obter_item(item_id: int):
	item = servico_item.obter_item(item_id)
	if item is not None:
		return item
	raise HTTPException(status_code=404, detail="Item não encontrado")

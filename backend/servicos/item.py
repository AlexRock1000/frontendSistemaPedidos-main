from repositorios import item as repositorio_item
from servicos.excecoes import ItemNaoEncontrado


def listar_itens(categoria: str | None = None):
    itens = repositorio_item.listar_itens()
    if categoria is None:
        return itens
    return [item for item in itens if item["categoria"] == categoria]


def obter_item(item_id: int):
    return repositorio_item.obter_item(item_id)


def validar_item(item_id: int):
    item = repositorio_item.obter_item(item_id)
    if item is None:
        raise ItemNaoEncontrado()
    return item
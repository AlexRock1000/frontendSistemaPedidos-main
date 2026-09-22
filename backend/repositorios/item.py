cardapio = [
    {"id": 1, "nome": "Pizza Marguerita", "preco": 39.90, "categoria": "prato"},
    {"id": 2, "nome": "Suco de Laranja", "preco": 12.50, "categoria": "bebida"},
]


def listar_itens():
    return cardapio


def obter_item(item_id: int):
    for item in cardapio:
        if item["id"] == item_id:
            return item
    return None
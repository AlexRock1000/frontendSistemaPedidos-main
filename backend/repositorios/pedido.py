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


def listar_pedidos():
    return pedidos


def obter_pedido(pedido_id: int):
    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            return pedido
    return None


def adicionar_pedido(pedido):
    pedidos.append(pedido)


def atualizar_pedido(pedido):
    return pedido


def listar_status():
    return [
        {"id": "recebido", "nome": "Recebido", "finalizado": False},
        {"id": "entregue", "nome": "Entregue", "finalizado": True},
    ]
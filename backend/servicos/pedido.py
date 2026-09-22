from datetime import datetime, timezone

from esquemas.pedido import PedidoEntrada
from repositorios import item as repositorio_item
from repositorios import pedido as repositorio_pedido


def listar_pedidos():
    pedidos = repositorio_pedido.listar_pedidos()
    return sorted(pedidos, key=lambda pedido: pedido["criadoEm"], reverse=True)


def criar_pedido(pedido: PedidoEntrada):
    itens_pedido = []
    for item in pedido.itens:
        produto = repositorio_item.obter_item(item.produtoId)
        if produto is None:
            return None
        itens_pedido.append({
            "produtoId": produto["id"],
            "nome": produto["nome"],
            "precoUnitario": produto["preco"],
            "quantidade": item.quantidade,
        })

    agora = datetime.now(timezone.utc).isoformat()
    pedidos = repositorio_pedido.listar_pedidos()
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
    repositorio_pedido.adicionar_pedido(novo_pedido)
    return novo_pedido


def listar_status():
    return repositorio_pedido.listar_status()


def atualizar_status(pedido_id: int, dados: dict):
    pedido = repositorio_pedido.obter_pedido(pedido_id)
    if pedido is None:
        return None
    if dados.get("status") not in {"recebido", "entregue"}:
        return False
    pedido["status"] = dados["status"]
    pedido["atualizadoEm"] = datetime.now(timezone.utc).isoformat()
    repositorio_pedido.atualizar_pedido(pedido)
    return pedido
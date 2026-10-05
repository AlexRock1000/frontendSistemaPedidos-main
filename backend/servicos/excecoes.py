class ErroDeRegra(Exception):
    status_code = 400
    mensagem = "Operação não permitida"

    def __init__(self, mensagem: str | None = None):
        super().__init__(mensagem or self.mensagem)


class ItemNaoEncontrado(ErroDeRegra):
    status_code = 404
    mensagem = "Item não encontrado"


class TarefaNaoEncontrada(ErroDeRegra):
    status_code = 404
    mensagem = "Tarefa não encontrada"


class PedidoNaoEncontrado(ErroDeRegra):
    status_code = 404
    mensagem = "Pedido não encontrado"


class StatusPedidoInvalido(ErroDeRegra):
    status_code = 422
    mensagem = "Status inválido"